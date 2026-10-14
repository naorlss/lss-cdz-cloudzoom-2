#!/usr/bin/env python3
"""Build the CloudZoom CrafterCMS site from the mirrored cloudzoom.dev pages.

The marketing and AltWheels bodies keep the live markup (so the imported CSS
matches), with links rewritten to Crafter URLs. Navigation, footers, page
metadata and articles are real content items.
"""

from __future__ import annotations

import hashlib
import re
import shutil
import uuid
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
MIRROR = Path("/tmp/cz/mirror")
NS = uuid.UUID("6ba7b811-9dad-11d1-80b4-00c04fd430c8")
DATE = "2026-10-05T14:01:03.000Z"

PAGES = [
    "index.html",
    "services.html",
    "software.html",
    "work.html",
    "about.html",
    "contact.html",
    "blog.html",
]

ARTICLES = [
    "blog/altwheels-fleet-day-2026-ai-resources.html",
    "blog/role-based-ai-qa-agents-cleaning-platform.html",
    "blog/exponential-growth-of-ai-software-industry.html",
    "blog/ai-agents-replacing-manual-workflows.html",
    "blog/iot-for-small-business-costs-and-roi.html",
]

RESOURCE_PAGES = [
    "altwheels/index.html",
    "altwheels/fleet-tools.html",
    "altwheels/references.html",
]


def oid(key: str) -> str:
    return str(uuid.uuid5(NS, "lss-smp-cloudzoom:" + key))


def cdata(value: str) -> str:
    value = value.replace("]]>", "]]]]><![CDATA[>")
    return f"<![CDATA[{value}]]>"


def field(name: str, value: str | None) -> str:
    if value is None:
        value = ""
    return f"\t<{name}>{cdata(value)}</{name}>"


def repeat(name: str, rows: list[dict]) -> str:
    lines = [f"\t<{name} item-list=\"true\">"]
    for row in rows:
        lines.append("\t\t<item>")
        for key, value in row.items():
            lines.append(f"\t\t\t<{key}>{cdata('' if value is None else str(value))}</{key}>")
        lines.append("\t\t</item>")
    lines.append(f"\t</{name}>")
    return "\n".join(lines)


def node_list(name: str, items: list[tuple[str, str]]) -> str:
    lines = [f"\t<{name} item-list=\"true\">"]
    for path, label in items:
        lines.append("\t\t<item>")
        lines.append(f"\t\t\t<key>{path}</key>")
        lines.append(f"\t\t\t<value>{cdata(label)}</value>")
        lines.append(f"\t\t\t<include>{path}</include>")
        lines.append("\t\t\t<disableFlattening>false</disableFlattening>")
        lines.append("\t\t</item>")
    lines.append(f"\t</{name}>")
    return "\n".join(lines)


def component_xml(ctype: str, template: str, filename: str, internal: str, key: str, body: str) -> str:
    ident = oid(key)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<component>
