#!/usr/bin/env python3
"""Write structured content types, templates wiring, and content items."""

from __future__ import annotations

import importlib.util
import re
import shutil
import uuid
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("remodel", ROOT / "tools/remodel_content.py")
remodel = importlib.util.module_from_spec(spec)
spec.loader.exec_module(remodel)

PROSE = {
    "subtitle_t", "subtext_t", "intro_t", "detail_t", "note_t", "quote_t", "lead_t",
    "bannerText_t", "closingText_t", "formSubtitle_t", "boxText_t", "subheading_t",
    "skillText_t", "closingBefore_t", "prompt_t", "textBefore_t", "textAfter_t",
}
IMAGE_FIELDS = {"image_s", "qrImage_s"}
LABELS = {
    "home-hero": ("Home Hero", "Home hero with actions, trust chips, and the systems diagram."),
    "eyebrow-hero": ("Eyebrow Hero", "Hero with an eyebrow, heading, and subheading."),
    "services-hero": ("Services Hero", "Services hero whose subheading includes one link."),
    "blog-hero": ("Blog Hero", "Blog index hero."),
    "work-hero": ("Work Hero", "Work page hero."),
    "value-props": ("Value Props", "Row of icon stats."),
    "why-section": ("Why Section", "Benefit list and diagram."),
    "home-services": ("Home Services", "Home service cards and footer links."),
    "social-proof": ("Social Proof", "Quote and audience labels."),
    "final-cta": ("Final Call to Action", "Closing call to action with phone and email."),
    "cta-band": ("Call to Action Band", "Section call to action. Variant selects the layout."),
    "newsletter": ("Newsletter", "Blog closing call to action."),
    "story": ("Story", "About story paragraphs and stats."),
    "expertise": ("Expertise", "Expertise chips."),
    "contact-card": ("Contact Card", "About page contact details."),
    "contact-panel": ("Contact Panel", "Contact details and message form."),
    "service-catalog": ("Service Catalog", "Services page card grid."),
    "ai-banner": ("AI Banner", "Benefit list and workflow diagram."),
    "software-catalog": ("Software Catalog", "Software category cards."),
    "fit-panels": ("Fit Panels", "Good-fit and poor-fit lists."),
    "process-steps": ("Process Steps", "Numbered process steps."),
    "case-studies": ("Case Studies", "Case study cards."),
    "blog-preview": ("Blog Preview", "Home page list of selected articles."),
    "article-index": ("Article Index", "Blog index built from article pages."),
    "aw-hero": ("AltWheels Hero", "AltWheels home hero."),
    "aw-nav": ("AltWheels Navigation", "In-page resource navigation."),
    "aw-patterns": ("AltWheels Patterns", "Four ways to use AI."),
    "aw-downloads": ("AltWheels Downloads", "Download cards."),
    "aw-prompts": ("AltWheels Prompts", "Copy-ready prompt list."),
    "aw-templates": ("AltWheels Templates", "Template downloads and example skill."),
    "aw-callout": ("AltWheels Directory Callout", "Link to the fleet-tool directory."),
    "aw-steps": ("AltWheels Steps", "First-session steps and share links."),
    "resource-intro": ("Resource Intro", "Back link, heading, and download for a resource page."),
    "tool-directory": ("Tool Directory", "Grouped fleet tools and a closing link."),
    "reference-list": ("Reference List", "Grouped reference links."),
}
LANDING = [
    "home-hero", "eyebrow-hero", "services-hero", "blog-hero", "work-hero", "value-props",
    "why-section", "home-services", "social-proof", "blog-preview", "article-index",
    "final-cta", "cta-band", "newsletter", "story", "expertise", "contact-card",
    "contact-panel", "service-catalog", "ai-banner", "software-catalog", "fit-panels",
    "process-steps", "case-studies",
]
RESOURCE = [
    "aw-hero", "aw-nav", "aw-patterns", "aw-downloads", "aw-prompts", "aw-templates",
    "aw-callout", "aw-steps", "resource-intro", "tool-directory", "reference-list",
]


def cdata(value):
    text = "" if value is None else str(value)
    text = text.replace("]]>", "]]]]><![CDATA[>")
    return f"<![CDATA[{text}]]>"


def title_of(field_id):
    name = re.sub(r"_(t|s|o|html|b)$", "", field_id)
    name = re.sub(r"([a-z])([A-Z])", r"\1 \2", name).replace("_", " ")
    titled = name.title()
    return titled.replace("Url", "URL").replace("Id", "ID").replace("Cta", "CTA").replace("Qr", "QR")


