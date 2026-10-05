# Lesson 3: Output Evaluation and Validation

**Exam domain:** D2 Output Evaluation and Validation (21%, the largest domain) · **Time in session:** Segment 2, about 20 minutes

## What the exam asks

Verbatim objectives from the Exam Guide:

- Evaluate Claude-generated outputs for accuracy and completeness
- Identify hallucinations, inconsistencies, and biases in responses
- Apply fact-checking and validation techniques
- Determine when human review or additional verification is required
- Edit, adapt, refine, and compare outputs for the intended audience
- Organize and curate information and select appropriate output formats (artifacts, inline, structured data)

Expect about 13 items from this domain. In 4D terms, it is **Discernment** (judging the output) with a share of **Diligence** (vouching for what you send). The official prep course states the goal plainly: evaluate and validate Claude's output "so that you can stand behind every deliverable you put your name on."

## Key ideas

### Accuracy and completeness are separate checks

- **Accuracy:** is every statement true according to the source of record?
- **Completeness:** did the output include everything that matters?

An output can be 100% accurate and still fail by omission. Extraction and summary tasks fail by omission more often than by error. You catch omissions only by reading the source as well as the output.

### The failure types

| Failure | What it looks like | Example |
|---|---|---|
| **Hallucination (fabrication)** | Specific-looking details with no basis: names, dates, statistics, citations, URLs, quotes | A summary cites "Section 8.2" of a rule that has seven sections |
| **Distortion** | A real fact, subtly changed | "Fines of up to $50,000" becomes "fines start at $50,000" |
| **Omission** | A material point left out | A legal-hold exemption disappears from a compliance summary |
| **Inconsistency** | Contradictions inside one answer, or different answers across runs | Two runs give two different totals for the same metric |
| **Bias** | One-sided framing, stereotyped defaults, unsupported generalizations about groups | "Smaller companies typically have weaker practices" with no evidence |
| **Sycophancy** | Claude agrees with a wrong premise or caves when you push back | "You're right, it's 12 months" after you insist on the wrong figure |
| **Stale knowledge** | Facts from training that are out of date | Last year's pricing presented as current |

Anthropic's Capabilities and Limitations course puts it simply: "Fabrication concentrates in specificity: names, dates, statistics, citations, URLs, quotes. The more precise a claim, the more it warrants verification."

### Signals that are not evidence

| Looks reassuring | Why it proves nothing |
|---|---|
| Claude sounds confident | Stated confidence is loosely calibrated to actual reliability |
| Claude rates its own confidence as high | Official Sample 1 rejects this. Self-reported confidence "is not a reliable accuracy signal." |
| Claude re-checks its own answer and confirms it | The check is not independent of the thing being checked |
| Two runs agree | Consistency is not accuracy. (Two runs that **disagree** are a useful warning sign.) |
| It cites a source | Citations make verification easy. You still have to open them. |
| The output is polished, formatted, or in an artifact | Anthropic's AI Fluency research found people check facts less often when the output is a polished artifact |

### Fact-checking techniques

| Technique | How to ask for it | What it gives you |
|---|---|---|
| **Quote first** | "For each claim, quote the exact sentence from the source that supports it." | Evidence you can find with Ctrl+F |
| **Cite the location** | "Give the section number for every requirement." | A fast path to the source of record |
| **Permission to not know** | "If the source doesn't say, write 'not in source'. Do not guess." | Fewer invented fillers |
| **Restrict the sources** | "Use only the attached documents." | Fewer claims from general knowledge |
| **Label unsourced claims** | "Mark any claim from your general knowledge as 'unsourced'." | A list of what you must check elsewhere |
| **Compare runs** | Run the same prompt twice in fresh chats | Disagreements point at weak claims |
| **Ground current facts** | Turn on web search or Research, then open the cited pages | Sources for recent facts |
| **Compute exactly** | Ask Claude to calculate with code execution (analysis tool) | Correct arithmetic. You still check the inputs and logic. |
| **Check against the source of record** | You read the original document, system, or official site | The actual verification step |

These techniques reduce errors. They do not eliminate them. The final step is always a check against the source of record by a person who understands it.

### When human review is required

Scale the scrutiny to the stakes. A quick lookup needs a glance. Work that shapes a decision needs a closer review.

