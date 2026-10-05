# Community Resources for CCAO-F (Claude Certified Associate – Foundations)

## Context

This file surveys community study material for the Claude Certified Associate – Foundations exam (code CCAO-F). It checks each source against the official exam guide, consolidates what the sources say is tested, collects practice questions for in-class drills, and lists structural ideas for lessons and a cheat sheet. The course is a 2-hour exam-prep session, so the priority is high-yield judgment patterns over feature trivia.

Source keys used below:

| Key | Source | URL fetched |
|---|---|---|
| OFFICIAL | Official exam guide v1.0 (PDF, linked from the Partner Academy certifications page) | https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542847%2FClaude+Certified+Associate+%E2%80%93+Foundations+Exam+Guide.pdf |
| CERTPAGE | Partner Academy certifications page | https://anthropic-partners.skilljar.com/page/partner-certifications |
| PREPPATH | Official prep course path | https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations |
| AMEY | Amey-Thakur/CLAUDE-CERTIFICATIONS, `associate-foundations/` | https://raw.githubusercontent.com/Amey-Thakur/CLAUDE-CERTIFICATIONS/main/associate-foundations/README.md (plus `notes.md`, `cheat-sheet.md`, `practice-questions.md`, `mock-exam-1..3.md`, `exam-guide.pdf` in the same folder) |
| EVG | evggzzz/ccao-f-guide (default branch `master`) | https://raw.githubusercontent.com/evggzzz/ccao-f-guide/master/guide.md |
| RAY | raybeecham/claude-certified-associate-foundations | https://raw.githubusercontent.com/raybeecham/claude-certified-associate-foundations/main/README.md (plus `docs/`, `practice-exams/`, `patterns/`, `modules/`) |
| PREP-GH | preporato/claude-certification-guide, `ccao-f/` | https://raw.githubusercontent.com/preporato/claude-certification-guide/main/ccao-f/guide.md |
| PREP-CERT | Preporato certificate page | https://preporato.com/certificates/claude-certified-associate-foundations |
| PREP-GUIDE | Preporato complete guide (blog) | https://preporato.com/blog/claude-certified-associate-foundations-complete-guide-2026 |
| PREP-PLAN | Preporato 3-week study plan (blog) | https://preporato.com/blog/ccao-f-study-plan-3-week-preparation-2026 |
| PREP-VS | Preporato CCAO-F vs CCDV-F (blog) | https://preporato.com/blog/ccao-f-vs-ccdv-f-which-claude-certification-2026 |
| ARCH | paullarionov/claude-certified-architect (different exam, format reference only) | https://raw.githubusercontent.com/paullarionov/claude-certified-architect/main/README.md and `guide_en.md` |

Fetch notes: the tree API returned 404 for `evggzzz/ccao-f-guide` on `main`; the repo's default branch is `master`, and all files loaded from there. The official certification registration page (https://anthropic-partners.skilljar.com/claude-certified-associate-foundations-certification) loaded but showed only the $99 price and a sign-in prompt.

## Findings

### Baseline: the official exam guide

AMEY ships a copy of the official guide (`exam-guide.pdf`). Its extracted text is identical to the PDF linked from CERTPAGE, so the community copy is a faithful mirror. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542847%2FClaude+Certified+Associate+%E2%80%93+Foundations+Exam+Guide.pdf]

