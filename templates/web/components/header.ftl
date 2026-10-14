<#import "/templates/system/common/crafter.ftl" as crafter />
<#assign active = (navKey)!"" />
<#if contentModel.variant_s! == "altwheels">
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="/"><img src="/static-assets/altwheels/assets/cloudzoom-mark.svg" width="40" height="40" alt=""><@crafter.span $field="brand_t">${(contentModel.brand_t!"CloudZoom Solutions")?html}</@crafter.span></a>
    <nav class="desktop-nav" aria-label="CloudZoom">
      <#if contentModel.nav_o?? && contentModel.nav_o.item??>
        <#list contentModel.nav_o.item as item>
          <@crafter.a href="${item.url_s!}" $field="nav_o.label_t" $index=item?index>${(item.label_t!"")?html}</@crafter.a>
        </#list>
      </#if>
    </nav>
    <details class="mobile-nav">
      <summary>Menu</summary>
      <nav aria-label="CloudZoom mobile">
        <#if contentModel.nav_o?? && contentModel.nav_o.item??>
          <#list contentModel.nav_o.item as item>
            <@crafter.a href="${item.url_s!}" $field="nav_o.label_t" $index=item?index>${(item.label_t!"")?html}</@crafter.a>
          </#list>
        </#if>
      </nav>
    </details>
  </div>
</header>
<#else>
<nav class="top-nav">
  <div class="top-nav-inner">
    <a href="/" class="logo">
      <div class="logo-icon"><i class="ph ph-cloud-arrow-up"></i></div>
      <@crafter.span $field="brand_t">${(contentModel.brand_t!"CloudZoom Solutions")?html}</@crafter.span>
    </a>
    <div class="nav-links">
      <#if contentModel.nav_o?? && contentModel.nav_o.item??>
        <#list contentModel.nav_o.item as item>
          <#if active == (item.key_s!"")>
            <@crafter.a href="${item.url_s!}" class="active" $field="nav_o.label_t" $index=item?index>${(item.label_t!"")?html}</@crafter.a>
          <#else>
            <@crafter.a href="${item.url_s!}" $field="nav_o.label_t" $index=item?index>${(item.label_t!"")?html}</@crafter.a>
          </#if>
        </#list>
      </#if>
      <#if contentModel.ctaLabel_t?has_content>
        <@crafter.a href="${contentModel.ctaUrl_s!'/contact'}" class="cta-button" $field="ctaLabel_t">${(contentModel.ctaLabel_t!"")?html} <i class="ph ph-arrow-right"></i></@crafter.a>
      </#if>
    </div>
  </div>
</nav>
</#if>
