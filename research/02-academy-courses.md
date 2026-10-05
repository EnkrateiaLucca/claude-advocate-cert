# Anthropic Academy Courses Mapped to the CCA-F Exam

## Context

The Claude Certified Associate – Foundations exam (code CCAO-F, 60 items, 120 minutes, scaled pass score 720/1,000) tests seven domains. Output Evaluation and Validation carries the most weight at 21% [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542847%2FClaude+Certified+Associate+%E2%80%93+Foundations+Exam+Guide.pdf]. The guide names no required course. It points candidates to official Anthropic documentation for Projects, Artifacts, Memory, Skills, and Code Execution, plus hands-on practice [same source]. This file pulls the exam-testable content out of the free Anthropic Academy courses and tutorials, then fills product gaps with docs.claude.com / platform.claude.com, support.claude.com, and anthropic.com pages. The content is organized by exam domain.

Academy lesson pages are public. The raw HTML of each lesson carries the summary, key takeaways, and exercises. Video transcripts were not in the HTML, so the transcript text was only captured where the page printed it inline.

## Sources reviewed

| Course / resource | Size | Domains it feeds | URL |
|---|---|---|---|
| AI Fluency: Framework and Foundations | 14 lessons, 4 hr, quiz | 1, 2, 4, 6 | https://academy.claude.com/courses/ai-fluency-framework-foundations |
| AI Capabilities and Limitations | 13 lessons, 3.5 hr, quiz | 2, 3, 7 | https://academy.claude.com/courses/ai-capabilities-and-limitations |
| Building Effective Human-Agent Teams (beta) | 5 lessons, 45 min, quiz | 4, 6 | https://academy.claude.com/courses/building-effective-human-agent-teams |
| Claude 101 | 13 lessons, 2.5 hr, quiz | 1, 2, 3, 5, 7 | https://academy.claude.com/courses/claude-101 |
| Introduction to Claude Cowork | 14 lessons, 2.5 hr, quiz | 3, 4, 5, 6 | https://academy.claude.com/courses/introduction-to-claude-cowork |
| Deploying Claude Enterprise with Confidence | 14 lessons, 2.5 hr, quiz | 5, 6 (admin view) | https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence |
| AI Fluency for Small Businesses | 8 lessons | 4, 6 | https://academy.claude.com/courses/ai-fluency-for-small-businesses |
| Introduction to Claude Tag | 11 lessons | 1, 4 | https://academy.claude.com/courses/introduction-to-claude-tag |
| Introduction to Agent Skills | 6 lessons, 1 hr | 5 (developer-leaning) | https://academy.claude.com/courses/introduction-to-agent-skills |
| Claude Code 101 | 12 lessons | 3 (context mgmt only) | https://academy.claude.com/courses/claude-code-101 |
| Academy tutorials (10 used) | 5–20 min each | 2, 3, 6, 7 | https://academy.claude.com/all |

