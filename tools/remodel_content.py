#!/usr/bin/env python3
"""Replace markup text areas with structured Crafter content types.

Reads the current section and page XML, checks that a structured rendering
matches the original element tree, then writes content types, templates,
and content items.
"""

from __future__ import annotations

import html
import re
import shutil
import uuid
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INLINE = {"a", "strong", "em", "span", "i", "b", "br", "img", "button", "small"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class Node:
    def __init__(self, tag, attrs):
        self.tag = tag
        self.attrs = {}
        for key, value in attrs:
            self.attrs[key] = "" if value is None else value
        self.children = []

    def elements(self):
        return [child for child in self.children if not isinstance(child, str)]

    def cls(self):
        return self.attrs.get("class", "")

    def has_class(self, name):
        return name in self.cls().split()

    def first(self, tag=None, class_name=None):
        found = self.all(tag, class_name)
        if not found:
            raise LookupError(f"missing <{tag} class={class_name}> under <{self.tag} class={self.cls()}>")
        return found[0]

    def all(self, tag=None, class_name=None):
        found = []
        for child in self.elements():
            matches = (tag is None or child.tag == tag) and (class_name is None or child.has_class(class_name))
            if matches:
                found.append(child)
            found.extend(child.all(tag, class_name))
        return found

    def text(self):
        parts = []
        for child in self.children:
            if isinstance(child, str):
                parts.append(child)
            else:
                parts.append(child.text())
        return re.sub(r"\s+", " ", "".join(parts)).strip()

    def direct(self):
        return re.sub(r"\s+", " ", "".join(child for child in self.children if isinstance(child, str))).strip()


class Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root", [])
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                self.stack = self.stack[:index]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def parse_html(value):
    builder = Builder()
    builder.feed(value)
    builder.close()
    return builder.root


def text_node(raw):
    collapsed = re.sub(r"\s+", " ", raw).strip()
    if not collapsed:
        return None
    return ("text", collapsed)


def walk(node):
    if isinstance(node, str):
        return text_node(node)
    if node.tag == "pre":
        exact = "".join(child for child in node.children if isinstance(child, str))
        return (node.tag, tuple(sorted(node.attrs.items())), [("exact", exact)])
    children = []
    for child in node.children:
        walked = text_node(child) if isinstance(child, str) else walk(child)
        if walked:
            children.append(walked)
    if node.tag == "root":
        return children
    return (node.tag, tuple(sorted(node.attrs.items())), children)


def canon(value):
    return walk(parse_html(value))


def first_diff(left, right, path="$"):
    if left == right:
        return None
    if type(left) is not type(right) or not isinstance(left, (list, tuple)):
        return f"{path}\n  got: {left!r}\n  exp: {right!r}"
    if isinstance(left, tuple) and len(left) == 3 and isinstance(left[2], list):
        if not (isinstance(right, tuple) and len(right) == 3):
            return f"{path}\n  got: {left[:2]!r}\n  exp: {right!r}"
        if left[0] != right[0] or left[1] != right[1]:
            return f"{path}\n  got: {left[:2]!r}\n  exp: {right[:2]!r}"
        return first_diff(left[2], right[2], path + "/" + str(left[0]))
    if len(left) != len(right):
        return f"{path} length {len(left)} != {len(right)}\n  got: {describe(left)}\n  exp: {describe(right)}"
    for index, (item, other) in enumerate(zip(left, right)):
        found = first_diff(item, other, f"{path}[{index}]")
        if found:
            return found
    return f"{path} mismatch"


def describe(nodes):
    lines = []
    for node in nodes[:8]:
        if isinstance(node, tuple) and len(node) == 3 and isinstance(node[2], list):
            lines.append(f"<{node[0]} {dict(node[1])}>")
        else:
            lines.append(repr(node)[:120])
    return "\n".join(lines)


def esc(value):
    return html.escape(value or "", quote=True)


def tag(name, attrs=None, inner="", void=False):
    attrs = attrs or {}
    bits = []
    for key, value in attrs.items():
        if value is None or value is False:
            continue
        if value is True:
            bits.append(f" {key}")
        else:
            bits.append(f' {key}="{esc(str(value))}"')
    body = "".join(bits)
    if void:
        return f"<{name}{body}>"
    return f"<{name}{body}>{inner}</{name}>"


def svg_of(value):
    match = re.search(r"<svg\b.*?</svg>", value, re.S)
    if not match:
        raise SystemExit("expected an svg diagram")
    return match.group(0)


def link_parts(node):
    anchor = None
    before, after = [], []
    seen = False
    for child in node.children:
        if not isinstance(child, str) and child.tag == "a" and anchor is None:
            anchor = child
            seen = True
            continue
        (after if seen else before).append(child.text() if not isinstance(child, str) else child)
    before_text = re.sub(r"\s+", " ", "".join(before)).strip()
    after_text = re.sub(r"\s+", " ", "".join(after)).strip()
    return before_text, anchor, after_text


def split_br(node):
    lines, current = [], []
    for child in node.children:
        if not isinstance(child, str) and child.tag == "br":
            lines.append(re.sub(r"\s+", " ", "".join(current)).strip())
            current = []
        elif isinstance(child, str):
            current.append(child)
        else:
            current.append(child.text())
    lines.append(re.sub(r"\s+", " ", "".join(current)).strip())
    return lines


# ---------- extractors ----------

def extract_home_hero(root, source):
    content = root.first(class_name="hero-content")
    row = content.first(class_name="hero-cta-row")
    primary, secondary = row.all("a")
    chips = []
    for chip in content.first(class_name="trust-chips").all(class_name="trust-chip"):
        chips.append({"icon_s": chip.first("i").cls(), "label_t": chip.first("span").text()})
    return {
        "title_t": content.first("h1").text(),
        "subtitle_t": content.first(class_name="hero-subtitle").text(),
        "primaryLabel_t": primary.direct() or primary.text().replace(primary.first("i").text(), "").strip(),
        "primaryUrl_s": primary.attrs["href"],
        "secondaryLabel_t": secondary.text(),
        "secondaryUrl_s": secondary.attrs["href"],
        "chips_o": chips,
        "_svg": svg_of(source),
    }


def extract_eyebrow_hero(root, _source):
    return {
        "eyebrow_t": root.first(class_name="hero-eyebrow").text(),
        "title_t": root.first(class_name="hero-heading").text(),
        "subtitle_t": root.first(class_name="hero-subtitle").text(),
    }


def extract_services_hero(root, _source):
    paragraph = root.first(class_name="hero-subtext")
    before, anchor, after = link_parts(paragraph)
    return {
        "eyebrow_t": root.first(class_name="hero-eyebrow").text(),
        "title_t": root.first(class_name="hero-heading").text(),
        "textBefore_t": before,
        "linkLabel_t": anchor.text(),
        "linkUrl_s": anchor.attrs["href"],
        "textAfter_t": after,
    }


def extract_blog_hero(root, _source):
    lines = split_br(root.first("h1"))
    return {
        "eyebrow_t": root.first(class_name="blog-hero-eyebrow").text(),
        "titleLine1_t": lines[0],
        "titleLine2_t": lines[1],
        "subtitle_t": root.first(class_name="blog-hero-sub").text(),
    }


def extract_work_hero(root, _source):
    return {
        "eyebrow_t": root.first(class_name="eyebrow-pill").text(),
        "title_t": root.first("h1").text(),
        "subtitle_t": root.first(class_name="page-hero-subtitle").text(),
    }


def extract_value_props(root, _source):
    items = []
    for card in root.all(class_name="stat-card"):
        items.append({
            "icon_s": card.first("i").cls(),
            "title_t": card.first(class_name="stat-number").text(),
            "text_t": card.first(class_name="stat-label").text(),
        })
    return {"items_o": items}


def extract_why(root, source):
    items = []
    for item in root.all(class_name="benefit-item"):
        items.append({"icon_s": item.first("i").cls(), "text_t": item.first(class_name="benefit-text").text()})
    return {
        "heading_t": root.first(class_name="section-heading").text(),
        "subheading_t": root.first(class_name="section-subheading").text(),
        "items_o": items,
        "_svg": svg_of(source),
    }


def extract_home_services(root, _source):
    cards = []
    for card in root.all(class_name="service-card"):
        link = card.all("a")
        cards.append({
            "icon_s": card.first("i").cls(),
            "title_t": card.first(class_name="service-name").text(),
            "text_t": card.first(class_name="service-description").text(),
            "linkLabel_t": link[0].direct() if link else "",
            "linkUrl_s": link[0].attrs.get("href", "") if link else "",
        })
    links = []
    for anchor in root.first(class_name="services-link").all("a"):
        links.append({"label_t": anchor.direct(), "url_s": anchor.attrs["href"]})
    return {
        "heading_t": root.first(class_name="section-title").text(),
        "subtitle_t": root.first(class_name="section-subtitle").text(),
        "cards_o": cards,
        "links_o": links,
    }


def extract_social(root, _source):
    logos = [{"label_t": item.text()} for item in root.all(class_name="logo-item")]
    return {
        "avatar_t": root.first(class_name="founder-avatar").text(),
        "name_t": root.first(class_name="founder-name").text(),
        "role_t": root.first(class_name="founder-title").text(),
        "quote_t": root.first(class_name="quote-text").text(),
        "logos_o": logos,
    }


def extract_final_cta(root, _source, variant):
    button = root.first("a")
    contact = root.first(class_name="final-cta-contact")
    phone, email = contact.all("a")
    return {
        "variant_s": variant,
        "heading_t": root.first(class_name="final-cta-heading").text(),
        "subtext_t": root.first(class_name="final-cta-subtext").text(),
        "ctaLabel_t": button.direct(),
        "ctaUrl_s": button.attrs["href"],
        "phoneLabel_t": phone.text(),
        "phoneUrl_s": phone.attrs["href"],
        "emailLabel_t": email.text(),
        "emailUrl_s": email.attrs["href"],
    }


def extract_cta_band(root, _source, variant):
    button = root.all("a")[-1]
    sub = root.all(class_name="cta-subtext")
    return {
        "variant_s": variant,
        "heading_t": root.first(class_name="cta-heading").text(),
        "subtext_t": sub[0].text() if sub else "",
        "ctaLabel_t": button.direct(),
        "ctaUrl_s": button.attrs["href"],
    }


def extract_newsletter(root, _source):
    button = root.first("a")
    return {
        "heading_t": root.first(class_name="newsletter-title").text(),
        "subtext_t": root.first(class_name="newsletter-sub").text(),
        "ctaLabel_t": button.direct(),
        "ctaUrl_s": button.attrs["href"],
        "note_t": root.first(class_name="newsletter-note").text(),
    }


def extract_story(root, _source):
    paragraphs = [{"text_t": item.text()} for item in root.first(class_name="story-content").all("p")]
    stats = []
    for item in root.all(class_name="stat-item"):
        stats.append({
            "value_t": item.first(class_name="stat-value").text(),
            "label_t": item.first(class_name="stat-label").text(),
        })
    return {"heading_t": root.first(class_name="story-heading").text(), "paragraphs_o": paragraphs, "stats_o": stats}


def extract_expertise(root, _source):
    chips = []
    for chip in root.all(class_name="expertise-chip"):
        chips.append({"icon_s": chip.first("i").cls(), "label_t": chip.first("span").text()})
    return {"heading_t": root.first(class_name="expertise-heading").text(), "chips_o": chips}


def extract_contact_card(root, _source):
    items = []
    for item in root.all(class_name="contact-item"):
        value = item.first(class_name="contact-value")
        anchors = value.all("a")
        items.append({
            "icon_s": item.first("i").cls(),
            "label_t": item.first(class_name="contact-label").text(),
            "value_t": anchors[0].text() if anchors else value.text(),
            "url_s": anchors[0].attrs.get("href", "") if anchors else "",
        })
    linkedin = root.first(class_name="contact-linkedin").first("a")
    return {
        "heading_t": root.first(class_name="contact-heading").text(),
        "items_o": items,
        "linkedinLabel_t": linkedin.direct(),
        "linkedinUrl_s": linkedin.attrs.get("href", ""),
        "note_t": root.first(class_name="contact-subtext").text(),
    }


def extract_contact_panel(root, _source):
    methods = []
    for method in root.all(class_name="contact-method"):
        value = method.first(class_name="contact-method-value")
        anchors = value.all("a")
        methods.append({
            "icon_s": method.first("i").cls(),
            "label_t": method.first(class_name="contact-method-label").text(),
            "value_t": anchors[0].text() if anchors else value.text(),
            "url_s": anchors[0].attrs.get("href", "") if anchors else "",
        })
    linkedin = root.first(class_name="linkedin-button")
    form = root.first("form")
    fields = []
    for group in form.all(class_name="form-group"):
        control = group.first("input") if group.all("input") else group.first("textarea")
        fields.append({
            "label_t": group.first("label").text(),
            "name_s": control.attrs.get("name", ""),
            "type_s": "textarea" if control.tag == "textarea" else control.attrs.get("type", "text"),
            "placeholder_t": control.attrs.get("placeholder", ""),
            "required_s": "true" if "required" in control.attrs else "",
        })
    return {
        "heading_t": root.first(class_name="contact-heading").text(),
        "intro_t": root.first(class_name="contact-intro").text(),
        "methods_o": methods,
        "linkedinLabel_t": linkedin.direct(),
        "linkedinUrl_s": linkedin.attrs.get("href", ""),
        "boxTitle_t": root.first(class_name="cta-box-title").text(),
        "boxText_t": root.first(class_name="cta-box-text").text(),
        "formHeading_t": root.first(class_name="form-heading").text(),
        "formSubtitle_t": root.first(class_name="form-subtitle").text(),
        "formEmail_s": form.attrs.get("action", "").removeprefix("mailto:"),
        "submitLabel_t": form.first("button").text(),
        "fields_o": fields,
    }


def extract_service_catalog(root, _source):
    cards = []
    for card in root.all(class_name="service-card"):
        cards.append({
            "icon_s": card.first("i").cls(),
            "title_t": card.first(class_name="service-title").text(),
            "text_t": card.first(class_name="service-description").text(),
            "tags_o": [{"label_t": tag.text()} for tag in card.all(class_name="service-tag")],
        })
    return {"heading_t": root.first(class_name="section-heading").text(), "cards_o": cards}


def extract_ai_banner(root, source):
    items = []
    for item in root.all(class_name="ai-benefit-item"):
        text = item.first(class_name="ai-benefit-text")
        items.append({
            "icon_s": item.first("i").cls(),
            "title_t": text.first("strong").text(),
            "text_t": text.direct(),
        })
    return {"heading_t": root.first("h2").text(), "items_o": items, "_svg": svg_of(source)}


def extract_software_catalog(root, _source):
    cards = []
    for card in root.all(class_name="software-card"):
        cards.append({
            "icon_s": card.first("i").cls(),
            "title_t": card.first(class_name="software-title").text(),
            "text_t": card.first(class_name="software-description").text(),
            "tags_o": [{"label_t": tag.text()} for tag in card.all(class_name="software-tag")],
        })
    return {
        "kicker_t": root.first(class_name="section-kicker").text(),
        "heading_t": root.first(class_name="section-heading").text(),
        "subtitle_t": root.first(class_name="section-subtitle").text(),
        "cards_o": cards,
    }


def extract_fit(root, _source):
    panels = []
    for panel in root.all(class_name="fit-panel"):
        panels.append({
            "title_t": panel.first("h2").text(),
            "icon_s": panel.first("i").cls(),
            "items_o": [{"text_t": item.first("span").text()} for item in panel.all("li")],
        })
    return {"panels_o": panels}


def extract_process(root, _source):
    steps = []
    for step in root.all(class_name="process-step"):
        steps.append({
            "number_t": step.first(class_name="process-step-number").text(),
            "title_t": step.first("h3").text(),
            "text_t": step.first("p").text(),
        })
    return {
        "kicker_t": root.first(class_name="section-kicker").text(),
        "heading_t": root.first(class_name="section-heading").text(),
        "subtitle_t": root.first(class_name="section-subtitle").text(),
        "steps_o": steps,
    }


def extract_cases(root, _source):
    items = []
    banner = root.first(class_name="ai-acceleration-banner")
    for card in root.elements()[0].elements()[0].elements():
        if card.has_class("ai-acceleration-banner"):
            continue
        featured = card.has_class("case-featured")
        body = card.first(class_name="case-featured-content") if featured else card
        title = body.first(class_name="case-title")
        badge = body.all(class_name="case-badge")
        link = body.all(class_name="case-external-link")
        split = body.all(class_name="case-stat")
        single = body.all(class_name="case-stat-single")
        kicker = body.all(class_name="featured-label")
        items.append({
            "style_s": "featured" if featured else "card",
            "titleTag_s": title.tag,
            "kicker_t": kicker[0].text() if kicker else "",
            "title_t": title.text(),
            "badge_t": badge[0].text() if badge else "",
            "linkLabel_t": link[0].direct() if link else "",
            "linkUrl_s": link[0].attrs.get("href", "") if link else "",
            "linkTarget_s": link[0].attrs.get("target", "") if link else "",
            "statBefore_t": split[0].first(class_name="stat-before").text() if split else "",
            "statArrow_t": split[0].first(class_name="stat-arrow").text() if split else "",
            "statAfter_t": split[0].first(class_name="stat-after").text() if split else "",
            "stat_t": single[0].text() if single else "",
            "text_t": body.first(class_name="case-description").text(),
            "tags_o": [{"label_t": tag.text()} for tag in body.all(class_name="tech-tag")],
        })
    return {
        "cases_o": items,
        "bannerTitle_t": banner.first(class_name="ai-banner-title").text(),
        "bannerText_t": banner.first(class_name="ai-banner-text").text(),
    }


def anchor_data(anchor):
    label = anchor.direct() or anchor.text()
    return {
        "label_t": label,
        "url_s": anchor.attrs.get("href", ""),
        "class_s": anchor.cls(),
        "download_s": "true" if "download" in anchor.attrs else "",
    }


def extract_aw_hero(root, _source):
    column = root.first(class_name="hero-grid").elements()[0]
    brand = column.first(class_name="brand-line")
    strong = brand.first("strong").text()
    rest = [line for line in split_br(brand) if line and line != strong][-1]
    title = split_br(column.first("h1"))
    buttons = column.first(class_name="button-row").all("a")
    figure = root.first("figure")
    image = figure.first("img")
    return {
        "eyebrow_t": column.first(class_name="eyebrow").text(),
        "brandStrong_t": strong,
        "brandRest_t": rest,
        "titleLine1_t": title[0],
        "titleLine2_t": title[1],
        "lead_t": column.first(class_name="lead").text(),
        "primaryLabel_t": buttons[0].text(),
        "primaryUrl_s": buttons[0].attrs["href"],
        "primaryDownload_s": "true" if "download" in buttons[0].attrs else "",
        "secondaryLabel_t": buttons[1].text(),
        "secondaryUrl_s": buttons[1].attrs["href"],
        "meta_t": column.first(class_name="meta").text(),
        "image_s": image.attrs.get("src", ""),
        "imageAlt_t": image.attrs.get("alt", ""),
        "imageWidth_s": image.attrs.get("width", ""),
        "imageHeight_s": image.attrs.get("height", ""),
        "imageUrl_s": figure.first("a").attrs.get("href", ""),
        "imageAria_t": figure.first("a").attrs.get("aria-label", ""),
        "caption_t": figure.first("figcaption").text(),
    }


def extract_aw_nav(root, _source):
    return {
        "ariaLabel_t": root.attrs.get("aria-label", ""),
        "links_o": [{"label_t": anchor.text(), "url_s": anchor.attrs["href"]} for anchor in root.all("a")],
    }


def extract_aw_patterns(root, _source):
    items = []
    for pattern in root.all(class_name="pattern"):
        items.append({
            "number_t": pattern.first(class_name="number").text(),
            "title_t": pattern.first("h2").text(),
            "text_t": pattern.first("p").text(),
        })
    return {"patterns_o": items}


def extract_aw_downloads(root, _source):
    head = root.first(class_name="section-head")
    cards = []
    for card in root.all(class_name="download-card"):
        button = card.first("a")
        note = card.all("p")[-1]
        note_link = note.all("a")
        cards.append({
            "format_t": card.first(class_name="format").text(),
            "title_t": card.first("h3").text(),
            "text_t": card.all("p")[0].text(),
            "buttonLabel_t": button.text(),
            "buttonUrl_s": button.attrs["href"],
            "buttonStyle_s": button_style(button.cls()),
            "download_s": "true" if "download" in button.attrs else "",
            "note_t": "" if note_link else note.text(),
            "noteSmall_s": "true" if note.has_class("small") else "",
            "noteLabel_t": note_link[0].text() if note_link else "",
            "noteUrl_s": note_link[0].attrs.get("href", "") if note_link else "",
        })
    return {
        "eyebrow_t": head.first(class_name="eyebrow").text(),
        "heading_t": head.first("h2").text(),
        "intro_t": [p for p in head.all("p") if not p.has_class("eyebrow")][0].text(),
        "cards_o": cards,
        "footnote_t": root.all("p")[-1].text(),
    }


def extract_aw_prompts(root, _source):
    intro = root.first(class_name="intro")
    paragraphs = [p for p in intro.all("p") if not p.has_class("eyebrow")]
    pack = intro.first("a")
    prompts = []
    for detail in root.all("details"):
        pre = detail.first("pre")
        button = detail.first("button")
        file_link = detail.first(class_name="prompt-actions").all("a")[0]
        prompts.append({
            "summary_t": detail.first("summary").text(),
            "prompt_t": "".join(child for child in pre.children if isinstance(child, str)),
            "promptId_s": pre.attrs.get("id", ""),
            "copyLabel_t": button.text(),
            "ariaLabel_t": button.attrs.get("aria-label", ""),
            "fileLabel_t": file_link.text(),
            "fileUrl_s": file_link.attrs.get("href", ""),
        })
    return {
        "eyebrow_t": intro.first(class_name="eyebrow").text(),
        "heading_t": intro.first("h2").text(),
        "intro_t": paragraphs[0].text(),
        "detail_t": paragraphs[1].text() if len(paragraphs) > 1 else "",
        "packLabel_t": pack.text(),
        "packUrl_s": pack.attrs.get("href", ""),
        "packDownload_s": "true" if "download" in pack.attrs else "",
        "prompts_o": prompts,
    }


def extract_aw_templates(root, _source):
    head = root.first(class_name="section-head")
    templates = []
    for card in root.all(class_name="template"):
        link = card.first("a")
        templates.append({
            "title_t": card.first("h3").text(),
            "text_t": card.first("p").text(),
            "linkLabel_t": link.text(),
            "linkUrl_s": link.attrs.get("href", ""),
            "download_s": "true" if "download" in link.attrs else "",
        })
    skill = root.first(class_name="skill-row")
    skill_link = skill.first("a")
    return {
        "eyebrow_t": head.first(class_name="eyebrow").text(),
        "heading_t": head.first("h2").text(),
        "intro_t": [p for p in head.all("p") if not p.has_class("eyebrow")][0].text(),
        "templates_o": templates,
        "skillTitle_t": skill.first("h3").text(),
        "skillText_t": skill.first("p").text(),
        "skillLabel_t": skill_link.text(),
        "skillUrl_s": skill_link.attrs.get("href", ""),
        "skillDownload_s": "true" if "download" in skill_link.attrs else "",
    }


def extract_aw_callout(root, _source):
    box = root.first(class_name="directory-callout")
    link = box.first("a")
    return {
        "eyebrow_t": box.first(class_name="eyebrow").text(),
        "heading_t": box.first("h2").text(),
        "text_t": box.first("p",) if False else [p for p in box.all("p") if not p.has_class("eyebrow")][0].text(),
        "linkLabel_t": link.text(),
        "linkUrl_s": link.attrs.get("href", ""),
    }


def extract_aw_steps(root, _source):
    head = root.first(class_name="section-head")
    steps = []
    for item in root.first("ol").all("li"):
        steps.append({"title_t": item.first("h3").text(), "text_t": item.first("p").text()})
    note = root.first(class_name="note")
    share = root.first(class_name="share-row")
    image = share.first("img")
    image_link = share.first("a")
    copy = share.elements()[-1]
    links = copy.all("a")
    return {
        "eyebrow_t": head.first(class_name="eyebrow").text(),
        "heading_t": head.first("h2").text(),
        "steps_o": steps,
        "noteStrong_t": note.first("strong").text(),
        "note_t": note.direct(),
        "qrUrl_s": image_link.attrs.get("href", ""),
        "qrAria_t": image_link.attrs.get("aria-label", ""),
        "qrImage_s": image.attrs.get("src", ""),
        "qrAlt_t": image.attrs.get("alt", ""),
        "qrWidth_s": image.attrs.get("width", ""),
        "qrHeight_s": image.attrs.get("height", ""),
        "shareTitle_t": copy.first("h3").text(),
        "siteLabel_t": links[0].text(),
        "siteUrl_s": links[0].attrs.get("href", ""),
        "qrFileLabel_t": links[1].text(),
        "qrFileUrl_s": links[1].attrs.get("href", ""),
        "qrFileDownload_s": "true" if "download" in links[1].attrs else "",
        "referencesLabel_t": links[2].text(),
        "referencesUrl_s": links[2].attrs.get("href", ""),
        "guideLabel_t": links[3].text(),
        "guideUrl_s": links[3].attrs.get("href", ""),
        "guideDownload_s": "true" if "download" in links[3].attrs else "",
    }


def extract_resource_intro(root, _source):
    container = root.first(class_name="container")
    paragraphs = [p for p in container.all("p") if not p.has_class("eyebrow")]
    button = container.first(class_name="button")
    note = [p for p in paragraphs if p.has_class("download-note") or p.has_class("small")]
    lead = [p for p in paragraphs if p not in note][0]
    back = container.first(class_name="back-link")
    return {
        "backLabel_t": back.text(),
        "backUrl_s": back.attrs.get("href", ""),
        "eyebrow_t": container.first(class_name="eyebrow").text(),
        "title_t": container.first("h1").text(),
        "lead_t": lead.text(),
        "buttonLabel_t": button.text(),
        "buttonUrl_s": button.attrs.get("href", ""),
        "download_s": "true" if "download" in button.attrs else "",
        "note_t": note[0].text() if note else "",
    }


def extract_tool_directory(root, _source):
    groups = []
    for group in root.all(class_name="tool-group"):
        tools = []
        for tool in group.all(class_name="tool"):
            title = tool.first("h3").first("a")
            prompt = tool.all("strong")
            paragraphs = [p for p in tool.all("p") if not p.has_class("tool-type") and not p.all("strong")]
            tools.append({
                "type_t": tool.first(class_name="tool-type").text(),
                "title_t": title.text(),
                "url_s": title.attrs.get("href", ""),
                "text_t": paragraphs[0].text() if paragraphs else "",
                "promptLabel_t": prompt[0].text() if prompt else "",
                "prompt_t": prompt[0].parent_direct() if False else (tool.all("p")[-1].direct() if prompt else ""),
            })
        groups.append({"title_t": group.first("h2").text(), "tools_o": tools})
    closing = [child for child in root.elements() if child.tag == "section" and not child.has_class("tool-group")]
    close = closing[0]
    close_link = close.first("a")
    texts = close.all("p")
    return {
        "groups_o": groups,
        "closingTitle_t": close.first("h2").text(),
        "closingText_t": texts[0].text(),
        "closingLabel_t": close_link.text(),
        "closingUrl_s": close_link.attrs.get("href", ""),
        "closingDownload_s": "true" if "download" in close_link.attrs else "",
    }


def extract_reference_list(root, _source):
    paragraphs = root.all("p")
    intro = paragraphs[0].text() if paragraphs else ""
    closing = paragraphs[-1] if len(paragraphs) > 1 else None
    if closing and closing.all("a"):
        before, anchor, after = link_parts(closing)
        closing_before, closing_label, closing_url, closing_after = before, anchor.text(), anchor.attrs.get("href", ""), after
    else:
        closing_before = closing.text() if closing else ""
        closing_label, closing_url, closing_after = "", "", ""
    groups = []
    for section in root.all("section"):
        items = []
        for item in section.all("li"):
            anchor = item.first("a")
            note = re.sub(r"\s+", " ", "".join(child for child in item.children if isinstance(child, str))).strip()
            items.append({"label_t": anchor.text(), "url_s": anchor.attrs.get("href", ""), "note_t": note})
        groups.append({"title_t": section.first("h2").text(), "links_o": items})
    return {
        "intro_t": intro,
        "groups_o": groups,
        "closingBefore_t": closing_before,
        "closingLabel_t": closing_label,
        "closingUrl_s": closing_url,
        "closingAfter_t": closing_after,
    }


# ---------- renderers ----------

def i_tag(icon):
    return tag("i", {"class": icon})


def render_home_hero(data):
    chips = "".join(
        tag("div", {"class": "trust-chip"}, i_tag(chip["icon_s"]) + tag("span", {}, esc(chip["label_t"])))
        for chip in data["chips_o"]
    )
    primary = tag(
        "a",
        {"href": data["primaryUrl_s"], "class": "cta-button"},
        esc(data["primaryLabel_t"]) + " " + i_tag("ph ph-arrow-right"),
    )
    secondary = tag("a", {"href": data["secondaryUrl_s"], "class": "ghost-button"}, esc(data["secondaryLabel_t"]))
    content = tag(
        "div",
        {"class": "hero-content"},
        tag("h1", {}, esc(data["title_t"]))
        + tag("div", {"class": "accent-underline"})
        + tag("p", {"class": "hero-subtitle"}, esc(data["subtitle_t"]))
        + tag("div", {"class": "hero-cta-row"}, primary + secondary)
        + tag("div", {"class": "trust-chips"}, chips),
    )
    image = tag("div", {"class": "hero-image"}, data["_svg"])
    return tag("section", {"class": "hero"}, tag("div", {"class": "hero-inner"}, content + image))


def render_eyebrow_hero(data):
    inner = (
        tag("span", {"class": "hero-eyebrow"}, esc(data["eyebrow_t"]))
        + tag("h1", {"class": "hero-heading"}, esc(data["title_t"]))
        + tag("p", {"class": "hero-subtitle"}, esc(data["subtitle_t"]))
    )
    return tag("section", {"class": "hero"}, tag("div", {"class": "hero-inner"}, inner))


def render_services_hero(data):
    link = tag(
        "a",
        {"href": data["linkUrl_s"], "style": "color:#06B6D4;text-decoration:none;font-weight:700;"},
        esc(data["linkLabel_t"]),
    )
    after = esc(data["textAfter_t"])
    paragraph = esc(data["textBefore_t"]) + " " + link + after
    inner = (
        tag("span", {"class": "hero-eyebrow"}, esc(data["eyebrow_t"]))
        + tag("h1", {"class": "hero-heading"}, esc(data["title_t"]))
        + tag("p", {"class": "hero-subtext"}, paragraph)
    )
    return tag("section", {"class": "hero"}, tag("div", {"class": "hero-container"}, tag("div", {"class": "hero-content"}, inner)))


def render_blog_hero(data):
    title = esc(data["titleLine1_t"]) + "<br>" + esc(data["titleLine2_t"])
    inner = (
        tag("p", {"class": "blog-hero-eyebrow"}, esc(data["eyebrow_t"]))
        + tag("h1", {"class": "blog-hero-title"}, title)
        + tag("p", {"class": "blog-hero-sub"}, esc(data["subtitle_t"]))
    )
    return tag("section", {"class": "blog-hero"}, tag("div", {"class": "blog-hero-inner"}, inner))


def render_work_hero(data):
    inner = (
        tag("div", {"class": "eyebrow-pill"}, esc(data["eyebrow_t"]))
        + tag("h1", {}, esc(data["title_t"]))
        + tag("div", {"class": "accent-underline"})
        + tag("p", {"class": "page-hero-subtitle"}, esc(data["subtitle_t"]))
    )
    return tag("section", {"class": "page-hero"}, tag("div", {"class": "page-hero-inner"}, inner))


def render_value_props(data):
    cards = "".join(
        tag(
            "div",
            {"class": "stat-card"},
            tag("div", {"class": "stat-icon"}, i_tag(item["icon_s"]))
            + tag("div", {"class": "stat-number"}, esc(item["title_t"]))
            + tag("div", {"class": "stat-label"}, esc(item["text_t"])),
        )
        for item in data["items_o"]
    )
    return tag("section", {"class": "value-props"}, tag("div", {"class": "value-props-inner"}, cards))


def render_why(data):
    items = "".join(
        tag(
            "div",
            {"class": "benefit-item"},
            tag("div", {"class": "benefit-icon"}, i_tag(item["icon_s"]))
            + tag("div", {"class": "benefit-text"}, esc(item["text_t"])),
        )
        for item in data["items_o"]
    )
    content = (
        tag("h2", {"class": "section-heading"}, esc(data["heading_t"]))
        + tag("p", {"class": "section-subheading"}, esc(data["subheading_t"]))
        + tag("div", {"class": "benefit-list"}, items)
    )
    inner = tag("div", {"class": "why-content"}, content) + tag("div", {"class": "ai-diagram-card"}, data["_svg"])
    return tag("section", {"class": "why-section"}, tag("div", {"class": "why-inner"}, inner))


def render_home_services(data):
    cards = []
    for card in data["cards_o"]:
        header = tag(
            "div",
            {"class": "service-header"},
            i_tag(card["icon_s"]) + tag("span", {"class": "service-name"}, esc(card["title_t"])),
        )
        body = header + tag("p", {"class": "service-description"}, esc(card["text_t"]))
        if card["linkLabel_t"]:
            body += tag(
                "a",
                {"href": card["linkUrl_s"], "class": "service-card-link"},
                esc(card["linkLabel_t"]) + " " + i_tag("ph ph-arrow-right"),
            )
        cards.append(tag("div", {"class": "service-card"}, body))
    links = "".join(
        tag("a", {"class": "ghost-link", "href": link["url_s"]}, esc(link["label_t"]) + " " + i_tag("ph ph-arrow-right"))
        for link in data["links_o"]
    )
    header = tag(
        "div",
        {"class": "section-header"},
        tag("h2", {"class": "section-title"}, esc(data["heading_t"]))
        + tag("p", {"class": "section-subtitle"}, esc(data["subtitle_t"])),
    )
    inner = header + tag("div", {"class": "services-grid"}, "".join(cards)) + tag("div", {"class": "services-link"}, links)
    return tag("section", {"class": "services-section"}, tag("div", {"class": "services-inner"}, inner))


def render_social(data):
    founder = tag(
        "div",
        {"class": "founder-info"},
        tag("div", {"class": "founder-avatar"}, esc(data["avatar_t"]))
        + tag(
            "div",
            {"class": "founder-details"},
            tag("div", {"class": "founder-name"}, esc(data["name_t"]))
            + tag("div", {"class": "founder-title"}, esc(data["role_t"])),
        ),
    )
    logos = "".join(tag("div", {"class": "logo-item"}, esc(item["label_t"])) for item in data["logos_o"])
    inner = founder + tag("div", {"class": "quote-text"}, esc(data["quote_t"])) + tag("div", {"class": "logos-strip"}, logos)
    return tag("section", {"class": "social-proof"}, tag("div", {"class": "social-proof-inner"}, inner))


def render_final_cta(data):
    button_class = "cta-button" if data["variant_s"] == "home" else "secondary-button"
    button = tag(
        "a",
        {"href": data["ctaUrl_s"], "class": button_class, "style": "font-size: 1.125rem; padding: 1rem 2rem;"},
        esc(data["ctaLabel_t"]) + " " + i_tag("ph ph-arrow-right"),
    )
    contact = tag(
        "div",
        {"class": "final-cta-contact"},
        tag("a", {"href": data["phoneUrl_s"]}, esc(data["phoneLabel_t"]))
        + " | "
        + tag("a", {"href": data["emailUrl_s"]}, esc(data["emailLabel_t"])),
    )
    inner = (
        tag("h2", {"class": "final-cta-heading"}, esc(data["heading_t"]))
        + tag("p", {"class": "final-cta-subtext"}, esc(data["subtext_t"]))
        + button
        + contact
    )
    return tag("section", {"class": "final-cta"}, tag("div", {"class": "final-cta-inner"}, inner))


def render_cta_band(data):
    variant = data["variant_s"]
    if variant == "services":
        button = tag("a", {"href": data["ctaUrl_s"], "class": "cta-button-white"}, esc(data["ctaLabel_t"]))
        wrap = "cta-container"
    else:
        attrs = {"href": data["ctaUrl_s"], "class": "secondary-button"}
        if variant == "about":
            attrs["style"] = "font-size: 1.125rem; padding: 1rem 2rem;"
        button = tag("a", attrs, esc(data["ctaLabel_t"]) + " " + i_tag("ph ph-arrow-right"))
        wrap = "cta-inner"
    inner = tag("h2", {"class": "cta-heading"}, esc(data["heading_t"]))
    if data["subtext_t"]:
        inner += tag("p", {"class": "cta-subtext"}, esc(data["subtext_t"]))
    inner += button
    return tag("section", {"class": "cta-section"}, tag("div", {"class": wrap}, inner))


def render_newsletter(data):
    button = tag(
        "a",
        {
            "class": "cta-button",
            "href": data["ctaUrl_s"],
            "style": "display:inline-flex;align-items:center;gap:8px;padding:14px 28px;background:linear-gradient(135deg,#06B6D4,#0EA5E9);color:white;text-decoration:none;border-radius:8px;font-weight:700;font-size:14px;",
        },
        esc(data["ctaLabel_t"]) + " " + i_tag("ph ph-arrow-right"),
    )
    inner = (
        tag("h2", {"class": "newsletter-title"}, esc(data["heading_t"]))
        + tag("p", {"class": "newsletter-sub"}, esc(data["subtext_t"]))
        + button
        + tag("p", {"class": "newsletter-note"}, esc(data["note_t"]))
    )
    return tag("section", {"class": "newsletter-section"}, tag("div", {"class": "newsletter-inner"}, inner))


def render_story(data):
    paragraphs = "".join(tag("p", {}, esc(item["text_t"])) for item in data["paragraphs_o"])
    stats = "".join(
        tag(
            "div",
            {"class": "stat-item"},
            tag("div", {"class": "stat-value"}, esc(item["value_t"]))
            + tag("div", {"class": "stat-label"}, esc(item["label_t"])),
        )
        for item in data["stats_o"]
    )
    inner = (
        tag("h2", {"class": "story-heading"}, esc(data["heading_t"]))
        + tag("div", {"class": "story-content"}, paragraphs)
        + tag("div", {"class": "stats-block"}, stats)
    )
    return tag("section", {"class": "story-section"}, tag("div", {"class": "story-section-inner"}, inner))


def render_expertise(data):
    chips = "".join(
        tag("div", {"class": "expertise-chip"}, i_tag(chip["icon_s"]) + tag("span", {}, esc(chip["label_t"])))
        for chip in data["chips_o"]
    )
    inner = tag("h2", {"class": "expertise-heading"}, esc(data["heading_t"])) + tag("div", {"class": "expertise-grid"}, chips)
    return tag("section", {"class": "expertise-section"}, tag("div", {"class": "expertise-section-inner"}, inner))


def render_contact_card(data):
    items = []
    for item in data["items_o"]:
        value = tag("a", {"href": item["url_s"]}, esc(item["value_t"])) if item["url_s"] else esc(item["value_t"])
        items.append(
            tag(
                "div",
                {"class": "contact-item"},
                i_tag(item["icon_s"])
                + tag("div", {"class": "contact-label"}, esc(item["label_t"]))
                + tag("div", {"class": "contact-value"}, value),
            )
        )
    linkedin = tag(
        "a",
        {"class": "secondary-button", "href": data["linkedinUrl_s"]},
        i_tag("ph ph-linkedin-logo") + esc(data["linkedinLabel_t"]),
    )
    inner = (
        tag("h2", {"class": "contact-heading"}, esc(data["heading_t"]))
        + tag("div", {"class": "contact-details"}, "".join(items))
        + tag("div", {"class": "contact-linkedin"}, linkedin)
        + tag("p", {"class": "contact-subtext"}, esc(data["note_t"]))
    )
    return tag("section", {"class": "contact-section"}, tag("div", {"class": "contact-section-inner"}, inner))


def render_contact_panel(data):
    methods = []
    for method in data["methods_o"]:
        value = tag("a", {"href": method["url_s"]}, esc(method["value_t"])) if method["url_s"] else esc(method["value_t"])
        methods.append(
            tag(
                "div",
                {"class": "contact-method"},
                tag("div", {"class": "contact-method-icon"}, i_tag(method["icon_s"]))
                + tag(
                    "div",
                    {"class": "contact-method-details"},
                    tag("span", {"class": "contact-method-label"}, esc(method["label_t"]))
                    + tag("span", {"class": "contact-method-value"}, value),
                ),
            )
        )
    linkedin = tag(
        "a",
        {"href": data["linkedinUrl_s"], "class": "linkedin-button"},
        i_tag("ph ph-linkedin-logo") + esc(data["linkedinLabel_t"]),
    )
    info = (
        tag("h2", {"class": "contact-heading"}, esc(data["heading_t"]))
        + tag("p", {"class": "contact-intro"}, esc(data["intro_t"]))
        + tag("div", {"class": "contact-methods"}, "".join(methods))
        + tag("div", {"class": "linkedin-section"}, linkedin)
        + tag(
            "div",
            {"class": "cta-box"},
            tag("h3", {"class": "cta-box-title"}, esc(data["boxTitle_t"]))
            + tag("p", {"class": "cta-box-text"}, esc(data["boxText_t"])),
        )
    )
    fields = []
    for field in data["fields_o"]:
        required = "required" in {"required": True} and field["required_s"] == "true"
        attrs = {
            "id": field["name_s"],
            "name": field["name_s"],
            "placeholder": field["placeholder_t"],
            "required": True if field["required_s"] == "true" else None,
        }
        if field["type_s"] == "textarea":
            control = tag("textarea", {"class": "form-textarea", **attrs})
        else:
            control = tag("input", {"type": field["type_s"], "class": "form-input", **attrs}, void=True)
        fields.append(
            tag(
                "div",
                {"class": "form-group"},
                tag("label", {"class": "form-label", "for": field["name_s"]}, esc(field["label_t"])) + control,
            )
        )
    form = tag(
        "form",
        {"class": "contact-form", "action": "mailto:" + data["formEmail_s"], "method": "post", "enctype": "text/plain"},
        "".join(fields) + tag("button", {"type": "submit", "class": "submit-button"}, esc(data["submitLabel_t"])),
    )
    form_col = (
        tag("h2", {"class": "form-heading"}, esc(data["formHeading_t"]))
        + tag("p", {"class": "form-subtitle"}, esc(data["formSubtitle_t"]))
        + form
    )
    grid = tag("div", {"class": "contact-info"}, info) + tag("div", {"class": "form-section-inner"}, form_col)
    return tag(
        "section",
        {"class": "contact-section"},
        tag("div", {"class": "contact-section-inner"}, tag("div", {"class": "contact-grid"}, grid)),
    )


def render_service_catalog(data):
    cards = []
    for card in data["cards_o"]:
        tags = "".join(tag("span", {"class": "service-tag"}, esc(tag_item["label_t"])) for tag_item in card["tags_o"])
        cards.append(
            tag(
                "div",
                {"class": "service-card"},
                tag("div", {"class": "service-icon"}, i_tag(card["icon_s"]))
                + tag("h3", {"class": "service-title"}, esc(card["title_t"]))
                + tag("p", {"class": "service-description"}, esc(card["text_t"]))
                + tag("div", {"class": "service-tags"}, tags),
            )
        )
    inner = tag("h2", {"class": "section-heading"}, esc(data["heading_t"])) + tag("div", {"class": "services-grid"}, "".join(cards))
    return tag("section", {"class": "services-section"}, tag("div", {"class": "services-container"}, inner))


def render_ai_banner(data):
    items = []
    for item in data["items_o"]:
        text = tag("strong", {}, esc(item["title_t"])) + " " + esc(item["text_t"])
        items.append(
            tag(
                "li",
                {"class": "ai-benefit-item"},
                i_tag(item["icon_s"]) + tag("span", {"class": "ai-benefit-text"}, text),
            )
        )
    content = tag("h2", {}, esc(data["heading_t"])) + tag("ul", {"class": "ai-benefits"}, "".join(items))
    inner = tag("div", {"class": "ai-content"}, content) + tag("div", {"class": "ai-visual"}, data["_svg"])
    return tag("section", {"class": "ai-banner"}, tag("div", {"class": "ai-banner-container"}, inner))


def render_software_catalog(data):
    cards = []
    for card in data["cards_o"]:
        tags = "".join(tag("span", {"class": "software-tag"}, esc(item["label_t"])) for item in card["tags_o"])
        cards.append(
            tag(
                "article",
                {"class": "software-card"},
                tag("div", {"class": "software-icon"}, i_tag(card["icon_s"]))
                + tag("h3", {"class": "software-title"}, esc(card["title_t"]))
                + tag("p", {"class": "software-description"}, esc(card["text_t"]))
                + tag("div", {"class": "software-tags"}, tags),
            )
        )
    header = tag(
        "div",
        {"class": "section-header"},
        tag("div", {"class": "section-kicker"}, esc(data["kicker_t"]))
        + tag("h2", {"class": "section-heading"}, esc(data["heading_t"]))
        + tag("p", {"class": "section-subtitle"}, esc(data["subtitle_t"])),
    )
    inner = header + tag("div", {"class": "software-grid"}, "".join(cards))
    return tag("section", {"class": "software-section"}, tag("div", {"class": "software-inner"}, inner))


def render_fit(data):
    panels = []
    for panel in data["panels_o"]:
        items = "".join(
            tag("li", {}, i_tag(panel["icon_s"]) + tag("span", {}, esc(item["text_t"])))
            for item in panel["items_o"]
        )
        panels.append(tag("div", {"class": "fit-panel"}, tag("h2", {}, esc(panel["title_t"])) + tag("ul", {"class": "fit-list"}, items)))
    return tag("section", {"class": "fit-section"}, tag("div", {"class": "fit-inner"}, "".join(panels)))


def render_process(data):
    steps = "".join(
        tag(
            "div",
            {"class": "process-step"},
            tag("div", {"class": "process-step-number"}, esc(step["number_t"]))
            + tag("h3", {}, esc(step["title_t"]))
            + tag("p", {}, esc(step["text_t"])),
        )
        for step in data["steps_o"]
    )
    header = tag(
        "div",
        {"class": "section-header"},
        tag("div", {"class": "section-kicker"}, esc(data["kicker_t"]))
        + tag("h2", {"class": "section-heading"}, esc(data["heading_t"]))
        + tag("p", {"class": "section-subtitle"}, esc(data["subtitle_t"])),
    )
    return tag("section", {"class": "process-section"}, tag("div", {"class": "process-inner"}, header + tag("div", {"class": "process-grid"}, steps)))


def render_cases(data):
    blocks = []
    for case in data["cases_o"]:
        title = tag(case["titleTag_s"], {"class": "case-title"}, esc(case["title_t"]))
        bits = ""
        if case["kicker_t"]:
            bits += tag("div", {"class": "featured-label"}, esc(case["kicker_t"]))
        bits += title
        if case["badge_t"]:
            bits += tag("div", {"class": "case-badge"}, esc(case["badge_t"]))
        if case["linkLabel_t"]:
            link_attrs = {"class": "case-external-link", "href": case["linkUrl_s"]}
            if case["linkTarget_s"]:
                link_attrs["target"] = case["linkTarget_s"]
            bits += tag(
                "a",
                link_attrs,
                esc(case["linkLabel_t"]) + " " + i_tag("ph ph-arrow-square-out"),
            )
        if case["statBefore_t"]:
            bits += tag(
                "div",
                {"class": "case-stat"},
                tag("span", {"class": "stat-before"}, esc(case["statBefore_t"]))
                + tag("span", {"class": "stat-arrow"}, esc(case["statArrow_t"]))
                + tag("span", {"class": "stat-after"}, esc(case["statAfter_t"])),
            )
        if case["stat_t"]:
            bits += tag("div", {"class": "case-stat-single"}, esc(case["stat_t"]))
        bits += tag("p", {"class": "case-description"}, esc(case["text_t"]))
        bits += tag("div", {"class": "tech-tags"}, "".join(tag("span", {"class": "tech-tag"}, esc(tag_item["label_t"])) for tag_item in case["tags_o"]))
        if case["style_s"] == "featured":
            blocks.append(tag("div", {"class": "case-featured"}, tag("div", {"class": "case-featured-content"}, bits)))
        else:
            blocks.append(tag("div", {"class": "case-card"}, bits))
    banner = tag(
        "div",
        {"class": "ai-acceleration-banner"},
        tag("div", {"class": "ai-banner-title"}, esc(data["bannerTitle_t"]))
        + tag("p", {"class": "ai-banner-text"}, esc(data["bannerText_t"])),
    )
    inner = tag("div", {"class": "case-studies-stack"}, "".join(blocks) + banner)
    return tag("section", {"class": "case-studies-content"}, tag("div", {"class": "case-studies-content-inner"}, inner))


def button_style(class_name):
    if "button-light" in class_name:
        return "light"
    if "button-primary" in class_name:
        return "primary"
    if "button-outline" in class_name:
        return "outline"
    return "default"


def button_html(label, url, style, download=False):
    classes = {
        "primary": "button button-primary",
        "outline": "button button-outline",
        "light": "button button-light",
        "default": "button",
    }[style]
    attrs = {"class": classes, "href": url}
    if download:
        attrs["download"] = True
    return tag("a", attrs, esc(label))


def render_aw_hero(data):
    brand = tag("strong", {}, esc(data["brandStrong_t"])) + "<br>" + esc(data["brandRest_t"])
    title = esc(data["titleLine1_t"]) + "<br>" + esc(data["titleLine2_t"])
    buttons = button_html(data["primaryLabel_t"], data["primaryUrl_s"], "primary", data["primaryDownload_s"] == "true")
    buttons += button_html(data["secondaryLabel_t"], data["secondaryUrl_s"], "outline")
    column = (
        tag("p", {"class": "eyebrow"}, esc(data["eyebrow_t"]))
        + tag("p", {"class": "brand-line"}, brand)
        + tag("h1", {}, title)
        + tag("p", {"class": "lead"}, esc(data["lead_t"]))
        + tag("div", {"class": "button-row"}, buttons)
        + tag("p", {"class": "meta"}, esc(data["meta_t"]))
    )
    image = tag("img", {"src": data["image_s"], "alt": data["imageAlt_t"], "width": data["imageWidth_s"] or None, "height": data["imageHeight_s"] or None}, void=True)
    figure = tag(
        "figure",
        {"class": "preview"},
        tag("a", {"href": data["imageUrl_s"], "aria-label": data["imageAria_t"]}, image) + tag("figcaption", {}, esc(data["caption_t"])),
    )
    return tag("section", {"class": "hero"}, tag("div", {"class": "container hero-grid"}, tag("div", {}, column) + figure))


def render_aw_nav(data):
    links = "".join(tag("a", {"href": link["url_s"]}, esc(link["label_t"])) for link in data["links_o"])
    return tag("nav", {"class": "section-nav", "aria-label": data["ariaLabel_t"]}, tag("div", {"class": "container"}, links))


def render_aw_patterns(data):
    items = "".join(
        tag(
            "section",
            {"class": "pattern"},
            tag("span", {"class": "number"}, esc(item["number_t"]))
            + tag("h2", {}, esc(item["title_t"]))
            + tag("p", {}, esc(item["text_t"])),
        )
        for item in data["patterns_o"]
    )
    return tag("div", {"class": "container patterns"}, items)


def render_aw_downloads(data):
    cards = []
    for card in data["cards_o"]:
        note_class = "download-note small" if card["noteSmall_s"] == "true" else "download-note"
        if card["noteLabel_t"]:
            note = tag("p", {"class": note_class}, tag("a", {"href": card["noteUrl_s"]}, esc(card["noteLabel_t"])))
        else:
            note = tag("p", {"class": note_class}, esc(card["note_t"]))
        cards.append(
            tag(
                "article",
                {"class": "download-card"},
                tag("span", {"class": "format"}, esc(card["format_t"]))
                + tag("h3", {}, esc(card["title_t"]))
                + tag("p", {}, esc(card["text_t"]))
                + button_html(card["buttonLabel_t"], card["buttonUrl_s"], card["buttonStyle_s"], card["download_s"] == "true")
                + note,
            )
        )
    head = tag(
        "div",
        {"class": "section-head"},
        tag("p", {"class": "eyebrow"}, esc(data["eyebrow_t"]))
        + tag("h2", {}, esc(data["heading_t"]))
        + tag("p", {}, esc(data["intro_t"])),
    )
    inner = head + tag("div", {"class": "download-grid"}, "".join(cards)) + tag("p", {"class": "small download-note"}, esc(data["footnote_t"]))
    return tag("section", {"class": "section section-white", "id": "downloads"}, tag("div", {"class": "container"}, inner))


def render_aw_prompts(data):
    prompts = []
    for prompt in data["prompts_o"]:
        actions = (
            tag(
                "button",
                {
                    "class": "button button-light",
                    "type": "button",
                    "data-copy": prompt["promptId_s"],
                    "aria-label": prompt["ariaLabel_t"],
                    "hidden": True,
                },
                esc(prompt["copyLabel_t"]),
            )
            + tag("a", {"href": prompt["fileUrl_s"], "download": True}, esc(prompt["fileLabel_t"]))
            + tag("span", {"class": "copy-status", "role": "status", "aria-live": "polite"})
        )
        body = tag("pre", {"id": prompt["promptId_s"]}, esc(prompt["prompt_t"])) + tag("div", {"class": "prompt-actions"}, actions)
        prompts.append(tag("details", {"class": "prompt"}, tag("summary", {}, esc(prompt["summary_t"])) + tag("div", {"class": "prompt-body"}, body)))
    intro = (
        tag("p", {"class": "eyebrow"}, esc(data["eyebrow_t"]))
        + tag("h2", {}, esc(data["heading_t"]))
        + tag("p", {}, esc(data["intro_t"]))
        + tag("p", {}, esc(data["detail_t"]))
        + tag("a", {"href": data["packUrl_s"], "download": True if data["packDownload_s"] == "true" else None}, esc(data["packLabel_t"]))
    )
    inner = tag("div", {"class": "intro"}, intro) + tag("div", {"class": "prompt-list"}, "".join(prompts))
    return tag("section", {"class": "section", "id": "prompts"}, tag("div", {"class": "container split"}, inner))


def render_aw_templates(data):
    cards = "".join(
        tag(
            "article",
            {"class": "template"},
            tag("h3", {}, esc(card["title_t"]))
            + tag("p", {}, esc(card["text_t"]))
            + tag("a", {"href": card["linkUrl_s"], "download": True if card["download_s"] == "true" else None}, esc(card["linkLabel_t"])),
        )
        for card in data["templates_o"]
    )
    skill = tag(
        "div",
        {"class": "skill-row"},
        tag("div", {}, tag("h3", {}, esc(data["skillTitle_t"])) + tag("p", {}, esc(data["skillText_t"])))
        + button_html(data["skillLabel_t"], data["skillUrl_s"], "light", data["skillDownload_s"] == "true"),
    )
    head = tag(
        "div",
        {"class": "section-head"},
        tag("p", {"class": "eyebrow"}, esc(data["eyebrow_t"]))
        + tag("h2", {}, esc(data["heading_t"]))
        + tag("p", {}, esc(data["intro_t"])),
    )
    inner = head + tag("div", {"class": "template-grid"}, cards) + skill
    return tag("section", {"class": "section section-white", "id": "templates"}, tag("div", {"class": "container"}, inner))


def render_aw_callout(data):
    copy = (
        tag("p", {"class": "eyebrow"}, esc(data["eyebrow_t"]))
        + tag("h2", {}, esc(data["heading_t"]))
        + tag("p", {}, esc(data["text_t"]))
    )
    box = tag("div", {}, copy) + button_html(data["linkLabel_t"], data["linkUrl_s"], "default")
    return tag("section", {"class": "section"}, tag("div", {"class": "container"}, tag("div", {"class": "directory-callout"}, box)))


def render_aw_steps(data):
    steps = "".join(
        tag("li", {}, tag("h3", {}, esc(step["title_t"])) + tag("p", {}, esc(step["text_t"])))
        for step in data["steps_o"]
    )
    note = tag("p", {"class": "note"}, tag("strong", {}, esc(data["noteStrong_t"])) + " " + esc(data["note_t"]))
    share_copy = (
        tag("h3", {}, esc(data["shareTitle_t"]))
        + tag(
            "p",
            {},
            tag("a", {"href": data["siteUrl_s"]}, esc(data["siteLabel_t"]))
            + "<br>"
            + tag("a", {"href": data["qrFileUrl_s"], "download": True if data["qrFileDownload_s"] == "true" else None}, esc(data["qrFileLabel_t"]))
            + " · "
            + tag("a", {"href": data["referencesUrl_s"]}, esc(data["referencesLabel_t"]))
            + " · "
            + tag("a", {"href": data["guideUrl_s"], "download": True if data["guideDownload_s"] == "true" else None}, esc(data["guideLabel_t"])),
        )
    )
    image = tag(
        "img",
        {
            "src": data["qrImage_s"],
            "alt": data["qrAlt_t"],
            "width": data["qrWidth_s"] or None,
            "height": data["qrHeight_s"] or None,
        },
        void=True,
    )
    share = tag(
        "div",
        {"class": "share-row"},
        tag("a", {"href": data["qrUrl_s"], "aria-label": data["qrAria_t"] or None}, image) + tag("div", {}, share_copy),
    )
    head = tag("div", {"class": "section-head"}, tag("p", {"class": "eyebrow"}, esc(data["eyebrow_t"])) + tag("h2", {}, esc(data["heading_t"])))
    inner = head + tag("ol", {"class": "steps"}, steps) + note + share
    return tag("section", {"class": "section section-white"}, tag("div", {"class": "container"}, inner))


def render_resource_intro(data):
    button_attrs = {"class": "button", "href": data["buttonUrl_s"]}
    if data["download_s"] == "true":
        button_attrs["download"] = True
    bits = (
        tag("a", {"class": "back-link", "href": data["backUrl_s"]}, esc(data["backLabel_t"]))
        + tag("p", {"class": "eyebrow"}, esc(data["eyebrow_t"]))
        + tag("h1", {}, esc(data["title_t"]))
        + tag("p", {}, esc(data["lead_t"]))
        + tag("a", button_attrs, esc(data["buttonLabel_t"]))
    )
    if data["note_t"]:
        bits += tag("p", {"class": "small download-note"}, esc(data["note_t"]))
    return tag("div", {"class": "page-intro"}, tag("div", {"class": "container"}, bits))


def render_tool_directory(data):
    groups = []
    for group in data["groups_o"]:
        tools = []
        for tool in group["tools_o"]:
            prompt = ""
            if tool["promptLabel_t"]:
                prompt = tag("p", {}, tag("strong", {}, esc(tool["promptLabel_t"])) + " " + esc(tool["prompt_t"]))
            tools.append(
                tag(
                    "article",
                    {"class": "tool"},
                    tag("p", {"class": "tool-type"}, esc(tool["type_t"]))
                    + tag("h3", {}, tag("a", {"href": tool["url_s"]}, esc(tool["title_t"])))
                    + tag("p", {}, esc(tool["text_t"]))
                    + prompt,
                )
            )
        groups.append(tag("section", {"class": "tool-group"}, tag("h2", {}, esc(group["title_t"])) + tag("div", {"class": "tool-list"}, "".join(tools))))
    closing = tag(
        "section",
        {},
        tag("h2", {}, esc(data["closingTitle_t"]))
        + tag("p", {}, esc(data["closingText_t"]))
        + tag("p", {}, tag("a", {"href": data["closingUrl_s"], "download": True if data["closingDownload_s"] == "true" else None}, esc(data["closingLabel_t"]))),
    )
    return tag("div", {"class": "container section"}, "".join(groups) + closing)


def render_reference_list(data):
    groups = []
    for group in data["groups_o"]:
        items = []
        for link in group["links_o"]:
            note = (" " + esc(link["note_t"])) if link["note_t"] else ""
            items.append(tag("li", {}, tag("a", {"href": link["url_s"]}, esc(link["label_t"])) + note))
        groups.append(tag("section", {}, tag("h2", {}, esc(group["title_t"])) + tag("ul", {}, "".join(items))))
    bits = tag("p", {}, esc(data["intro_t"])) + "".join(groups)
    if data["closingLabel_t"]:
        closing = esc(data["closingBefore_t"]) + " " + tag("a", {"href": data["closingUrl_s"]}, esc(data["closingLabel_t"])) + esc(data["closingAfter_t"])
        bits += tag("p", {}, closing)
    elif data["closingBefore_t"]:
        bits += tag("p", {}, esc(data["closingBefore_t"]))
    return tag("div", {"class": "container reading"}, bits)


RENDERERS = {
    "home-hero": render_home_hero,
    "eyebrow-hero": render_eyebrow_hero,
    "services-hero": render_services_hero,
    "blog-hero": render_blog_hero,
    "work-hero": render_work_hero,
    "value-props": render_value_props,
    "why-section": render_why,
    "home-services": render_home_services,
    "social-proof": render_social,
    "final-cta": render_final_cta,
    "cta-band": render_cta_band,
    "newsletter": render_newsletter,
    "story": render_story,
    "expertise": render_expertise,
    "contact-card": render_contact_card,
    "contact-panel": render_contact_panel,
    "service-catalog": render_service_catalog,
    "ai-banner": render_ai_banner,
    "software-catalog": render_software_catalog,
    "fit-panels": render_fit,
    "process-steps": render_process,
    "case-studies": render_cases,
    "aw-hero": render_aw_hero,
    "aw-nav": render_aw_nav,
    "aw-patterns": render_aw_patterns,
    "aw-downloads": render_aw_downloads,
    "aw-prompts": render_aw_prompts,
    "aw-templates": render_aw_templates,
    "aw-callout": render_aw_callout,
    "aw-steps": render_aw_steps,
    "resource-intro": render_resource_intro,
    "tool-directory": render_tool_directory,
    "reference-list": render_reference_list,
}


def main_root(source):
    root = parse_html(source)
    elements = root.elements()
    if len(elements) != 1:
        raise SystemExit(f"expected one root element, found {len(elements)}")
    return elements[0]


def check_pair(name, source, rendered):
    diff = first_diff(canon(rendered), canon(source))
    if diff:
        raise SystemExit(f"{name} diverges from the original markup\n{diff}")


SECTION_JOBS = {
    "home/01-hero.xml": ("home-hero", extract_home_hero),
    "home/02-value-props.xml": ("value-props", extract_value_props),
    "home/03-why-section.xml": ("why-section", extract_why),
    "home/04-services-section.xml": ("home-services", extract_home_services),
    "home/05-social-proof.xml": ("social-proof", extract_social),
    "home/07-final-cta.xml": ("final-cta", lambda root, source: extract_final_cta(root, source, "home")),
    "services/01-hero.xml": ("services-hero", extract_services_hero),
    "services/02-services-section.xml": ("service-catalog", extract_service_catalog),
    "services/03-ai-banner.xml": ("ai-banner", extract_ai_banner),
    "services/04-cta-section.xml": ("cta-band", lambda root, source: extract_cta_band(root, source, "services")),
    "software/01-hero.xml": ("eyebrow-hero", extract_eyebrow_hero),
    "software/02-software-section.xml": ("software-catalog", extract_software_catalog),
    "software/03-fit-section.xml": ("fit-panels", extract_fit),
    "software/04-process-section.xml": ("process-steps", extract_process),
    "software/05-cta-section.xml": ("cta-band", lambda root, source: extract_cta_band(root, source, "software")),
    "work/01-page-hero.xml": ("work-hero", extract_work_hero),
    "work/02-case-studies-content.xml": ("case-studies", extract_cases),
    "work/03-final-cta.xml": ("final-cta", lambda root, source: extract_final_cta(root, source, "work")),
    "about/01-hero.xml": ("eyebrow-hero", extract_eyebrow_hero),
    "about/02-story-section.xml": ("story", extract_story),
    "about/03-expertise-section.xml": ("expertise", extract_expertise),
    "about/04-contact-section.xml": ("contact-card", extract_contact_card),
    "about/05-cta-section.xml": ("cta-band", lambda root, source: extract_cta_band(root, source, "about")),
    "contact/01-hero.xml": ("eyebrow-hero", extract_eyebrow_hero),
    "contact/02-contact-section.xml": ("contact-panel", extract_contact_panel),
    "blog/01-blog-hero.xml": ("blog-hero", extract_blog_hero),
    "blog/03-newsletter-section.xml": ("newsletter", extract_newsletter),
}


def check_sections():
    base = ROOT / "site/components/sections"
    import xml.etree.ElementTree as ET
    for rel, (kind, extractor) in SECTION_JOBS.items():
        source = ET.parse(base / rel).getroot().findtext("markup_html")
        data = extractor(main_root(source), source)
        rendered = RENDERERS[kind](data)
        check_pair(rel, source, rendered)
        print("ok", rel)


def check_resources():
    import xml.etree.ElementTree as ET
    pages = {
        "altwheels/index.xml": [
            ("aw-hero", extract_aw_hero),
            ("aw-nav", extract_aw_nav),
            ("aw-patterns", extract_aw_patterns),
            ("aw-downloads", extract_aw_downloads),
            ("aw-prompts", extract_aw_prompts),
            ("aw-templates", extract_aw_templates),
            ("aw-callout", extract_aw_callout),
            ("aw-steps", extract_aw_steps),
        ],
        "altwheels/fleet-tools/index.xml": [
            ("resource-intro", extract_resource_intro),
            ("tool-directory", extract_tool_directory),
        ],
        "altwheels/references/index.xml": [
            ("resource-intro", extract_resource_intro),
            ("reference-list", extract_reference_list),
        ],
    }
    for rel, jobs in pages.items():
        source = ET.parse(ROOT / "site/website" / rel).getroot().findtext("main_html")
        children = main_root(source).elements()
        if len(children) != len(jobs):
            raise SystemExit(f"{rel} has {len(children)} regions, expected {len(jobs)}")
        for child, (kind, extractor) in zip(children, jobs):
            data = extractor(child, source)
            rendered = parse_html(RENDERERS[kind](data)).elements()[0]
            diff = first_diff(walk(rendered), walk(child))
            if diff:
                raise SystemExit(f"{rel} {kind} diverges\n{diff}")
            print("ok", rel, kind)


if __name__ == "__main__":
    check_sections()
    check_resources()
