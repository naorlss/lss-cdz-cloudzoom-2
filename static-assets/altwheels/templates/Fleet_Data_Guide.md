# Fleet Data Guide
Status: DRAFT | Owner: [role] | Version: [version] | Reviewed: [date]

## Source inventory
| Source/system | Business purpose | Authoritative for | Owner | Coverage/as-of date | Refresh | Allowed audience | Known gaps |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [source] | [purpose] | [facts] | [role] | [date] | [cadence] | [group] | [gaps] |

## Definitions
| Field or term | Approved meaning | Unit/type | Source | Join/key rule | Missing-value rule | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| [field] | [do not guess] | [unit] | [source] | [rule] | [rule] | [role] |

## Metrics
For each metric record its purpose, approved formula, numerator/denominator, filters, comparison group, time zone, reporting period, exclusions and validation example. Do not adopt a guessed definition as approved.

## Identity and quality
Document vehicle-ID mappings, leading zeros, duplicates, unmatched rows, status codes, old assets, data errors and what to do when sources disagree.

## Exceptions and context
Specify reserve/seasonal vehicles, special duty cycles, incomplete reporting and valid reasons for low mileage. Attribute each rule to its owner and approved source.

## Allowed access
Identify approved exports, document retrieval and any later read-only query interfaces. Record who can access what; the actual application must enforce those permissions.

ERP means enterprise resource planning: a business system that may hold operational or financial records. RAG means retrieval-augmented generation: retrieve relevant source material before generating an answer; it is not a guarantee that the answer is correct.
