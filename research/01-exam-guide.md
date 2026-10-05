# Claude Certified Associate – Foundations (CCAO-F): Exam Guide Research

## Context

This file captures the official blueprint, logistics, scoring, and policies for the Claude Certified Associate – Foundations exam. It is the reference for a 2-hour O'Reilly exam-prep live course. The official Exam Guide (Version 1.0, effective July 2026) is the primary source. Text in quotation marks or in the "verbatim" blocks is copied from the source documents. Cross-checks come from the Anthropic Partner Academy pages (Skilljar) and the two policy PDFs.

### Sources fetched

| Short name | URL | Status |
|---|---|---|
| Exam Guide PDF (v1.0, 8 pages) | https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542847%2FClaude+Certified+Associate+%E2%80%93+Foundations+Exam+Guide.pdf | Downloaded, extracted with `pdftotext -layout` |
| Cert page | https://anthropic-partners.skilljar.com/claude-certified-associate-foundations-certification | Fetched (sparse; links to sub-pages) |
| Certifications overview | https://anthropic-partners.skilljar.com/page/partner-certifications | Fetched |
| Certifications FAQ | https://anthropic-partners.skilljar.com/page/faq-certifications | Fetched |
| Policies page | https://anthropic-partners.skilljar.com/page/policies-certifications | Fetched |
| Prep courses index | https://anthropic-partners.skilljar.com/page/claude-certification-exam-prep-courses | Fetched |
| Associate prep path | https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations | Fetched |
| O'Reilly event page | https://www.oreilly.com/live-events/claude-certified-associate-exam-prep-a-two-hour-crash-course/0642572438333/ | Fetched (the `learning.oreilly.com` URL 307-redirects here) |
| Exam Policy PDF (GitHub mirror) | https://raw.githubusercontent.com/Amey-Thakur/CLAUDE-CERTIFICATIONS/main/guide/anthropic-certification-exam-policy.pdf | Downloaded |
| Terms and Conditions PDF (GitHub mirror) | https://raw.githubusercontent.com/Amey-Thakur/CLAUDE-CERTIFICATIONS/main/guide/certification-terms-and-conditions.pdf | Downloaded |

The GitHub mirror PDFs produce text identical to the official copies linked from the policies page (`diff` showed no differences). Official copies:
- Exam Policy: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F34hhd92iyp94a0gtbr15cy5jk%2Fpublic%2F1782870704%2FAnthropic+Certification+Exam+Policy.pdf
- Terms and Conditions: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F34hhd92iyp94a0gtbr15cy5jk%2Fpublic%2F1782870634%2FCertification+Terms+and+Conditions.pdf

To keep citations readable, `[source: GUIDE]` below means the Exam Guide PDF URL in the table above. All other citations use full URLs.

## Findings

### 1. Naming and exam code

- The official exam code is **CCAO-F**. The guide header reads: "Version 1.0 · Effective July 2026 · Exam code: CCAO-F · This guide is subject to change without notice." [source: GUIDE]
- The O'Reilly page also uses "CCAO-F" ("Decoding the CCAO-F exam blueprint"). [source: https://www.oreilly.com/live-events/claude-certified-associate-exam-prep-a-two-hour-crash-course/0642572438333/]
- "CCA-F" does not appear in any fetched official source. The "advocate" nickname also does not appear in any official source. [unverified]

### 2. Exam logistics

Verbatim table "5. Exam Details at a Glance" [source: GUIDE]:

| Field | Value (verbatim) |
|---|---|
| Credential | Claude Certified Associate – Foundations |
| Exam code | CCAO-F |
| Number of items | 60 |
| Item format | Multiple-choice and multiple-response items; each item states how many responses to select |
| Time limit | 120 minutes |
| Delivery | Proctored: online proctored and/or test center, per program policy |
| Passing score | Scaled score of 720 on a scale of 100–1,000 |
| Exam fee | $99 USD |
| Validity period | 12 months from the date the credential is awarded |
| Result reporting | Pass/fail with scaled score (100–1,000), plus percent-correct by domain on the score report |

