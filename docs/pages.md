# Page content types

Marketing pages and the blog index use `/page/landing`. Posts use `/page/article`. The AltWheels library uses `/page/resource`. Header and footer come from the level descriptor unless a page overrides `header_o` or `footer_o`.

## `/page/article` — Article

Blog article.

- Form: `config/studio/content-types/page/article/form-definition.xml`
- Display template: `/templates/web/pages/article.ftl`
- Datasources:
  - headerComponents (shared-content) repoPath=/site/components/headers/
  - footerComponents (shared-content) repoPath=/site/components/footers/

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false |  |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false |  |
| navLabel | input | Nav Label | false | maxlength=500; tokenize=false |  |
| title_t | input | Title | true | maxlength=500; tokenize=false |  |
| headline_t | input | Headline | true | maxlength=500; tokenize=false |  |
| seoDescription_t | textarea | SEO Description | false | maxlength=4000; tokenize=false |  |
| navKey_s | input | Active Nav Key | false | maxlength=500; tokenize=false |  |
| stylesheet_s | input | Stylesheet | false | maxlength=500; tokenize=false |  |
| headLinks_html | textarea | Head Links | false | maxlength=8000; tokenize=false |  |
| author_t | input | Author | false | maxlength=500; tokenize=false |  |
| dateLabel_t | input | Date | false | maxlength=500; tokenize=false |  |
| readTime_t | input | Read Time | false | maxlength=500; tokenize=false |  |
| listRead_t | input | Blog Index Read Time | false | maxlength=500; tokenize=false |  |
| wrap_s | input | Wrapper (main or empty) | false | maxlength=500; tokenize=false |  |
| sortOrder_s | input | Sort Order | false | maxlength=500; tokenize=false |  |
| featured_s | input | Featured on Blog Index (true/false) | false | maxlength=500; tokenize=false |  |
| showOnHome_s | input | Show on Home (true/false) | false | maxlength=500; tokenize=false |  |
| homeOrder_s | input | Home Order | false | maxlength=500; tokenize=false |  |
| visualLabel_t | input | Blog Card Label | false | maxlength=500; tokenize=false |  |
| icon_s | input | Icon Class | false | maxlength=500; tokenize=false |  |
| listExcerpt_t | textarea | Blog Index Excerpt | false | maxlength=2000; tokenize=false |  |
| homeTag_t | input | Home Card Tag | false | maxlength=500; tokenize=false |  |
| homeIcon_s | input | Home Icon Class | false | maxlength=500; tokenize=false |  |
| homeMeta_t | input | Home Card Meta | false | maxlength=500; tokenize=false |  |
| homeExcerpt_t | textarea | Home Card Excerpt | false | maxlength=2000; tokenize=false |  |
| homeCta_t | input | Home Card Link Label | false | maxlength=500; tokenize=false |  |
| tags_o | repeat | Tags | false | minOccurs=0; maxOccurs=* | Repeatable group. Nested fields below. |
| tags_o.label_t | input | Tag | true | maxlength=500; tokenize=false |  |
| listTags_o | repeat | Blog Index Tags | false | minOccurs=0; maxOccurs=* | Repeatable group. Nested fields below. |
| listTags_o.label_t | input | Tag | true | maxlength=500; tokenize=false |  |
| listDate_t | input | Blog Index Date | false | maxlength=500; tokenize=false |  |
| body_html | textarea | Article Body HTML | false | maxlength=500000; tokenize=false |  |
| header_o | node-selector | Header Override | false | maxSize=1; itemManager=headerComponents; contentTypes=/component/header | List. Allowed: /component/header. itemManager=headerComponents. |
| footer_o | node-selector | Footer Override | false | maxSize=1; itemManager=footerComponents; contentTypes=/component/footer | List. Allowed: /component/footer. itemManager=footerComponents. |

## `/page/landing` — Landing Page

Page composed of sections.

- Form: `config/studio/content-types/page/landing/form-definition.xml`
- Display template: `/templates/web/pages/landing.ftl`
- Datasources:
  - headerComponents (shared-content) repoPath=/site/components/headers/
  - footerComponents (shared-content) repoPath=/site/components/footers/
  - sectionComponents (shared-content) repoPath=/site/components/sections/

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false |  |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false |  |
| navLabel | input | Nav Label | false | maxlength=500; tokenize=false |  |
| title_t | input | Title | true | maxlength=500; tokenize=false |  |
| seoDescription_t | textarea | SEO Description | false | maxlength=4000; tokenize=false |  |
| navKey_s | input | Active Nav Key | false | maxlength=40; tokenize=false |  |
| stylesheet_s | input | Stylesheet | false | maxlength=500; tokenize=false |  |
| headLinks_html | textarea | Head Links | false | maxlength=8000; tokenize=false |  |
| footerMode_s | input | Footer Mode (inherit, marketing, blog, article) | false | maxlength=500; tokenize=false |  |
| footerTagline_t | textarea | Footer Tagline Override | false | maxlength=800; tokenize=false |  |
| footerLinkedIn_s | input | Footer LinkedIn Override (true/false) | false | maxlength=500; tokenize=false |  |
| footerLegal_s | input | Footer Copyright Override (true/false) | false | maxlength=500; tokenize=false |  |
| header_o | node-selector | Header Override | false | maxSize=1; itemManager=headerComponents; contentTypes=/component/header | List. Allowed: /component/header. itemManager=headerComponents. |
| footer_o | node-selector | Footer Override | false | maxSize=1; itemManager=footerComponents; contentTypes=/component/footer | List. Allowed: /component/footer. itemManager=footerComponents. |
| sections_o | node-selector | Sections | false | itemManager=sectionComponents; contentTypes=/component/section | List. Allowed: /component/section. itemManager=sectionComponents. |

## `/page/resource` — Resource Page

AltWheels resource page.

- Form: `config/studio/content-types/page/resource/form-definition.xml`
- Display template: `/templates/web/pages/resource.ftl`
- Datasources:
  - headerComponents (shared-content) repoPath=/site/components/headers/
  - footerComponents (shared-content) repoPath=/site/components/footers/

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false |  |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false |  |
| navLabel | input | Nav Label | false | maxlength=500; tokenize=false |  |
| title_t | input | Title | true | maxlength=500; tokenize=false |  |
| seoDescription_t | textarea | SEO Description | false | maxlength=4000; tokenize=false |  |
| stylesheet_s | input | Stylesheet | false | maxlength=500; tokenize=false |  |
| headLinks_html | textarea | Head Links | false | maxlength=8000; tokenize=false |  |
| script_s | input | Script | false | maxlength=500; tokenize=false |  |
| main_html | textarea | Main HTML | false | maxlength=500000; tokenize=false |  |
| header_o | node-selector | Header Override | false | maxSize=1; itemManager=headerComponents; contentTypes=/component/header | List. Allowed: /component/header. itemManager=headerComponents. |
| footer_o | node-selector | Footer Override | false | maxSize=1; itemManager=footerComponents; contentTypes=/component/footer | List. Allowed: /component/footer. itemManager=footerComponents. |
