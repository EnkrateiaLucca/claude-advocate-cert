# Lesson 05: Projects and Knowledge Management

**Exam domain: D5 Configuration and Knowledge Management (12%)** · Time in session: about 12 minutes (Segment 3, after Lesson 04)

4Ds lens: **Description**. A Project is a description you write once so every later chat starts with the right context.

---

## 1. What the exam asks

The exam guide lists four objectives for this domain (verbatim):

- Configure Claude Projects with instructions and knowledge sources
- Manage uploaded knowledge and connectors (e.g., Google Drive, Gmail)
- Create effective system-level instructions
- Inform, maintain, and update Claude configurations, knowledge sources, and instructions

Expect about seven items. Most of them describe a team whose Project, instructions, or connector is set up badly and ask for the best fix.

---

## 2. Key ideas

### Where each piece of context belongs

Exam items often test placement. Learn this table.

| You want Claude to... | Put it in | Scope |
|---|---|---|
| Follow your company's house rules in every chat | Organization instructions (set by an admin on Enterprise) | Everyone in the org |
| Know who you are, your shorthand, your format preferences | Personal instructions in Settings | All your chats |
| Behave a certain way for one workstream (tone, process, format, guardrails) | **Project instructions** | Every chat in that Project |
| Know reference material for one workstream (style guide, policy, fact sheet) | **Project knowledge** | Every chat in that Project |
| Follow a repeatable procedure (format a quiz, apply brand rules to a deck) | **Skill** | Loads only when a request matches it |
| Read live or frequently changing files and email | **Connector** (Google Drive, Gmail, and others) | Whatever the connected account can see |
| Recall details from past conversations | **Memory** | Per Project, or global outside Projects |
| Handle today's one-off details (this client, this deadline) | The chat prompt | That message |

A short way to remember the middle rows: **instructions say how Claude should behave, knowledge says what Claude should know, and a Skill says how to do a repeatable task.** Anthropic's Claude 101 course puts it as "Projects store knowledge, skills perform tasks."

### Projects

A Project is a self-contained workspace with its own chat history, knowledge base, instructions, and memory. Use one when you have reference material you will reuse, a consistent output requirement, or teammates who need the same setup.

Setup has four parts:

1. **Name and description.** Claude does not see the description. It helps you and your teammates find the Project. Any rule you type into the description has no effect on Claude.
2. **Visibility** (private or shared, on Team and Enterprise plans).
3. **Instructions.** These shape every chat in the Project.
4. **Knowledge.** Uploaded files (PDF, DOCX, CSV, TXT, HTML and similar) or Google Drive documents.

Facts that show up in exam items:

- **Context isolation.** A file you upload inside one chat stays in that chat. Other chats in the same Project cannot see it. Add the file to Project knowledge if every chat needs it.
- **Retrieval mode.** When knowledge grows close to the context limit, Claude switches to searching the Project's files and pulling only the relevant parts. This expands capacity by up to 10x on paid plans, and the interface shows an indicator when it is on.
- **Name files descriptively.** "Travel-Policy-2026-10.pdf" helps Claude more than "policy.pdf". Refer to documents by name in your questions.
- **Sharing permissions** on Team and Enterprise: *Can view* (chat with the Project and use its knowledge), *Can edit* (change instructions and knowledge, manage members), and *Owner*.

### Effective system-level instructions

Project instructions act as system-level instructions for every chat in the Project. Strong instructions share five features:

| Feature | Weak | Strong |
|---|---|---|
| Role and context | "Be helpful." | "You draft replies for Acme's Tier 1 support agents." |
| Source rule | (none) | "Use only the attached help-center articles for product facts. If the answer is not there, say so." |
| Process | (none) | "Identify the customer's question, find the matching article, then draft." |
| Format | "Be concise." | "Under 150 words. End with one clear next step." |
| Conflict priority | "Be concise and comprehensive." | "If brevity and completeness conflict, keep every required fact and cut background." |

Two more habits help. Split rules into short labeled sections instead of one long paragraph. Keep instructions concise, because every chat in the Project carries them.

### Connectors

Connectors let Claude read information and take actions in other tools such as Google Drive, Gmail, and Google Calendar. They run on the Model Context Protocol (MCP). Know these behaviors:

- **Claude sees what you see.** A connector uses your own account permissions. Connecting your work email does not expose anyone else's inbox.
- **Scoped and revocable.** You grant permissions during setup and can disconnect at any time.
- **Approval before actions.** Gmail send, reply, and forward, and Drive share, move, and trash, ask for your approval before each action by default.
- **Google Drive works in private Projects only.** The Drive connector is not available in shared Projects.
- **Admins enable them first** on Team and Enterprise plans. A common pattern is read-only access first and write access later with sign-off from the risk owner.
- **Synced docs.** Google Docs added to chats and Projects sync to the latest version. Uploaded files do not update themselves.

