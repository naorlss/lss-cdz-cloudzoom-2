<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="section section-white" id="templates">
  <div class="container">
    <div class="section-head">
      <@crafter.p class="eyebrow" $field="eyebrow_t">${(contentModel.eyebrow_t!"")?html}</@crafter.p>
      <@crafter.h2 $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
      <@crafter.p $field="intro_t">${(contentModel.intro_t!"")?html}</@crafter.p>
    </div>
    <div class="template-grid">
      <#if contentModel.templates_o?? && contentModel.templates_o.item??>
        <@crafter.renderRepeatGroup $field="templates_o"; item, index>
          <article class="template">
            <@crafter.h3 $field="templates_o.title_t" $index=index>${(item.title_t!"")?html}</@crafter.h3>
            <@crafter.p $field="templates_o.text_t" $index=index>${(item.text_t!"")?html}</@crafter.p>
            <#if item.download_s! == "true">
              <@crafter.a href="${item.linkUrl_s!}" download="" $field="templates_o.linkLabel_t" $index=index>${(item.linkLabel_t!"")?html}</@crafter.a>
            <#else>
              <@crafter.a href="${item.linkUrl_s!}" $field="templates_o.linkLabel_t" $index=index>${(item.linkLabel_t!"")?html}</@crafter.a>
            </#if>
          </article>
        </@crafter.renderRepeatGroup>
      </#if>
    </div>
    <div class="skill-row">
      <div>
        <@crafter.h3 $field="skillTitle_t">${(contentModel.skillTitle_t!"")?html}</@crafter.h3>
        <@crafter.p $field="skillText_t">${(contentModel.skillText_t!"")?html}</@crafter.p>
      </div>
      <#if contentModel.skillDownload_s! == "true">
        <@crafter.a class="button button-light" href="${contentModel.skillUrl_s!}" download="" $field="skillLabel_t">${(contentModel.skillLabel_t!"")?html}</@crafter.a>
      <#else>
        <@crafter.a class="button button-light" href="${contentModel.skillUrl_s!}" $field="skillLabel_t">${(contentModel.skillLabel_t!"")?html}</@crafter.a>
      </#if>
    </div>
  </div>
</section>
