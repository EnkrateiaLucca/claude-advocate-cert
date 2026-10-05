# Practice Questions: CCAO-F

Fifty original, scenario-based questions in the style of the Claude Certified Associate – Foundations exam. They are written for this course. None of them come from the live exam, whose content is confidential.

**How to use this bank**

- **Timed run:** answer all 50 in 100 minutes (2 minutes each, the same pace as the real exam). Open an answer only after you commit to your choice.
- **Domain drill:** do one domain at a time after the matching lesson.
- **Multiple-response items** say "Choose TWO". Score them all-or-nothing: you need both correct choices and no wrong ones.
- **Review every miss.** Label it Knowledge, Reading, or Judgment (see Lesson 08), and write down which distractor pattern caught you.

**Weighting.** The number of questions per domain follows the exam weights.

| Domain | Weight | Questions | Numbers |
|---|---|---|---|
| D1 Prompting and Task Execution | 14% | 7 | Q1–Q7 |
| D2 Output Evaluation and Validation | 21% | 11 | Q8–Q18 |
| D3 Product and Model Selection | 12% | 6 | Q19–Q24 |
| D4 Workflow Integration and Solution Design | 16% | 8 | Q25–Q32 |
| D5 Configuration and Knowledge Management | 12% | 6 | Q33–Q38 |
| D6 Governance, Risk, and Responsible Use | 15% | 8 | Q39–Q46 |
| D7 Troubleshooting and Optimization | 10% | 4 | Q47–Q50 |

**Distractor patterns** named in the explanations: *blind trust*, *fake safeguard*, *irrelevant fix*, *over-reaction*, and *over-engineering*. Lesson 08 describes each one.

