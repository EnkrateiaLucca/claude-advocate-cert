# Lesson 4: Workflow Integration and Solution Design

**Exam domain:** D4 Workflow Integration and Solution Design (16%) · **Time in session:** Segment 3, about 15 minutes

## What the exam asks

Verbatim objectives from the Exam Guide:

- Apply Claude to analyze requirements and use cases
- Leverage Claude for research, planning, and process optimization
- Use Claude to support solution design, development, and iteration
- Integrate Claude into existing workflows to augment or redesign them
- Communicate Claude's value and limitations to stakeholders

The official prep course describes the shift as moving from "I use Claude" to "our workflow uses Claude" by deciding which steps to delegate to the model and which to keep with humans. In 4D terms, this domain is **Delegation**: what work goes to Claude, what stays with people, and where the review step sits.

## Key ideas

### Start with requirements

Define four things before you prompt or design anything:

| Requirement | Question | Example (weekly ticket report) |
|---|---|---|
| **Deliverable** | What exactly gets produced? | One-page summary of tickets by category, with week-over-week change |
| **Audience** | Who uses it, and for what decision? | Ops lead, to decide where to add help content |
| **Sources** | What data goes in, and is it approved for use? | Ticket export (contains customer emails, so legal must check it) |
| **Success** | How will you know it works? | Ready by Monday 10:00, category counts match a manual spot check |

Then audit the task with four questions: How often does it happen? How long does it take? Is it standardized or variable? What happens if it is imperfect?

Claude can help with this analysis. Ask it to interview you about the requirements before it proposes a design.

### Where Claude fits

| Strong fits | Weak fits |
|---|---|
| Drafting from approved inputs | Being the final authority on facts |
| Summarizing, categorizing, extracting | Accountable decisions (who to hire, which account to escalate) |
| Repurposing content for new formats and audiences | Emotionally sensitive conversations (complaints, bad news to a person) |
| Brainstorming and first-pass planning | Precise high-volume calculation a spreadsheet should own |
| Research synthesis with citations | Live data without web search, Research, or a connector |

### The delegation map

Sort each step of a workflow into one of three buckets.

| Bucket | What belongs here | Example |
|---|---|---|
| **Claude handles** | Standardized, documented, repeatable steps with low cost of error | Categorize tickets from an approved export |
| **Claude assists, human decides** | Claude drafts, a person reviews before it counts | Draft the weekly summary, ops lead approves |
| **Human handles** | High-stakes decisions, sensitive situations, complex judgment | Decide whether to change the pricing page |

Three criteria decide the bucket:

- **Reversibility:** can you undo it easily if it is wrong? Sending an email to 5,000 customers is hard to undo.
- **Stakes:** what does an error cost in money, reputation, legal exposure, or harm to people?
- **Accountability:** who has to answer for the result? That person keeps the decision.

Keep a human approval step wherever an action is hard to reverse or has external consequences. Before automating any step, ask whether the step needs to exist at all. Automating unnecessary work makes waste faster.

### Augment or redesign

| Approach | What changes | When to choose it |
|---|---|---|
| **Augment** | The workflow keeps its shape. Claude speeds up individual steps (drafting, summarizing, checking). | Start here. Low risk, quick to test, easy to roll back. |
| **Redesign** | The workflow changes shape. Steps merge, disappear, or move. Claude may own a step end to end with review. | The augmented version works, the bottleneck is the process itself, and you have evidence Claude is reliable on the task |

Good solution design follows a sequence:

1. **Pilot one workflow** with a small group.
2. **Validate on a known answer.** Have Claude redo a past task where you know the right result, compare, and refine. If you can't get there after several refinements, the task is a poor candidate for delegation.
3. **Measure** against the success criteria.
4. **Release autonomy gradually.** Recurring and scheduled tasks should draft for review until they have earned trust. Expand per task type after repeated successes.
5. **Turn repeated explanations into persistent setup:** Project instructions, knowledge, or skills (Lesson 5).

Big-bang rollouts and "full autonomy on day one" are wrong answers on the exam.

### Research, planning, and process optimization

Claude supports the design work itself:

- **Research:** Research mode for market scans, vendor comparisons, and synthesis across sources, with citations you verify.
- **Planning:** turn a goal into phases, owners, dependencies, and risks. Ask Claude to challenge the plan.
- **Process optimization:** paste a process description and ask Claude to find the bottleneck. The slow part is often a human step (approvals, handoffs, waiting for data), and a faster model won't fix it.

### Communicating value and limitations

Stakeholders trust a description that pairs a concrete benefit with an honest limit and a named person. A credible message includes:

