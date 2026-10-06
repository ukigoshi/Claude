#!/usr/bin/env python3
"""Technical on-page SEO audit for live pages.

Usage:
  python3 scripts/seo_audit.py https://example.com/
  python3 scripts/seo_audit.py https://example.com/sitemap_index.xml --limit 50
  python3 scripts/seo_audit.py URL [URL ...] --json

Accepts page URLs or XML sitemaps (sitemap indexes are followed).
Exit code 1 if any page has errors. Standard library only.
"""
import argparse
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

UA = "Mozilla/5.0 (compatible; SEOStudioAudit/1.0)"
SM_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.geturl(), r.headers, r.read()


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._in = None
        self.meta = {}
        self.canonical = None
        self.h1 = []
        self.imgs_no_alt = []
        self.img_count = 0
        self.jsonld = []
        self.lang = None
        self.links = []
        self._buf = ""

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._in, self._buf = "title", ""
        elif tag == "h1":
            self._in, self._buf = "h1", ""
        elif tag == "script" and a.get("type", "").lower() == "application/ld+json":
            self._in, self._buf = "jsonld", ""
        elif tag == "meta":
            key = (a.get("name") or a.get("property") or "").lower()
            if key:
                self.meta[key] = a.get("content", "")
        elif tag == "link" and "canonical" in a.get("rel", "").lower().split():
            self.canonical = a.get("href")
        elif tag == "img":
            self.img_count += 1
            if not a.get("alt", "").strip() and a.get("role") != "presentation":
                self.imgs_no_alt.append(a.get("src") or a.get("data-src") or "?")
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])

    def handle_data(self, data):
        if self._in:
            self._buf += data

    def handle_endtag(self, tag):
        if self._in == "title" and tag == "title":
            self.title = self._buf.strip()
        elif self._in == "h1" and tag == "h1":
            self.h1.append(" ".join(self._buf.split()))
        elif self._in == "jsonld" and tag == "script":
            self.jsonld.append(self._buf)
        else:
            return
        self._in = None


def schema_types(blocks):
    types = set()

    def walk(node):
        if isinstance(node, dict):
            t = node.get("@type")
            if isinstance(t, str):
                types.add(t)
            elif isinstance(t, list):
                types.update(x for x in t if isinstance(x, str))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    bad = 0
    for b in blocks:
        try:
            walk(json.loads(b))
        except ValueError:
            bad += 1
    return sorted(types), bad


def audit_page(url):
    res = {"url": url, "errors": [], "warnings": [], "info": {}}
    E, W = res["errors"].append, res["warnings"].append
    try:
        status, final, headers, body = fetch(url)
    except Exception as e:  # noqa: BLE001
        E(f"fetch failed: {e}")
        return res
    if final.rstrip("/") != url.rstrip("/"):
        W(f"redirects to {final}")
    if urlparse(final).scheme != "https":
        E("not served over HTTPS")
    xrobots = headers.get("X-Robots-Tag", "")
    if "noindex" in xrobots.lower():
        E("X-Robots-Tag: noindex")

    p = PageParser()
    p.feed(body.decode("utf-8", errors="replace"))
    n = len(p.title)
    if not p.title:
        E("missing <title>")
    elif not 30 <= n <= 60:
        W(f"title length {n} (aim 30-60): {p.title!r}")
    desc = p.meta.get("description", "")
    if not desc:
        E("missing meta description")
    elif not 70 <= len(desc) <= 160:
        W(f"meta description length {len(desc)} (aim 70-160)")
    robots = p.meta.get("robots", "").lower()
    if "noindex" in robots:
        E("meta robots noindex")
    if len(p.h1) == 0:
        E("no <h1>")
    elif len(p.h1) > 1:
        W(f"{len(p.h1)} <h1> tags")
    if not p.canonical:
        W("no canonical link")
    elif urljoin(final, p.canonical).rstrip("/") != final.rstrip("/"):
        W(f"canonical points elsewhere: {p.canonical}")
    if not p.lang:
        W("<html> missing lang attribute")
    if "viewport" not in p.meta:
        E("missing viewport meta (mobile)")
    if p.imgs_no_alt:
        W(f"{len(p.imgs_no_alt)}/{p.img_count} images missing alt: {p.imgs_no_alt[:3]}")
    for og in ("og:title", "og:description", "og:image"):
        if og not in p.meta:
            W(f"missing {og}")
    types, bad = schema_types(p.jsonld)
    if bad:
        E(f"{bad} invalid JSON-LD block(s)")
    if not types:
        W("no JSON-LD structured data")
    host = urlparse(final).netloc
    internal = [l for l in p.links if urlparse(urljoin(final, l)).netloc == host]
    if len(internal) < 3:
        W(f"only {len(internal)} internal links")
    res["info"] = {
        "status": status, "title": p.title, "h1": p.h1[:1], "schema": types,
        "internal_links": len(internal), "images": p.img_count,
        "kb": round(len(body) / 1024),
    }
    return res


def expand(target, limit):
    if not target.endswith(".xml"):
        return [target]
    _, _, _, body = fetch(target)
    root = ET.fromstring(body)
    urls = []
    if root.tag == SM_NS + "sitemapindex":
        for loc in root.iter(SM_NS + "loc"):
            urls += expand(loc.text.strip(), limit - len(urls))
            if len(urls) >= limit:
                break
    else:
        urls = [loc.text.strip() for loc in root.iter(SM_NS + "loc")]
    return urls[:limit]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("targets", nargs="+", help="page URLs or sitemap .xml URLs")
    ap.add_argument("--limit", type=int, default=100, help="max pages per sitemap")
    ap.add_argument("--json", action="store_true", help="print JSON report")
    args = ap.parse_args()

    urls = []
    for t in args.targets:
        try:
            urls += expand(t, args.limit)
        except Exception as e:  # noqa: BLE001
            print(f"could not read {t}: {e}", file=sys.stderr)
    results = [audit_page(u) for u in dict.fromkeys(urls)]

    titles = {}
    for r in results:
        t = r["info"].get("title")
        if t:
            titles.setdefault(t, []).append(r["url"])
    for t, us in titles.items():
        if len(us) > 1:
            for r in results:
                if r["url"] in us:
                    r["warnings"].append(f"duplicate title shared with {len(us) - 1} other page(s)")

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            mark = "FAIL" if r["errors"] else ("WARN" if r["warnings"] else "OK  ")
            print(f"[{mark}] {r['url']}")
            for e in r["errors"]:
                print(f"    error: {e}")
            for w in r["warnings"]:
                print(f"    warn:  {w}")
        ne = sum(bool(r["errors"]) for r in results)
        print(f"\n{len(results)} pages, {ne} with errors, "
              f"{sum(bool(r['warnings']) for r in results)} with warnings")
    sys.exit(1 if any(r["errors"] for r in results) else 0)


if __name__ == "__main__":
    main()
