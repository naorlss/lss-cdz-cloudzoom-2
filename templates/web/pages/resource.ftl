<#import "/templates/system/common/crafter.ftl" as crafter />
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${contentModel.title_t!""?html}</title>
  <#if contentModel.seoDescription_t?has_content>
    <meta name="description" content="${contentModel.seoDescription_t?html}">
  </#if>
  <link rel="icon" type="image/svg+xml" href="/static-assets/altwheels/assets/cloudzoom-mark.svg">
  ${(contentModel.headLinks_html)!""}
  <#if contentModel.stylesheet_s?has_content>
    <link rel="stylesheet" href="${contentModel.stylesheet_s}">
  </#if>
  <@crafter.head/>
</head>
<body>
<@crafter.body_top/>
<a class="skip-link" href="#main">Skip to content</a>
<@crafter.renderComponentCollection $field="header_o" />
${(contentModel.main_html)!""}
<@crafter.renderComponentCollection $field="footer_o" />
<#if contentModel.script_s?has_content>
  <script src="${contentModel.script_s}" defer></script>
</#if>
<@crafter.body_bottom/>
</body>
</html>