| Element | Example |
|---|---|
| Bounded task | "Claude drafts the weekly ticket summary from an approved export." |
| Expected benefit, labeled honestly | "We estimate it saves about 2 hours a week. We'll measure it during the pilot." |
| Limitation | "Claude can miscategorize unusual tickets, so we spot-check 10 a week." |
| Human owner | "Dana approves the summary before it is shared." |
| Constraint | "No new tool spend. Any change goes through IT review." |

Avoid "fully automated", "error-free", or unmeasured savings claims. Usage numbers (active users, chats per week) are diagnostics. Pair them with work outcomes before calling something a success.

A simple team AI-use statement has three parts: **What we use AI for**, **What stays human**, and **How we stay accountable**.

### Know when to escalate

| Situation | Escalate to |
|---|---|
| Connecting Claude to internal systems (ticketing, CRM, databases), automated pipelines at volume, API work, custom connectors or agents | **Claude Developer or Architect** |
| Legal, medical, financial, or employment judgments | **A qualified human professional** |
| Personal or regulated data, new data sources | **Legal, privacy, or data owner** (and anonymize first) |
| New tool purchases, new integrations, policy exceptions | **IT, security, or the policy owner** |

The Associate keeps the work moving inside those lines. Escalating everything is over-engineering. Escalating nothing is blind trust.

## Exam traps

| Trap | Pattern | Why it fails |
|---|---|---|
| "Yes, Claude can handle the whole process, start building" | Blind trust | The right answer is a division of labor with a review step |
| "No, it involves customer data" | Over-reaction | Anonymize or use approved data, then proceed |
| Give the new workflow full autonomy on day one | Blind trust | Grant autonomy in proportion to demonstrated reliability |
| Roll out to every team at once | Over-engineering | Pilot one workflow, measure, then expand |
| Automate a report nobody reads | Irrelevant fix | Question the step before automating it |
| Escalate a simple drafting workflow to an Architect | Over-engineering | Associates own everyday workflow design |
| Report adoption numbers as proof of value | Fake safeguard | Usage is a diagnostic. Outcomes prove value. |
| Promise "fully automated, no errors" to win buy-in | Blind trust | Credibility needs stated limits and a named human owner |

## Demo: map a workflow and write the stakeholder note

**Goal:** analyze one workflow from the ops meeting, build a delegation map with escalation points, and write a stakeholder note that states value and limits honestly.

**Files:** `assets/demo-files/meeting-notes-raw.md`

**Steps:**

1. Open claude.ai, start a new chat (Sonnet), and upload `meeting-notes-raw.md`.
2. **Requirements first.** Ask Claude to interview you:

```
I'm Dana, the ops lead in these notes. I want to design a workflow for the "weekly summary of tickets by category" that nobody owns today. Before proposing anything, ask me up to 5 questions you need answered to define the requirements: deliverable, audience, data sources, success criteria, and constraints. Ask them all in one message.
```

3. Answer with these fictional details (copy and edit as needed):

```
1. Deliverable: a one-page summary every Monday by 10:00 with ticket counts by category, change vs last week, and the top 3 recurring questions.
2. Audience: me (ops lead) and Raj (support). We use it to decide which help-center articles to write.
3. Data: a CSV export from our ticketing system. It contains customer emails. Legal hasn't approved sharing it yet.
4. Success: ready on time every week, counts match a manual spot check of 10 tickets, and support tickets for "how do I export" go down after we publish the help article.
5. Constraints: no budget for new tools until Nov 1, and any AI tool spend goes through IT review. Nobody on the team writes code.
```

4. **Build the delegation map.**

```
Now map this workflow step by step, from getting the data to sharing the summary. Present it as a table with columns:
Step | Who does it (Claude handles / Claude assists, human decides / Human handles) | Why (reversibility, stakes, accountability) | Risk or dependency | Escalate to whom, if anyone

Then answer in 3 bullets: should we augment the current process or redesign it, and why? Which step should we pilot first?
```

5. **Check the map against what you know.** A good map:
   - puts the legal check on the CSV and the removal of customer emails **before** any upload to Claude
   - has Claude categorize and draft the summary, with Dana reviewing before it is shared
   - names Dana or Raj as the owner (the notes say nobody owns it today)
   - flags any automatic pull from the ticketing system as an integration to escalate to a Claude Developer or Architect, plus IT review because of the budget freeze
   - recommends augmenting first, with a manual weekly export and a short pilot
6. **Pressure-test one step.** Paste Mei's question from the notes:

