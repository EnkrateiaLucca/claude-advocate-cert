# Lesson 2: Prompting and Task Execution

**Exam domain:** D1 Prompting and Task Execution (14%) · **Time in session:** Segment 2, about 15 minutes

## What the exam asks

Verbatim objectives from the Exam Guide:

- Create effective prompts for business and technical tasks
- Apply task decomposition techniques to structure complex requests
- Iterate prompts to improve output quality
- Adapt prompting strategies based on task type (analysis, research, drafting, brainstorming)

In 4D terms, this domain is **Description**: communicating clearly enough that Claude can do the work the way you need it done.

## Key ideas

### The mental model

Anthropic's prompting guide says to treat Claude as "a brilliant but new employee who lacks context on your norms and workflows." Its golden rule: show your prompt to a colleague with minimal context on the task. If they would be confused, Claude will be too.

Exam questions about weak output usually describe a prompt that a new colleague could not act on. The fix is almost always more specific context, constraints, or structure.

### Prompt anatomy

| Part | What it answers | Weak | Strong |
|---|---|---|---|
| **Role** | Who should Claude act as? | (none) | "You are an operations analyst." |
| **Context** | Why does this matter, who reads it, what background applies? | (none) | "Our VP reads this on mobile before Monday's meeting." |
| **Task** | What exact action? | "Look at this." | "List every action item with owner and due date." |
| **Inputs** | What material should Claude use? | Implied | "Use only the attached notes." |
| **Constraints** | Length, tone, scope, what to avoid | "Be concise." | "Under 120 words. No jargon." |
| **Output format** | What shape should the answer take? | "Make it organized." | "A table with columns: Item, Owner, Due, Status." |
| **Examples** | What does good look like? | (none) | One filled-in example row or paragraph |

Add a line about **how to collaborate** when it matters. Anthropic's AI Fluency research found that only about 30% of conversations tell Claude how to interact. Useful lines:

- "If something isn't in the notes, write 'not stated'. Do not guess."
- "Push back if my assumptions are wrong."
- "Tell me what you're uncertain about."

Four principles show up repeatedly in exam answers:

- **Concrete limits beat adjectives.** "Under 100 words" works. "Be concise" and "be thorough" do not change much.
- **An example is the strongest signal for format.** If output must match a template, show a filled-in example.
- **Explain why.** "This goes to a text-to-speech reader" helps Claude generalize better than "NEVER use ellipses."
- **State the goal as well as the format.** "Three bullets" is a format. "Convince my team this timeline is realistic" is a goal. Claude needs both.

### Structure with labels or tags

For longer prompts, separate the parts with clear labels so instructions don't blur into source material. XML-style tags work well in claude.ai, and plain headings work too:

```
<context>Who I am, who reads this, why it matters</context>
<notes>The pasted source material</notes>
<task>What to do</task>
<format>The exact output shape</format>
```

For long documents, put the material first and the question at the end.

### Task decomposition and prompt chaining

One giant prompt that asks for six things tends to produce shallow work on all six. Decompose when the request has several deliverables, depends on earlier results, or needs a check in the middle.

| Technique | How it works | Use it when |
|---|---|---|
| **Sequential steps in one prompt** | "First do A. Then B. Then C." | Steps are simple and you trust the flow |
| **Checkpoint** | "Stop after step 2 and show me the result before continuing." | Later steps depend on an earlier result you must verify |
| **Prompt chain** | Separate prompts, each using the checked output of the last | Multi-part deliverables, long documents, anything you will review step by step |
| **Self-correction chain** | Draft → "Review this draft against these criteria" → "Revise it" | Quality matters and you can state the criteria |

Each step should produce something you can check. A checkpoint also counters reasoning drift on long, dependent tasks.

### Iteration

Your first prompt rarely produces the final result. Iterate with **specific** feedback.

| Vague feedback | Specific feedback |
|---|---|
| "Make it shorter." | "Cut the first two paragraphs and end with the ask." |
| "Make it better." | "The second bullet repeats the first. Replace it with the budget freeze." |
| "More professional." | "The real problem is that it buries the ask. Put the request in the first sentence." |

