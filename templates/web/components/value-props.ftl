<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="value-props">
  <div class="value-props-inner">
    <#if contentModel.items_o?? && contentModel.items_o.item??>
      <@crafter.renderRepeatGroup $field="items_o"; item, index>
        <div class="stat-card">
          <div class="stat-icon"><i class="${item.icon_s!}"></i></div>
          <@crafter.div class="stat-number" $field="items_o.title_t" $index=index>${(item.title_t!"")?html}</@crafter.div>
          <@crafter.div class="stat-label" $field="items_o.text_t" $index=index>${(item.text_t!"")?html}</@crafter.div>
        </div>
      </@crafter.renderRepeatGroup>
    </#if>
  </div>
</section>