def input_field(fid, title, maxlength=500, required=False):
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


def textarea_field(fid, title, maxlength=4000, rows=4):
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


def image_field(fid, title):
    return f"""
\t\t\t\t<field>
\t\t\t\t\t<type>image-picker</type>
\t\t\t\t\t<id>{fid}</id>
\t\t\t\t\t<iceId></iceId>
\t\t\t\t\t<title>{title}</title>
\t\t\t\t\t<description></description>
\t\t\t\t\t<defaultValue></defaultValue>
\t\t\t\t\t<help></help>
\t\t\t\t\t<properties>
\t\t\t\t\t\t<property><name>width</name><value></value><type>int</type></property>
\t\t\t\t\t\t<property><name>height</name><value></value><type>int</type></property>
\t\t\t\t\t\t<property><name>thumbnailWidth</name><value></value><type>int</type></property>
\t\t\t\t\t\t<property><name>thumbnailHeight</name><value></value><type>int</type></property>
\t\t\t\t\t\t<property><name>imageManager</name><value>uploadImages,existingImages</value><type>datasource:image</type></property>
\t\t\t\t\t</properties>
\t\t\t\t\t<constraints>
\t\t\t\t\t\t<constraint><name>required</name><value><![CDATA[]]></value><type>boolean</type></constraint>
\t\t\t\t\t</constraints>
\t\t\t\t</field>"""


def image_sources():
    return """
\t\t<datasource>
\t\t\t<type>img-repository-upload</type>
\t\t\t<id>existingImages</id>
\t\t\t<title>Existing Images</title>
\t\t\t<interface>image</interface>
\t\t\t<properties>
\t\t\t\t<property><name>repoPath</name><value>/static-assets/</value><type>string</type></property>
\t\t\t</properties>
\t\t</datasource>
\t\t<datasource>
\t\t\t<type>img-desktop-upload</type>
\t\t\t<id>uploadImages</id>
\t\t\t<title>Upload Images</title>
\t\t\t<interface>image</interface>
\t\t\t<properties>
\t\t\t\t<property><name>repoPath</name><value>/static-assets/images/</value><type>string</type></property>
\t\t\t</properties>
\t\t</datasource>"""


def repeat_field(fid, title, children):
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


def kind_of(key, samples):
    if isinstance(samples[0], list) if samples else key.endswith("_o"):
        return "repeat"
    if key in IMAGE_FIELDS:
        return "image"
    longest = max((len(str(item)) for item in samples), default=0)
    if key.endswith("_t") and (key in PROSE or longest > 90):
        return "textarea"
    return "input"


def collect(data, spec):
    for key, value in data.items():
        if str(key).startswith("_"):
            continue
        if isinstance(value, list):
            nested = spec.get(key)
            if not isinstance(nested, dict):
                nested = {}
                spec[key] = nested
            for item in value:
                if isinstance(item, dict):
                    collect(item, nested)
        else:
            bucket = spec.get(key)
            if not isinstance(bucket, list):
                bucket = []
                spec[key] = bucket
            bucket.append("" if value is None else str(value))


def fields_xml(spec, indent_title=True):
    xml = ""
    docs = []
    for key, samples in spec.items():
        if isinstance(samples, dict):
            nested_xml, nested_docs = fields_xml(samples)
            xml += repeat_field(key, title_of(key), nested_xml)
            docs.append((key, "repeat", title_of(key), False, "minOccurs=0; maxOccurs=*", "Repeatable group."))
            for child in nested_docs:
                docs.append((f"{key}.{child[0]}", child[1], child[2], child[3], child[4], "Nested in " + key + "."))
            continue
        kind = kind_of(key, samples)
        title = title_of(key)
        if kind == "textarea":
            rows = 14 if key == "prompt_t" else 4
            limit = 50000 if key == "prompt_t" else 4000
            xml += textarea_field(key, title, limit, rows)
            docs.append((key, "textarea", title, False, f"maxlength={limit}; tokenize=false", "Plain text."))
        elif kind == "image":
            xml += image_field(key, title)
            docs.append((key, "image-picker", title, False, "imageManager=uploadImages,existingImages", "Stored path under /static-assets/."))
        else:
            limit = 80 if key.endswith("icon_s") or key == "variant_s" else 500
            xml += input_field(key, title, limit, False)
            docs.append((key, "input", title, False, f"maxlength={limit}; tokenize=false", ""))
    return xml, docs


