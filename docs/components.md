# Section and chrome components

Header and footer stay shared components. Each visible region is its own component type: 35 types and 41 content items, referenced in order from the page `sections_o` field. Plain text uses `input` or `textarea`. Lists use repeat groups. Images use `image-picker`. Article body copy uses `rte`.

## `/component/home-hero` — Home Hero

Home hero with actions, trust chips, and the systems diagram.

- Form: `config/studio/content-types/component/home-hero/form-definition.xml`
- Display template: `/templates/web/components/home-hero.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| title_t | input | Title | false | maxlength=500; tokenize=false |  |
| subtitle_t | textarea | Subtitle | false | maxlength=4000; tokenize=false | Plain text. |
| primaryLabel_t | input | Primary Label | false | maxlength=500; tokenize=false |  |
| primaryUrl_s | input | Primary URL | false | maxlength=500; tokenize=false |  |
| secondaryLabel_t | input | Secondary Label | false | maxlength=500; tokenize=false |  |
| secondaryUrl_s | input | Secondary URL | false | maxlength=500; tokenize=false |  |
| chips_o | repeat | Chips | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| chips_o.icon_s | input | Icon | false | maxlength=80; tokenize=false | Nested in chips_o. |
| chips_o.label_t | input | Label | false | maxlength=500; tokenize=false | Nested in chips_o. |

## `/component/eyebrow-hero` — Eyebrow Hero

Hero with an eyebrow, heading, and subheading.

- Form: `config/studio/content-types/component/eyebrow-hero/form-definition.xml`
- Display template: `/templates/web/components/eyebrow-hero.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| eyebrow_t | input | Eyebrow | false | maxlength=500; tokenize=false |  |
| title_t | input | Title | false | maxlength=500; tokenize=false |  |
| subtitle_t | textarea | Subtitle | false | maxlength=4000; tokenize=false | Plain text. |

## `/component/services-hero` — Services Hero

Services hero whose subheading includes one link.

- Form: `config/studio/content-types/component/services-hero/form-definition.xml`
- Display template: `/templates/web/components/services-hero.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| eyebrow_t | input | Eyebrow | false | maxlength=500; tokenize=false |  |
| title_t | input | Title | false | maxlength=500; tokenize=false |  |
| textBefore_t | textarea | Text Before | false | maxlength=4000; tokenize=false | Plain text. |
| linkLabel_t | input | Link Label | false | maxlength=500; tokenize=false |  |
| linkUrl_s | input | Link URL | false | maxlength=500; tokenize=false |  |
| textAfter_t | textarea | Text After | false | maxlength=4000; tokenize=false | Plain text. |

## `/component/blog-hero` — Blog Hero

Blog index hero.

- Form: `config/studio/content-types/component/blog-hero/form-definition.xml`
- Display template: `/templates/web/components/blog-hero.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| eyebrow_t | input | Eyebrow | false | maxlength=500; tokenize=false |  |
| titleLine1_t | input | Title Line1 | false | maxlength=500; tokenize=false |  |
| titleLine2_t | input | Title Line2 | false | maxlength=500; tokenize=false |  |
| subtitle_t | textarea | Subtitle | false | maxlength=4000; tokenize=false | Plain text. |

## `/component/work-hero` — Work Hero

Work page hero.

- Form: `config/studio/content-types/component/work-hero/form-definition.xml`
- Display template: `/templates/web/components/work-hero.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| eyebrow_t | input | Eyebrow | false | maxlength=500; tokenize=false |  |
| title_t | input | Title | false | maxlength=500; tokenize=false |  |
| subtitle_t | textarea | Subtitle | false | maxlength=4000; tokenize=false | Plain text. |

## `/component/value-props` — Value Props

Row of icon stats.

- Form: `config/studio/content-types/component/value-props/form-definition.xml`
- Display template: `/templates/web/components/value-props.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| items_o | repeat | Items | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| items_o.icon_s | input | Icon | false | maxlength=80; tokenize=false | Nested in items_o. |
| items_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in items_o. |
| items_o.text_t | input | Text | false | maxlength=500; tokenize=false | Nested in items_o. |

## `/component/why-section` — Why Section

Benefit list and diagram.

