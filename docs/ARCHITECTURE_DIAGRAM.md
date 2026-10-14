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
        REG["Region components"]
        AW["AltWheels components"]
    end
    subgraph RepeatGroups
        NAV["nav_o items"]
        CON["connect_o items"]
        TAG["tags_o / listTags_o items"]
    end
    LD -->|header_o| HDR
    LD -->|footer_o| FTR
    LAND -->|sections_o| REG
    RES -->|sections_o| AW
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
- Each region is its own component type, listed in `components.md`.
- `/page/article` stores author copy in `body_html` (`rte`). Card fields feed the blog index and home preview.
- `/page/resource` renders AltWheels regions from `sections_o`.

## Statistics

| Category | Count |
|----------|------:|
| Page types | 3 |
| Global components | 3 (level descriptor, header, footer) |
| Section components | 35 types, 41 content items |
| Item content types | 0 (repeat groups instead) |
| Landing pages | 7 |
| Article pages | 5 |
| Resource pages | 3 |
| Shared headers | 2 |
| Shared footers | 4 |
