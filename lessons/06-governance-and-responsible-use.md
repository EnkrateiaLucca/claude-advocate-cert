# Lesson 06: Governance and Responsible Use

**Exam domain: D6 Governance, Risk, and Responsible Use (15%)** · Time in session: about 9 minutes (Segment 4)

4Ds lens: **Diligence**. You decide what is safe to bring to Claude, you stay honest about its role, and you take responsibility for what you ship.

---

## 1. What the exam asks

The exam guide lists four objectives for this domain (verbatim):

- Identify appropriate and inappropriate use cases
- Apply data sensitivity, regulatory, and privacy considerations
- Follow organizational AI policies and governance standards
- Understand the ethical implications of AI usage

Expect about nine items. Official Sample Question 3 shows the pattern. A project manager wants to upload customer names and account numbers. The right answer removes or anonymizes the identifiers first, then runs the analysis.

---

## 2. Key ideas

### The governance rule of thumb

**Make the task safe, then do it.** The exam rewards the proportionate step that lets work continue within policy. It penalizes three other moves: going ahead unsafely, adding a fake safeguard, and abandoning the task.

### Appropriate and inappropriate use cases

Sort every task into one of three buckets before you start.

| Bucket | Typical tasks | What you do |
|---|---|---|
| **Claude can handle** | Standard replies from documented information, reformatting, summarizing your own notes, brainstorming | Delegate, then spot-check |
| **Claude assists, a human decides** | Drafting customer letters, analyzing survey results, preparing a hiring rubric | Claude drafts. A person reviews and owns the result |
| **A human handles** | Decisions about a specific person's job, pay, health, credit, or legal standing; emotionally sensitive conversations | Claude may organize inputs. A qualified person makes the call |

Anthropic's Usage Policy names **high-risk use cases** where output affects people's rights or wellbeing: legal, healthcare, insurance, finance and lending, employment and housing, academic testing and admissions, and media and journalism. These need **a qualified professional in the loop** to review content or decisions, and **disclosure** that AI was involved. Consumer-facing chatbots must also tell users they are talking to AI.

### Data sensitivity and anonymization

Before you upload anything, ask three questions:

1. **What kind of data is this?** Public, internal, confidential, or regulated personal data (names, contact details, account numbers, health or financial records).
2. **What does my organization's policy allow** for this data class and this tool?
3. **What does the task actually need?** Most analysis needs patterns. It rarely needs names.

Then minimize and anonymize:

| Technique | Example |
|---|---|
| **Remove** columns the task does not need | Delete `customer_name` and `email` |
| **Replace** identifiers with codes (pseudonymize) | `AC-40021` becomes `C001`. Keep the lookup key on your own machine |
| **Generalize** precise values | `2025-02-11` becomes `2025-02` |
| **Scrub free text** | Comments can contain names, order numbers, and locations |
| **Check rare combinations** | "Only Enterprise customer in LATAM" can still point to one company |

**Fake safeguards** that the exam treats as wrong:

- "Upload it and tell Claude not to retain it." An instruction to the model is not a policy control. The data has already left your hands.
- "Use an Incognito chat." Incognito chats are not saved to your history, but they still follow your organization's retention policy, and the data was still shared.
- "It's internal" or "Legal asked for it." Neither the purpose nor the requester's seniority overrides policy.
- "Add a disclaimer." A disclaimer does not make inaccurate or non-compliant content acceptable.

### Data retention and training settings by plan

You follow these settings. Admins and policy owners set them. Verify current terms at Anthropic's privacy pages before relying on them, because terms change.

| Plan type | Training on your chats | Notes |
|---|---|---|
| Free, Pro, Max (consumer plans) | You choose in Privacy Settings | If you allow model improvement, data is kept up to 5 years. If you opt out, standard retention is 30 days. Paying for Pro or Max does not change this choice |
| Team, Enterprise, Education, API (commercial plans) | Not used for training by default | Enterprise admins can set custom retention (30-day minimum). Admins control memory and connectors |
| Incognito chat (all plans) | Same as your plan | Not saved to history and not used by memory. Still subject to org retention |

### Organizational AI policies

Your company's AI policy usually covers four things: approved tools and workspaces, which data classes may go into them, which outputs need review, and how to disclose AI use. As a candidate you are expected to **follow** it.

- Use the approved workspace for work data, even when a personal account looks faster.
- When the approved setup lacks something you need, ask the policy owner. Do not work around the policy.
- When Claude declines a request and explains why, treat the refusal as information about a limit. Do not rephrase the request to slip past it.
- When you see a gap between policy and practice (for example, colleagues pasting client files into personal accounts), report it and help make the approved path easier to use.

### Ethics: bias, fabrication, accountability, disclosure