\t<content-type>{ctype}</content-type>
\t<display-template>{template}</display-template>
\t<no-template-required></no-template-required>
\t<merge-strategy>inherit-levels</merge-strategy>
\t<objectGroupId>{ident[:4]}</objectGroupId>
\t<objectId>{ident}</objectId>
\t<file-name>{filename}</file-name>
\t<folder-name></folder-name>
\t<internal-name>{cdata(internal)}</internal-name>
\t<createdDate>{DATE}</createdDate>
\t<createdDate_dt>{DATE}</createdDate_dt>
\t<lastModifiedDate>{DATE}</lastModifiedDate>
\t<lastModifiedDate_dt>{DATE}</lastModifiedDate_dt>
{body}
</component>
"""


def page_xml(ctype: str, template: str, filename: str, folder: str, internal: str, key: str, body: str) -> str:
    ident = oid(key)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<page>
\t<content-type>{ctype}</content-type>
\t<display-template>{template}</display-template>
\t<no-template-required></no-template-required>
\t<merge-strategy>inherit-levels</merge-strategy>
\t<objectGroupId>{ident[:4]}</objectGroupId>
\t<objectId>{ident}</objectId>
\t<file-name>{filename}</file-name>
\t<folder-name>{folder}</folder-name>
\t<internal-name>{cdata(internal)}</internal-name>
\t<placeInNav>false</placeInNav>
\t<disabled>false</disabled>
\t<createdDate>{DATE}</createdDate>
\t<createdDate_dt>{DATE}</createdDate_dt>
\t<lastModifiedDate>{DATE}</lastModifiedDate>
\t<lastModifiedDate_dt>{DATE}</lastModifiedDate_dt>
{body}
</page>
"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def page_url(rel: str) -> str:
    if rel.endswith("index.html"):
        parent = rel[: -len("index.html")]
        return "/" + parent
    return "/" + rel


def map_path(path: str) -> str:
    path = path.split("#", 1)[0]
    if path in ("", "/"):
        return "/"
    if path.endswith("/index.html"):
        path = path[: -len("index.html")] or "/"
    if path.endswith(".html"):
        path = path[: -len(".html")]
    if path == "/index":
        path = "/"
    prefixes = (
        ("/altwheels/assets/", "/static-assets/altwheels/assets/"),
        ("/altwheels/downloads/", "/static-assets/altwheels/downloads/"),
        ("/altwheels/prompts/", "/static-assets/altwheels/prompts/"),
        ("/altwheels/templates/", "/static-assets/altwheels/templates/"),
        ("/altwheels/skills/", "/static-assets/altwheels/skills/"),
        ("/assets/", "/static-assets/images/"),
    )
    for src, dst in prefixes:
        if path.startswith(src):
            return dst + path[len(src):]
    files = {
        "/altwheels/REFERENCE_GUIDE.md": "/static-assets/altwheels/REFERENCE_GUIDE.md",
    }
    if path in files:
        return files[path]
    if path.endswith("/") and path != "/":
        path = path[:-1]
    return path or "/"


def rewrite_url(url: str, page: str) -> str:
    if not url or url.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return url
    if url.startswith("#"):
        return url
    split = urlsplit(url)
    if split.scheme in ("http", "https"):
        if split.netloc not in ("www.cloudzoom.dev", "cloudzoom.dev"):
            return url
        path = split.path or "/"
        frag = ("#" + split.fragment) if split.fragment else ""
        query = ("?" + split.query) if split.query else ""
        return map_path(path) + query + frag
    abs_url = urljoin(page_url(page), url)
    split = urlsplit(abs_url)
    frag = ("#" + split.fragment) if split.fragment else ""
    query = ("?" + split.query) if split.query else ""
    mapped = map_path(split.path or "/")
    if query and "/static-assets/" not in mapped:
        query = ""
    return mapped + query + frag


def rewrite_html(html: str, page: str) -> str:
    def repl(match: re.Match) -> str:
        attr, quote, url = match.group(1), match.group(2), match.group(3)
        return f"{attr}={quote}{rewrite_url(url, page)}{quote}"

    return re.sub(r"\b(href|src)=([\"'])([^\"']*)\2", repl, html)


def end_of_start(html: str, lt: int) -> int:
    quote = None
    j = lt + 1
    while j < len(html):
        c = html[j]
        if quote:
            if c == quote:
                quote = None
        elif c in "\"'":
            quote = c
        elif c == ">":
            return j
        j += 1
    return len(html) - 1


def find_close(html: str, tag: str, i: int) -> int:
    depth = 1
    lower = tag.lower()
    while i < len(html) and depth:
        lt = html.find("<", i)
        if lt < 0:
            return len(html)
        if html.startswith("<!--", lt):
            end = html.find("-->", lt)
            i = len(html) if end < 0 else end + 3
            continue
        if html.startswith("<!", lt) or html.startswith("<?", lt):
            i = html.find(">", lt) + 1
            continue
        closing = html[lt + 1] == "/"
        m = re.match(r"</?([a-zA-Z0-9:-]+)", html[lt:])
        if not m:
            i = lt + 1
            continue
        name = m.group(1).lower()
        gt = end_of_start(html, lt)
        self_close = html[gt - 1] == "/"
        if name == lower and not self_close:
            if closing:
                depth -= 1
                if depth == 0:
                    return gt + 1
            else:
                depth += 1
        i = gt + 1
    return len(html)


def top_elements(body: str) -> list[str]:
    out = []
    i = 0
    while i < len(body):
        lt = body.find("<", i)
        if lt < 0:
            break
        if body.startswith("<!--", lt):
            end = body.find("-->", lt)
            i = len(body) if end < 0 else end + 3
            continue
        if body[lt + 1] == "/":
            i = body.find(">", lt) + 1
            continue
        m = re.match(r"<([a-zA-Z0-9:-]+)", body[lt:])
        if not m:
            i = lt + 1
            continue
        tag = m.group(1)
        gt = end_of_start(body, lt)
        self_close = body[gt - 1] == "/"
        if self_close or tag.lower() in ("br", "hr", "img", "input", "meta", "link"):
            i = gt + 1
            continue
        close = find_close(body, tag, gt + 1)
        out.append(body[lt:close])
        i = close
    return out


def tag_class(element: str) -> tuple[str, str]:
    m = re.match(r"<([a-zA-Z0-9:-]+)([^>]*)>", element, re.S)
    tag = m.group(1).lower() if m else ""
    attrs = m.group(2) if m else ""
    cm = re.search(r'class="([^"]*)"', attrs)
    return tag, cm.group(1) if cm else ""


def inner(element: str) -> str:
    gt = end_of_start(element, 0)
    close = element.lower().rfind(f"</{tag_class(element)[0]}>")
    return element[gt + 1:close]


def text_of(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&mdash;", "—", text)
    text = re.sub(r"&middot;", "·", text)
    text = re.sub(r"&ldquo;", "“", text)
    text = re.sub(r"&rdquo;", "”", text)
    text = re.sub(r"&rsquo;", "’", text)
    text = re.sub(r"&#x27;", "'", text)
    text = re.sub(r"&copy;", "©", text)
    return re.sub(r"\s+", " ", text).strip()


def first(pattern: str, html: str, flags=re.S) -> str:
    m = re.search(pattern, html, flags)
    return m.group(1).strip() if m else ""


def meta(html: str, name: str) -> str:
    m = re.search(rf'<meta[^>]+name="{name}"[^>]+content="([^"]*)"', html)
    if not m:
        m = re.search(rf'<meta[^>]+content="([^"]*)"[^>]+name="{name}"', html)
    return m.group(1) if m else ""


def title_of(html: str) -> str:
    return first(r"<title>(.*?)</title>", html)


def head_links(html: str) -> str:
    keep = []
    for link in re.findall(r"<link\b[^>]*>", html):
        if "icon" in link and "http" not in link and "/static-assets/" not in link:
            continue
        if any(token in link for token in ("fonts.googleapis", "fonts.gstatic", "phosphor", "rel=\"icon\"", "rel='icon'")):
            keep.append(link)
    return "\n  ".join(keep)


def css_of(html: str) -> str:
    blocks = re.findall(r"<style>(.*?)</style>", html, re.S)
    return "\n".join(blocks).strip() + "\n"


def load(rel: str) -> str:
    return (MIRROR / rel).read_text(encoding="utf-8")


def slug_of(rel: str) -> str:
    name = Path(rel).name
    if name == "index.html":
        parent = Path(rel).parent.name
        return parent or "home"
    return name[: -len(".html")]


def folder_of(rel: str) -> str:
    if rel == "index.html":
        return ""
    if rel.endswith("/index.html"):
        return str(Path(rel).parent)
    return str(Path(rel).with_suffix(""))


# ---------- forms ----------

def input_field(fid: str, title: str, required=False, maxlength=500) -> str:
    req = "<![CDATA[true]]>" if required else "<![CDATA[]]>"
    return f"""
