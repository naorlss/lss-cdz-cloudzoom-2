# Fleet AI Reference Guide
Bill Scott · CloudZoom Solutions · AltWheels

Reviewed September 30, 2026. Model names, features, settings, plans and prices change. Consult the provider's current documentation before purchasing or configuring access. No ranking of providers or numerical price comparison is intended.

## How to read the handout
The numbered references below correspond to the source notes on the two-page action plan. The four use patterns, sample prompts, memory-document structure and fleet pilot examples are proposed teaching aids. They are not claims that a vendor feature guarantees an outcome. Every fleet application listed is hypothetical; no customer case study or savings claim is included.

## Two starting points
**Explore:** use an approved interactive service with a small knowledge kit and review its outputs. Start with an existing license or the lowest-cost suitable plan; upgrade only when a real requirement justifies it. That is a purchasing recommendation, not a claim that every free or personal plan satisfies company requirements.

**Apply:** choose a specific problem, identify necessary sources, tools and controls, and run a bounded test. A fixed workflow, ordinary software or a process improvement may be more appropriate than an agent. APIs and custom integrations are later choices, not prerequisites to learning.

## Memory practice
The proposed cycle is summarize, review, save and reload. Keep stable approved context in a Fleet Brief, operational definitions in a Data Guide, and ongoing decisions/actions in a dated Session Handoff. Review before approving it; confirm storage and retrieval. Do not use a handoff as a live database. Stale statements, sensitive information, superseded versions and content permissions require active management.

## SaaS assessment
For the software-subscription pilot, request authorized contract, invoice, license and feature-use evidence. Low login counts alone do not establish nonuse. Compare retain, downgrade, consolidate and build, and include one-time migration/build costs plus recurring hosting, model usage if any, maintenance, security and support. The prompt requests evidence and uncertainty; it does not promise cheaper replacement software or authorize any cancellation.

## Official sources

### [1] Four use patterns and workflows versus agents

- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Explains predefined workflows versus agents that select steps. The four Explore/Build/Automate/Guide labels are this handout’s teaching framework, not an industry standard.

### [2] Hosted service examples

- [OpenAI — ChatGPT Plus](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus) — Application features, limits and separate API billing.

- [Anthropic — Claude plans](https://claude.com/pricing) — Application capabilities, plans and feature availability.

- [Google — Gemini overview](https://gemini.google/overview/) — Examples of Gemini assistant capabilities.

- [Microsoft — Copilot for business plans](https://www.microsoft.com/en-us/copilot/pricing/business) — Work-app integration and plan distinctions.

- [Grok — product overview](https://x.ai/grok) — Examples of Grok capabilities.

### [3] Tokens, subscriptions and API costs

- [OpenAI — Understanding and counting tokens](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens) — Input, output and reasoning-token concepts.

- [OpenAI — ChatGPT Plus](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus) — API usage is separately billed; subscriptions have limits.

- [LM Studio — Offline operation](https://lmstudio.ai/docs/app/offline) — Local model use is a separate deployment choice. The handout recommends starting with an approved hosted app, not buying hardware.

### [4] Persistent instructions and better prompts

- [OpenAI — Custom instructions](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions) — Where user standing instructions are configured.

- [OpenAI — Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) — Project instructions, files, sharing and project-scoped context.

- [OpenAI — Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) — Clear instructions, examples and relevant context; developer-oriented reference, not an API prerequisite.

### [5] Session memory and safe retention

- [OpenAI — Memory in ChatGPT](https://help.openai.com/en/articles/8590148-memory-in-chatgpt) — Product memory controls and limitations.

- [Microsoft — Manage AI memory safety](https://learn.microsoft.com/en-us/security/zero-trust/sfi/manage-agentic-memory-safety) — Memory validation, access boundaries, freshness and poisoned-memory risks.

- [Anthropic — Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Curating relevant context and durable notes.

### [6] Company knowledge and retrieval

- [Microsoft — Retrieval-augmented generation](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview) — Retrieval, grounding, document preparation and access control. Data-guide templates here are proposed working aids, not automatic data validation.

### [7] Useful starting tools

- [OpenAI — Data analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt) — File analysis, calculation/code capabilities and supported workflows.

- [Anthropic — Writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) — Tool design and evaluation; tools expose specific operations.

### [8] Tools versus skills

- [Anthropic — Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — Skills package reusable instructions and resources.

- [Anthropic — Equipping agents with skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) — Skills can contain instructions, scripts and supporting materials; review their contents before enabling them.

### [9] Verification and evaluation

- [OpenAI — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) — Representative tests, objectives, evaluation criteria and iteration.

### [10] Security and unreliable output

- [OWASP — Prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) — Untrusted content can redirect model behavior; retrieval does not remove the risk.

- [OWASP — Excessive agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) — Limit permissions and capabilities; retain approval for consequential actions.

- [OWASP — Misinformation](https://genai.owasp.org/llmrisk/llm092025-misinformation/) — Incorrect output and overreliance risks.
