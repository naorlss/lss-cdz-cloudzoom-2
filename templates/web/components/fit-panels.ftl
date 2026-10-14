<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="fit-section">
  <div class="fit-inner">
    <#if contentModel.panels_o?? && contentModel.panels_o.item??>
      <@crafter.renderRepeatGroup $field="panels_o"; panel, panelIndex>
        <div class="fit-panel">
          <@crafter.h2 $field="panels_o.title_t" $index=panelIndex>${(panel.title_t!"")?html}</@crafter.h2>
          <ul class="fit-list">
            <#if panel.items_o?? && panel.items_o.item??>
              <@crafter.renderRepeatGroup $field="panels_o.items_o" $fieldCarryover="panels_o" $indexCarryover="${panelIndex}"; row, rowIndex>
                <li>
                  <i class="${panel.icon_s!}"></i>
                  <@crafter.span $field="panels_o.items_o.text_t" $index="${panelIndex}.${rowIndex}">${(row.text_t!"")?html}</@crafter.span>
                </li>
              </@crafter.renderRepeatGroup>
            </#if>
          </ul>
        </div>
      </@crafter.renderRepeatGroup>
    </#if>
  </div>
</section>
