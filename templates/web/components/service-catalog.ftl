<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="services-section">
  <div class="services-container">
    <@crafter.h2 class="section-heading" $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
    <div class="services-grid">
      <#if contentModel.cards_o?? && contentModel.cards_o.item??>
        <@crafter.renderRepeatGroup $field="cards_o"; card, cardIndex>
          <div class="service-card">
            <div class="service-icon"><i class="${card.icon_s!}"></i></div>
            <@crafter.h3 class="service-title" $field="cards_o.title_t" $index=cardIndex>${(card.title_t!"")?html}</@crafter.h3>
            <@crafter.p class="service-description" $field="cards_o.text_t" $index=cardIndex>${(card.text_t!"")?html}</@crafter.p>
            <div class="service-tags">
              <#if card.tags_o?? && card.tags_o.item??>
                <@crafter.renderRepeatGroup $field="cards_o.tags_o" $fieldCarryover="cards_o" $indexCarryover="${cardIndex}"; tag, tagIndex>
                  <@crafter.span class="service-tag" $field="cards_o.tags_o.label_t" $index="${cardIndex}.${tagIndex}">${(tag.label_t!"")?html}</@crafter.span>
                </@crafter.renderRepeatGroup>
              </#if>
            </div>
          </div>
        </@crafter.renderRepeatGroup>
      </#if>
    </div>
  </div>
</section>