\t\t\t\t<field>
\t\t\t\t\t<type>input</type>
\t\t\t\t\t<id>{fid}</id>
\t\t\t\t\t<iceId></iceId>
\t\t\t\t\t<title>{title}</title>
\t\t\t\t\t<description></description>
\t\t\t\t\t<defaultValue></defaultValue>
\t\t\t\t\t<help></help>
\t\t\t\t\t<properties>
\t\t\t\t\t\t<property><name>size</name><value>50</value><type>int</type></property>
\t\t\t\t\t\t<property><name>maxlength</name><value>{maxlength}</value><type>int</type></property>
\t\t\t\t\t\t<property><name>readonly</name><value></value><type>boolean</type></property>
\t\t\t\t\t\t<property><name>tokenize</name><value>false</value><type>boolean</type></property>
\t\t\t\t\t</properties>
\t\t\t\t\t<constraints>
\t\t\t\t\t\t<constraint><name>required</name><value>{req}</value><type>boolean</type></constraint>
\t\t\t\t\t</constraints>
\t\t\t\t</field>"""


def textarea_field(fid: str, title: str, maxlength=200000, rows=12) -> str:
    return f"""
\t\t\t\t<field>
\t\t\t\t\t<type>textarea</type>
\t\t\t\t\t<id>{fid}</id>
\t\t\t\t\t<iceId></iceId>
\t\t\t\t\t<title>{title}</title>
\t\t\t\t\t<description></description>
\t\t\t\t\t<defaultValue></defaultValue>
\t\t\t\t\t<help></help>
\t\t\t\t\t<properties>
\t\t\t\t\t\t<property><name>cols</name><value>80</value><type>int</type></property>
\t\t\t\t\t\t<property><name>rows</name><value>{rows}</value><type>int</type></property>
\t\t\t\t\t\t<property><name>maxlength</name><value>{maxlength}</value><type>int</type></property>
\t\t\t\t\t\t<property><name>readonly</name><value></value><type>boolean</type></property>
\t\t\t\t\t\t<property><name>tokenize</name><value>false</value><type>boolean</type></property>
\t\t\t\t\t</properties>
\t\t\t\t\t<constraints>
\t\t\t\t\t\t<constraint><name>required</name><value><![CDATA[]]></value><type>boolean</type></constraint>
\t\t\t\t\t</constraints>
\t\t\t\t</field>"""


def repeat_field(fid: str, title: str, children: str) -> str:
    return f"""
\t\t\t\t<field>
\t\t\t\t\t<type>repeat</type>
\t\t\t\t\t<id>{fid}</id>
\t\t\t\t\t<iceId></iceId>
\t\t\t\t\t<title>{title}</title>
\t\t\t\t\t<description></description>
\t\t\t\t\t<minOccurs>0</minOccurs>
\t\t\t\t\t<maxOccurs>*</maxOccurs>
\t\t\t\t\t<properties>
\t\t\t\t\t\t<property><name>minOccurs</name><value>0</value><type>string</type></property>
\t\t\t\t\t\t<property><name>maxOccurs</name><value>*</value><type>string</type></property>
\t\t\t\t\t</properties>
\t\t\t\t\t<fields>{children}
\t\t\t\t\t</fields>
\t\t\t\t</field>"""


def node_field(fid: str, title: str, datasource: str, types: str, max_size="") -> str:
    return f"""
\t\t\t\t<field>
\t\t\t\t\t<type>node-selector</type>
\t\t\t\t\t<id>{fid}</id>
\t\t\t\t\t<iceId></iceId>
\t\t\t\t\t<title>{title}</title>
\t\t\t\t\t<description></description>
\t\t\t\t\t<defaultValue></defaultValue>
\t\t\t\t\t<help></help>
\t\t\t\t\t<properties>
\t\t\t\t\t\t<property><name>minSize</name><value></value><type>int</type></property>
\t\t\t\t\t\t<property><name>maxSize</name><value>{max_size}</value><type>int</type></property>
\t\t\t\t\t\t<property><name>itemManager</name><value>{datasource}</value><type>datasource:item</type></property>
\t\t\t\t\t\t<property><name>readonly</name><value></value><type>boolean</type></property>
\t\t\t\t\t\t<property><name>disableFlattening</name><value></value><type>boolean</type></property>
\t\t\t\t\t\t<property><name>useSingleValueFilename</name><value></value><type>boolean</type></property>
\t\t\t\t\t\t<property><name>contentTypes</name><value>{types}</value><type>contentTypes</type></property>
\t\t\t\t\t\t<property><name>tags</name><value></value><type>string</type></property>
\t\t\t\t\t</properties>
\t\t\t\t\t<constraints>
\t\t\t\t\t\t<constraint><name>allowDuplicates</name><value><![CDATA[]]></value><type>boolean</type></constraint>
\t\t\t\t\t</constraints>
\t\t\t\t</field>"""


def shared_ds(did: str, title: str, path: str) -> str:
    return f"""
\t\t<datasource>
\t\t\t<type>shared-content</type>
\t\t\t<id>{did}</id>
\t\t\t<title>{title}</title>
\t\t\t<interface>item</interface>
\t\t\t<properties>
\t\t\t\t<property><name>repoPath</name><value>{path}</value><type>undefined</type></property>
\t\t\t\t<property><name>browsePath</name><value>{path}</value><type>undefined</type></property>
\t\t\t\t<property><name>type</name><value></value><type>undefined</type></property>
\t\t\t\t<property><name>enableCreateNew</name><value>true</value><type>boolean</type></property>
\t\t\t\t<property><name>enableBrowseExisting</name><value>true</value><type>boolean</type></property>
\t\t\t\t<property><name>enableSearchExisting</name><value>true</value><type>boolean</type></property>
\t\t\t</properties>
\t\t</datasource>"""


def form(title: str, description: str, object_type: str, ctype: str, template: str, sections: str, datasources: str) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<form>
\t<title>{title}</title>
\t<description>{description}</description>
\t<objectType>{object_type}</objectType>
\t<content-type>{ctype}</content-type>
\t<imageThumbnail></imageThumbnail>
\t<quickCreate>false</quickCreate>
\t<quickCreatePath></quickCreatePath>
\t<properties>
\t\t<property>
\t\t\t<name>display-template</name>
\t\t\t<label>Display Template</label>
\t\t\t<value>{template}</value>
\t\t\t<type>template</type>
\t\t</property>
\t\t<property>
\t\t\t<name>no-template-required</name>
\t\t\t<label>No Template Required</label>
\t\t\t<value></value>
\t\t\t<type>boolean</type>
\t\t</property>
\t\t<property>
\t\t\t<name>merge-strategy</name>
\t\t\t<label>Merge Strategy</label>
\t\t\t<value>inherit-levels</value>
\t\t\t<type>string</type>
\t\t</property>
\t</properties>
\t<sections>
{sections}
\t</sections>
\t<datasources>
{datasources}
\t</datasources>
</form>
"""


