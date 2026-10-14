<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="cta-section">
  <#if contentModel.variant_s! == "services">
    <div class="cta-container">
      <@crafter.h2 class="cta-heading" $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
      <#if contentModel.subtext_t?has_content>
        <@crafter.p class="cta-subtext" $field="subtext_t">${(contentModel.subtext_t!"")?html}</@crafter.p>
      </#if>
      <@crafter.a class="cta-button-white" href="${contentModel.ctaUrl_s!}" $field="ctaLabel_t">${(contentModel.ctaLabel_t!"")?html}</@crafter.a>
    </div>
  <#else>
    <div class="cta-inner">
      <@crafter.h2 class="cta-heading" $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
      <#if contentModel.subtext_t?has_content>
        <@crafter.p class="cta-subtext" $field="subtext_t">${(contentModel.subtext_t!"")?html}</@crafter.p>
      </#if>
      <#if contentModel.variant_s! == "about">
        <@crafter.a class="secondary-button" href="${contentModel.ctaUrl_s!}" style="font-size: 1.125rem; padding: 1rem 2rem;" $field="ctaLabel_t">${(contentModel.ctaLabel_t!"")?html} <i class="ph ph-arrow-right"></i></@crafter.a>
      <#else>
        <@crafter.a class="secondary-button" href="${contentModel.ctaUrl_s!}" $field="ctaLabel_t">${(contentModel.ctaLabel_t!"")?html} <i class="ph ph-arrow-right"></i></@crafter.a>
      </#if>
    </div>
  </#if>
</section>
