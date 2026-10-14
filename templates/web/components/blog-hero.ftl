<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="blog-hero">
  <div class="blog-hero-inner">
    <@crafter.p class="blog-hero-eyebrow" $field="eyebrow_t">${(contentModel.eyebrow_t!"")?html}</@crafter.p>
    <h1 class="blog-hero-title">${(contentModel.titleLine1_t!"")?html}<br>${(contentModel.titleLine2_t!"")?html}</h1>
    <@crafter.p class="blog-hero-sub" $field="subtitle_t">${(contentModel.subtitle_t!"")?html}</@crafter.p>
  </div>
</section>