def section_block(title: str, fields: str) -> str:
    return f"""
\t\t<section>
\t\t\t<title>{title}</title>
\t\t\t<description></description>
\t\t\t<defaultOpen>true</defaultOpen>
\t\t\t<fields>
{fields}
\t\t\t</fields>
\t\t</section>"""


def config_xml(name: str, label: str, previewable: bool, content_as_folder: bool, description: str) -> str:
    preview = "true" if previewable else "false"
    folder = "true" if content_as_folder else "false"
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<content-type name="{name}" is-wcm-type="true">
\t<label>{label}</label>
\t<form>{name}</form>
\t<form-path>simple</form-path>
\t<model-instance-path>NOT-USED-BY-SIMPLE-FORM-ENGINE</model-instance-path>
\t<file-extension>xml</file-extension>
\t<content-as-folder>{folder}</content-as-folder>
\t<previewable>{preview}</previewable>
\t<quickCreate>false</quickCreate>
\t<quickCreatePath></quickCreatePath>
\t<noThumbnail>true</noThumbnail>
\t<image-thumbnail></image-thumbnail>
\t<description>{description}</description>
</content-type>
"""


def write_type(kind: str, name: str, label: str, description: str, template: str, form_xml: str, previewable: bool, folder: bool) -> None:
    base = ROOT / "config/studio/content-types" / kind / name
    write(base / "config.xml", config_xml(f"/{kind}/{name}", label, previewable, folder, description))
    write(base / "form-definition.xml", form_xml)


# ---------- card / article parsing ----------

def icon_class(html: str) -> str:
    m = re.search(r"ph ph-[a-z0-9-]+", html)
    return m.group(0) if m else ""


def parse_blog_cards(html: str) -> list[dict]:
    cards = []
    for m in re.finditer(r'<article class="article-card([^"]*)"[\s\S]*?</article>', html):
        block = m.group(0)
        featured = "featured" in m.group(1)
        href = first(r'href="([^"]+)"', block)
        tags = re.findall(r'<span class="article-tag">([^<]*)</span>', block)
        cards.append({
            "href": href,
            "featured": featured,
            "visual": text_of(first(r'<span class="article-card-visual-label">([\s\S]*?)</span>', block)),
            "icon": icon_class(block),
            "date": text_of(first(r'<span class="article-date">([\s\S]*?)</span>', block)),
            "read": text_of(first(r'<span class="article-read-time">([\s\S]*?)</span>', block)),
            "title": text_of(first(r'<h2 class="article-title">([\s\S]*?)</h2>', block)),
            "excerpt": text_of(first(r'<p class="article-excerpt">([\s\S]*?)</p>', block)),
            "tags": [text_of(t) for t in tags],
        })
    return cards


def parse_home_cards(html: str) -> list[dict]:
    cards = []
    for m in re.finditer(r'<a\b[^>]*class="blog-card"[^>]*>[\s\S]*?</a>', html):
        block = m.group(0)
        cards.append({
            "href": first(r'href="([^"]+)"', block),
            "tag": text_of(first(r'<span class="blog-card-tag">([\s\S]*?)</span>', block)),
            "icon": icon_class(block),
            "meta": text_of(first(r'<span class="blog-card-meta">([\s\S]*?)</span>', block)),
            "title": text_of(first(r'<h3 class="blog-card-title">([\s\S]*?)</h3>', block)),
            "excerpt": text_of(first(r'<p class="blog-card-excerpt">([\s\S]*?)</p>', block)),
            "cta": text_of(first(r'<span class="blog-card-link">([\s\S]*?)</span>', block)).replace("→", "").strip(),
        })
    return cards


def norm_href(href: str) -> str:
    return href.split("?", 1)[0].split("#", 1)[0].lstrip("./")


def main() -> None:
    raise SystemExit(
        "build_site.py stores page regions in markup text areas. "
        "The content model is structured now; do not regenerate it with this script."
    )
    if not MIRROR.exists():
        raise SystemExit(f"Missing mirror at {MIRROR}")

    # assets
    img_dst = ROOT / "static-assets/images"
    if img_dst.exists():
        shutil.rmtree(img_dst)
    shutil.copytree(MIRROR / "assets", img_dst)
    aw_dst = ROOT / "static-assets/altwheels"
    if aw_dst.exists():
        shutil.rmtree(aw_dst)
    aw_dst.mkdir(parents=True)
    src_aw = MIRROR / "altwheels"
    for name in ("assets", "downloads", "prompts", "templates", "skills"):
        shutil.copytree(src_aw / name, aw_dst / name)
    for md in src_aw.glob("*.md"):
        shutil.copy2(md, aw_dst / md.name)
    css_dir = ROOT / "static-assets/app/css"
    css_dir.mkdir(parents=True, exist_ok=True)

    blog_html = load("blog.html")
    home_html = load("index.html")
    list_cards = {norm_href(c["href"]): c for c in parse_blog_cards(blog_html)}
    home_cards = {norm_href(c["href"]): c for c in parse_home_cards(home_html)}

    # ---------- content types ----------
    file_name = input_field("file-name", "File Name", True, 50)
    internal = input_field("internal-name", "Internal Name", True, 120)
    nav_children = input_field("label_t", "Label", True) + input_field("url_s", "URL", True) + input_field("key_s", "Nav Key", True, 40)
    write_type(
        "component", "header", "Header", "Site header and primary navigation.",
        "/templates/web/components/header.ftl",
        form(
            "Header", "Primary navigation.", "component", "/component/header",
            "/templates/web/components/header.ftl",
            section_block("Header", file_name + internal
                + input_field("variant_s", "Variant (marketing or altwheels)", True, 40)
                + input_field("brand_t", "Brand", True)
                + input_field("ctaLabel_t", "Call to Action Label")
                + input_field("ctaUrl_s", "Call to Action URL")
                + repeat_field("nav_o", "Navigation", nav_children)
                + textarea_field("tagline_t", "AltWheels Tagline", 500, 3)),
            "",
        ),
        False, False,
    )
    footer_nav = input_field("label_t", "Label", True) + input_field("url_s", "URL", True)
    write_type(
        "component", "footer", "Footer", "Site footer.",
        "/templates/web/components/footer.ftl",
        form(
            "Footer", "Footer content. Pages can override the tagline and which blocks show.",
            "component", "/component/footer", "/templates/web/components/footer.ftl",
            section_block("Footer", file_name + internal
                + input_field("variant_s", "Variant (marketing, blog, article, altwheels)", True, 40)
                + input_field("brand_t", "Brand")
                + textarea_field("tagline_t", "Tagline", 800, 3)
                + input_field("phone_t", "Phone")
                + input_field("phoneUrl_s", "Phone URL")
                + input_field("email_t", "Email")
                + input_field("linkedinLabel_t", "LinkedIn Label")
                + input_field("linkedinUrl_s", "LinkedIn URL")
                + input_field("copyright_t", "Copyright")
                + input_field("showLinkedIn_s", "Show LinkedIn (true/false)")
                + input_field("showLegal_s", "Show Copyright Bar (true/false)")
                + repeat_field("nav_o", "Footer Navigation", footer_nav)
                + repeat_field("connect_o", "Blog Connect Column", footer_nav)),
            "",
        ),
        False, False,
    )
    write_type(
        "component", "section", "Section", "A page section. HTML sections keep the imported markup. Blog sections list articles.",
        "/templates/web/components/section.ftl",
        form(
            "Section", "Page section.", "component", "/component/section",
            "/templates/web/components/section.ftl",
            section_block("Section", file_name + internal
                + input_field("layout_s", "Layout (html, blog-preview, article-index)", True, 40)
                + input_field("title_t", "Heading")
                + textarea_field("subtitle_t", "Subheading", 2000, 4)
                + input_field("linkLabel_t", "Link Label")
                + input_field("linkUrl_s", "Link URL")
                + textarea_field("markup_html", "Section HTML", 500000, 18)),
            "",
        ),
        False, False,
    )
    overrides = (
        node_field("header_o", "Header Override", "headerComponents", "/component/header", "1")
        + node_field("footer_o", "Footer Override", "footerComponents", "/component/footer", "1")
    )
    ds = shared_ds("headerComponents", "Headers", "/site/components/headers/") + shared_ds("footerComponents", "Footers", "/site/components/footers/") + shared_ds("sectionComponents", "Sections", "/site/components/sections/")
    page_fields = (
        file_name + internal
        + input_field("navLabel", "Nav Label")
        + input_field("title_t", "Title", True)
        + textarea_field("seoDescription_t", "SEO Description", 4000, 4)
        + input_field("navKey_s", "Active Nav Key", False, 40)
        + input_field("stylesheet_s", "Stylesheet")
        + textarea_field("headLinks_html", "Head Links", 8000, 6)
        + input_field("footerMode_s", "Footer Mode (inherit, marketing, blog, article)")
        + textarea_field("footerTagline_t", "Footer Tagline Override", 800, 3)
        + input_field("footerLinkedIn_s", "Footer LinkedIn Override (true/false)")
        + input_field("footerLegal_s", "Footer Copyright Override (true/false)")
        + overrides
        + node_field("sections_o", "Sections", "sectionComponents", "/component/section")
    )
    write_type(
        "page", "landing", "Landing Page", "Marketing or blog index page composed of sections.",
        "/templates/web/pages/landing.ftl",
        form("Landing Page", "Page composed of sections.", "page", "/page/landing",
             "/templates/web/pages/landing.ftl",
             section_block("Page", page_fields), ds),
        True, True,
    )
    article_fields = (
        file_name + internal
        + input_field("navLabel", "Nav Label")
        + input_field("title_t", "Title", True)
        + input_field("headline_t", "Headline", True)
        + textarea_field("seoDescription_t", "SEO Description", 4000, 4)
        + input_field("navKey_s", "Active Nav Key")
        + input_field("stylesheet_s", "Stylesheet")
        + textarea_field("headLinks_html", "Head Links", 8000, 6)
        + input_field("author_t", "Author")
        + input_field("dateLabel_t", "Date")
        + input_field("readTime_t", "Read Time")
        + input_field("listRead_t", "Blog Index Read Time")
        + input_field("wrap_s", "Wrapper (main or empty)")
        + input_field("sortOrder_s", "Sort Order")
        + input_field("featured_s", "Featured on Blog Index (true/false)")
        + input_field("showOnHome_s", "Show on Home (true/false)")
        + input_field("homeOrder_s", "Home Order")
        + input_field("visualLabel_t", "Blog Card Label")
        + input_field("icon_s", "Icon Class")
        + textarea_field("listExcerpt_t", "Blog Index Excerpt", 2000, 4)
        + input_field("homeTag_t", "Home Card Tag")
        + input_field("homeIcon_s", "Home Icon Class")
        + input_field("homeMeta_t", "Home Card Meta")
        + textarea_field("homeExcerpt_t", "Home Card Excerpt", 2000, 4)
        + input_field("homeCta_t", "Home Card Link Label")
        + repeat_field("tags_o", "Tags", input_field("label_t", "Tag", True))
        + repeat_field("listTags_o", "Blog Index Tags", input_field("label_t", "Tag", True))
        + input_field("listDate_t", "Blog Index Date")
        + textarea_field("body_html", "Article Body HTML", 500000, 20)
        + overrides
    )
    write_type(
        "page", "article", "Article", "Blog article.",
        "/templates/web/pages/article.ftl",
        form("Article", "Blog article.", "page", "/page/article",
             "/templates/web/pages/article.ftl",
             section_block("Article", article_fields),
             shared_ds("headerComponents", "Headers", "/site/components/headers/") + shared_ds("footerComponents", "Footers", "/site/components/footers/")),
        True, True,
    )
    resource_fields = (
        file_name + internal
        + input_field("navLabel", "Nav Label")
        + input_field("title_t", "Title", True)
        + textarea_field("seoDescription_t", "SEO Description", 4000, 4)
        + input_field("stylesheet_s", "Stylesheet")
        + textarea_field("headLinks_html", "Head Links", 8000, 6)
        + input_field("script_s", "Script")
        + textarea_field("main_html", "Main HTML", 500000, 20)
        + overrides
    )
    write_type(
        "page", "resource", "Resource Page", "AltWheels resource page.",
        "/templates/web/pages/resource.ftl",
        form("Resource Page", "AltWheels resource page.", "page", "/page/resource",
             "/templates/web/pages/resource.ftl",
             section_block("Resource", resource_fields),
             shared_ds("headerComponents", "Headers", "/site/components/headers/") + shared_ds("footerComponents", "Footers", "/site/components/footers/")),
        True, True,
    )

    # ---------- shared chrome ----------
    nav = [
        {"label_t": "Home", "url_s": "/", "key_s": "home"},
        {"label_t": "Services", "url_s": "/services", "key_s": "services"},
        {"label_t": "Software", "url_s": "/software", "key_s": "software"},
        {"label_t": "Work", "url_s": "/work", "key_s": "work"},
        {"label_t": "Blog", "url_s": "/blog", "key_s": "blog"},
        {"label_t": "About", "url_s": "/about", "key_s": "about"},
        {"label_t": "Contact", "url_s": "/contact", "key_s": "contact"},
    ]
    footer_nav_rows = [
        {"label_t": "Home", "url_s": "/"},
        {"label_t": "Services", "url_s": "/services"},
        {"label_t": "Software", "url_s": "/software"},
        {"label_t": "Work", "url_s": "/work"},
        {"label_t": "About", "url_s": "/about"},
        {"label_t": "Contact", "url_s": "/contact"},
    ]
    blog_footer_nav = footer_nav_rows[:4] + [{"label_t": "Blog", "url_s": "/blog"}] + footer_nav_rows[4:]
    connect = [
        {"label_t": "bill@cloudzoom.dev", "url_s": "mailto:bill@cloudzoom.dev"},
        {"label_t": "LinkedIn", "url_s": "https://www.linkedin.com/in/bill-scott-boston/"},
        {"label_t": "Automated QA Agents", "url_s": "/services"},
        {"label_t": "Book Strategy Call", "url_s": "/contact"},
    ]
    header_body = "\n".join([
        field("variant_s", "marketing"),
        field("brand_t", "CloudZoom Solutions"),
        field("ctaLabel_t", "STRATEGY CALL"),
        field("ctaUrl_s", "/contact"),
        field("tagline_t", ""),
        repeat("nav_o", nav),
    ])
    write(ROOT / "site/components/headers/main-header.xml", component_xml(
        "/component/header", "/templates/web/components/header.ftl", "main-header.xml",
        "Main Header", "header-main", header_body,
    ))
    aw_header = "\n".join([
        field("variant_s", "altwheels"),
        field("brand_t", "CloudZoom Solutions"),
        field("ctaLabel_t", ""),
        field("ctaUrl_s", ""),
        field("tagline_t", ""),
        repeat("nav_o", nav),
    ])
    write(ROOT / "site/components/headers/altwheels-header.xml", component_xml(
        "/component/header", "/templates/web/components/header.ftl", "altwheels-header.xml",
        "AltWheels Header", "header-altwheels", aw_header,
    ))
    footer_body = "\n".join([
        field("variant_s", "marketing"),
        field("brand_t", "CloudZoom Solutions"),
        field("tagline_t", "Boston-based. Senior-led. AI-accelerated."),
        field("phone_t", "617.921.3657"),
        field("phoneUrl_s", "tel:6179213657"),
        field("email_t", "bill@cloudzoom.dev"),
        field("linkedinLabel_t", "LinkedIn"),
        field("linkedinUrl_s", "https://www.linkedin.com/in/bill-scott-boston/"),
        field("copyright_t", "© 2025 CloudZoom Solutions Inc. All rights reserved."),
        field("showLinkedIn_s", "true"),
        field("showLegal_s", "true"),
        repeat("nav_o", footer_nav_rows),
        repeat("connect_o", []),
    ])
    write(ROOT / "site/components/footers/main-footer.xml", component_xml(
        "/component/footer", "/templates/web/components/footer.ftl", "main-footer.xml",
        "Main Footer", "footer-main", footer_body,
    ))
    blog_footer = "\n".join([
        field("variant_s", "blog"),
        field("brand_t", "CloudZoom Solutions"),
        field("tagline_t", "AI-enhanced custom software development and automated QA agents for teams that need reliable releases. Built by experts. Priced for reality."),
        field("phone_t", ""),
        field("phoneUrl_s", ""),
        field("email_t", "bill@cloudzoom.dev"),
        field("linkedinLabel_t", "LinkedIn"),
        field("linkedinUrl_s", "https://www.linkedin.com/in/bill-scott-boston/"),
        field("copyright_t", "© 2026 CloudZoom Solutions Inc. All rights reserved."),
        field("showLinkedIn_s", "true"),
        field("showLegal_s", "true"),
        repeat("nav_o", blog_footer_nav),
        repeat("connect_o", connect),
    ])
    write(ROOT / "site/components/footers/blog-footer.xml", component_xml(
        "/component/footer", "/templates/web/components/footer.ftl", "blog-footer.xml",
        "Blog Footer", "footer-blog", blog_footer,
    ))
    article_footer = "\n".join([
        field("variant_s", "article"),
        field("brand_t", "CloudZoom Solutions"),
        field("tagline_t", ""),
        field("phone_t", ""),
        field("phoneUrl_s", ""),
        field("email_t", "bill@cloudzoom.dev"),
        field("linkedinLabel_t", ""),
        field("linkedinUrl_s", ""),
        field("copyright_t", "© 2026 CloudZoom Solutions Inc. All rights reserved."),
        field("showLinkedIn_s", "false"),
        field("showLegal_s", "true"),
        repeat("nav_o", []),
        repeat("connect_o", []),
    ])
    write(ROOT / "site/components/footers/article-footer.xml", component_xml(
        "/component/footer", "/templates/web/components/footer.ftl", "article-footer.xml",
        "Article Footer", "footer-article", article_footer,
    ))
    aw_footer = "\n".join([
        field("variant_s", "altwheels"),
        field("brand_t", "CloudZoom Solutions"),
        field("tagline_t", "Smarter systems. Brighter possibilities."),
        field("phone_t", "617.921.3657"),
        field("phoneUrl_s", "tel:6179213657"),
        field("email_t", "bill@cloudzoom.dev"),
        field("linkedinLabel_t", ""),
        field("linkedinUrl_s", ""),
        field("copyright_t", "© 2026 CloudZoom Solutions Inc."),
        field("showLinkedIn_s", "false"),
        field("showLegal_s", "true"),
        repeat("nav_o", []),
        repeat("connect_o", []),
    ])
    write(ROOT / "site/components/footers/altwheels-footer.xml", component_xml(
        "/component/footer", "/templates/web/components/footer.ftl", "altwheels-footer.xml",
        "AltWheels Footer", "footer-altwheels", aw_footer,
    ))

    level = f"""<?xml version="1.0" encoding="UTF-8"?>
