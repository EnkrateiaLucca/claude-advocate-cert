# Lesson 0: The Exam Blueprint

**Exam domain:** all seven (how the exam is built) · **Time in session:** Segment 1, about 10 minutes

## What the exam asks

The official Exam Guide (v1.0, effective July 2026) describes the credential this way:

> "The Claude Certified Associate – Foundations certification validates that an individual can apply Claude to complete business and productivity tasks with minimal guidance. This includes using built-in platform features, capabilities, and tools to streamline workflows; identifying opportunities to improve processes with Claude; selecting approaches that balance quality, efficiency, and cost; and recognizing limitations and escalating more complex or technical work to Claude Architects and Developers."

The guide states five things a credential holder can do:

- Apply Claude to complete structured business tasks with minimal guidance
- Use built-in platform features and tools to streamline workflows
- Identify opportunities to improve processes using Claude
- Select appropriate approaches to balance quality, efficiency, and cost
- Recognize limitations and escalate more complex or technical implementations

Every item on the exam is written against one of 30 objectives spread across seven domains. Lessons 1 to 7 quote each domain's objectives verbatim.

## Key ideas

### The program: four credentials

| Credential | Level | Fee | Who it targets |
|---|---|---|---|
| **Claude Certified Associate – Foundations (CCAO-F)** | Foundations | $99 | Professionals who use Claude as a productivity tool and build Projects |
| Claude Certified Developer – Foundations | Foundations | $125 | Engineers building with the Claude API, Claude Code, and MCP |
| Claude Certified Architect – Foundations | Foundations | $125 | People designing Claude solutions end to end |
| Claude Certified Architect – Professional | Professional | $175 | Advanced architecture expertise |

The Associate sits at the business-user end. The guide says the exam "is not intended for software developers who build against APIs or design agentic systems." Associates escalate that work to Developers and Architects. Many correct answers on this exam depend on knowing where that line sits.

### Logistics at a glance

| Item | Fact |
|---|---|
| Exam code | CCAO-F |
| Items | 60, multiple-choice and multiple-response (each item states how many to pick) |
| Time | 120 minutes, about 2 minutes per item. Plan for about 135 minutes of seat time. |
| Passing score | Scaled 720 on a 100–1,000 scale. A scaled 720 is not the same as 72% raw correct. |
| Score report | Pass/fail, scaled score, and percent-correct by domain |
| Fee | $99 USD per attempt |
| Delivery | Pearson VUE, online proctored or test center |
| Rules | Closed book, English only, no AI tools, no translation tools |
| Validity | 12 months. On-time renewal is a free, non-proctored assessment. A lapsed credential means retaking the full exam. |
| Retakes | Wait 14 days after the first fail, 30 after the second, 90 after the third. Maximum 4 attempts per rolling 12 months. |
| Reschedule or cancel | Do it at least **48 hours** ahead to be safe. (The guide says 24 hours. The FAQ and policies page say 48.) |

**Eligibility.** Registration currently requires a Claude Partner Network company email address. Personal email addresses do not work. If your employer is not a partner, you cannot sit the exam today. The skills in this course still apply to anyone who uses Claude at work.

### The minimally qualified candidate (MQC)

The passing standard was set by experts judging what a minimally qualified candidate should know. The guide describes the MQC as a professional who:

- uses Claude as a core productivity tool in real workflows
- knows prompt structuring, task orchestration, Projects, and Artifacts
- "moves beyond basic question-and-answer usage to process reimagination, task automation, and project development"
- understands where adoption risks exist and aligns usage with responsible-AI practice
- has a practical grasp of hallucinations, context constraints, and data sensitivity

Read every question as this person would. The MQC works independently, uses features on purpose, and knows when to stop and escalate.

### The seven domains and their weights

