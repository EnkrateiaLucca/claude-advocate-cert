# /// script
# requires-python = ">=3.11"
# ///
"""Build study-guide/ccao-f-study-guide.html; render to PDF with headless Chrome (see README)."""
from pathlib import Path

# ---------- figures (rebuilt from course material) ----------
FIG_PROMPT = """
<div class="fig"><div class="fig-t">Figure · Weak vs. strong prompt</div>
<div class="pbox weak"><span class="lbl">Weak prompt: everything left implicit</span>
"Write a summary of our quarterly operations."
<p class="note">Claude returns three plausible paragraphs that could describe almost any company. No audience, figures, format or priorities. The output is not wrong. It is unusable, because the prompt specified almost nothing.</p></div>
<div class="pbox strong"><span class="lbl">Strong prompt: components made explicit</span>
"You are an operations analyst <i class="tag">(role)</i>. I am preparing a one-page update for our regional director, who cares about throughput and cost, not process detail <i class="tag">(context and audience)</i>. Summarize the attached Q3 operations data <i class="tag">(task)</i>, covering only the three metrics that moved more than 10 percent against target <i class="tag">(constraint)</i>. Format as a short headline followed by three bullet points, each one sentence <i class="tag">(output format)</i>."</div>
</div>"""

FIG_DIAG = """
<div class="fig"><div class="fig-t">Figure · Output deficiencies are prompt diagnostics</div>
<table><thead><tr><th>Symptom</th><th>Likely cause</th><th>Fix</th></tr></thead><tbody>
<tr><td>Output is generic or off-base</td><td>The context was thin</td><td>Add the background Claude could not infer</td></tr>
<tr><td>Output answered the wrong question</td><td>The task verb was ambiguous</td><td>Sharpen the instruction</td></tr>
<tr><td>Output is the wrong length, tone or shape</td><td>A constraint or the format was missing</td><td>Add it</td></tr>
<tr><td>Output is close but misses on one section</td><td>—</td><td>Iterate on that section only. Do not discard a draft that is mostly right</td></tr>
</tbody></table></div>"""

FIG_ITER = """
<div class="fig"><div class="fig-t">Worked example · A live iteration cycle</div>
<div class="rounds">
<div class="rd"><span class="lbl">Round 1 prompt</span>"Write a follow-up email to the client about the delayed deliverable."</div>
<div class="rd out"><span class="lbl">Round 1 output</span>A generic, slightly defensive three-paragraph email that never says when the deliverable will arrive or why it slipped. <b>Diagnosis:</b> thin context (no reason, no new date) and no tone constraint.</div>
<div class="rd"><span class="lbl">Round 2 prompt</span>"Write a follow-up to the client about the two-day delay on the analytics deliverable. The cause was a data-quality issue we have now fixed; new delivery is Thursday. Tone: accountable, not over-apologetic. Keep it under 120 words."</div>
<div class="rd out"><span class="lbl">Round 2 output</span>A tight, accountable note with the cause, the new date and a confident close. <b>Diagnosis:</b> strong. Only the subject line is missing.</div>
<div class="rd"><span class="lbl">Round 3 prompt</span>"Good. Add a subject line that signals resolution, not just delay."</div>
</div>
<p class="note">The lesson: fix the specific component the output exposed. Do not restart from scratch.</p></div>"""

FIG_STRATEGY = """
<div class="fig"><div class="fig-t">Figure · Strategy quick reference</div>
<table><thead><tr><th>Task type</th><th>What to tighten</th><th>What to loosen</th><th>Latitude</th></tr></thead><tbody>
<tr><td>Analysis</td><td>Criteria, standards, scope</td><td>Phrasing</td><td><span class="meter m1"></span>Low</td></tr>
<tr><td>Research</td><td>Question, sources, citations</td><td>Synthesis approach</td><td><span class="meter m2"></span>Low–med</td></tr>
<tr><td>Drafting</td><td>Audience, tone, format</td><td>Word choice</td><td><span class="meter m3"></span>Medium</td></tr>
<tr><td>Brainstorming</td><td>Goal and guardrails only</td><td>Quantity and direction</td><td><span class="meter m4"></span>High</td></tr>
</tbody></table>
<p class="note">Research tip: web search in chat covers quick currency needs. Deep multi-source investigation points to the Research feature (paid plans).</p></div>"""

