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
          <@crafter.span class="article-tag" $field="tags_o.label_t" $index=tag?index>${(tag.label_t!"")?html}</@crafter.span>
        </#list>
      </div>
    </#if>
    <@crafter.h1 class="article-title" $field="headline_t">${(contentModel.headline_t!"")?html}</@crafter.h1>
    <div class="article-meta">
      <@crafter.span class="article-author" $field="author_t">${(contentModel.author_t!"")?html}</@crafter.span>
      <@crafter.span class="article-date" $field="dateLabel_t">${(contentModel.dateLabel_t!"")?html}</@crafter.span>
      <@crafter.span class="article-read" $field="readTime_t">${(contentModel.readTime_t!"")?html}</@crafter.span>
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
