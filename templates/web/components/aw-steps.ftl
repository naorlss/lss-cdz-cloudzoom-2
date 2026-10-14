<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="section section-white">
  <div class="container">
    <div class="section-head">
      <@crafter.p class="eyebrow" $field="eyebrow_t">${(contentModel.eyebrow_t!"")?html}</@crafter.p>
      <@crafter.h2 $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
    </div>
    <ol class="steps">
      <#if contentModel.steps_o?? && contentModel.steps_o.item??>
        <@crafter.renderRepeatGroup $field="steps_o"; step, index>
          <li>
            <@crafter.h3 $field="steps_o.title_t" $index=index>${(step.title_t!"")?html}</@crafter.h3>
            <@crafter.p $field="steps_o.text_t" $index=index>${(step.text_t!"")?html}</@crafter.p>
          </li>
        </@crafter.renderRepeatGroup>
      </#if>
    </ol>
    <p class="note"><strong>${(contentModel.noteStrong_t!"")?html}</strong> ${(contentModel.note_t!"")?html}</p>
    <div class="share-row">
      <a href="${contentModel.qrUrl_s!}"<#if contentModel.qrAria_t?has_content> aria-label="${contentModel.qrAria_t?html}"</#if>><img src="${contentModel.qrImage_s!}" alt="${(contentModel.qrAlt_t!"")?html}"<#if contentModel.qrWidth_s?has_content> width="${contentModel.qrWidth_s}"</#if><#if contentModel.qrHeight_s?has_content> height="${contentModel.qrHeight_s}"</#if>></a>
      <div>
        <@crafter.h3 $field="shareTitle_t">${(contentModel.shareTitle_t!"")?html}</@crafter.h3>
        <p>
          <a href="${contentModel.siteUrl_s!}">${(contentModel.siteLabel_t!"")?html}</a><br>
          <a href="${contentModel.qrFileUrl_s!}"<#if contentModel.qrFileDownload_s! == "true"> download</#if>>${(contentModel.qrFileLabel_t!"")?html}</a>
          ·
          <a href="${contentModel.referencesUrl_s!}">${(contentModel.referencesLabel_t!"")?html}</a>
          ·
          <a href="${contentModel.guideUrl_s!}"<#if contentModel.guideDownload_s! == "true"> download</#if>>${(contentModel.guideLabel_t!"")?html}</a>
        </p>
      </div>
    </div>
  </div>
</section>