| # | Domain | Weight | ~Items | Lesson |
|---|---|---|---|---|
| D1 | Prompting and Task Execution | 14% | ~8 | 02 |
| D2 | **Output Evaluation and Validation** | **21%** | ~13 | 03 |
| D3 | Product and Model Selection | 12% | ~7 | 01 |
| D4 | Workflow Integration and Solution Design | 16% | ~10 | 04 |
| D5 | Configuration and Knowledge Management | 12% | ~7 | 05 |
| D6 | Governance, Risk, and Responsible Use | 15% | ~9 | 06 |
| D7 | Troubleshooting and Optimization | 10% | ~6 | 07 |

Item counts are weight × 60, rounded. The guide publishes weights only. Two facts set your study priorities:

- D2 alone is the largest domain. D1 and D2 together are 35% of the exam.
- D2, D4, and D6 together are 52%. Judgment about accuracy, workflow fit, and risk outweighs feature trivia.

### How items are written

The three official sample questions share one shape:

1. A short workplace scenario with a role (associate, project manager).
2. A constraint in the stem (compliance audience, speed and cost, data policy).
3. A question asking for the **most appropriate** action or the choice that **best fits**.
4. Four options. One is proportionate. Three fail in predictable ways.

The correct answer is usually **the proportionate step that lets the work continue safely**. The work goes ahead, and a real control protects it.

### The five distractor patterns

| Pattern | What it looks like | Example from the official samples |
|---|---|---|
| **Blind trust** | Accept output because it sounds confident, cites something, or is "internal" | "Send it as-is, since Claude expressed high confidence." |
| **Fake safeguard** | A step that feels careful but controls nothing | "Ask Claude to rate its own confidence." "Instruct Claude not to retain it." |
| **Irrelevant fix** | A change that does not touch the actual problem | "Reword the summary to sound more formal." "Switch to a different AI platform." |
| **Over-reaction** | Abandon the task, ban the tool, refuse | "Skip the analysis entirely." |
| **Over-engineering** | Top model for everything, escalate everything, build a system for a one-off | "Use the most capable, highest-cost model for every reply." |

Learn these five labels. When you can name the pattern behind a wrong option, you can eliminate it in seconds.

### The core exam logic

Lessons 1 to 7 repeat these rules. They decide most items.

1. Verify specifics against the source. Model confidence is not evidence.
2. Match the model and the feature to the task.
3. Anonymize before upload. An instruction to Claude ("don't retain this") is not a control.
4. Put recurring context in a Project.
5. When something breaks, diagnose what changed before rewriting.
6. Escalate technical integration work to Developers or Architects, and high-stakes judgments to qualified humans.

### A second lens: the AI Fluency 4Ds

Anthropic's AI Fluency course (a recommended prerequisite on the official prep path) teaches four competencies. They map onto the domains.

| 4D | Definition (Academy wording) | Domains it feeds |
|---|---|---|
| **Delegation** | "Deciding what work to do with AI vs. yourself" | D3, D4 |
| **Description** | "Communicating effectively with AI systems" | D1, D5 |
| **Discernment** | "Evaluating AI outputs critically" | D2, D7 |
| **Diligence** | "Ensuring responsible AI collaboration" | D6, D2 |

When a question feels unfamiliar, ask which D it tests. A Discernment question wants verification. A Diligence question wants a control or a disclosure. A Delegation question wants a split of work between people and Claude.

## Exam traps

- **Reading "most appropriate" as "most thorough."** The longest, most elaborate option often over-engineers. Pick the option that meets the stated constraint.
- **Ignoring the constraint in the stem.** Words like "compliance team", "high volume", "policy restricts", or "every week" decide the answer. Underline them mentally.
- **Treating multiple-response items as partial credit.** Anthropic does not publish a partial-credit rule. Treat every multiple-response item as all-or-nothing and judge each option as a separate true/false.
- **Assuming a domain is "easy points."** Each domain's percent-correct shows on your score report, but only the total scaled score decides pass or fail.

## Demo: walk the three official samples

**Goal:** practice the four-step read on the official sample items, then use Claude as a study partner to label distractors.

**Files:** none.

**Steps:**

