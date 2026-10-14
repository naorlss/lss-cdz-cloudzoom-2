<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="why-section">
  <div class="why-inner">
    <div class="why-content">
      <@crafter.h2 class="section-heading" $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
      <@crafter.p class="section-subheading" $field="subheading_t">${(contentModel.subheading_t!"")?html}</@crafter.p>
      <div class="benefit-list">
        <#if contentModel.items_o?? && contentModel.items_o.item??>
          <@crafter.renderRepeatGroup $field="items_o"; item, index>
            <div class="benefit-item">
              <div class="benefit-icon"><i class="${item.icon_s!}"></i></div>
              <@crafter.div class="benefit-text" $field="items_o.text_t" $index=index>${(item.text_t!"")?html}</@crafter.div>
            </div>
          </@crafter.renderRepeatGroup>
        </#if>
      </div>
    </div>
    <div class="ai-diagram-card">
      <#include "/templates/web/fragments/diagrams/why-section.ftl">
    </div>
  </div>
</section>