- Form: `config/studio/content-types/component/why-section/form-definition.xml`
- Display template: `/templates/web/components/why-section.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| subheading_t | textarea | Subheading | false | maxlength=4000; tokenize=false | Plain text. |
| items_o | repeat | Items | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| items_o.icon_s | input | Icon | false | maxlength=80; tokenize=false | Nested in items_o. |
| items_o.text_t | textarea | Text | false | maxlength=4000; tokenize=false | Nested in items_o. |

## `/component/home-services` — Home Services

Home service cards and footer links.

- Form: `config/studio/content-types/component/home-services/form-definition.xml`
- Display template: `/templates/web/components/home-services.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| subtitle_t | textarea | Subtitle | false | maxlength=4000; tokenize=false | Plain text. |
| cards_o | repeat | Cards | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| cards_o.icon_s | input | Icon | false | maxlength=80; tokenize=false | Nested in cards_o. |
| cards_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in cards_o. |
| cards_o.text_t | textarea | Text | false | maxlength=4000; tokenize=false | Nested in cards_o. |
| cards_o.linkLabel_t | input | Link Label | false | maxlength=500; tokenize=false | Nested in cards_o. |
| cards_o.linkUrl_s | input | Link URL | false | maxlength=500; tokenize=false | Nested in cards_o. |
| links_o | repeat | Links | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| links_o.label_t | input | Label | false | maxlength=500; tokenize=false | Nested in links_o. |
| links_o.url_s | input | URL | false | maxlength=500; tokenize=false | Nested in links_o. |

## `/component/social-proof` — Social Proof

Quote and audience labels.

- Form: `config/studio/content-types/component/social-proof/form-definition.xml`
- Display template: `/templates/web/components/social-proof.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| avatar_t | input | Avatar | false | maxlength=500; tokenize=false |  |
| name_t | input | Name | false | maxlength=500; tokenize=false |  |
| role_t | input | Role | false | maxlength=500; tokenize=false |  |
| quote_t | textarea | Quote | false | maxlength=4000; tokenize=false | Plain text. |
| logos_o | repeat | Logos | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| logos_o.label_t | input | Label | false | maxlength=500; tokenize=false | Nested in logos_o. |

## `/component/blog-preview` — Blog Preview

Home page list of selected articles.

- Form: `config/studio/content-types/component/blog-preview/form-definition.xml`
- Display template: `/templates/web/components/blog-preview.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| title_t | input | Title | false | maxlength=500; tokenize=false |  |
| subtitle_t | textarea | Subtitle | false | maxlength=4000; tokenize=false | Plain text. |
| linkLabel_t | input | Link Label | false | maxlength=500; tokenize=false |  |
| linkUrl_s | input | Link URL | false | maxlength=500; tokenize=false |  |

## `/component/article-index` — Article Index

Blog index built from article pages.

- Form: `config/studio/content-types/component/article-index/form-definition.xml`
- Display template: `/templates/web/components/article-index.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |

## `/component/final-cta` — Final Call to Action

Closing call to action with phone and email.

- Form: `config/studio/content-types/component/final-cta/form-definition.xml`
- Display template: `/templates/web/components/final-cta.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| variant_s | input | Variant | false | maxlength=80; tokenize=false |  |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| subtext_t | textarea | Subtext | false | maxlength=4000; tokenize=false | Plain text. |
| ctaLabel_t | input | CTA Label | false | maxlength=500; tokenize=false |  |
| ctaUrl_s | input | CTA URL | false | maxlength=500; tokenize=false |  |
| phoneLabel_t | input | Phone Label | false | maxlength=500; tokenize=false |  |
| phoneUrl_s | input | Phone URL | false | maxlength=500; tokenize=false |  |
| emailLabel_t | input | Email Label | false | maxlength=500; tokenize=false |  |
| emailUrl_s | input | Email URL | false | maxlength=500; tokenize=false |  |

## `/component/cta-band` — Call to Action Band

Section call to action. Variant selects the layout.

