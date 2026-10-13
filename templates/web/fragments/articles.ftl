<#function czArticles>
  <#local rows = []>
  <#if siteItemService??>
    <#local tree = siteItemService.getSiteTree("/site/website/blog", 2)!>
    <#if tree?has_content && tree.childItems??>
      <#list tree.childItems as child>
        <#local url = (child.storeUrl)!"">
        <#if !url?contains("/index.xml") && url?has_content>
          <#local item = siteItemService.getSiteItem(url + "/index.xml")!>
          <#if item?has_content && (item["content-type"]!"") == "/page/article" && (item.disabled!"false") != "true">
            <#local rows = rows + [item]>
          </#if>
        </#if>
      </#list>
    </#if>
  </#if>
  <#return rows>
</#function>
