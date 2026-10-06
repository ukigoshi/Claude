---
name: new-site
description: Launch a new SEO-ready WordPress site on Hostinger - brief, keyword map, install, base SEO configuration. Use when the user wants to create/start/launch a new website.
---

# New site

1. **Brief.** Ask only for what's missing: business name, domain, location/audience,
   services or products, 3 competitors, brand voice/colors. Copy `sites/_template/`
   to `sites/<slug>/` and fill `site.yml`.
2. **Keyword map.** Build the site structure from search intent: home, one page per
   service/product category, about, contact, and 5–10 starter blog topics. One primary
   keyword per URL in `seo.keyword_map`. Use an SEO data connector (Semrush, Ahrefs,
   Ubersuggest) if one is connected; otherwise mark volumes as "unverified".
3. **Hosting (confirm with user first).** With the Hostinger tools: check the domain
   (`connect-domain`), create the WordPress site (`hostinger:hosting-deploy-wordpress-site`),
   make sure SSL is active. Store the website id in `site.yml`.
4. **Base SEO setup** per `docs/seo-standards.md` "Site-level": permalinks, theme,
   Rank Math, LiteSpeed Cache, sitemap, robots, Organization/LocalBusiness schema,
   llms.txt. Use the WordPress REST API or wordpress-mcp (see CLAUDE.md); otherwise
   give the user a short hPanel / wp-admin checklist.
5. **Design.** Pick the look with `/taste-skill` plus one preset
   (`/minimalist-skill` or `/soft-skill`) from `brand` in `site.yml`, applied through
   `theme.json`, block patterns and Additional CSS per `docs/design-taste.md`.
6. **Core pages** as drafts via `/seo-page`, hero images via `/site-media`.
7. **Verify:** `python3 scripts/seo_audit.py https://<domain>/sitemap_index.xml`.
   Fix errors, then remind the user to submit the sitemap in Search Console.
8. Start `sites/<slug>/CHANGELOG.md` and commit.
