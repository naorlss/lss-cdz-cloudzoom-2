<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="hero">
  <div class="container hero-grid">
    <div>
      <@crafter.p class="eyebrow" $field="eyebrow_t">${(contentModel.eyebrow_t!"")?html}</@crafter.p>
      <p class="brand-line"><strong>${(contentModel.brandStrong_t!"")?html}</strong><br>${(contentModel.brandRest_t!"")?html}</p>
      <h1>${(contentModel.titleLine1_t!"")?html}<br>${(contentModel.titleLine2_t!"")?html}</h1>
      <@crafter.p class="lead" $field="lead_t">${(contentModel.lead_t!"")?html}</@crafter.p>
      <div class="button-row">
        <#if contentModel.primaryDownload_s! == "true">
          <@crafter.a class="button button-primary" href="${contentModel.primaryUrl_s!}" download="" $field="primaryLabel_t">${(contentModel.primaryLabel_t!"")?html}</@crafter.a>
        <#else>
          <@crafter.a class="button button-primary" href="${contentModel.primaryUrl_s!}" $field="primaryLabel_t">${(contentModel.primaryLabel_t!"")?html}</@crafter.a>
        </#if>
        <@crafter.a class="button button-outline" href="${contentModel.secondaryUrl_s!}" $field="secondaryLabel_t">${(contentModel.secondaryLabel_t!"")?html}</@crafter.a>
      </div>
      <@crafter.p class="meta" $field="meta_t">${(contentModel.meta_t!"")?html}</@crafter.p>
    </div>
    <figure class="preview">
      <a href="${contentModel.imageUrl_s!}" aria-label="${(contentModel.imageAria_t!"")?html}"><img src="${contentModel.image_s!}" alt="${(contentModel.imageAlt_t!"")?html}"<#if contentModel.imageWidth_s?has_content> width="${contentModel.imageWidth_s}"</#if><#if contentModel.imageHeight_s?has_content> height="${contentModel.imageHeight_s}"</#if>></a>
      <figcaption>${(contentModel.caption_t!"")?html}</figcaption>
    </figure>
  </div>
</section>
