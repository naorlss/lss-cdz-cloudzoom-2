<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="services-section">
  <div class="services-inner">
    <div class="section-header">
      <@crafter.h2 class="section-title" $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
      <@crafter.p class="section-subtitle" $field="subtitle_t">${(contentModel.subtitle_t!"")?html}</@crafter.p>
    </div>
    <div class="services-grid">
      <#if contentModel.cards_o?? && contentModel.cards_o.item??>
        <@crafter.renderRepeatGroup $field="cards_o"; card, cardIndex>
          <div class="service-card">
            <div class="service-header">
              <i class="${card.icon_s!}"></i>
              <@crafter.span class="service-name" $field="cards_o.title_t" $index=cardIndex>${(card.title_t!"")?html}</@crafter.span>
            </div>
            <@crafter.p class="service-description" $field="cards_o.text_t" $index=cardIndex>${(card.text_t!"")?html}</@crafter.p>
            <#if (card.linkLabel_t!"")?has_content>
              <@crafter.a class="service-card-link" href="${card.linkUrl_s!}" $field="cards_o.linkLabel_t" $index=cardIndex>${(card.linkLabel_t!"")?html} <i class="ph ph-arrow-right"></i></@crafter.a>
            </#if>
          </div>
        </@crafter.renderRepeatGroup>
      </#if>
    </div>
    <div class="services-link">
      <#if contentModel.links_o?? && contentModel.links_o.item??>
        <@crafter.renderRepeatGroup $field="links_o"; link, index>
          <@crafter.a class="ghost-link" href="${link.url_s!}" $field="links_o.label_t" $index=index>${(link.label_t!"")?html} <i class="ph ph-arrow-right"></i></@crafter.a>
        </@crafter.renderRepeatGroup>
      </#if>
    </div>
  </div>
</section>