- Version 1.0, effective July 2026. Exam code CCAO-F. [source: OFFICIAL]
- 60 items. Multiple-choice and multiple-response, and each item states how many responses to select. 120 minutes. [source: OFFICIAL]
- Scaled score from 100 to 1,000. The cut score is 720. Criterion-referenced. The report shows pass/fail, the scaled score, and percent-correct by domain. Domain percentages do not decide pass or fail. [source: OFFICIAL]
- $99 USD. Pearson VUE delivery, online proctored or at a test center. Valid 12 months. On-time renewal is a free, non-proctored assessment on Partner Academy. A lapsed credential requires the full exam at full fee. [source: OFFICIAL]
- Retake waits are 14, 30, and 90 days after the 1st, 2nd, and 3rd failures. Candidates get at most 4 attempts per rolling 12 months, and each attempt costs the fee. Cancel or reschedule ≥24 hours ahead. [source: OFFICIAL]
- No prerequisites. Not intended for API developers or agentic-system designers. Associates escalate complex or technical work to Architects and Developers. [source: OFFICIAL]
- The exam does not count toward Claude Partner Network tier eligibility. Non-partners see an "apply to become one" prompt. [source: https://anthropic-partners.skilljar.com/page/partner-certifications]
- Domain weights: D1 Prompting and Task Execution 14%, D2 Output Evaluation and Validation 21%, D3 Product and Model Selection 12%, D4 Workflow Integration and Solution Design 16%, D5 Configuration and Knowledge Management 12%, D6 Governance, Risk, and Responsible Use 15%, D7 Troubleshooting and Optimization 10%. [source: OFFICIAL]
- The guide gives three sample items with rationales: verify a cited subsection (D2), pick a fast, low-cost model for high-volume replies (D3), and anonymize identifiers before upload (D6). [source: OFFICIAL]
- The official prep path has 8 modules: Platform & Model Foundations (59 min), Prompting (53), Evaluating & Validating Output (74), Workflow Integration (63), Configuration & Knowledge (47), Governance (55), Troubleshooting (30), Summary (8). The path recommends Claude 101, AI Fluency: Framework & Foundations, and AI Capabilities and Limitations as prerequisites. [source: https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations]

### Per-source summaries

#### AMEY: Amey-Thakur/CLAUDE-CERTIFICATIONS (`associate-foundations/`)

- **Covers:** a README that condenses the official guide, the official PDF itself, domain notes, a one-page cheat sheet, 35 practice questions with rationales, and three 15-question timed mocks with answer keys and readiness tables. The repo root also has Claude Code slash commands (`/cert:drill`, `/cert:mock`, `/cert:diagnostic`, `/cert:score-check`) and an `exam-coach` skill. [source: https://raw.githubusercontent.com/Amey-Thakur/CLAUDE-CERTIFICATIONS/main/associate-foundations/README.md]
- **Quality:** high. This source tracks the official guide most closely. It separates official facts from the maintainer's advice. Its questions are original, scenario-based, and use "distractors that fail the stated constraint." Facts were last verified 2026-10-03. [source: AMEY README, practice-questions.md]
- **Notable claims:**
  - Registration "requires a partner company email address recognized in the Claude Partner Network." [source: AMEY README] [unverified: the official guide does not state this, and CERTPAGE only says non-partners should apply]
  - Seat time is about 135 minutes. [source: AMEY README] [unverified: the official guide says only 120-minute time limit]
  - Results appear on screen immediately, and the badge comes via Credly. [source: https://raw.githubusercontent.com/Amey-Thakur/CLAUDE-CERTIFICATIONS/main/associate-foundations/notes.md] [unverified: not in the official guide]
  - "There is no practice exam. The sample questions in the guide are the only official items available." [source: AMEY README]
  - The sample rationales reward three moves: verify against authoritative sources, match the model tier to the task, and anonymize before upload rather than instructing the model. [source: AMEY README]

#### EVG: evggzzz/ccao-f-guide

- **Covers:** one long "Enhanced Edition" guide (English and Japanese). It is laid out like the official Architect exam guide v0.2 and organized by the official task statements (1.1–7.3). Each domain ends with a "common pitfall" box and a list of sources. The guide also has 15 sample questions (3 official, 12 original), 4 hands-on exercises, and in-scope and out-of-scope appendices. [source: https://raw.githubusercontent.com/evggzzz/ccao-f-guide/master/guide.md]
- **Quality:** mixed. The task-statement structure is useful. But most enrichment cites developer-platform docs (platform.claude.com API pages, managed-agents memory, compliance API), and that pulls the content well past the Associate scope. [source: EVG guide]
- **Notable claims and problems:**
  - "In my experience taking the exam... Items were evenly distributed across all blueprint domains." [source: EVG guide] This anecdote conflicts with the official weights (10–21%). [unverified]
  - The guide changes the official sample distractors. On sample 2 it replaces option D ("Switch to a different AI platform") with "one mid-tier model for every reply". On sample 3 it replaces option D ("Skip the analysis entirely") with "a consumer Claude.ai account". It still labels them "from the official CCAO-F Exam Guide". [source: EVG guide; compare OFFICIAL Section 8]
  - Its "Topics Covered" list includes XML tags, the prompt generator and improver, Structured Outputs with constrained decoding, few-shot with 3–5 examples, and the Constitution's priority order. Its own "Not Covered" list excludes "Constitutional AI" and API development. The two lists contradict each other. [source: EVG guide]
  - It lists a model tier called "Fable (highest capability, long-running agents, 1M)" and context sizes per model (Haiku 200k, Sonnet and Opus 1M). [unverified: volatile facts, not checked for this file, and the official guide names only Haiku, Sonnet, and Opus]
  - Governance pitfalls: masking before upload, qualified review for high-risk decisions, RBAC, subgroup disparate-impact monitoring, age-coded job-ad language ("digital native"), and no fabricated testimonials. [source: EVG guide]

#### RAY: raybeecham/claude-certified-associate-foundations

- **Covers:** 8 modules that mirror the official prep path one-to-one. Each module has lessons, notes, a lab, flashcards, and a quiz. The repo also has a master cheat sheet, an exam-strategy doc, a glossary, 30+ "pattern" cards, prompt notebooks, `data/questions.json`, a study CLI, and three practice exams: two balanced 28-item exams and one blueprint-weighted 60-item exam with multiple-response items. A vendor-neutral "AI Systems Engineering" playbook is attached. [source: https://raw.githubusercontent.com/raybeecham/claude-certified-associate-foundations/main/README.md]
- **Quality:** high on judgment frameworks and very thorough. It drifts toward engineering in places: the cheat sheet covers idempotency keys, cache breakpoints, prompt injection, and stop reasons. [source: https://raw.githubusercontent.com/raybeecham/claude-certified-associate-foundations/main/docs/master-cheat-sheet.md]
- **Notable claims:**
  - It provides a crosswalk because the course and exam number domains differently: repo Module 1 (Platform & Model Foundations) maps to official Domain 3. [source: RAY README]
  - It uses AI Fluency vocabulary: Delegation, Discernment, and Diligence. Examples are "Diligence gap" (the difference between required governance and observed practice) and delegation modes (AI-appropriate, collaborative, human-retained). [source: https://raw.githubusercontent.com/raybeecham/claude-certified-associate-foundations/main/modules/04-workflow-integration-solutions-design/lessons/05-delegation-mapping.md]
  - The 60-item mock allocates 8/13/7/10/7/9/6 items across D1–D7, the closest integer fit to the weights. Multiple-response items are scored all-or-nothing. [source: https://raw.githubusercontent.com/raybeecham/claude-certified-associate-foundations/main/practice-exams/README.md]
  - It warns that model names, limits, pricing, plan entitlements, and exam logistics are "volatile facts" to re-verify. [source: https://raw.githubusercontent.com/raybeecham/claude-certified-associate-foundations/main/docs/certification-overview.md]

#### PREP-GH and the preporato.com pages

- **Covers:** a ~5,100-word guide in three parts. Part I has 7 topic chapters, Part II has domain notes (Know / Be able to / Anti-patterns), and Part III has six named trap answers, 10 worked questions, a 3-week plan, and a pre-exam checklist. The blogs add a day-by-day plan and a CCAO-F vs CCDV-F comparison. Paid tier: six 60-question tests and 500 flashcards. [source: https://raw.githubusercontent.com/preporato/claude-certification-guide/main/ccao-f/guide.md]
- **Quality:** good and exam-focused, with compact decision tables. It is commercial and pushes paid practice tests. Some facts go beyond the official guide (see Disagreements). [source: PREP-GH]
- **Notable claims:**
  - "Single-answer plus multiple-response (~a quarter of items), no partial credit." [source: PREP-GH; https://preporato.com/blog/claude-certified-associate-foundations-complete-guide-2026] [unverified]
  - Registration requires free Claude Partner Network membership. [source: https://preporato.com/blog/ccao-f-study-plan-3-week-preparation-2026]
  - The scope is the claude.ai product only: "API knowledge earns nothing here." [source: https://raw.githubusercontent.com/preporato/claude-certification-guide/main/ccao-f/README.md]
  - "Default to Sonnet and move on evidence." [source: PREP-GH]
  - It gives a launch date of July 23, 2026 (as reported by the fetch of PREP-GUIDE). [unverified]
  - Comparison: CCDV-F has 53 items at $125. CCAO-F has 60 items at $99. Both are 120 minutes with a 720 cut score. [source: https://preporato.com/blog/ccao-f-vs-ccdv-f-which-claude-certification-2026]
  - Study plan: ~1 hour/day, ~20 hours over 3 weeks. Revisit any domain scoring below ~80%. [source: PREP-PLAN]

#### ARCH: paullarionov/claude-certified-architect (format reference only)

- **Covers:** a single long guide in 15 languages, with PDF and EPUB builds, Anki decks, an HTML "practical test" app, and a NotebookLM video link. The guide runs Part I Theory (13 chapters), Part II Exam Domain Notes (each task has "Key knowledge" and "Key skills" lists plus anti-patterns), worked exam questions grouped by scenario, a scenario-grouped practice test, practical exercises, a technologies appendix, an out-of-scope list, and preparation recommendations. [source: https://raw.githubusercontent.com/paullarionov/claude-certified-architect/main/README.md]
- **Reading-habit advice worth borrowing:** find the "deciding phrase" in the stem, prefer the proportionate first step, and "separate guidance from guarantees". The last one maps directly to CCAO-F's rule that an instruction to the model is not a control. [source: ARCH README]

### Disagreements between sources

| Topic | Official guide | Community claims | Status |
|---|---|---|---|
| Score scale | 100–1,000, cut 720 | PREP-CERT page says "0–1000" | Use 100–1,000 [source: OFFICIAL; https://preporato.com/certificates/claude-certified-associate-foundations] |
| Multiple-response share and partial credit | Each item states how many to select. No share or partial-credit rule is published | Preporato: ~25% multiple-response, no partial credit. RAY scores its own mocks all-or-nothing. EVG: most items are 1-of-4 | Teach "assume no partial credit" as a safe heuristic. Mark the share [unverified] |
| Registration eligibility | Partner Academy. Non-partners are prompted to apply | AMEY: partner company email recognized in CPN. Preporato: free CPN membership | Tell learners to check the Partner Academy page. Mark both claims [unverified] [source: CERTPAGE] |
| Domain numbering | D1 Prompting … D7 Troubleshooting | PREP-GH renumbers by weight (Output Eval = Domain 1). PREP-PLAN uses a third order (Workflow Integration = 7). RAY modules follow the prep-course order (Module 1 = official D3) | Always use official numbering in slides |
| Item distribution | Weighted 10–21% | EVG says items were "evenly distributed" based on the author's own sitting | Trust the official weights. Treat EVG's claim as anecdote [unverified] |
| Scope depth | Not for API builders. Prep should cover Projects, Artifacts, Memory, Skills, and Code Execution | Preporato: claude.ai only, API "earns nothing". EVG: tests XML tags, Structured Outputs, few-shot counts, Constitution ordering, commercial-terms training rules | Treat EVG's API-level material as out of scope unless the official prep course covers it |
| Official sample wording | Sample 2 D = "Switch to a different AI platform". Sample 3 D = "Skip the analysis entirely" | EVG rewrites both D options | Quote the official text, not EVG's |
| Default model framing | Match the model to the task. The guide gives no default | PREP: "default to Sonnet". AMEY/RAY: "smallest/fastest model that holds quality" | Both frames lead to the same exam answers. Avoid stating a default as official |
| Logistics extras | Not stated | AMEY: ~135 min seat time, immediate results, Credly. Preporato: Credly | [unverified] |
| Preporato practice-bank size | n/a | "360+" (cert page) vs "390+" (study plan) | Minor internal inconsistency |

## Consolidated topic map by domain

Facts in the "Official objective" lines come from OFFICIAL Section 6. Bullets beneath list what community sources say is tested.

### D1 Prompting and Task Execution (14%)

Official objective: create effective prompts, decompose complex requests, iterate, and adapt strategy by task type (analysis, research, drafting, brainstorming). [source: OFFICIAL]

- Five-part business prompt: role/context, task, source material, constraints (audience, length, tone), and output format. Every improvement traces back to one of the five. [source: PREP-GH]
- RAY's "task contract" is a longer form of the same list: objective, audience, inputs, authoritative sources, constraints, process, output schema, uncertainty behavior, and success criteria. [source: RAY master-cheat-sheet]
- Structure beats intensifiers. "Be detailed and thorough" or "be concise" do not fix output. Concrete limits (word count, number of bullets) and a filled example do. [source: AMEY cheat-sheet; AMEY practice Q24, Q25]
- Decomposition is the tested answer for multi-part deliverables, long documents, or shallow output from one giant prompt. Each step yields something you can check. [source: PREP-GH; AMEY practice Q4, Q26]
- Iteration means targeted feedback ("cut to half, more direct, keep the three statistics") rather than regenerating. [source: PREP-GH]
- Strategy by task type: [source: PREP-GH]
  - Analysis: provide sources, name the criteria, and ask for reasoning before conclusions.
  - Research: use research mode and require checkable sources.
  - Drafting: give audience, tone, length, format, and an example.
  - Brainstorming: ask for volume first, then narrow.
- If you want a recommendation, ask for one. A "balanced discussion" means the prompt never requested a decision. [source: AMEY mock-exam-3 Q8]
- API-level prompt techniques (XML tags, 3–5 few-shot examples in `<example>` tags, long document at the top and query at the end). [source: EVG guide] [unverified as in scope]

### D2 Output Evaluation and Validation (21%, the largest domain)

Official objective: accuracy and completeness, hallucinations, inconsistencies and bias, fact-checking, when human review is needed, adapting output for the audience, and output format (artifact, inline, structured). [source: OFFICIAL]

- Hallucination red flags: [source: PREP-GH]
  - specific numbers, dates, or statistics with no source
  - named studies or quotes you can't locate
  - details beyond the provided material
  - uniform confidence across claims
  - post-cutoff facts without research mode or an attached source
- Confidence is not evidence. Self-rated confidence, a self-check ("double-check your work"), and agreement across reruns all fail to validate a claim. [source: OFFICIAL Sample 1; AMEY mock-exam-2 Q2; AMEY practice Q12]
- Omission is a failure even when every word is true. Extraction fails by omission more often than by error. Read the source, not only the output. [source: AMEY cheat-sheet; AMEY practice Q13]
- Verifying one claim does not validate the rest. [source: AMEY mock-exam-3 Q1]
- Validation sequence: [source: PREP-GH; RAY practice-exam-03 Q18, Q49]
  1. Verify names, numbers, dates, and quotes against the source of record.
  2. Ask Claude which passage supports a claim.
  3. Cross-check external facts independently.
  4. Watch for bias: one-sided framing, stereotyped examples, missing counterarguments.
- Grounding techniques: quote the passage first, cite the section or clause, allow "not supported / unknown", and use only the attached sources. [source: RAY practice-exam-03 Q18, Q49; EVG guide]
- Human review is mandatory for: [source: PREP-GH]
  - external-facing output
  - legal, financial, or health content
  - decisions about people (hiring, performance, vendors)
  - regulated workflows
- Review depth scales with consequences: a skim for brainstorms, source verification for summaries, qualified human review for external or consequential output. [source: https://preporato.com/blog/claude-certified-associate-foundations-complete-guide-2026]
- Three-reference review: check the output against the task requirements, the evidence, and professional standards. [source: https://raw.githubusercontent.com/raybeecham/claude-certified-associate-foundations/main/patterns/three-reference-discernment-pattern.md]
- A declared gap ("data unavailable") is a finding. Keep it rather than filling it with an estimate. [source: AMEY practice Q11]
- Formats: [source: PREP-GH]
  - inline for quick answers
  - an Artifact for a deliverable you will revise and share
  - a structured format (table, list) for output feeding another step
- Calculations: a clean table with a wrong subtotal should be recomputed with Code Execution. Executed code still needs its logic and source data checked. [source: RAY practice-exam-03 Q13, Q59]

### D3 Product and Model Selection (12%)

Official objective: features (Projects, research mode, chat, artifacts), Haiku/Sonnet/Opus, cost/speed/quality alignment, and context and memory (restart, summarize, persist). [source: OFFICIAL]

- Model tiers: Haiku is fastest and cheapest, for high-volume routine work. Sonnet is balanced, for everyday work. Opus is the most capable, for complex reasoning worth the cost. "Strongest model everywhere" is a recurring wrong answer. So is "smallest model for hard work". [source: AMEY notes; PREP-GH; OFFICIAL Sample 2]
- A larger model does not fix a governance, format, process, or grounding problem. [source: AMEY cheat-sheet; RAY master-cheat-sheet]
- Benchmarks are a general signal. They do not replace testing on your own task. [source: AMEY mock-exam-2 Q11]
- Feature triggers: [source: PREP-GH; RAY master-cheat-sheet]
  - Chat for one-off work.
  - A Project for recurring context.
  - Research mode for current, citable information.
  - An Artifact for an editable deliverable.
  - Features combine: a recurring current-information workflow may use a Project, Research, and an Artifact together.
- RAY's capability layer: [source: RAY master-cheat-sheet]
  - A Skill holds a repeatable ordered procedure.
  - Code Execution handles calculation, charts, and files.
  - Memory gives cross-session continuity but is not a source of truth.
  - Incognito reduces persistence but does not make data approved.
- Context moves: [source: PREP-GH; RAY master-cheat-sheet]
  - Restart when a long chat drifts or ignores instructions.
  - Summarize decisions into the new chat.
  - Persist durable material into Project knowledge.
- "Context limit" (depth of one conversation) is a different thing from "usage limit" (amount of use over time). [source: RAY master-cheat-sheet]
- Long inputs dilute attention. Quality drops when relevant material competes with much more text. [source: AMEY mock-exam-2 Q8]
- Projects suit exploratory, human-driven work. High volume, scheduled runs, and automatic handoff to other systems point to the API, which means escalating to Developer/Architect. [source: AMEY practice Q29]

### D4 Workflow Integration and Solution Design (16%)

Official objective: analyze requirements and use cases, research and planning, solution design and iteration, augment or redesign workflows, and communicate value and limitations. [source: OFFICIAL]

- Define the deliverable, audience, sources, and success before prompting. [source: PREP-GH]
- Strong fits: drafts, summaries, repurposing, brainstorming. [source: PREP-GH]
- Weak fits: [source: PREP-GH]
  - final factual authority
  - accountable decisions
  - precise high-volume calculation a spreadsheet should own
  - live data without research mode
- "Can Claude do X?" is answered with a division of labor: what Claude drafts, what humans judge, and where the review step sits. [source: AMEY cheat-sheet; AMEY practice Q7]
- Delegation criteria are reversibility, stakes, and accountability. Modes are AI-appropriate, collaborative, and human-retained. [source: RAY delegation-mapping lesson; RAY practice-exam-03 Q38]
- Pilot one workflow, measure, then expand. Big-bang rollouts lose. [source: PREP-GH; AMEY mock-exam-3 Q5]
- Question whether a step is needed before automating it. "Automating unnecessary work makes waste faster." [source: AMEY mock-exam-3 Q4]
- Stakeholder framing pairs a concrete benefit with an honest limitation and names the human approver. [source: PREP-GH; RAY practice-exam-03 Q20]
- Keep a human approval step where an action is hard to reverse or has external consequences. [source: AMEY practice Q19]
- Escalate integrations with internal systems to Developers/Architects. [source: AMEY cheat-sheet; OFFICIAL Section 3]

### D5 Configuration and Knowledge Management (12%)

Official objective: configure Projects with instructions and knowledge, manage uploaded knowledge and connectors (Google Drive, Gmail), write system-level instructions, and maintain configurations. [source: OFFICIAL]

- Placement table: [source: PREP-GH]
  - Standing tone, role, and format go in Project instructions.
  - Reference docs go in Project knowledge.
  - Today-only details go in the chat prompt.
  - Frequently changing email or files go through a connector.
- RAY's short form: "Standing instructions = how Claude should behave. Knowledge = what Claude should know." [source: RAY master-cheat-sheet]
- Project knowledge does not update itself. Replace superseded documents rather than accumulating them. Keeping both versions produces mixed answers, and stale knowledge produces confidently outdated answers. [source: AMEY practice Q8, Q33; AMEY mock-exam-3 Q12]
- Adding many documents can dilute or contradict the right sources. [source: AMEY practice Q10, Q32]
- Duplicate copies across teams drift apart. [source: AMEY mock-exam-2 Q12]
- A good instruction includes a guardrail: "All statistics must come from the attached fact sheet; if not there, say so." [source: PREP-GH]
- Narrow connectors to the minimum folders. "Connect everything and tell Claude to ignore it" is unreliable. [source: EVG guide]
- Use topic sections rather than one long paragraph of rules. Resolve contradictory rules ("concise" vs "comprehensive") with an explicit priority. [source: EVG guide]
- Review third-party and internal Skills before use. Check provenance, reach, and proportionality. [source: RAY practice-exam-03 Q12, Q56]

### D6 Governance, Risk, and Responsible Use (15%)

Official objective: appropriate and inappropriate use cases, data sensitivity, regulatory and privacy considerations, organizational AI policy, and ethical implications. [source: OFFICIAL]

- Make the task safe, then do it: anonymize or pseudonymize before upload. Three answers are wrong: uploading as-is, telling the model to ignore or not retain data, and abandoning the task. [source: OFFICIAL Sample 3; AMEY notes]
- An instruction to the model shapes behavior but does not guarantee it. Controls live outside the prompt. [source: AMEY practice Q21]
- Neither the requester's purpose nor their seniority overrides policy. [source: AMEY cheat-sheet; AMEY mock-exam-1 Q5]
- "Summarizing" customer data still means submitting it. [source: AMEY mock-exam-3 Q6]
- Anonymized free text can still identify people. [source: AMEY mock-exam-2 Q6]
- Two decision rules: [source: PREP-GH]
  - If the output affects rights, money, health, or legal standing, a qualified human owns the call.
  - If data would cause harm if leaked, the policy check comes before productivity.
- Accountability stays with whoever files or sends. The tool does not transfer it. [source: AMEY practice Q22; AMEY mock-exam-2 Q7]
- Disclosure: don't present AI output as human-written or as independently verified. Disclose where provenance would change how the reader judges the work. [source: AMEY practice Q23; AMEY mock-exam-3 Q7; PREP-GH]
- Shadow AI (personal accounts): contain the practice, record the Diligence gap, and make the compliant path the easy default. [source: RAY practice-exam-03 Q42]
- Ethics examples: [source: EVG guide]
  - Watch for age-coded job ads.
  - Don't fabricate testimonials.
  - Monitor subgroup impact.
  - No autonomous legally binding actions.
- A refusal with a reason tells you something about a limit or policy. Don't work around it. [source: AMEY mock-exam-3 Q2]
- Consumer vs commercial data-training terms, AUP high-risk use cases, and the Constitution priority ordering. [source: EVG guide] [unverified as in scope]

### D7 Troubleshooting and Optimization (10%)

Official objective: diagnose underperforming prompts and outputs, adjust from feedback, optimize workflows. [source: OFFICIAL]

- Symptom → cause → first fix: [source: PREP-GH]

  | Symptom | Cause | First fix |
  |---|---|---|
  | Generic output | Missing context | Add role, audience, sources, example |
  | Late-chat instruction loss | Drift | Restart with a summary, move rules into Project instructions |
  | Confident wrong business facts | No source | Attach or connect the source |
  | Wrong format | Format described vaguely | Show an example |
  | Variance across teammates | No shared setup | Shared Project |
  | Half a request ignored | Too many asks | Decompose |

- When something that worked breaks, find what changed (inputs, configuration, knowledge) before rewriting anything. [source: AMEY practice Q34; AMEY mock-exam-3 Q14]
- Change one variable at a time. [source: PREP-GH; RAY master-cheat-sheet]
- If you can't reproduce a problem, get the exact prompt, inputs, and configuration. [source: AMEY mock-exam-2 Q14]
- Run-to-run variation is normal. Design for tolerance. [source: AMEY mock-exam-2 Q15]
- If one analyst succeeds and others fail with the same prompt, look for unstated context. [source: AMEY practice Q18]
- Optimize by finding the actual bottleneck, which is often the human steps. [source: AMEY practice Q35]
- Optimization means lower cost and time at equal quality: reusable prompts, Projects, and the smallest model that holds quality. [source: AMEY notes]

## Practice questions

All items are scenario or judgment questions with answer and a one-line rationale. Stems are paraphrased. "MR" marks multiple-response items. Domain uses official numbering.

### Official samples

1. **(D2)** Claude confidently summarizes a new regulation and cites a specific subsection. You are about to send it to compliance. A) send since confident B) verify the subsection against the official text C) ask Claude to rate its confidence D) reword more formally. **Answer: B.** Specific citations can be fabricated, and self-reported confidence is not evidence. [source: OFFICIAL]
2. **(D3)** You need many short customer-reply drafts, and speed and cost matter more than depth. A) top model every time B) faster, lower-cost model C) disable features D) switch AI platform. **Answer: B.** Match the tier to the task and save the top model for complex reasoning. [source: OFFICIAL]
3. **(D6)** A PM wants to upload a spreadsheet with customer names and account numbers for trend analysis. Policy restricts regulated personal data. A) upload since it's internal B) remove or anonymize identifiers first C) upload but tell Claude not to retain D) skip the analysis. **Answer: B.** Anonymizing makes the task compliant. "Don't retain" is not a control, and abandoning the task is unnecessary. [source: OFFICIAL]

### Output Evaluation (D2)

4. Claude's contract summary says termination needs 60 days' notice, citing §14.2, and it's headed to legal. A) check §14.2 first B) send because it cites a section C) ask its confidence D) rephrase formally. **Answer: A.** A precise citation is a hallucination surface, so verify it against the document. [source: AMEY practice Q1]
5. Two runs of the same prompt give different figures for one metric. A) the higher figure is better B) average them C) neither is established, so check the source D) the model needs a longer context. **Answer: C.** Disagreement shows the figure isn't grounded, and averaging two unverified numbers doesn't help. [source: AMEY practice Q12]
6. Claude extracts four payment terms from a 40-page contract, cleanly formatted. First check? A) formatting consistency B) ask Claude if it found all C) rerun at higher temperature D) read the payment sections for omissions. **Answer: D.** Extraction fails by omission, and tidy formatting says nothing about completeness. [source: AMEY practice Q13]
7. A comparison table has one row marked "data unavailable", and a colleague wants it deleted. A) delete B) keep the row and label C) fill with an estimate D) push Claude to search harder. **Answer: B.** A declared gap is a finding. Filling it invites fabrication. [source: AMEY practice Q11]
8. Claude summarizes your Q2 report and adds an "18% growth" figure and a Gartner citation that the source never contains. A) Claude calculated it, keep it B) hallucination, remove or verify C) newer data, keep it D) formatting error, regenerate. **Answer: B.** Details beyond the provided material are a red flag. [source: PREP-GH Q1]
9. A colleague asks Claude to check its own earlier answer, and it confirms. How much weight does that carry? A) none on its own B) substantial C) substantial if detailed D) depends on the model. **Answer: A.** A self-check is not independent of the thing being checked. [source: AMEY mock-exam-2 Q2]
10. **MR, pick 2.** Which make human review mandatory? A) internal meeting agenda B) customer billing-complaint reply under the company name C) internal tagline brainstorm D) summary feeding a vendor-termination decision E) reformatting your own notes. **Answer: B, D.** External, financial, and consequential-decision outputs need review. [source: PREP-GH Q6]
11. **MR, pick 3.** Which instructions reduce hallucination in document-grounded work? A) "If the documents don't support it, say so" B) "Use only the attached source and list gaps" C) "Answer confidently even if evidence is incomplete" D) "Cite the section supporting each claim". **Answer: A, B, D.** Permission to say "unknown", bounded sources, and citations all reduce invention. [source: RAY practice-exam-03 Q49]
12. A reconciliation table is neatly formatted, but the subtotal doesn't match its line items. A) accept B) make the subtotal less precise C) recompute with code execution and reconcile D) submit and explain later. **Answer: C.** Exact arithmetic belongs in deterministic computation. [source: RAY practice-exam-03 Q13]
13. **MR, pick 2.** Code Execution returns a total for a material decision. What must still be checked? A) the prose sounds confident B) logic, formulas, definitions, and edge cases C) assume executed code is correct D) source data, units, filters, and reconciliation. **Answer: B, D.** Running code proves the method ran, not that the method or inputs were right. [source: RAY practice-exam-03 Q59]

