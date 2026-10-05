# Lesson 1: Platform and Model Selection

**Exam domain:** D3 Product and Model Selection (12%) · **Time in session:** Segment 1, about 15 minutes

## What the exam asks

Verbatim objectives from the Exam Guide:

- Select appropriate Claude product features (Projects, research mode, chat, artifacts)
- Differentiate between Claude model types (Haiku, Sonnet, Opus)
- Align model selection with task requirements (cost, speed, quality)
- Understand and manage context limitations and memory considerations (when to restart, summarize, or persist)

The official prep course frames this domain as "the four decisions that set the quality ceiling for every Claude session before you write a single prompt": entry point, capability features, model, and context.

## Key ideas

### Decision 1: the entry point and features

| You need to... | Use | Signal words in a question |
|---|---|---|
| Think, draft, or brainstorm turn by turn | **Chat** | "explore", "quick draft", "talk through" |
| Reuse the same reference files and instructions across many chats | **Project** | "every week", "same format", "team", "ongoing" |
| Get one current fact fast | **Web search** | "today's", "latest price", "who won" |
| Produce a cited report from many sources | **Research** (web search must be on) | "comprehensive", "compare vendors", "market scan", "with sources" |
| Reason hard over material you already have | **Extended thinking** or higher **effort** | "complex logic", "trade-offs", "multi-step analysis" |
| Get a standalone deliverable to edit, reuse, or share | **Artifact** | "one-pager", "dashboard", "tracker", "share with the team" |
| Get a downloadable Word, Excel, PowerPoint, or PDF file | **File creation** (needs code execution and file creation enabled) | ".docx", "spreadsheet", "slide deck to send" |
| Hand off a multi-step task that ends in a finished file, works in your folders, or runs on a schedule | **Cowork** (desktop app, paid plans) | "every Monday", "in this folder", "finished file" |
| Write, test, and ship software | **Claude Code** | "code", "repository", "deploy". This is developer territory, so an Associate escalates. |

Three rules settle most feature questions:

- **Research is for depth.** A quick fact needs web search. Research takes minutes and returns a cited report from many sources.
- **Projects are for recurring context.** If you paste the same background into every chat, the answer is a Project. Lesson 5 covers configuration.
- **Features combine.** A weekly competitor brief can use a Project (standing instructions), Research (current sources), and an Artifact (the shareable output) together.

### Decision 2: the model tier

The exam guide names three model families. Learn the trade-off, never the version number.

| Tier | Speed | Cost and usage | Best for | Exam cue |
|---|---|---|---|---|
| **Haiku** | Fastest | Lowest | Quick answers, summaries, simple extraction, high-volume routine drafts | "hundreds of", "simple", "fast", "keep usage light" |
| **Sonnet** | Fast | Moderate | Everyday writing, analysis, and multi-step work. The versatile default. | "typical", "most tasks", "not sure" |
| **Opus** | Slower | Highest | Deep reasoning, complex analysis, hard judgment calls that justify the cost | "complex", "nuanced", "high-stakes reasoning" |

Anthropic's current lineup also includes **Fable**, a newer tier above Opus for long, complex tasks with fewer check-ins. The exam guide names three tiers, so answer exam items with Haiku, Sonnet, and Opus.

The tested logic comes straight from official Sample 2: match "a faster, lower-cost model" to "straightforward, high-volume tasks," and reserve "the most capable model for complex reasoning." Two answers are wrong every time:

- **Strongest model everywhere.** It wastes the cost and latency budget.
- **Smallest model for hard work.** It under-serves complex reasoning.

Escalate on evidence. Start with Sonnet. Move to Opus when you have tested Sonnet on the task and it struggled.

### The effort lever

Model choice is one lever. Effort (and extended thinking) is a second.

| Lever | What it changes | Use it when |
|---|---|---|
| **Model** | Capability and cost | The task needs more (or less) raw capability |
| **Effort / extended thinking** | How thoroughly Claude works before answering. Cost goes up. The model's core capability stays the same. | The model is capable, but the task needs more careful reasoning, or the work is routine and needs less |

Signs of too little effort: missed instructions, unfinished work. Signs of too much: verbose answers with no quality gain, scope creep, slow replies to simple questions. Think in **cost per task**. A stronger setup that finishes in one turn can cost less than a cheap one that needs five follow-ups.

A bigger model does not fix a missing source, a vague prompt, or a policy problem. If a question's real issue is context or governance, the "upgrade the model" option is an irrelevant fix.

### Decision 3: context

The **context window** holds everything Claude can attend to in one conversation: your messages, its replies, and uploaded files. Standard windows hold roughly 500 pages of text, and some plans and models offer more. Four facts matter for the exam:

