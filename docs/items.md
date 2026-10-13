# Nested items

This site does not use separate item content types. Repeatable groups inside header, footer, and article content types hold the nested items. Section HTML is stored as one `markup_html` field so the original element tree, classes, and nesting stay intact.

## Header `nav_o`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| label_t | input | Navigation label. | true | maxlength=500 | Child of `nav_o`. |
| url_s | input | Navigation URL. | true | maxlength=500 | Site paths such as `/services`. |
| key_s | input | Key matched to the page `navKey_s` to mark the active link. | false | maxlength=40 | Marketing header only. |

## Footer `nav_o` and `connect_o`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| label_t | input | Link label. | true | maxlength=500 | Child of `nav_o` or `connect_o`. |
| url_s | input | Link URL. | true | maxlength=500 | May be a site path or `mailto:`. |

## Article `tags_o` and `listTags_o`

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| label_t | input | Tag label. | true | maxlength=500 | `tags_o` is the article header. `listTags_o` is the blog index card. |