### Prompting (D1)

14. A colleague's prompt "analyze our customer feedback and fix the problems" gives generic output. Best decomposition? A) add "be specific" B) ask three times and merge C) paste more feedback D) categorized themes with counts, then top three, then one action each. **Answer: D.** Decomposition turns a vague compound request into steps you can check. [source: AMEY practice Q4]
15. Output is accurate but always too long. A) add "be concise" B) summarize afterwards C) state a word or bullet limit D) use a smaller model. **Answer: C.** Concrete limits can be checked and reproduced. Adjectives can't. [source: AMEY practice Q24]
16. Output must paste into a fixed template every time. A) describe the structure in prose B) ask for "well organized" C) generate twice and pick D) provide a filled example. **Answer: D.** An example is the strongest signal for format. [source: AMEY practice Q25]
17. "Write a blog post about our new product" returns generic copy. A) regenerate B) top model C) role, audience, tone, length, product sheet, and an example post D) split across three chats. **Answer: C.** Generic output means missing context and constraints. [source: PREP-GH Q4]
18. **MR, pick 3.** A PM has 200 survey responses and wants the top three issues by frequency. Which elements improve the specification? A) "You are a product analyst" B) "Attached are 200 survey responses" C) "Make it insightful and polished" D) "Count the 3 most frequent issues with a quote and share each, ranked". **Answer: A, B, D.** Role, context, and a countable output contract help. Polish adjectives don't. [source: RAY practice-exam-03 Q31]
19. You asked for a recommendation and got a balanced discussion. Likely cause? A) Claude can't recommend B) temperature C) the prompt didn't require a single recommendation with a reason D) input too short. **Answer: C.** Output shape follows the instruction. [source: AMEY mock-exam-3 Q8]