**Readiness bands** (a rough guide that is not calibrated to the real exam's scaled score): 45–50 strong, 38–44 close, 30–37 keep studying your weakest domains, below 30 restart with the lessons.

---

## Domain 1: Prompting and Task Execution

### Q1

An HR coordinator types, "Write a welcome email for new hires." Claude returns a generic, upbeat email that could come from any company. She needs an email for remote software engineers starting Monday. It must cover laptop pickup, the first-day schedule, and who to contact with questions. What should she do next?

- A. Add "Make it great and very personalized" to the same prompt.
- B. Switch to the most capable model and resend the same prompt.
- C. Rewrite the prompt with the audience, the start date, the three required items, the tone, a length limit, and a past welcome email as an example.
- D. Regenerate the response three times and pick the best version.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Generic output signals missing context and constraints. C supplies the audience, the required content, tone, length, and an example, which are the parts of an effective business prompt.

- **A fails:** "Great" and "personalized" are vague intensifiers. They give Claude no new facts to personalize with. *(Irrelevant fix)*
- **B fails:** A more capable model still doesn't know about laptop pickup or Monday's schedule. *(Over-engineering)*
- **D fails:** Regenerating the same underspecified prompt produces different generic emails. *(Irrelevant fix)*

</details>

### Q2

A marketing manager asks, in one prompt, for a comparison of six competitors, a positioning recommendation, and a launch email. The comparison comes back shallow and the email is missing. What is the best approach?

- A. Split the work into steps: a comparison table on named criteria first, review it, then positioning options based on the table, then the email for the chosen position.
- B. Add "Be thorough and do not skip any part of this request" to the prompt.
- C. Paste the full text of all six competitors' websites into the same prompt.
- D. Ask Claude to make the response twice as long.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Task decomposition breaks a complex request into steps that each produce something you can check. Each later step builds on a reviewed earlier output, which also lets the manager catch errors early.

- **B fails:** An instruction to "be thorough" adds pressure without structure. The single prompt still asks for three different deliverables at once. *(Irrelevant fix)*
- **C fails:** More raw text in one prompt dilutes attention and makes the shallow-coverage problem worse. *(Over-engineering)*
- **D fails:** Length is not depth. A longer response can still skip the email. *(Irrelevant fix)*

</details>

### Q3

A program director asks Claude for a board update. The draft is accurate, but the funding request appears in paragraph four, and the board chair reads only the opening. Which follow-up is most effective?

- A. "Make it better for the board."
- B. Start a new chat and send the original prompt again.
- C. "Move the funding request and amount into the first two sentences. Cut the background section to three bullets. Keep every figure unchanged."
- D. "Rate this draft from 1 to 10 and fix anything below 8."

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Good iteration gives specific, checkable feedback. C names what to move, what to cut, and what must stay the same, so the accurate content survives the edit.

- **A fails:** "Better" gives no direction. Claude has to guess what the problem is. *(Irrelevant fix)*
- **B fails:** The same prompt is likely to produce the same structure. The draft was mostly right, so steering it is faster than restarting. *(Over-reaction)*
- **D fails:** A self-rating is not a reliable quality signal and does not tell Claude what the reader needs. *(Fake safeguard)*

</details>

### Q4

A team lead needs a name for a new internal mentoring program and has no strong ideas yet. Which prompting strategy fits this brainstorming task?

- A. Ask for 25 varied name ideas without filtering, then give Claude selection criteria in a second turn to narrow them to a shortlist of five.
- B. Ask Claude for the single best name with a one-paragraph justification.
- C. Turn on Research mode to find which program names other companies use most.
- D. Ask for a formal analysis of naming theory before any names are proposed.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Brainstorming works best as volume first, then narrowing. A separates idea generation from selection and adds criteria only once there is something to filter.

- **B fails:** A single answer cuts off exploration at the stage where options matter most.
- **C fails:** Research mode suits cited, multi-source reports. Copying other companies' popular names does not serve an original internal brand. *(Irrelevant fix)*
- **D fails:** A theory report delays the actual task and suits analysis more than brainstorming. *(Over-engineering)*

</details>

### Q5

An operations analyst must recommend one of three warehouse vendors to the COO. She has the three proposals as PDFs. Which prompt strategy best fits this analysis task?

- A. Ask "Which warehouse vendor is best?" without attaching the proposals, to get an unbiased view.
- B. Ask for a balanced discussion of the pros and cons of outsourcing warehousing.
- C. Ask for a persuasive email to the COO that favors the lowest-cost vendor.
- D. Attach the proposals, list the evaluation criteria and their weights, ask Claude to assess each vendor against each criterion with evidence from the proposals, and then give one recommendation with reasons.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** Analysis prompts work best with the sources attached, explicit criteria, reasoning before the conclusion, and evidence tied to the documents. D also asks for the decision the analyst actually needs.

- **A fails:** Without the proposals, Claude can only guess or invent vendor details. *(Blind trust)*
- **B fails:** The task needs a recommendation among three vendors. A balanced essay about outsourcing answers a different question. *(Irrelevant fix)*
- **C fails:** It skips the analysis and decides the answer in advance.

</details>

### Q6

A support lead asks Claude for a customer apology "under 100 words." Claude stays under 100 words but leaves out the refund amount and date, which the customer needs. What is the best next prompt?

- A. "UNDER 100 WORDS. FOLLOW THE INSTRUCTIONS."
- B. "The customer must know the refund amount ($240) and the date it will arrive (May 3). Keep it under 100 words by cutting the background instead."
- C. "Remove the word limit and include everything."
- D. Switch to a faster model and resend the original prompt.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** Claude followed the letter of the instruction and missed its purpose. The fix restates the goal (the customer must know the refund details) and tells Claude where to make room.

- **A fails:** Claude already met the word limit. Repeating it more loudly does not tell Claude what was missing. *(Irrelevant fix)*
- **C fails:** It throws away a useful constraint instead of resolving the conflict. *(Over-reaction)*
- **D fails:** A different model gets the same incomplete prompt. *(Irrelevant fix)*

</details>

### Q7

A project manager writes, "Summarize the attached 30-page retrospective." The summary is for executives. Which TWO additions would most improve the prompt? **(Choose TWO.)**

- A. "You are the world's greatest summarizer."
- B. "The readers are executives deciding whether to fund Phase 2. Focus on what affects that decision."
- C. "Be accurate."
- D. "Return at most five bullets, each naming a risk and its owner, followed by one recommendation."
- E. "Provide the summary in English, Spanish, and French."

<details><summary>Answer</summary>

**Answer: B, D**

**Why B and D win:** B gives audience and purpose, so Claude knows what to keep. D gives a concrete, checkable output format. Together they turn a vague request into a useful brief.

- **A fails:** Flattering role labels add no information about the task or the readers.
- **C fails:** "Be accurate" is a wish with no mechanism. Accuracy comes from grounding and verification.
- **E fails:** Nothing in the scenario asks for translations. It adds work without serving the executives.

</details>

---

## Domain 2: Output Evaluation and Validation

### Q8

Claude extracts action items from a 45-minute meeting transcript. The list has six neat items, each with an owner. Before sending it to attendees, which check best evaluates completeness?

- A. Ask Claude, "Did you capture every action item?"
- B. Read the parts of the transcript where decisions and commitments were made and compare them with the list.
- C. Reformat the list as a table so missing fields stand out.
- D. Rerun the extraction and keep whichever list is longer.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** Extraction usually fails by omission, and a tidy list hides what's missing. Comparing the output with the source is the only check that finds a missing commitment.

- **A fails:** Claude's yes is not independent evidence. *(Fake safeguard)*
- **C fails:** A table shows missing owners or dates for listed items. It cannot show items that were never listed. *(Irrelevant fix)*
- **D fails:** A longer list may contain duplicates or invented items. Length is not completeness. *(Blind trust)*

</details>

### Q9

Claude's summary of a vendor contract says, "The agreement auto-renews for three years (Clause 11.4)." The summary is going to the procurement director. The contract has only nine clauses. What should the associate do?

- A. Send the summary with a note that it was AI-generated and may contain errors.
- B. Ask Claude to double-check Clause 11.4 and send the summary if it confirms.
- C. Raise the effort setting and regenerate the summary.
- D. Treat the clause reference as fabricated, find the actual renewal terms in the contract, and correct the summary before sending.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** A citation to a clause that does not exist is a hallucination. Its claim may be wrong too. Verifying against the contract and correcting the summary is the diligence step before it reaches a decision-maker.

- **A fails:** A disclaimer passes a known error to the reader. *(Fake safeguard)*
- **B fails:** Claude checking itself is not independent verification. It may confirm the same error. *(Fake safeguard)*
- **C fails:** Regenerating does not verify anything. The new version needs the same check. *(Irrelevant fix)*

</details>

### Q10

A recruiter asks Claude to draft a job ad for a sales role. The draft asks for "digital natives" who will "fit our young, energetic team." What is the most appropriate response?

- A. Keep the wording, since Claude learned it from many real job ads.
- B. Ask Claude whether the ad is biased and publish it if Claude says no.
- C. Recognize the age-coded language as bias, revise the ad to describe the skills and behaviors the role needs, and follow the company's hiring-review process.
- D. Stop using Claude for job ads.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** "Digital natives" and "young" signal an age preference, which is a bias inherited from training data. C identifies it, fixes the wording to focus on job requirements, and keeps the normal human review for hiring content.

- **A fails:** Common wording can still be biased. Frequency in training data is not a quality signal. *(Blind trust)*
- **B fails:** Claude's self-assessment does not replace your own review. *(Fake safeguard)*
- **D fails:** Claude is useful for job ads when the output is reviewed. *(Over-reaction)*

</details>

### Q11

A market brief from Claude says in the executive summary that a segment grew 12%. The table in the body shows 21% for the same segment and year. What is the best action?

- A. Check both figures against the source data, correct the brief, and check the other figures in the brief for similar errors.
- B. Use the average of the two figures.
- C. Ask Claude which figure is correct and use its answer.
- D. Keep the executive-summary figure, because executives read that section.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** An internal inconsistency means at least one figure is wrong. Only the source data can settle it. One error also suggests others, so the rest of the figures need a check.

- **B fails:** The average of two unverified numbers is a third unverified number. *(Irrelevant fix)*
- **C fails:** Claude produced both figures. Its pick is not evidence. *(Fake safeguard)*
- **D fails:** Which section gets read says nothing about which number is right. *(Blind trust)*

</details>

### Q12

A communications specialist attaches a 60-page annual report and asks Claude for a fact sheet for journalists. Which instruction best supports fact-checking?

- A. "Rate your confidence in each fact from 1 to 10."
- B. "For each figure, quote the exact sentence from the report that supports it. Label any figure you cannot find in the report as UNSUPPORTED."
- C. "Write in a confident, authoritative tone."
- D. "Generate the fact sheet twice and keep only the figures that match."

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** Asking for direct quotes grounds each claim in the source and makes verification fast. Permission to say UNSUPPORTED removes pressure to fill gaps. The specialist still checks the quotes against the report.

- **A fails:** Self-rated confidence does not track accuracy. *(Fake safeguard)*
- **C fails:** Tone changes how claims sound. It does nothing for whether they are true. *(Irrelevant fix)*
- **D fails:** Two runs can agree on the same wrong figure. Agreement across runs is not verification. *(Fake safeguard)*

</details>

### Q13

Which Claude-assisted output most clearly needs review by a qualified person before it is used?

- A. A list of themes for a team offsite.
- B. A reformatted version of your own meeting notes.
- C. A draft agenda for a weekly stand-up.
- D. A letter to an insurance policyholder explaining why their claim is denied.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** Insurance decisions are a high-risk category in Anthropic's Usage Policy. The letter affects a person's money and rights, so a qualified professional must review it before it goes out.

- **A fails:** Offsite themes are low-stakes and internal. A quick glance is enough.
- **B fails:** You wrote the source and can spot changes yourself.
- **C fails:** An internal agenda is easy to fix and affects no one's rights.

</details>

### Q14

A product manager has a Claude summary of a software release written for engineers. She now needs a version for customer support agents. Which approach best adapts the output?

- A. Forward the engineering summary to the support team unchanged.
- B. Ask Claude to make the summary shorter.
- C. Ask Claude to rewrite it for support agents: what changed for customers, the questions customers will likely ask with suggested answers, and no internal ticket numbers. Then compare it with the original to confirm no facts changed.
- D. Ask Claude to make the summary more formal.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Adapting for an audience means changing content and framing to fit what that audience needs, then comparing versions so facts survive the rewrite. C does both.

- **A fails:** Engineering detail and ticket numbers don't help agents answer customers. *(Irrelevant fix)*
- **B fails:** Shorter text is not the same as audience-appropriate text. *(Irrelevant fix)*
- **D fails:** Formality does not address what support agents need to know. *(Irrelevant fix)*

</details>

### Q15

A team lead wants an onboarding checklist that she will revise over several weeks and share with new hires by link. Which output format fits best?

- A. An inline chat reply.
- B. An artifact.
- C. A CSV file.
- D. A long email draft.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** An artifact is a standalone deliverable that you can edit, reuse, and share. Those are the three requirements in the stem.

- **A fails:** Inline replies suit quick answers that you read once.
- **C fails:** Structured data suits output that feeds another tool. A checklist for people to read and revise needs a document.
- **D fails:** An email is hard to revise over weeks and cannot be shared as a living link.

</details>

### Q16

An operations analyst asks Claude to categorize 200 support tickets. The results will go straight into a spreadsheet pivot table. Which output should she request?

- A. A table with fixed columns: ticket ID, category (from a list she provides), and a one-line reason.
- B. A narrative paragraph for each category.
- C. A slide deck artifact with one slide per category.
- D. A bulleted list of highlights.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Output that feeds another step should be structured data with fixed fields. A fixed category list keeps labels consistent so the pivot table counts them correctly.

- **B fails:** Paragraphs must be re-keyed before any spreadsheet can use them.
- **C fails:** Slides suit presenting results, and this step only needs the data.
- **D fails:** Highlights drop most tickets and have no consistent fields.

</details>

### Q17

Claude's Research report includes a statistic attributed to "a 2025 industry survey," with a link. The statistic will appear in a client deck. Which TWO actions validate it? **(Choose TWO.)**

- A. Open the link and confirm the page exists and contains the statistic.
- B. Ask Claude, "Are you sure about this number?"
- C. Find the survey publisher's original report or a second independent source with the figure.
- D. Accept it, because Research mode added a citation.
- E. Change the figure to "approximately" so it is less precise.

<details><summary>Answer</summary>

**Answer: A, C**

**Why A and C win:** Citations make verification easier and do not replace it. Checking that the linked page says what the report claims (A) and tracing the figure to its original or an independent source (C) are both external checks.

- **B fails:** Claude's reassurance is not evidence. *(Fake safeguard)*
- **D fails:** A citation can point to a page that doesn't contain the claim. *(Blind trust)*
- **E fails:** A vaguer wrong number is still wrong. *(Irrelevant fix)*

</details>

### Q18

Which TWO outputs require review by a qualified human before use? **(Choose TWO.)**

- A. Icebreaker ideas for an internal workshop.
- B. Color palette suggestions for internal slides.
- C. A plain-language summary of a patient's lab results that a clinic will send to the patient.
- D. A reworded version of your own to-do list.
- E. A draft performance-improvement plan for a named employee.

<details><summary>Answer</summary>

**Answer: C, E**

**Why C and E win:** Healthcare (C) and employment (E) are high-risk categories. Each output affects a specific person's health or job, so a qualified professional must review it.

- **A fails:** Low stakes and internal. A skim is enough.
- **B fails:** Cosmetic and easy to change.
- **D fails:** Your own low-stakes notes, which you can check yourself.

</details>

---

## Domain 3: Product and Model Selection

### Q19

An event planner needs a cited comparison of five conference venues' accessibility policies, gathered from many websites. Which feature fits best?

- A. A plain chat that relies on Claude's training knowledge.
- B. A Project containing last year's venue brochures.
- C. An artifact built from what Claude already knows.
- D. Research mode, followed by spot-checks of the cited pages.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** Research mode searches many sources and returns a cited report, which matches a multi-source comparison of current policies. Spot-checking the citations completes the job.

- **A fails:** Training knowledge may be outdated or missing for specific venues, and it gives no citations. *(Blind trust)*
- **B fails:** Last year's brochures are stale for current policies. *(Irrelevant fix)*
- **C fails:** An artifact is an output format. It doesn't add current, cited information. *(Irrelevant fix)*

</details>

### Q20

A policy analyst must work through an 80-page impact assessment with conflicting assumptions and write one recommendation for leadership. Quality matters far more than speed, and there is only one document. Which choice fits best?

- A. The fastest, lowest-cost model, because the document is long.
- B. Whatever model the chat opened with, without checking.
- C. The most capable model tier, such as Opus, with a higher effort setting.
- D. Split the document into 80 one-page chats on the fastest model.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** The task is a single, high-stakes, complex reasoning job. That profile justifies the most capable tier and more effort, and the low volume keeps the cost reasonable.

- **A fails:** Length is not the deciding factor. Reasoning depth and quality are.
- **B fails:** Model choice should match the task, and this task has clear requirements.
- **D fails:** Splitting the document breaks the connections between conflicting assumptions, which is the core of the analysis. *(Over-engineering)*

</details>

### Q21

A content team uses the most capable model at maximum effort to reformat 300 product descriptions into a fixed template. They hit their usage limit by midday. What is the best adjustment?

- A. Move the reformatting to a faster, lower-cost model or a lower effort setting, test a sample for quality, and keep the top model for hard cases.
- B. Ask the admin to raise the team's limit and keep the current setup.
- C. Stop using Claude for product descriptions.
- D. Add "Work quickly" to the prompt.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Reformatting to a template is routine, high-volume work. A faster tier or lower effort fits it. Testing a sample confirms quality holds before the change goes wide.

- **B fails:** It pays for capability the task doesn't need. *(Over-engineering)*
- **C fails:** The task suits Claude well. Only the configuration is wrong. *(Over-reaction)*
- **D fails:** Prompt wording doesn't change which model or effort level runs the task. *(Irrelevant fix)*

</details>

### Q22

Three hours into a single chat building a training plan, Claude starts contradicting earlier decisions and drops the agreed format. What should the user do?

- A. Keep correcting Claude in the same chat until it settles.
- B. Ask Claude to summarize the decisions and format so far, start a new chat with that summary, and save the standing format rules in Project instructions.
- C. Switch to the fastest model to reduce confusion.
- D. Edit each earlier message to remove the old discussion.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** Long conversations drift as context fills up. B uses all three context moves: summarize what matters, restart clean, and persist stable rules where every future chat will see them.

- **A fails:** Each correction adds more text to an already overloaded conversation. *(Irrelevant fix)*
- **C fails:** A smaller model does not fix context overload. *(Irrelevant fix)*
- **D fails:** It is slow, error-prone, and still leaves the format rules unpersisted. *(Over-engineering)*

</details>

### Q23

Last week a consultant explained her firm's acronyms in a regular chat. Today, in a new chat outside any Project, Claude doesn't know them. Memory is turned off. What explains this, and what is the fix?

- A. Claude has a bug. Report it to support.
- B. The acronyms fall after Claude's training cutoff. Wait for a newer model.
- C. Use an Incognito chat so Claude keeps the context.
- D. A new chat starts without earlier conversations unless context is persisted. Add the acronym list to her personal instructions or to a Project.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** With memory off, each chat starts fresh. Claude does not learn from past conversations. Information that should carry across sessions needs a persistent home such as personal instructions, Project instructions, or Project knowledge.

- **A fails:** This is expected behavior.
- **B fails:** Training cutoff concerns public knowledge. Her firm's acronyms were never in training data, and a newer model wouldn't know them either.
- **C fails:** Incognito chats are not saved and not used by memory. It does the opposite of persisting context.

</details>

### Q24

Which TWO tasks fit a Claude Project better than a one-off chat? **(Choose TWO.)**

- A. Converting one recipe from cups to grams.
- B. A weekly client status report written from the same statement of work and style guide.
- C. Asking what a single acronym stands for.
- D. A grant application that several colleagues draft over a month using the same funder guidelines.
- E. A one-time thank-you note to a speaker.

<details><summary>Answer</summary>

**Answer: B, D**

**Why B and D win:** Projects suit recurring work with reusable reference material (B) and team collaboration on shared context (D).

- **A, C, and E fail:** Each is a one-time task with no reusable context. A regular chat is faster.

</details>

---

## Domain 4: Workflow Integration and Solution Design

### Q25

A head of customer success asks, "Can Claude run our renewal process?" What is the best first response?

- A. Yes. Connect Claude to the CRM and let it send renewal notices.
- B. No. Renewals involve money, so AI should stay out of them.
- C. Map the renewal process step by step and mark which steps Claude can draft or summarize, which need human judgment or approval, and which need system integration.
- D. Ask Claude whether it can run renewals and follow its answer.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** "Can Claude do X?" is answered with a division of labor. Mapping the steps shows where Claude helps, where people decide, and which integration work goes to Developers or Architects.

- **A fails:** It automates customer-facing, financial actions without analysis or review. *(Blind trust)*
- **B fails:** Many renewal steps, such as drafting reminders and summarizing account history, suit Claude well. *(Over-reaction)*
- **D fails:** Claude's opinion of its own fit is not a requirements analysis. *(Fake safeguard)*

</details>

### Q26

A product manager is planning a launch in three countries. How should she use Claude for research and planning?

- A. Ask Claude for a final go/no-go decision on each country.
- B. Use Research mode to gather each country's relevant regulations, verify the key sources, and have Claude draft a timeline with dependencies and assumptions flagged for owners to confirm.
- C. Have Claude email the local vendors to confirm dates.
- D. Skip planning and adjust as problems come up.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** Claude speeds up research and drafts a plan. People verify sources and confirm assumptions. B uses the right feature and keeps decisions with the owners.

- **A fails:** A go/no-go call carries accountability that stays with people. *(Blind trust)*
- **C fails:** External actions need human approval, and the plan doesn't exist yet. *(Over-engineering)*
- **D fails:** It abandons the planning task. *(Over-reaction)*

</details>

### Q27

A marketing team produces 12 social posts a week through four steps: research, drafting, legal review, and scheduling. Drafting takes the most time. Which integration is most proportionate?

- A. Claude drafts posts in a Project that holds the brand rules. A marketer edits each draft. Legal review and scheduling stay as they are.
- B. Claude drafts and publishes posts directly, skipping legal review to save time.
- C. Replace the whole workflow with an autonomous agent built this week.
- D. Keep the process fully manual until AI is perfect.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** It augments the bottleneck step and keeps the existing review controls. The Project keeps drafts consistent with brand rules.

- **B fails:** It removes a required control on public content. *(Blind trust)*
- **C fails:** A full redesign is out of proportion to a drafting bottleneck, and building agents belongs with Developers or Architects. *(Over-engineering)*
- **D fails:** "Perfect" is not the standard. Reviewed drafts are safe today. *(Over-reaction)*

</details>

### Q28

An operations coordinator spends four hours a week compiling a status report. The document's view history shows nobody has opened it in two months. What should happen before anyone automates it with Claude?

- A. Build a Project to automate the report right away.
- B. Use the most capable model so the report takes less time.
- C. Hand the report to a junior colleague.
- D. Confirm with the stakeholders whether the report is still needed and what they actually use.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** Process optimization starts with whether a step should exist. Automating an unused report makes waste faster.

- **A fails:** It automates before analyzing the requirement. *(Over-engineering)*
- **B fails:** It speeds up work that may be unnecessary. *(Over-engineering)*
- **C fails:** It moves the waste to someone else. *(Irrelevant fix)*

</details>

### Q29

An associate is briefing a VP on a pilot in which Claude drafts first answers to RFP questions. Which statement best communicates value and limits?

- A. "Claude now answers RFPs automatically, with no errors."
- B. "Claude drafts first answers from our approved content library. In the pilot, drafting time fell from six hours to two. A proposal manager reviews every answer, and pricing and legal terms stay with the proposal and legal teams."
- C. "AI carries risk, so we are keeping the pilot quiet until it is finished."
- D. "We use the latest model, so the quality is guaranteed."

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** A credible stakeholder message pairs a measured benefit with honest limits and names who reviews the work. B does all three.

- **A fails:** It overclaims. No AI output is error-free. *(Blind trust)*
- **C fails:** Hiding the pilot undermines trust and stops useful feedback. *(Over-reaction)*
- **D fails:** A newer model does not guarantee quality. *(Blind trust)*

</details>

### Q30

Marketing wants Claude to pull new leads from the CRM every night, score them, write the scores back to the CRM, and route hot leads to sales. What is the best step for an associate?

- A. Document the requirements and use case, then bring in a Claude Developer or Architect (or IT) to design the integration.
- B. Build it yourself with a Project and paste CRM exports into it each night.
- C. Tell marketing it cannot be done with Claude.
- D. Give Claude full write access to the CRM and test it in production.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Scheduled, automated integration with a business system is outside the Associate scope. The associate adds value by capturing requirements and escalating the build to the right specialists.

- **B fails:** A manual nightly paste is fragile, can't write back to the CRM, and stretches a Project past its purpose. *(Irrelevant fix)*
- **C fails:** The use case may be feasible with the right build. *(Over-reaction)*
- **D fails:** It grants broad write access to a live system without design or testing. *(Blind trust)*

</details>

### Q31

A support team is piloting Claude to draft replies to "How do I export my data?" tickets. Which TWO practices fit a sound rollout? **(Choose TWO.)**

- A. Start with that one ticket category and compare handle time and quality against a baseline before expanding.
- B. Turn on automatic sending for all ticket categories on day one.
- C. Measure success by the number of prompts the team sends.
- D. Have agents review each draft before sending until accuracy is proven.
- E. Skip the baseline measurement, since Claude is obviously faster.

<details><summary>Answer</summary>

**Answer: A, D**

**Why A and D win:** Pilot one workflow, measure against a baseline, and expand trust step by step. Human review stays in place until the drafts prove reliable.

- **B fails:** It grants full autonomy before any evidence. *(Blind trust)*
- **C fails:** Usage counts show activity. They don't show outcomes.
- **E fails:** Without a baseline you cannot show the value to stakeholders.

</details>

### Q32

A training manager is designing a new onboarding curriculum with Claude. Which TWO uses of Claude support solution design and iteration? **(Choose TWO.)**

- A. Have Claude approve the curriculum budget.
- B. Ask Claude to confirm the curriculum meets employment law and skip the legal check.
- C. Ask Claude to propose two different module sequences with trade-offs, then pilot one with a small group of new hires.
- D. Publish Claude's first draft to all employees immediately.
- E. Ask Claude to critique the draft from the viewpoints of a new hire and a busy hiring manager, then revise.

<details><summary>Answer</summary>

**Answer: C, E**

**Why C and E win:** Generating alternatives, testing one, and critiquing drafts from user viewpoints are design-and-iterate uses. The manager stays in charge of decisions.

- **A fails:** Budget approval is an accountable decision for a person.
- **B fails:** Legal compliance needs a qualified reviewer. *(Blind trust)*
- **D fails:** It skips iteration and review. *(Blind trust)*

</details>

---

## Domain 5: Configuration and Knowledge Management

### Q33

A content lead creates a Project and types in the project description: "Use British spelling and keep posts under 150 words." Claude ignores both rules. What is the cause, and what is the fix?

- A. The model is too small. Switch to the most capable model.
- B. Claude does not support British spelling. Edit each post by hand.
- C. Claude does not see the project description. Move the rules into the Project instructions.
- D. The knowledge base is too large. Delete some files.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** The project description helps people find and understand the Project. Claude does not read it. Rules belong in the Project instructions.

- **A fails:** No model reads the description. *(Over-engineering)*
- **B fails:** Claude handles British spelling when instructed. *(Irrelevant fix)*
- **D fails:** Knowledge size has nothing to do with where the rules were typed. *(Irrelevant fix)*

</details>

### Q34

A Project still answers questions using last year's travel policy, even though Finance published a new one. What is the best fix?

- A. Upload the new policy alongside the old one.
- B. Tell users to start each question with "Use the new policy."
- C. Delete the Project and build a new one.
- D. Replace the old policy file with the new one, named with its date, then test with questions whose answers changed.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** Project knowledge does not update itself. Replacing the superseded file removes the conflict, a dated name helps Claude and people, and targeted test questions confirm the fix.

- **A fails:** Two versions compete and produce mixed answers. *(Fake safeguard)*
- **B fails:** It pushes the fix onto every user and every chat. *(Irrelevant fix)*
- **C fails:** One file is the problem. Rebuilding loses the working instructions. *(Over-reaction)*

</details>

### Q35

In a shared Project, a colleague uploaded the current price list into one of her chats. In your chat in the same Project, Claude says it has no price list. Why?

- A. Files uploaded in a chat stay in that chat. Add the price list to Project knowledge so every chat can use it.
- B. You have view-only permission, so Claude hides files from you.
- C. Claude has reached its context limit.
- D. Claude refuses to share information between users.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Context isolation: chats in a Project share only the Project knowledge and instructions. A file uploaded in one chat stays there.

- **B fails:** View permission still lets you use the Project's knowledge. The file was never in knowledge.
- **C fails:** Nothing in the scenario suggests a long conversation.
- **D fails:** This is how chat uploads work. It is not a refusal.

</details>

### Q36

A team lead is writing instructions for a Project that support agents use to draft replies. Which instruction is most effective?

- A. "Be helpful, friendly, and accurate."
- B. "You draft replies for Acme support agents. Use only the attached help-center articles for product facts. If the answer is not in them, say so and suggest escalating to Tier 2. Keep replies under 150 words and end with one clear next step."
- C. "Answer like a world-class expert."
- D. "NEVER MAKE MISTAKES."

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** It sets a role, a source rule, a fallback for missing information, a concrete length, and a required ending. Each part is specific and checkable.

- **A fails:** These are adjectives with nothing to act on.
- **C fails:** A grand role label adds no context, sources, or format.
- **D fails:** Capital letters add pressure without a mechanism. Grounding and a fallback rule prevent errors.

</details>

### Q37

A coordinator wants to connect Google Drive so Claude can use team documents. A colleague worries that Claude could then read confidential HR folders. Which statement is accurate?

- A. The connector uses the coordinator's own permissions, so Claude can reach only what she can access. She should connect only what the task needs and follow org policy.
- B. Claude can read every file in the company's Drive once any user connects.
- C. Connecting Drive automatically adds all files to model training data.
- D. A connector cannot be disconnected once it is set up.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Connectors inherit the user's own access: Claude sees what you see. Scoping the connection to the task and following policy addresses the remaining risk.

- **B fails:** Connectors do not expand access beyond the user's permissions.
- **C fails:** Connecting a tool does not change data-training terms.
- **D fails:** Connectors can be revoked at any time.

</details>

### Q38

A team Project drafts client newsletters. Which TWO items belong in the Project instructions? **(Choose TWO.)**

- A. The name of the client for this month's issue.
- B. The house tone and the required section order for every newsletter.
- C. The 40-page product catalog.
- D. A note that this month's issue is running late.
- E. "Only state statistics that appear in the attached fact sheet. If a statistic is missing, flag it."

<details><summary>Answer</summary>

**Answer: B, E**

**Why B and E win:** Instructions hold how Claude should behave in every chat: standing tone and structure (B) and guardrails on sources (E).

- **A fails:** This month's client is a one-off detail for the chat prompt.
- **C fails:** Reference material belongs in Project knowledge.
- **D fails:** A temporary note belongs in the chat prompt. Standing instructions should hold only rules that apply every time.

</details>

---

## Domain 6: Governance, Risk, and Responsible Use

### Q39

A finance analyst wants Claude to look for unusual payments in a spreadsheet that includes vendor bank account numbers and contact names. Company policy restricts sharing financial identifiers. What should he do?

- A. Upload the file and tell Claude not to store it.
- B. Upload the file, since the analysis is internal.
- C. Replace the bank account numbers and contact names with codes, keep the lookup key on his own computer, and upload the coded file.
- D. Skip the analysis.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Pseudonymizing the identifiers satisfies the policy and keeps the payment patterns intact for analysis. The local key lets him trace findings back afterward.

- **A fails:** An instruction to Claude is not a policy control. The data has already been shared. *(Fake safeguard)*
- **B fails:** Internal purpose does not override the data policy. *(Blind trust)*
- **D fails:** A compliant path exists. *(Over-reaction)*

</details>

### Q40

A manager asks Claude to decide which of four employees should be laid off, based on performance notes. What is the most appropriate approach?

- A. Let Claude decide, because it is objective.
- B. Anonymize the notes, then let Claude decide.
- C. Refuse to use Claude for any HR work.
- D. Use Claude to organize the notes against the agreed criteria, while the manager and HR make and own the decision.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** Employment decisions are high-risk and need an accountable human. Claude can still help by structuring the evidence.

- **A fails:** Claude can carry bias and cannot hold accountability. *(Blind trust)*
- **B fails:** Anonymizing addresses privacy. It does not make the decision appropriate to delegate. *(Fake safeguard)*
- **C fails:** Many HR tasks, such as drafting policies or organizing notes, are appropriate. *(Over-reaction)*

</details>

### Q41

Company AI policy allows only the company's Team workspace for client work. A colleague prefers his personal Pro account because it feels faster. What is the right approach?

- A. Use the company workspace. If it lacks something the work needs, raise a request with the policy owner.
- B. Use the personal account in an Incognito chat.
- C. Use the personal account after turning off the model-improvement setting.
- D. Use the personal account for drafts and the company workspace for final versions.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Following organizational policy means using the approved workspace. If it falls short, the fix is a request through the policy owner.

- **B fails:** Incognito does not make an unapproved account approved. *(Fake safeguard)*
- **C fails:** A personal privacy setting does not override company policy. *(Fake safeguard)*
- **D fails:** Drafts contain the same client data. *(Fake safeguard)*

</details>

### Q42

A consultant used Claude to draft most of a client market report. The client contract requires disclosure of AI tools. What should she do?

- A. Say nothing, because she edited the draft.
- B. Include a short diligence statement: what Claude helped with, what she verified and changed, and that she is responsible for the final report.
- C. Mention AI only if the client asks.
- D. Remove phrasing that sounds AI-written so disclosure isn't needed.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** The contract requires disclosure, and a diligence statement meets it honestly while making clear who is accountable.

- **A fails:** Editing does not remove the contractual duty to disclose.
- **C fails:** The contract already asks. Waiting breaks it.
- **D fails:** Hiding AI involvement is deceptive, whatever the wording.

</details>

### Q43

A marketing specialist on a personal Pro plan asks whether her chats can be used to train Anthropic's models. Which answer is accurate?

- A. No. Paid plans are never used for training.
- B. Only uploaded files can be used. Typed messages never are.
- C. Pro is a consumer plan, so she chooses the model-improvement setting in her privacy settings. For work data, she should also follow her company's policy on approved plans.
- D. She can prevent it by typing "Do not train on this" at the start of each chat.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Free, Pro, and Max are consumer plans with a user-controlled model-improvement setting. Commercial plans such as Team and Enterprise don't train on data by default. Company policy still decides which plan she may use for work.

- **A fails:** Paying for Pro does not make it a commercial plan.
- **B fails:** The setting covers conversations as well as files. The claim is invented.
- **D fails:** An instruction in the chat is not a privacy control. *(Fake safeguard)*

</details>

### Q44

A lender's operations team wants Claude to draft letters that explain loan declines to applicants. What does Anthropic's Usage Policy require for this use?

- A. Nothing extra, because the letters are only text.
- B. Using the most capable model for every letter.
- C. Adding a line that says the letter may contain errors.
- D. Review by a qualified professional before the letters are sent, and disclosure that AI was involved.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** Finance and lending is a high-risk use case. The Usage Policy requires a qualified human in the loop and disclosure of AI involvement.

- **A fails:** The letters affect people's access to credit, whatever their format. *(Blind trust)*
- **B fails:** Model choice does not meet the review requirement. *(Over-engineering)*
- **C fails:** An error disclaimer is neither review nor proper disclosure. *(Fake safeguard)*

</details>

### Q45

A team deleted the name and email columns from a customer feedback file before uploading it. Which TWO risks should they still check? **(Choose TWO.)**

- A. Free-text comments that mention names, order numbers, or addresses.
- B. The file extension of the spreadsheet.
- C. The font used in the spreadsheet.
- D. Rare combinations of fields, such as a small town, a job title, and an exact date, that could point to one person.
- E. The number of rows in the file.

<details><summary>Answer</summary>

**Answer: A, D**

**Why A and D win:** Removing direct identifier columns is incomplete anonymization. Free text often contains identifiers (A), and rare combinations of ordinary fields can re-identify people (D).

- **B, C, and E fail:** None of these affects whether a person can be identified.

</details>

### Q46

A marketing intern asks Claude to write five customer testimonials for a new website because "we don't have any yet." Which TWO responses are appropriate? **(Choose TWO.)**

- A. Publish the testimonials with first names only.
- B. Decline to publish invented testimonials as if real customers wrote them.
- C. Use Claude to draft an email asking real customers for feedback and permission to quote them.
- D. Label the invented testimonials "representative" and publish them.
- E. Ask Claude to make the testimonials sound more realistic.

<details><summary>Answer</summary>

**Answer: B, C**

**Why B and C win:** Invented testimonials deceive customers. Declining (B) avoids the harm, and drafting an outreach email (C) keeps the work moving with real input.

- **A fails:** First names make fake quotes look more real. *(Blind trust)*
- **D fails:** "Representative" still presents invented praise as customer opinion. *(Fake safeguard)*
- **E fails:** It makes the deception more convincing.

</details>

---

## Domain 7: Troubleshooting and Optimization

### Q47

A Project has produced good weekly newsletters for months. This week's draft includes pricing, which the brand rules forbid. Nobody edited the instructions. What is the best first step?

- A. Rewrite the Project instructions from scratch.
- B. Check what changed in the Project, starting with recently added or edited knowledge files.
- C. Switch to the most capable model.
- D. Build a new Project.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** When something that worked breaks, find what changed before rewriting anything. A new or outdated knowledge file that lists pricing is the likely cause.

- **A fails:** The instructions worked for months. Rewriting them adds a new variable. *(Over-reaction)*
- **C fails:** A model upgrade doesn't remove conflicting knowledge. *(Over-engineering)*
- **D fails:** It discards a working setup without diagnosis. *(Over-reaction)*

</details>

### Q48

The sales team says Claude's follow-up emails are "too long." Each rep types "shorter" in every chat. What is the best adjustment?

- A. Keep correcting in each chat, since Claude learns from the corrections.
- B. Switch to the fastest model, because it writes shorter emails.
- C. Ask reps to edit every email by hand.
- D. Add a concrete rule to the team Project instructions, such as "Under 120 words: one recap line, one next step, one question", then check a sample of new emails with the team.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** Repeated feedback should become standing configuration. A concrete limit replaces a vague complaint, and checking a sample confirms the change worked.

- **A fails:** Claude does not learn from corrections across chats. *(Blind trust)*
- **B fails:** Model tier does not reliably control length. The prompt does. *(Irrelevant fix)*
- **C fails:** It moves the work back to people and leaves the cause in place. *(Over-reaction)*

</details>

### Q49

Every Monday an analyst opens a new chat, pastes the same three background documents, and asks for a ticket summary on the most capable model at maximum effort. It takes 40 minutes. What is the best optimization?

- A. Drop the summary to save time.
- B. Switch to an even more capable model.
- C. Move the background documents into a Project, save the request as a template with a fixed output table, and test whether a mid-tier model at normal effort keeps the same quality.
- D. Write a longer and more detailed prompt each week.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** It removes repeated setup, standardizes the output, and right-sizes the model with a quality check. Time and cost drop while quality holds.

- **A fails:** Nothing suggests the summary is unused. *(Over-reaction)*
- **B fails:** More capability adds cost to a routine task. *(Over-engineering)*
- **D fails:** It adds work every week instead of reusing it. *(Irrelevant fix)*

</details>

### Q50

Claude's supplier-audit summaries got worse after the team made three changes on the same day: a new model, revised instructions, and three new knowledge files. Which TWO steps follow a sound troubleshooting approach? **(Choose TWO.)**

- A. Make more changes now to find a fix faster.
- B. Set effort to maximum and hope the quality returns.
- C. Delete the Project and start over.
- D. Return to the last known-good setup and reintroduce one change at a time.
- E. Rerun the same set of past audits with known-good summaries after each change and compare.

<details><summary>Answer</summary>

**Answer: D, E**

**Why D and E win:** Changing one variable at a time (D) isolates the cause. A fixed test set (E) shows whether each change helps or hurts.

- **A fails:** More simultaneous changes make the cause harder to find. *(Over-engineering)*
- **B fails:** It guesses at a fix without diagnosis. *(Irrelevant fix)*
- **C fails:** It throws away the working parts along with the broken one. *(Over-reaction)*

</details>

---

## Answer key

Objective numbers follow the order of objectives in the exam guide (for example, 2.3 is the third objective in Domain 2).

| Q | Answer | Domain | Objective |
|---|---|---|---|
| 1 | C | D1 | 1.1 Create effective prompts for business and technical tasks |
| 2 | A | D1 | 1.2 Apply task decomposition techniques to structure complex requests |
| 3 | C | D1 | 1.3 Iterate prompts to improve output quality |
| 4 | A | D1 | 1.4 Adapt prompting strategies based on task type (analysis, research, drafting, brainstorming) |
| 5 | D | D1 | 1.4 Adapt prompting strategies based on task type (analysis, research, drafting, brainstorming) |
| 6 | B | D1 | 1.3 Iterate prompts to improve output quality |
| 7 | B, D | D1 | 1.1 Create effective prompts for business and technical tasks |
| 8 | B | D2 | 2.1 Evaluate Claude-generated outputs for accuracy and completeness |
| 9 | D | D2 | 2.2 Identify hallucinations, inconsistencies, and biases in responses |
| 10 | C | D2 | 2.2 Identify hallucinations, inconsistencies, and biases in responses |
| 11 | A | D2 | 2.2 Identify hallucinations, inconsistencies, and biases in responses |
| 12 | B | D2 | 2.3 Apply fact-checking and validation techniques |
| 13 | D | D2 | 2.4 Determine when human review or additional verification is required |
| 14 | C | D2 | 2.5 Edit, adapt, refine, and compare outputs for the intended audience |
| 15 | B | D2 | 2.6 Organize and curate information and select appropriate output formats (artifacts, inline, structured data) |
| 16 | A | D2 | 2.6 Organize and curate information and select appropriate output formats (artifacts, inline, structured data) |
| 17 | A, C | D2 | 2.3 Apply fact-checking and validation techniques |
| 18 | C, E | D2 | 2.4 Determine when human review or additional verification is required |
| 19 | D | D3 | 3.1 Select appropriate Claude product features (Projects, research mode, chat, artifacts) |
| 20 | C | D3 | 3.2 Differentiate between Claude model types (Haiku, Sonnet, Opus) |
| 21 | A | D3 | 3.3 Align model selection with task requirements (cost, speed, quality) |
| 22 | B | D3 | 3.4 Understand and manage context limitations and memory considerations (when to restart, summarize, or persist) |
| 23 | D | D3 | 3.4 Understand and manage context limitations and memory considerations (when to restart, summarize, or persist) |
| 24 | B, D | D3 | 3.1 Select appropriate Claude product features (Projects, research mode, chat, artifacts) |
| 25 | C | D4 | 4.1 Apply Claude to analyze requirements and use cases |
| 26 | B | D4 | 4.2 Leverage Claude for research, planning, and process optimization |
| 27 | A | D4 | 4.4 Integrate Claude into existing workflows to augment or redesign them |
| 28 | D | D4 | 4.2 Leverage Claude for research, planning, and process optimization |
| 29 | B | D4 | 4.5 Communicate Claude's value and limitations to stakeholders |
| 30 | A | D4 | 4.1 Apply Claude to analyze requirements and use cases |
| 31 | A, D | D4 | 4.4 Integrate Claude into existing workflows to augment or redesign them |
| 32 | C, E | D4 | 4.3 Use Claude to support solution design, development, and iteration |
| 33 | C | D5 | 5.1 Configure Claude Projects with instructions and knowledge sources |
| 34 | D | D5 | 5.4 Inform, maintain, and update Claude configurations, knowledge sources, and instructions |
| 35 | A | D5 | 5.2 Manage uploaded knowledge and connectors (e.g., Google Drive, Gmail) |
| 36 | B | D5 | 5.3 Create effective system-level instructions |
| 37 | A | D5 | 5.2 Manage uploaded knowledge and connectors (e.g., Google Drive, Gmail) |
| 38 | B, E | D5 | 5.3 Create effective system-level instructions |
| 39 | C | D6 | 6.2 Apply data sensitivity, regulatory, and privacy considerations |
| 40 | D | D6 | 6.1 Identify appropriate and inappropriate use cases |
| 41 | A | D6 | 6.3 Follow organizational AI policies and governance standards |
| 42 | B | D6 | 6.4 Understand the ethical implications of AI usage |
| 43 | C | D6 | 6.2 Apply data sensitivity, regulatory, and privacy considerations |
| 44 | D | D6 | 6.1 Identify appropriate and inappropriate use cases |
| 45 | A, D | D6 | 6.2 Apply data sensitivity, regulatory, and privacy considerations |
| 46 | B, C | D6 | 6.4 Understand the ethical implications of AI usage |
| 47 | B | D7 | 7.1 Identify, diagnose, and resolve issues with underperforming prompts or poor outputs |
| 48 | D | D7 | 7.2 Adjust approach based on feedback and results |
| 49 | C | D7 | 7.3 Optimize workflows for efficiency and effectiveness |
| 50 | D, E | D7 | 7.1 Identify, diagnose, and resolve issues with underperforming prompts or poor outputs |

**Single-answer distribution:** A 10, B 10, C 10, D 10. **Multiple-response items:** Q7, Q17, Q18, Q24, Q31, Q32, Q38, Q45, Q46, Q50.

---

**Back to:** [Lesson 00: The Exam Blueprint](00-exam-blueprint.md)
