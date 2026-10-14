<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="case-studies-content">
  <div class="case-studies-content-inner">
    <div class="case-studies-stack">
      <#if contentModel.cases_o?? && contentModel.cases_o.item??>
        <@crafter.renderRepeatGroup $field="cases_o"; item, index>
          <#if item.style_s! == "featured">
            <div class="case-featured"><div class="case-featured-content">
          <#else>
            <div class="case-card">
          </#if>
            <#if item.kicker_t?has_content>
              <@crafter.div class="featured-label" $field="cases_o.kicker_t" $index=index>${(item.kicker_t!"")?html}</@crafter.div>
            </#if>
            <#if item.titleTag_s! == "h3">
              <@crafter.h3 class="case-title" $field="cases_o.title_t" $index=index>${(item.title_t!"")?html}</@crafter.h3>
            <#else>
              <@crafter.h2 class="case-title" $field="cases_o.title_t" $index=index>${(item.title_t!"")?html}</@crafter.h2>
            </#if>
            <#if item.badge_t?has_content>
              <@crafter.div class="case-badge" $field="cases_o.badge_t" $index=index>${(item.badge_t!"")?html}</@crafter.div>
            </#if>
            <#if item.linkLabel_t?has_content>
              <#if item.linkTarget_s?has_content>
                <@crafter.a class="case-external-link" href="${item.linkUrl_s!}" target="${item.linkTarget_s}" $field="cases_o.linkLabel_t" $index=index>${(item.linkLabel_t!"")?html} <i class="ph ph-arrow-square-out"></i></@crafter.a>
              <#else>
                <@crafter.a class="case-external-link" href="${item.linkUrl_s!}" $field="cases_o.linkLabel_t" $index=index>${(item.linkLabel_t!"")?html} <i class="ph ph-arrow-square-out"></i></@crafter.a>
              </#if>
            </#if>
            <#if item.statBefore_t?has_content>
              <div class="case-stat">
                <@crafter.span class="stat-before" $field="cases_o.statBefore_t" $index=index>${(item.statBefore_t!"")?html}</@crafter.span>
                <@crafter.span class="stat-arrow" $field="cases_o.statArrow_t" $index=index>${(item.statArrow_t!"")?html}</@crafter.span>
                <@crafter.span class="stat-after" $field="cases_o.statAfter_t" $index=index>${(item.statAfter_t!"")?html}</@crafter.span>
              </div>
            </#if>
            <#if item.stat_t?has_content>
              <@crafter.div class="case-stat-single" $field="cases_o.stat_t" $index=index>${(item.stat_t!"")?html}</@crafter.div>
            </#if>
            <@crafter.p class="case-description" $field="cases_o.text_t" $index=index>${(item.text_t!"")?html}</@crafter.p>
            <div class="tech-tags">
              <#if item.tags_o?? && item.tags_o.item??>
                <@crafter.renderRepeatGroup $field="cases_o.tags_o" $fieldCarryover="cases_o" $indexCarryover="${index}"; tag, tagIndex>
                  <@crafter.span class="tech-tag" $field="cases_o.tags_o.label_t" $index="${index}.${tagIndex}">${(tag.label_t!"")?html}</@crafter.span>
                </@crafter.renderRepeatGroup>
              </#if>
            </div>
          <#if item.style_s! == "featured"></div></#if>
          </div>
        </@crafter.renderRepeatGroup>
      </#if>
      <div class="ai-acceleration-banner">
        <@crafter.div class="ai-banner-title" $field="bannerTitle_t">${(contentModel.bannerTitle_t!"")?html}</@crafter.div>
        <@crafter.p class="ai-banner-text" $field="bannerText_t">${(contentModel.bannerText_t!"")?html}</@crafter.p>
      </div>
    </div>
  </div>
</section>