### Product and Model Selection (D3)

20. A rep needs 50 simple, lightly personalized email openers this afternoon, and the manager wants usage kept light. A) Opus B) Sonnet as the default C) Haiku D) Research. **Answer: C.** The task is simple, high-volume, and time-sensitive. [source: PREP-PLAN]
21. You need competitors' pricing announced in the last month for a presentation. A) trust training knowledge B) research mode, then verify cited pages C) Opus has newer knowledge D) ask three times. **Answer: B.** Recent facts trigger research mode, and the citations still need checking. A bigger model doesn't move the training cutoff. [source: PREP-GH Q8]
22. Twenty turns into a chat, Claude ignores your early formatting rules. A) repeat the rules forcefully B) restart with a summary and move the rules to Project instructions C) faster model D) ask why. **Answer: B.** Restart, summarize, and persist. [source: PREP-GH Q7]
23. A team wants a bigger model because outputs are inconsistent. What should be established first? A) whether the prompt and inputs cause the inconsistency B) cost difference C) regional availability D) speed. **Answer: A.** Underspecified tasks cause variance, and a larger model won't fix them. [source: AMEY practice Q30]
24. A coordinator writes the same weekly status report from stable background docs in a fixed format. Foundation? A) a new chat weekly B) research mode C) a Project with recurring context and instructions D) Incognito with pasted context. **Answer: C.** Recurring, stable context is the trigger for a Project. [source: RAY practice-exam-03 Q3]