- Form: `config/studio/content-types/component/cta-band/form-definition.xml`
- Display template: `/templates/web/components/cta-band.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| variant_s | input | Variant | false | maxlength=80; tokenize=false |  |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| subtext_t | textarea | Subtext | false | maxlength=4000; tokenize=false | Plain text. |
| ctaLabel_t | input | CTA Label | false | maxlength=500; tokenize=false |  |
| ctaUrl_s | input | CTA URL | false | maxlength=500; tokenize=false |  |

## `/component/newsletter` — Newsletter

Blog closing call to action.

- Form: `config/studio/content-types/component/newsletter/form-definition.xml`
- Display template: `/templates/web/components/newsletter.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| subtext_t | textarea | Subtext | false | maxlength=4000; tokenize=false | Plain text. |
| ctaLabel_t | input | CTA Label | false | maxlength=500; tokenize=false |  |
| ctaUrl_s | input | CTA URL | false | maxlength=500; tokenize=false |  |
| note_t | textarea | Note | false | maxlength=4000; tokenize=false | Plain text. |

## `/component/story` — Story

About story paragraphs and stats.

- Form: `config/studio/content-types/component/story/form-definition.xml`
- Display template: `/templates/web/components/story.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| paragraphs_o | repeat | Paragraphs | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| paragraphs_o.text_t | textarea | Text | false | maxlength=4000; tokenize=false | Nested in paragraphs_o. |
| stats_o | repeat | Stats | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| stats_o.value_t | input | Value | false | maxlength=500; tokenize=false | Nested in stats_o. |
| stats_o.label_t | input | Label | false | maxlength=500; tokenize=false | Nested in stats_o. |

## `/component/expertise` — Expertise

Expertise chips.

- Form: `config/studio/content-types/component/expertise/form-definition.xml`
- Display template: `/templates/web/components/expertise.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| chips_o | repeat | Chips | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| chips_o.icon_s | input | Icon | false | maxlength=80; tokenize=false | Nested in chips_o. |
| chips_o.label_t | input | Label | false | maxlength=500; tokenize=false | Nested in chips_o. |

## `/component/contact-card` — Contact Card

About page contact details.

- Form: `config/studio/content-types/component/contact-card/form-definition.xml`
- Display template: `/templates/web/components/contact-card.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| items_o | repeat | Items | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| items_o.icon_s | input | Icon | false | maxlength=80; tokenize=false | Nested in items_o. |
| items_o.label_t | input | Label | false | maxlength=500; tokenize=false | Nested in items_o. |
| items_o.value_t | input | Value | false | maxlength=500; tokenize=false | Nested in items_o. |
| items_o.url_s | input | URL | false | maxlength=500; tokenize=false | Nested in items_o. |
| linkedinLabel_t | input | Linkedin Label | false | maxlength=500; tokenize=false |  |
| linkedinUrl_s | input | Linkedin URL | false | maxlength=500; tokenize=false |  |
| note_t | textarea | Note | false | maxlength=4000; tokenize=false | Plain text. |

## `/component/contact-panel` — Contact Panel

Contact details and message form.

- Form: `config/studio/content-types/component/contact-panel/form-definition.xml`
- Display template: `/templates/web/components/contact-panel.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| intro_t | textarea | Intro | false | maxlength=4000; tokenize=false | Plain text. |
| methods_o | repeat | Methods | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| methods_o.icon_s | input | Icon | false | maxlength=80; tokenize=false | Nested in methods_o. |
| methods_o.label_t | input | Label | false | maxlength=500; tokenize=false | Nested in methods_o. |
| methods_o.value_t | input | Value | false | maxlength=500; tokenize=false | Nested in methods_o. |
| methods_o.url_s | input | URL | false | maxlength=500; tokenize=false | Nested in methods_o. |
| linkedinLabel_t | input | Linkedin Label | false | maxlength=500; tokenize=false |  |
| linkedinUrl_s | input | Linkedin URL | false | maxlength=500; tokenize=false |  |
| boxTitle_t | input | Box Title | false | maxlength=500; tokenize=false |  |
| boxText_t | textarea | Box Text | false | maxlength=4000; tokenize=false | Plain text. |
| formHeading_t | input | Form Heading | false | maxlength=500; tokenize=false |  |
| formSubtitle_t | textarea | Form Subtitle | false | maxlength=4000; tokenize=false | Plain text. |
| formEmail_s | input | Form Email | false | maxlength=500; tokenize=false |  |
| submitLabel_t | input | Submit Label | false | maxlength=500; tokenize=false |  |
| fields_o | repeat | Fields | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| fields_o.label_t | input | Label | false | maxlength=500; tokenize=false | Nested in fields_o. |
| fields_o.name_s | input | Name | false | maxlength=500; tokenize=false | Nested in fields_o. |
| fields_o.type_s | input | Type | false | maxlength=500; tokenize=false | Nested in fields_o. |
| fields_o.placeholder_t | input | Placeholder | false | maxlength=500; tokenize=false | Nested in fields_o. |
| fields_o.required_s | input | Required | false | maxlength=500; tokenize=false | Nested in fields_o. |

