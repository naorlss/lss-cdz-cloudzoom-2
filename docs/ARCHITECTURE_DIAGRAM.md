# Content model

```mermaid
graph TB
    subgraph Pages
        LAND["/page/landing"]
        ART["/page/article"]
        RES["/page/resource"]
    end
    subgraph Globals
        LD["/component/level-descriptor"]
        HDR["/component/header"]
        FTR["/component/footer"]
    end
    subgraph Sections
        SEC["/component/section"]
    end
    subgraph RepeatGroups
        NAV["nav_o items"]
        CON["connect_o items"]
        TAG["tags_o / listTags_o items"]
    end
    LD -->|header_o| HDR
    LD -->|footer_o| FTR
    LAND -->|sections_o| SEC
    LAND -->|header_o footer_o optional| HDR
    LAND -->|header_o footer_o optional| FTR
    ART -->|header_o footer_o optional| HDR
    ART -->|header_o footer_o optional| FTR
    RES -->|header_o footer_o optional| HDR
    RES -->|header_o footer_o optional| FTR
    HDR --> NAV
    FTR --> NAV
    FTR --> CON
    ART --> TAG
```

## Hierarchy

- `/component/level-descriptor` inherits `header_o` and `footer_o` into pages.
- `/page/landing` renders `header_o`, then `sections_o`, then `footer_o`.
- `/component/section` is the only section type. `layout_s` is `html`, `blog-preview`, or `article-index`.
- `/page/article` stores the article body in `body_html` and card fields used by the blog index and home preview.
- `/page/resource` stores the AltWheels `<main>` in `main_html`.

## Statistics

| Category | Count |
|----------|------:|
| Page types | 3 |
| Global components | 3 (level descriptor, header, footer) |
| Section components | 1 (`/component/section`) |
| Item content types | 0 (repeat groups instead) |
| Landing pages | 7 |
| Article pages | 5 |
| Resource pages | 3 |
| Shared headers | 2 |
| Shared footers | 4 |
