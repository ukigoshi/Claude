# SEO WordPress Studio

This repo is the control center for building and maintaining SEO-friendly
WordPress sites hosted on Hostinger. Each site lives in `sites/<slug>/`.

## Tools and what each one is for

| Need | Tool |
|---|---|
| Hosting, domains, DNS, SSL, WordPress installs, backups | **Hostinger** plugin/MCP (`maintain-wordpress`, `deploy-to-hosting`, `connect-domain`, `audit-hosting`, `hostinger:hosting-deploy-wordpress-*`) |
| Posts, pages, products, media inside WordPress | **WordPress REST API** (`/wp-json/wp/v2/`, WooCommerce `/wp-json/wc/v3/`) with Basic auth from env `WP_<SLUG>_USER` + `WP_<SLUG>_APP_PASSWORD` (an Application Password); needs the site's domain allowed in the environment's network access. Or **wordpress-mcp** (`wp-content`, `wp-admin`) if the site has the WordPress MCP Adapter plugin |
| Hero images, product shots, short videos | **Higgsfield** MCP (`.mcp.json`, `https://mcp.higgsfield.ai/mcp`, OAuth) |
| Article writing and on-page audits | `seo-article-writer` / `seo-article-audit`, plus `docs/seo-standards.md` |
| Schema / JSON-LD | `wp-structured-data` |
| Visual design quality ("taste") | `/taste-skill`, `/redesign-skill`, `/minimalist-skill`, `/soft-skill` in `.claude/skills/` — read `docs/design-taste.md` for the WordPress adaptation |
| Technical audit of a live site | `python3 scripts/seo_audit.py <url-or-sitemap>` |
| Code, history, scheduled audits | This GitHub repo + `.github/workflows/seo-audit.yml` |

If a tool above is not available in the session, say so and fall back to the
next best option (e.g. Hostinger hPanel steps for the user to click through).

## Workflow (project skills in `.claude/skills/`)

1. `/new-site` — brief → `sites/<slug>/site.yml` → Hostinger WordPress install → base SEO setup.
2. `/seo-page` — keyword → outline → draft → images → publish as **draft** in WordPress.
3. `/site-media` — generate and optimize images/video with Higgsfield.
4. `/site-maintenance` — monthly: updates, backups, audit, content refresh.

## Rules

- Never publish, delete content, change DNS, or run updates on a live site
  without the user confirming first. Create WordPress content as `draft`.
- Take (or confirm) a Hostinger backup before plugin/theme/core updates.
- Never commit or print secrets. Credentials go in the cloud environment's settings /
  GitHub secrets (`WP_<SLUG>_USER`, `WP_<SLUG>_APP_PASSWORD`), never in `site.yml` or
  the chat. Read them only from the environment.
- Follow `docs/seo-standards.md` for every page. Apply design taste per
  `docs/design-taste.md`; when taste and SEO/speed conflict, SEO wins.
- Record what changed on each site in `sites/<slug>/CHANGELOG.md`.