## `/component/service-catalog` — Service Catalog

Services page card grid.

- Form: `config/studio/content-types/component/service-catalog/form-definition.xml`
- Display template: `/templates/web/components/service-catalog.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| cards_o | repeat | Cards | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| cards_o.icon_s | input | Icon | false | maxlength=80; tokenize=false | Nested in cards_o. |
| cards_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in cards_o. |
| cards_o.text_t | textarea | Text | false | maxlength=4000; tokenize=false | Nested in cards_o. |
| cards_o.tags_o | repeat | Tags | false | minOccurs=0; maxOccurs=* | Nested in cards_o. |
| cards_o.tags_o.label_t | input | Label | false | maxlength=500; tokenize=false | Nested in cards_o. |

## `/component/ai-banner` — AI Banner

Benefit list and workflow diagram.

- Form: `config/studio/content-types/component/ai-banner/form-definition.xml`
- Display template: `/templates/web/components/ai-banner.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| items_o | repeat | Items | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| items_o.icon_s | input | Icon | false | maxlength=80; tokenize=false | Nested in items_o. |
| items_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in items_o. |
| items_o.text_t | textarea | Text | false | maxlength=4000; tokenize=false | Nested in items_o. |

## `/component/software-catalog` — Software Catalog

Software category cards.

- Form: `config/studio/content-types/component/software-catalog/form-definition.xml`
- Display template: `/templates/web/components/software-catalog.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| kicker_t | input | Kicker | false | maxlength=500; tokenize=false |  |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| subtitle_t | textarea | Subtitle | false | maxlength=4000; tokenize=false | Plain text. |
| cards_o | repeat | Cards | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| cards_o.icon_s | input | Icon | false | maxlength=80; tokenize=false | Nested in cards_o. |
| cards_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in cards_o. |
| cards_o.text_t | textarea | Text | false | maxlength=4000; tokenize=false | Nested in cards_o. |
| cards_o.tags_o | repeat | Tags | false | minOccurs=0; maxOccurs=* | Nested in cards_o. |
| cards_o.tags_o.label_t | input | Label | false | maxlength=500; tokenize=false | Nested in cards_o. |

## `/component/fit-panels` — Fit Panels

Good-fit and poor-fit lists.

- Form: `config/studio/content-types/component/fit-panels/form-definition.xml`
- Display template: `/templates/web/components/fit-panels.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| panels_o | repeat | Panels | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| panels_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in panels_o. |
| panels_o.icon_s | input | Icon | false | maxlength=80; tokenize=false | Nested in panels_o. |
| panels_o.items_o | repeat | Items | false | minOccurs=0; maxOccurs=* | Nested in panels_o. |
| panels_o.items_o.text_t | input | Text | false | maxlength=500; tokenize=false | Nested in panels_o. |

## `/component/process-steps` — Process Steps

Numbered process steps.

