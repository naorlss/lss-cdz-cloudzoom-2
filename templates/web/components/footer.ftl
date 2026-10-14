<#import "/templates/system/common/crafter.ftl" as crafter />
<#assign variant = contentModel.variant_s!"marketing" />
<#assign tagline = contentModel.tagline_t!"" />
<#assign taglineFromPage = footerTagline?? && footerTagline?has_content />
<#if taglineFromPage>
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
      <a class="brand" href="/"><img src="/static-assets/altwheels/assets/cloudzoom-mark.svg" width="40" height="40" alt=""><@crafter.span $field="brand_t">${(contentModel.brand_t!"CloudZoom Solutions")?html}</@crafter.span></a>
      <p>AI, Data, Software, IoT</p>
      <#if taglineFromPage>
        <p class="tagline">${tagline?html}</p>
      <#else>
        <@crafter.p class="tagline" $field="tagline_t">${(contentModel.tagline_t!"")?html}</@crafter.p>
      </#if>
    </div>
    <div>
      <p class="eyebrow">Keep the conversation going</p>
      <@crafter.a href="mailto:${contentModel.email_t!'bill@cloudzoom.dev'}" $field="email_t">${(contentModel.email_t!"bill@cloudzoom.dev")?html}</@crafter.a><br>
      <@crafter.a href="${contentModel.phoneUrl_s!'tel:6179213657'}" $field="phone_t">${(contentModel.phone_t!"617.921.3657")?html}</@crafter.a><br>
      <a href="/contact">Talk with CloudZoom →</a>
    </div>
  </div>
  <div class="container footer-bottom"><@crafter.span $field="copyright_t">${(contentModel.copyright_t!"")?html}</@crafter.span> · <a href="/altwheels">AltWheels resource library</a></div>
</footer>
<#elseif variant == "blog">
<footer class="footer">
  <div class="footer-inner">
    <div>
      <@crafter.div class="footer-brand-name" $field="brand_t">${(contentModel.brand_t!"CloudZoom Solutions")?html}</@crafter.div>
      <#if taglineFromPage>
        <p class="footer-brand-desc">${tagline?html}</p>
      <#else>
        <@crafter.p class="footer-brand-desc" $field="tagline_t">${(contentModel.tagline_t!"")?html}</@crafter.p>
      </#if>
    </div>
    <div>
      <p class="footer-col-title">Pages</p>
      <ul class="footer-links">
        <#if contentModel.nav_o?? && contentModel.nav_o.item??>
          <#list contentModel.nav_o.item as item>
            <li><@crafter.a href="${item.url_s!}" $field="nav_o.label_t" $index=item?index>${(item.label_t!"")?html}</@crafter.a></li>
          </#list>
        </#if>
      </ul>
    </div>
    <div>
      <p class="footer-col-title">Connect</p>
      <ul class="footer-links">
        <#if contentModel.connect_o?? && contentModel.connect_o.item??>
          <#list contentModel.connect_o.item as item>
            <li>
              <#if (item.url_s!"")?starts_with("http")>
                <@crafter.a href="${item.url_s!}" target="_blank" rel="noopener" $field="connect_o.label_t" $index=item?index>${(item.label_t!"")?html}</@crafter.a>
              <#else>
                <@crafter.a href="${item.url_s!}" $field="connect_o.label_t" $index=item?index>${(item.label_t!"")?html}</@crafter.a>
              </#if>
            </li>
          </#list>
        </#if>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <@crafter.span class="footer-copy" $field="copyright_t">${(contentModel.copyright_t!"")?html}</@crafter.span>
    <span class="footer-email"><@crafter.a href="mailto:${contentModel.email_t!}" $field="email_t">${(contentModel.email_t!"")?html}</@crafter.a></span>
  </div>
</footer>
<#elseif variant == "article">
<footer class="footer">
  <div class="footer-bottom">
    <@crafter.span class="footer-copy" $field="copyright_t">${(contentModel.copyright_t!"")?html}</@crafter.span>
    <span class="footer-email"><@crafter.a href="mailto:${contentModel.email_t!}" $field="email_t">${(contentModel.email_t!"")?html}</@crafter.a></span>
  </div>
</footer>
<#else>
<footer class="footer">
  <div class="footer-inner">
    <div class="footer-logo-section">
      <a href="/" class="footer-logo">
        <div class="logo-icon"><i class="ph ph-cloud-arrow-up"></i></div>
        <@crafter.span $field="brand_t">${(contentModel.brand_t!"CloudZoom Solutions")?html}</@crafter.span>
      </a>
      <#if tagline?has_content>
        <#if taglineFromPage>
          <p class="footer-tagline">${tagline?html}</p>
        <#else>
          <@crafter.p class="footer-tagline" $field="tagline_t">${(contentModel.tagline_t!"")?html}</@crafter.p>
        </#if>
      </#if>
    </div>
    <nav class="footer-nav">
      <#if contentModel.nav_o?? && contentModel.nav_o.item??>
        <#list contentModel.nav_o.item as item>
          <@crafter.a href="${item.url_s!}" $field="nav_o.label_t" $index=item?index>${(item.label_t!"")?html}</@crafter.a>
        </#list>
      </#if>
    </nav>
    <div class="footer-contact">
      <#if contentModel.phone_t?has_content>
        <div class="footer-contact-item">
          <i class="ph ph-phone"></i>
          <@crafter.a href="${contentModel.phoneUrl_s!}" $field="phone_t">${(contentModel.phone_t!"")?html}</@crafter.a>
        </div>
      </#if>
      <#if contentModel.email_t?has_content>
        <div class="footer-contact-item">
          <i class="ph ph-envelope"></i>
          <@crafter.a href="mailto:${contentModel.email_t}" $field="email_t">${(contentModel.email_t!"")?html}</@crafter.a>
        </div>
      </#if>
      <#if showLinkedIn == "true" && contentModel.linkedinUrl_s?has_content>
        <div class="footer-contact-item">
          <i class="ph ph-linkedin-logo"></i>
          <@crafter.a href="${contentModel.linkedinUrl_s!}" target="_blank" $field="linkedinLabel_t">${(contentModel.linkedinLabel_t!"LinkedIn")?html}</@crafter.a>
        </div>
      </#if>
    </div>
  </div>
  <#if showLegal == "true">
    <@crafter.div class="footer-bottom" $field="copyright_t">${(contentModel.copyright_t!"")?html}</@crafter.div>
  </#if>
</footer>
</#if>
