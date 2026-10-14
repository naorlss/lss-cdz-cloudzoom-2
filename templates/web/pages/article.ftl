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
  <#include "/templates/web/fragments/head-article.ftl">
  <#if contentModel.stylesheet_s?has_content>
    <link rel="stylesheet" href="${contentModel.stylesheet_s}">
  </#if>
  <@crafter.head/>
</head>
<body>
<@crafter.body_top/>
<@crafter.renderComponentCollection $field="header_o" renderComponentArguments={ "navKey": (contentModel.navKey_s)!"blog" } />
<#if contentModel.wrap_s! == "main"><main></#if>
<header class="article-header">
  <div class="article-header-inner">
    <a href="/blog" class="back-link"><i class="ph ph-arrow-left"></i> Back to Blog</a>
    <#if contentModel.tags_o?? && contentModel.tags_o.item??>
      <div class="article-tags">
        <#list contentModel.tags_o.item as tag>
          <span class="article-tag">${tag.label_t!""?html}</span>
        </#list>
      </div>
    </#if>
    <h1 class="article-title">${contentModel.headline_t!""?html}</h1>
    <div class="article-meta">
      <span class="article-author">${contentModel.author_t!""?html}</span>
      <span class="article-date">${contentModel.dateLabel_t!""?html}</span>
      <span class="article-read">${contentModel.readTime_t!""?html}</span>
    </div>
  </div>
</header>
<article class="article-body">
<@crafter.div $field="body_html">${contentModel.body_html!""}</@crafter.div>
</article>
<#if contentModel.wrap_s! == "main"></main></#if>
<@crafter.renderComponentCollection $field="footer_o" />
<@crafter.body_bottom/>
</body>
</html>