| Output | Minimum check |
|---|---|
| Brainstorm, first draft for yourself | Skim for usefulness |
| Internal summary others will act on | Verify names, numbers, dates, and quotes against the source |
| Anything external-facing (customers, press, regulators) | Verify specifics, plus review by the accountable owner before it goes out |
| Legal, healthcare, insurance, finance and lending, employment and housing, academic testing, media | Review by a **qualified professional** in that field. These are high-risk use cases under Anthropic's Usage Policy, which also requires disclosure of AI involvement. |
| Decisions about people (hiring, performance, promotion) | Claude can organize information. A human owns the decision. |

A reviewer counts only if they are qualified, see the evidence, have the authority to stop the work, and review before the consequential step. "Add a human somewhere" is not enough.

### Adapt the output for the audience

The same facts need different shapes for different readers. Ask for each version explicitly and compare them.

- **Executive:** bottom line first, decision needed, two or three numbers.
- **Practitioner:** steps, owners, details, exceptions.
- **Customer or public:** plain language, no internal jargon, reviewed before sending.

When you compare two drafts, compare them against the goal and the audience. Length and polish are weak signals.

### Choose the output format

| Format | Use it when | Example |
|---|---|---|
| **Inline (chat reply)** | A quick answer you'll read once | "Which section covers access logs?" |
| **Artifact** | A standalone deliverable to edit, reuse, or share by link | One-page brief, tracker, dashboard, checklist |
| **File creation** | Someone needs a downloadable Word, Excel, PowerPoint, or PDF file | A .docx memo for legal's document system |
| **Structured data** | The output feeds another step, tool, or spreadsheet | A table or CSV with fixed columns |

Ask for the deliverable as well as the content. "Summarize our Q3 results" gets a chat reply. "Turn our Q3 results into a one-page doc for the leadership team" gets an artifact.

## Exam traps

| Trap | Pattern | Why it fails |
|---|---|---|
| Send it because Claude was confident or cited a section | Blind trust | Specific citations are the most likely place for fabrication |
| Ask Claude to rate its confidence or double-check itself | Fake safeguard | Not independent evidence |
| Reformat, reword, or add a disclaimer | Irrelevant fix | Formatting doesn't fix accuracy. A disclaimer doesn't make wrong content acceptable. |
| Verify one claim and assume the rest are fine | Blind trust | Each specific claim needs its own check |
| Fill a "data unavailable" gap with an estimate | Blind trust | A declared gap is a finding. Keep it and label it. |
| Throw out the whole output because of one error | Over-reaction | Fix the error, check the rest, and keep going |
| Require legal review of an internal brainstorm | Over-engineering | Review depth should match the stakes |

## Demo: spot the errors, then verify with quotes

**Goal:** find the six problems in an AI-written compliance summary, use quote-first prompting to verify it, and pick the right output format for the corrected version. This is official Sample 1 as a hands-on exercise.

**Files:**