FIG_RISK = """
<div class="fig"><div class="fig-t">Figure · Four risk thresholds for reviewing AI output</div>
<table><thead><tr><th>Threshold</th><th>What to ask</th></tr></thead><tbody>
<tr><td>Stakes</td><td>What is the cost if this is wrong? High-cost errors demand human review regardless of how confident the output appears.</td></tr>
<tr><td>Reversibility</td><td>Can the action be undone? An irreversible step (a sent client deliverable, a filed report) clears a higher bar than a draft you can revise.</td></tr>
<tr><td>Audience</td><td>Who sees it? External, executive and regulatory audiences raise the review requirement above internal working drafts.</td></tr>
<tr><td>Regulatory exposure</td><td>Does a rule, contract or law govern this? Regulated content carries obligations that AI assistance does not remove.</td></tr>
</tbody></table></div>"""

FIG_CTX = """
<div class="fig"><div class="fig-t">Figure · What fills one request's context window</div>
<div class="stack">
<span class="seg in">System prompt</span><span class="seg in">Messages · files · tool results</span><span class="seg in">Tool definitions</span><span class="seg outp">Output</span><span class="seg think">Thinking</span>
</div>
<p class="note"><b>input + output + reasoning ≤ model window.</b> The chat product (claude.ai, ChatGPT, Gemini app) may cap you lower than the model's advertised maximum.</p></div>"""