### Workflow Integration (D4)

25. A department head asks, "Could Claude handle our customer onboarding?" A) yes, start building B) map the steps and mark which Claude can draft, summarize, or look up, and which need human judgment or system access C) no, it involves customer data D) ask Anthropic support. **Answer: B.** The answer is a division of labor, not a yes or no. [source: AMEY practice Q7]
26. Which monthly-reporting step is the weakest candidate for delegation? A) draft the narrative from agreed figures B) reformat into the new template C) extract the top five variances D) decide which account to escalate to execs. **Answer: D.** That decision carries accountability and relationship context. [source: AMEY practice Q17]
27. A four-hour manual process produces a document nobody reads. What comes before automating it? A) automate now B) ask whether the work is needed C) automate faster D) redistribute it. **Answer: B.** Automating waste makes waste faster. [source: AMEY mock-exam-3 Q4]
28. **MR, pick 2.** What makes a stakeholder description of an AI-assisted contract-review workflow credible? A) state the bounded tasks Claude performs B) call it fully automated C) name the qualified human approver D) omit limitations. **Answer: A, C.** Credibility comes from clear value, clear limits, and a named human. [source: RAY practice-exam-03 Q20]
29. **MR, pick 3.** When mapping a workflow for delegation, which criteria matter? A) reversibility B) stakes C) accountability D) model popularity. **Answer: A, B, C.** These three decide AI-appropriate vs collaborative vs human-retained. [source: RAY practice-exam-03 Q38]

