<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="process-section">
  <div class="process-inner">
    <div class="section-header">
      <@crafter.div class="section-kicker" $field="kicker_t">${(contentModel.kicker_t!"")?html}</@crafter.div>
      <@crafter.h2 class="section-heading" $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
      <@crafter.p class="section-subtitle" $field="subtitle_t">${(contentModel.subtitle_t!"")?html}</@crafter.p>
    </div>
    <div class="process-grid">
      <#if contentModel.steps_o?? && contentModel.steps_o.item??>
        <@crafter.renderRepeatGroup $field="steps_o"; step, index>
          <div class="process-step">
            <@crafter.div class="process-step-number" $field="steps_o.number_t" $index=index>${(step.number_t!"")?html}</@crafter.div>
            <@crafter.h3 $field="steps_o.title_t" $index=index>${(step.title_t!"")?html}</@crafter.h3>
            <@crafter.p $field="steps_o.text_t" $index=index>${(step.text_t!"")?html}</@crafter.p>
          </div>
        </@crafter.renderRepeatGroup>
      </#if>
    </div>
  </div>
</section>