# ---------- domains: (code, title, weight, intro, [items]) ----------
# item = ("q", question, answer, source) | ("fig", html)
DOMAINS = [
 ("D1", "Prompting and Task Execution", "14%",
  "Build prompts from explicit components, decompose multi-part work, diagnose weak output and adapt your strategy to the task type.", [
  ("q", "What are the five components of a well-built prompt?",
   "<ol><li><b>Role</b></li><li><b>Context</b> (including audience)</li><li><b>Task</b></li><li><b>Constraints</b></li><li><b>Output format</b></li></ol>", ""),
  ("fig", FIG_PROMPT),
  ("q", "A communications manager must turn a dense 20-page policy change into a staff announcement, a staff FAQ and a short executive briefing. Decompose this into an ordered sequence of steps to run with Claude.",
   "<ol><li><b>Extract</b> the substantive changes and what each one means in practice.</li><li><b>Confirm</b> the extraction is complete and accurate before building on it.</li><li><b>Draft the staff announcement</b> from the confirmed change list, tuned to a general audience.</li><li><b>Draft the FAQ</b>, anticipating the questions staff will ask.</li><li><b>Draft the executive briefing</b>, compressed to decisions and impact.</li></ol><p class='why'>Key idea: verify the shared foundation once, then build every deliverable on it.</p>", ""),
  ("fig", FIG_DIAG),
  ("q", "Claude's output is generic and off-base. What is the likely cause and the fix?",
   "Cause: <b>thin context</b>. Fix: <b>add the background Claude could not infer.</b>", "Prompt diagnostics"),
  ("q", "Claude answered the wrong question. What is the likely cause and the fix?",
   "Cause: <b>an ambiguous task verb</b>. Fix: <b>sharpen the instruction.</b>", "Prompt diagnostics"),
  ("q", "A draft is close but misses on one section. What should you do?",
   "<b>Iterate on that section only.</b> Do not discard a draft that is mostly right.", "Prompt diagnostics"),
  ("fig", FIG_ITER),
  ("q", "What are the four core task types for everyday chat use of Claude?",
   "<b>Analysis · Research · Drafting · Brainstorming</b>", ""),
  ("q", "When you set up an <u>analysis</u> prompt, what three things do you spell out?",
   "<b>What to measure</b>, <b>the standard to measure it against</b> and <b>how to handle ambiguity</b>. Low creative latitude, high specification.", "Prompt configuration by task type"),
  ("q", "When you set up a <u>research</u> prompt, what do you define up front and what do you ask for in the output?",
   "Define <b>the question, its boundaries and whether current sources are required</b>. Ask for <b>citations</b> so you can check the claims.", "Prompt configuration by task type"),
  ("q", "In a <u>drafting</u> prompt, what do you specify and what do you leave to Claude?",
   "You specify <b>audience, tone and format</b>. Claude finds <b>the phrasing</b>. You control the shape; Claude fills it.", "Prompt configuration by task type"),
  ("q", "How do you set up a <u>brainstorming</u> chat, and why keep it loose?",
   "Give <b>the goal and the boundaries</b>, then ask for <b>many varied ideas</b> before narrowing. Too many constraints kill the variety you want.", "Prompt configuration by task type"),
  ("fig", FIG_STRATEGY),
  ("q", "Name the three ways to format Claude's output by purpose.",
   "<b>Inline</b> · <b>Artifact</b> · <b>Structured format</b> (table, JSON, CSV and similar)", "Format by purpose"),
  ("q", "What separates an artifact from an inline reply?",
   "An artifact is a <b>standalone deliverable</b> you edit and reuse. An inline reply is contextual and gets used up in the chat.", "Format by purpose"),
 ]),
 ("D2", "Output Evaluation and Validation", "21%",
  "Spot hallucination patterns, tune prompts for verifiability, check output with concrete techniques and decide what must never ship without human review.", [
  ("q", "Describe in one sentence the hallucination pattern called <i>plausible-but-unsupported claims</i>.",
   "A statement that sounds reasonable and fits the topic but has <b>no basis in the source or in fact</b>. It is the most dangerous kind because nothing about it looks wrong.", ""),
  ("q", "Your prompt implies a preferred answer and Claude agrees a little too readily on a question that should be open. What is this an example of?",
   "<b>Confirmation bias in framing</b>: the way you phrased the question steered the answer.", ""),
  ("q", "What are the three techniques to tune a prompt for verifiability, and how do you implement each?",
   "<ol><li><b>Permit \"I don't know\"</b>: tell Claude it may say so (works well in a system prompt or Project instructions).</li><li><b>Restrict to provided sources</b>: attach the documents or links and tell Claude to answer only from them.</li><li><b>Require auditable citations</b>: ask for direct quotes from the PDF or traceable links to the exact section of a page.</li></ol>", ""),
  ("q", "Name three ways to check Claude's output.",
   "<b>Quote first, then analyze</b> · <b>Best-of-N comparison</b> · <b>Validate against an authoritative source</b>", "Anthropic docs: Reduce hallucinations"),
  ("q", "Before Claude analyzes a long document, what should you ask it to do first?",
   "Extract the <b>word-for-word quotes</b> that support the task, then analyze using only those quotes. Anthropic suggests this for documents over ~20k tokens.", "Anthropic docs: Reduce hallucinations"),
  ("q", "Why does quote-first analysis make Claude's output easier to check?",
   "Each conclusion ties to a pulled quote, so the reasoning and the errors become <b>visible</b>. You can check each quote against the source.", "Anthropic docs: Reduce hallucinations"),
  ("q", "Best-of-N: after re-running the same request several times, how do you read the results?",
   "<b>Agreement</b> raises confidence. <b>Divergence</b> marks a soft spot that needs a human look (a possible hallucination).", "Anthropic docs: Reduce hallucinations"),
  ("q", "Why isn't a second Claude response enough to validate a claim that matters?",
   "It is <b>not independent</b> and can repeat the same error. Check against a <b>trusted external reference</b>.", "Anthropic docs: \"Always validate critical information\""),
  ("q", "You're about to act on a figure Claude produced in a spreadsheet. Which in-product aid helps you validate it?",
   "<b>Claude for Excel's cell-level citations</b>, which tie each figure back to its input cells.", ""),
  ("q", "What belongs on the <i>do-not-ship-without-review</i> list? (Decide it in advance and treat it as fixed.)",
   "<ul><li>Final client deliverables</li><li>Audit-critical or financially material calculations</li><li>Anything with regulated, confidential or highly sensitive data</li><li>Public or legal communications where a misstatement has lasting consequences</li></ul>", ""),
  ("fig", FIG_RISK),
  ("q", "Risk threshold <u>Stakes</u>: what question do you ask?",
   "<b>What is the cost if this is wrong?</b> High-cost errors demand human review however confident the output looks.", "Four risk thresholds"),
  ("q", "Risk threshold <u>Reversibility</u>: what question do you ask?",
   "<b>Can the action be undone?</b> A sent client deliverable or a filed report clears a higher bar than a revisable draft.", "Four risk thresholds"),
  ("q", "Risk threshold <u>Audience</u>: what question do you ask?",
   "<b>Who sees it?</b> External, executive and regulatory audiences raise the review requirement above internal drafts.", "Four risk thresholds"),
  ("q", "Risk threshold <u>Regulatory exposure</u>: what question do you ask?",
   "<b>Does a rule, contract or law govern this?</b> Regulated content carries obligations that AI assistance does not remove.", "Four risk thresholds"),
 ]),
 ("D3", "Platform and Model Selection", "12%",
  "Know what a context window holds and how the chat product's limits differ from the model's.", [
  ("fig", FIG_CTX),
  ("q", "What counts toward a model's context window in a single API request?",
   "Everything sent <b>plus</b> everything generated: system prompt + messages (including tool results and files) + tool definitions + output + thinking tokens.", "Anthropic docs: Context windows"),
  ("q", "Model context window vs. chat-product context window: which one limits you in the app, and how do they relate?",
   "The <b>product's cap</b> limits you. The model window is the hard ceiling for one request. The product sets its own cap per plan and model, and that cap can sit <b>below</b> the model's maximum.", "Anthropic docs; Claude Help Center"),
  ("q", "A chat app loses early details in a long conversation even though its model advertises 1M tokens. What should you suspect first?",
   "The <b>product's cap</b> for your plan and model, plus the app <b>trimming old turns</b> (rolling first-in-first-out). The model's advertised max is not what the app gives you.", "Anthropic docs: Context windows"),
 ]),
 ("D6", "Governance and Responsible Use", "15%",
  "Match data-handling controls to the sensitivity of the task.", [
  ("q", "When is redaction the wrong tool for making data usable?",
   "When the task <b>genuinely depends on the sensitive specifics</b> you would remove.", "Data sensitivity and privacy controls"),
  ("q", "Incognito keeps a chat out of Memory and chat history. Which separate control still applies to Incognito chats and can surface them in org data exports?",
   "<b>The organization's data-retention policy.</b>", "Data sensitivity and privacy controls"),
 ]),
]

