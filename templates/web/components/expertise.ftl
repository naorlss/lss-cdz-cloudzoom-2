<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="expertise-section">
  <div class="expertise-section-inner">
    <@crafter.h2 class="expertise-heading" $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
    <div class="expertise-grid">
      <#if contentModel.chips_o?? && contentModel.chips_o.item??>
        <@crafter.renderRepeatGroup $field="chips_o"; item, index>
          <div class="expertise-chip">
            <i class="${item.icon_s!}"></i>
            <@crafter.span $field="chips_o.label_t" $index=index>${(item.label_t!"")?html}</@crafter.span>
          </div>
        </@crafter.renderRepeatGroup>
      </#if>
    </div>
  </div>
</section>