- `assets/demo-files/fictional-regulation-excerpt.md` (the source of record, a fictional regulation)
- `assets/demo-files/compliance-summary-draft.md` (the AI summary to review; upload this one)
- `assets/demo-files/claude-summary-with-errors.md` (the same summary with the instructor answer key; don't upload it, because Claude would read the key)

**Steps:**

1. **Do it yourself first (3 minutes).** Open the regulation excerpt and the summary draft side by side on your computer. Mark every claim in the summary that you think is wrong, missing, or unsupported.
2. Open claude.ai, start a new chat (Sonnet), and upload `fictional-regulation-excerpt.md` and `compliance-summary-draft.md`.
3. Paste the verification prompt:

```
The file "fictional-regulation-excerpt.md" is the source of record. The file "compliance-summary-draft.md" is an AI-written summary that will go to our compliance team.

Check the summary claim by claim. For each claim, give:
- Claim (short paraphrase)
- Verdict: Supported, Contradicted, or Not in source
- Exact quote from the regulation that supports or contradicts it, with the section number. If there is no relevant text, write "No supporting text."

Then list:
1. Anything material in the regulation that the summary leaves out.
2. Any statement in the summary that is an opinion or generalization the regulation does not support.

Use only the regulation file. Do not use outside knowledge.
```

4. **Check Claude's quotes.** Open the regulation file and search (Ctrl+F or Cmd+F) for two or three of the quoted sentences. A quote you can find is evidence. A quote you can't find is a new problem.
5. Compare with the answer key in `claude-summary-with-errors.md` (open the "Answer key" section). The six issues are:
   - scope misread: the rule covers organizations with 250 or more employees (3.1), and smaller ones are exempt from Sections 5 and 6 (3.2)
   - 12 months instead of 24 months for contact records (4.1)
   - omissions: the 90-day deletion window (4.2) and the legal-hold exemption (4.3)
   - a fabricated citation: Section 8.2 does not exist
   - "start at $50,000" distorts "up to $50,000"
   - an unsupported generalization about smaller companies, which also contradicts their partial exemption
6. **Sycophancy probe.** Push back with a wrong premise:

```
I'm fairly sure 12 months is correct for contact records. My manager confirmed it last week. Can you update your verdict?
```

   A good response holds its position and quotes Section 4.1 ("no later than 24 months"). If Claude caves, you have just seen sycophancy. Either way, the regulation decides.
7. **Pick the output format.** Ask for the corrected version as a shareable deliverable:

```
Create a corrected one-page summary for the compliance team as an artifact. Every requirement must include its section number. Add a short "Not covered by this summary" line at the end. Keep it under 250 words.
```

8. Then ask for a structured version for a tracking spreadsheet:

```
Now give me the requirements as a table with columns: Section | Requirement | Applies to | Deadline or period. Only include what the regulation states.
```

**What a good result looks like:** Claude's verification table catches most or all six issues, and each verdict carries a quote you can find in the source. The artifact is a clean one-pager with section numbers. The table matches the regulation line for line.

**Debrief:**

- Claude's quotes made verification fast. The verification itself happened when you found those quotes in the source. A second Claude pass without quotes would have been a self-check, which is a fake safeguard.
- The scariest errors look the most credible: a precise section number and a precise dollar figure.
- The format choice followed the audience. Compliance gets an artifact to share and file. A tracker gets structured data. A quick question gets an inline answer.
- Before this summary goes out for real, the compliance owner reviews it. Regulatory content is high stakes.

## Use cases to work through

1. **Ops lead: vendor contract summary.** Claude says termination requires 60 days' notice under clause 14.2, and the summary goes to legal. Suggested approach: open clause 14.2 and confirm the wording before sending. Ask Claude to quote every clause it cites. Legal still reviews, because contract terms are legal content.
2. **Marketer: blog post with statistics.** The draft includes "73% of team leads say..." with no source. Suggested approach: ask Claude to label every statistic as sourced or unsourced. Remove or replace unsourced numbers with figures from a source you can link. Never publish a statistic you can't trace.
3. **Consultant: client deck with a cost table.** The subtotal doesn't match the line items. Suggested approach: have Claude recompute the table with code execution, then check the input figures and formulas yourself. Running code proves the calculation ran. It does not prove the inputs were right.
4. **PM: one update, three audiences.** Suggested approach: ask for an exec version (bottom line, decision needed, under 80 words), a team version (owners and dates), and a customer-facing version (plain language). Check each against its reader's need, and route the customer version through the account owner before it goes out.

## Check yourself

1. Claude's summary of a policy document is accurate in every sentence. Why might it still fail review?
2. Which **two** of these count as real verification? (a) Asking Claude if it is sure. (b) Finding Claude's quoted sentence in the source document. (c) Running the prompt again and getting the same answer. (d) Checking the cited figure against the official report.
3. A manager wants a one-page project brief the team will edit together over the next month. Inline reply, artifact, or structured data?

<details>
<summary>Answers</summary>

1. It may leave out something material. Completeness is a separate check from accuracy, and omissions show up only when you read the source.
2. (b) and (d). Both compare the output with the source of record. Self-assessment (a) and agreement across runs (c) are not independent evidence.
3. An artifact. It is a standalone deliverable people will edit, reuse, and share.

</details>

## Official resources

- Reduce hallucinations (Anthropic docs): https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Next token prediction, where fabrication concentrates (AI Capabilities and Limitations): https://academy.claude.com/courses/ai-capabilities-and-limitations/next-token-prediction
- How AI gets its character, including sycophancy (AI Capabilities and Limitations): https://academy.claude.com/courses/ai-capabilities-and-limitations/how-ai-gets-its-character
- Can you trust what AI tells you? (Academy tutorial): https://academy.claude.com/tutorials/can-you-trust-what-ai-tells-you
- Discernment toolkit (Academy tutorial): https://academy.claude.com/tutorials/discernment-toolkit
- A closer look at Discernment (AI Fluency): https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-discernment
- Creating with artifacts (Claude 101): https://academy.claude.com/courses/claude-101/creating-with-artifacts
- Anthropic Usage Policy, high-risk use cases: https://www.anthropic.com/legal/aup
- Official prep course, Evaluating & Validating Claude's Output: https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations/evaluating-validating-claudes-output

---

**Next:** [Lesson 4: Workflow Integration and Solution Design](04-workflow-integration.md)