CSS = """
:root{--cream:#f5f0e6;--paper:#fbf8f1;--line:#ddd5c0;--ink:#1a1a1a;--ink-2:#444;--muted:#6b6559;--accent:#b85c1f;--gold:#d9a441;--ans:#eef3ea;--ans-line:#b9cdb0}
@page{size:Letter;margin:.5in .55in .55in;
 @bottom-left{content:"CCAO-F Visual Study Guide · Claude Certified Associate – Foundations";font:600 7pt Inter,sans-serif;color:#8a8478}
 @bottom-right{content:counter(page) " / " counter(pages);font:600 7pt Inter,sans-serif;color:#8a8478}}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{margin:0;padding:0}
body{font-family:Inter,-apple-system,'Helvetica Neue',Arial,sans-serif;font-size:10pt;line-height:1.4;color:var(--ink);background:#fff}
@media screen{body{max-width:8.5in;margin:20px auto;padding:0 16px}}
h1,h2,h3,p,ol,ul{margin:0}
ol,ul{padding-left:1.25em} li{margin:1px 0}
.masthead{background:var(--ink);color:var(--cream);padding:22px 24px 20px;border-radius:6px;border-top:6px solid var(--gold)}
.kicker{color:var(--gold);font-size:8pt;font-weight:700;letter-spacing:.16em;text-transform:uppercase}
.masthead h1{font-size:26pt;font-weight:800;line-height:1.1;margin:6px 0 8px}
.masthead p{color:#c9c4b5;font-size:10pt;max-width:5.6in}
.howto{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:16px 0}
.tile{background:var(--cream);border:1px solid var(--line);border-radius:4px;padding:10px 12px}
.tile b{display:block;color:var(--accent);font-size:8pt;text-transform:uppercase;letter-spacing:.08em;margin-bottom:3px}
.toc{border-top:2px solid var(--ink);padding-top:8px}
.toc-row{display:flex;align-items:center;gap:10px;padding:7px 0;border-bottom:1px solid var(--line)}
.toc-row .bar{height:8px;background:var(--gold);border-radius:4px}
.code{background:var(--accent);color:#fff;font-weight:800;font-size:9.5pt;padding:2px 8px;border-radius:3px}
.dom{margin-top:18px}
.dom:first-of-type{break-before:page;margin-top:0}
.dom-h,.intro{break-after:avoid}
.dom-h{display:flex;align-items:baseline;gap:10px;border-bottom:3px solid var(--ink);padding-bottom:4px;margin-bottom:6px}
.dom-h h2{font-size:17pt;font-weight:800}
.dom-h .w{margin-left:auto;color:var(--muted);font-weight:600;font-size:9pt}
.dom-h .w b{color:var(--accent)}
.intro{color:var(--ink-2);font-size:9.5pt;margin-bottom:12px}
.q{border:1px solid var(--line);border-radius:5px;margin:0 0 10px;break-inside:avoid;overflow:hidden}
.q .qt{background:var(--paper);padding:8px 12px;display:flex;gap:10px;font-weight:600}
.q .num{flex:none;background:var(--ink);color:var(--cream);font-size:8pt;font-weight:800;border-radius:3px;padding:2px 6px;height:fit-content;margin-top:1px}
.q .at{background:var(--ans);border-top:1px dashed var(--ans-line);padding:6px 12px 8px 60px;text-indent:-48px}
.q .at:before{content:"ANSWER";display:inline-block;width:48px;text-indent:0;font-size:6pt;font-weight:800;letter-spacing:.06em;color:#5e7a52}
.q .at ol,.q .at ul,.q .at .src,.q .at .why{text-indent:0}
.q .src{font-size:7.5pt;color:var(--muted);margin-top:3px}
.why{margin-top:4px;color:var(--ink-2);font-style:italic}
.fig{background:#fff;border:1.5px solid var(--ink);border-radius:5px;padding:10px 12px;margin:4px 0 14px;break-inside:avoid}
.fig-t{font-size:8pt;font-weight:800;color:var(--accent);text-transform:uppercase;letter-spacing:.08em;margin-bottom:7px}
.fig .note{font-size:8.5pt;color:var(--ink-2);margin-top:6px}
table{width:100%;border-collapse:collapse;font-size:9pt;line-height:1.3}
th{background:var(--ink);color:var(--cream);text-align:left;padding:4px 7px;font-size:8.5pt}
td{padding:4px 7px;border-bottom:1px solid var(--line);vertical-align:top}
tbody tr:nth-child(even) td{background:rgba(235,228,212,.45)}
td:first-child{font-weight:700}
.meter{display:inline-block;height:7px;border-radius:4px;background:var(--gold);margin-right:6px;vertical-align:middle}
.m1{width:10px}.m2{width:20px}.m3{width:32px}.m4{width:48px}
.pbox{border-radius:4px;padding:8px 10px;margin-bottom:8px;font-size:9.5pt}
.pbox .lbl,.rd .lbl{display:block;font-size:7pt;font-weight:800;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px}
.pbox.weak{background:#fbefe4;border-left:4px solid var(--accent)} .pbox.weak .lbl{color:var(--accent)}
.pbox.strong{background:var(--ans);border-left:4px solid #5e7a52;margin-bottom:0} .pbox.strong .lbl{color:#5e7a52}
.tag{color:var(--accent);font-weight:600}
.rounds{display:grid;gap:5px}
.rd{background:var(--paper);border-left:4px solid var(--gold);padding:6px 10px;font-size:9pt}
.rd.out{background:#fff;border-left-color:var(--line);margin-left:22px}
.rd .lbl{color:var(--muted)}
.stack{display:flex;border-radius:4px;overflow:hidden;font-size:8pt;font-weight:700;color:#fff;text-align:center}
.seg{padding:9px 4px;flex:1}
.seg.in{background:#4a4a4a}.seg.in:nth-child(2){flex:1.6;background:#333}.seg.outp{background:var(--accent)}.seg.think{background:var(--gold);color:var(--ink)}
.drill{break-before:page}
.drill ol{columns:2;column-gap:22px;font-size:9pt;padding-left:1.6em}
.drill li{break-inside:avoid;margin-bottom:6px}
.drill .d{font-size:7.5pt;font-weight:800;color:var(--accent)}
"""


