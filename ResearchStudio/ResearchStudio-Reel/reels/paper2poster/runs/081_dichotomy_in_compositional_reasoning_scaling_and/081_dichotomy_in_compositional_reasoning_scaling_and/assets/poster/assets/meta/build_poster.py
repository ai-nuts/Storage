#!/usr/bin/env python3
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    # titlebar / metadata
    "{{TITLE}}": "Do LLMs Have Compositional Ability? Limitations and Scalability of In-Context Composition",
    "{{AUTHORS}}": "Zhuoyan Xu<sup>1</sup>, Zhenmei Shi<sup>1</sup>, Yingyu Liang<sup>1</sup>",
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> University of Wisconsin-Madison",
    "{{VENUE_NAME}}": "COLM",
    "{{VENUE_YEAR}}": "2024",
    "{{VENUE_LOGO}}": "",
    "{{CONTACT}}": "",
    "{{LOGO_1}}": "assets/logos/university-of-wisconsin-madison.png",
    "{{LOGO_2}}": "", "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",

    # Problem
    "{{PROBLEM}}": "Can an LLM that has learned two simple tasks from in-context examples automatically solve their <strong>composition</strong> — an unseen composite task — <em>without ever seeing a composite example?</em> Trivial for humans, this basic generalization is largely untested for LLMs.",

    # Motivation
    "{{MOTIVATION_1}}": "LLMs excel at individual in-context tasks, but real reasoning demands <strong>fusing skills</strong>. It is unknown whether in-context learning integrates known abilities or fails to compose them.",
    "{{MOTIVATION_2}}": "Even <strong>GPT-4</strong> and <strong>Claude 3</strong> solve each simple rule yet fail the asterisk-and-parenthesis composite; prior work offers no theory of when composition succeeds.",
    "{{TEASER_FIGURE}}": "assets/figures/figure1.png",
    "{{TEASER_CAPTION}}": "GPT-4 solves the two simple tasks (left) but fails their composite (right): correct answer <strong>SPORTS PIE</strong>, not <em>sports * pie *</em>.",

    # Method (wide, figure2 = the dichotomy plot)
    "{{METHOD_1}}": "Standard ICL with <strong>K=10</strong> simple-task demos + one test input. Four settings per composite: each <strong>simple</strong> task, <strong>composite</strong> (simple demos, composite test), and <strong>composite in-context</strong> (the gold-standard upper bound).",
    "{{METHOD_2}}": "Evaluated across the <strong>Llama-1/2/3</strong> and <strong>GPT</strong> families over many scales, on word-level, arithmetic, and translation tasks.",
    "{{METHOD_3}}": "Theory on a one-layer linear self-attention model: composition succeeds iff the two simple tasks have <strong>confined support</strong> — each occupies a separate subspace of the input embedding.",
    "{{METHOD_FIGURE}}": "assets/figures/figure2.png",
    "{{METHOD_CAPTION}}": "The four evaluation settings across model scale (Capitalization &amp; Swap): the simple <em>capital</em>/<em>swap</em> tasks stay near-perfect; the <strong>composite</strong> (red) collapses and never improves with scale, while <strong>composite in-context</strong> (orange) recovers toward the gold standard.",

    # Dataset / Benchmark (first-class: paper introduces the test suite)
    "{{DATASET_1}}": "A custom test suite of <strong>composite tasks</strong>, each built from two simple building blocks.",
    "{{DATASET_2}}": "Grouped into <strong>separable</strong> (sub-tasks on distinct input parts) vs <strong>compose-by-step</strong> (chained reasoning on shared support).",

    # Key Result (figure3 injected by later Edit) — filler tokens
    "{{BASELINE}}": "Composite (simple demos)", "{{BASELINE_NUM}}": "~20%",
    "{{OURS}}": "Composite in-context", "{{OURS_NUM}}": "~90%",
    "{{HEADLINE_DELTA}}": "~90% on simple tasks → ~20% on the composite — with no gain from scale.",
    "{{KEY_RESULT_CONCLUSION}}": "Models have the representational power but fail to compose it from simple-task demos alone.",

    # Ablation (table injected by later Edit) — filler tokens
    "{{ABLATION_1}}": "Scaling within a family splits the two regimes: separable tasks rise with scale; compose-by-step tasks stay flat.",
    "{{ABLATION_2}}": "Swapping simple-task demos for composite in-context demos recovers accuracy.",
    "{{ABLATION_CONCLUSION}}": "Larger models help a composite task only when the underlying simple tasks improve — matching the confined-support theory.",

    # Headline Numbers
    "{{HERO_VAL}}": "~90% → ~20%",
    "{{HERO_LABEL}}": "Simple → compose-by-step accuracy (Llama)",
    "{{HERO_NOTE}}": "no gain from scaling",
    "{{STAT_2_VAL}}": "44%", "{{STAT_2_LBL}}": "(A)+(C) at larger scale",
    "{{STAT_3_VAL}}": "66%", "{{STAT_3_LBL}}": "(B)+(D) at larger scale",
    "{{STAT_4_VAL}}": "K=10", "{{STAT_4_LBL}}": "in-context examples",

    # Contribution — lives inside an HTML comment (lean render drops the section); blank the tokens
    "{{CONTRIBUTION_1}}": "", "{{CONTRIBUTION_2}}": "", "{{CONTRIBUTION_3}}": "",

    # Takeaway
    "{{TAKEAWAY}}": "LLMs compose two skills only when the sub-tasks act on <strong>separate parts</strong> of the input; for tasks needing chained multi-step reasoning they fail, and scaling does not rescue them.",
}

missing = [k for k in SUBS if k not in html]
if missing:
    sys.exit(f"placeholder(s) not in template: {missing}")
for token, value in SUBS.items():
    html = html.replace(token, value)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