### Configuration and Knowledge (D5)

30. HR publishes a new handbook, and your Project answers policy questions from the old one. A) nothing, Claude finds it B) add the new one alongside the old C) replace the old one and spot-check D) tell users to mention the new version. **Answer: C.** Knowledge does not self-update, and keeping both versions gives mixed answers. [source: AMEY practice Q8]
31. A Project's answers got vaguer after a dozen new documents were added. A) the model changed B) too few documents C) overlapping or outdated material competes with the right sources D) prompts too specific. **Answer: C.** Unmaintained accumulation dilutes retrieval. [source: AMEY practice Q32]
32. Five analysts' weekly client reports vary in tone, structure, and where their statistics come from. One fix for all three? A) the best analyst reviews everything B) a shared Project with standards in instructions and approved sources in knowledge C) the top model D) a shared prompt doc. **Answer: B.** Variance across teammates means there is no shared setup. [source: PREP-GH Q9]
33. Several colleagues use one Project for client messages. What belongs in the Project instructions? A) today's client name B) today's date C) house tone, required disclaimers, and standard structure D) personal preferences. **Answer: C.** Instructions hold what recurs across every chat. [source: AMEY mock-exam-1 Q9]

### Governance (D6)

34. Legal requests analysis of support tickets that contain names and emails, and policy bars sending personal data to external tools. A) upload, legal asked B) upload and tell Claude to disregard those columns C) strip or pseudonymize the columns, then analyze D) say it's impossible. **Answer: C.** Neither the requester's seniority nor the purpose overrides policy. [source: AMEY mock-exam-1 Q5]
35. A manager wants Claude to rank five reps for promotion from performance notes. A) fine if anonymized B) fine with Opus C) Claude can organize the notes, but the manager owns the decision D) never use Claude near this data. **Answer: C.** A decision about people requires human judgment. Anonymizing fixes privacy but not accountability. [source: PREP-GH Q2]
36. A team removed names from customer feedback before theme analysis. What risk remains? A) none B) permanent storage C) the analysis is unreliable D) free text can still identify people. **Answer: D.** Anonymization of free text is not automatically complete. [source: AMEY mock-exam-2 Q6]
37. Someone asks that Claude output be presented to a customer as human-written. A) decline and raise the disclosure question with the relationship owner B) comply, quality matters more C) comply if heavily edited D) comply and log it. **Answer: A.** Misrepresenting provenance is the issue. [source: AMEY mock-exam-3 Q7]
38. **MR, pick 2.** An audit finds staff pasting client drafts into personal Claude accounts because the approved workspace is hard to reach. A durable response? A) contain the practice and record the Diligence gap B) remove the friction so the compliant path is easiest C) ban all AI permanently D) treat it as individual misconduct only. **Answer: A, B.** Fix the system cause, not only the people. [source: RAY practice-exam-03 Q42]

