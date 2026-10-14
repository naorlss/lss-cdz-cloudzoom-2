<#import "/templates/system/common/crafter.ftl" as crafter />
<nav class="section-nav" aria-label="${(contentModel.ariaLabel_t!"")?html}">
  <div class="container">
    <#if contentModel.links_o?? && contentModel.links_o.item??>
      <@crafter.renderRepeatGroup $field="links_o"; item, index>
        <@crafter.a href="${item.url_s!}" $field="links_o.label_t" $index=index>${(item.label_t!"")?html}</@crafter.a>
      </@crafter.renderRepeatGroup>
    </#if>
  </div>
</nav>
