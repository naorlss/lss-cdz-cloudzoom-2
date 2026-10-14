<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="social-proof">
  <div class="social-proof-inner">
    <div class="founder-info">
      <@crafter.div class="founder-avatar" $field="avatar_t">${(contentModel.avatar_t!"")?html}</@crafter.div>
      <div class="founder-details">
        <@crafter.div class="founder-name" $field="name_t">${(contentModel.name_t!"")?html}</@crafter.div>
        <@crafter.div class="founder-title" $field="role_t">${(contentModel.role_t!"")?html}</@crafter.div>
      </div>
    </div>
    <@crafter.div class="quote-text" $field="quote_t">${(contentModel.quote_t!"")?html}</@crafter.div>
    <div class="logos-strip">
      <#if contentModel.logos_o?? && contentModel.logos_o.item??>
        <@crafter.renderRepeatGroup $field="logos_o"; item, index>
          <@crafter.div class="logo-item" $field="logos_o.label_t" $index=index>${(item.label_t!"")?html}</@crafter.div>
        </@crafter.renderRepeatGroup>
      </#if>
    </div>
  </div>
</section>
