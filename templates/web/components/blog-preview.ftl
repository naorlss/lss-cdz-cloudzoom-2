<#import "/templates/system/common/crafter.ftl" as crafter />
<#include "/templates/web/fragments/articles.ftl">
<section class="blog-preview">
  <div class="blog-preview-inner">
    <div class="blog-preview-header">
      <div class="section-header">
        <@crafter.h2 class="section-title" $field="title_t">${(contentModel.title_t!"")?html}</@crafter.h2>
        <@crafter.p class="section-subtitle" $field="subtitle_t">${(contentModel.subtitle_t!"")?html}</@crafter.p>
      </div>
      <@crafter.a href="${contentModel.linkUrl_s!'/blog'}" class="blog-preview-all" $field="linkLabel_t">${(contentModel.linkLabel_t!'View all articles')?html} <i class="ph ph-arrow-right"></i></@crafter.a>
    </div>
    <div class="blog-preview-grid">
      <#list czArticles()?sort_by("homeOrder_s") as post>
        <#if post.showOnHome_s! == "true">
          <a class="blog-card" href="/blog/${post['folder-name']}">
            <div class="blog-card-top">
              <@crafter.span class="blog-card-tag" $model=post $field="homeTag_t">${post.homeTag_t!""?html}</@crafter.span>
              <#if post.homeIcon_s?has_content><i class="${post.homeIcon_s} blog-card-top-icon"></i></#if>
            </div>
            <div class="blog-card-body">
              <@crafter.span class="blog-card-meta" $model=post $field="homeMeta_t">${post.homeMeta_t!""?html}</@crafter.span>
              <@crafter.h3 class="blog-card-title" $model=post $field="headline_t">${post.headline_t!""?html}</@crafter.h3>
              <@crafter.p class="blog-card-excerpt" $model=post $field="homeExcerpt_t">${post.homeExcerpt_t!""?html}</@crafter.p>
              <span class="blog-card-link">${(post.homeCta_t!'Read article')?html} <i class="ph ph-arrow-right"></i></span>
            </div>
          </a>
        </#if>
      </#list>
    </div>
  </div>
</section>
