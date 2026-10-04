---
name: site-media
description: Generate on-brand, SEO-optimized images or short videos for a site with Higgsfield, then prepare them for WordPress. Use for hero images, featured images, product shots, banners, or background videos.
---

# Site media (Higgsfield)

1. Read `brand.image_style` and `brand.colors` from `sites/<slug>/site.yml`.
2. Write the prompt: subject + setting + style + lighting + composition, and leave
   negative space where text will overlay. No text inside images, no real people's
   likenesses or logos you don't own.
3. Generate with the Higgsfield MCP (`generate_image`, or `generate_video` for short
   loops). Aspect ratios: hero 16:9, featured image 1200x630 (also the OG image),
   product 1:1, mobile/social 9:16. Poll `get_generation_status` until done.
   For a recurring mascot/person, use `create_character` once and reuse it.
4. Show the user the options; download the chosen one.
5. Optimize: convert to WebP, resize (hero max 1920px wide, inline 1200px), target
   < 200 KB (hero < 300 KB). E.g. `cwebp -q 80 -resize 1920 0 in.png -o out.webp`.
6. SEO metadata: descriptive hyphenated filename with the keyword
   (`emergency-plumber-austin.webp`), alt text describing the image in context,
   title and caption if helpful.
7. Upload with wordpress-mcp (`wp-content` media) and set it on the draft. Videos:
   keep them short and muted, add a poster image, never let them be the LCP element.
