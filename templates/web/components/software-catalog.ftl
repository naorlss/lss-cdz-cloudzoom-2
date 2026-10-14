<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="software-section">
  <div class="software-inner">
    <div class="section-header">
      <@crafter.div class="section-kicker" $field="kicker_t">${(contentModel.kicker_t!"")?html}</@crafter.div>
      <@crafter.h2 class="section-heading" $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
      <@crafter.p class="section-subtitle" $field="subtitle_t">${(contentModel.subtitle_t!"")?html}</@crafter.p>
    </div>
    <div class="software-grid">
      <#if contentModel.cards_o?? && contentModel.cards_o.item??>
        <@crafter.renderRepeatGroup $field="cards_o"; card, cardIndex>
          <article class="software-card">
            <div class="software-icon"><i class="${card.icon_s!}"></i></div>
            <@crafter.h3 class="software-title" $field="cards_o.title_t" $index=cardIndex>${(card.title_t!"")?html}</@crafter.h3>
            <@crafter.p class="software-description" $field="cards_o.text_t" $index=cardIndex>${(card.text_t!"")?html}</@crafter.p>
            <div class="software-tags">
              <#if card.tags_o?? && card.tags_o.item??>
                <@crafter.renderRepeatGroup $field="cards_o.tags_o" $fieldCarryover="cards_o" $indexCarryover="${cardIndex}"; tag, tagIndex>
                  <@crafter.span class="software-tag" $field="cards_o.tags_o.label_t" $index="${cardIndex}.${tagIndex}">${(tag.label_t!"")?html}</@crafter.span>
                </@crafter.renderRepeatGroup>
              </#if>
            </div>
          </article>
        </@crafter.renderRepeatGroup>
      </#if>
    </div>
  </div>
</section>
