<#import "/templates/system/common/crafter.ftl" as crafter />
<#include "/templates/web/fragments/articles.ftl">
<#assign layout = contentModel.layout_s!"html" />
<#if layout == "html">
${(contentModel.markup_html)!""}
<#elseif layout == "blog-preview">
<section class="blog-preview">
  <div class="blog-preview-inner">
    <div class="blog-preview-header">
      <div class="section-header">
        <h2 class="section-title">${contentModel.title_t!""?html}</h2>
        <p class="section-subtitle">${contentModel.subtitle_t!""?html}</p>
      </div>
      <a href="${contentModel.linkUrl_s!"/blog"}" class="blog-preview-all">${contentModel.linkLabel_t!"View all articles"} <i class="ph ph-arrow-right"></i></a>
    </div>
    <div class="blog-preview-grid">
      <#list czArticles()?sort_by("homeOrder_s") as post>
        <#if post.showOnHome_s! == "true">
          <a class="blog-card" href="/blog/${post['folder-name']}">
            <div class="blog-card-top">
              <span class="blog-card-tag">${post.homeTag_t!""}</span>
              <#if post.homeIcon_s?has_content><i class="${post.homeIcon_s} blog-card-top-icon"></i></#if>
            </div>
            <div class="blog-card-body">
              <span class="blog-card-meta">${post.homeMeta_t!""}</span>
              <h3 class="blog-card-title">${post.headline_t!""}</h3>
              <p class="blog-card-excerpt">${post.homeExcerpt_t!""}</p>
              <span class="blog-card-link">${post.homeCta_t!"Read article"} <i class="ph ph-arrow-right"></i></span>
            </div>
          </a>
        </#if>
      </#list>
    </div>
  </div>
</section>
<#elseif layout == "article-index">
<section class="articles-section">
  <div class="articles-inner">
    <div class="articles-grid">
      <#list czArticles()?sort_by("sortOrder_s") as post>
        <article class="article-card<#if post.featured_s! == 'true'> featured</#if>">
          <div class="article-card-visual">
            <span class="article-card-visual-label">${post.visualLabel_t!""}</span>
            <#if post.icon_s?has_content><i class="${post.icon_s} article-card-visual-icon"></i></#if>
          </div>
          <div class="article-card-body">
            <div class="article-meta">
              <#if post.listTags_o?? && post.listTags_o.item??>
                <#list post.listTags_o.item as tag>
                  <span class="article-tag">${tag.label_t}</span>
                </#list>
              </#if>
              <span class="article-date">${post.listDate_t!post.dateLabel_t!""}</span>
              <span class="article-read-time">${post.listRead_t!""}</span>
            </div>
            <h2 class="article-title">${post.headline_t!""}</h2>
            <p class="article-excerpt">${post.listExcerpt_t!""}</p>
            <a class="article-read-link" href="/blog/${post['folder-name']}">Read article <i class="ph ph-arrow-right"></i></a>
          </div>
        </article>
      </#list>
    </div>
  </div>
</section>
</#if>