- **The whole conversation is re-sent every turn.** Long chats cost more usage and slow down. A fresh chat is often the cheapest way to get a good answer.
- **Attention is finite.** Key facts buried in the middle of long material get missed more often. Put the most important instructions at the start and end.
- **Long chats drift.** Early rules (format, tone) get followed less reliably as the conversation grows.
- **Near the limit, claude.ai can summarize earlier messages** to keep going. A summary loses detail.

**Context limit** and **usage limit** are different things. The context limit is how much fits in one conversation. The usage limit is how much you can use Claude over a period of time.

### Restart, summarize, or persist

| Situation | Move |
|---|---|
| The chat drifted or ignores early rules | **Restart:** open a new chat with a short summary of decisions and the rules |
| Same task, conversation is getting long | **Summarize:** ask Claude for a handoff summary, check it, and carry it into a new chat |
| New, unrelated task | **Restart:** a fresh chat avoids old context biasing the answer |
| Facts or rules needed across many sessions | **Persist:** Project instructions and knowledge, your personal instructions in Settings, or memory |
| Sensitive one-off you don't want in history | **Incognito chat** |

### Memory and Incognito

- Claude does not learn from your corrections. It responds only to what is in context. A correction lasts only if it is persisted somewhere.
- **Memory** saves useful context across chats. It is on by default for Free, Pro, and Max. On Team and Enterprise, owners control it. Each Project has its own memory space. You can view, edit, and delete memory in Settings.
- **Search and reference chats** (paid plans) lets Claude look up past conversations.
- **Incognito chats** are not saved to your history and are not searched in later chats. They still follow your organization's retention policy. Incognito does not make restricted data safe to upload.
- Memory is a convenience. It is not a source of truth, and it does not replace Project knowledge for reference material.

## Exam traps

| Trap | Why it fails |
|---|---|
| "Use the most capable model for everything" | Over-engineering. Ignores cost and speed (official Sample 2, option A). |
| "Upgrade the model" when the output lacks facts or context | Irrelevant fix. The problem is the input. |
| "Use Research mode" for a single quick fact | Over-engineering. Web search answers it in seconds. |
| "Claude will remember what I told it last week" | Only through memory, a Project, or instructions. A new chat outside those starts blank. |
| "Repeat the formatting rule more forcefully" in a drifting 60-turn chat | Irrelevant fix. Restart with a summary and persist the rule. |
| "Incognito means the data is approved for upload" | Fake safeguard. Policy decides what you may upload. |
| "Keep everything in one long chat to save effort" | Long chats re-send everything, cost more, and drift. |

## Demo A: feature picker and same task, two models

**Goal:** pick the right feature and model tier for realistic tasks, then see the tier trade-off on a real file.

**Files:** `assets/demo-files/meeting-notes-raw.md`

**Part 1: feature picker (3 minutes).** For each scenario, choose a feature before you open the answers.

| # | Scenario |
|---|---|
| 1 | A PM needs today's exchange rate for a budget line. |
| 2 | A consultant needs a cited comparison of five project-management vendors for a client. |
| 3 | A teacher writes weekly parent newsletters from the same school calendar and style guide. |
| 4 | A marketer wants a one-page launch brief the whole team will edit and reuse. |
| 5 | An ops lead wants a status roll-up file created from a folder of reports every Monday morning. |
| 6 | A finance analyst needs a downloadable Excel file with formulas for a vendor comparison. |
| 7 | A comms manager is brainstorming headline angles for a press release. |
| 8 | A colleague wants to build an internal tool that pulls tickets from the help-desk system automatically. |

<details>
<summary>Answers</summary>

1. Web search. 2. Research. 3. Project. 4. Artifact. 5. Cowork scheduled task. 6. File creation. 7. Chat. 8. Escalate to a Claude Developer or Architect. System integration is outside the Associate scope.

</details>

**Part 2: same task, two models (5 minutes).**

1. Open claude.ai and start a new chat. Pick **Haiku** in the model selector.
2. Upload `meeting-notes-raw.md`.
3. Paste this prompt:

```
Summarize the attached meeting notes in five bullet points. Then flag the one item you would most want a human to check before anyone acts on it, and explain why in one sentence.
```

4. Start a second new chat. Pick **Sonnet**. Upload the same file and paste the same prompt.
5. Put the two answers side by side.

**What a good result looks like:** both models produce a usable summary. Compare where the answers differ. Look at which item each flags. A strong answer flags the ticket CSV that contains customer emails (legal must check it before sharing) or the request to let AI send promo emails automatically. Ignore length. Judge substance.

**Debrief:** for a short summary, the faster tier is often good enough, and that is the Sample 2 logic. When the task needs judgment about risk, compare the tiers on that part of the answer. Choose the smallest model that holds quality on the task you actually run.

