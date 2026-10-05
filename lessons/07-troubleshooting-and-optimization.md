# Lesson 07: Troubleshooting and Optimization

**Exam domain: D7 Troubleshooting and Optimization (10%)** · Time in session: about 6 minutes (Segment 4)

4Ds lens: **Discernment**. You judge why an output fell short, then fix the cause instead of retrying and hoping.

---

## 1. What the exam asks

The exam guide lists three objectives for this domain (verbatim):

- Identify, diagnose, and resolve issues with underperforming prompts or poor outputs
- Adjust approach based on feedback and results
- Optimize workflows for efficiency and effectiveness

Expect about six items. A typical stem says "this used to work and now it doesn't" or "the output keeps coming back wrong" and asks for the best *first* step.

---

## 2. Key ideas

### The five-question diagnostic checklist

Run these in order before you rewrite anything.

| # | Question | What to look at |
|---|---|---|
| 1 | **What changed?** | New or edited knowledge files, edited instructions, a different model or effort setting, a new connector, a different input file, a different person running it |
| 2 | **Does Claude have the context it needs?** | Is the source attached or connected? Is the key fact buried in a long chat? Has the chat drifted? Did a teammate supply context you don't? |
| 3 | **Are the instructions clear and consistent?** | Is the goal stated? Are limits concrete ("under 120 words") or vague ("be concise")? Do two rules conflict? |
| 4 | **Do the model and settings fit the task?** | A light model on hard reasoning, or the top model at maximum effort on routine work |
| 5 | **Where do the facts come from?** | An attached or connected source, or Claude's general knowledge? Specific names, numbers, and citations need a source |

Then apply two working rules:

- **Change one thing at a time.** If you change the model, the instructions, and the knowledge at once, you cannot tell which change helped.
- **Rerun the same test inputs.** Keep five to ten examples with known-good outputs and compare against them after each change.

### Common failures and first fixes

| Symptom | Likely cause | First fix |
|---|---|---|
| Generic, could-be-anyone output | Missing context | Add role, audience, purpose, source material, and an example |
| Too long or too short | Claude is guessing the length | State a number: "under 100 words", "five bullets" |
| Wrong format | Format described vaguely | Show a filled example of the format |
| Confident but wrong facts | No source for specifics | Attach or connect the source, ask for quotes, verify |
| Wrong tone | Default helpful-professional voice | Describe the tone plainly and give a sample |
| Half the request ignored | Too many asks in one prompt | Decompose into steps and check each one |
| Instructions forgotten late in a long chat | Context drift | Summarize decisions, start a new chat, move standing rules into Project instructions |
| A balanced essay when you wanted a decision | The prompt never asked for one | Ask for one recommendation with reasons |
| Rule followed literally but uselessly | Claude met the letter of the instruction | Restate the goal behind the rule. Repeating the rule louder does not help |
| Agrees with your flawed premise | Sycophancy | Invite pushback: "Tell me where I'm wrong" |
| Arithmetic errors in a table | Language models are unreliable at exact math | Use code execution or a spreadsheet, then check the inputs |
| Works for one colleague, fails for others | Unstated context in that colleague's prompts or setup | Compare exact prompts, files, and settings. Share a Project |
| Different answers on each run | Normal variation plus an underspecified task | Tighten the instructions and output format. Verify facts at the source |
| Project answers got worse after new files were added | Stale, duplicate, or conflicting knowledge | Remove superseded files and rerun the test set |
| Missed instructions or unfinished work | Effort set too low | Raise effort for this task |
| Wordy output, scope creep, overthinking | Effort set too high | Lower effort for routine work |

### Adjust based on feedback and results

- **Ask for specific feedback.** "Too long" becomes "cut the background paragraph and keep the three figures."
- **Steer early.** Redirect a draft as soon as it heads the wrong way. A quick correction costs less than a full regenerate.
- **Know when to restart.** When a chat has drifted far off track, a new chat with a clearer prompt is often faster.
- **Make repeated corrections permanent.** A correction you type every week belongs in personal or Project instructions. An explanation you repeat belongs in a Skill.
- **Remember the model does not learn from you.** A correction lasts only while it stays in context or gets saved to instructions, knowledge, or memory.

### Optimize workflows for efficiency and effectiveness