- Form: `config/studio/content-types/component/process-steps/form-definition.xml`
- Display template: `/templates/web/components/process-steps.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| kicker_t | input | Kicker | false | maxlength=500; tokenize=false |  |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| subtitle_t | textarea | Subtitle | false | maxlength=4000; tokenize=false | Plain text. |
| steps_o | repeat | Steps | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| steps_o.number_t | input | Number | false | maxlength=500; tokenize=false | Nested in steps_o. |
| steps_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in steps_o. |
| steps_o.text_t | textarea | Text | false | maxlength=4000; tokenize=false | Nested in steps_o. |

## `/component/case-studies` — Case Studies

Case study cards.

- Form: `config/studio/content-types/component/case-studies/form-definition.xml`
- Display template: `/templates/web/components/case-studies.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| cases_o | repeat | Cases | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| cases_o.style_s | input | Style | false | maxlength=500; tokenize=false | Nested in cases_o. |
| cases_o.titleTag_s | input | Title Tag | false | maxlength=500; tokenize=false | Nested in cases_o. |
| cases_o.kicker_t | input | Kicker | false | maxlength=500; tokenize=false | Nested in cases_o. |
| cases_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in cases_o. |
| cases_o.badge_t | input | Badge | false | maxlength=500; tokenize=false | Nested in cases_o. |
| cases_o.linkLabel_t | input | Link Label | false | maxlength=500; tokenize=false | Nested in cases_o. |
| cases_o.linkUrl_s | input | Link URL | false | maxlength=500; tokenize=false | Nested in cases_o. |
| cases_o.linkTarget_s | input | Link Target | false | maxlength=500; tokenize=false | Nested in cases_o. |
| cases_o.statBefore_t | input | Stat Before | false | maxlength=500; tokenize=false | Nested in cases_o. |
| cases_o.statArrow_t | input | Stat Arrow | false | maxlength=500; tokenize=false | Nested in cases_o. |
| cases_o.statAfter_t | input | Stat After | false | maxlength=500; tokenize=false | Nested in cases_o. |
| cases_o.stat_t | input | Stat | false | maxlength=500; tokenize=false | Nested in cases_o. |
| cases_o.text_t | textarea | Text | false | maxlength=4000; tokenize=false | Nested in cases_o. |
| cases_o.tags_o | repeat | Tags | false | minOccurs=0; maxOccurs=* | Nested in cases_o. |
| cases_o.tags_o.label_t | input | Label | false | maxlength=500; tokenize=false | Nested in cases_o. |
| bannerTitle_t | input | Banner Title | false | maxlength=500; tokenize=false |  |
| bannerText_t | textarea | Banner Text | false | maxlength=4000; tokenize=false | Plain text. |

## `/component/aw-hero` — AltWheels Hero

AltWheels home hero.

- Form: `config/studio/content-types/component/aw-hero/form-definition.xml`
- Display template: `/templates/web/components/aw-hero.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| eyebrow_t | input | Eyebrow | false | maxlength=500; tokenize=false |  |
| brandStrong_t | input | Brand Strong | false | maxlength=500; tokenize=false |  |
| brandRest_t | input | Brand Rest | false | maxlength=500; tokenize=false |  |
| titleLine1_t | input | Title Line1 | false | maxlength=500; tokenize=false |  |
| titleLine2_t | input | Title Line2 | false | maxlength=500; tokenize=false |  |
| lead_t | textarea | Lead | false | maxlength=4000; tokenize=false | Plain text. |
| primaryLabel_t | input | Primary Label | false | maxlength=500; tokenize=false |  |
| primaryUrl_s | input | Primary URL | false | maxlength=500; tokenize=false |  |
| primaryDownload_s | input | Primary Download | false | maxlength=500; tokenize=false |  |
| secondaryLabel_t | input | Secondary Label | false | maxlength=500; tokenize=false |  |
| secondaryUrl_s | input | Secondary URL | false | maxlength=500; tokenize=false |  |
| meta_t | input | Meta | false | maxlength=500; tokenize=false |  |
| image_s | image-picker | Image | false | imageManager=uploadImages,existingImages | Stored path under /static-assets/. |
| imageAlt_t | textarea | Image Alt | false | maxlength=4000; tokenize=false | Plain text. |
| imageWidth_s | input | Image Width | false | maxlength=500; tokenize=false |  |
| imageHeight_s | input | Image Height | false | maxlength=500; tokenize=false |  |
| imageUrl_s | input | Image URL | false | maxlength=500; tokenize=false |  |
| imageAria_t | input | Image Aria | false | maxlength=500; tokenize=false |  |
| caption_t | input | Caption | false | maxlength=500; tokenize=false |  |

## `/component/aw-nav` — AltWheels Navigation

In-page resource navigation.

- Form: `config/studio/content-types/component/aw-nav/form-definition.xml`
- Display template: `/templates/web/components/aw-nav.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| ariaLabel_t | input | Aria Label | false | maxlength=500; tokenize=false |  |
| links_o | repeat | Links | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| links_o.label_t | input | Label | false | maxlength=500; tokenize=false | Nested in links_o. |
| links_o.url_s | input | URL | false | maxlength=500; tokenize=false | Nested in links_o. |