- **Bias.** Claude can reproduce stereotypes from its training data. Watch for coded language in job ads ("digital native", "young team"), one-sided framing, and generalizations about groups. Ask Claude to review for bias, then review it yourself.
- **Fabrication.** Never ask Claude to invent testimonials, reviews, quotes, or data and present them as real.
- **Accountability.** The person who sends or files the work owns it. Using Claude does not transfer responsibility.
- **Disclosure.** Tell people about AI's role when it would change how they judge the work, when a contract or policy requires it, and always in high-risk use cases. Anthropic's AI Fluency course suggests a **diligence statement** with five elements: what AI helped with, which tool, what you reviewed, what you changed, and who is responsible.
- **Claude's own design.** Anthropic trains Claude with Constitutional AI to be helpful, harmless, and honest. That training reduces risk. It does not replace your judgment.

---

## 3. Exam traps

| Trap answer | Why it fails | Pattern |
|---|---|---|
| "Upload as-is, the analysis is internal." | Internal use does not change the data's sensitivity. | Blind trust |
| "Upload and instruct Claude not to retain the data." | An instruction is not a control. | Fake safeguard |
| "Use Incognito so nothing is stored." | Incognito still follows org retention, and the data was shared anyway. | Fake safeguard |
| "Skip the analysis entirely." | Anonymization makes the task possible. | Over-reaction |
| "Ban AI for the whole team." | A proportionate control exists. | Over-reaction |
| "Let Claude make the hiring decision because it is objective." | Decisions about people need a qualified human who owns them. | Blind trust |
| "Anonymize the notes, then let Claude decide." | Anonymizing fixes privacy. It does not fix accountability. | Fake safeguard |
| "Use your personal Pro account and turn off training." | The org policy decides the workspace, whatever the setting. | Fake safeguard |
| "Escalate every Claude request to Legal." | Review effort should match the stakes. | Escalate everything |

---

## 4. Demos

### Demo A: Anonymize, then analyze churn

**Goal:** Practice the Sample Question 3 pattern. Remove identifiers before upload, then analyze the anonymized data and verify one result yourself.

**Files:** `assets/demo-files/customer-accounts.csv` (contains fake names, account numbers, and emails) and `assets/demo-files/customer-accounts-anonymized.csv`

#### Steps

**1. Inspect the raw file locally. Do not upload it.** Open `customer-accounts.csv` in a spreadsheet app. Point out the three identifier columns (`customer_name`, `account_number`, `email`) and the exact `signup_date`. Treat this file as if your policy restricts sharing customer personal data.

**2. Ask Claude for an anonymization plan using only the header and a made-up row.** Start a new chat and paste:

```
I need to analyze customer churn with you. My company policy does not allow me to upload customer names, emails, or account numbers. Below is the header row of my spreadsheet and one made-up example row. Do not analyze anything yet.

customer_name,account_number,email,region,plan,signup_date,monthly_spend_usd,support_tickets_90d,nps,churned
Jane Example,AC-00000,jane@example.com,EMEA,Pro,2025-02-11,420,1,9,no

For each column, tell me whether to keep it, remove it, replace it with a code, or generalize it, with a one-line reason. Then list any re-identification risks I should check before I upload the anonymized file. The file has 16 rows.
```

**What good looks like:** remove `customer_name` and `email`. Replace `account_number` with a neutral code and keep the lookup key outside Claude. Generalize `signup_date` to month. Keep the analysis columns. A strong answer also warns that a small file with exact spend amounts can single out a large customer.

**3. Anonymize the file yourself.** Do this in your spreadsheet app, outside Claude: delete the name and email columns, replace account numbers with `C001`, `C002`, and so on, and change dates to year-month. Compare your result with `customer-accounts-anonymized.csv`. Discuss one open question: should `monthly_spend_usd` be grouped into bands? (The single LATAM Enterprise account has a distinctive spend figure.)

**4. Upload the anonymized file and analyze.** Upload `customer-accounts-anonymized.csv` and send:

```
Attached is an anonymized customer file with 16 rows. Analyze churn.

1. Show churn by plan and by region in one table, as "churned / total".
2. Compare churned and retained accounts on support_tickets_90d and nps.
3. List up to three patterns, each with the evidence from the data.
4. Add a short "Limits of this analysis" section.

Do not suggest causes the data does not show.
```

**What good looks like:**

- 6 of 16 accounts churned.
- By plan: Basic 4/6, Pro 2/6, Enterprise 0/4.
- Every churned account had 4 or more support tickets in 90 days and an NPS of 5 or lower. No retained account had more than 3 tickets.
- The limits section says 16 rows are too few to generalize and that the data shows association without proving cause.

**5. Verify one number yourself.** Open the anonymized file and count the Basic accounts and how many churned. You should get 4 of 6. One manual check against the source is a habit the exam rewards.

**6. Draft a diligence statement.** Send:

```
I will share this churn analysis with my manager. Draft a short AI diligence statement covering five points: what you helped with, which tool was used, what I reviewed, what I changed, and who is responsible for the final analysis. Leave placeholders where only I know the answer.
```

**What good looks like:** five short lines with placeholders such as "[what I verified]". Fill them in honestly. A statement that claims checks you did not do is its own integrity problem.

#### Debrief

