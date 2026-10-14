<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="story-section">
  <div class="story-section-inner">
    <@crafter.h2 class="story-heading" $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
    <div class="story-content">
      <#if contentModel.paragraphs_o?? && contentModel.paragraphs_o.item??>
        <@crafter.renderRepeatGroup $field="paragraphs_o"; item, index>
          <@crafter.p $field="paragraphs_o.text_t" $index=index>${(item.text_t!"")?html}</@crafter.p>
        </@crafter.renderRepeatGroup>
      </#if>
    </div>
    <div class="stats-block">
      <#if contentModel.stats_o?? && contentModel.stats_o.item??>
        <@crafter.renderRepeatGroup $field="stats_o"; item, index>
          <div class="stat-item">
            <@crafter.div class="stat-value" $field="stats_o.value_t" $index=index>${(item.value_t!"")?html}</@crafter.div>
            <@crafter.div class="stat-label" $field="stats_o.label_t" $index=index>${(item.label_t!"")?html}</@crafter.div>
          </div>
        </@crafter.renderRepeatGroup>
      </#if>
    </div>
  </div>
</section>