The full Academy catalog has 24 courses. Courses aimed at API builders (Building with the Claude API, Claude Platform 101, MCP, Bedrock, Vertex, subagents) were left out. The guide puts API work and agentic system design outside the Associate audience and assigns it to the Architect and Developer credentials [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542847%2FClaude+Certified+Associate+%E2%80%93+Foundations+Exam+Guide.pdf] [catalog source: https://academy.claude.com/all].

---

## Findings

### Cross-domain frameworks (learn these verbatim)

These three frameworks show up in almost every Academy course. They supply the vocabulary that scenario questions are likely to use.

#### 1. AI Fluency and the three modes of engagement

- **AI Fluency** is "the ability to collaborate with AI in ways that are effective, efficient, ethical, and safe" [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/introduction-to-ai-fluency]. The original Ringling College framework wording is "the ability to work effectively, efficiently, ethically, and safely within emerging modalities of Human-AI interaction" [source: https://ringling.libguides.com/ai/framework].
- The framework was developed by Prof. Rick Dakan (Ringling College of Art and Design) and Prof. Joseph Feller (University College Cork) in 2023–2024, in partnership with Anthropic [source: https://academy.claude.com/courses/ai-fluency-framework-foundations].
- The three ways of engaging with AI [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/the-4d-framework]:
  - **Automation**: "AI executes specific tasks based on your instructions."
  - **Augmentation**: "You and AI collaborate as creative thinking and task execution partners."
  - **Agency**: "You guide AI to work independently on your behalf, shaping its knowledge and behavior rather than specific actions." A configured Project or a custom chatbot fits this mode. Ringling's examples for Agency are "game characters, tutors, chatbots" [source: https://ringling.libguides.com/ai/framework].
- The 4Ds apply across all three modes [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/conclusion].

#### 2. The 4D Framework with its 12 sub-competencies

| D | One-line definition | Sub-competencies (verbatim names) |
|---|---|---|
| **Delegation** | "Deciding what work to do with AI vs. yourself" | **Problem Awareness** (understanding your goals and the work involved), **Platform Awareness** (knowing what different AI systems can do), **Task Delegation** (strategically dividing work between you and AI) |
| **Description** | "Communicating effectively with AI systems" | **Product Description** (what you want: outputs, format, audience, style), **Process Description** (how the AI approaches the request), **Performance Description** (how the AI behaves during the collaboration, e.g., concise vs detailed, challenging vs supportive) |
| **Discernment** | "Evaluating AI outputs critically" | **Product Discernment** (quality of outputs: accuracy, appropriateness, coherence, relevance), **Process Discernment** (how the AI arrived at the output: logical errors, attention gaps, inappropriate reasoning), **Performance Discernment** (how the AI behaved in the collaboration) |
| **Diligence** | "Ensuring responsible AI collaboration" | **Creation Diligence** (thoughtful about which AI systems you use and how), **Transparency Diligence** (honest about AI's role with everyone who needs to know), **Deployment Diligence** (verifying and vouching for outputs you use or share) |

Sources: [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/the-4d-framework] [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-delegation] [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-description] [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-discernment] [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-diligence]

- **Two loops.** The **inner loop** pairs Description and Discernment and "guides your day-to-day AI interactions." The **outer loop** pairs Delegation and Diligence and "guides broader decisions about when and how to use AI" [source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/the-4d-framework]. The Small Business course says "It's a loop, not a line" [source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/closure-and-looking-forward].
- **Description-Discernment loop steps:** Describe, then Discern, then Refine, then Integrate your own expertise and judgment ("Take responsibility for the final output") [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/the-description-discernment-loop].
- **Delegation-Diligence loop:** "decide upfront what's right to hand off — the right task, the right tool, the right data — and afterward you take responsibility for what comes back" [source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/using-data-with-ai].
- The 4D framework defines **24 behaviors**. **11** of them can be observed directly in Claude.ai/Claude Code conversations. The other 13, such as being honest about AI's role, happen outside the chat [source: https://academy.claude.com/tutorials/the-ai-fluency-index].
- **Name variant:** Ringling's framework PDF page (V1.1) names the first Delegation sub-competency "Goal and Task Awareness," where the Academy course says "Problem Awareness" [source: https://ringling.libguides.com/ai/framework]. Teach the Academy name and mention the variant.

#### 3. The four properties of AI (machine side of the 4Ds)

The 4D Framework covers human competencies. The Capabilities and Limitations course covers "the machine properties those competencies respond to" [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/intro-to-ai-capabilities-and-limitations].

| Property | Guiding question | Capability zone | Limitation zone / characteristic failure | Product mitigations | 4D link |
|---|---|---|---|---|---|
| **Next Token Prediction** | "Where do the answers come from?" | Well-worn patterns: summarizing, reformatting, explaining common concepts | Novel/sparse territory. "Fabrication concentrates in specificity: names, dates, statistics, citations, URLs, quotes" | Citations, uncertainty signaling, constrained generation, generator-verifier loops | Foundation of **Discernment** |
| **Knowledge** | "What does it know?" | Frequent, recent-in-training, consistent topics | Rare, post-cutoff, niche, local, contested. Failures: **staleness, uneven coverage, inherited bias, source amnesia** | Web search, retrieval (RAG/MCPs), tool use | Core to **Delegation** |
| **Working Memory** | "What's it paying attention to?" | Material fits, session current, relevant context supplied | Very long docs/conversations, expecting cross-session continuity, critical info buried in the middle. "A cliff rather than a gradient. Silent truncation is the failure mode" | Memory, compaction, projects, larger windows, multi-agent workflows | What **Description** acts on |
| **Steerability** | "How much am I in control?" | "Short, concrete, verifiable instructions. Format specs, length limits, explicit roles" | Long reasoning chains, abstract asks, numerical/logical precision. Failures: **reasoning drift, letter-over-spirit, brittle arithmetic** | System prompts, code execution, visible reasoning, structured outputs | Bounds **Description** |

Sources: [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/what-we-mean-by-ai] [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/next-token-prediction] [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/knowledge] [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/working-memory] [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/steerability]

- Each property is "a continuum. The same mechanism gives you both the capability and the limitation" [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/what-we-mean-by-ai].
- **Calibrated trust** "means locating your task on each continuum and matching your verification and context habits to where it sits" [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/next-steps]. The tutorial version: trust "is a dial you turn, not a switch you flip" [source: https://academy.claude.com/tutorials/can-you-trust-what-ai-tells-you].
- **Training fingerprints.** Pretraining produces "a document completer." Fine-tuning adds assistant behavior using human judgments. Those judgments leave four fingerprints: "a pull toward **sycophancy**, a default toward **verbosity**, occasional **over-caution**, and **loose calibration** between stated confidence and actual reliability" [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/how-ai-gets-its-character].
- **Durability claim.** "The properties stay stable even as models improve. Boundaries shift but the properties remain the same" [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/intro-to-ai-capabilities-and-limitations].

---

### Domain 1: Prompting and Task Execution (14%)

**Guide objectives:** create effective prompts, apply task decomposition, iterate prompts, adapt strategy by task type (analysis, research, drafting, brainstorming).

#### Core concepts

- **Claude 101 three-part prompt structure** [source: https://academy.claude.com/courses/claude-101/your-first-conversation-with-claude]:
  1. **Setting the stage**: your role, objectives, relevant work context.
  2. **Defining the task**: the action (write, analyze, build...).
  3. **Specifying rules**: style, tone, format, examples.
  The course frames this structure as "adapted from the 4D Framework" and "rooted in Description" [source: https://academy.claude.com/courses/claude-101/getting-better-results].
- **Six foundational prompting techniques**, verbatim from AI Fluency Deep Dive 2 [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/effective-prompting-techniques]:
  1. **Give context** ("what you want, why you want it, and relevant background")
  2. **Show examples**
  3. **Specify constraints** (format, length, other output requirements)
  4. **Break complex tasks into steps**
  5. **Ask the AI to think first**
  6. **Define the AI's role or tone**
  - The **"secret weapon"**: "Ask the AI itself to help improve your prompt" [same source].
- **Anthropic docs principles** [source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices]:
  - "Think of Claude as a brilliant but new employee who lacks context on your norms and workflows."
  - **Golden rule:** "Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too."
  - **Explain why.** Context or motivation behind an instruction helps Claude generalize. Example: explain that output will be read by text-to-speech instead of writing "NEVER use ellipses."
  - **Examples (few-shot/multishot)** should be "Relevant," "Diverse," "Structured." Include "3–5 examples for best results."
  - **XML tags** separate instructions, context, examples, inputs.
  - **Role** in the system prompt focuses behavior and tone.
  - **Long context (20k+ tokens):** put longform data at the top and the query at the end. "Queries at the end can improve response quality by up to 30 percent."
  - **Prompt chaining** is still useful "when you need to inspect intermediate outputs." Most common pattern: "self-correction: generate a draft → have Claude review it against criteria → have Claude refine."
- **Before prompt engineering**, have (1) clear success criteria, (2) a way to test against them, (3) a first-draft prompt. "Not every success criteria or failing eval is best solved by prompt engineering", and latency/cost can be fixed by choosing a different model [source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview].
- **Task decomposition.**
  - Delegation planning: list major tasks, then for each ask which parts need human strengths, which suit AI, and where collaboration has the most impact [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/project-planning-and-delegation].
  - Steerability: for 4–5 dependent steps, insert a **checkpoint** ("stop and show you the result of step 2 before continuing"). This counters **reasoning drift** [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/steerability].
  - Research mode decomposes a request on its own: it "breaks a complex request into manageable pieces" [source: https://academy.claude.com/courses/claude-101/research-mode-for-deep-dives].
- **Iteration.**
  - "Your first prompt rarely produces a perfect result." Treat first drafts as starting points, give specific feedback ("Cut the first two paragraphs and make the conclusion more action-oriented" beats "Make it shorter"), know when to start fresh [source: https://academy.claude.com/courses/claude-101/getting-better-results].
  - Tools: follow-up questions, feedback, redirect/restart, and the pencil icon to edit and resubmit a prompt [source: https://academy.claude.com/courses/claude-101/your-first-conversation-with-claude].
  - **AI Fluency Index:** 85.7% of sampled conversations showed iteration and refinement. Iterating conversations showed 2.67 more fluency behaviors (about double the 1.33 baseline). They were 5.6x more likely to question Claude's reasoning and 4x more likely to identify missing context [source: https://academy.claude.com/tutorials/the-ai-fluency-index].
  - "In Chat, the signature move is **iterating**." "In Claude Code and Claude Cowork, the signature move is **clarifying the goal**" [source: https://academy.claude.com/tutorials/getting-good-at-claude-a-research-backed-curriculum].
- **Adapting by task type.**
  - **Brainstorming / thinking out loud:** turn-by-turn Chat, "The answer changes what you ask next" [source: https://academy.claude.com/courses/claude-101/claude-desktop-app-chat-cowork-code].
  - **Research:** use Research mode. Be specific about goals, specify sections/structure, include constraints (budget, timeline, geography), ask Claude to help refine the Research prompt [source: https://academy.claude.com/courses/claude-101/research-mode-for-deep-dives].
  - **Analysis / reasoning without external info:** turn on Thinking [same source].
  - **Delegated multi-step work (Cowork):** a good prompt "Names the deliverable," "Names the inputs," and "Names additional specifics or nuances" [source: https://academy.claude.com/courses/introduction-to-claude-cowork/the-task-loop].
  - **Delegated team work (Claude Tag):** state goal and process, point to inputs, "Build in a way to check Claude's work," say what to prioritize and what form the result takes. For big tasks, ask for a plan outline first. For exploratory work, say so and let Claude propose directions [source: https://academy.claude.com/courses/introduction-to-claude-tag/write-a-request-claude-can-work-with].
- **Set the terms of the collaboration (Performance Description).** Only 30% of conversations tell Claude how to interact. Suggested lines: "Push back if my assumptions are wrong," "Walk me through your reasoning before giving me the answer," "Tell me what you're uncertain about" [source: https://academy.claude.com/tutorials/the-ai-fluency-index].
- **State the goal, not just the format.** "'Convince my team this timeline is realistic' is a goal. 'Three bullet points' is a format" [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/steerability].

#### Concrete examples

- Claude 101 model prompt: "I'm the marketing lead at an indie streaming startup, and we're preparing an investor pitch deck for Series A investors. Can you research the current state of the independent film streaming market... Use current web research with citations and structure it as a professional report of up to 5 pages, with an executive summary, market analysis, competitive landscape, and growth opportunities." [source: https://academy.claude.com/courses/claude-101/your-first-conversation-with-claude]
- Generic vs specific: "Write an email about the project delay" becomes "Write an email to our enterprise client explaining that the software integration will be delayed by two weeks. They've been patient so far but this is the second delay. Keep it professional but apologetic." [source: https://academy.claude.com/courses/claude-101/getting-better-results]
- Cowork nuance line: "I want to see base, best, and worst case scenarios that also account for the 3 new locations we opened in Q3 last year." [source: https://academy.claude.com/courses/introduction-to-claude-cowork/the-task-loop]

#### Traps and misconceptions

- **Trap: "Prompting means finding the magic words."** The course frames Description as more than writing prompts. It means building a collaborative environment, and "AI systems are interactive partners, not databases or vending machines" [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-description].
- **Trap: "Repeat the instruction more forcefully when it's ignored."** "When an instruction is followed literally but uselessly, restate the goal. Repeating the instruction with more force won't close the gap" [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/steerability].
- **Trap: "More context is always better."** "More context ≠ better results. The model's attention is finite. Curate ruthlessly, place strategically, and repeat what matters" [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/try-it-out-q7hdjm9twcbt].
- **Trap: forgetting Process and Performance Description.** Most people only describe the product. The Bad Prompt Makeover exercise drills all three [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-description].

#### Live demo ideas (claude.ai)

- **Bad Prompt Makeover** (5 min): ask Claude for three poorly written prompts, rewrite each with Product/Process/Performance description, then swap roles [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-description].
- **Letter vs spirit:** paste a weak email and ask "Make this more professional." Then re-prompt with the goal stated ("the real problem is it buries the ask") and compare [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/steerability].
- **Reasoning-drift checkpoint:** run a 5-step calculation task end to end, then rerun with "stop after step 2 and show me" [same source].
- **Secret weapon:** paste a vague prompt and ask Claude to interview you and improve it [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/effective-prompting-techniques].

---

### Domain 2: Output Evaluation and Validation (21%, highest weight)

**Guide objectives:** evaluate accuracy and completeness; identify hallucinations, inconsistencies, biases; apply fact-checking; decide when human review is required; edit and adapt outputs for audience; pick output formats (artifacts, inline, structured data).

#### Core concepts

- **Three types of Discernment:** Product, Process, Performance (see the 4D table). "Discernment works hand-in-hand with Description in a continuous feedback loop" [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-discernment].
- **Where fabrication concentrates:** "names, dates, statistics, citations, URLs, quotes. The more precise a claim, the more it warrants verification" [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/next-token-prediction]. This maps directly to exam Sample Q1, where Claude cites a fabricated regulation subsection. The guide's answer is to verify against the official text, because "Self-reported confidence ... is not a reliable accuracy signal" [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542847%2FClaude+Certified+Associate+%E2%80%93+Foundations+Exam+Guide.pdf].
- **Loose confidence calibration** is a trained-in fingerprint: stated confidence does not track reliability [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/how-ai-gets-its-character].
- **Two ways answers go wrong:** hallucination and sycophancy [source: https://academy.claude.com/tutorials/can-you-trust-what-ai-tells-you].
- **Sycophancy test:** open with a wrong premise ("I think this strategy is bulletproof"). Then add "I want you to genuinely disagree with me if you think I'm wrong" and compare [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/how-ai-gets-its-character]. "Agreeable bad premises" is one of the named collision failures [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/when-properties-collide].
- **Bias.**
  - Knowledge failures include "inherited bias in what counts as 'default' or 'normal'" [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/knowledge].
  - Creation Diligence (Ringling wording) covers "Applying ethical principles and identifying bias" [source: https://ringling.libguides.com/ai/framework].
  - Discernment checks output "quality, relevance, bias" [source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/researching-with-ai].
- **Anthropic's documented hallucination-reduction techniques** [source: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations]:
  - Basic: **Allow Claude to say "I don't know"**; **Use direct quotes for factual grounding** (extract word-for-word quotes first for docs >20k tokens); **Verify with citations** (and have Claude retract any claim it can't support with a quote).
  - Advanced: **Chain-of-thought verification**, **Best-of-N verification** (same prompt multiple times; "Inconsistencies across outputs could indicate hallucinations"), **Iterative refinement**, **External knowledge restriction** (only use provided documents).
  - Caveat: these "don't eliminate them entirely. Always validate critical information."
- **Claude 101 fix for confident wrong info:** "For high-stakes work, verify key facts independently. Ask Claude to cite sources or indicate confidence level. Enable web search to ground responses in current information" [source: https://academy.claude.com/courses/claude-101/getting-better-results]. Note: the exam guide rejects *relying* on self-rated confidence, so asking for confidence is a supplement and never a substitute for verification.
- **Research mode citations:** "Every claim in Research reports links back to its source" [source: https://academy.claude.com/courses/claude-101/research-mode-for-deep-dives].
- **Discernment Toolkit (Anthropic Education Report, Sept 2026)** [source: https://academy.claude.com/tutorials/discernment-toolkit]:
  - 51% of interviewed power users verified against **something external** (source documents, official docs, their own data, another person, another AI). A read-through without external validation was the minority practice.
  - The **biggest barrier was lack of domain expertise**, ahead of time pressure.
  - Habits adopted after a missed error: require Claude to **quote its source text first**; put **approval gates at each step** of multi-step tasks; use **multiple agents** (one produces, others check).
  - Five tools: build tests/rubrics for frequent work products; use the discernment-nudge skill; adversarial review (fresh subagent); **build a panel of experts** (people to "phone a friend"); **ask Claude for source grounding** ("If a claim comes from your general knowledge, label it 'unsourced'").
- **Polished-output trap (AI Fluency Index):** in conversations that produced artifacts, users were *less* likely to identify missing context (−5.2pp), check facts (−3.7pp), or question reasoning (−3.1pp) [source: https://academy.claude.com/tutorials/the-ai-fluency-index].
- **Discernment must be taught.** It "doesn't grow with tenure." Observational review (skimming a diff or report) "misses wrong assumptions, missing context, and plausible-but-false claims." "If your training time is limited, Discernment is where to concentrate it" [source: https://academy.claude.com/tutorials/getting-good-at-claude-a-research-backed-curriculum].
- **When human review is required.**
  - Anthropic's Usage Policy lists **high-risk use cases**: legal, healthcare, insurance, finance/lending, employment and housing, academic testing/admissions, media/journalism. These require **human-in-the-loop** ("a qualified professional in that field must review the content or decision") and **disclosure** [source: https://www.anthropic.com/legal/aup].
  - Scrutiny should scale with stakes: "check the result in proportion to what's riding on it: a quick lookup needs only a glance, while analysis that will shape a decision deserves a closer review" [source: https://academy.claude.com/tutorials/choosing-the-right-claude-model].
  - "Even the most advanced AI systems benefit from human judgment and oversight" [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-discernment].
- **Reviewing delegated deliverables (Cowork):** check "Does it meet the actual objective?", "Are the facts accurate?" (ask Claude which docs it pulled from, then check them), "Does anything sound made up?" ("A specific date, name, or quote that you can't trace to an input is a flag, not a feature"). If mostly right, tell Claude what to change instead of starting over [source: https://academy.claude.com/courses/introduction-to-claude-cowork/the-task-loop].
- **Validate before you trust (Rio example).** Take a past analysis where the right answer is known, have AI reproduce it, compare, refine, and retest. "If you can't get there after several refinements, you've learned that this isn't a task you should delegate." "Validation builds confidence, but it doesn't eliminate responsibility" [source: https://academy.claude.com/courses/claude-101/getting-better-results].
- **Simple eval approach:** gather 5–10 examples of a recurring task, create test prompts, compare outputs to your examples, refine [same source].
- **Adapting for audience.**
  - Versatility test: explain one topic for a customer, a business partner, and a new employee in one response [source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/ai-capabilities-and-limits].
  - "Describe the end user" so artifacts get appropriate design choices [source: https://academy.claude.com/courses/claude-101/creating-with-artifacts].
- **Output formats.**
  - **Artifacts** are "outputs you create with Claude: a document, a deck, a design, a dashboard, a prototype," shown in a dedicated window. Claude makes one "when you ask for something that stands on its own — something you'll want to edit, reuse, or share rather than just read once." You can force it: "Create this as an artifact" [source: https://academy.claude.com/courses/claude-101/creating-with-artifacts].
  - **Ask for the deliverable, not just the content:** "Summarize our Q3 results" gets a chat reply. "Turn our Q3 results into a one-page doc for the leadership team" gets an artifact [same source].
  - **Artifacts vs file creation:** file creation "produces downloadable Word documents, Excel spreadsheets, PowerPoint presentations, and PDF files." An artifact "opens and updates right in Claude and is shared by link" [same source].
  - **Inline** chat text suits quick answers. Claude Tag guidance: "A short answer belongs in the thread... If people will open it, revisit it, or pass it on, ask for a page" [source: https://academy.claude.com/courses/introduction-to-claude-tag/write-a-request-claude-can-work-with].
  - **Structured output** (tables, fixed formats) sits in Steerability's capability zone ("respond as a three-column table") [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/steerability].
  - Doc charts pulled from connectors are "a snapshot, not a live feed." Ask Claude to refresh them [source: https://academy.claude.com/courses/claude-101/creating-with-artifacts].

#### Traps and misconceptions

- **Trap: "It cited a source, so it's verified."** Citations make verification *easy*. They do not replace it [source: https://academy.claude.com/courses/claude-101/research-mode-for-deep-dives].
- **Trap: "Ask Claude to rate its confidence."** Exam Sample 1 rationale rejects this [source: exam guide URL above].
- **Trap: "Polished means correct."** See the AI Fluency Index artifact finding [source: https://academy.claude.com/tutorials/the-ai-fluency-index].
- **Trap: "Rewording or formatting fixes accuracy."** Sample 1 option D. "Reformatting ... does not address correctness" [source: exam guide URL above].
- **Trap: "The AI agreed with me, so I'm right."** Sycophancy is a trained-in pull [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/how-ai-gets-its-character].

#### Live demo ideas

- **Verification Test:** in a domain the instructor knows, ask for five checkable specifics (3 sources, an author, a URL) and score them live. Rerun in a fresh chat to show sampling variation, then rerun with Research mode on [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/next-token-prediction].
- **Source-grounding prompt:** "For each factual claim in your answer, tell me where it came from. Quote the exact passage ... If a claim comes from your general knowledge, label it 'unsourced'" [source: https://academy.claude.com/tutorials/discernment-toolkit].
- **Hallucination test for business users:** ask for 2–3 specific trade associations or regulators and spot-check that they exist [source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/ai-capabilities-and-limits].
- **Expert Discernment:** ask for three explanations of one concept in your domain, critique each on Product/Process/Performance, then co-write a better one [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-discernment].
- **Chat reply vs artifact:** send the same content request twice, once as "summarize" and once as "a one-page doc for leadership" [source: https://academy.claude.com/courses/claude-101/creating-with-artifacts].

---

### Domain 3: Product and Model Selection (12%)

**Guide objectives:** select features (Projects, research mode, chat, artifacts); differentiate Haiku/Sonnet/Opus; align models to cost, speed, quality; manage context limits and memory (restart, summarize, persist).

#### Core concepts: features

- **Three shapes of work in the desktop app** [source: https://academy.claude.com/courses/claude-101/claude-desktop-app-chat-cowork-code]:

| You're about to... | Shape | Where it lives |
|---|---|---|
| Ask, brainstorm, draft, think something through turn by turn | Working with Claude, turn by turn | **Chat** |
| Hand off a multi-step task that ends in a finished deliverable, spans your tools, or runs on a schedule | Handing work off | **Cowork** (folder access, connectors, scheduled tasks, subagents) |
| Write, test, run, ship code | Building software | **Code tab** (Local or Cloud) |

- **Chat vs Cowork** [source: https://academy.claude.com/tutorials/choosing-between-claude-cowork-or-chat]:
  - Goal: "Still working it out" (Chat) vs "Clear deliverable in mind" (Cowork).
  - Role: "Present for every turn" vs "Describe it once, check back."
  - Output: "Text you'll read or copy" vs "A finished file or an action taken."
  - Cowork is available to Pro, Max, Team, and Enterprise [source: https://academy.claude.com/courses/claude-101/claude-desktop-app-chat-cowork-code].
- **Research vs web search vs Thinking vs Enterprise Search** [source: https://academy.claude.com/courses/claude-101/research-mode-for-deep-dives]:
  - **Research**: agentic, multi-search, minutes not seconds, sometimes "hundreds of sources," cited report. Use for comprehensive reports, comparative analysis (competitors, vendors), and synthesis across web plus connected Google Workspace. **Web search must be enabled for Research to work.**
  - **Web search**: a quick specific fact, one or two sources, speed over comprehensiveness.
  - **Thinking**: deep reasoning that needs no external info (math, debugging, logic).
  - **Enterprise Search**: internal org knowledge (docs, Slack, email). Team/Enterprise only, admin setup required. It appears as "Ask {Org Name}" and is described as "a pre-built project for your entire organization" [source: https://academy.claude.com/courses/claude-101/enterprise-search].
- **Projects**: for ongoing work with reusable reference materials, consistent response requirements, or team collaboration (details in Domain 5) [source: https://academy.claude.com/courses/claude-101/introduction-to-projects].
- **Artifacts**: standalone deliverables. Claude Design, Slides, and Docs are beta on paid plans. Basic artifacts (dashboards, trackers, flowcharts, code) work "on every plan, including Free." On paid plans artifacts are saved in the Artifacts tab. On Free they stay with the conversation [source: https://academy.claude.com/courses/claude-101/creating-with-artifacts].
- **Other surfaces** [source: https://academy.claude.com/courses/claude-101/other-ways-to-work-with-claude]:
  - **Claude Code**: software development.
  - **Claude Tag**: Slack.
  - **Claude Design**: UI prototypes.
  - **Claude for Microsoft 365**: Excel/PowerPoint/Word/Outlook sidebars.
  - **Claude in Chrome**: browser sidebar on paid plans only. Anthropic recommends it "for low-risk tasks on trusted websites." It asks permission before high-risk actions. Financial services and adult sites are blocked by default.

#### Core concepts: models

- **Exam-guide framing:** Haiku, Sonnet, Opus. Sample 2 answer: use "a faster, lower-cost model suited to straightforward, high-volume tasks," "reserving the most capable model for complex reasoning" [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542847%2FClaude+Certified+Associate+%E2%80%93+Foundations+Exam+Guide.pdf].
- **Academy model tutorial** lists four models, adding **Fable** above Opus [source: https://academy.claude.com/tutorials/choosing-the-right-claude-model]:

| Model | Rate-limit use | Best for (verbatim) |
|---|---|---|
| Haiku | Lightest | "Quick answers, summaries, and simple extraction — anything you want done instantly" |
| Sonnet | Moderate | "Coding, writing, analysis, and multi-step workflows — your versatile default" ("If you're not sure which model to pick, start here.") |
| Opus | Heavy | "Deep research and complex reasoning that genuinely needs sustained thinking" |
| Fable | Heaviest | "Your largest, most critical projects: long, complex tasks Claude works through with fewer check-ins" |

  - Worked mapping: summarizing articles → Haiku; debugging code → Sonnet; analyzing complex research papers → Opus; building a working project from a rough idea → Fable [same source].
  - Escalation rule: try Opus when "you've tested with Sonnet and it struggled," and try Fable when "you've tested with Opus and it struggled" [same source].
  - Biology and security questions are answered with Opus even if Fable is selected [same source].
  - Plan access: "Free includes Haiku and Sonnet; Pro and Max add Opus, Fable, and more headroom" [same source]. The pricing page lists Fable on Pro "via usage credits" [source: https://claude.com/pricing].
- **Current API lineup (platform docs, October 2026)** [source: https://platform.claude.com/docs/en/about-claude/models/overview]:
  - Fable 5.1 ("demanding reasoning and long-horizon agentic work," slower, $10/$50 per MTok)
  - Opus 5.5 ("long-running agentic coding and knowledge work," moderate, $4/$20)
  - Sonnet 5.5 ("best combination of speed and intelligence," fast, $2/$10)
  - Haiku 4.5 ("fastest model with near-frontier intelligence," $1/$5)
  - Context: 1M tokens for Fable/Opus/Sonnet, 200K for Haiku 4.5.
  - The docs tell API users to start with Opus 5.5. The Academy tutorial and Claude 101 tell claude.ai users Sonnet is the default [source: https://academy.claude.com/courses/claude-101/your-first-conversation-with-claude].
- **Effort setting** [source: https://academy.claude.com/tutorials/how-to-select-the-right-effort-setting-for-claude-cowork-and-chat]:
  - Effort "controls how thoroughly Claude works through a task on its own before returning an answer."
  - Model vs effort: "Changing the selected Claude model changes both capability and cost." Effort "changes cost while keeping the model's core capabilities intact."
  - "A frontier model at medium or low effort often outperforms an older model at high or maximum effort."
  - **Cost per task vs cost per token:** a stronger model can cost less per *task* because it needs fewer follow-ups.
  - Signs of **too little effort**: missed instructions, unfinished work. Signs of **too much**: verbosity without quality gain, scope creep, talking itself out of a correct answer.
- **Extended thinking** helps complex analysis but "increases latency and may not be necessary for simple questions." Start with Sonnet and thinking off for straightforward tasks [source: https://academy.claude.com/courses/claude-101/your-first-conversation-with-claude]. Changing the model starts a new chat [same source].

#### Core concepts: context and memory (restart, summarize, persist)

- **Context window size.** Claude 101: "200K+ tokens (about 500 pages of text or more), with up to 1M tokens available on Pro, Max, Team, and Enterprise plans when using supported models" [source: https://academy.claude.com/courses/claude-101/what-is-claude]. Support: 1M, 500K, or 200K depending on model [source: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work].
- **Usage limits vs length limits.** Usage limits "control how much you can interact with Claude over a specific time period." Length limits relate to the context window. Usage is consumed faster by long and complex conversations, model choice, effort level, and features (extended thinking, tools, connectors) [same source].
- **Context is re-sent every turn.** "A short question late in a long conversation may cost more than the same question in a fresh one, and ... starting a new chat can be the cheapest and fastest way to get an answer" [source: https://academy.claude.com/tutorials/parametric-memory-and-context].
- **Parametric memory** (knowledge in the weights) vs **context** (what's in the window) vs **agentic context** (what Claude looks up). "When an LLM produces incorrect information, it's usually a side-effect of missing, incorrect, or low-quality context" [same source].
- **Compaction** (summarize): near the limit, the app has Claude summarize the conversation, and the summary replaces the history. "It is still a summary, and can still occasionally result in lost details" [same source]. In claude.ai, "Claude summarizes earlier messages to continue the conversation seamlessly." This requires code execution to be enabled [source: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work].
- **Written memory** (persist): Claude writes notes and reads them back in later conversations. "Compaction is how Claude can continue a single conversation beyond the context limit. Written memory is how Claude keeps important details in context across multiple conversations." What's worth remembering is project, preferences, and relationships. Ephemeral details (RSVP counts, quotes) should be looked up fresh [source: https://academy.claude.com/tutorials/parametric-memory-and-context].
- **Memory product facts** [source: https://support.claude.com/en/articles/11817273]:
  - On by default for Free/Pro/Max. For Team/Enterprise, owners control it and members opt in.
  - "Each project has its own separate memory space."
  - View/edit/delete under Settings > Memory.
  - **Search and reference chats** (paid plans) uses RAG over past chats.
  - **Incognito chats** (all plans) aren't saved to history and aren't searched later, but still follow org retention policies.
  - Disabling memory at org level "will automatically and permanently delete all memory data for all users."
- **The model doesn't learn from your corrections.** "It only responds to what's currently in context" [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/working-memory].
- **Restart vs compact (Claude Code rule of thumb, generalizable):** `/compact` to continue the same task near the limit. `/clear` to start something new so prior conversation doesn't "introduce bias." Persist cross-session facts in CLAUDE.md [source: https://academy.claude.com/courses/claude-code-101/context-management]. The claude.ai equivalents are a new chat, auto-summarization, and project instructions/knowledge or memory.
- **Lost in the middle.** A 2023 Stanford result is cited: accuracy dropped "more than 30%" when the key fact sat mid-context. Advice: "put your most important instructions at the beginning and end of the context" [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/try-it-out-q7hdjm9twcbt].

#### Traps and misconceptions

- **Trap: "Always use the best model."** Sample 2 option A. It "wastes the cost and latency budget" [source: exam guide URL above].
- **Trap: "To save usage, switch to a smaller model."** Lowering effort on a frontier model is often better, and cost per task matters more than cost per token [source: https://academy.claude.com/tutorials/how-to-select-the-right-effort-setting-for-claude-cowork-and-chat].
- **Trap: "Research mode for every lookup."** Use web search for a quick fact [source: https://academy.claude.com/courses/claude-101/research-mode-for-deep-dives].
- **Trap: "Claude remembers what I taught it last week."** It does only through memory, projects, or instructions. Outside those, a new chat starts blank [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/working-memory].
- **Trap: "Long conversations are free."** Each turn re-sends the whole window [source: https://academy.claude.com/tutorials/parametric-memory-and-context].
- **Trap: "Chat can save into my folders."** Chat hands files back as downloads. Cowork saves into the working folder [source: https://academy.claude.com/courses/claude-101/claude-desktop-app-chat-cowork-code].

#### Live demo ideas

- **Same task, two models:** "Summarize the attached report in five bullet points, then flag the one claim in it you'd most want a second source for." Run on Haiku, then Sonnet. "Compare where the answers differ, not how long they are" [source: https://academy.claude.com/tutorials/choosing-the-right-claude-model].
- **Blank slate:** teach Claude a fact, open a new chat, and show it doesn't know. Then repeat inside a Project with the fact in instructions [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/working-memory].
- **Lost in the middle:** bury an instruction mid-document, ask a dependent question, then move the instruction to the top [same source].
- **Feature triage quiz:** give five tasks (stock price, vendor comparison, logic puzzle, company PTO policy, Monday status roll-up) and have learners pick web search / Research / Thinking / Enterprise Search / Cowork scheduled task [source: https://academy.claude.com/courses/claude-101/research-mode-for-deep-dives].

---

### Domain 4: Workflow Integration and Solution Design (16%)

**Guide objectives:** analyze requirements and use cases; use Claude for research, planning, process optimization; support solution design and iteration; integrate into workflows to augment or redesign; communicate value and limitations to stakeholders.

#### Core concepts

- **Delegation is "should," not just "can."** "Task Delegation means asking 'should AI do this?' not just 'can it?'" Documented FAQs make good candidates. "Complaints and judgment calls stay human" [source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/tying-it-all-together].
- **Three-bucket task audit** (verbatim categories) [same source]:
  - **AI can handle:** "standardized responses, documented information, clear repeatable processes"
  - **AI can assist, human decides:** AI drafts, a human reviews before sending
  - **Human should handle:** "high-stakes decisions, emotionally sensitive situations, or complex judgment"
  - Audit questions: frequency, time per occurrence, standardized vs variable, consequence of imperfection.
- **Build-the-workflow sequence:** Problem Awareness (analyze actual workload) → Task Delegation → rich Description (what the system produces, step-by-step logic, tone/boundaries/behavior rules) → test iteratively with real examples (Discernment) → Diligence ("review outputs before they reach customers, be honest about AI's role, and provide a clear path to a human") [same source].
- **"The goal isn't to automate everything, but to create the most effective human-AI partnership"** [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-delegation].
- **Effective delegation requires both domain expertise and an understanding of AI capabilities** [same source].
- **Augment vs redesign.**
  - Single-player AI is "like putting on a super suit": it speeds up the individual but silos information. Multiplayer AI puts humans and agents in a shared space with shared context [source: https://academy.claude.com/courses/building-effective-human-agent-teams/why-multiplayer-ai-matters].
  - A multiplayer agent has "its own identity and credentials, shared memory, and shared context." A single-player agent "operates as an extension of you" [source: https://academy.claude.com/courses/building-effective-human-agent-teams/how-multiplayer-agents-differ].
- **Four principles of healthy human-agent teams:** "clear roles, a written north star, gradual release, and the right information access" [source: https://academy.claude.com/courses/building-effective-human-agent-teams].
  - "For an agent, if it isn't written down and accessible, it doesn't exist."
  - "Humans always set" the north star.
  - "Grant autonomy in proportion to demonstrated reliability, then expand it deliberately."
  - Higher task-completion rates mean "the cost of misalignment and error is also higher" [source: https://academy.claude.com/courses/building-effective-human-agent-teams/what-a-strong-team-looks-like].
- **Five readiness questions:** open and searchable; clear owners (agents included); right tools for every teammate; a check before a person sees the work (rubric, test, or second agent); a north star everyone can point to [source: https://academy.claude.com/courses/building-effective-human-agent-teams/organizational-checklist].
- **Getting-started checklist:** one space, 3–5 people, one agent; work in public; write the roster; pin the north star; give the agent "one visible job first" (a morning briefing, reviewed by a person for the first few days); build rubric-based checks; extend trust per task type after several successes; turn repeated explanations into written instructions or skills; hold a weekly retro [source: https://academy.claude.com/courses/building-effective-human-agent-teams/practical-ways-to-get-started].
- **Scheduled and recurring work.** Cowork scheduled tasks run remotely "even when your computer is asleep." Tasks needing local files run only while the app is open [source: https://academy.claude.com/courses/claude-101/claude-desktop-app-chat-cowork-code]. Scheduled tasks should **draft for review** until trusted [source: https://academy.claude.com/courses/introduction-to-claude-cowork/permissions-usage-choosing-your-model].
- **Research and planning use cases.** Research suits market and competitive analysis, planning complex projects (offsites, launches), synthesis across email/calendar/docs, and pre-meeting briefings [source: https://academy.claude.com/courses/claude-101/research-mode-for-deep-dives].
- **Use-case gallery by role.** Claude 101 lists project status reports, user-feedback analysis, brand-guideline skills (general); battle cards, deal prep, sales reports (sales); campaign analysis and cross-platform content adaptation (marketing); financial models, investment memos, inherited spreadsheets (finance); onboarding guides (HR); discovery timelines (legal); literature review and statistics verification (research) [source: https://academy.claude.com/courses/claude-101/claude-in-action-use-cases-by-role].
- **Communicating value and limitations to stakeholders.**
  - **AI use policy** with three sections: "What we use AI for," "What stays human," "How we stay accountable." Stress-test it: "If a customer asked 'do you use AI in your business?' — does this policy give you a clear, honest answer?" [source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/human-in-the-loop].
  - "Set cultural norms around productivity early: discuss what happens with the time AI saves" [same source].
  - **Adoption signals** are "diagnostics rather than proofs." Breadth means active members and weekly returners. Depth means chats per member, skills/projects in use, connector use. "The month you turn a diagnostic into a quota, members optimize for the number instead of the work" [source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/adoption-signals].
  - **Rollout objective** has two halves: what success looks like plus the constraint that must hold [source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/five-decisions-and-the-frame].
- **Escalation boundary.** Associates are "not expected to design enterprise-scale AI architectures or integrations." That work escalates to Claude Architects and Developers [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542847%2FClaude+Certified+Associate+%E2%80%93+Foundations+Exam+Guide.pdf]. Building custom MCP servers or agents through the Managed Agents API falls on the developer side of that line [source: https://academy.claude.com/courses/building-effective-human-agent-teams/practical-ways-to-get-started].

#### Traps and misconceptions

- **Trap: "Automate as much as possible."** The guide and courses favor matching approach to task. Judgment calls and emotionally sensitive work stay human [source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/tying-it-all-together].
- **Trap: "Give the agent full autonomy on day one."** Use gradual release and per-task trust expansion [source: https://academy.claude.com/courses/building-effective-human-agent-teams/practical-ways-to-get-started].
- **Trap: "Usage numbers prove ROI."** Adoption metrics are leading indicators. Pair them with work outcomes [source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/adoption-signals].
- **Trap: "Skip the AI-assisted analysis entirely when data is sensitive."** Exam Sample 3 option D is wrong. Anonymize and proceed [source: exam guide URL above].

#### Live demo ideas

- **Delegation plan conversation:** "Hi Claude, I'm preparing how to [task] and want to discuss with you what a delegation plan may look like..." Have a real back-and-forth [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-delegation].
- **Three-bucket sort:** learners list 5–10 repetitive tasks and have Claude challenge their bucket assignments [source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/tying-it-all-together].
- **Draft your roster:** use the course prompt to propose a human-agent roster that keeps judgment calls with people [source: https://academy.claude.com/courses/building-effective-human-agent-teams/what-a-strong-team-looks-like].
- **One-page AI use policy** built live from the three-section template [source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/human-in-the-loop].

---

### Domain 5: Configuration and Knowledge Management (12%)

**Guide objectives:** configure Projects with instructions and knowledge; manage uploaded knowledge and connectors (Google Drive, Gmail); create effective system-level instructions; maintain and update configurations.

#### Core concepts: Projects

- **Definition.** "Self-contained workspaces with their own memory, chat histories, knowledge bases, and customized instructions" [source: https://academy.claude.com/courses/claude-101/introduction-to-projects].
- **When to use:** reference materials you'll reuse, consistent response requirements, team collaboration needs [same source].
- **Setup steps:**
  1. Name, plus a **description that Claude doesn't see** ("While Claude doesn't see this description directly, it helps you and your teammates").
  2. Visibility.
  3. Instructions.
  4. Knowledge files (PDF, DOCX, CSV, TXT, HTML; or Google Drive) [same source].
- **Good project instructions include** context about the work, process instructions, tone/style preferences, specific requirements (e.g., "Always include a call-to-action"). Instructions can automate workflows: "When I upload a meeting transcript, create a structured summary using this template." They "work alongside any user preferences and styles you've set" [same source].
- **Context isolation.** "Context is not shared across disparate chats within a project unless the information is added into the project knowledge base." A file uploaded inside a chat "stays separate from your project knowledge" [same source].
- **RAG scaling.** When knowledge approaches the context limit, Claude "searches your project's files, retrieving only what's relevant," which expands capacity "by up to 10x." A visual indicator shows when RAG is on [same source]. RAG expansion requires paid plans. Free users get up to five projects [source: https://support.claude.com/en/articles/9517075-what-are-projects].
- **Best practices** [source: https://academy.claude.com/courses/claude-101/introduction-to-projects]:
  - Start focused, then expand.
  - **Keep your knowledge base current** ("Outdated documents can lead to outdated responses").
  - Write clear instructions.
  - **Name documents descriptively** ("Q4-2025-Sales-Report.pdf" not "report.pdf"; "Claude uses filenames and proximity to understand relationships").
  - **Reference documents by name** in questions.
- **Sharing (Team/Enterprise).** Permission levels are **Can view** (see contents, use knowledge, chat; no changes), **Can edit** (modify instructions and knowledge, manage members), and **Owner** (controls everything, including org-wide visibility) [same source]. Admins can disable project sharing org-wide [source: https://support.claude.com/en/articles/9517075-what-are-projects].
- **Cowork projects** add scheduled tasks, working folders/links as context, and **memory Claude builds automatically**. "Outside of a project, each session starts fresh apart from your global instructions" [source: https://academy.claude.com/courses/introduction-to-claude-cowork/giving-cowork-context].

#### Core concepts: instruction layers (system-level instructions)

| Layer | Scope | Who sets it | Source |
|---|---|---|---|
| Organization instructions | Every member's conversations on supporting surfaces | Admin (Enterprise) | https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/governing-customizations |
| Global instructions / "Instructions for Claude" (Settings) | Every chat and scheduled task for you | You | https://academy.claude.com/courses/introduction-to-claude-cowork/giving-cowork-context ; https://academy.claude.com/courses/claude-101/your-first-conversation-with-claude |
| Project instructions | Every chat in that project | Project owner/editors | https://academy.claude.com/courses/claude-101/introduction-to-projects |
| Skills | Loaded only when a task calls for it | You / org | https://academy.claude.com/courses/claude-101/working-with-skills |
| Memory | Auto-saved context, per project or global | Claude (user can edit) | https://support.claude.com/en/articles/11817273 |

- **What to put in global instructions:** who you are and what you do, your shorthand and acronyms, how you want output delivered (format, length, tone). **Corrections you keep repeating** ("share the bottom line up front," "don't use Oxford commas") are global-instruction candidates [source: https://academy.claude.com/courses/introduction-to-claude-cowork/giving-cowork-context].
- **Org instructions example (Pluto):** "You are assisting Pluto, a fintech with five business units... Customer-facing writing is plain and short, in Pluto's house style." Org instructions are "soft steering ... not a hard limit" [source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/governing-customizations] [source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/managing-spend].
- **"Keep your project instructions concise"** is listed as a usage-saving tip [source: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work].

#### Core concepts: Skills

- **Definition.** "Folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks" [source: https://academy.claude.com/courses/claude-101/working-with-skills].
- **Types.** Anthropic Skills cover Excel/Word/PowerPoint/PDF creation and are invoked automatically. Custom Skills are your own [same source].
- **Requirements.** Skills are available on all plans but need **Code execution and file creation** enabled (Settings > Capabilities). On Enterprise, Owners must first enable Code execution and Skills [same source].
- **Create one by conversation.** Tell Claude what you want, answer its interview questions, upload references, save. Manage skills in the **Customize** tab [same source].
- **"Projects store knowledge, skills perform tasks."** The project provides the *what*, the skill provides the *how*. They can combine, e.g., a call-prep skill that pulls customer profiles from project knowledge [same source].
- **Security.** "Only install custom Skills from trusted sources." Custom Skills you upload are private to your account [same source].
- **Plugins** bundle skills, connectors, and sub-agents. "A plugin can't give a member a connector or capability their groups don't include" [source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/governing-customizations].
- **Skills load on demand.** Unlike CLAUDE.md, which loads into every conversation, skills activate when Claude matches the request to the skill's **description** [source: https://academy.claude.com/courses/introduction-to-agent-skills/what-are-skills].
- **Write a skill when:** "If you find yourself explaining the same thing to Claude repeatedly, that's a skill waiting to be written" [same source].

#### Core concepts: Connectors

- **What they are.** Connectors "allow Claude to read information and perform actions on your behalf." They are powered by **MCP** ("like USB-C for AI"). The two types are **web connectors** (cloud services) and **desktop extensions** (local, via the Desktop app). The directory is at claude.ai/directory [source: https://academy.claude.com/courses/claude-101/connecting-your-tools].
- **Setup flow:** find, Connect, authenticate, review and grant permissions, test ("Can you access my [tool name]?") [same source].
- **Security model** [same source]:
  - **Scoped access**, with per-permission toggles.
  - **"Claude sees what you see"**: connecting work email doesn't expose the CEO's inbox.
  - **Revocable at any time.**
  - Install only trusted custom connectors.
- **Google Workspace specifics** [source: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors]:
  - Gmail, Calendar, and Drive connectors are available to all users.
  - Gmail send/reply/forward and Drive share/move/trash ask for approval before each action by default.
  - **The Drive connector works only in private projects, not shared projects.**
  - Google Docs added to chats and projects **sync** to the latest version. Images embedded in documents are not processed.
  - On Team/Enterprise, an Owner or Primary Owner must enable the connectors before users can authenticate.
- **Three gates (Enterprise).** Organization gate, role gate, and member gate (the member connects their own account). Access depth is read-only vs read-write, with write and delete tools set to Always allow, Needs approval, or Blocked. "Claude inherits the member's own permissions from the connected service." The common pattern is **read-only first, write later with risk-owner sign-off** [source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/connectors].

#### Maintaining configurations

- Keep knowledge current [source: https://academy.claude.com/courses/claude-101/introduction-to-projects].
- Iterate on skills by asking Claude to edit them [source: https://academy.claude.com/courses/claude-101/working-with-skills].
- Validate skills with **evals**. Skill-creator produces paired outputs (with skill vs without skill). Give specific feedback. **Change one thing at a time.** The bar for shipping: "the cases you care about pass meaningfully better than the baseline" [source: https://academy.claude.com/courses/introduction-to-claude-cowork/validating-skills-for-plugins].
- Shared plugin hygiene: **one owner**, evals before every publish, specific names ("sales-customer-renewal-prep" not "meeting-prep"), a **quarterly review rhythm** to retire stale items. Distribution modes are **Available**, **Installed by default**, and **Required** [source: https://academy.claude.com/courses/introduction-to-claude-cowork/share-what-you-build-with-your-team].
- Org governance postures: **Open build, reviewed spread** / **Centralized** / **Fully open** [source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/governing-customizations].

#### Traps and misconceptions

- **Trap: "The project description guides Claude."** Claude doesn't see it. Instructions do the guiding [source: https://academy.claude.com/courses/claude-101/introduction-to-projects].
- **Trap: "A file uploaded in one project chat is available to other chats in the project."** Only files in project knowledge are shared [same source].
- **Trap: "Use a Skill to store reference documents."** Projects store knowledge. Skills encode procedures [source: https://academy.claude.com/courses/claude-101/working-with-skills].
- **Trap: "Connectors give Claude broader access than I have."** Claude sees what you see [source: https://academy.claude.com/courses/claude-101/connecting-your-tools].
- **Trap: "Add the Drive connector to a shared team project."** It's disabled for shared projects [source: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors].
- **Trap: "Skills don't work."** Check whether Code execution and file creation is off [source: https://academy.claude.com/courses/claude-101/working-with-skills].

#### Live demo ideas

- Build a **"Client account hub"** project live: instructions (tone, CTA rule, transcript-to-summary automation), two descriptively named knowledge files, then one chat that references a file by name [source: https://academy.claude.com/courses/claude-101/introduction-to-projects].
- Show **context isolation:** upload a file in chat A of the project and ask about it in chat B [same source].
- **Create a skill by conversation** ("I need a skill that applies our brand guidelines to presentations"), then trigger it with a natural request [source: https://academy.claude.com/courses/claude-101/working-with-skills].
- **Connector test:** connect Google Drive and ask "Can you access my Google Drive?", then show the Gmail send-approval prompt [source: https://academy.claude.com/courses/claude-101/connecting-your-tools] [source: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors].

---

### Domain 6: Governance, Risk, and Responsible Use (15%)

**Guide objectives:** identify appropriate and inappropriate use cases; apply data sensitivity, regulatory, privacy considerations; follow org AI policies; understand ethical implications.

#### Core concepts

- **Diligence's three parts:** Creation, Transparency, Deployment (see the 4D table). "Different contexts (personal, academic, professional) may have different expectations for disclosure and verification" [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-diligence].
- **AI diligence statement.** "A transparent acknowledgment of AI's role in your work, paired with your commitment to taking responsibility for the final output," described as the "methods section" for AI collaboration [source: https://academy.claude.com/tutorials/writing-an-ai-diligence-statement]. **Five elements:**
  1. What AI assisted with
  2. Which AI tool you used
  3. What you reviewed and your general involvement
  4. What you changed
  5. Who is responsible
  Also: verify the statement itself, avoid generic copy-paste, and know that vague or absent disclosure "is what erodes trust" [same source].
- **Data hygiene (Delegation-Diligence loop)** [source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/using-data-with-ai]:
  - "Some tools use your inputs to train future models."
  - "Match the tool to the task — higher sensitivity data needs stricter privacy settings."
  - "Strip what isn't needed — remove identifying details" ("replace names with 'Customer A / Vendor X'").
  - "If something goes wrong, act fast — delete the conversation and request data deletion."
  This matches **exam Sample 3**: remove or anonymize identifiers before uploading. "Instructing the model not to retain data ... does not satisfy the policy control" [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542847%2FClaude+Certified+Associate+%E2%80%93+Foundations+Exam+Guide.pdf].
- **Consumer vs commercial data terms** [source: https://code.claude.com/docs/en/data-usage] [source: https://www.anthropic.com/news/updates-to-our-consumer-terms]:
  - **Free, Pro, Max (consumer):** the user chooses whether data may train future models. **Opted in: 5-year retention. Opted out: 30-day retention.** Deleted conversations are not used for future training. The setting can be changed any time in Privacy Settings.
  - **Team, Enterprise, API, Gov, Education (commercial):** not covered by the consumer change. Anthropic does not train on this data unless the customer opts in (e.g., Development Partner Program). Standard API/commercial retention is 30 days (Claude Code doc).
  - Team plans: "No model training on your content by default" [source: https://claude.com/pricing].
- **Enterprise controls a candidate should recognize** (admin-owned, so Associates *follow* them):
  - **Custom data retention** has a 30-day minimum and no zero option. Default retention is indefinite until deleted [source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/visibility-what-you-can-measure].
  - **Compliance API** records content. **Audit logs** are metadata-only [same source].
  - **Inference hooks** can block prompts before they reach Claude [same source].
  - **SSO, SCIM, role-based permissions**: permissions are the **union** of a member's groups, so a narrower group can't remove a broader grant [source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/your-groups].
  - **Domain claiming** is irreversible [source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/prerequisites].
- **Usage Policy (effective Sept 15, 2025)** [source: https://www.anthropic.com/legal/aup]:
  - 14 Universal Usage Standards (e.g., "Do Not Compromise Privacy or Identity Rights," "Do Not Create or Spread Misinformation," "Do Not Engage in Fraudulent, Abusive, or Predatory Practices").
  - **High-risk use cases** (legal, healthcare, insurance, finance, employment/housing, academic testing/admissions, media/journalism) require **human-in-the-loop** review by a qualified professional and **disclosure** of AI involvement.
  - **Consumer-facing chatbots** must disclose that users are talking to AI.
- **Responsible-AI basis of Claude.**
  - Claude 101 says Claude is trained with **Constitutional AI** to avoid toxic or discriminatory outputs and to avoid helping with illegal or unethical activity [source: https://academy.claude.com/courses/claude-101/what-is-claude].
  - The 2022 CAI paper defines it as "training a harmless AI assistant through self-improvement, without any human labels identifying harmful outputs," using "a list of rules or principles." It has two phases: supervised self-critique and revision, then **RL from AI Feedback (RLAIF)** [source: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback].
  - **Claude's constitution** priority order: **Broadly Safe, Broadly Ethical, Compliant with Anthropic's Guidelines, Genuinely Helpful** ("holistic rather than strict" prioritization) [source: https://www.anthropic.com/constitution].
  - Claude 101 summary: Claude is "built to be helpful, harmless, and honest" [source: https://academy.claude.com/courses/claude-101/what-s-next].
- **Agentic safety (Cowork)** [source: https://academy.claude.com/courses/introduction-to-claude-cowork/permissions-usage-choosing-your-model]:
  - Use a **dedicated working folder** instead of Documents or Desktop.
  - **Back up irreplaceable files.**
  - **Test new workflows on copies.**
  - Be explicit with destructive verbs ("Remove the section from the draft, but keep the file").
  - Name bounds ("Don't message anyone — draft only").
  - Read the plan, watch for scope creep, and approve confirmations deliberately ("Most mistakes ... happen because someone clicked through a confirmation").
  - **When Cowork isn't the right tool:** regulated workflows needing an audit trail; "Anything you wouldn't trust a smart, quick colleague to do unsupervised" ("Claude can prepare; you ship"); highly sensitive personal data outside IT-approved boundaries.
- **Human in the loop and dependency** [source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/human-in-the-loop]:
  - Being the human in the loop "means more than oversight — you decide what problems AI should solve."
  - Avoid dependency "through understanding, not avoidance: can you explain what the AI is doing?"
  - AI should free you for more human work.
- **Disclosure culture.** "Avoid policies that treat AI use as inherently suspect ... If your culture penalizes honesty, you won't get responsibility either" [source: https://academy.claude.com/tutorials/writing-an-ai-diligence-statement].
- **Sensitive work in team channels.** "Sensitive work belongs in a private channel" [source: https://academy.claude.com/courses/introduction-to-claude-tag/write-a-request-claude-can-work-with].

#### Traps and misconceptions

- **Trap: "Tell Claude not to retain the data."** That isn't a policy control (Sample 3) [source: exam guide URL above].
- **Trap: "Internal use means no privacy concern."** Sample 3 option A violates policy [same source].
- **Trap: "Incognito means nothing is retained anywhere."** Incognito chats stay subject to org retention policies [source: https://support.claude.com/en/articles/11817273].
- **Trap: "Paid consumer plans (Pro/Max) never train on data."** Pro and Max are consumer plans and follow the same opt-in choice as Free [source: https://code.claude.com/docs/en/data-usage].
- **Trap: "Disclosure makes my work look less credible."** The tutorial argues the opposite [source: https://academy.claude.com/tutorials/writing-an-ai-diligence-statement].
- **Trap: "Diligence is just disclosure."** It is three parts: Creation, Transparency, Deployment [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-diligence].

#### Live demo ideas

- **Anonymize before upload:** take a fake customer CSV and have Claude produce a redaction plan *before* real data is shared (the redaction itself happens outside Claude). Then analyze the redacted copy [source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/using-data-with-ai].
- **Draft a diligence statement** for the session's deliverable using the five elements, then verify that every claim in the statement is true [source: https://academy.claude.com/tutorials/writing-an-ai-diligence-statement].
- **Settings tour:** Privacy (model-improvement toggle), Memory (view/edit/delete, Search and reference chats), Incognito ghost icon [source: https://support.claude.com/en/articles/11817273].
- **High-risk triage:** show 6 use cases and have learners flag which need qualified human review per the AUP [source: https://www.anthropic.com/legal/aup].

---

### Domain 7: Troubleshooting and Optimization (10%)

**Guide objectives:** diagnose and resolve underperforming prompts or poor outputs; adjust based on feedback; optimize workflows.

#### Core concepts

- **Claude 101 common-challenges table** (symptom → cause → fix) [source: https://academy.claude.com/courses/claude-101/getting-better-results]:
  - **Too generic** → not enough context → add audience, role, constraints.
  - **Too long/short** → Claude guessing length → be explicit ("under 100 words").
  - **Didn't follow format** → understood *what* but not *how* → "Show, don't just tell" with an example or explicit structure.
  - **Confident but wrong** → plausible fabrication on specifics/niche → verify, ask for sources, enable web search.
  - **Wrong tone** → default helpful-professional → describe the tone plainly and give a style example.
- **Property-pair diagnostic.** "Real-world failures are usually two properties interacting." The method: name the property, place the task on its spectrum, apply a targeted fix "instead of just trying again" [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/when-properties-collide] [source: https://academy.claude.com/courses/ai-capabilities-and-limitations]:
  - Next Token Prediction + Knowledge → **hallucinated specifics** → verify specifics, add retrieval or search.
  - Working Memory + Steerability → **long-conversation drift** → re-supply context or start fresh.
  - Confidently wrong math → **offload to code execution**.
  - Agreeable bad premises → **invite pushback**.
- **Effort tuning.** Too little effort shows as missed instructions or unfinished work, so raise it. Too much shows as verbosity, scope creep, or overthinking, so lower it. Right-sized effort finishes "in one or a few turns" [source: https://academy.claude.com/tutorials/how-to-select-the-right-effort-setting-for-claude-cowork-and-chat].
- **Usage optimization:** start fresh conversations, use Projects (RAG), disable unused tools and connectors, keep project instructions concise, lower effort for routine work, turn off extended thinking when not needed [source: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work]. A skill loads only when needed, so it is "less token-intensive than re-sharing the prompt every time" [source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/managing-spend].
- **Cowork course-correction.** Steer mid-task instead of waiting and regenerating ("Resist that... the cost of a redirect is low"). If a draft is wrong "in a load-bearing way, the prompt was missing the load-bearing piece of context" [source: https://academy.claude.com/courses/introduction-to-claude-cowork/the-task-loop].
- **Claude Tag troubleshooting.** If Claude looked in the wrong place, move the task or ask an admin for access. If the work is incomplete, ask which sources it searched. If the request was unclear, rewrite it with what, form, priority, and where. If Claude missed a team pattern, save it to memory [source: https://academy.claude.com/courses/introduction-to-claude-tag/write-a-request-claude-can-work-with].
- **Recurring corrections → persistent config.** Repeated corrections become global instructions [source: https://academy.claude.com/courses/introduction-to-claude-cowork/giving-cowork-context]. Repeated explanations become skills [source: https://academy.claude.com/courses/building-effective-human-agent-teams/practical-ways-to-get-started].
- **Workflow evals.** Change one thing at a time and rerun the same prompts [source: https://academy.claude.com/courses/introduction-to-claude-cowork/validating-skills-for-plugins].
- **Personal prompt and pattern library:** 5–10 recurring tasks with template prompts and placeholders [source: https://academy.claude.com/courses/ai-fluency-framework-foundations/additional-activities].
- **Know when to start fresh.** "If a conversation has gone off track, sometimes it's faster to open a new chat with a clearer prompt than to try to redirect" [source: https://academy.claude.com/courses/claude-101/getting-better-results].
- **Enterprise-level optimization (Pluto example).** When spend climbed, the review found the most capable model doing routine summaries. Lowering the role's default model fixed it without raising the cap [source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/managing-spend].

#### Traps and misconceptions

- **Trap: "Just regenerate until it works."** The diagnostic approach says to name the failing property and apply a targeted fix [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/when-properties-collide].
- **Trap: "Bigger model fixes every bad output."** Many failures are context or description gaps. Fix the prompt or context first [source: https://academy.claude.com/tutorials/parametric-memory-and-context].
- **Trap: "Correcting Claude once fixes it forever."** Corrections persist only through instructions, memory, or skills [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/working-memory].

#### Live demo ideas

- **Failure Diagnosis:** learners describe a recent disappointing output, Claude names the property pair, learners push back if Claude simply agrees, then test the targeted fix [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/when-properties-collide].
- **Five-symptom clinic:** produce each Claude 101 failure on purpose and fix it live [source: https://academy.claude.com/courses/claude-101/getting-better-results].
- **Verbosity test:** ask a one-sentence question, then re-ask with "Answer in one sentence" [source: https://academy.claude.com/courses/ai-capabilities-and-limitations/how-ai-gets-its-character].

---

## Comparison

### Which feature for which job

| Need | Use | Not | Source |
|---|---|---|---|
| Quick current fact | Web search | Research | https://academy.claude.com/courses/claude-101/research-mode-for-deep-dives |
| Multi-source cited report | Research (web search on) | Plain chat | same |
| Hard reasoning, no external info | Thinking / higher effort | Research | same |
| Internal company knowledge | Enterprise Search ("Ask {Org}") | Public web Research | https://academy.claude.com/courses/claude-101/enterprise-search |
| Reusable reference context for a workstream | Project (knowledge + instructions) | Re-uploading each chat | https://academy.claude.com/courses/claude-101/introduction-to-projects |
| Repeatable procedure applied automatically | Skill | Project | https://academy.claude.com/courses/claude-101/working-with-skills |
| Standalone deliverable to edit and share | Artifact | Inline text | https://academy.claude.com/courses/claude-101/creating-with-artifacts |
| Downloadable .docx/.xlsx/.pptx/.pdf | File creation (Skills) | Artifact link | same |
| Multi-step hand-off, files in a folder, schedule | Cowork | Chat | https://academy.claude.com/tutorials/choosing-between-claude-cowork-or-chat |
| Live data from your tools | Connectors (MCP) | Copy-paste | https://academy.claude.com/courses/claude-101/connecting-your-tools |
| Standing personal preferences | Global instructions / memory | Repeating in every prompt | https://academy.claude.com/courses/introduction-to-claude-cowork/giving-cowork-context |

### Restart vs summarize vs persist

| Situation | Action | Source |
|---|---|---|
| Conversation drifted or is off track | Start a new chat with a clearer prompt | https://academy.claude.com/courses/claude-101/getting-better-results |
| Same task, nearing context limit | Let it auto-summarize/compact (accept some loss of detail) | https://academy.claude.com/tutorials/parametric-memory-and-context |
| New, unrelated task | Fresh chat (avoids bias from prior context and re-sent tokens) | https://academy.claude.com/courses/claude-code-101/context-management |
| Facts needed across sessions | Project knowledge/instructions, memory, or global instructions | https://academy.claude.com/tutorials/parametric-memory-and-context |
| Sensitive one-off | Incognito chat | https://support.claude.com/en/articles/11817273 |

## Version and consistency notes (for instructor)

- **Model names.** The exam guide covers Haiku, Sonnet, Opus only. The Academy tutorial adds Fable and names "Sonnet 5," "Opus 5," "Fable 5.1," "Haiku 4.5." Platform docs list Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 4.5 [source: https://academy.claude.com/tutorials/choosing-the-right-claude-model] [source: https://platform.claude.com/docs/en/about-claude/models/overview]. Teach tiers and trade-offs, not version numbers.
- **"Default" model.** claude.ai materials call Sonnet the recommended default [source: https://academy.claude.com/courses/claude-101/your-first-conversation-with-claude]. API docs tell developers to start with Opus 5.5 [source: https://platform.claude.com/docs/en/about-claude/models/overview]. For an Associate exam, the claude.ai framing is the likely reference [unverified].
- **Styles.** The Claude 101 video notes "The 'Use style' menu it shows has since been deprecated" [source: https://academy.claude.com/courses/claude-101/your-first-conversation-with-claude]. Avoid teaching Styles as a current feature.
- **Problem Awareness vs Goal and Task Awareness.** See the cross-domain notes [source: https://ringling.libguides.com/ai/framework].
- **AI Fluency Index indicator list.** The 11 observable behaviors and their prevalence were seen only in a translated secondary summary (iteration 85.7%, clarify goals 51.1%, examples 41.1%, format 30%, interaction style 30%, tone 22.7%, missing context 20.3%, audience 17.6%, question reasoning 15.8%, consult on approach 10.1%, verify facts 8.7%) [unverified]. The Academy page shows the chart only as an image. The 85.7% iteration figure and the 30% interaction-style figure are verified in the Academy text [source: https://academy.claude.com/tutorials/the-ai-fluency-index].

## Failed or partial fetches

- `https://www-cdn.anthropic.com/7e9692bba414a91a562af2a64b7e99d7946de590.pdf` ("About this course" PDF): WebFetch returned unparsed binary. The course page text covered the same content.
- `https://www.anthropic.com/news/anthropic-education-report-the-ai-fluency-index`: 404. The research URL redirects to the Academy tutorial, which was used instead.
- `https://academy.claude.com/tutorials/the-4-ds-of-ai-fluency-behavioral-indicators`: the page body (the 24-behavior list) is not in static HTML.
- Video transcripts for Academy lessons: not in static HTML. Only summaries and takeaways were captured.

## Open questions

- Should the course teach Fable as a fourth tier? The exam guide lists three model families only.
- The guide names "Code Execution" as a study topic. Academy coverage reaches it only through the Skills and file-creation prerequisite and the "offload math to code execution" fix. A dedicated support-doc pass on code execution and file creation may be worth adding.
- The Enterprise Deployment course is admin-level (Owner role). Use it as background only, or include admin concepts (retention, union rule, three connector gates) as exam-relevant? The guide's MQC "follow[s] organizational AI policies" and does not set them.