Optimization means less time and cost at the same quality.

| Lever | When to pull it |
|---|---|
| **Right model tier** | Routine, high-volume work on a faster, lower-cost model. Hard reasoning on the most capable model |
| **Effort setting** | Lower for routine tasks, higher for complex analysis |
| **Fresh chats** | Each turn re-sends the whole conversation. A new chat for a new task is cheaper and avoids stale context |
| **Projects** | Stop re-pasting the same background every week |
| **Templates and Skills** | Save prompts for recurring tasks. A Skill loads only when needed |
| **Fewer active tools** | Turn off connectors and features the task doesn't use |
| **Find the real bottleneck** | The slow step is often a human handoff or approval |
| **Question the step** | Before you automate a report, confirm someone uses it |

---

## 3. Exam traps

| Trap answer | Why it fails | Pattern |
|---|---|---|
| "Regenerate until it works." | Retrying does not address the cause. | Irrelevant fix |
| "Switch to the most capable model." | Most failures come from context, instructions, or sources. A bigger model costs more and leaves those in place. | Over-engineering |
| "Rewrite the whole prompt from scratch." | You lose what worked and still don't know what broke. Diagnose what changed first. | Over-reaction |
| "Repeat the instruction in capital letters." | Volume adds no structure. State the goal or a concrete limit. | Irrelevant fix |
| "Change the model, the instructions, and the files together to save time." | You cannot tell which change mattered. | Over-engineering |
| "Ask Claude to double-check itself and trust the answer." | A self-check is not independent evidence. | Fake safeguard |
| "Stop using Claude for this task." | A targeted fix usually exists. | Over-reaction |
| "Use the top model at maximum effort for everything." | It wastes cost and time on routine work. | Over-engineering |

---

## 4. Demos

### Demo A: Diagnose and fix a bad prompt

**Goal:** Show that retrying does not fix a weak prompt, then use the checklist to find and fix the cause.

**File:** `assets/demo-files/project-knowledge-brand-voice.md`

#### Steps

**1. Run the bad prompt.** In a new chat (outside any Project), send:

```
write a linkedin post about our courses
```

**What you'll see:** a generic post. It may invent course names, prices, or statistics, use hype words, and run to any length.

**2. Retry once.** Click the retry button. The new version is different but no better. Retrying changed nothing about the cause.

**3. Run the checklist out loud.** Ask the room each question:

- What changed? Nothing yet. This is a first attempt.
- Context? Claude knows nothing about "our courses", our audience, or our rules.
- Instructions? No audience, length, structure, or tone.
- Model and settings? Fine for a short post. A bigger model would not know our facts either.
- Source of facts? None. Any specifics in the post were invented.

**4. Fix the cause.** Start a new chat, upload `project-knowledge-brand-voice.md`, and send:

```
You are writing for Northwind Learning's LinkedIn page.

Use the attached brand voice file for audience, voice, format, and facts. Only use facts from its "Facts we can state" section.

Write one LinkedIn post about our live online courses for team leads.
- Length: 120 to 180 words.
- Structure: problem, short example, takeaway, closing question.
- Avoid every word on the "Never use" list.

After the post, list any fact you used and the line in the file it came from.
```

**What good looks like:** 120 to 180 words with the four-part structure. Only file-backed facts appear (4 weeks, 2 hours per week, live online, 12,000+ learners). No pricing and no banned words. The fact list at the end lets you verify each claim in seconds.

#### Debrief

The fix came from diagnosis: missing context, missing constraints, and no source. This maps to *Identify, diagnose, and resolve issues with underperforming prompts or poor outputs*. On the exam, "regenerate" and "use a more capable model" are the usual wrong answers for this situation.

### Demo B: What changed? A stale file in the Project

**Goal:** Show the first question of the checklist in action. A Project that worked starts misbehaving after someone adds an old file.

**Files:** the `Northwind content` Project from Lesson 05, plus `assets/demo-files/brand-voice-2023-edition.md` (an outdated, fictional brand guide)

#### Steps

**1. Simulate a colleague's change.** Upload `brand-voice-2023-edition.md` to the `Northwind content` Project's knowledge. Leave the current brand voice file in place.

**2. Run a request in a new Project chat:**

```
Write a promo email for our October webinar on giving feedback.
```