Additional logistics:
- Pacing: 60 items in 120 minutes gives 2 minutes per item (derived arithmetic).
- FAQ wording on format: "All Claude certification exams use multiple choice and scenario-based multiple response questions. You have 120 minutes to answer them. Plan for about 135 minutes of total seat time, which includes check-in, instructions, and a brief post-exam survey." [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- Delivery partner: "The exam is delivered by Pearson VUE." Candidates choose "either online proctoring or a Pearson test center." [source: GUIDE]
- Closed book: "No. Exams are closed-book, and browser translation tools are prohibited." (answer to "Can I use notes, documentation, translation tools, or AI assistants during the exam?") [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- Language: "Exams and prep content are English-only." [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- Minimum age: "You must be at least 18 years old to take a Claude Certification exam." [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- Registration validity: "Once you register for an exam, your registration is valid for 5 years." [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- Results timing: "You'll see your score on screen at the end of your exam". Passing candidates receive a Credly badge email. [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- Practice exam: the earlier platform's practice exam "was retired". The exam guide sample questions are the official style reference. [source: https://anthropic-partners.skilljar.com/page/faq-certifications]

#### Price and discounts

- $99 USD. [source: GUIDE] [source: https://anthropic-partners.skilljar.com/claude-certified-associate-foundations-certification]
- "Discounts follow your organization's Claude Partner Network tier. Registered-tier partners pay full price. Select, Preferred, and Global Premier partners receive 50% off, applied automatically at checkout. Through December 31, 2026, Global Premier partners receive a 100% discount on all certification exams." [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- Sibling credential prices: Developer – Foundations $125, Architect – Foundations $125, Architect – Professional $175. [source: https://anthropic-partners.skilljar.com/page/partner-certifications]

#### Eligibility (important for an O'Reilly audience)

- "Certification is available to people at Claude Partner Network organizations. Registration requires a partner email address on a recognized company domain — personal email addresses will not work." [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- "Certification is currently available only to organizations in the Claude Partner Network." [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- The Associate credential "does not count toward Claude Partner Network tier eligibility". Developer – Foundations, Architect – Foundations, and Architect – Professional do count. [source: https://anthropic-partners.skilljar.com/page/partner-certifications] [source: https://anthropic-partners.skilljar.com/page/faq-certifications]

#### Prerequisites

Verbatim: "Prerequisites: There are no mandatory prerequisites or required courses, and no software-development or API experience is needed. The experience above is recommended, not required. The credential is awarded based on exam performance alone." [source: GUIDE]

#### Retakes

Verbatim: "Candidates who do not pass may retake the exam after a required waiting period. Waiting periods increase with each failed attempt: 14 days after the first, 30 days after the second, and 90 days after the third. You may take an exam up to four times within a rolling twelve-month period. Limits apply per exam, so not passing one exam does not prevent you from registering for a different one. The exam fee applies to each attempt." [source: GUIDE]

- Retakes cost the full fee with the tier discount applied. [source: https://anthropic-partners.skilljar.com/page/faq-certifications]

#### Validity and recertification

Verbatim (Section 14): "The Claude Certified Associate – Foundations credential is valid for 12 months from the date it is awarded. Because the underlying technology evolves rapidly, the credential is time-limited so that holders maintain current knowledge. To renew on time, you review what has changed since you certified and complete a free, non-proctored assessment on the Anthropic Partner Academy. There is no fee for on-time renewal. If your credential lapses, you must retake the full exam at the full fee to regain certified status. If exam content changes significantly, Anthropic may require holders to retake the full exam to recertify rather than complete the renewal assessment. Holders remain subject to the rules of conduct described in Section 12." [source: GUIDE]

- Certifications earned before June 30, 2026 under the old 6-month validity were extended to 12 months. [source: https://anthropic-partners.skilljar.com/page/faq-certifications]

### 3. Purpose, audience, and candidate profile

#### About This Certification (Section 1, verbatim)

"The Claude Certified Associate – Foundations certification validates that an individual can apply Claude to complete business and productivity tasks with minimal guidance. This includes using built-in platform features, capabilities, and tools to streamline workflows; identifying opportunities to improve processes with Claude; selecting approaches that balance quality, efficiency, and cost; and recognizing limitations and escalating more complex or technical work to Claude Architects and Developers.

It is intended for professionals who use Claude as a productivity tool in roles such as operations, marketing, project management, education, and communications." [source: GUIDE]

#### Purpose and Value (Section 2, verbatim)

"The primary purpose of the Claude Certified Associate – Foundations certification is to provide an independent assessment of the knowledge and skills required to use Claude effectively and responsibly in real-world business workflows."

Candidates who earn the credential can demonstrate that they are able to:
- Apply Claude to complete structured business tasks with minimal guidance
- Use built-in platform features and tools to streamline workflows
- Identify opportunities to improve processes using Claude
- Select appropriate approaches to balance quality, efficiency, and cost
- Recognize limitations and escalate more complex or technical implementations

[source: GUIDE]

#### Intended Audience (Section 3, verbatim)

"The certification is intended for professionals who use Claude as a productivity tool and build Claude Projects in their day-to-day roles. They operate across functions such as operations, marketing, project management, education, communications, and general knowledge work, applying AI to improve efficiency, decision-making, and content development. The audience includes both internal staff who maintain and optimize ongoing AI-enabled workflows and external consultants who support implementation, use-case identification, and process redesign.

Candidates generally have limited to moderate technical expertise. They are positioned between casual AI prompt users and technical AI practitioners, and are distinguished by their ability to translate business objectives into effective AI interactions, select appropriate tools and features, create structured prompts, critically evaluate AI-generated content, adapt outputs for different audiences, and recognize when human expertise, validation, or escalation is required." [source: GUIDE]

- The overview page describes the audience differently: "For consultants, sellers, and delivery leads who guide customers toward the [right] Claude use cases". The fetch truncated the sentence. [source: https://anthropic-partners.skilljar.com/page/partner-certifications]

#### Out of scope (Section 3, verbatim)

"This certification is not intended for software developers who build against APIs or design agentic systems, nor for specialists in machine learning, software engineering, or advanced AI system design. Candidates are not expected to design enterprise-scale AI architectures or integrations; that scope belongs to the Claude Architect and Claude Developer credentials, to which Associates escalate more complex or technical work." [source: GUIDE]

The guide contains no other explicit in-scope or out-of-scope list. The domain objectives in Section 6 define the in-scope content.

#### Minimally Qualified Candidate (Section 4, verbatim)

"The exam is targeted at the minimally qualified candidate (MQC): a professional who uses Claude as a core productivity tool and can apply it effectively within real-world workflows to improve efficiency, quality, and outcomes. The MQC has foundational, applied knowledge of Claude's capabilities, including prompt structuring, task orchestration, and familiarity with features such as Projects, Artifacts, and workflow-based interactions, and moves beyond basic question-and-answer usage to process reimagination, task automation, and project development.

The MQC is aware of organizational context: how Claude creates value, where adoption risks exist, and how to align usage with business needs and responsible-AI practices. They have regular, hands-on experience using Claude in a professional setting and can independently complete common productivity and workflow tasks on the platform." [source: GUIDE]

Recommended experience (verbatim):
- Regular, hands-on experience using Claude in a professional setting
- A foundational understanding of structured problem-solving, workflow design, and digital tool usage
- Experience in roles such as business analyst, project manager, operations lead, marketing/communications/HR/education professional, consultant, or knowledge worker
- A practical understanding of AI limitations, including hallucinations, context constraints, and data sensitivity

[source: GUIDE]

### 4. Exam Content Outline (Blueprint): all domains and objectives

Section 6 intro (verbatim): "The exam blueprint defines the content domains measured and the approximate weight of each domain on the exam. Weights reflect the relative importance of each domain to competent performance as determined through the job task analysis. The percentages indicate the approximate proportion of scored items drawn from each domain." [source: GUIDE]

"Each domain below lists the tasks a candidate is expected to perform. Exam items are written against these objectives." [source: GUIDE]

| Domain | Content Domain | Weight | Approx. items of 60 (derived) |
|---|---|---|---|
| 1 | Prompting and Task Execution | 14% | ~8 |
| 2 | Output Evaluation and Validation | 21% | ~13 |
| 3 | Product and Model Selection | 12% | ~7 |
| 4 | Workflow Integration and Solution Design | 16% | ~10 |
| 5 | Configuration and Knowledge Management | 12% | ~7 |
| 6 | Governance, Risk, and Responsible Use | 15% | ~9 |
| 7 | Troubleshooting and Optimization | 10% | ~6 |
| | Total | 100% | 60 |

Domain names and weights come from [source: GUIDE]. The item counts are my rounding of weight x 60. The guide gives no per-domain item counts, and the sum of the rounded values depends on rounding. Weights are "approximate", and the exam may include unscored items. [unverified]

The guide uses the words "objectives" and "tasks". It does not separate "task statements" from "knowledge and skills". Each domain has one flat bullet list. All 30 bullets below are verbatim. [source: GUIDE]

#### Domain 1: Prompting and Task Execution (14%) — 4 objectives
- Create effective prompts for business and technical tasks
- Apply task decomposition techniques to structure complex requests
- Iterate prompts to improve output quality
- Adapt prompting strategies based on task type (analysis, research, drafting, brainstorming)

#### Domain 2: Output Evaluation and Validation (21%) — 6 objectives
- Evaluate Claude-generated outputs for accuracy and completeness
- Identify hallucinations, inconsistencies, and biases in responses
- Apply fact-checking and validation techniques
- Determine when human review or additional verification is required
- Edit, adapt, refine, and compare outputs for the intended audience
- Organize and curate information and select appropriate output formats (artifacts, inline, structured data)

#### Domain 3: Product and Model Selection (12%) — 4 objectives
- Select appropriate Claude product features (Projects, research mode, chat, artifacts)
- Differentiate between Claude model types (Haiku, Sonnet, Opus)
- Align model selection with task requirements (cost, speed, quality)
- Understand and manage context limitations and memory considerations (when to restart, summarize, or persist)

#### Domain 4: Workflow Integration and Solution Design (16%) — 5 objectives
- Apply Claude to analyze requirements and use cases
- Leverage Claude for research, planning, and process optimization
- Use Claude to support solution design, development, and iteration
- Integrate Claude into existing workflows to augment or redesign them
- Communicate Claude's value and limitations to stakeholders

#### Domain 5: Configuration and Knowledge Management (12%) — 4 objectives
- Configure Claude Projects with instructions and knowledge sources
- Manage uploaded knowledge and connectors (e.g., Google Drive, Gmail)
- Create effective system-level instructions
- Inform, maintain, and update Claude configurations, knowledge sources, and instructions

#### Domain 6: Governance, Risk, and Responsible Use (15%) — 4 objectives
- Identify appropriate and inappropriate use cases
- Apply data sensitivity, regulatory, and privacy considerations
- Follow organizational AI policies and governance standards
- Understand the ethical implications of AI usage

#### Domain 7: Troubleshooting and Optimization (10%) — 3 objectives
- Identify, diagnose, and resolve issues with underperforming prompts or poor outputs
- Adjust approach based on feedback and results
- Optimize workflows for efficiency and effectiveness

Teaching notes (derived from the weights):
- Domains 1 and 2 together cover 35%. The O'Reilly agenda uses the same figure. Domain 2 alone is the largest domain at 21%.
- Domains 2, 4, and 6 together cover 52% of the exam.

### 5. Sample questions (Section 8, verbatim)

Intro: "These illustrative items show the style and cognitive level of the exam. They are not drawn from the live item bank. Correct answers and rationale appear after the questions." [source: GUIDE]

**Sample 1 · Domain 2 — Output Evaluation and Validation**
An associate asks Claude to summarize a new regulation, and Claude produces a confident summary citing a specific subsection number. Before sending the summary to the compliance team, what is the most appropriate action?
- A. Send it as-is, since Claude expressed high confidence.
- B. Verify the cited subsection against the official regulation text before sharing.
- C. Ask Claude to rate its own confidence and send it if the rating is high.
- D. Reword the summary to sound more formal, then send it.

Answer: **B**. "Language models can fabricate specific-looking details such as citation numbers, a hallucination. Validating factual claims, especially citations bound for a compliance audience, against an authoritative source is the diligence step required. Self-reported confidence (A, C) is not a reliable accuracy signal, and reformatting (D) does not address correctness."

**Sample 2 · Domain 3 — Product and Model Selection**
An associate needs to generate a high volume of short customer-reply drafts where speed and cost matter more than deep reasoning. Which choice best fits the task?
- A. Use the most capable, highest-cost model for every reply to maximize quality.
- B. Use a faster, lower-cost model suited to straightforward, high-volume tasks.
- C. Disable all product features to reduce cost.
- D. Switch to a different AI platform.

Answer: **B**. "Aligning model selection with task requirements means matching a faster, lower-cost model to straightforward, high-volume work, reserving the most capable model for complex reasoning. Always using the top model (A) wastes the cost and latency budget; disabling features (C) or switching platforms (D) does not address the trade-off."

**Sample 3 · Domain 6 — Governance, Risk, and Responsible Use**
A project manager wants to upload a spreadsheet containing customer names and account numbers so Claude can analyze trends. Organizational policy restricts sharing regulated personal data. What is the most appropriate action?
- A. Upload the file as-is, since the analysis is internal.
- B. Remove or anonymize the personal identifiers before uploading, consistent with policy.
- C. Upload the file but instruct Claude not to retain it.
- D. Skip the analysis entirely.

Answer: **B**. "Applying data-sensitivity and privacy safeguards means redacting or anonymizing regulated identifiers before use, so the analysis can proceed without exposing protected data. Uploading as-is (A) violates policy; instructing the model not to retain data (C) does not satisfy the policy control; abandoning the task (D) is unnecessary when anonymization enables it."

[source: GUIDE]

Item-style patterns visible in the samples (my analysis):
- Each item uses a short workplace scenario and asks for the "most appropriate" or "best fits" action.
- The distractors follow a pattern: blind trust (A), a fake safeguard (C, such as self-rated confidence or "tell Claude not to retain"), an irrelevant fix (D-style reformatting or platform switching), and over-reaction (skip the task).
- The correct answer is the proportionate step that lets the work continue safely.

The guide includes no multiple-response sample. It also contains no named scenarios list. A different credential's guide may contain one. [unverified]

### 6. Scoring (Section 9, verbatim)

"The Claude Certified Associate – Foundations exam is a criterion-referenced assessment: each candidate is measured against a fixed performance standard, not against other candidates. You pass by demonstrating the knowledge and skills defined in the blueprint, not by outperforming a percentage of peers.

Passing standard. The passing score was established through a formal standard-setting study in which trained subject matter experts judged the level of performance expected of a minimally qualified candidate. The score is reported on a scaled range of 100–1,000, and the cut score is 720.

Result reporting. Your result is reported as a pass or fail status with a scaled score from 100 to 1,000. Your score report also shows the percentage of items you answered correctly within each content domain. Section-level percentages are provided to help you understand your performance and are not used to determine your pass or fail result, which is based on your total scaled score." [source: GUIDE]

- 720 is the cut score "for all four certifications". [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- A scaled 720 does not equal 72% raw correct. The guide does not publish the raw-to-scaled conversion. [unverified]
- The guide does not state whether multiple-response items give partial credit. [unverified]
- The guide does not mention a penalty for wrong answers. [unverified]

### 7. How to Prepare (Section 7, verbatim)

"There is no single required course. Anthropic does not guarantee that any particular resource ensures a passing result. Candidates are encouraged to combine hands-on experience with the resources below:
- Study the exam blueprint in Section 6 and self-assess against each objective
- Review official Anthropic documentation and help articles for Claude features such as Projects, Artifacts, Memory, Skills, and Code Execution
- Practice structuring prompts, decomposing tasks, and iterating to improve outputs
- Build real workflows: configure a Project with instructions and knowledge sources, and evaluate outputs for accuracy and bias
- Practice responsible-use judgment: data sensitivity, appropriate use cases, and when to escalate or seek human review
- Complete the sample questions in Section 8 to familiarize yourself with item style" [source: GUIDE]

The guide lists no URLs for prep resources.

#### Official prep path (Partner Academy, 8 courses)

Path: "Claude Certified Associate - Foundations Prep Course". Description: "Learn how to operate Claude with professional discipline, turning everyday business problems into reliable Claude workflows you can stand behind." [source: https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations]

| # | Course | Duration | Maps to domain (my mapping) | URL |
|---|---|---|---|---|
| 1 | Claude Platform & Model Foundations | 59 min | D3 | https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/claude-platform-model-foundations |
| 2 | Prompting & Task Execution | 53 min | D1 | https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/prompting-task-execution |
| 3 | Evaluating & Validating Claude's Output | 74 min | D2 | https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/evaluating-validating-claudes-output |
| 4 | Workflow Integration & Solution Design | 63 min | D4 | https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/workflow-integration-solution-design |
| 5 | Configuration & Knowledge Management | 47 min | D5 | https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/configuration-knowledge-management |
| 6 | Governance, Risk & Responsible Use | 55 min | D6 | https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/governance-risk-responsible-use |
| 7 | Troubleshooting & Optimization | 30 min | D7 | https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/troubleshooting-optimization |
| 8 | Course Summary & Next Steps | 8 min | all | https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/course-summary-next-steps |

Course descriptions (verbatim from the path page):
1. "Master the four decisions that set the quality ceiling for every Claude session before you write a single prompt: entry point, capability features, model, and context."
2. "Learn effective prompting as a communication discipline with a repeatable structure that anyone can build."
3. "Learn to evaluate and validate Claude's output so that you can stand behind every deliverable you put your name on."
4. "Learn how to move from 'I use Claude' to 'our workflow uses Claude' by deciding which steps to delegate to the model and which to keep with humans."
5. "Learn to configure Claude once, so that every conversation that follows benefits from having the right context in place."
6. "Build the judgement to decide what is safe and appropriate to bring to Claude."
7. "Diagnose why output is underperforming, trace the root cause, and apply the necessary fixes."
8. "Learn how to connect the seven skills taught in the previous modules into one discipline for operating Claude with confidence."

[source: https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations]

- The courses total 389 minutes, about 6.5 hours (derived sum).
- The O'Reilly page calls this path "Anthropic's free eight-course prep path". The Partner Academy pages do not state a price for the path. [source: https://www.oreilly.com/live-events/claude-certified-associate-exam-prep-a-two-hour-crash-course/0642572438333/] The path's cost is [unverified].

### 8. The four-credential program

| Credential | Level | Price | Audience (per overview page) | Counts toward CPN tier |
|---|---|---|---|---|
| Claude Certified Associate – Foundations | Foundations | $99 | Consultants, sellers, and delivery leads guiding customers to Claude use cases | No |
| Claude Certified Developer – Foundations | Foundations | $125 | Engineers building with Claude API, Claude Code, and Model Context Protocol | Yes |
| Claude Certified Architect – Foundations | Foundations | $125 | Partners designing Claude solutions end-to-end | Yes |
| Claude Certified Architect – Professional | Professional | $175 | Advanced partners with architecture expertise | Yes |

[source: https://anthropic-partners.skilljar.com/page/partner-certifications] [source: https://anthropic-partners.skilljar.com/page/faq-certifications]

- FAQ program description: "The Claude Certification program validates that people at partner organizations have the skills to do real work with Claude, across three roles: Associate, Developer, and Architect." [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- The Exam Guide frames escalation: Associates escalate "more complex or technical work to Claude Architects and Developers." [source: GUIDE]

### 9. Key terminology used in the guide

| Term | Meaning in the guide |
|---|---|
| MQC (minimally qualified candidate) | The target candidate profile used for standard setting (Section 4) |
| Blueprint / Exam Content Outline | Domains plus weights plus objectives (Section 6) |
| Job task analysis | The study that set the domain weights |
| Criterion-referenced assessment | Candidates are measured against a fixed standard, not each other |
| Standard-setting study / cut score | The SME process that set 720 on the 100–1,000 scale |
| Scaled score | The reported score from 100 to 1,000 |
| Multiple-choice / multiple-response items | One answer, or several answers with the count stated in the item |
| Escalate / escalation | Handing complex or technical work to Claude Architects and Developers, or to human expertise |
| Projects, Artifacts, research mode, chat | Product features named in D3 and D5 |
| Memory, Skills, Code Execution | Features named in "How to Prepare" |
| Connectors (e.g., Google Drive, Gmail) | Named in D5 |
| Haiku, Sonnet, Opus | Model families named in D3 |
| Context limitations / restart, summarize, persist | D3 context-management vocabulary |
| Hallucinations, inconsistencies, biases | D2 failure modes |
| Task decomposition, iterate prompts | D1 techniques |
| System-level instructions | D5 (Project instructions) |
| Output formats: artifacts, inline, structured data | D2 |
| Human review / additional verification | D2 and D6 judgment calls |
| Data sensitivity, regulatory, privacy considerations | D6 |
| Organizational AI policies and governance standards | D6 |

[source: GUIDE]

### 10. O'Reilly live event page

Title: "Claude Certified Associate Exam Prep: A Two-Hour Crash Course". Content level: Intermediate. Instructor: Lucas Soares. The fetched page shows no date. [source: https://www.oreilly.com/live-events/claude-certified-associate-exam-prep-a-two-hour-crash-course/0642572438333/]

What you'll learn:
- Decoding the CCAO-F exam blueprint
- Structuring and iterating prompts per exam expectations
- Evaluating and validating Claude outputs
- Selecting appropriate product features and models
- Configuring Claude Projects for knowledge management
- Applying governance and responsible-use judgment

Who should attend:
- Operations, marketing, project management, education, or communications professionals using Claude daily
- Consultants, sellers, or delivery leads guiding customers toward appropriate Claude use cases
- Managers rolling out Claude across teams seeking structured competence-building

Prerequisites:
- Regular, hands-on professional Claude experience (no coding/API knowledge required)
- Familiarity with basic features including chat, file uploads, and ideally Projects and artifacts
- Practical awareness of AI limitations like hallucinations and context constraints

Recommended preparation:
- Create a Claude account (Pro recommended for Projects access during exercises)
- Download the official Exam Guide from the Anthropic Partner Academy
- Optionally enroll in Anthropic's free eight-course prep path
- Clone/download the course repository before the session

Schedule (120 min total):

| Segment | Length | Topics |
|---|---|---|
| The exam, the platform, and model selection | 25 min | Exam program overview, the four credentials and their positioning; seven-domain blueprint with weights; product and model selection strategies; hands-on exam-style question and Q&A |
| Prompting and output validation—35% of the exam | 35 min | Domains 1 and 2: prompt structure, task decomposition, output validation; hallucination, inconsistency, and bias detection; hands-on structured prompt building and output validation; Q&A and break |
| Workflows, Projects, and knowledge management | 30 min | Workflow integration and solution design; hands-on Project configuration with instructions, knowledge sources, and connectors; practice questions on workflow integration; Q&A |
| Governance, troubleshooting, and exam strategy | 20 min | Governance, risk, and responsible use principles; troubleshooting diagnostic checklist; exam-day strategy and time budgeting; Q&A |
| Your four-week study plan | 10 min | Domain-by-domain self-assessment framework; registration and rescheduling information; Q&A |

[source: https://www.oreilly.com/live-events/claude-certified-associate-exam-prep-a-two-hour-crash-course/0642572438333/]

Agenda-to-blueprint coverage (my analysis):
- Segment 1 covers D3 (12%). Segment 2 covers D1 and D2 (35%). Segment 3 covers D4 and D5 (28%). Segment 4 covers D6 and D7 (25%).
- Segment 4 gives 20 minutes to 25% of the exam. Segment 1 gives about 15 minutes of model-selection content to 12% of the exam. Time per weight point is lowest in Segment 4.
- The page promises content that the exam guide does not supply: a "troubleshooting diagnostic checklist", "exam-day strategy and time budgeting", a "four-week study plan", and a "domain-by-domain self-assessment framework". The course must create these.
- The page targets a general O'Reilly audience. The FAQ restricts the exam to Claude Partner Network employees with a partner email domain. The course should state this restriction early.

### 11. Policy highlights

Registration and scheduling:
- Register on the Partner Academy, pay by credit card, then schedule through Pearson VUE (online or test center). [source: GUIDE]
- The guide says: "You may cancel or reschedule up to 24 hours before your appointment. Changes made within 24 hours forfeit the exam fee." [source: GUIDE]
- The FAQ and policies page say 48 hours: "You can reschedule or cancel free of charge as long as you do it at least 48 hours before your appointment." [source: https://anthropic-partners.skilljar.com/page/policies-certifications] [source: https://anthropic-partners.skilljar.com/page/faq-certifications] **These sources conflict. Teach 48 hours as the safe rule.**
- Cancelling in Pearson does not issue a refund automatically. Candidates must email certifications-support@anthropic.com. [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- No-show or late arrival forfeits the fee and requires re-registration. [source: GUIDE]

Identification:
- "valid, unexpired, government-issued photo identification. The name on your ID must match the name on your registration exactly." [source: GUIDE]
- Name corrections: email certifications-support@anthropic.com at least 24 hours before the exam with subject "Name Correction Request", using Latin characters. Processing takes 24–48 business hours. A mismatch at check-in means Pearson refuses the test and the fee is forfeited. [source: https://anthropic-partners.skilljar.com/page/faq-certifications]

Exam-day conduct (guide Section 12, verbatim): during the exam you must:
- Remain within view of the proctor and webcam for the entire session, if testing online
- Keep your workspace clear of notes, books, phones, secondary monitors, and other materials
- Refrain from communicating with any other person during the exam
- Not capture, copy, photograph, or reproduce any exam content in any form

"Prohibited items include mobile phones, smart watches, headphones, study materials, and any recording device. Permitted items, if any, such as scratch paper provided by the proctor, are specified by Pearson VUE." [source: GUIDE]

The Exam Policy lists prohibited activities. Selected items, verbatim:
- "Using AI products or services to assist you during the Exam;"
- "Misrepresenting your country of residence or the country where the Exam will be delivered;"
- "Seeking or obtaining unauthorized access to any Exam or Exam Content, including use of unauthorized publication of Exam questions or answers;"
- "Possessing unauthorized items while taking an Exam or during any breaks, including electronic devices, more than one monitor, notes or other documentation;"
- "Taking unscheduled breaks during the Exam, unless requested and approved in advance"

[source: https://raw.githubusercontent.com/Amey-Thakur/CLAUDE-CERTIFICATIONS/main/guide/anthropic-certification-exam-policy.pdf] (last updated June 25, 2026)

Consequences:
- Misconduct can lead to invalidated results, credential revocation, and a ban from future exams. [source: GUIDE]
- Under the Exam Policy, Anthropic may also require a retake or exclude the candidate from the Program, "without obligation to refund any Exam-related fees". [source: https://raw.githubusercontent.com/Amey-Thakur/CLAUDE-CERTIFICATIONS/main/guide/anthropic-certification-exam-policy.pdf]

Confidentiality and NDA:
- Candidates accept an NDA before the exam. If a candidate declines, "the exam session ends and no refund is issued." [source: GUIDE]
- Exam Content counts as Anthropic Confidential Information. [source: https://raw.githubusercontent.com/Amey-Thakur/CLAUDE-CERTIFICATIONS/main/guide/anthropic-certification-exam-policy.pdf]
- Course implication: practice questions must be original, and recalled live items must not be used.

Accommodations:
- Request accommodations through Pearson VUE and get approval before scheduling. [source: GUIDE]
- The FAQ advises requesting "10 days or more" ahead. [source: https://anthropic-partners.skilljar.com/page/faq-certifications]

Appeals:
- Appeal within 14 days of notification, or within 14 days of the exam date for result concerns. Submit appeals to Pearson VUE. "The standard-setting outcome and the content of individual exam items are not subject to appeal." [source: GUIDE]

Geographic limits:
- Holders of IDs from Belarus, Cuba, North Korea, Russia, Syria, or restricted regions of Ukraine cannot use OnVUE online proctoring. They can test at Pearson centers. [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- Pearson suspended delivery for Iran residents from September 8, 2026. [source: https://anthropic-partners.skilljar.com/page/faq-certifications]

Terms and Conditions:
- "Certification is not a warranty or guarantee of an individual's abilities". Holders "may not represent yourself as currently certified after expiration". [source: https://raw.githubusercontent.com/Amey-Thakur/CLAUDE-CERTIFICATIONS/main/guide/certification-terms-and-conditions.pdf]
- Anthropic may disclose pass/fail and certification status to the candidate's Partner employer. [source: https://raw.githubusercontent.com/Amey-Thakur/CLAUDE-CERTIFICATIONS/main/guide/certification-terms-and-conditions.pdf]

Support contacts:
- certifications-support@anthropic.com handles name corrections and refunds.
- pearsonvue.com/us/en/anthropic.html handles registration, scheduling, accommodations, and results.
- partner-support@anthropic.com handles email-domain and discount issues.

[source: GUIDE] [source: https://anthropic-partners.skilljar.com/page/faq-certifications]

## Comparison: discrepancies across sources

| Topic | Exam Guide v1.0 | Partner Academy pages | Note |
|---|---|---|---|
| Reschedule/cancel window | 24 hours | 48 hours | Teach 48h as the safe rule |
| Question types | "Multiple-choice and multiple-response" | "multiple choice and scenario-based multiple response" | Consistent; FAQ adds "scenario-based" |
| Audience framing | Ops, marketing, PM, education, comms professionals | "consultants, sellers, and delivery leads" | O'Reilly page lists both |
| Eligibility | Silent on partner requirement | Partner Network members only, partner email required | Critical for a public O'Reilly audience |
| Exam code | CCAO-F | Not shown | "CCA-F" is not official |

## Open questions

- Is the prep path free? The O'Reilly page says "free". The Partner Academy page shows no price. The Partner Academy path may also require a partner login, so non-partner attendees may lack access.
- Are non-partner O'Reilly attendees able to sit the exam at all? The FAQ says no. Lucas should decide how the course frames this restriction.
- The guide and the FAQ give different reschedule windows (24h vs 48h). Which one should the slides cite?
- Does the exam give partial credit on multiple-response items? No source says.
- Does the exam include unscored pretest items? No source says.
- Should the course include the full exam-day rules, or only a one-slide summary?
