# SEO WordPress Studio

A Claude Code workflow for building and maintaining SEO-friendly WordPress sites
on Hostinger, with AI-generated media from Higgsfield.

## One-time setup

1. **Plugins (claude.ai → Customize → Plugins)** — enable:
   - *Hostinger Connector*: hosting, domains, DNS, SSL, WordPress installs, backups (sign in with OAuth)
   - *wordpress-mcp*: edit posts/pages/media inside WordPress
   - *Fully SEO optimized Article with FAQ's*, *WordPress Dev Skills*, *AEOTester* (optional)
2. **Higgsfield** — already configured in `.mcp.json` for Claude Code
   (`https://mcp.higgsfield.ai/mcp`, OAuth on first use). On claude.ai, add it as a
   custom connector with the same URL.
3. **On each WordPress site** — install the *WordPress MCP Adapter* plugin and create an
   Application Password (Users → Profile). Store it as an env var / GitHub secret
   (`WP_<SLUG>_USER`, `WP_<SLUG>_APP_PASSWORD`), never in the repo.
4. **Optional SEO data** — connect Semrush, Ahrefs or Ubersuggest for real keyword volumes.

## Daily use (ask Claude in this repo)

| Command | What it does |
|---|---|
| `/new-site` | Brief → keyword map → Hostinger WordPress install → base SEO setup |
| `/seo-page` | Keyword research → brief → article → images → WordPress **draft** |
| `/site-media` | Higgsfield images/video → WebP, alt text → WordPress media library |
| `/site-maintenance` | Backups, updates, security, technical audit, content refresh |

## Layout

```
CLAUDE.md                 rules + tool map Claude follows
.claude/skills/           the four workflow skills
.mcp.json                 Higgsfield MCP server
docs/seo-standards.md     site- and page-level SEO checklist
sites/_template/          copy to sites/<slug>/ for each site
scripts/seo_audit.py      technical SEO audit (URLs or sitemaps)
.github/workflows/        weekly audit of every site in sites/
```

## Audit a site manually

```bash
python3 scripts/seo_audit.py https://example.com/sitemap_index.xml --limit 50
```
