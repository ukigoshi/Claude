---
name: site-maintenance
description: Monthly maintenance and SEO health check for a WordPress site on Hostinger - backups, updates, security, speed, technical SEO audit, and content refresh. Use when the user asks to maintain, update, check, or audit a site.
---

# Site maintenance

Run for one site (`sites/<slug>/`) or all sites. Report findings before changing anything.

1. **Backup.** Confirm a fresh Hostinger backup exists (Hostinger `maintain-wordpress` /
   `audit-hosting`); create one if not.
2. **Updates (confirm first).** WordPress core, plugins, theme — one at a time, checking
   the site loads after each. Remove unused plugins/themes.
3. **Hosting health.** SSL validity, PHP version (latest supported), disk/inode usage,
   uptime, malware scan (Hostinger `audit-hosting`, `troubleshoot-website`).
4. **Technical SEO.** `python3 scripts/seo_audit.py <sitemap-url> --json` and fix
   errors first, then warnings. Also check Search Console coverage/Core Web Vitals if
   the user can share them.
5. **Content.** Find pages with `status: published` older than 6–12 months or losing
   traffic; refresh facts, dates, internal links, and FAQ via `/seo-page` (refresh mode).
   Add 1–2 new posts from the keyword map backlog.
6. **Design (optional, quarterly).** Run `redesign-existing-projects` as an audit only;
   propose fixes in its priority order, apply only with user approval.
7. **Report.** Append a dated entry to `sites/<slug>/CHANGELOG.md`: what was checked,
   what changed, open issues. Commit.
