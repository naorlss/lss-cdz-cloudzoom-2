<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="section" id="prompts">
  <div class="container split">
    <div class="intro">
      <@crafter.p class="eyebrow" $field="eyebrow_t">${(contentModel.eyebrow_t!"")?html}</@crafter.p>
      <@crafter.h2 $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
      <@crafter.p $field="intro_t">${(contentModel.intro_t!"")?html}</@crafter.p>
      <@crafter.p $field="detail_t">${(contentModel.detail_t!"")?html}</@crafter.p>
      <#if contentModel.packDownload_s! == "true">
        <@crafter.a href="${contentModel.packUrl_s!}" download="" $field="packLabel_t">${(contentModel.packLabel_t!"")?html}</@crafter.a>
      <#else>
        <@crafter.a href="${contentModel.packUrl_s!}" $field="packLabel_t">${(contentModel.packLabel_t!"")?html}</@crafter.a>
      </#if>
    </div>
    <div class="prompt-list">
      <#if contentModel.prompts_o?? && contentModel.prompts_o.item??>
        <@crafter.renderRepeatGroup $field="prompts_o"; prompt, index>
          <details class="prompt">
            <summary>${(prompt.summary_t!"")?html}</summary>
            <div class="prompt-body">
              <pre id="${prompt.promptId_s!}">${(prompt.prompt_t!"")?html}</pre>
              <div class="prompt-actions">
                <button class="button button-light" type="button" data-copy="${prompt.promptId_s!}" aria-label="${(prompt.ariaLabel_t!"")?html}" hidden>${(prompt.copyLabel_t!"")?html}</button>
                <a href="${prompt.fileUrl_s!}" download>${(prompt.fileLabel_t!"")?html}</a>
                <span class="copy-status" role="status" aria-live="polite"></span>
              </div>
            </div>
          </details>
        </@crafter.renderRepeatGroup>
      </#if>
    </div>
  </div>
</section>