Three iteration moves:

1. **Follow up** in the same chat with specific feedback when the draft is mostly right.
2. **Edit the original prompt** (the pencil icon) and resubmit when the first prompt itself was the problem.
3. **Start fresh** with a clearer prompt when the chat has gone off track.

When you are stuck, ask Claude to improve the prompt: "Here's my prompt and the output I got. Ask me the questions you need answered to write a better prompt."

When Claude follows an instruction literally but uselessly, restate the goal. Repeating the instruction louder does not close the gap.

### Strategy by task type

| Task type | What to include | What to avoid |
|---|---|---|
| **Analysis** | The data or document, the criteria, a request for reasoning before conclusions, and a request for a single recommendation if you want one | Asking "what do you think?" with no criteria. You get a balanced discussion when you wanted a decision. |
| **Research** | Research mode or web search, specific goals, sections you want, constraints (budget, region, timeframe), and a requirement for checkable sources | Trusting the model's training knowledge for recent facts |
| **Drafting** | Audience, purpose, tone, length, format, and an example | Generic "write a post about X" |
| **Brainstorming** | Ask for volume first (20 ideas), then narrow with criteria. Use turn-by-turn chat. | Asking for "the best idea" in one shot |

## Exam traps

| Trap | Why it fails |
|---|---|
| Add "be detailed", "be concise", or CAPITAL LETTERS | Intensifiers add no structure. Use concrete limits. |
| Regenerate the same prompt until it works | Doesn't address the cause. Change the prompt. |
| One giant prompt for a multi-part deliverable | Decompose into steps you can check. |
| Paste every document you have "for context" | More context is not always better. Attention is finite. Curate what you include. |
| Switch to a bigger model to fix generic output | Generic output usually means missing context and constraints. |
| Describe the format in prose when it must match a template | Show a filled example. |
| Repeat an ignored instruction more forcefully | Restate the goal behind the instruction. |

## Demo: from raw notes to a structured, decomposed prompt

**Goal:** turn messy meeting notes into a reliable action-item table and follow-up email, using structure, decomposition, and specific iteration.

**Files:** `assets/demo-files/meeting-notes-raw.md` (fictional weekly ops sync)

**Steps:**

1. Open claude.ai, start a new chat (Sonnet), and upload `meeting-notes-raw.md`.
2. Run the weak prompt first so you have a baseline:

```
Summarize these notes and tell me what to do.
```

3. Note what you got. Typical problems: no owners or dates, a generic "next steps" list, and possibly invented owners for items nobody owns.
4. Start a **new chat**, upload the file again, and run the structured prompt. This is step 1 of a chain, with a checkpoint:

```
<role>You are the chief of staff to Dana, the operations lead.</role>

<context>The attached notes are from our weekly ops sync. Dana will send a follow-up to the four attendees today. Accuracy matters more than polish: if something is not in the notes, it must not appear in your output.</context>

<task>Step 1 only: extract every action item, request, and open decision from the notes. Then stop and wait for me to review before doing anything else.</task>

<format>
A table with columns: Item | Owner | Due date | Status | Risk or dependency.
- Owner: use a name only if the notes name one. Otherwise write "Unassigned".
- Due date: use only dates stated in the notes. Otherwise write "Not stated".
- Status: one of Open, Decided, No decision.
- Risk or dependency: note any legal, IT, or budget check mentioned.
Example row:
| Export last 90 days of tickets | Raj | Not stated | Open | Contains customer emails; legal check before sharing |
</format>
```

5. **Checkpoint.** Compare the table with the notes yourself before going on. Check that:
   - the weekly ticket summary shows **Unassigned** (the notes say nobody owns it)
   - Mei's "let the AI send the promo emails automatically" shows **No decision**
   - the dates are Oct 20 (webinar assets), Nov 1 (budget freeze), and Thursday (next sync)
   - the budget freeze and IT review for AI tool spend appear as a dependency
6. If anything is wrong, give specific feedback. For example:

```
Row 4 has an owner the notes don't name. Change it to Unassigned. Also add the IT review requirement for any AI tool spend as a dependency on every row that involves a new tool.
```