def form_xml(name, label, description, body, datasources):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<form>
\t<title>{label}</title>
\t<description>{description}</description>
\t<objectType>component</objectType>
\t<content-type>/component/{name}</content-type>
\t<imageThumbnail></imageThumbnail>
\t<quickCreate>false</quickCreate>
\t<quickCreatePath></quickCreatePath>
\t<properties>
\t\t<property>
\t\t\t<name>display-template</name>
\t\t\t<label>Display Template</label>
\t\t\t<value>/templates/web/components/{name}.ftl</value>
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
\t\t<section>
\t\t\t<title>{label}</title>
\t\t\t<description></description>
\t\t\t<defaultOpen>true</defaultOpen>
\t\t\t<fields>
{body}
\t\t\t</fields>
\t\t</section>
\t</sections>
\t<datasources>
{datasources}
\t</datasources>
</form>
"""


def config_xml(name, label, description):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<content-type name="/component/{name}" is-wcm-type="true">
\t<label>{label}</label>
\t<form>/component/{name}</form>
\t<form-path>simple</form-path>
\t<model-instance-path>NOT-USED-BY-SIMPLE-FORM-ENGINE</model-instance-path>
\t<file-extension>xml</file-extension>
\t<content-as-folder>false</content-as-folder>
\t<previewable>false</previewable>
\t<quickCreate>false</quickCreate>
\t<quickCreatePath></quickCreatePath>
\t<noThumbnail>true</noThumbnail>
\t<image-thumbnail></image-thumbnail>
\t<description>{description}</description>
\t<paths>
\t\t<excludes>
\t\t\t<pattern>^/site/website.*</pattern>
\t\t</excludes>
\t</paths>
</content-type>
"""


def emit_values(data, indent="\t"):
    lines = []
    for key, value in data.items():
        if str(key).startswith("_"):
            continue
        if isinstance(value, list):
            if not value:
                continue
            lines.append(f'{indent}<{key} item-list="true">')
            for item in value:
                lines.append(f"{indent}\t<item>")
                lines.append(emit_values(item, indent + "\t\t"))
                lines.append(f"{indent}\t</item>")
            lines.append(f"{indent}</{key}>")
        else:
            lines.append(f"{indent}<{key}>{cdata(value)}</{key}>")
    return "\n".join(lines)


