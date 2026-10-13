import java.util.regex.Pattern

// groovy.xml.MarkupBuilder is not on the Engine classpath, so the XML is written directly
def pageItems = queryPages(params.route, elasticsearch)
def excludePatterns = getBlackListPatterns(siteConfig)
def port = (request.serverPort == 80 || request.serverPort == 443) ? "" : ":${request.serverPort}"
def base = "${request.scheme}://${request.serverName}${port}"

def out = new StringBuilder()
out << '<?xml version="1.0" encoding="UTF-8"?>\n'
out << '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

pageItems.each { v ->
    def blackListed = v["content-type"] == "/page/redirect" || v.disabled == true || v.disabled == "true"
    if (!blackListed) {
        blackListed = excludePatterns.any { patternAsStr ->
            Pattern.compile(patternAsStr, Pattern.CASE_INSENSITIVE).matcher(v.localId).find()
        }
    }
    if (!blackListed) {
        def renderUrl = urlTransformationService.transform("storeUrlToRenderUrl", v.localId)
        out << '  <url>\n'
        out << "    <loc>${xmlEscape(base + renderUrl)}</loc>\n"
        if (v.lastModifiedDate_dt) {
            out << "    <lastmod>${xmlEscape(v.lastModifiedDate_dt.toString())}</lastmod>\n"
        }
        out << '    <changefreq>weekly</changefreq>\n'
        out << '    <priority>0.8000</priority>\n'
        out << '  </url>\n'
    }
}
out << '</urlset>\n'

response.setContentType("application/xml;charset=UTF-8")
response.writer.write(out.toString())
response.flushBuffer()
return null

def xmlEscape(String s) {
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&apos;")
}

def getBlackListPatterns(siteConfig) {
    def excludePatternsConfig = siteConfig.getStringArray("siteMap.excludes")
    return excludePatternsConfig ? excludePatternsConfig as List : ["^.*level[\\.]xml\$"]
}

def queryPages(route, elasticsearch) {
    def routeFolder = route ?: "/"
    def path = "/site/website" + routeFolder + "*"
    return elasticsearch.search([
        from : 0,
        size : 1000,
        sort : [[localId: [order: "asc"]]],
        query: [bool: [filter: [[wildcard: [localId: path]], [prefix: ["content-type": "/page/"]]]]]
    ]).hits.hits*.sourceAsMap
}
