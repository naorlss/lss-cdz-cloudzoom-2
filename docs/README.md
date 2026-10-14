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
- `/page/article` for the five posts. Card fields feed the home preview and the blog index. `body_html` is an `rte` field for the article copy; the `article-body` wrapper stays in the template.
- `/page/resource` for the three AltWheels pages. Each region is a component in `sections_o`.
- `/component/header` and `/component/footer`, chosen by the level descriptor. AltWheels has its own descriptor.
- One content type per region (hero, card grid, call to action, AltWheels block, and so on). Headings, links, and list items are fields. Diagrams and font links live in templates.

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

Section order matches the source on home, services, software, work, about, and contact. Each region is its own component type. The blog index uses `/component/blog-hero`, `/component/article-index`, and `/component/newsletter`. Marketing navigation is Home, Services, Software, Work, Blog, About, Contact.

Studio project `lss-cdz-cloudzoom-2` serves these pages in preview. All 15 URLs returned HTTP 200 with the source title and H1 and no FreeMarker error. Home, services, software, work, about, contact, and the blog index render `top-nav`, `hero`, and `cta-button`. Each article renders `article-body`.

## Site map and token analysis

The page map is the information architecture table above. `count_tokens_directory.py` (`gpt-5`, tokenizer `o200k_base`) reports 265 text files and 394,594 tokens. The table below uses the same text rules and also lists binary files, except two `.DS_Store` files, so the file total is 273 and the token total stays 394,594.

### By directory and file type

