<#import "/templates/system/common/crafter.ftl" as crafter />
<section class="section section-white" id="downloads">
  <div class="container">
    <div class="section-head">
      <@crafter.p class="eyebrow" $field="eyebrow_t">${(contentModel.eyebrow_t!"")?html}</@crafter.p>
      <@crafter.h2 $field="heading_t">${(contentModel.heading_t!"")?html}</@crafter.h2>
      <@crafter.p $field="intro_t">${(contentModel.intro_t!"")?html}</@crafter.p>
    </div>
    <div class="download-grid">
      <#if contentModel.cards_o?? && contentModel.cards_o.item??>
        <@crafter.renderRepeatGroup $field="cards_o"; card, index>
          <article class="download-card">
            <@crafter.span class="format" $field="cards_o.format_t" $index=index>${(card.format_t!"")?html}</@crafter.span>
            <@crafter.h3 $field="cards_o.title_t" $index=index>${(card.title_t!"")?html}</@crafter.h3>
            <@crafter.p $field="cards_o.text_t" $index=index>${(card.text_t!"")?html}</@crafter.p>
            <#assign buttonClass = "button" />
            <#if card.buttonStyle_s! == "light"><#assign buttonClass = "button button-light" /></#if>
            <#if card.buttonStyle_s! == "primary"><#assign buttonClass = "button button-primary" /></#if>
            <#if card.download_s! == "true">
              <@crafter.a class="${buttonClass}" href="${card.buttonUrl_s!}" download="" $field="cards_o.buttonLabel_t" $index=index>${(card.buttonLabel_t!"")?html}</@crafter.a>
            <#else>
              <@crafter.a class="${buttonClass}" href="${card.buttonUrl_s!}" $field="cards_o.buttonLabel_t" $index=index>${(card.buttonLabel_t!"")?html}</@crafter.a>
            </#if>
            <#assign noteClass = "download-note" />
            <#if card.noteSmall_s! == "true"><#assign noteClass = "download-note small" /></#if>
            <p class="${noteClass}">
              <#if card.noteLabel_t?has_content>
                <@crafter.a href="${card.noteUrl_s!}" $field="cards_o.noteLabel_t" $index=index>${(card.noteLabel_t!"")?html}</@crafter.a>
              <#else>
                ${(card.note_t!"")?html}
              </#if>
            </p>
          </article>
        </@crafter.renderRepeatGroup>
      </#if>
    </div>
    <p class="small download-note">${(contentModel.footnote_t!"")?html}</p>
  </div>
</section>