7. Step 2 of the chain: draft the email from the checked table only.

```
Step 2: Using only the table we just confirmed, draft Dana's follow-up email to Raj, Mei, and Tom.
- Under 150 words.
- Open with the two items due soonest.
- List unassigned items and ask who will own them.
- Keep the promo-email automation as an open question for Thursday. Do not imply it was approved.
- Plain, friendly tone. No subject-line puns.
```

8. Step 3: a self-correction pass with stated criteria.

```
Review your email against these criteria and list any failures before revising: (1) every fact appears in the table, (2) under 150 words, (3) no decision is presented as made when the notes say "no decision", (4) the ask to each person is clear. Then give me the revised email.
```

9. Optional: ask Claude to coach you on the weak prompt from step 2.

```
Earlier I used this prompt: "Summarize these notes and tell me what to do." Explain in three bullets why it produced weak output, and rewrite it using role, context, task, constraints, and format.
```

**What a good result looks like:** a table with six to eight rows, no invented owners or dates, the legal check and IT review flagged, and an email under 150 words that asks for owners and leaves the automation question open. The self-review lists concrete checks. "Looks good" is not a review.

**Debrief:** the structured prompt fixed the output with role, context, a precise format, an example row, and an explicit rule for missing information. Decomposition put a human checkpoint between extraction and drafting, so errors got caught before they spread into the email. The iteration step used specific feedback in place of "make it better." Each of these maps to one D1 objective.

## Use cases to work through

1. **Teacher: feedback on 30 student essays against a rubric.** Suggested approach: paste the rubric, one anonymized essay, and one example of feedback you consider excellent. Ask for feedback in the same structure, under 120 words, with one strength and two specific next steps. Review each draft before it reaches a student.
2. **Marketer: webinar title ideas.** Suggested approach: brainstorm in turn-by-turn chat. Ask for 20 titles across five angles, then narrow: "Keep the five that promise a concrete outcome for team leads, under 8 words." Volume first, criteria second.
3. **PM: 200 survey responses, top three issues.** Suggested approach: analysis prompt with role (product analyst), the attached responses, and a countable output: "Rank the three most frequent issues with the count and one representative quote each." Decompose if the first pass mixes themes: categorize first, then count. Spot-check the counts.
4. **Consultant: market scan for a client in a new region.** Suggested approach: Research mode with a specific goal, the sections you want, constraints (region, company size, last 12 months), and a requirement that every figure link to its source. Ask Claude to help sharpen the research prompt before running it.

## Check yourself

1. A colleague's output is accurate but always runs too long. They added "be concise" and nothing changed. What should they do?
2. You need a slide outline, speaker notes, and a one-paragraph summary from a 40-page report. Why decompose, and where would you put a checkpoint?
3. You asked Claude to evaluate three vendors and got a balanced discussion with no recommendation. What is the most likely cause?

<details>
<summary>Answers</summary>

1. Replace the adjective with a concrete limit, such as "under 100 words" or "five bullets maximum." Concrete limits can be checked. Adjectives can't.
2. Three deliverables from a long source produce shallow work in one prompt. Extract the key points first, check them against the report (checkpoint), then build each deliverable from the checked points.
3. The prompt never asked for a decision. Ask for a single recommendation with the reason and the criteria used.

</details>

## Official resources

- Prompting best practices (Anthropic docs): https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Getting better results (Claude 101): https://academy.claude.com/courses/claude-101/getting-better-results
- Your first conversation with Claude (Claude 101): https://academy.claude.com/courses/claude-101/your-first-conversation-with-claude
- Effective prompting techniques (AI Fluency): https://academy.claude.com/courses/ai-fluency-framework-foundations/effective-prompting-techniques
- A closer look at Description (AI Fluency): https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-description
- Steerability (AI Capabilities and Limitations): https://academy.claude.com/courses/ai-capabilities-and-limitations/steerability
- Official prep course, Prompting & Task Execution: https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/prompting-task-execution

---

**Next:** [Lesson 3: Output Evaluation and Validation](03-output-evaluation-and-validation.md)
