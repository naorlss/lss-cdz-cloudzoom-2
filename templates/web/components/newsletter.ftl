<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="newsletter-section">
  <div class="newsletter-inner">
    <@crafter.h2 class="newsletter-title" $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
    <@crafter.p class="newsletter-sub" $field="subtext_t">${(contentModel.subtext_t!"")?html}</@crafter.p>
    <@crafter.a class="cta-button" href="${contentModel.ctaUrl_s!}" style="display:inline-flex;align-items:center;gap:8px;padding:14px 28px;background:linear-gradient(135deg,#06B6D4,#0EA5E9);color:white;text-decoration:none;border-radius:8px;font-weight:700;font-size:14px;" $field="ctaLabel_t">${(contentModel.ctaLabel_t!"")?html} <i class="ph ph-arrow-right"></i></@crafter.a>
    <@crafter.p class="newsletter-note" $field="note_t">${(contentModel.note_t!"")?html}</@crafter.p>
  </div>
</section>