def component_xml(name, meta, data):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<component>
\t<content-type>/component/{name}</content-type>
\t<display-template>/templates/web/components/{name}.ftl</display-template>
\t<no-template-required></no-template-required>
\t<merge-strategy>inherit-levels</merge-strategy>
\t<objectGroupId>{meta['objectGroupId']}</objectGroupId>
\t<objectId>{meta['objectId']}</objectId>
\t<file-name>{meta['file-name']}</file-name>
\t<folder-name>{meta['folder-name']}</folder-name>
\t<internal-name>{cdata(meta['internal-name'])}</internal-name>
\t<createdDate>{meta['createdDate']}</createdDate>
\t<createdDate_dt>{meta['createdDate_dt']}</createdDate_dt>
\t<lastModifiedDate>{meta['lastModifiedDate']}</lastModifiedDate>
\t<lastModifiedDate_dt>{meta['lastModifiedDate_dt']}</lastModifiedDate_dt>
{emit_values(data)}
</component>
"""


def existing_meta(path):
    root = ET.parse(path).getroot()
    def text(tag):
        node = root.find(tag)
        return "" if node is None or node.text is None else node.text
    return {
        "objectGroupId": text("objectGroupId"),
        "objectId": text("objectId"),
        "file-name": text("file-name"),
        "folder-name": text("folder-name"),
        "internal-name": text("internal-name"),
        "createdDate": text("createdDate"),
        "createdDate_dt": text("createdDate_dt"),
        "lastModifiedDate": text("lastModifiedDate"),
        "lastModifiedDate_dt": text("lastModifiedDate_dt"),
    }


def new_meta(filename, internal):
    identifier = uuid.uuid5(uuid.NAMESPACE_URL, "cloudzoom:" + filename + ":" + internal)
    stamp = "2026-10-14T17:00:00.000Z"
    return {
        "objectGroupId": identifier.hex[:4],
        "objectId": str(identifier),
        "file-name": filename,
        "folder-name": "",
        "internal-name": internal[:120],
        "createdDate": stamp,
        "createdDate_dt": stamp,
        "lastModifiedDate": stamp,
        "lastModifiedDate_dt": stamp,
    }


def strings_of(data):
    found = []
    for key, value in data.items():
        if str(key).startswith("_"):
            continue
        if isinstance(value, list):
            for item in value:
                found.extend(strings_of(item))
        elif isinstance(value, str):
            found.append(value)
    return found


def check_template(name, rendered, data):
    ftl_path = ROOT / f"templates/web/components/{name}.ftl"
    corpus = ftl_path.read_text(encoding="utf-8")
    if name in {"home-hero", "why-section", "ai-banner"}:
        corpus += (ROOT / f"templates/web/fragments/diagrams/{name}.ftl").read_text(encoding="utf-8")
    owned = set()
    for value in strings_of(data):
        owned.update(value.split())
    missing = []
    for classes in re.findall(r'class="([^"]*)"', rendered):
        for token in classes.split():
            if token not in corpus and token not in owned:
                missing.append(token)
    for style in re.findall(r'style="([^"]*)"', rendered):
        if style not in corpus:
            missing.append("style:" + style[:40])
    for marker in (" hidden", "enctype=", "aria-live=", "data-copy=", 'id="downloads"', 'id="prompts"', 'id="templates"'):
        if marker in rendered and marker.strip(' =') not in corpus and marker not in corpus:
            missing.append(marker)
    if re.search(r"(?:^|\s)download(?:[\s=>]|$)", rendered) and not re.search(r"\bdownload\b", corpus):
        missing.append("download")
    if missing:
        raise SystemExit(f"{name} template is missing {sorted(set(missing))[:12]}")


def replace_flat_field(xml, field_id, replacement=""):
    pattern = re.compile(r"[ \t]*<field>\s*<type>(?:input|textarea|rte)</type>.*?</field>\s*", re.S)
    def replacer(match):
        return replacement if f"<id>{field_id}</id>" in match.group(0) else match.group(0)
    return pattern.sub(replacer, xml)


def rte_field():
    return """
\t\t\t\t<field>
\t\t\t\t\t<type>rte</type>
\t\t\t\t\t<id>body_html</id>
\t\t\t\t\t<iceId></iceId>
\t\t\t\t\t<title>Article Body</title>
\t\t\t\t\t<description></description>
\t\t\t\t\t<defaultValue></defaultValue>
\t\t\t\t\t<help></help>
\t\t\t\t\t<properties>
\t\t\t\t\t\t<property><name>height</name><value>400</value><type>int</type></property>
\t\t\t\t\t\t<property><name>forceRootBlockPTag</name><value>false</value><type>boolean</type></property>
\t\t\t\t\t\t<property><name>forcePTags</name><value>false</value><type>boolean</type></property>
\t\t\t\t\t\t<property><name>forceBRTags</name><value>false</value><type>boolean</type></property>
\t\t\t\t\t\t<property><name>rteConfiguration</name><value>generic</value><type>string</type></property>
\t\t\t\t\t\t<property><name>imageManager</name><value>uploadImages,existingImages</value><type>datasource:image</type></property>
\t\t\t\t\t</properties>
\t\t\t\t\t<constraints>
\t\t\t\t\t\t<constraint><name>required</name><value><![CDATA[]]></value><type>boolean</type></constraint>
\t\t\t\t\t</constraints>
\t\t\t\t</field>"""


def node_field(fid, title, manager, types):
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
\t\t\t\t\t\t<property><name>maxSize</name><value></value><type>int</type></property>
\t\t\t\t\t\t<property><name>itemManager</name><value>{manager}</value><type>datasource:item</type></property>
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


def selector_item(path, label):
    return f"""\t\t<item>
