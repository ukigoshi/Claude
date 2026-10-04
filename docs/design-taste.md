# Design taste on WordPress

The taste skills in `.claude/skills/` (from taste-skill) assume a React/Next.js + Tailwind
stack. Our sites are WordPress, so apply the **rules**, not the stack.

## How to apply them
| Taste rule | WordPress implementation |
|---|---|
| Fonts (no Inter/Roboto by default; Geist, Satoshi, Outfit...) | Self-host via the theme's `theme.json` `fontFamilies` (or Appearance > Editor > Styles > Typography). No Google Fonts `<link>` |
| One accent color, one gray family, no pure #000/#fff | `theme.json` color palette; remove unused default palette colors |
| One corner-radius scale | `theme.json` / block styles; set button, image and group radii once |
| Spacing / whitespace | `theme.json` `spacing.spacingSizes` and block-gap; generous section padding |
| Layouts (no 3 equal cards, no repeated section layout) | Build as block patterns (Columns, Group, Cover) with varied compositions |
| Hover/active/focus states, motion | Additional CSS (Appearance > Customize, or a child theme `style.css`); `transform`/`opacity` only, wrapped in `prefers-reduced-motion` |
| Real images, not placeholders | Generate with `/site-media` (Higgsfield), never picsum in production |
| Copy rules (no "Elevate/Seamless", no em-dashes, sentence case) | Apply to every page/post written via `/seo-page` |

Skip what doesn't translate: Motion/GSAP React components, `next/font`, shadcn, Server Components.
Prefer a block theme (Twenty Twenty-Five, Ollie, Frost) or a light classic theme
(GeneratePress/Kadence) over page builders, so design lives in `theme.json` + patterns.

## When taste and SEO disagree, SEO wins
- **Speed:** heavy motion, blur, video backgrounds and extra fonts must not push
  LCP > 2.5s or CLS > 0.1. Max 2 font families, preload the hero image, no autoplaying hero video as LCP.
- **Structure:** keep exactly one H1 and a logical H2/H3 order even when the design
  wants big type elsewhere.
- **Content:** the taste "short copy" rule applies to landing/hero sections only.
  Service pages and blog posts still need enough text to answer search intent.
- **Redesigns:** never change URLs, slugs, titles or nav labels without approval
  (taste-skill section 11.F agrees). Record before/after in `sites/<slug>/CHANGELOG.md`.

## Which skill to use
- New site look → `design-taste-frontend` + one preset (`minimalist-ui` or `high-end-visual-design`), chosen from `brand` in `site.yml`.
- Improving an existing site → `redesign-existing-projects` (audit first, fix in its priority order).
