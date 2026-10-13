<#import "/templates/system/common/crafter.ftl" as crafter />
<#assign variant = contentModel.variant_s!"marketing" />
<#assign tagline = contentModel.tagline_t!"" />
<#if footerTagline?? && footerTagline?has_content>
  <#assign tagline = footerTagline />
</#if>
<#assign showLinkedIn = contentModel.showLinkedIn_s!"true" />
<#if footerLinkedIn?? && footerLinkedIn?has_content>
  <#assign showLinkedIn = footerLinkedIn />
</#if>
<#assign showLegal = contentModel.showLegal_s!"true" />
<#if footerLegal?? && footerLegal?has_content>
  <#assign showLegal = footerLegal />
</#if>
<#if variant == "altwheels">
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <a class="brand" href="/"><img src="/static-assets/altwheels/assets/cloudzoom-mark.svg" width="40" height="40" alt=""><span>${contentModel.brand_t!"CloudZoom Solutions"}</span></a>
      <p>AI, Data, Software, IoT</p>
      <p class="tagline">${tagline}</p>
    </div>
    <div>
      <p class="eyebrow">Keep the conversation going</p>
      <a href="mailto:${contentModel.email_t!"bill@cloudzoom.dev"}">${contentModel.email_t!"bill@cloudzoom.dev"}</a><br>
      <a href="${contentModel.phoneUrl_s!"tel:6179213657"}">${contentModel.phone_t!"617.921.3657"}</a><br>
      <a href="/contact">Talk with CloudZoom →</a>
    </div>
  </div>
  <div class="container footer-bottom">${contentModel.copyright_t!""} · <a href="/altwheels">AltWheels resource library</a></div>
</footer>
<#elseif variant == "blog">
<footer class="footer">
  <div class="footer-inner">
    <div>
      <div class="footer-brand-name">${contentModel.brand_t!"CloudZoom Solutions"}</div>
      <p class="footer-brand-desc">${tagline}</p>
    </div>
    <div>
      <p class="footer-col-title">Pages</p>
      <ul class="footer-links">
        <#if contentModel.nav_o?? && contentModel.nav_o.item??>
          <#list contentModel.nav_o.item as item>
            <li><a href="${item.url_s}">${item.label_t}</a></li>
          </#list>
        </#if>
      </ul>
    </div>
    <div>
      <p class="footer-col-title">Connect</p>
      <ul class="footer-links">
        <#if contentModel.connect_o?? && contentModel.connect_o.item??>
          <#list contentModel.connect_o.item as item>
            <li><a href="${item.url_s}"<#if item.url_s?starts_with("http")> target="_blank" rel="noopener"</#if>>${item.label_t}</a></li>
          </#list>
        </#if>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span class="footer-copy">${contentModel.copyright_t!""}</span>
    <span class="footer-email"><a href="mailto:${contentModel.email_t!""}">${contentModel.email_t!""}</a></span>
  </div>
</footer>
<#elseif variant == "article">
<footer class="footer">
  <div class="footer-bottom">
    <span class="footer-copy">${contentModel.copyright_t!""}</span>
    <span class="footer-email"><a href="mailto:${contentModel.email_t!""}">${contentModel.email_t!""}</a></span>
  </div>
</footer>
<#else>
<footer class="footer">
  <div class="footer-inner">
    <div class="footer-logo-section">
      <a href="/" class="footer-logo">
        <div class="logo-icon"><i class="ph ph-cloud-arrow-up"></i></div>
        <span>${contentModel.brand_t!"CloudZoom Solutions"}</span>
      </a>
      <#if tagline?has_content>
        <p class="footer-tagline">${tagline}</p>
      </#if>
    </div>
    <nav class="footer-nav">
      <#if contentModel.nav_o?? && contentModel.nav_o.item??>
        <#list contentModel.nav_o.item as item>
          <a href="${item.url_s}">${item.label_t}</a>
        </#list>
      </#if>
    </nav>
    <div class="footer-contact">
      <#if contentModel.phone_t?has_content>
        <div class="footer-contact-item">
          <i class="ph ph-phone"></i>
          <a href="${contentModel.phoneUrl_s}">${contentModel.phone_t}</a>
        </div>
      </#if>
      <#if contentModel.email_t?has_content>
        <div class="footer-contact-item">
          <i class="ph ph-envelope"></i>
          <a href="mailto:${contentModel.email_t}">${contentModel.email_t}</a>
        </div>
      </#if>
      <#if showLinkedIn == "true" && contentModel.linkedinUrl_s?has_content>
        <div class="footer-contact-item">
          <i class="ph ph-linkedin-logo"></i>
          <a href="${contentModel.linkedinUrl_s}" target="_blank">${contentModel.linkedinLabel_t!"LinkedIn"}</a>
        </div>
      </#if>
    </div>
  </div>
  <#if showLegal == "true">
    <div class="footer-bottom">${contentModel.copyright_t!""}</div>
  </#if>
</footer>
</#if>
