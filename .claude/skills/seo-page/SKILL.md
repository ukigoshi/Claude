---
name: seo-page
description: Research, write and create an SEO-optimized WordPress page or blog post as a draft. Use when the user asks for a page, post, article, landing page, or blog content for one of the sites.
---

# SEO page

Input: site slug + topic or keyword. Read `sites/<slug>/site.yml` and `docs/seo-standards.md`.

1. **Pick the keyword.** Check `seo.keyword_map` so it isn't already targeted (cannibalization).
   Add the new row with `status: planned`.
2. **Research intent.** Look at the current top results (WebSearch) — format, length,
   subtopics, "People also ask". Note what's missing that we can add.
3. **Brief.** Copy `sites/_template/content/_brief-template.md` to
   `sites/<slug>/content/<slug>.md`, fill meta title/description, outline, schema, links.
4. **Write.** Use the `seo-article-writer` skill if available. Brand voice from `site.yml`.
   Answer intent in the first 100 words, include FAQ, cite sources, add internal links.
   Follow the copy rules in `docs/design-taste.md` (no filler verbs like "elevate", no em-dashes, sentence-case headings).
   Write the body into the same markdown file below the brief.
5. **Images.** Run `/site-media` for the hero and any inline images.
6. **Self-audit** against the page-level checklist (or `seo-article-audit`). Fix issues.
7. **Create in WordPress as draft** with wordpress-mcp (`wp-content`): content, slug,
   categories, featured image, Rank Math title/description/focus keyword, schema.
   Save the returned id as `wp_id`, set `status: draft`, and give the user the preview link.
8. Publish only after the user approves. Then update `keyword_map` status and CHANGELOG.
