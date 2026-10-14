<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="contact-section">
  <div class="contact-section-inner">
    <div class="contact-grid">
      <div class="contact-info">
        <@crafter.h2 class="contact-heading" $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
        <@crafter.p class="contact-intro" $field="intro_t">${(contentModel.intro_t!"")?html}</@crafter.p>
        <div class="contact-methods">
          <#if contentModel.methods_o?? && contentModel.methods_o.item??>
            <@crafter.renderRepeatGroup $field="methods_o"; item, index>
              <div class="contact-method">
                <div class="contact-method-icon"><i class="${item.icon_s!}"></i></div>
                <div class="contact-method-details">
                  <@crafter.span class="contact-method-label" $field="methods_o.label_t" $index=index>${(item.label_t!"")?html}</@crafter.span>
                  <span class="contact-method-value">
                    <#if item.url_s?has_content>
                      <@crafter.a href="${item.url_s}" $field="methods_o.value_t" $index=index>${(item.value_t!"")?html}</@crafter.a>
                    <#else>
                      ${(item.value_t!"")?html}
                    </#if>
                  </span>
                </div>
              </div>
            </@crafter.renderRepeatGroup>
          </#if>
        </div>
        <div class="linkedin-section">
          <@crafter.a href="${contentModel.linkedinUrl_s!}" class="linkedin-button" $field="linkedinLabel_t"><i class="ph ph-linkedin-logo"></i>${(contentModel.linkedinLabel_t!"")?html}</@crafter.a>
        </div>
        <div class="cta-box">
          <@crafter.h3 class="cta-box-title" $field="boxTitle_t">${(contentModel.boxTitle_t!"")?html}</@crafter.h3>
          <@crafter.p class="cta-box-text" $field="boxText_t">${(contentModel.boxText_t!"")?html}</@crafter.p>
        </div>
      </div>
      <div class="form-section-inner">
        <@crafter.h2 class="form-heading" $field="formHeading_t">${(contentModel.formHeading_t!"")?html}</@crafter.h2>
        <@crafter.p class="form-subtitle" $field="formSubtitle_t">${(contentModel.formSubtitle_t!"")?html}</@crafter.p>
        <form class="contact-form" action="mailto:${contentModel.formEmail_s!}" method="post" enctype="text/plain">
          <#if contentModel.fields_o?? && contentModel.fields_o.item??>
            <@crafter.renderRepeatGroup $field="fields_o"; field, index>
              <div class="form-group">
                <label class="form-label" for="${field.name_s!}">${(field.label_t!"")?html}</label>
                <#if field.type_s! == "textarea">
                  <textarea id="${field.name_s!}" name="${field.name_s!}" class="form-textarea" placeholder="${(field.placeholder_t!"")?html}"<#if field.required_s! == "true"> required</#if>></textarea>
                <#else>
                  <input type="${field.type_s!}" id="${field.name_s!}" name="${field.name_s!}" class="form-input" placeholder="${(field.placeholder_t!"")?html}"<#if field.required_s! == "true"> required</#if>>
                </#if>
              </div>
            </@crafter.renderRepeatGroup>
          </#if>
          <button type="submit" class="submit-button">${(contentModel.submitLabel_t!"")?html}</button>
        </form>
      </div>
    </div>
  </div>
</section>
