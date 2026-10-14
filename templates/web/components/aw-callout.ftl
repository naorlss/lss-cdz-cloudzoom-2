<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="section">
  <div class="container">
    <div class="directory-callout">
      <div>
        <@crafter.p class="eyebrow" $field="eyebrow_t">${(contentModel.eyebrow_t!"")?html}</@crafter.p>
        <@crafter.h2 $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
        <@crafter.p $field="text_t">${(contentModel.text_t!"")?html}</@crafter.p>
      </div>
      <@crafter.a class="button" href="${contentModel.linkUrl_s!}" $field="linkLabel_t">${(contentModel.linkLabel_t!"")?html}</@crafter.a>
    </div>
  </div>
</section>
