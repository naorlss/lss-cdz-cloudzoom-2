<#import "/templates/system/common/crafter.ftl" as crafter />
<#include "/templates/web/fragments/articles.ftl">
<section class="articles-section">
  <div class="articles-inner">
    <div class="articles-grid">
      <#list czArticles()?sort_by("sortOrder_s") as post>
        <article class="article-card<#if post.featured_s! == 'true'> featured</#if>">
          <div class="article-card-visual">
            <@crafter.span class="article-card-visual-label" $model=post $field="visualLabel_t">${post.visualLabel_t!""?html}</@crafter.span>
            <#if post.icon_s?has_content><i class="${post.icon_s} article-card-visual-icon"></i></#if>
          </div>
          <div class="article-card-body">
            <div class="article-meta">
              <#if post.listTags_o?? && post.listTags_o.item??>
                <#list post.listTags_o.item as tag>
                  <@crafter.span class="article-tag" $model=post $field="listTags_o.label_t" $index=tag?index>${(tag.label_t!"")?html}</@crafter.span>
                </#list>
              </#if>
              <#if post.listDate_t?has_content>
                <@crafter.span class="article-date" $model=post $field="listDate_t">${post.listDate_t?html}</@crafter.span>
              <#else>
                <@crafter.span class="article-date" $model=post $field="dateLabel_t">${(post.dateLabel_t!"")?html}</@crafter.span>
              </#if>
              <@crafter.span class="article-read-time" $model=post $field="listRead_t">${(post.listRead_t!"")?html}</@crafter.span>
            </div>
            <@crafter.h2 class="article-title" $model=post $field="headline_t">${post.headline_t!""?html}</@crafter.h2>
            <@crafter.p class="article-excerpt" $model=post $field="listExcerpt_t">${post.listExcerpt_t!""?html}</@crafter.p>
            <a class="article-read-link" href="/blog/${post['folder-name']}">Read article <i class="ph ph-arrow-right"></i></a>
          </div>
        </article>
      </#list>
    </div>
  </div>
</section>
