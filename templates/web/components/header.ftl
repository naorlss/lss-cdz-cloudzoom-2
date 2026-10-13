<#import "/templates/system/common/crafter.ftl" as crafter />
<#assign active = (navKey)!"" />
<#if contentModel.variant_s! == "altwheels">
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="/"><img src="/static-assets/altwheels/assets/cloudzoom-mark.svg" width="40" height="40" alt=""><span>${contentModel.brand_t!"CloudZoom Solutions"}</span></a>
    <nav class="desktop-nav" aria-label="CloudZoom">
      <#if contentModel.nav_o?? && contentModel.nav_o.item??>
        <#list contentModel.nav_o.item as item>
          <a href="${item.url_s}">${item.label_t}</a>
        </#list>
      </#if>
    </nav>
    <details class="mobile-nav">
      <summary>Menu</summary>
      <nav aria-label="CloudZoom mobile">
        <#if contentModel.nav_o?? && contentModel.nav_o.item??>
          <#list contentModel.nav_o.item as item>
            <a href="${item.url_s}">${item.label_t}</a>
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
      <span>${contentModel.brand_t!"CloudZoom Solutions"}</span>
    </a>
    <div class="nav-links">
      <#if contentModel.nav_o?? && contentModel.nav_o.item??>
        <#list contentModel.nav_o.item as item>
          <a href="${item.url_s}"<#if active == (item.key_s!"")> class="active"</#if>>${item.label_t}</a>
        </#list>
      </#if>
      <#if contentModel.ctaLabel_t?has_content>
        <a href="${contentModel.ctaUrl_s!"/contact"}" class="cta-button">${contentModel.ctaLabel_t} <i class="ph ph-arrow-right"></i></a>
      </#if>
    </div>
  </div>
</nav>
</#if>
