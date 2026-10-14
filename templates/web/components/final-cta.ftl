<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="final-cta">
  <div class="final-cta-inner">
    <@crafter.h2 class="final-cta-heading" $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
    <@crafter.p class="final-cta-subtext" $field="subtext_t">${(contentModel.subtext_t!"")?html}</@crafter.p>
    <#assign buttonClass = "secondary-button" />
    <#if contentModel.variant_s! == "home"><#assign buttonClass = "cta-button" /></#if>
    <@crafter.a class="${buttonClass}" href="${contentModel.ctaUrl_s!}" style="font-size: 1.125rem; padding: 1rem 2rem;" $field="ctaLabel_t">${(contentModel.ctaLabel_t!"")?html} <i class="ph ph-arrow-right"></i></@crafter.a>
    <div class="final-cta-contact">
      <@crafter.a href="${contentModel.phoneUrl_s!}" $field="phoneLabel_t">${(contentModel.phoneLabel_t!"")?html}</@crafter.a> | <@crafter.a href="${contentModel.emailUrl_s!}" $field="emailLabel_t">${(contentModel.emailLabel_t!"")?html}</@crafter.a>
    </div>
  </div>
</section>