### Troubleshooting (D7)

39. A prompt that worked for weeks degrades after many new documents are added to the Project. First diagnostic? A) check whether the new knowledge dilutes or contradicts the old B) rewrite the prompt C) bigger model D) rebuild the Project. **Answer: A.** Suspect the change that coincided with the regression. [source: AMEY practice Q10]
40. A prompt works for one analyst and fails for three others. Likely cause? A) the first analyst supplies context without noticing B) the others need a better model C) the task is unsuitable D) shorter inputs. **Answer: A.** Unstated context is the hidden variable. [source: AMEY practice Q18]
41. A user reports a wrong answer you can't reproduce. A) assume user error B) get the exact prompt, inputs, and configuration C) bigger model for everyone D) add a warning. **Answer: B.** You need the exact conditions before you can diagnose. [source: AMEY mock-exam-2 Q14]
42. Quality is fine but the process takes too long to be worth it. Examine first? A) a faster model B) whether the slow part is the model or the human steps C) a shorter prompt D) abandon the task. **Answer: B.** Find the bottleneck before optimizing. [source: AMEY practice Q35]

### Out-of-scope flavored items (for instructor awareness, not drilling)

EVG includes items on few-shot counts (3–5 in `<example>` tags), Structured Outputs with constrained decoding, the Constitution priority order (broadly safe > broadly ethical > guidelines > helpful), and commercial terms forbidding training on customer content. [source: EVG guide] The official guide excludes API builders, and the Preporato guide says API knowledge "earns nothing". Treat these items as low priority. [source: OFFICIAL; PREP-GH README] [unverified as in scope]

## Common traps and exam-taking tips

### Distractor patterns (consolidated)

| Trap | Why it fails | Sources |
|---|---|---|
| Trust the output (confident, cited, fluent, consistent across runs) | Fluency and consistency are not evidence | OFFICIAL S1; PREP-GH; AMEY |
| Ask Claude to rate or check itself | Not an independent check | OFFICIAL S1; AMEY mock-2 Q2 |
| Strongest model everywhere / "upgrade the model" as the fix | Ignores cost and latency, and doesn't fix format, process, grounding, or governance | OFFICIAL S2; AMEY; PREP-GH; RAY |
| Smallest model for hard work | Under-serves complex cases | AMEY practice Q5 |
| Paste first / upload as-is because it's "internal", "just formatting", or "legal asked" | The policy check comes before productivity | OFFICIAL S3; PREP-GH; AMEY |
| "Tell Claude to ignore, not retain, or keep it confidential" | An instruction is not a control. The data has already left | OFFICIAL S3; AMEY practice Q9, Q21 |
| Abandon the task / do nothing / say no | Wrong when a compliant path exists | OFFICIAL S3; AMEY cheat-sheet |
| Regenerate and hope / retry the identical prompt | Doesn't address the cause | PREP-GH; AMEY practice Q3 |
| Vague intensifiers ("be detailed", "be concise", CAPITALS, "follow all rules") | Add no structure | AMEY practice Q4, Q24, Q26 |
| One giant prompt | Decompose into steps you can check | PREP-GH |
| Rebuild context every session | Recurring context belongs in a Project | PREP-GH |
| Add the new doc alongside the old | Mixed and contradictory answers | AMEY practice Q8; mock-3 Q12 |
| Add a disclaimer | Doesn't make inaccurate content acceptable | AMEY cheat-sheet; mock-1 Q1 |
| "Add a human somewhere" | Review only counts if the reviewer is qualified, sees the evidence, has authority, and acts before the consequential step | RAY exam-strategy |
| Change several things at once / rewrite from scratch | You can't tell what worked. Diagnose the change first | PREP-GH; AMEY |
| Longest or most elaborate option | The exam rewards the option that meets the stated constraint | AMEY cheat-sheet |
| Over-correcting (refuse all AI near the data, ban AI) | A proportionate answer exists | PREP-GH Q2; RAY Q42 |
| Mismatched intensity (right practice, wrong level of urgency) | Review depth should be proportional to stakes | PREP-GUIDE |