def build():
    n = 0
    body, drill = [], []
    total_q = sum(1 for d in DOMAINS for it in d[4] if it[0] == "q")
    toc = "".join(
        f'<div class="toc-row"><span class="code">{c}</span><b style="flex:1">{t}</b>'
        f'<span class="bar" style="width:{float(w[:-1])*6}px"></span><span class="muted">{w} of exam · '
        f'{sum(1 for it in items if it[0]=="q")} questions</span></div>'
        for c, t, w, _, items in DOMAINS)
    for code, title, weight, intro, items in DOMAINS:
        body.append(f'<section class="dom"><div class="dom-h"><span class="code">{code}</span><h2>{title}</h2>'
                    f'<span class="w">Exam weight <b>{weight}</b></span></div><p class="intro">{intro}</p>')
        for it in items:
            if it[0] == "fig":
                body.append(it[1]); continue
            _, q, a, src = it
            n += 1
            s = f'<div class="src">Source: {src}</div>' if src else ""
            body.append(f'<div class="q"><div class="qt"><span class="num">Q{n}</span><div>{q}</div></div>'
                        f'<div class="at">{a}{s}</div></div>')
            drill.append(f'<li><span class="d">{code}</span> {q}</li>')
        body.append("</section>")
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>CCAO-F Study Guide</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="masthead"><div class="kicker">Claude Certified Associate – Foundations · CCAO-F</div>
<h1>Visual Study Guide:<br>Quiz Questions with Answers</h1>
<p>{total_q} exam-style recall questions with worked examples and reference tables, organized by exam domain.</p></div>
<div class="howto">
<div class="tile"><b>1 · Cover</b>Cover the green answer box. Answer each question out loud or on paper.</div>
<div class="tile"><b>2 · Check</b>Reveal the answer. Mark any question you missed or hesitated on.</div>
<div class="tile"><b>3 · Drill</b>Use the question-only list on the last page for a closed-book pass before exam day.</div>
</div>
<div class="toc">{toc}</div>
{''.join(body)}
<section class="drill"><div class="dom-h"><h2>Closed-book drill</h2><span class="w">Questions only · answers in the domain sections</span></div>
<ol>{''.join(drill)}</ol></section>
</body></html>"""


if __name__ == "__main__":
    out = Path(__file__).with_name("ccao-f-study-guide.html")
    out.write_text(build())
    print(out)