<component>
\t<content-type>/component/level-descriptor</content-type>
\t<display-template></display-template>
\t<no-template-required></no-template-required>
\t<merge-strategy>inherit-levels</merge-strategy>
\t<objectGroupId>{oid('level')[:4]}</objectGroupId>
\t<objectId>{oid('level')}</objectId>
\t<file-name>crafter-level-descriptor.level.xml</file-name>
\t<folder-name></folder-name>
\t<internal-name>Section Defaults</internal-name>
\t<createdDate>{DATE}</createdDate>
\t<createdDate_dt>{DATE}</createdDate_dt>
\t<lastModifiedDate>{DATE}</lastModifiedDate>
\t<lastModifiedDate_dt>{DATE}</lastModifiedDate_dt>
{node_list('header_o', [('/site/components/headers/main-header.xml', 'Main Header')])}
{node_list('footer_o', [('/site/components/footers/main-footer.xml', 'Main Footer')])}
</component>
"""
    write(ROOT / "site/website/crafter-level-descriptor.level.xml", level)
    aw_level = level.replace("main-header.xml", "altwheels-header.xml").replace("Main Header", "AltWheels Header")
    aw_level = aw_level.replace("main-footer.xml", "altwheels-footer.xml").replace("Main Footer", "AltWheels Footer")
    aw_level = aw_level.replace(oid("level"), oid("level-altwheels"))
    aw_level = aw_level.replace(
        f"<objectGroupId>{oid('level')[:4]}</objectGroupId>",
        f"<objectGroupId>{oid('level-altwheels')[:4]}</objectGroupId>",
    )
    write(ROOT / "site/website/altwheels/crafter-level-descriptor.level.xml", aw_level)

    # page-specific footer presentation
    footer_overrides = {
        "index.html": ("Boston-based. Senior-led. AI-enhanced software and QA.", "true", "true", "marketing"),
        "services.html": ("Boston-based. Senior-led. AI-accelerated.", "true", "true", "marketing"),
        "software.html": ("Boston-based. Senior-led. AI-enhanced software and QA.", "false", "false", "marketing"),
        "work.html": ("Boston-based. Senior-led. AI-accelerated.", "true", "true", "marketing"),
        "about.html": ("Technology that works for your people.", "true", "true", "marketing"),
        "contact.html": ("Boston-based. Senior-led. AI-accelerated.", "true", "true", "marketing"),
        "blog.html": ("", "", "", "blog"),
    }
    nav_keys = {
        "index.html": "home",
        "services.html": "services",
        "software.html": "software",
        "work.html": "work",
        "about.html": "about",
        "contact.html": "contact",
        "blog.html": "blog",
    }

    def emit_sections(rel: str, html: str) -> list[tuple[str, str]]:
        body_m = re.search(r"<body[^>]*>", html, re.I)
        end = html.lower().rfind("</body>")
        body = html[body_m.end():end]
        refs = []
        n = 0
        page_slug = slug_of(rel)
        for el in top_elements(body):
            tag, cls = tag_class(el)
            if tag in ("nav", "footer"):
                continue
            classes = cls.split()
            n += 1
            if "blog-preview" in classes:
                layout = "blog-preview"
                title = text_of(first(r"<h2[^>]*>([\s\S]*?)</h2>", el))
                subtitle = text_of(first(r'<p class="section-subtitle">([\s\S]*?)</p>', el))
                link_label = "View all articles"
                link_url = "/blog"
                markup = ""
                internal_name = f"{page_slug} — {title or 'Blog preview'}"
            elif "articles-section" in classes:
                layout = "article-index"
                title = ""
                subtitle = ""
                link_label = ""
                link_url = ""
                markup = ""
                internal_name = f"{page_slug} — Articles"
            else:
                layout = "html"
                title = text_of(first(r"<h1[^>]*>([\s\S]*?)</h1>", el) or first(r"<h2[^>]*>([\s\S]*?)</h2>", el))
                subtitle = ""
                link_label = ""
                link_url = ""
                markup = rewrite_html(el, rel)
                internal_name = f"{page_slug} — {title or cls or tag}"
            fname = f"{n:02d}-{layout if layout != 'html' else (classes[0] if classes else tag)}.xml"
            path = f"/site/components/sections/{page_slug}/{fname}"
            body_xml = "\n".join([
                field("layout_s", layout),
                field("title_t", title),
                field("subtitle_t", subtitle),
                field("linkLabel_t", link_label),
                field("linkUrl_s", link_url),
                field("markup_html", markup),
            ])
            write(ROOT / path.lstrip("/"), component_xml(
                "/component/section", "/templates/web/components/section.ftl", fname,
                internal_name[:110], f"section-{page_slug}-{n}", body_xml,
            ))
            refs.append((path, internal_name[:110]))
        return refs

    for rel in PAGES:
        html = load(rel)
        slug = slug_of(rel)
        css_name = f"{slug}.css"
        write(css_dir / css_name, css_of(html))
        sections = emit_sections(rel, html)
        tagline, linkedin, legal, mode = footer_overrides[rel]
        folder = folder_of(rel)
        filename = "index.xml"
        body = "\n".join([
            field("navLabel", "Home" if rel == "index.html" else slug.replace("-", " ").title() if slug != "blog" else "Blog"),
            field("title_t", title_of(html)),
            field("seoDescription_t", meta(html, "description")),
            field("navKey_s", nav_keys[rel]),
            field("stylesheet_s", f"/static-assets/app/css/{css_name}"),
            field("headLinks_html", head_links(html)),
            field("footerMode_s", mode),
            field("footerTagline_t", tagline),
            field("footerLinkedIn_s", linkedin),
            field("footerLegal_s", legal),
            node_list("sections_o", sections),
        ])
        if mode == "blog":
            body += "\n" + node_list("footer_o", [("/site/components/footers/blog-footer.xml", "Blog Footer")])
        label = "Home" if rel == "index.html" else title_of(html).split("|")[0].strip()
        dest = ROOT / "site/website" / (f"{folder}/index.xml" if folder else "index.xml")
        write(dest, page_xml(
            "/page/landing", "/templates/web/pages/landing.ftl", filename, folder,
            label, f"page-{slug}", body,
        ))
        print(f"page {slug}: {len(sections)} sections")

    for index, rel in enumerate(ARTICLES, start=1):
        html = load(rel)
        slug = slug_of(rel)
        css_name = f"article-{slug}.css"
        write(css_dir / css_name, css_of(html))
        body_m = re.search(r"<body[^>]*>", html, re.I)
        end = html.lower().rfind("</body>")
        elements = top_elements(html[body_m.end():end])
        wrap = ""
        if any(tag_class(el)[0] == "main" for el in elements):
            wrap = "main"
            main_el = next(el for el in elements if tag_class(el)[0] == "main")
            elements = top_elements(inner(main_el))
        article_el = next(el for el in elements if tag_class(el)[0] == "article")
        header_el = next(el for el in elements if "article-header" in tag_class(el)[1])
        h1 = text_of(first(r"<h1[^>]*>([\s\S]*?)</h1>", header_el))
        tags = [text_of(t) for t in re.findall(r'<span class="article-tag">([\s\S]*?)</span>', header_el)]
        card = list_cards.get(f"blog/{slug}.html", {})
        home = home_cards.get(f"blog/{slug}.html", {})
        body = "\n".join([
            field("navLabel", card.get("title") or slug),
            field("title_t", title_of(html)),
            field("headline_t", h1),
            field("seoDescription_t", meta(html, "description")),
            field("navKey_s", "blog"),
            field("stylesheet_s", f"/static-assets/app/css/{css_name}"),
            field("headLinks_html", head_links(html)),
            field("author_t", text_of(first(r'<span class="article-author">([\s\S]*?)</span>', header_el))),
            field("dateLabel_t", text_of(first(r'<span class="article-date">([\s\S]*?)</span>', header_el))),
            field("readTime_t", text_of(first(r'<span class="article-read">([\s\S]*?)</span>', header_el))),
            field("listRead_t", card.get("read", "")),
            field("wrap_s", wrap),
            field("sortOrder_s", f"{index:02d}"),
            field("featured_s", "true" if card.get("featured") else "false"),
            field("showOnHome_s", "true" if home else "false"),
            field("homeOrder_s", f"{list(home_cards).index('blog/' + slug + '.html') + 1:02d}" if home else ""),
            field("visualLabel_t", card.get("visual", "")),
            field("icon_s", card.get("icon", "")),
            field("listExcerpt_t", card.get("excerpt", "")),
            field("homeTag_t", home.get("tag", "")),
            field("homeIcon_s", home.get("icon", "")),
            field("homeMeta_t", home.get("meta", "")),
            field("homeExcerpt_t", home.get("excerpt", "")),
            field("homeCta_t", re.sub(r"\s+", " ", home.get("cta", "")).strip()),
            repeat("tags_o", [{"label_t": t} for t in tags]),
            repeat("listTags_o", [{"label_t": t} for t in card.get("tags", [])]),
            field("listDate_t", card.get("date", "")),
            field("body_html", rewrite_html(article_el, rel)),
            node_list("footer_o", [("/site/components/footers/article-footer.xml", "Article Footer")]),
        ])
        write(ROOT / "site/website/blog" / slug / "index.xml", page_xml(
            "/page/article", "/templates/web/pages/article.ftl", "index.xml", slug,
            h1[:110], f"article-{slug}", body,
        ))
        print(f"article {slug} home={bool(home)} featured={card.get('featured')}")

    for rel in RESOURCE_PAGES:
        html = load(rel)
        slug = slug_of(rel)
        body_m = re.search(r"<body[^>]*>", html, re.I)
        end = html.lower().rfind("</body>")
        elements = top_elements(html[body_m.end():end])
        main_el = next(el for el in elements if tag_class(el)[0] == "main")
        script = "/static-assets/altwheels/assets/altwheels.js" if "altwheels.js" in html else ""
        folder = folder_of(rel)
        body = "\n".join([
            field("navLabel", title_of(html).split("|")[0].strip()),
            field("title_t", title_of(html)),
            field("seoDescription_t", meta(html, "description")),
            field("stylesheet_s", "/static-assets/altwheels/assets/altwheels.css"),
            field("headLinks_html", head_links(html)),
            field("script_s", script),
            field("main_html", rewrite_html(main_el, rel)),
        ])
        dest_folder = folder
        write(ROOT / "site/website" / dest_folder / "index.xml", page_xml(
            "/page/resource", "/templates/web/pages/resource.ftl", "index.xml", dest_folder,
            title_of(html).split("|")[0].strip()[:110], f"resource-{slug}", body,
        ))
        print(f"resource {folder}")

    print("built", ROOT)


if __name__ == "__main__":
    main()