Test a new connector with a plain question: "Can you access my Google Drive? List three files in the Marketing folder."

### Skills and memory

- **Skills** are folders of instructions and resources that Claude loads when a request matches the Skill's description. They need *Code execution and file creation* turned on in Settings. You can create one by describing the task to Claude in a conversation. Install custom Skills only from trusted sources.
- **Memory** saves details from your conversations. Each Project has its own memory space. You can view, edit, and delete memory in Settings. On Team and Enterprise plans, owners control whether memory is available. Memory helps continuity. It is not a source of truth, so keep authoritative facts in knowledge files.

### Maintaining configurations

Project knowledge does not update itself. Stale files produce confidently outdated answers.

- **Replace superseded documents.** Keeping both the old and new versions produces mixed answers.
- **Keep a small test set.** Write five to ten questions whose correct answers you know. Rerun them after every change.
- **Change one thing at a time** so you can tell which change helped or hurt.
- **Give each shared Project an owner** and a review rhythm, such as quarterly.
- **Turn repeated corrections into configuration.** If you type the same correction in every chat, move it into the instructions.

---

## 3. Exam traps

| Trap answer | Why it fails | Pattern |
|---|---|---|
| "Put the rule in the Project description." | Claude does not see the description. | Irrelevant fix |
| "Add the new policy alongside the old one." | Two versions compete. Replace the old file. | Fake safeguard |
| "Tell users to remind Claude which version to use." | It pushes the fix onto every user and every chat. Fix the knowledge base. | Irrelevant fix |
| "Upload the file in your chat so the whole team can use it." | Chat uploads stay in that chat. Use Project knowledge. | Irrelevant fix |
| "Connect the whole Drive and tell Claude to ignore the HR folders." | An instruction is not an access control. Scope the connection. | Fake safeguard |
| "Store the procedure as a knowledge file." | A repeatable procedure fits a Skill or instructions. Knowledge holds reference material. | Irrelevant fix |
| "Rebuild the Project from scratch." | A targeted update solves the problem with less risk. | Over-reaction |
| "Switch to the most capable model." | A configuration problem stays a configuration problem on any model. | Over-engineering |

---

## 4. Demo: Build the "Northwind content" Project

**Goal:** Configure a Project with knowledge and instructions, test it, then update it the right way.

**File:** `assets/demo-files/project-knowledge-brand-voice.md` (fictional brand rules for Northwind Learning)

**You need:** a Claude plan that includes Projects (Pro or higher recommended).

### Steps

**1. Create the Project.** In claude.ai, open **Projects** and choose **Create project**. Name it `Northwind content`. In the description field, type:

```
Drafts newsletter blurbs, LinkedIn posts, and course descriptions for Northwind Learning.
```

Point out to learners that Claude never reads this description.

**2. Add knowledge.** Open the Project's knowledge section and upload `project-knowledge-brand-voice.md`.

**3. Add instructions.** Open the Project instructions and paste:

```
You write marketing content for Northwind Learning.

Sources:
- Use the brand voice file in project knowledge for audience, voice, formats, and facts.
- Only state facts listed under "Facts we can state". If a request needs any other fact, write [CHECK: describe the fact] in its place and list every [CHECK] at the end.

Process:
1. Identify the asset type (newsletter blurb, LinkedIn post, or course description). If it is unclear, ask me one question before drafting.
2. Draft to the length and structure in the Formats table.
3. Check the draft against the "Never use" words and the "Facts we must NOT state" list. Fix any problem before you reply.

Output:
- The draft first.
- Then one line: "Word count: N · Asset: <type>".
```

**4. Test the happy path.** Start a chat inside the Project and send:

```
Write a LinkedIn post announcing our new course "Feedback That Lands", which teaches team leads how to give feedback in under five minutes.
```

**What good looks like:** 120 to 180 words. Structure follows Problem → example → takeaway → question. Second person ("you"), short sentences, none of the banned words. It ends with a question and shows the word-count line.

**5. Test the guardrails.** In the same chat, send:

```
Now write a newsletter blurb for the same course. Mention the price and say that graduates get a 20% salary increase.
```

**What good looks like:** Claude leaves out the price and the salary claim, or marks them with [CHECK]. It explains that the brand rules forbid pricing and salary-outcome claims and suggests linking to the pricing page. The blurb lands at 60 to 90 words.

**6. Test isolation.** Open a **new chat** in the same Project and ask:

```
How long are Northwind courses, and how many learners have we had?
```

