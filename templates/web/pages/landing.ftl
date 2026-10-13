<#import "/templates/system/common/crafter.ftl" as crafter />
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${contentModel.title_t!""?html}</title>
  <#if contentModel.seoDescription_t?has_content>
    <meta name="description" content="${contentModel.seoDescription_t?html}">
  </#if>
  ${(contentModel.headLinks_html)!""}
  <#if contentModel.stylesheet_s?has_content>
    <link rel="stylesheet" href="${contentModel.stylesheet_s}">
  </#if>
  <@crafter.head/>
</head>
<body>
<@crafter.body_top/>
<@crafter.renderComponentCollection $field="header_o" renderComponentArguments={ "navKey": (contentModel.navKey_s)!"" } />
<@crafter.renderComponentCollection $field="sections_o" />
<@crafter.renderComponentCollection $field="footer_o" renderComponentArguments={
  "footerTagline": (contentModel.footerTagline_t)!"" ,
  "footerLinkedIn": (contentModel.footerLinkedIn_s)!"" ,
  "footerLegal": (contentModel.footerLegal_s)!""
} />
<@crafter.body_bottom/>
</body>
</html>