## `/component/aw-patterns` — AltWheels Patterns

Four ways to use AI.

- Form: `config/studio/content-types/component/aw-patterns/form-definition.xml`
- Display template: `/templates/web/components/aw-patterns.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| patterns_o | repeat | Patterns | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| patterns_o.number_t | input | Number | false | maxlength=500; tokenize=false | Nested in patterns_o. |
| patterns_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in patterns_o. |
| patterns_o.text_t | input | Text | false | maxlength=500; tokenize=false | Nested in patterns_o. |

## `/component/aw-downloads` — AltWheels Downloads

Download cards.

- Form: `config/studio/content-types/component/aw-downloads/form-definition.xml`
- Display template: `/templates/web/components/aw-downloads.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| eyebrow_t | input | Eyebrow | false | maxlength=500; tokenize=false |  |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| intro_t | textarea | Intro | false | maxlength=4000; tokenize=false | Plain text. |
| cards_o | repeat | Cards | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| cards_o.format_t | input | Format | false | maxlength=500; tokenize=false | Nested in cards_o. |
| cards_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in cards_o. |
| cards_o.text_t | textarea | Text | false | maxlength=4000; tokenize=false | Nested in cards_o. |
| cards_o.buttonLabel_t | input | Button Label | false | maxlength=500; tokenize=false | Nested in cards_o. |
| cards_o.buttonUrl_s | input | Button URL | false | maxlength=500; tokenize=false | Nested in cards_o. |
| cards_o.buttonStyle_s | input | Button Style | false | maxlength=500; tokenize=false | Nested in cards_o. |
| cards_o.download_s | input | Download | false | maxlength=500; tokenize=false | Nested in cards_o. |
| cards_o.note_t | textarea | Note | false | maxlength=4000; tokenize=false | Nested in cards_o. |
| cards_o.noteSmall_s | input | Note Small | false | maxlength=500; tokenize=false | Nested in cards_o. |
| cards_o.noteLabel_t | input | Note Label | false | maxlength=500; tokenize=false | Nested in cards_o. |
| cards_o.noteUrl_s | input | Note URL | false | maxlength=500; tokenize=false | Nested in cards_o. |
| footnote_t | textarea | Footnote | false | maxlength=4000; tokenize=false | Plain text. |

## `/component/aw-prompts` — AltWheels Prompts

Copy-ready prompt list.

- Form: `config/studio/content-types/component/aw-prompts/form-definition.xml`
- Display template: `/templates/web/components/aw-prompts.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| eyebrow_t | input | Eyebrow | false | maxlength=500; tokenize=false |  |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| intro_t | textarea | Intro | false | maxlength=4000; tokenize=false | Plain text. |
| detail_t | textarea | Detail | false | maxlength=4000; tokenize=false | Plain text. |
| packLabel_t | input | Pack Label | false | maxlength=500; tokenize=false |  |
| packUrl_s | input | Pack URL | false | maxlength=500; tokenize=false |  |
| packDownload_s | input | Pack Download | false | maxlength=500; tokenize=false |  |
| prompts_o | repeat | Prompts | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| prompts_o.summary_t | input | Summary | false | maxlength=500; tokenize=false | Nested in prompts_o. |
| prompts_o.prompt_t | textarea | Prompt | false | maxlength=50000; tokenize=false | Nested in prompts_o. |
| prompts_o.promptId_s | input | Prompt ID | false | maxlength=500; tokenize=false | Nested in prompts_o. |
| prompts_o.copyLabel_t | input | Copy Label | false | maxlength=500; tokenize=false | Nested in prompts_o. |
| prompts_o.ariaLabel_t | input | Aria Label | false | maxlength=500; tokenize=false | Nested in prompts_o. |
| prompts_o.fileLabel_t | input | File Label | false | maxlength=500; tokenize=false | Nested in prompts_o. |
| prompts_o.fileUrl_s | input | File URL | false | maxlength=500; tokenize=false | Nested in prompts_o. |

## `/component/aw-templates` — AltWheels Templates

Template downloads and example skill.

- Form: `config/studio/content-types/component/aw-templates/form-definition.xml`
- Display template: `/templates/web/components/aw-templates.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| eyebrow_t | input | Eyebrow | false | maxlength=500; tokenize=false |  |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| intro_t | textarea | Intro | false | maxlength=4000; tokenize=false | Plain text. |
| templates_o | repeat | Templates | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| templates_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in templates_o. |
| templates_o.text_t | textarea | Text | false | maxlength=4000; tokenize=false | Nested in templates_o. |
| templates_o.linkLabel_t | input | Link Label | false | maxlength=500; tokenize=false | Nested in templates_o. |
| templates_o.linkUrl_s | input | Link URL | false | maxlength=500; tokenize=false | Nested in templates_o. |
| templates_o.download_s | input | Download | false | maxlength=500; tokenize=false | Nested in templates_o. |
| skillTitle_t | input | Skill Title | false | maxlength=500; tokenize=false |  |
| skillText_t | textarea | Skill Text | false | maxlength=4000; tokenize=false | Plain text. |
| skillLabel_t | input | Skill Label | false | maxlength=500; tokenize=false |  |
| skillUrl_s | input | Skill URL | false | maxlength=500; tokenize=false |  |
| skillDownload_s | input | Skill Download | false | maxlength=500; tokenize=false |  |