```
Mei asked whether we can "just let the AI send the promo emails automatically." Using the same reversibility, stakes, and accountability criteria, where would sending promo emails sit in a delegation map? Give a recommendation in under 80 words.
```

   A good answer keeps sending with a human: Claude drafts, a person approves, and the send happens in the email tool. Sending to customers is external and hard to reverse.
7. **Write the stakeholder note.**

```
Write a note from Dana to Tom (finance) proposing a 4-week pilot of this workflow. Under 180 words. Include: the bounded task Claude performs, the expected benefit labeled as an estimate to be measured, one honest limitation and how we check for it, who approves the output, the legal and IT dependencies, and confirmation that the pilot needs no new tool spend. No hype words.
```

8. **Adapt it once.** Ask for a 3-bullet version for Raj's support team that focuses on what changes in their week.

**What a good result looks like:** a delegation map with five to seven steps, at least one step in each bucket, and the legal check placed before upload. The note to Tom states the benefit as an estimate, names Dana as approver, mentions the IT review, and avoids "fully automated" claims.

**Debrief:** you used Claude for all five D4 objectives in one pass. It helped analyze requirements, planned the process, designed the solution, judged augment versus redesign, and drafted the stakeholder message. You kept the judgment calls: approving the data, owning the summary, and deciding what goes to customers. The escalation points came straight from the notes. Customer data went to legal, the system integration went to a Developer or Architect, and the spend question went to IT.

## Use cases to work through

1. **Ops lead: onboarding emails take 3 hours a week.** Raj's team copy-pastes from a doc. Suggested approach: augment. Put the template and rules in a Project, have Claude draft each personalized email from a short form, and keep a person sending them. Measure time saved over four weeks before considering any automation, which would be an escalation to a Developer.
2. **Marketer: "Can Claude run our social calendar?"** Suggested approach: answer with a division of labor. Claude drafts posts and adapts content across platforms. A person approves every post, owns replies to comments, and handles anything sensitive. Pilot one channel for a month.
3. **Teacher: department-wide feedback workflow.** Teachers want faster feedback on lab reports. Suggested approach: pilot with one teacher and one assignment. Validate on last term's graded reports, where the right feedback is known. Claude drafts feedback against the rubric, and the teacher edits and owns every grade. Grades are an academic assessment decision, so they stay human.
4. **Consultant: a client asks, "Could Claude handle our customer onboarding?"** Suggested approach: map the onboarding steps with the client and mark which Claude can draft, summarize, or look up, and which need human judgment or system access. Route system integrations to a Claude Architect, and present the client with a pilot plan that names a human owner for each step.

## Check yourself

1. In a monthly reporting workflow, which step is the weakest candidate for delegation: drafting the narrative from agreed figures, reformatting into the new template, extracting the top five variances, or deciding which account to escalate to executives?
2. A team wants Claude to pull tickets from the help-desk system automatically every hour and post summaries to a channel. What should the Associate do?
3. **Pick two.** What makes a stakeholder description of an AI-assisted contract-review workflow credible? (a) Stating the bounded tasks Claude performs. (b) Calling it fully automated. (c) Naming the qualified human approver. (d) Leaving out limitations to keep it short.

<details>
<summary>Answers</summary>

1. Deciding which account to escalate. It carries accountability and relationship context, so it stays human.
2. Define the requirements and the human review step, then escalate the system integration to a Claude Developer or Architect (and IT). Building automated integrations is outside the Associate scope.
3. (a) and (c). Clear value, clear limits, and a named human create credibility.

</details>

## Official resources

- A closer look at Delegation (AI Fluency): https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-delegation
- Project planning and delegation (AI Fluency): https://academy.claude.com/courses/ai-fluency-framework-foundations/project-planning-and-delegation
- Tying it all together, the three-bucket audit (AI Fluency for Small Businesses): https://academy.claude.com/courses/ai-fluency-for-small-businesses/tying-it-all-together
- Human in the loop and AI-use policy (AI Fluency for Small Businesses): https://academy.claude.com/courses/ai-fluency-for-small-businesses/human-in-the-loop
- Building Effective Human-Agent Teams: https://academy.claude.com/courses/building-effective-human-agent-teams
- Claude in action: use cases by role (Claude 101): https://academy.claude.com/courses/claude-101/claude-in-action-use-cases-by-role
- Getting better results, validating before you trust (Claude 101): https://academy.claude.com/courses/claude-101/getting-better-results
- Official prep course, Workflow Integration & Solution Design: https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/workflow-integration-solution-design

---

**Next:** [Lesson 5: Projects and Knowledge Management](05-projects-and-knowledge-management.md)
