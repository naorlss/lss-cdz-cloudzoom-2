<#import "/templates/system/common/crafter.ftl" as crafter />
<div class="page-intro">
  <div class="container">
    <@crafter.a class="back-link" href="${contentModel.backUrl_s!}" $field="backLabel_t">${(contentModel.backLabel_t!"")?html}</@crafter.a>
    <@crafter.p class="eyebrow" $field="eyebrow_t">${(contentModel.eyebrow_t!"")?html}</@crafter.p>
    <@crafter.h1 $field="title_t">${(contentModel.title_t!"")?html}</@crafter.h1>
    <@crafter.p $field="lead_t">${(contentModel.lead_t!"")?html}</@crafter.p>
    <#if contentModel.download_s! == "true">
      <@crafter.a class="button" href="${contentModel.buttonUrl_s!}" download="" $field="buttonLabel_t">${(contentModel.buttonLabel_t!"")?html}</@crafter.a>
    <#else>
      <@crafter.a class="button" href="${contentModel.buttonUrl_s!}" $field="buttonLabel_t">${(contentModel.buttonLabel_t!"")?html}</@crafter.a>
    </#if>
    <#if contentModel.note_t?has_content>
      <p class="small download-note">${(contentModel.note_t!"")?html}</p>
    </#if>
  </div>
</div>
