<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="hero">
  <div class="hero-inner">
    <div class="hero-content">
      <@crafter.h1 $field="title_t">${(contentModel.title_t!"")?html}</@crafter.h1>
      <div class="accent-underline"></div>
      <@crafter.p class="hero-subtitle" $field="subtitle_t">${(contentModel.subtitle_t!"")?html}</@crafter.p>
      <div class="hero-cta-row">
        <@crafter.a class="cta-button" href="${contentModel.primaryUrl_s!}" $field="primaryLabel_t">${(contentModel.primaryLabel_t!"")?html} <i class="ph ph-arrow-right"></i></@crafter.a>
        <@crafter.a class="ghost-button" href="${contentModel.secondaryUrl_s!}" $field="secondaryLabel_t">${(contentModel.secondaryLabel_t!"")?html}</@crafter.a>
      </div>
      <#if contentModel.chips_o?? && contentModel.chips_o.item??>
        <div class="trust-chips">
          <@crafter.renderRepeatGroup $field="chips_o"; item, index>
            <div class="trust-chip">
              <i class="${item.icon_s!}"></i>
              <@crafter.span $field="chips_o.label_t" $index=index>${(item.label_t!"")?html}</@crafter.span>
            </div>
          </@crafter.renderRepeatGroup>
        </div>
      </#if>
    </div>
    <div class="hero-image">
      <#include "/templates/web/fragments/diagrams/home-hero.ftl">
    </div>
  </div>
</section>
