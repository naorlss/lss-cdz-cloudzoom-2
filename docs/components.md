# Section and chrome components

Header and footer are shared components. Each visible region of a landing page is a `/component/section` stored under `/site/components/sections/{page}/` and referenced, in source order, from the page `sections_o` field.

## `/component/footer` — Footer

Footer content. Pages can override the tagline and which blocks show.

- Form: `config/studio/content-types/component/footer/form-definition.xml`
- Display template: `/templates/web/components/footer.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false |  |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false |  |
| variant_s | input | Variant (marketing, blog, article, altwheels) | true | maxlength=40; tokenize=false |  |
| brand_t | input | Brand | false | maxlength=500; tokenize=false |  |
| tagline_t | textarea | Tagline | false | maxlength=800; tokenize=false |  |
| phone_t | input | Phone | false | maxlength=500; tokenize=false |  |
| phoneUrl_s | input | Phone URL | false | maxlength=500; tokenize=false |  |
| email_t | input | Email | false | maxlength=500; tokenize=false |  |
| linkedinLabel_t | input | LinkedIn Label | false | maxlength=500; tokenize=false |  |
| linkedinUrl_s | input | LinkedIn URL | false | maxlength=500; tokenize=false |  |
| copyright_t | input | Copyright | false | maxlength=500; tokenize=false |  |
| showLinkedIn_s | input | Show LinkedIn (true/false) | false | maxlength=500; tokenize=false |  |
| showLegal_s | input | Show Copyright Bar (true/false) | false | maxlength=500; tokenize=false |  |
| nav_o | repeat | Footer Navigation | false | minOccurs=0; maxOccurs=* | Repeatable group. Nested fields below. |
| nav_o.label_t | input | Label | true | maxlength=500; tokenize=false |  |
| nav_o.url_s | input | URL | true | maxlength=500; tokenize=false |  |
| connect_o | repeat | Blog Connect Column | false | minOccurs=0; maxOccurs=* | Repeatable group. Nested fields below. |
| connect_o.label_t | input | Label | true | maxlength=500; tokenize=false |  |
| connect_o.url_s | input | URL | true | maxlength=500; tokenize=false |  |

## `/component/header` — Header

Primary navigation.

- Form: `config/studio/content-types/component/header/form-definition.xml`
- Display template: `/templates/web/components/header.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false |  |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false |  |
| variant_s | input | Variant (marketing or altwheels) | true | maxlength=40; tokenize=false |  |
| brand_t | input | Brand | true | maxlength=500; tokenize=false |  |
| ctaLabel_t | input | Call to Action Label | false | maxlength=500; tokenize=false |  |
| ctaUrl_s | input | Call to Action URL | false | maxlength=500; tokenize=false |  |
| nav_o | repeat | Navigation | false | minOccurs=0; maxOccurs=* | Repeatable group. Nested fields below. |
| nav_o.label_t | input | Label | true | maxlength=500; tokenize=false |  |
| nav_o.url_s | input | URL | true | maxlength=500; tokenize=false |  |
| nav_o.key_s | input | Nav Key | true | maxlength=40; tokenize=false |  |
| tagline_t | textarea | AltWheels Tagline | false | maxlength=500; tokenize=false |  |

## `/component/section` — Section

Page section.

- Form: `config/studio/content-types/component/section/form-definition.xml`
- Display template: `/templates/web/components/section.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false |  |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false |  |
| layout_s | input | Layout (html, blog-preview, article-index) | true | maxlength=40; tokenize=false |  |
| title_t | input | Heading | false | maxlength=500; tokenize=false |  |
| subtitle_t | textarea | Subheading | false | maxlength=2000; tokenize=false |  |
| linkLabel_t | input | Link Label | false | maxlength=500; tokenize=false |  |
| linkUrl_s | input | Link URL | false | maxlength=500; tokenize=false |  |
| markup_html | textarea | Section HTML | false | maxlength=500000; tokenize=false |  |
