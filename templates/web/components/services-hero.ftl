<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="hero">
  <div class="hero-container">
    <div class="hero-content">
      <@crafter.span class="hero-eyebrow" $field="eyebrow_t">${(contentModel.eyebrow_t!"")?html}</@crafter.span>
      <@crafter.h1 class="hero-heading" $field="title_t">${(contentModel.title_t!"")?html}</@crafter.h1>
      <p class="hero-subtext">${(contentModel.textBefore_t!"")?html} <@crafter.a href="${contentModel.linkUrl_s!}" style="color:#06B6D4;text-decoration:none;font-weight:700;" $field="linkLabel_t">${(contentModel.linkLabel_t!"")?html}</@crafter.a>${(contentModel.textAfter_t!"")?html}</p>
    </div>
  </div>
</section>