## `/component/aw-callout` — AltWheels Directory Callout

Link to the fleet-tool directory.

- Form: `config/studio/content-types/component/aw-callout/form-definition.xml`
- Display template: `/templates/web/components/aw-callout.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| eyebrow_t | input | Eyebrow | false | maxlength=500; tokenize=false |  |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| text_t | textarea | Text | false | maxlength=4000; tokenize=false | Plain text. |
| linkLabel_t | input | Link Label | false | maxlength=500; tokenize=false |  |
| linkUrl_s | input | Link URL | false | maxlength=500; tokenize=false |  |

## `/component/aw-steps` — AltWheels Steps

First-session steps and share links.

- Form: `config/studio/content-types/component/aw-steps/form-definition.xml`
- Display template: `/templates/web/components/aw-steps.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| eyebrow_t | input | Eyebrow | false | maxlength=500; tokenize=false |  |
| heading_t | input | Heading | false | maxlength=500; tokenize=false |  |
| steps_o | repeat | Steps | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| steps_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in steps_o. |
| steps_o.text_t | textarea | Text | false | maxlength=4000; tokenize=false | Nested in steps_o. |
| noteStrong_t | input | Note Strong | false | maxlength=500; tokenize=false |  |
| note_t | textarea | Note | false | maxlength=4000; tokenize=false | Plain text. |
| qrUrl_s | input | QR URL | false | maxlength=500; tokenize=false |  |
| qrAria_t | input | QR Aria | false | maxlength=500; tokenize=false |  |
| qrImage_s | image-picker | QR Image | false | imageManager=uploadImages,existingImages | Stored path under /static-assets/. |
| qrAlt_t | input | QR Alt | false | maxlength=500; tokenize=false |  |
| qrWidth_s | input | QR Width | false | maxlength=500; tokenize=false |  |
| qrHeight_s | input | QR Height | false | maxlength=500; tokenize=false |  |
| shareTitle_t | input | Share Title | false | maxlength=500; tokenize=false |  |
| siteLabel_t | input | Site Label | false | maxlength=500; tokenize=false |  |
| siteUrl_s | input | Site URL | false | maxlength=500; tokenize=false |  |
| qrFileLabel_t | input | QR File Label | false | maxlength=500; tokenize=false |  |
| qrFileUrl_s | input | QR File URL | false | maxlength=500; tokenize=false |  |
| qrFileDownload_s | input | QR File Download | false | maxlength=500; tokenize=false |  |
| referencesLabel_t | input | References Label | false | maxlength=500; tokenize=false |  |
| referencesUrl_s | input | References URL | false | maxlength=500; tokenize=false |  |
| guideLabel_t | input | Guide Label | false | maxlength=500; tokenize=false |  |
| guideUrl_s | input | Guide URL | false | maxlength=500; tokenize=false |  |
| guideDownload_s | input | Guide Download | false | maxlength=500; tokenize=false |  |