## Demo B: drift, summarize, start fresh

**Goal:** practice the restart and summarize moves, and see why rules belong somewhere persistent.

**Files:** `assets/demo-files/meeting-notes-raw.md`

**Steps:**

1. Start a new chat (Sonnet). Upload `meeting-notes-raw.md` and set a rule:

```
For this whole conversation, follow two rules: answer in at most 3 bullet points, and end every answer with a line that says "Owner: <name>" naming the person responsible. First question: what is the most urgent item in these notes?
```

2. Ask a few follow-ups, then pull the chat off course with a long tangent:

```
Forget the format for a moment. Write me a 400-word brainstorm of ideas for the Q4 webinar theme.
```

```
Now back to the notes: what should Raj do first this week?
```

3. Check the last answer. Did it keep the 3-bullet limit and the "Owner:" line? In a short demo the rule may hold. In a 50-turn working chat with long tangents, early rules weaken. The next steps are the habit to build either way.
4. Ask for a handoff summary:

```
Write a handoff summary I can paste into a new chat. Include: the goal, decisions made so far, open questions, and the two formatting rules I set at the start. Keep it under 150 words.
```

5. Read the summary and fix anything wrong or missing. A summary loses detail, so you check it before you rely on it.
6. Open a **new chat**, paste the summary, re-upload the notes file, and ask: `What should Raj do first this week?`
7. Optional blank-slate check: in another new chat, ask `What formatting rules did I give you?` Without the summary, Claude has no access to the earlier chat's rules. (If memory or chat search is on, Claude may find related context. That is persistence through a feature you can see and manage in Settings.)

**What a good result looks like:** the new chat follows both rules from the first answer, with a much shorter context.

**Debrief:** restart when a chat drifts, summarize to carry decisions forward, and persist rules you will need again. If this were a weekly ops sync, the two formatting rules belong in Project instructions so every chat starts with them. That is the D3 objective "when to restart, summarize, or persist" in one exercise.

## Use cases to work through

1. **Marketer: 300 product-tag descriptions by Friday.** Each is two sentences from a short spec. Suggested approach: Haiku (or Sonnet with low effort), a single tested prompt with one example, and spot checks on a sample. Opus would waste cost on routine work.
2. **Consultant: board memo on a merger's operational risks.** It requires weighing conflicting evidence across several long documents. Suggested approach: Opus, or Sonnet with extended thinking, with documents uploaded and the key question placed at the end of the prompt. Verify every figure before it goes to the board.
3. **PM: "What changed in our competitor's pricing this quarter?"** Suggested approach: Research with web search on, then open the cited pages for the key numbers. A bigger model does not know events after its training data.
4. **Ops lead: a 70-turn chat now ignores the agreed report template.** Suggested approach: ask for a handoff summary, start fresh, and move the template into Project instructions so it applies to every future chat.

## Check yourself

1. A support lead needs 500 short, simple reply drafts today, and usage is tight. Which tier fits best, and which wrong answer is the exam's favorite trap?
2. A chat has run for two hours and Claude has stopped following the citation format you set at the start. What are the two best moves?
3. You need one fact: the current CEO of a supplier. Research mode or web search?

<details>
<summary>Answers</summary>

1. Haiku (the fast, low-cost tier). The trap is "use the most capable model for every reply."
2. Start a new chat with a summary of decisions and rules, and persist the citation format in Project instructions (or personal instructions) so you stop re-teaching it.
3. Web search. Research is for multi-source, cited reports and takes minutes.

</details>

## Official resources

- Choosing the right Claude model (Academy tutorial): https://academy.claude.com/tutorials/choosing-the-right-claude-model
- Selecting the right effort setting: https://academy.claude.com/tutorials/how-to-select-the-right-effort-setting-for-claude-cowork-and-chat
- Research mode for deep dives (Claude 101): https://academy.claude.com/courses/claude-101/research-mode-for-deep-dives
- Chat, Cowork, and Code in the desktop app (Claude 101): https://academy.claude.com/courses/claude-101/claude-desktop-app-chat-cowork-code
- Choosing between Cowork and Chat: https://academy.claude.com/tutorials/choosing-between-claude-cowork-or-chat
- Creating with artifacts (Claude 101): https://academy.claude.com/courses/claude-101/creating-with-artifacts
- Parametric memory and context: https://academy.claude.com/tutorials/parametric-memory-and-context
- Usage and length limits (Help Center): https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
- Memory and Incognito (Help Center): https://support.claude.com/en/articles/11817273
- Official prep course, Claude Platform & Model Foundations: https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/claude-platform-model-foundations

---

**Next:** [Lesson 2: Prompting and Task Execution](02-prompting-and-task-execution.md)
