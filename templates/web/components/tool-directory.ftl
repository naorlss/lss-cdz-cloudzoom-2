<#import "/templates/system/common/crafter.ftl" as crafter />
<div class="container section">
  <#if contentModel.groups_o?? && contentModel.groups_o.item??>
    <@crafter.renderRepeatGroup $field="groups_o"; group, groupIndex>
      <section class="tool-group">
        <@crafter.h2 $field="groups_o.title_t" $index=groupIndex>${(group.title_t!"")?html}</@crafter.h2>
        <div class="tool-list">
          <#if group.tools_o?? && group.tools_o.item??>
            <@crafter.renderRepeatGroup $field="groups_o.tools_o" $fieldCarryover="groups_o" $indexCarryover="${groupIndex}"; tool, toolIndex>
              <article class="tool">
                <@crafter.p class="tool-type" $field="groups_o.tools_o.type_t" $index="${groupIndex}.${toolIndex}">${(tool.type_t!"")?html}</@crafter.p>
                <h3><@crafter.a href="${tool.url_s!}" $field="groups_o.tools_o.title_t" $index="${groupIndex}.${toolIndex}">${(tool.title_t!"")?html}</@crafter.a></h3>
                <p>${(tool.text_t!"")?html}</p>
                <#if tool.promptLabel_t?has_content>
                  <p><strong>${(tool.promptLabel_t!"")?html}</strong> ${(tool.prompt_t!"")?html}</p>
                </#if>
              </article>
            </@crafter.renderRepeatGroup>
          </#if>
        </div>
      </section>
    </@crafter.renderRepeatGroup>
  </#if>
  <section>
    <@crafter.h2 $field="closingTitle_t">${(contentModel.closingTitle_t!"")?html}</@crafter.h2>
    <@crafter.p $field="closingText_t">${(contentModel.closingText_t!"")?html}</@crafter.p>
    <p>
      <#if contentModel.closingDownload_s! == "true">
        <@crafter.a href="${contentModel.closingUrl_s!}" download="" $field="closingLabel_t">${(contentModel.closingLabel_t!"")?html}</@crafter.a>
      <#else>
        <@crafter.a href="${contentModel.closingUrl_s!}" $field="closingLabel_t">${(contentModel.closingLabel_t!"")?html}</@crafter.a>
      </#if>
    </p>
  </section>
</div>