## `/component/resource-intro` — Resource Intro

Back link, heading, and download for a resource page.

- Form: `config/studio/content-types/component/resource-intro/form-definition.xml`
- Display template: `/templates/web/components/resource-intro.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| backLabel_t | input | Back Label | false | maxlength=500; tokenize=false |  |
| backUrl_s | input | Back URL | false | maxlength=500; tokenize=false |  |
| eyebrow_t | input | Eyebrow | false | maxlength=500; tokenize=false |  |
| title_t | input | Title | false | maxlength=500; tokenize=false |  |
| lead_t | textarea | Lead | false | maxlength=4000; tokenize=false | Plain text. |
| buttonLabel_t | input | Button Label | false | maxlength=500; tokenize=false |  |
| buttonUrl_s | input | Button URL | false | maxlength=500; tokenize=false |  |
| download_s | input | Download | false | maxlength=500; tokenize=false |  |
| note_t | textarea | Note | false | maxlength=4000; tokenize=false | Plain text. |

## `/component/tool-directory` — Tool Directory

Grouped fleet tools and a closing link.

- Form: `config/studio/content-types/component/tool-directory/form-definition.xml`
- Display template: `/templates/web/components/tool-directory.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| groups_o | repeat | Groups | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| groups_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in groups_o. |
| groups_o.tools_o | repeat | Tools | false | minOccurs=0; maxOccurs=* | Nested in groups_o. |
| groups_o.tools_o.type_t | input | Type | false | maxlength=500; tokenize=false | Nested in groups_o. |
| groups_o.tools_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in groups_o. |
| groups_o.tools_o.url_s | input | URL | false | maxlength=500; tokenize=false | Nested in groups_o. |
| groups_o.tools_o.text_t | textarea | Text | false | maxlength=4000; tokenize=false | Nested in groups_o. |
| groups_o.tools_o.promptLabel_t | input | Prompt Label | false | maxlength=500; tokenize=false | Nested in groups_o. |
| groups_o.tools_o.prompt_t | textarea | Prompt | false | maxlength=50000; tokenize=false | Nested in groups_o. |
| closingTitle_t | input | Closing Title | false | maxlength=500; tokenize=false |  |
| closingText_t | textarea | Closing Text | false | maxlength=4000; tokenize=false | Plain text. |
| closingLabel_t | input | Closing Label | false | maxlength=500; tokenize=false |  |
| closingUrl_s | input | Closing URL | false | maxlength=500; tokenize=false |  |
| closingDownload_s | input | Closing Download | false | maxlength=500; tokenize=false |  |

## `/component/reference-list` — Reference List

Grouped reference links.

- Form: `config/studio/content-types/component/reference-list/form-definition.xml`
- Display template: `/templates/web/components/reference-list.ftl`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | input | File Name | true | maxlength=50; tokenize=false | |
| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |
| intro_t | textarea | Intro | false | maxlength=4000; tokenize=false | Plain text. |
| groups_o | repeat | Groups | false | minOccurs=0; maxOccurs=* | Repeatable group. |
| groups_o.title_t | input | Title | false | maxlength=500; tokenize=false | Nested in groups_o. |
| groups_o.links_o | repeat | Links | false | minOccurs=0; maxOccurs=* | Nested in groups_o. |
| groups_o.links_o.label_t | input | Label | false | maxlength=500; tokenize=false | Nested in groups_o. |
| groups_o.links_o.url_s | input | URL | false | maxlength=500; tokenize=false | Nested in groups_o. |
| groups_o.links_o.note_t | textarea | Note | false | maxlength=4000; tokenize=false | Nested in groups_o. |
| closingBefore_t | textarea | Closing Before | false | maxlength=4000; tokenize=false | Plain text. |
| closingLabel_t | input | Closing Label | false | maxlength=500; tokenize=false |  |
| closingUrl_s | input | Closing URL | false | maxlength=500; tokenize=false |  |
| closingAfter_t | input | Closing After | false | maxlength=500; tokenize=false |  |

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