**What you'll see:** some mix of the old rules. Possible signs: a price ($499 or $399 early-bird), a partner name (Brightline Consulting), a promotion statistic, exclamation points, or a longer length. Results vary. If Claude notices two conflicting brand files and asks which one to follow, that is a good outcome to discuss. It still means the knowledge base needs fixing.

**3. Diagnose.** Ask the room: "Nobody touched the instructions. What changed?" Open the Project knowledge and find two brand voice files with conflicting facts.

**4. Fix one thing.** Remove `brand-voice-2023-edition.md` from knowledge. Change nothing else.

**5. Rerun the same request in a new chat.**

**What good looks like:** no price, no partner names, no outcome claims. Because the current file has no promo-email format, Claude should ask a clarifying question or choose the closest format and say so. That behavior comes from the instructions you wrote in Lesson 05.

#### Debrief

This is the most testable pattern in D7: when something that worked breaks, find what changed before rewriting anything. It also connects back to D5. Replace superseded files instead of adding them beside the current ones, and rerun a fixed test after each change.

---

## 5. Use cases to work through

**Communications manager: press releases went off-tone.** Drafts from the team's Project were fine last month and now sound stiff and legalistic. *Suggested approach:* check what changed. She finds a colleague added "always include full legal disclaimers" to the Project instructions. She discusses the rule with the colleague, moves it to a separate instruction for investor releases only, and reruns three past releases as a test.

**Sales operations lead: usage limits by noon.** The team hits its limits every day. *Suggested approach:* review which model and effort the team uses for which task. Routine email personalization runs on the most capable model at high effort. Move routine drafting to a faster tier or lower effort, test ten samples for quality, and keep the top tier for complex deal analysis. Encourage fresh chats for each new task instead of one all-day thread.

**Teacher: inconsistent feedback across essays.** Claude's feedback on similar essays varies a lot. *Suggested approach:* the prompt never included the rubric. Add the rubric and two annotated sample essays to a Project, require feedback organized by rubric criterion, and compare the output on three essays she has already graded. She still assigns every grade herself.

**Financial analyst: totals that don't add up.** Claude's variance table looks clean but a subtotal is off. *Suggested approach:* have Claude compute the figures with code execution, or recompute in the spreadsheet. Then check the inputs and definitions, because correct arithmetic on the wrong rows is still wrong.

---

## 6. Check yourself

**1.** A Project that produced good onboarding emails for months now includes outdated benefit amounts. Nobody edited the instructions. What is your first step?

<details><summary>Answer</summary>

Check what changed in the Project, starting with the knowledge files. An old or duplicate benefits document is the likely cause. Remove the superseded file and rerun a few known test requests.

</details>

**2.** Your manager says every summary Claude writes for her is "too long". You keep typing "shorter please" in each chat. What is the better adjustment?

<details><summary>Answer</summary>

Turn the feedback into a concrete, standing rule, such as "Summaries for Dana: five bullets maximum, decision first". Put it in your Project or personal instructions, then check a few new summaries with her.

</details>

**3.** An analyst spends 40 minutes every Monday pasting the same three background documents into a new chat and asking for a ticket summary on the most capable model at maximum effort. Name two optimizations.

<details><summary>Answer</summary>

Any two of these: move the background documents into a Project, save the prompt as a template with a fixed output table, and test whether a faster tier or a lower effort setting gives the same quality. Also ask whether anyone still uses every part of the summary.

</details>

---

## 7. Official resources

- Anthropic Partner Academy prep course 7, *Troubleshooting & Optimization* (30 min): https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/troubleshooting-optimization
- Claude 101, *Getting better results*: https://academy.claude.com/courses/claude-101/getting-better-results
- AI Capabilities and Limitations, *When properties collide*: https://academy.claude.com/courses/ai-capabilities-and-limitations/when-properties-collide
- Tutorial, *How to select the right effort setting*: https://academy.claude.com/tutorials/how-to-select-the-right-effort-setting-for-claude-cowork-and-chat
- Tutorial, *Parametric memory and context*: https://academy.claude.com/tutorials/parametric-memory-and-context
- Help center, *How do usage and length limits work?*: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work

---

**Next:** [Lesson 08: Exam Strategy and Study Plan](08-exam-strategy-and-study-plan.md)
