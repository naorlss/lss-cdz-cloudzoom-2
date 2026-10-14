<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="page-hero">
  <div class="page-hero-inner">
    <@crafter.div class="eyebrow-pill" $field="eyebrow_t">${(contentModel.eyebrow_t!"")?html}</@crafter.div>
    <@crafter.h1 $field="title_t">${(contentModel.title_t!"")?html}</@crafter.h1>
    <div class="accent-underline"></div>
    <@crafter.p class="page-hero-subtitle" $field="subtitle_t">${(contentModel.subtitle_t!"")?html}</@crafter.p>
  </div>
</section>
