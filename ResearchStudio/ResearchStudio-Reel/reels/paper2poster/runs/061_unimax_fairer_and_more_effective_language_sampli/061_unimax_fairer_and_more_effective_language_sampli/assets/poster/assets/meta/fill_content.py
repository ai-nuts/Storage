#!/usr/bin/env python3
"""Disk-to-disk fill of poster.html for the UniMax poster (3col layout)."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# ---- structural block swaps (widgets) ----
BLOCKS = [
    # Problem: paragraph + callout-bar + paragraph
    ("<p>{{PROBLEM}}</p>",
     '<p>Multilingual pretraining must decide how much to train on each language — an open, '
     'expensive question with no standard answer.</p>\n'
     '        <div class="p-callout-bar">In mC4, English holds <strong>~9.7 trillion</strong> '
     'characters — over <strong>92,000×</strong> the lowest-resource language, Yoruba.</div>\n'
     '        <p>The dominant fix, <strong>temperature sampling</strong> (τ), has never been '
     'evaluated systematically across model scales.</p>'),

    # Motivation: bullets + callout-soft (teaser figure stays below)
    ("""        <ul>
          <li>{{MOTIVATION_1}}</li>
          <li>{{MOTIVATION_2}}</li>
        </ul>""",
     '        <ul>\n'
     '          <li><strong>Tail over-repeated.</strong> At τ=3.33, the lowest-resource languages '
     'are seen <strong>&gt;100×</strong> under a trillion-token budget.</li>\n'
     '          <li><strong>Head under-covered.</strong> Tuning τ for head languages still leaves '
     'high-resource coverage far from uniform.</li>\n'
     '        </ul>\n'
     '        <div class="p-callout-soft">Excessive repetition drives overfitting, risks memorizing '
     'private text, and wastes compute — and the harm grows with model size.</div>'),

    # Method: numbered steps (replace bullet ul)
    ("""        <ul>
          <li>{{METHOD_1}}</li>
          <li>{{METHOD_2}}</li>
        </ul>""",
     '        <div class="p-steps">\n'
     '          <div class="step"><strong>Sort</strong> languages ascending by corpus size; set '
     'the budget <strong>B = C</strong>.</div>\n'
     '          <div class="step"><strong>Split</strong> the remaining budget uniformly across the '
     'languages not yet allocated.</div>\n'
     '          <div class="step"><strong>Cap</strong> any language that would exceed <strong>N '
     'epochs</strong> at N·D<sub>l</sub>; free the surplus.</div>\n'
     '          <div class="step"><strong>Redistribute</strong> the freed budget uniformly among '
     'the rest. Default <strong>N=1</strong> ⇒ no repeats.</div>\n'
     '        </div>'),

    # Method: key-equation comment -> real p-eq widget
    (re.compile(r'<!-- ★ KEY EQUATION.*?empirical\)\. -->', re.DOTALL),
     '<div class="p-eq">$$U_l = \\min\\left(N\\,D_l,\\ \\frac{B}{|L|-i}\\right),\\quad '
     'B \\leftarrow B - U_l$$'
     '<span class="where">Languages sorted ascending by size; D<sub>l</sub> = characters in '
     'language l, B = remaining budget, i = index, N = max epochs (N=1 ⇒ no repeats).</span></div>'),

    # Dataset / Benchmark: stat-strip + chips
    ("""        <ul>
          <li>{{DATASET_1}}</li>
          <li>{{DATASET_2}}</li>
        </ul>""",
     '        <div class="p-stat-strip">\n'
     '          <div class="cell"><div class="v">29T</div><div class="l">characters (mC4)</div></div>\n'
     '          <div class="cell"><div class="v">107</div><div class="l">languages</div></div>\n'
     '          <div class="cell"><div class="v">9.0B</div><div class="l">documents</div></div>\n'
     '          <div class="cell"><div class="v">+35%</div><div class="l">corpus size</div></div>\n'
     '        </div>\n'
     '        <div class="p-chips">\n'
     '          <span>TyDi QA</span><span>WMT21</span><span>XNLI</span>'
     '<span>XQuAD</span><span>MLQA</span><span>PAWS-X</span>\n'
     '        </div>'),

    # Key Results: 3-column results table
    ("""        <table class="results">
          <tr><th>Method</th><th>Metric</th></tr>
          <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>
          <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>
        </table>""",
     '        <table class="results">\n'
     '          <tr><th>Sampling</th><th>TyDi QA</th><th>Δ vs τ=1</th></tr>\n'
     '          <tr><td class="method">τ = 1</td><td>81.2</td><td>—</td></tr>\n'
     '          <tr><td class="method">τ = 3.33</td><td>82.8</td><td>+1.6</td></tr>\n'
     '          <tr class="best"><td class="method">UniMax</td><td>83.1</td><td>+1.9</td></tr>\n'
     '        </table>'),

    # Takeaway: paragraph + callout-primary
    ("<p>{{TAKEAWAY}}</p>",
     '<p>Capping per-language repeats and spreading the remaining budget uniformly beats '
     'temperature sampling for multilingual pretraining — and the advantage holds as models scale.</p>\n'
     '        <div class="p-callout-primary">Cap the repeats, spread the rest uniformly: a drop-in, '
     'hyperparameter-light replacement for temperature sampling, shipped with a refreshed mC4 corpus '
     'and umT5 checkpoints.</div>'),
]

for pat, rep in BLOCKS:
    if isinstance(pat, re.Pattern):
        html, n = pat.subn(lambda m: rep, html)
    else:
        n = html.count(pat)
        html = html.replace(pat, rep)
    if n != 1:
        sys.exit(f"BLOCK match count {n} (expected 1) for: {str(pat)[:70]}")

# remove the commented-out ablation block (kills {{ABLATION_*}} tokens)
html = re.sub(r'<!--\s*═+\s*\n?\s*ABLATION STUDY.*?═+\s*-->', '', html, flags=re.DOTALL)

# ---- simple token substitutions ----
SUBS = {
    "{{TITLE}}": "UniMax: Fairer and More Effective Language Sampling for Large-Scale Multilingual Pretraining",
    "{{AUTHORS}}": ("Hyung Won Chung<sup>1</sup>, Noah Constant<sup>1</sup>, Xavier Garcia<sup>1</sup>, "
                    "Adam Roberts<sup>1</sup>, Yi Tay<sup>1</sup>, Sharan Narang<sup>1</sup>, Orhan Firat<sup>1</sup>"),
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> Google Research",
    "{{CONTACT}}": "Email: h.w.chung27@gmail.com",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{VENUE_NAME}}": "ICLR",
    "{{VENUE_YEAR}}": "2023",
    "{{LOGO_1}}": "assets/logos/google.png",
    "{{LOGO_2}}": "", "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",

    # Motivation teaser figure (Fig 2 loss curves)
    "{{TEASER_FIGURE}}": "assets/figures/figure2.png",
    "{{TEASER_CAPTION}}": ("Held-out loss over training: low-resource (yo) losses stay high under "
                           "temperature sampling, and overfitting worsens with model size."),

    # Method figure (Fig 1 signature epochs plot)
    "{{METHOD_FIGURE}}": "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": ("UniMax caps every language at ≤1 epoch (N=1); temperature sampling repeats "
                           "the lowest-resource tail dozens to 100+ times."),

    # Key Results
    "{{HEADLINE_DELTA}}": "+1.9 TyDi QA over τ=1, +0.3 over τ=3.33 (Large, ½ budget)",
    "{{SECONDARY_FIGURE}}": "assets/figures/figure4.png",
    "{{SECONDARY_CAPTION}}": ("Average TyDi QA GoldP vs model size — UniMax beats τ=3.33 and τ=1 "
                              "at every scale."),
    "{{KEY_RESULT_CONCLUSION}}": ("UniMax wins at every model size on TyDi QA and WMT21, with the "
                                  "majority of WMT21 language pairs improving."),

    # Headline Numbers (hero + supporting)
    "{{HERO_VAL}}": "29T",
    "{{HERO_LABEL}}": "characters across 107 languages",
    "{{HERO_NOTE}}": "refreshed mC4 corpus — +35% larger, released",
    "{{STAT_2_VAL}}": "83.1", "{{STAT_2_LBL}}": "TyDi QA (Large)",
    "{{STAT_3_VAL}}": ">100×", "{{STAT_3_LBL}}": "τ=3.33 tail repeats",
    "{{STAT_4_VAL}}": "9.0B", "{{STAT_4_LBL}}": "mC4 documents",

    # 3col: suppress standalone scan-to-read (QR empty -> auto-hides)
    "{{QR_PAPER}}": "", "{{QR_CODE}}": "",
}
for k, v in SUBS.items():
    html = html.replace(k, v)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
