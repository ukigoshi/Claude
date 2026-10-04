# SEO standards (apply to every site and page)

## Site-level (set once in `/new-site`, re-check in `/site-maintenance`)
- HTTPS forced, one canonical host (www or non-www), 301 the other.
- Permalinks: `/%postname%/`.
- SEO plugin: **Rank Math** (or Yoast) — XML sitemap on, submitted to Google Search Console and Bing Webmaster Tools.
- `robots.txt` allows crawling and lists the sitemap; "Discourage search engines" is OFF.
- Caching: **LiteSpeed Cache** (Hostinger runs LiteSpeed) with page cache, CSS/JS minify, lazy-load images, WebP conversion.
- Lightweight theme (Astra, GeneratePress, Kadence or a block theme). Avoid page-builder bloat.
- Core Web Vitals targets (mobile): LCP < 2.5s, INP < 200ms, CLS < 0.1.
- Organization / LocalBusiness schema with name, logo, sameAs, contact.
- `llms.txt` at the root summarizing the site for AI search engines.
- Analytics: GA4 + Search Console linked.

## Page-level
- **One primary keyword** per page; no two pages target the same keyword.
- `<title>` 30–60 chars, keyword near the start, brand at the end.
- Meta description 70–160 chars, a reason to click.
- Exactly one `<h1>`; logical H2/H3 hierarchy.
- Slug: short, lowercase, hyphenated, contains the keyword.
- First 100 words answer the search intent directly.
- At least 3 internal links in, 2–5 out to related pages; 1–2 authoritative external links.
- Every image: descriptive filename, `alt` text, WebP, width/height set, < 200 KB (hero < 300 KB).
- Schema matched to page type: Article/BlogPosting, Product, Service, FAQPage, LocalBusiness, BreadcrumbList.
- FAQ section for informational pages (real questions from "People also ask").
- Canonical tag points to itself unless intentionally consolidated.
- E-E-A-T: author box, updated date, sources cited.
