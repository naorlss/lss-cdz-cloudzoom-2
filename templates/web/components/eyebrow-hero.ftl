<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="hero">
  <div class="hero-inner">
    <@crafter.span class="hero-eyebrow" $field="eyebrow_t">${(contentModel.eyebrow_t!"")?html}</@crafter.span>
    <@crafter.h1 class="hero-heading" $field="title_t">${(contentModel.title_t!"")?html}</@crafter.h1>
    <@crafter.p class="hero-subtitle" $field="subtitle_t">${(contentModel.subtitle_t!"")?html}</@crafter.p>
  </div>
</section>