**What good looks like:** "4 weeks, 2 hours per week, live online" and "12,000+ learners". Knowledge carries into every chat in the Project. Now upload any small file directly into this chat, open a third chat, and ask about that file. Claude cannot see it, because chat uploads stay in their chat.

**7. Update the knowledge the right way.** Northwind now has 15,000+ learners.

1. Open `project-knowledge-brand-voice.md` on your computer in any text editor.
2. Change `12,000+ learners` to `15,000+ learners`.
3. Save it under a dated name: `project-knowledge-brand-voice-2026-10.md`.
4. In the Project, **remove** the old file from knowledge, then upload the new one.
5. Rerun the question from step 6 in a new chat.

**What good looks like:** "15,000+ learners". If you had added the new file without removing the old one, answers could mix both numbers.

**8. Optional: description versus instructions.** Edit the Project description to add `Always end every post with #NorthwindLearns`. Run step 4 again. The hashtag does not appear. Move the same line into the instructions and rerun. Now it appears.

### Debrief

- Steps 2 and 3 cover *Configure Claude Projects with instructions and knowledge sources*.
- Step 3 shows *Create effective system-level instructions*: role, source rule, process, format, and a guardrail for missing facts.
- Steps 6 and 7 cover *Inform, maintain, and update Claude configurations*: replace the stale file, then retest with a known question.
- Step 8 is a classic exam distractor. A rule in the description does nothing.

---

## 5. Use cases to work through

**HR operations coordinator: policy Q&A.** Employees ask the same benefits and leave questions every week. *Suggested approach:* create a Project with the current handbook and benefits guide as knowledge, each named with a date. Instructions say: answer only from the attached policies, quote the section, and route anything about an individual case to HR. Keep ten test questions and rerun them whenever HR publishes a new version. Replace the old handbook instead of adding the new one beside it.

**Customer success lead: account hub.** Account notes live in Google Drive and change weekly. *Suggested approach:* use a private Project with the Drive connector so Claude reads current documents. Limit the connection to the account folders the lead already works in. Remember that the Drive connector does not work in shared Projects, so teammates who need the same setup should add exported files to a shared Project's knowledge or connect their own Drive in their own private Project.

**Instructional designer: quiz formatting.** She converts lesson notes into quizzes with the same layout every time and keeps retyping the rules. *Suggested approach:* turn the layout and steps into a Skill by describing the procedure to Claude and saving it. Keep the course content itself in Project knowledge. The Skill holds the *how* and the Project holds the *what*.

**Marketing team of five writers: inconsistent drafts.** Each writer pastes a different version of the style guide into chats. *Suggested approach:* one shared Project with one current style guide in knowledge, house tone and structure in instructions, and one named owner who updates both. Inconsistent teammates usually point to a missing shared setup.

---

## 6. Check yourself

**1.** A team lead types "Always cite the source document" into the Project description. Claude keeps answering without citations. What is the fix?

<details><summary>Answer</summary>

Move the rule into the Project instructions. Claude does not see the Project description, so rules placed there have no effect.

</details>

**2.** Your Project answers expense questions from last year's policy after Finance published a new one. You uploaded the new file yesterday. What did you miss, and how do you confirm the fix?

<details><summary>Answer</summary>

You left the old policy in knowledge, so two versions compete. Remove the old file and keep the new one, named with its date. Then rerun a few test questions whose answers changed between versions.

</details>

**3.** A colleague wants Claude to apply the same five-step review procedure to every vendor contract. Should the procedure go in Project knowledge, Project instructions, or a Skill?

<details><summary>Answer</summary>

A Skill fits a repeatable procedure that Claude should run whenever the task comes up. Project instructions also work if the procedure only applies inside one Project. Project knowledge holds reference material such as the contract templates, and it does not fit a procedure.

</details>

---

## 7. Official resources

- Anthropic Partner Academy prep course 5, *Configuration & Knowledge Management* (47 min): https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/configuration-knowledge-management
- Claude 101, *Introduction to Projects*: https://academy.claude.com/courses/claude-101/introduction-to-projects
- Claude 101, *Working with Skills*: https://academy.claude.com/courses/claude-101/working-with-skills
- Claude 101, *Connecting your tools*: https://academy.claude.com/courses/claude-101/connecting-your-tools
- Help center, *What are projects?*: https://support.claude.com/en/articles/9517075-what-are-projects
- Help center, *Use Google Workspace connectors*: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors
- Help center, Memory: https://support.claude.com/en/articles/11817273
- Exam Guide (v1.0): https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542847%2FClaude+Certified+Associate+%E2%80%93+Foundations+Exam+Guide.pdf

---

**Next:** [Lesson 06: Governance and Responsible Use](06-governance-and-responsible-use.md)