\t\t\t<key>{path}</key>
\t\t\t<value>{cdata(label)}</value>
\t\t\t<include>{path}</include>
\t\t\t<disableFlattening>false</disableFlattening>
\t\t</item>"""


def main():
    section_root = ROOT / "site/components/sections"
    grouped = {}
    instances = []
    for rel, (kind, extractor) in remodel.SECTION_JOBS.items():
        path = section_root / rel
        source = ET.parse(path).getroot().findtext("markup_html")
        data = extractor(remodel.main_root(source), source)
        rendered = remodel.RENDERERS[kind](data)
        remodel.check_pair(rel, source, rendered)
        if "_svg" in data:
            fragment = ROOT / f"templates/web/fragments/diagrams/{kind}.ftl"
            fragment.parent.mkdir(parents=True, exist_ok=True)
            fragment.write_text(data["_svg"], encoding="utf-8")
        check_template(kind, rendered, data)
        grouped.setdefault(kind, {})
        collect(data, grouped[kind])
        instances.append((path, kind, data, existing_meta(path)))

    resource_pages = {
        "altwheels/index.xml": [
            ("01-hero.xml", "aw-hero", remodel.extract_aw_hero),
            ("02-nav.xml", "aw-nav", remodel.extract_aw_nav),
            ("03-patterns.xml", "aw-patterns", remodel.extract_aw_patterns),
            ("04-downloads.xml", "aw-downloads", remodel.extract_aw_downloads),
            ("05-prompts.xml", "aw-prompts", remodel.extract_aw_prompts),
            ("06-templates.xml", "aw-templates", remodel.extract_aw_templates),
            ("07-callout.xml", "aw-callout", remodel.extract_aw_callout),
            ("08-steps.xml", "aw-steps", remodel.extract_aw_steps),
        ],
        "altwheels/fleet-tools/index.xml": [
            ("01-intro.xml", "resource-intro", remodel.extract_resource_intro),
            ("02-directory.xml", "tool-directory", remodel.extract_tool_directory),
        ],
        "altwheels/references/index.xml": [
            ("01-intro.xml", "resource-intro", remodel.extract_resource_intro),
            ("02-list.xml", "reference-list", remodel.extract_reference_list),
        ],
    }
    resource_sections = {}
    for rel, jobs in resource_pages.items():
        source = ET.parse(ROOT / "site/website" / rel).getroot().findtext("main_html")
        children = remodel.main_root(source).elements()
        folder = "altwheels" if rel == "altwheels/index.xml" else str(Path(rel).parent)
        refs = []
        for child, (filename, kind, extractor) in zip(children, jobs):
            data = extractor(child, source)
            rendered = remodel.RENDERERS[kind](data)
            rendered_node = remodel.parse_html(rendered).elements()[0]
            diff = remodel.first_diff(remodel.walk(rendered_node), remodel.walk(child))
            if diff:
                raise SystemExit(diff)
            check_template(kind, rendered, data)
            grouped.setdefault(kind, {})
            collect(data, grouped[kind])
            path = section_root / folder / filename
            label = data.get("heading_t") or data.get("title_t") or data.get("eyebrow_t") or kind
            meta = new_meta(str(path.relative_to(section_root)), label)
            instances.append((path, kind, data, meta))
            refs.append((f"/site/components/sections/{folder}/{filename}", meta["internal-name"]))
        resource_sections[rel] = refs

    grouped["blog-preview"] = {}
    collect({
        "title_t": "FROM THE BLOG",
        "subtitle_t": "Practical articles on AI-assisted software delivery, QA automation, and building systems that hold up in production.",
        "linkLabel_t": "View all articles",
        "linkUrl_s": "/blog",
    }, grouped["blog-preview"])
    grouped["article-index"] = {}

    docs = ["# Section and chrome components\n", "Header and footer stay shared components. Each visible region is its own component type, referenced in order from the page `sections_o` field. Plain text uses `input` or `textarea`. Lists use repeat groups. Images use `image-picker`. Article body copy uses `rte`.\n"]
    for name in LANDING + RESOURCE:
        label, description = LABELS[name]
        spec = grouped.get(name, {})
        body, rows = fields_xml(spec)
        base = input_field("file-name", "File Name", 50, True) + input_field("internal-name", "Internal Name", 120, True)
        datasources = image_sources() if any(key in IMAGE_FIELDS for key in spec) else ""
        type_dir = ROOT / "config/studio/content-types/component" / name
        type_dir.mkdir(parents=True, exist_ok=True)
        (type_dir / "config.xml").write_text(config_xml(name, label, description), encoding="utf-8")
        (type_dir / "form-definition.xml").write_text(form_xml(name, label, description, base + body, datasources), encoding="utf-8")
        docs.append(f"## `/component/{name}` — {label}\n\n{description}\n\n- Form: `config/studio/content-types/component/{name}/form-definition.xml`\n- Display template: `/templates/web/components/{name}.ftl`\n")
        docs.append("| Name | Type | Description | Required | Constraints | Notes |\n|------|------|-------------|----------|-------------|-------|")
        docs.append("| file-name | input | File Name | true | maxlength=50; tokenize=false | |")
        docs.append("| internal-name | input | Internal Name | true | maxlength=120; tokenize=false | |")
        for row in rows:
            docs.append(f"| {row[0]} | {row[1]} | {row[2]} | {'true' if row[3] else 'false'} | {row[4]} | {row[5]} |")
        docs.append("")

    for path, kind, data, meta in instances:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(component_xml(kind, meta, data), encoding="utf-8")

    preview = section_root / "home/06-blog-preview.xml"
    meta = existing_meta(preview)
    preview.write_text(component_xml("blog-preview", meta, {
        "title_t": "FROM THE BLOG",
        "subtitle_t": "Practical articles on AI-assisted software delivery, QA automation, and building systems that hold up in production.",
        "linkLabel_t": "View all articles",
        "linkUrl_s": "/blog",
    }), encoding="utf-8")
    index = section_root / "blog/02-article-index.xml"
    index.write_text(component_xml("article-index", existing_meta(index), {}), encoding="utf-8")

    shutil.rmtree(ROOT / "config/studio/content-types/component/section")
    (ROOT / "templates/web/components/section.ftl").unlink()

    landing_types = ",".join(f"/component/{name}" for name in LANDING)
    resource_types = ",".join(f"/component/{name}" for name in RESOURCE)
    landing_form = ROOT / "config/studio/content-types/page/landing/form-definition.xml"
    landing_xml = replace_flat_field(landing_form.read_text(encoding="utf-8"), "headLinks_html")
    landing_xml = landing_xml.replace(
        "<property><name>contentTypes</name><value>/component/section</value><type>contentTypes</type></property>",
        f"<property><name>contentTypes</name><value>{landing_types}</value><type>contentTypes</type></property>",
    )
    landing_form.write_text(landing_xml, encoding="utf-8")

    article_form = ROOT / "config/studio/content-types/page/article/form-definition.xml"
    article_xml = replace_flat_field(article_form.read_text(encoding="utf-8"), "headLinks_html")
    article_xml = replace_flat_field(article_xml, "body_html", rte_field() + "\n")
    if "existingImages" not in article_xml:
        article_xml = article_xml.replace("\t<datasources>", "\t<datasources>" + image_sources(), 1)
    article_form.write_text(article_xml, encoding="utf-8")

    resource_form = ROOT / "config/studio/content-types/page/resource/form-definition.xml"
    resource_xml = replace_flat_field(resource_form.read_text(encoding="utf-8"), "headLinks_html")
    resource_xml = replace_flat_field(resource_xml, "main_html")
    resource_xml = resource_xml.replace(
        "\t\t\t\t<field>\n\t\t\t\t\t<type>node-selector</type>\n\t\t\t\t\t<id>header_o</id>",
        node_field("sections_o", "Sections", "sectionComponents", resource_types) + "\n\t\t\t\t<field>\n\t\t\t\t\t<type>node-selector</type>\n\t\t\t\t\t<id>header_o</id>",
        1,
    )
    if "sectionComponents" not in resource_xml:
        resource_xml = resource_xml.replace(
            "\t</datasources>",
            """\t\t<datasource>