1. Read Sample 1 aloud (from the Exam Guide, Section 8):

   > An associate asks Claude to summarize a new regulation, and Claude produces a confident summary citing a specific subsection number. Before sending the summary to the compliance team, what is the most appropriate action?
   > A. Send it as-is, since Claude expressed high confidence.
   > B. Verify the cited subsection against the official regulation text before sharing.
   > C. Ask Claude to rate its own confidence and send it if the rating is high.
   > D. Reword the summary to sound more formal, then send it.

2. Find the deciding phrase: "citing a specific subsection" and "compliance team". Specific citations are where fabrication concentrates, and the audience is high stakes.
3. Label each option with a pattern: A is blind trust, C is a fake safeguard, D is an irrelevant fix. B is the proportionate step. **Answer: B.**
4. Repeat for Sample 2 (high-volume customer-reply drafts). A is over-engineering (top model everywhere), C and D are irrelevant fixes. **Answer: B,** a faster, lower-cost model.
5. Repeat for Sample 3 (spreadsheet with customer names and account numbers, policy restricts personal data). A is blind trust, C is a fake safeguard, D is over-reaction. **Answer: B,** remove or anonymize identifiers before uploading.
6. Open claude.ai and start a new chat. Paste this prompt to build your own pattern drill:

```
I'm studying for a certification exam about using Claude at work. Wrong answers on this exam usually fall into five patterns: blind trust, fake safeguard, irrelevant fix, over-reaction, and over-engineering. The right answer is the proportionate step that lets the work continue safely.

Write 3 new multiple-choice scenarios for a marketing manager using Claude. Each has 4 options: 1 proportionate answer and 3 distractors that each follow a different pattern. Don't show the answers. After I reply with my picks and the pattern for each wrong option, grade me and explain any miss in two sentences.
```

7. Answer the three items in the chat and let Claude grade you.

**What to look for:** you can name the pattern behind each wrong option before you pick the right one. If Claude's own scenario has two defensible answers, say so in the chat. Spotting a flawed item is the same skill the exam rewards.

**Debrief:** all three official samples reward the same move. The associate keeps the work going and adds the one control that addresses the real risk. Carry that question into every lesson: "What is the proportionate step here?"

## Use cases to work through

1. **Ops lead deciding whether to sit the exam.** Your company is a Claude partner, and you have a work email on the partner domain. Suggested approach: register on the Partner Academy, schedule through Pearson VUE, and book at least 48 hours of buffer before any change. Use the free renewal to stay current after 12 months.
2. **Consultant whose client is not a partner.** The client's staff cannot register. Suggested approach: use the seven domains as a skills checklist for their Claude rollout. The domain objectives work as a competency framework without the exam.
3. **Teacher with limited study time.** Suggested approach: spend time in proportion to weight. Start with D2 (21%), then D4 (16%) and D6 (15%). Do every sample and practice question while naming the distractor pattern out loud.

## Check yourself

1. A scaled score of 720 means you answered 72% of items correctly. True or false?
2. Which three domains together make up just over half the exam?
3. A question offers "Ask Claude to confirm it has deleted the file" as an option for protecting personal data. Which distractor pattern is it?

<details>
<summary>Answers</summary>

1. False. 720 is a scaled cut score on a 100–1,000 scale. The guide does not publish the raw-to-scaled conversion.
2. D2 Output Evaluation (21%), D4 Workflow Integration (16%), and D6 Governance (15%), for 52%.
3. Fake safeguard. An instruction or a self-report from the model is not a policy control.

</details>

## Official resources

- Exam Guide v1.0 (PDF): https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542847%2FClaude+Certified+Associate+%E2%80%93+Foundations+Exam+Guide.pdf
- Certifications overview: https://anthropic-partners.skilljar.com/page/partner-certifications
- Certifications FAQ: https://anthropic-partners.skilljar.com/page/faq-certifications
- Policies: https://anthropic-partners.skilljar.com/page/policies-certifications
- Official prep path (8 courses): https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations
- AI Fluency: Framework and Foundations: https://academy.claude.com/courses/ai-fluency-framework-foundations
- Pearson VUE for Anthropic: https://www.pearsonvue.com/us/en/anthropic.html

---

**Next:** [Lesson 1: Platform and Model Selection](01-platform-and-model-selection.md)
