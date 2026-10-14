<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="ai-banner">
  <div class="ai-banner-container">
    <div class="ai-content">
      <@crafter.h2 $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
      <ul class="ai-benefits">
        <#if contentModel.items_o?? && contentModel.items_o.item??>
          <@crafter.renderRepeatGroup $field="items_o"; item, index>
            <li class="ai-benefit-item">
              <i class="${item.icon_s!}"></i>
              <span class="ai-benefit-text"><strong><@crafter.span $field="items_o.title_t" $index=index>${(item.title_t!"")?html}</@crafter.span></strong> ${(item.text_t!"")?html}</span>
            </li>
          </@crafter.renderRepeatGroup>
        </#if>
      </ul>
    </div>
    <div class="ai-visual">
      <#include "/templates/web/fragments/diagrams/ai-banner.ftl">
    </div>
  </div>
</section>
