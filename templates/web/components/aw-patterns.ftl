<#import "/templates/system/common/crafter.ftl" as crafter />
<div class="container patterns">
  <#if contentModel.patterns_o?? && contentModel.patterns_o.item??>
    <@crafter.renderRepeatGroup $field="patterns_o"; item, index>
      <section class="pattern">
        <@crafter.span class="number" $field="patterns_o.number_t" $index=index>${(item.number_t!"")?html}</@crafter.span>
        <@crafter.h2 $field="patterns_o.title_t" $index=index>${(item.title_t!"")?html}</@crafter.h2>
        <@crafter.p $field="patterns_o.text_t" $index=index>${(item.text_t!"")?html}</@crafter.p>
      </section>
    </@crafter.renderRepeatGroup>
  </#if>
</div>
