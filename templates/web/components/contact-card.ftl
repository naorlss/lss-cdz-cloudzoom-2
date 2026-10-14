<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="contact-section">
  <div class="contact-section-inner">
    <@crafter.h2 class="contact-heading" $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
    <div class="contact-details">
      <#if contentModel.items_o?? && contentModel.items_o.item??>
        <@crafter.renderRepeatGroup $field="items_o"; item, index>
          <div class="contact-item">
            <i class="${item.icon_s!}"></i>
            <@crafter.div class="contact-label" $field="items_o.label_t" $index=index>${(item.label_t!"")?html}</@crafter.div>
            <div class="contact-value">
              <#if item.url_s?has_content>
                <@crafter.a href="${item.url_s}" $field="items_o.value_t" $index=index>${(item.value_t!"")?html}</@crafter.a>
              <#else>
                <@crafter.span $field="items_o.value_t" $index=index>${(item.value_t!"")?html}</@crafter.span>
              </#if>
            </div>
          </div>
        </@crafter.renderRepeatGroup>
      </#if>
    </div>
    <div class="contact-linkedin">
      <@crafter.a class="secondary-button" href="${contentModel.linkedinUrl_s!}" $field="linkedinLabel_t"><i class="ph ph-linkedin-logo"></i>${(contentModel.linkedinLabel_t!"")?html}</@crafter.a>
    </div>
    <@crafter.p class="contact-subtext" $field="note_t">${(contentModel.note_t!"")?html}</@crafter.p>
  </div>
</section>