- Steps 1 to 4 apply *Apply data sensitivity, regulatory, and privacy considerations*. The task continued safely, and nobody uploaded identifiers.
- Step 2 used Claude to plan the anonymization without sharing real data.
- Step 6 applies *Understand the ethical implications of AI usage*: transparency and accountability.
- Map it to Sample Question 3. Uploading as-is fails. "Tell Claude not to retain it" fails. Skipping the analysis fails. Anonymize, then analyze.

### Demo B: High-risk triage (3 minutes)

**Goal:** Practice *Identify appropriate and inappropriate use cases*.

**Steps:**

1. Learners vote alone first. Which of these need a qualified human reviewer and disclosure under Anthropic's Usage Policy?
   1. Drafting a newsletter blurb about a webinar
   2. Summarizing a patient's discharge notes to send to the patient
   3. Shortlisting job applicants from résumés
   4. Drafting a letter that declines a rental application
   5. Brainstorming team-offsite activities
   6. Drafting a news article for publication
2. Then paste the list into Claude:

```
For each use case below, say whether it falls into a high-risk category in Anthropic's Usage Policy (legal, healthcare, insurance, finance and lending, employment and housing, academic testing and admissions, media and journalism). For each high-risk case, name the category and the human review step you would add.

1. Drafting a newsletter blurb about a webinar
2. Summarizing a patient's discharge notes to send to the patient
3. Shortlisting job applicants from résumés
4. Drafting a letter that declines a rental application
5. Brainstorming team-offsite activities
6. Drafting a news article for publication
```

**What good looks like:** items 2 (healthcare), 3 (employment), 4 (housing), and 6 (media and journalism) are high-risk. Items 1 and 5 are not. Then open the Usage Policy at https://www.anthropic.com/legal/aup and confirm the categories at the source. Claude's answer is a starting point. The policy page is the authority.

---

## 5. Use cases to work through

**HR generalist: engagement survey.** She wants themes from 400 free-text survey comments. *Suggested approach:* check the policy for employee data first. Remove names and team identifiers, then scan the free text for names, managers, and rare details ("the only night-shift nurse in Building C"). Ask Claude for themes with counts and representative paraphrases. Keep any finding about an individual out of the analysis.

**Agency marketer: missing testimonials.** A client's new landing page needs testimonials and the client has none. *Suggested approach:* decline to have Claude invent them. Use Claude to draft a short email asking real customers for feedback and permission to quote them, and a placeholder layout for the page until real quotes arrive.

**Finance operations analyst: vendor payments.** He wants to find duplicate payments in a sheet with vendor bank details. *Suggested approach:* replace vendor names and bank numbers with codes before upload and keep the key locally. Ask Claude to find candidate duplicates by amount and date. Confirm each candidate in the finance system before anyone acts on it.

**University instructor: grading support.** She wants help giving feedback on 60 essays. *Suggested approach:* academic testing is a high-risk category. Claude can draft feedback against her rubric, with student names removed. She reads each essay, decides every grade, and follows her institution's disclosure rules.

---

## 6. Check yourself

**1.** A sales director asks you to upload a full CRM export with client names and phone numbers so Claude can rank accounts by upsell potential. Policy restricts client personal data. The director says it's urgent. What do you do?

<details><summary>Answer</summary>

Remove or code the names and phone numbers, keep only the fields the ranking needs, then run the analysis. Urgency and seniority do not override policy, and the anonymized data still supports the task.

</details>

**2.** True or false: if you are on a paid Pro plan, your chats are never used for model training.

<details><summary>Answer</summary>

False. Pro and Max are consumer plans, and the user chooses the model-improvement setting in Privacy Settings. Commercial plans such as Team and Enterprise do not train on your data by default. For work data, follow your organization's policy on which plan and workspace to use.

</details>

**3.** A manager wants Claude to choose which of three employees gets a promotion. What is the appropriate role for Claude?

<details><summary>Answer</summary>

Claude can organize the evidence against the agreed criteria and point out gaps or inconsistencies. The manager makes and owns the decision. Employment is a high-risk category that needs a qualified human decision-maker.

</details>

---

## 7. Official resources

- Anthropic Partner Academy prep course 6, *Governance, Risk & Responsible Use* (55 min): https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/governance-risk-responsible-use
- Anthropic Usage Policy (high-risk use cases): https://www.anthropic.com/legal/aup
- Updates to Anthropic's consumer terms: https://www.anthropic.com/news/updates-to-our-consumer-terms
- Data usage and retention: https://code.claude.com/docs/en/data-usage
- AI Fluency for Small Businesses, *Using data with AI*: https://academy.claude.com/courses/ai-fluency-for-small-businesses/using-data-with-ai
- AI Fluency, *A closer look at Diligence*: https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-diligence
- Tutorial, *Writing an AI diligence statement*: https://academy.claude.com/tutorials/writing-an-ai-diligence-statement
- Help center, Memory and Incognito chats: https://support.claude.com/en/articles/11817273

---

**Next:** [Lesson 07: Troubleshooting and Optimization](07-troubleshooting-and-optimization.md)