| Directory | File type | Files | Tokens |
|-----------|-----------|------:|-------:|
| `(root)` | `.yaml` | 1 | 204 |
| `.cursor/skills` | `.md` | 1 | 34,894 |
| `config/engine` | `.xml` | 4 | 1,250 |
| `config/studio` | `.xml` | 7 | 11,798 |
| `config/studio/administration` | `.xml` | 2 | 4,210 |
| `config/studio/content-types/component/ai-banner` | `.xml` | 2 | 1,966 |
| `config/studio/content-types/component/article-index` | `.xml` | 2 | 937 |
| `config/studio/content-types/component/aw-callout` | `.xml` | 2 | 2,061 |
| `config/studio/content-types/component/aw-downloads` | `.xml` | 2 | 4,420 |
| `config/studio/content-types/component/aw-hero` | `.xml` | 2 | 5,315 |
| `config/studio/content-types/component/aw-nav` | `.xml` | 2 | 1,733 |
| `config/studio/content-types/component/aw-patterns` | `.xml` | 2 | 1,736 |
| `config/studio/content-types/component/aw-prompts` | `.xml` | 2 | 4,192 |
| `config/studio/content-types/component/aw-steps` | `.xml` | 2 | 6,328 |
| `config/studio/content-types/component/aw-templates` | `.xml` | 2 | 3,972 |
| `config/studio/content-types/component/blog-hero` | `.xml` | 2 | 1,829 |
| `config/studio/content-types/component/blog-preview` | `.xml` | 2 | 1,823 |
| `config/studio/content-types/component/case-studies` | `.xml` | 2 | 4,724 |
| `config/studio/content-types/component/contact-card` | `.xml` | 2 | 2,822 |
| `config/studio/content-types/component/contact-panel` | `.xml` | 2 | 5,386 |
| `config/studio/content-types/component/cta-band` | `.xml` | 2 | 2,055 |
| `config/studio/content-types/component/expertise` | `.xml` | 2 | 1,719 |
| `config/studio/content-types/component/eyebrow-hero` | `.xml` | 2 | 1,639 |
| `config/studio/content-types/component/final-cta` | `.xml` | 2 | 2,919 |
| `config/studio/content-types/component/fit-panels` | `.xml` | 2 | 1,878 |
| `config/studio/content-types/component/footer` | `.xml` | 2 | 4,464 |
| `config/studio/content-types/component/header` | `.xml` | 2 | 2,797 |
| `config/studio/content-types/component/home-hero` | `.xml` | 2 | 2,845 |
| `config/studio/content-types/component/home-services` | `.xml` | 2 | 3,209 |
| `config/studio/content-types/component/level-descriptor` | `.groovy` | 2 | 458 |
| `config/studio/content-types/component/level-descriptor` | `.xml` | 2 | 3,262 |
| `config/studio/content-types/component/newsletter` | `.xml` | 2 | 2,060 |
| `config/studio/content-types/component/process-steps` | `.xml` | 2 | 2,419 |
| `config/studio/content-types/component/reference-list` | `.xml` | 2 | 3,233 |
| `config/studio/content-types/component/resource-intro` | `.xml` | 2 | 2,941 |
| `config/studio/content-types/component/service-catalog` | `.xml` | 2 | 2,323 |
| `config/studio/content-types/component/services-hero` | `.xml` | 2 | 2,293 |
| `config/studio/content-types/component/social-proof` | `.xml` | 2 | 2,174 |
| `config/studio/content-types/component/software-catalog` | `.xml` | 2 | 2,776 |
| `config/studio/content-types/component/story` | `.xml` | 2 | 2,102 |
| `config/studio/content-types/component/tool-directory` | `.xml` | 2 | 3,887 |
| `config/studio/content-types/component/value-props` | `.xml` | 2 | 1,724 |
| `config/studio/content-types/component/why-section` | `.xml` | 2 | 1,992 |
| `config/studio/content-types/component/work-hero` | `.xml` | 2 | 1,607 |
| `config/studio/content-types/page/article` | `.xml` | 2 | 8,444 |
| `config/studio/content-types/page/landing` | `.xml` | 2 | 4,660 |
| `config/studio/content-types/page/resource` | `.xml` | 2 | 3,683 |
| `config/studio/dependency` | `.xml` | 1 | 3,406 |
| `config/studio/targeting` | `.xml` | 1 | 462 |
| `config/studio/workflow` | `.xml` | 1 | 2,240 |
| `docs` | `.md` | 6 | 18,937 |
| `scripts/controllers/plugins/org/craftercms/plugin/sitemap` | `.groovy` | 1 | 599 |
| `site/components/footers` | `.xml` | 4 | 2,550 |
| `site/components/headers` | `.xml` | 2 | 1,395 |
| `site/components/sections/about` | `.xml` | 5 | 2,507 |
| `site/components/sections/altwheels` | `.xml` | 8 | 8,776 |
| `site/components/sections/altwheels/fleet-tools` | `.xml` | 2 | 2,047 |
| `site/components/sections/altwheels/references` | `.xml` | 2 | 3,279 |
| `site/components/sections/blog` | `.xml` | 3 | 1,009 |
| `site/components/sections/contact` | `.xml` | 2 | 1,432 |
| `site/components/sections/home` | `.xml` | 7 | 4,259 |
| `site/components/sections/services` | `.xml` | 4 | 3,577 |
| `site/components/sections/software` | `.xml` | 5 | 4,237 |
| `site/components/sections/work` | `.xml` | 3 | 3,529 |
| `site/website` | `.xml` | 2 | 1,414 |
| `site/website/about` | `.xml` | 1 | 842 |
| `site/website/altwheels` | `.xml` | 2 | 1,486 |
| `site/website/altwheels/fleet-tools` | `.xml` | 1 | 559 |
| `site/website/altwheels/references` | `.xml` | 1 | 558 |
| `site/website/blog` | `.xml` | 1 | 769 |
| `site/website/blog/ai-agents-replacing-manual-workflows` | `.xml` | 1 | 2,226 |
| `site/website/blog/altwheels-fleet-day-2026-ai-resources` | `.xml` | 1 | 2,114 |
| `site/website/blog/exponential-growth-of-ai-software-industry` | `.xml` | 1 | 3,816 |
| `site/website/blog/iot-for-small-business-costs-and-roi` | `.xml` | 1 | 2,475 |
| `site/website/blog/role-based-ai-qa-agents-cleaning-platform` | `.xml` | 1 | 4,867 |
| `site/website/contact` | `.xml` | 1 | 608 |
| `site/website/services` | `.xml` | 1 | 785 |
| `site/website/software` | `.xml` | 1 | 870 |
| `site/website/work` | `.xml` | 1 | 700 |
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
| `templates/web/components` | `.ftl` | 37 | 15,200 |
| `templates/web/errors` | `.ftl` | 7 | 456 |
| `templates/web/fragments` | `.ftl` | 6 | 943 |
| `templates/web/fragments/diagrams` | `.ftl` | 3 | 8,837 |
| `templates/web/pages` | `.ftl` | 3 | 1,162 |
| `tools` | `.py` | 3 | 40,444 |

### Entire site

| File type | Files | Tokens |
|-----------|------:|-------:|
| `.xml` | 162 | 210,401 |
| `.md` | 14 | 59,504 |
| `.css` | 13 | 46,252 |
| `.py` | 3 | 40,444 |
| `.ftl` | 56 | 26,598 |
| `.svg` | 3 | 7,993 |
| `.txt` | 9 | 2,004 |
| `.groovy` | 3 | 1,057 |
| `.yaml` | 1 | 204 |
| `.js` | 1 | 137 |
| `.pdf` | 1 | 0 |
| `.png` | 6 | 0 |
| `.zip` | 1 | 0 |
| **Total** | **273** | **394,594** |

Binary files: 8 (7.6 MB), included in the file counts above with 0 tokens.

Content-type documentation: [pages.md](pages.md), [components.md](components.md), [items.md](items.md), [global.md](global.md), [ARCHITECTURE_DIAGRAM.md](ARCHITECTURE_DIAGRAM.md).
