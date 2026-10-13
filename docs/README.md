# CloudZoom Solutions — CrafterCMS project

Studio site id: `lss-cdz-cloudzoom-2`.

Source: [https://www.cloudzoom.dev/](https://www.cloudzoom.dev/).

## Source site

CloudZoom Solutions is a static marketing site. Each URL is one HTML document. There is no application framework, bundler, or client-side router. Marketing and blog pages repeat a `<style>` block in the document. The AltWheels library is the only area with a shared stylesheet and a small script.

### Information architecture

| Path | Role |
|------|------|
| `/` | Home |
| `/services` | Services |
| `/software` | Software |
| `/work` | Work |
| `/blog` | Article index |
| `/blog/{article}` | Five articles |
| `/about` | About |
| `/contact` | Contact |
| `/altwheels` | AltWheels resource library |
| `/altwheels/fleet-tools` | Fleet tool directory |
| `/altwheels/references` | Reference templates and prompts |

Primary navigation is Home, Services, Software, Work, Blog, About, Contact, plus a Strategy Call action to `/contact`. Blog articles and AltWheels pages keep that same destination set. AltWheels adds its own header treatment and a resource footer.

### Styles

Marketing pages share one visual system, copied into each document rather than linked as a site-wide CSS file:

- Type: Space Grotesk and Manrope from Google Fonts.
- Icons: Phosphor Icons, regular weight, from `unpkg.com/@phosphor-icons/web`.
- Tokens: CSS custom properties on `:root` for type scale, spacing, radius, and motion.
- Color: page canvas `#f8fafc`, text `#0f172a`, muted slate, cyan accent `#06b6d4`, logo navy `#0D2545`.
- Layout: fixed top navigation, content width up to 1440px, hero, card grids, and a closing call to action.
- Elevation: soft shadows (`--theme-shadow-elevated`, `--theme-shadow-md`, `--theme-shadow-lift-hover`).

AltWheels uses `/altwheels/assets/altwheels.css` and `/altwheels/assets/altwheels.js` instead of the marketing `<style>` block. Its header is a different component variant (`site-header`) and its pages are long-form resource documents.

### Model and frameworks

The source has no React, Vue, Angular, or server template. Pages are hand-written HTML. Behavior is limited to Phosphor icon CSS and the AltWheels script. Images are PNG and SVG files under `/assets` and `/altwheels/assets`. Downloads are Markdown, PDF, and a zip resource pack.

The Crafter model follows that shape:

- `/page/landing` for the seven sectioned pages (home, services, software, work, about, contact, blog).
- `/page/article` for the five posts. Card fields feed the home preview and the blog index.
- `/page/resource` for the three AltWheels pages. The original `<main>` is stored in `main_html`.
- `/component/header` and `/component/footer`, chosen by the level descriptor. AltWheels has its own descriptor.
- `/component/section` for each top-level region. `layout_s=html` keeps the original markup and class names in `markup_html`. Blog regions use `blog-preview` and `article-index`, which list article content items instead of copying cards.

Per-page marketing CSS is extracted to `/static-assets/app/css/{page}.css`. Image paths move from `/assets/` to `/static-assets/images/`. AltWheels files move under `/static-assets/altwheels/`. Old `.html` URLs redirect to the extensionless Crafter paths.

## Alignment with the source

Titles and H1 text were compared between the mirrored HTML and the content items.

| Path | Title matches | H1 matches | Source title |
|------|---------------|------------|--------------|
| `/` | yes | yes | CloudZoom Solutions Inc. \| AI-Enhanced Software Development & Automated QA |
| `/services` | yes | yes | Services \| AI-Enhanced Software Development & Automated QA |
| `/software` | yes | yes | What Kind of Software We Build \| CloudZoom Solutions Inc. |
| `/work` | yes | yes | Work \| CloudZoom Solutions Inc. |
| `/about` | yes | yes | About \| CloudZoom Solutions Inc. |
| `/contact` | yes | yes | Contact \| CloudZoom Solutions Inc. |
| `/blog` | yes | yes | Blog & Articles \| AI Software Delivery & QA \| CloudZoom Solutions |
| `/blog/altwheels-fleet-day-2026-ai-resources` | yes | yes | CloudZoom at AltWheels Fleet Day 2026: Practical AI for Fleet Teams \| CloudZoom Solutions |
| `/blog/role-based-ai-qa-agents-cleaning-platform` | yes | yes | OAQA for MyTidyBiz: Role-Based AI QA Agents \| CloudZoom Solutions |
| `/blog/exponential-growth-of-ai-software-industry` | yes | yes | The Exponential Growth of AI and What It Means for Software \| CloudZoom Solutions |
| `/blog/ai-agents-replacing-manual-workflows` | yes | yes | How AI Agents Are Replacing Manual Business Workflows \| CloudZoom Solutions |
| `/blog/iot-for-small-business-costs-and-roi` | yes | yes | IoT for Small Business: What It Actually Costs and What You Get Back \| CloudZoom Solutions |
| `/altwheels` | yes | yes | What can AI do for your fleet? \| AltWheels \| CloudZoom Solutions |
| `/altwheels/fleet-tools` | yes | yes | Fleet-tool directory \| AltWheels \| CloudZoom Solutions |
| `/altwheels/references` | yes | yes | Fleet AI references \| AltWheels \| CloudZoom Solutions |

Every compared title and H1 matches the source. The article headline stores the em dash as a character; the source HTML uses `&mdash;`.

Section order matches the source on home, services, software, work, about, and contact. The blog index keeps `blog-hero` and `newsletter-section` as stored HTML. The middle region is a `/component/section` with `layout_s=article-index`, and the template renders the source `articles-section` from the article content items. Marketing navigation is Home, Services, Software, Work, Blog, About, Contact. All 52 `/static-assets/` references in content and templates resolve to files in this project.

Studio project `lss-cdz-cloudzoom-2` serves these pages in preview. All 15 URLs returned HTTP 200 with the source title and H1 and no FreeMarker error. Home, services, software, work, about, contact, and the blog index render `top-nav`, `hero`, and `cta-button`. Each article renders `article-body`.

## Site map and token analysis

The page map is the information architecture table above. `count_tokens_directory.py` (`gpt-5`, tokenizer `o200k_base`) reports 142 text files, 242,559 tokens, and 10 skipped binary files (7.7 MB). The table below uses the same text rules and also lists binary files, except two `.DS_Store` files, so the file total is 150 and the token total stays 242,559.

### By directory and file type

| Directory | File type | Files | Tokens |
|-----------|-----------|------:|-------:|
| `(root)` | `.yaml` | 1 | 204 |
| `.cursor/skills` | `.md` | 1 | 34,894 |
| `config/engine` | `.xml` | 4 | 1,250 |
| `config/studio` | `.xml` | 7 | 11,798 |
| `config/studio/administration` | `.xml` | 2 | 4,210 |
| `config/studio/content-types/component/footer` | `.xml` | 2 | 4,464 |
| `config/studio/content-types/component/header` | `.xml` | 2 | 2,797 |
| `config/studio/content-types/component/level-descriptor` | `.groovy` | 2 | 458 |
| `config/studio/content-types/component/level-descriptor` | `.xml` | 2 | 3,262 |
| `config/studio/content-types/component/section` | `.xml` | 2 | 2,255 |
| `config/studio/content-types/page/article` | `.xml` | 2 | 8,465 |
| `config/studio/content-types/page/landing` | `.xml` | 2 | 4,790 |
| `config/studio/content-types/page/resource` | `.xml` | 2 | 3,568 |
| `config/studio/dependency` | `.xml` | 1 | 3,406 |
| `config/studio/targeting` | `.xml` | 1 | 462 |
| `config/studio/workflow` | `.xml` | 1 | 2,240 |
| `docs` | `.md` | 6 | 7,335 |
| `scripts/controllers/plugins/org/craftercms/plugin/sitemap` | `.groovy` | 1 | 599 |
| `site/components/footers` | `.xml` | 4 | 2,550 |
| `site/components/headers` | `.xml` | 2 | 1,395 |
| `site/components/sections/about` | `.xml` | 5 | 2,875 |
| `site/components/sections/blog` | `.xml` | 3 | 1,336 |
| `site/components/sections/contact` | `.xml` | 2 | 1,625 |
| `site/components/sections/home` | `.xml` | 7 | 10,241 |
| `site/components/sections/services` | `.xml` | 4 | 7,042 |
| `site/components/sections/software` | `.xml` | 5 | 4,215 |
| `site/components/sections/work` | `.xml` | 3 | 2,984 |
| `site/website` | `.xml` | 2 | 1,507 |
| `site/website/about` | `.xml` | 1 | 935 |
| `site/website/altwheels` | `.xml` | 2 | 6,267 |
| `site/website/altwheels/fleet-tools` | `.xml` | 1 | 1,506 |
| `site/website/altwheels/references` | `.xml` | 1 | 2,019 |
| `site/website/blog` | `.xml` | 1 | 931 |
| `site/website/blog/ai-agents-replacing-manual-workflows` | `.xml` | 1 | 2,377 |
| `site/website/blog/altwheels-fleet-day-2026-ai-resources` | `.xml` | 1 | 2,265 |
| `site/website/blog/exponential-growth-of-ai-software-industry` | `.xml` | 1 | 3,967 |
| `site/website/blog/iot-for-small-business-costs-and-roi` | `.xml` | 1 | 2,626 |
| `site/website/blog/role-based-ai-qa-agents-cleaning-platform` | `.xml` | 1 | 5,018 |
| `site/website/contact` | `.xml` | 1 | 701 |
| `site/website/services` | `.xml` | 1 | 878 |
| `site/website/software` | `.xml` | 1 | 963 |
| `site/website/work` | `.xml` | 1 | 793 |
| `static-assets/altwheels` | `.md` | 1 | 1,456 |
| `static-assets/altwheels/assets` | `.css` | 1 | 3,427 |
| `static-assets/altwheels/assets` | `.js` | 1 | 137 |
| `static-assets/altwheels/assets` | `.png` | 1 | 0 |
| `static-assets/altwheels/assets` | `.svg` | 2 | 6,002 |
| `static-assets/altwheels/downloads` | `.md` | 2 | 3,007 |
| `static-assets/altwheels/downloads` | `.pdf` | 1 | 0 |
| `static-assets/altwheels/downloads` | `.zip` | 1 | 0 |
| `static-assets/altwheels/prompts` | `.txt` | 9 | 2,004 |
| `static-assets/altwheels/skills/fleet-weekly-briefing` | `.md` | 1 | 353 |
| `static-assets/altwheels/templates` | `.md` | 3 | 857 |
| `static-assets/app/css` | `.css` | 12 | 42,825 |
| `static-assets/images` | `.png` | 5 | 0 |
| `static-assets/images` | `.svg` | 1 | 1,991 |
| `templates/web/components` | `.ftl` | 3 | 2,543 |
| `templates/web/errors` | `.ftl` | 7 | 456 |
| `templates/web/fragments` | `.ftl` | 2 | 504 |
| `templates/web/pages` | `.ftl` | 3 | 1,065 |
| `tools` | `.py` | 1 | 12,459 |

### Entire site

| File type | Files | Tokens |
|-----------|------:|-------:|
| `.xml` | 82 | 119,983 |
| `.md` | 14 | 47,902 |
| `.css` | 13 | 46,252 |
| `.py` | 1 | 12,459 |
| `.svg` | 3 | 7,993 |
| `.ftl` | 15 | 4,568 |
| `.txt` | 9 | 2,004 |
| `.groovy` | 3 | 1,057 |
| `.yaml` | 1 | 204 |
| `.js` | 1 | 137 |
| `.pdf` | 1 | 0 |
| `.png` | 6 | 0 |
| `.zip` | 1 | 0 |
| **Total** | **150** | **242,559** |

Binary files: 8 (7.6 MB), included in the file counts above with 0 tokens.

Content-type documentation: [pages.md](pages.md), [components.md](components.md), [items.md](items.md), [global.md](global.md), [ARCHITECTURE_DIAGRAM.md](ARCHITECTURE_DIAGRAM.md).
