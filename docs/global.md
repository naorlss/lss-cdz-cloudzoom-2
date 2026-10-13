# Level descriptor

Section defaults are inherited by every page below the descriptor. The site root descriptor points at the marketing header and footer. `/site/website/altwheels/` has its own descriptor for the AltWheels header and footer.

## `/component/level-descriptor` — Section Defaults

Section Defaults provides inherited header, footer and popup to all pages below it.

- Form: `config/studio/content-types/component/level-descriptor/form-definition.xml`
- Display template: `(none)`
- Datasources:
  - headerComponents (shared-content) repoPath=/site/components/headers/
  - footerComponents (shared-content) repoPath=/site/components/footers/
  - popupComponents (shared-content) repoPath=/site/components/popups/

| Name | Type | Description | Required | Constraints | Notes |
|------|------|-------------|----------|-------------|-------|
| file-name | file-name | File Name | false | maxlength=50; readonly=true |  |
| internal-name | input | Internal Name | true | maxlength=120 |  |
| header_o | node-selector | Header | false | maxSize=1; itemManager=headerComponents; contentTypes=/component/header | List. Allowed: /component/header. itemManager=headerComponents. |
| footer_o | node-selector | Footer | false | maxSize=1; itemManager=footerComponents; contentTypes=/component/footer | List. Allowed: /component/footer. itemManager=footerComponents. |
| popup_o | node-selector | Popup | false | maxSize=1; itemManager=popupComponents; contentTypes=/component/popup | List. Allowed: /component/popup. itemManager=popupComponents. |
