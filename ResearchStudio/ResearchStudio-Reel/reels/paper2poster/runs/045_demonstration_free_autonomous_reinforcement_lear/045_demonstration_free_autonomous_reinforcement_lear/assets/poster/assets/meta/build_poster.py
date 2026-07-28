#!/usr/bin/env python3
"""Indirect fill for poster.html (half layout) — reads template from disk, emits only paper content."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")


def drop_section(doc, sec):
    m = re.search(rf'<div\b[^>]*\bdata-section="{re.escape(sec)}"', doc)
    if not m:
        return doc
    start = doc.rfind("<div", 0, m.end())
    i, depth = start, 0
    while i < len(doc):
        o, c = doc.find("<div", i), doc.find("</div>", i)
        if c == -1:
            return doc
        if o != -1 and o < c:
            depth += 1; i = o + 4
        else:
            depth -= 1; i = c + len("</div>")
            if depth == 0:
                while i < len(doc) and doc[i] in " \t\r\n":
                    i += 1
                return doc[:start] + doc[i:]
    return doc


REPLACEMENTS = []

# Problem — para + compact callout-bar (p-vs is too tall in a narrow column)
REPLACEMENTS.append((
    "        <p>{{PROBLEM}}</p>",
    """        <p>Standard RL resets to a fixed initial state after every episode. Real autonomous robots cannot &mdash; they must learn from one continual, <strong>non-episodic</strong> stream.</p>
        <div class="p-callout-bar">The goal: learn robotic tasks from scratch with <strong>no resets</strong> and <strong>no demonstrations</strong>.</div>"""))

# Motivation — 2 short bullets (no callout, so figure1 can fill width)
REPLACEMENTS.append((
    """        <ul>
          <li>{{MOTIVATION_1}}</li>
          <li>{{MOTIVATION_2}}</li>
        </ul>""",
    """        <ul>
          <li>Naive reset-free RL is unstable: rollouts strand the agent in arbitrary states, so every attempt starts from wildly different initial conditions.</li>
          <li>Prior reset-free methods reintroduce human effort &mdash; manual resets, reliance on chance, or (VaPRL, MEDAL) <strong>demonstrations</strong> to seed curricula and the backward objective.</li>
        </ul>
        <div class="p-callout-soft">IBC instead supplies its <em>own</em> anchor and its <em>own</em> curriculum, from its own experience.</div>"""))

# Method — 3 bullets + key-equation card
REPLACEMENTS.append((
    """        <ul>
          <li>{{METHOD_1}}</li>
          <li>{{METHOD_2}}</li>
          <li>{{METHOD_3}}</li>
        </ul>""",
    """        <ul>
          <li>Two roles alternate: a <strong>forward agent</strong> $\\pi_f$ pursues the task; an <strong>auxiliary agent</strong> $\\pi_a$ resets it toward target states.</li>
          <li>The auxiliary agent fires <strong>only on forward-agent failure</strong>, so its help fades &mdash; an <em>implicit curriculum</em>.</li>
          <li>A <strong>bidirectional curriculum</strong> solves a Wasserstein Barycenter over replay particles (Min-Cost-Max-Flow) for $K$ forward + $K$ auxiliary goals.</li>
        </ul>
        <div class="p-eq">$\\max_{\\mathcal{T},\\pi}\\big[\\,V^{\\pi}(\\mathcal{T}) - L\\cdot D(\\mathcal{T},\\mathcal{T}^{*})\\,\\big]$<span class="where">Lipschitz-relaxed RL objective; $D$ = optimal-transport distance to the target task distribution $\\mathcal{T}^{*}$.</span></div>"""))

# Key Results — supported 3-column table + callout + figure4 + conclusion
REPLACEMENTS.append((
    """        <table class="results">
          <tr><th>Method</th><th>Metric</th></tr>
          <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>
          <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>
        </table>
        <div class="callout">{{HEADLINE_DELTA}}</div>
        <p class="conclusion">{{KEY_RESULT_CONCLUSION}}</p>""",
    """        <table class="results">
          <tr><th>Method</th><th>Demos</th><th>Resets</th></tr>
          <tr><td class="method">Oracle RL (episodic)</td><td>0</td><td>required</td></tr>
          <tr><td class="method">VaPRL / MEDAL</td><td>expert</td><td>0</td></tr>
          <tr class="best"><td class="method">IBC (ours)</td><td>0</td><td>0</td></tr>
        </table>
        <div class="callout">SOTA success on all 6 environments &mdash; beats demo-using VaPRL &amp; MEDAL, approaches the episodic oracle</div>
        <figure><img src="assets/figures/figure4.png" alt=""><figcaption>Evaluation success rate vs. steps: IBC (blue) reaches the episodic oracle (dashed) while demo-free baselines stay near zero. Shading = std over 5 seeds.</figcaption></figure>
        <p class="conclusion">IBC matches oracle-level success with zero demonstrations or resets; demo-based baselines falter where task interactions are sparse (e.g. the Fetch tasks).</p>
        <p>A <strong>demonstration-free</strong> VaPRL performs far worse than the original &mdash; prior methods lean heavily on that extra data.</p>"""))

# Takeaway — narrative + mic-drop + ablation insight & limitations (fills col3)
REPLACEMENTS.append((
    "        <p>{{TAKEAWAY}}</p>",
    """        <p>By pairing a self-fading auxiliary agent with an optimal-transport bidirectional goal curriculum, <strong>IBC</strong> is the first method to learn robotic manipulation and locomotion tasks autonomously &mdash; no resets, no demonstrations &mdash; while matching approaches that rely on expert data.</p>
        <div class="p-callout-bar">First demonstration-free, reset-free autonomous RL that rivals demonstration-based methods and approaches the episodic oracle.</div>
        <p>Ablations confirm <strong>both</strong> the bidirectional curriculum and the fading auxiliary agent are necessary. IBC assumes reversible (ergodic) environments and still needs a human-specified sparse reward; a reward-free <em>C-learning</em> variant is promising future work.</p>"""))

for old, new in REPLACEMENTS:
    if old not in html:
        sys.exit(f"structural anchor not found:\n{old[:90]!r}")
    html = html.replace(old, new)

# remove the commented CONTRIBUTION block (carried {{CONTRIBUTION*}} placeholders)
html = re.sub(r'<!--\s*═+.*?CONTRIBUTION SECTION.*?═+\s*-->', '', html, flags=re.S)
# drop Dataset / Benchmark and Ablation Study (narrow col3 can't hold a 4th section;
# ablation insight folded into Takeaway).
html = drop_section(html, "dataset-benchmark")
html = drop_section(html, "ablation-study")
# fix PLAYLIST (6 sections, no dataset-benchmark / ablation-study)
html = html.replace(
    '["title", "problem", "motivation", "method", "dataset-benchmark", "key-result", "ablation-study", "takeaway"]',
    '["title", "problem", "motivation", "method", "key-result", "takeaway"]')

SUBS = {
    "{{TITLE}}": "Demonstration-free Autonomous Reinforcement Learning via Implicit and Bidirectional Curriculum",
    "{{AUTHORS}}": 'Jigang Kim<sup>1,2</sup>, Daesol Cho<sup>1,2</sup>, H. Jin Kim<sup>1,3</sup>',
    "{{AUTHOR_LEGEND}}": '<sup>1</sup> Seoul National University &nbsp;&nbsp; <sup>2</sup> AI Institute of SNU (AIIS) &nbsp;&nbsp; <sup>3</sup> ASRI',
    "{{CONTACT}}": "Email: jgkim2020@snu.ac.kr",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{VENUE_NAME}}": "ICML",
    "{{VENUE_YEAR}}": "2023",
    "{{LOGO_1}}": "assets/logos/seoul-national-university.png",
    "{{LOGO_2}}": "assets/logos/automation-and-systems-research-institute-asri.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png", "{{QR_CODE}}": "assets/qr/code.png",
    "{{TEASER_FIGURE}}": "assets/figures/figure1.png",
    "{{TEASER_CAPTION}}": "Bidirectional curriculum: the auxiliary agent stops once the agent of interest is capable, leaving only forward episodes.",
    "{{METHOD_FIGURE}}": "assets/figures/figure2.png",
    "{{METHOD_CAPTION}}": "Overview of IBC: non-episodic training alternates forward and auxiliary agents; only the forward policy π_f is deployed at episodic evaluation.",
    "{{HERO_VAL}}": "0",
    "{{HERO_LABEL}}": "demonstrations &middot; manual resets",
    "{{HERO_NOTE}}": "yet matches episodic oracle RL",
    "{{STAT_2_VAL}}": "6", "{{STAT_2_LBL}}": "sparse-reward envs",
    "{{STAT_3_VAL}}": "~10", "{{STAT_3_LBL}}": "target states (vs thousands)",
    "{{STAT_4_VAL}}": "5", "{{STAT_4_LBL}}": "seeds averaged",
}
missing = [k for k in SUBS if k not in html]
if missing:
    sys.exit(f"placeholder(s) not in template: {missing}")
for tok, val in SUBS.items():
    html = html.replace(tok, val)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