\t\t\t<type>shared-content</type>
\t\t\t<id>sectionComponents</id>
\t\t\t<title>Sections</title>
\t\t\t<interface>item</interface>
\t\t\t<properties>
\t\t\t\t<property><name>repoPath</name><value>/site/components/sections/</value><type>undefined</type></property>
\t\t\t\t<property><name>browsePath</name><value>/site/components/sections/</value><type>undefined</type></property>
\t\t\t\t<property><name>type</name><value></value><type>undefined</type></property>
\t\t\t\t<property><name>enableCreateNew</name><value>true</value><type>boolean</type></property>
\t\t\t\t<property><name>enableBrowseExisting</name><value>true</value><type>boolean</type></property>
\t\t\t\t<property><name>enableSearchExisting</name><value>true</value><type>boolean</type></property>
\t\t\t</properties>
\t\t</datasource>
\t</datasources>""",
            1,
        )
    resource_form.write_text(resource_xml, encoding="utf-8")

    for page in (ROOT / "site/website").rglob("index.xml"):
        xml = page.read_text(encoding="utf-8")
        xml = re.sub(r"\t<headLinks_html><!\[CDATA\[.*?\]\]></headLinks_html>\n", "", xml, flags=re.S)
        xml = re.sub(r"\t<main_html><!\[CDATA\[.*?\]\]></main_html>\n", "", xml, flags=re.S)
        rel = str(page.relative_to(ROOT / "site/website"))
        if rel in resource_sections:
            items = "\n".join(selector_item(path, label) for path, label in resource_sections[rel])
            block = f'\t<sections_o item-list="true">\n{items}\n\t</sections_o>\n'
            xml = xml.replace("\t<header_o", block + "\t<header_o") if "<header_o" in xml else xml.replace("</page>", block + "</page>")
        if "<body_html>" in xml:
            def unwrap(match):
                inner = match.group(1)
                inner = re.sub(r"^\s*<article class=\"article-body\">", "", inner)
                inner = re.sub(r"</article>\s*$", "", inner)
                return "<body_html>" + cdata(inner.strip("\n")) + "</body_html>"
            xml = re.sub(r"<body_html><!\[CDATA\[(.*?)\]\]></body_html>", unwrap, xml, flags=re.S)
        page.write_text(xml, encoding="utf-8")

    write_heads_and_pages()
    previous = (ROOT / "docs/components.md").read_text(encoding="utf-8")
    chrome = previous[previous.index("## `/component/footer`"):previous.index("## `/component/section`")]
    (ROOT / "docs/components.md").write_text("\n".join(docs) + "\n" + chrome, encoding="utf-8")
    write_other_docs()
    outline = ROOT / "docs/_altwheels-outline.txt"
    if outline.exists():
        outline.unlink()
    print("wrote", len(instances) + 2, "components")


def write_heads_and_pages():
    fragments = ROOT / "templates/web/fragments"
    (fragments / "head-marketing.ftl").write_text(
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Manrope:wght@400;500;600;700&display=swap">\n'
        '<link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web/src/regular/style.css">\n',
        encoding="utf-8",
    )
    (fragments / "head-blog.ftl").write_text(
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">\n'
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1/src/regular/style.css">\n'
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1/src/bold/style.css">\n',
        encoding="utf-8",
    )
    (fragments / "head-article.ftl").write_text(
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">\n'
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1/src/regular/style.css">\n',
        encoding="utf-8",
    )
    (fragments / "head-altwheels.ftl").write_text(
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Manrope:wght@400;500;600;700&display=swap">\n',
        encoding="utf-8",
    )
    landing = ROOT / "templates/web/pages/landing.ftl"
    text = landing.read_text(encoding="utf-8").replace(
        "  ${(contentModel.headLinks_html)!\"\"}\n",
        "  <#if (contentModel.stylesheet_s!\"\")?contains(\"blog.css\")>\n    <#include \"/templates/web/fragments/head-blog.ftl\">\n  <#else>\n    <#include \"/templates/web/fragments/head-marketing.ftl\">\n  </#if>\n",
    )
    landing.write_text(text, encoding="utf-8")
    article = ROOT / "templates/web/pages/article.ftl"
    text = article.read_text(encoding="utf-8").replace(
        "  ${(contentModel.headLinks_html)!\"\"}\n",
        "  <#include \"/templates/web/fragments/head-article.ftl\">\n",
    ).replace(
        "${(contentModel.body_html)!\"\"}\n",
        "<article class=\"article-body\">\n<@crafter.div $field=\"body_html\">${contentModel.body_html!\"\"}</@crafter.div>\n</article>\n",
    )
    article.write_text(text, encoding="utf-8")
    resource = ROOT / "templates/web/pages/resource.ftl"
    text = resource.read_text(encoding="utf-8").replace(
        "  ${(contentModel.headLinks_html)!\"\"}\n",
        "  <#include \"/templates/web/fragments/head-altwheels.ftl\">\n",
    ).replace(
        "${(contentModel.main_html)!\"\"}\n",
        "<main id=\"main\">\n<@crafter.renderComponentCollection $field=\"sections_o\" />\n</main>\n",
    )
    resource.write_text(text, encoding="utf-8")


def write_other_docs():
    pages = ROOT / "docs/pages.md"
    text = pages.read_text(encoding="utf-8")
    text = text.replace("| headLinks_html | textarea | Head Links | false | maxlength=8000; tokenize=false |  |\n", "")
    text = text.replace("| body_html | textarea | Article Body HTML | false | maxlength=500000; tokenize=false |  |", "| body_html | rte | Article Body | false | rteConfiguration=generic; forceRootBlockPTag=false | Author HTML inside `article-body`. Stored in CDATA. |")
    text = text.replace("| main_html | textarea | Main HTML | false | maxlength=500000; tokenize=false |  |\n", "| sections_o | node-selector | Sections | false | itemManager=sectionComponents | AltWheels region components. |\n")
    text = text.replace("| sections_o | node-selector | Sections | false | itemManager=sectionComponents; contentTypes=/component/section | List. Allowed: /component/section. itemManager=sectionComponents. |", "| sections_o | node-selector | Sections | false | itemManager=sectionComponents | Landing region components. See `components.md`. |")
    pages.write_text(text, encoding="utf-8")
    readme = ROOT / "docs/README.md"
    readme_text = readme.read_text(encoding="utf-8")
    readme_text = readme_text.replace(
        "- `/page/article` for the five posts. Card fields feed the home preview and the blog index.\n- `/page/resource` for the three AltWheels pages. The original `<main>` is stored in `main_html`.\n- `/component/header` and `/component/footer`, chosen by the level descriptor. AltWheels has its own descriptor.\n- `/component/section` for each top-level region. `layout_s=html` keeps the original markup and class names in `markup_html`. Blog regions use `blog-preview` and `article-index`, which list article content items instead of copying cards.",
        "- `/page/article` for the five posts. Card fields feed the home preview and the blog index. `body_html` is an `rte` field for the article copy; the `article-body` wrapper stays in the template.\n- `/page/resource` for the three AltWheels pages. Each region is a component in `sections_o`.\n- `/component/header` and `/component/footer`, chosen by the level descriptor. AltWheels has its own descriptor.\n- One content type per region (hero, card grid, call to action, AltWheels block, and so on). Headings, links, and list items are fields. Diagrams and font links live in templates.",
    )
    readme.write_text(readme_text, encoding="utf-8")
    items = ROOT / "docs/items.md"
    items.write_text(
        items.read_text(encoding="utf-8").replace(
            "This site does not use separate item content types. Repeatable groups inside header, footer, and article content types hold the nested items. Section HTML is stored as one `markup_html` field so the original element tree, classes, and nesting stay intact.",
            "This site does not use separate item content types. Repeatable groups inside header, footer, article, and region components hold the nested items. Header, footer, and article groups are listed below. Region lists are documented with each component in `components.md`.",
        ),
        encoding="utf-8",
    )
    diagram = ROOT / "docs/ARCHITECTURE_DIAGRAM.md"
    diagram_text = diagram.read_text(encoding="utf-8")
    diagram_text = diagram_text.replace(
        "    subgraph Sections\n        SEC[\"/component/section\"]\n    end",
        "    subgraph Sections\n        REG[\"Region components\"]\n        AW[\"AltWheels components\"]\n    end",
    )
    diagram_text = diagram_text.replace("    LAND -->|sections_o| SEC", "    LAND -->|sections_o| REG\n    RES -->|sections_o| AW")
    diagram_text = diagram_text.replace(
        "- `/component/section` is the only section type. `layout_s` is `html`, `blog-preview`, or `article-index`.\n- `/page/article` stores the article body in `body_html` and card fields used by the blog index and home preview.\n- `/page/resource` stores the AltWheels `<main>` in `main_html`.",
        "- Each region is its own component type, listed in `components.md`.\n- `/page/article` stores author copy in `body_html` (`rte`). Card fields feed the blog index and home preview.\n- `/page/resource` renders AltWheels regions from `sections_o`.",
    )
    diagram_text = diagram_text.replace("| Section components | 1 (`/component/section`) |", "| Section components | one type per region (`components.md`) |")
    diagram.write_text(diagram_text, encoding="utf-8")
    build = ROOT / "tools/build_site.py"
    source = build.read_text(encoding="utf-8")
    needle = "def main() -> None:\n    if not MIRROR.exists():\n"
    guard = (
        "def main() -> None:\n"
        "    raise SystemExit(\n"
        "        \"build_site.py stores page regions in markup text areas. \"\n"
        "        \"The content model is structured now; do not regenerate it with this script.\"\n"
        "    )\n"
        "    if not MIRROR.exists():\n"
    )
    if needle not in source:
        raise SystemExit("could not guard build_site.py")
    build.write_text(source.replace(needle, guard, 1), encoding="utf-8")


if __name__ == "__main__":
    main()
