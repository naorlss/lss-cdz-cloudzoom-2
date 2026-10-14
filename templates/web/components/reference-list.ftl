<#import "/templates/system/common/crafter.ftl" as crafter />
<div class="container reading">
  <@crafter.p $field="intro_t">${(contentModel.intro_t!"")?html}</@crafter.p>
  <#if contentModel.groups_o?? && contentModel.groups_o.item??>
    <@crafter.renderRepeatGroup $field="groups_o"; group, groupIndex>
      <section>
        <@crafter.h2 $field="groups_o.title_t" $index=groupIndex>${(group.title_t!"")?html}</@crafter.h2>
        <ul>
          <#if group.links_o?? && group.links_o.item??>
            <@crafter.renderRepeatGroup $field="groups_o.links_o" $fieldCarryover="groups_o" $indexCarryover="${groupIndex}"; link, linkIndex>
              <li>
                <@crafter.a href="${link.url_s!}" $field="groups_o.links_o.label_t" $index="${groupIndex}.${linkIndex}">${(link.label_t!"")?html}</@crafter.a><#if link.note_t?has_content> ${(link.note_t!"")?html}</#if>
              </li>
            </@crafter.renderRepeatGroup>
          </#if>
        </ul>
      </section>
    </@crafter.renderRepeatGroup>
  </#if>
  <#if contentModel.closingLabel_t?has_content>
    <p>${(contentModel.closingBefore_t!"")?html} <@crafter.a href="${contentModel.closingUrl_s!}" $field="closingLabel_t">${(contentModel.closingLabel_t!"")?html}</@crafter.a>${(contentModel.closingAfter_t!"")?html}</p>
  <#elseif contentModel.closingBefore_t?has_content>
    <p>${(contentModel.closingBefore_t!"")?html}</p>
  </#if>
</div>