### Tips

- Find the constraint in the stem first (cost, privacy, speed, policy, scale, stakes), then eliminate options that ignore it. Two options usually survive. Pick the one that changes the system rather than compensating around it. [source: AMEY cheat-sheet]
- Tie-breaker: choose the option a careful professional would defend to the risk owner. [source: AMEY cheat-sheet]
- RAY's five-element read: Objective, Failure, Constraint, Risk, and Decision layer. Fix the problem at the lowest layer that owns it. [source: https://raw.githubusercontent.com/raybeecham/claude-certified-associate-foundations/main/docs/exam-strategy.md]
- Cue words: [source: PREP-PLAN]
  - "every week / same format" → Project
  - "customer, regulator, executive, legal" → verify plus human review
  - "names, accounts, PII" → anonymize first
  - "last month / current" → research mode
  - "hundreds / routine / fast" → Haiku
- Multiple-response items: [source: PREP-GH; PREP-GUIDE; AMEY cheat-sheet]
  - Read the "select N" line first.
  - Judge each option as an independent true/false.
  - Assume no partial credit. [unverified]
- Pacing: [source: AMEY cheat-sheet; PREP-PLAN]
  - About 2 minutes per item.
  - Flag anything over 90 seconds to 3 minutes.
  - Answer everything, because blanks score zero.
  - Change an answer only with a named reason.
- Closed book: no notes, phones, second monitors, or recording devices. [source: OFFICIAL Section 12] AMEY adds that browser translation tools are not allowed. [source: AMEY README] [unverified: not stated in the official guide]

## Structural ideas worth borrowing

From ARCH (Architect repo):

- Per-task "Key knowledge / Key skills / Anti-patterns" blocks under each official task statement. This maps cleanly onto the 25 CCAO-F objectives. [source: https://raw.githubusercontent.com/paullarionov/claude-certified-architect/main/README.md]
- Questions grouped by scenario (one business context, several questions). Each shows the correct option inline and a short "Why A" that also says why the distractors fail. [source: ARCH guide_en.md]
- A "How to read the questions" section: find the deciding phrase, choose the proportionate first step, separate guidance from guarantees. Run disagreement as an exercise: vote alone, discuss in pairs, then vote again. This fits a live O'Reilly session well. [source: ARCH README]
- Closing appendices: technologies and concepts, an explicit out-of-scope list, and preparation recommendations. [source: ARCH guide_en.md]
- Anki deck and PDF/EPUB builds generated from one markdown source. [source: ARCH README]

From AMEY:

- A one-page cheat sheet: exam facts table, weights bar chart, "If you remember nothing else" (12 rules), a situation → right-instinct table, a pacing plan, and a traps list. [source: https://raw.githubusercontent.com/Amey-Thakur/CLAUDE-CERTIFICATIONS/main/associate-foundations/cheat-sheet.md]
- A D2 decision-tree diagram: does it answer the question → any claim that matters if wrong → does it hold against the source → regulated or high-stakes → adapt for audience → accept. [source: AMEY notes.md]
- 15-question mocks with an answer key table (answer, domain, why) and a readiness band (13–15, 10–12, 7–9, ≤6). [source: AMEY mock-exam-2.md]

From RAY:

- A crosswalk table from official domains to the course order. This is needed because the official prep course order (Platform first) differs from the blueprint numbering. [source: RAY README; PREPPATH]
- A miss-classification taxonomy for post-mock review: Knowledge, Reading, Judgment, Layering, Execution. For each miss, also write "one variation that would make the distractor correct". [source: RAY practice-exams/README.md]
- "Lowest appropriate control layer" table (problem → first control). [source: RAY exam-strategy.md]
- Responsibility table for the capability layer: Project instructions, knowledge, Skill, Code Execution, Memory, external system, human. [source: RAY master-cheat-sheet]

From Preporato:

- Six named traps with memorable labels: Trust-the-output, Strongest-model-everywhere, One-giant-prompt, Paste-first, Regenerate-and-hope, Rebuild-every-session. These make good slide anchors. [source: PREP-GH]
- A symptom → cause → first-fix table for D7, and a "you want to… / put it in…" placement table for D5. [source: PREP-GH]
- A worked hallucination example: a source excerpt next to a summary, with three hallucinations for learners to spot. This works as a live exercise. [source: PREP-GH]
- A pre-exam checklist of "I can…" statements. [source: PREP-GH]

## Decision

Not requested.

## Open questions

- Registration eligibility. AMEY says a partner-company email is required. Preporato says free CPN membership is enough. The official page shows only "apply to become one". Should the course tell learners to check eligibility on Partner Academy before buying?
- Multiple-response share (~25%) and no partial credit come only from Preporato. Present them as unofficial heuristics, or omit them?
- Scope of the capability layer. The official prep list names Memory, Skills, and Code Execution, and RAY and EVG drill Skills trust, Incognito, and Code Execution. Do we have official help-center sources for these product facts? EVG's model list (including "Fable") and its context sizes were not verified here.
- The AI Fluency 4D vocabulary (Delegation, Description, Discernment, Diligence) appears in RAY and in Preporato's course mapping, and AI Fluency is a recommended prerequisite on the official prep path. Should the course teach the 4Ds explicitly as an organizing frame?
