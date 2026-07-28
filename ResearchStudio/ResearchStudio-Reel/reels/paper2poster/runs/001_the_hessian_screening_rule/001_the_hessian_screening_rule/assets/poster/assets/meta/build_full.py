#!/usr/bin/env python3
"""Comprehensive content build for the Hessian Screening Rule poster.
   Replaces template placeholder blocks with the final widget-rich content in one pass,
   drops unused optional sections, and applies the column/scan CSS tweaks."""
import re
import sys
from pathlib import Path

p = Path(sys.argv[1])
h = p.read_text(encoding="utf-8")


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
            depth -= 1; i = c + 6
            if depth == 0:
                while i < len(doc) and doc[i] in " \t\r\n":
                    i += 1
                return doc[:start] + doc[i:]
    return doc


# --- block replacements (structure + content together) ---
REPL = []

# Problem
REPL.append((
    "        <p>{{PROBLEM}}</p>",
    '        <p>Fitting the lasso along a full regularization path is costly: the optimal penalty λ is unknown, so it is tuned by cross-validation — refitting the whole path repeatedly over high-dimensional data.</p>\n'
    '        <div class="p-callout-bar">Screening rules discard predictors before the solver runs — but existing rules screen conservatively under high correlation.</div>'
))

# Motivation (3 bullets + callout, no teaser figure)
REPL.append((
    '        <ul>\n          <li>{{MOTIVATION_1}}</li>\n          <li>{{MOTIVATION_2}}</li>\n        </ul>\n'
    '        <!-- OPTIONAL: half-column Motivation figure. If the spec\'s Motivation figure line is `**Figure:** none`, REMOVE this entire <figure> block. -->\n'
    '        <figure><img src="{{TEASER_FIGURE}}" alt=""><figcaption>{{TEASER_CAPTION}}</figcaption></figure>',
    '        <ul>\n'
    '          <li>Sequential rules (the <strong>strong rule</strong>, <strong>working-set</strong>) rely on a <em>first-order</em> estimate of the next-step correlation.</li>\n'
    '          <li>That crudeness <strong>over-screens</strong> and yields <strong>inaccurate warm starts</strong>, forcing costly KKT re-checks and extra solver passes.</li>\n'
    '          <li>Both are really next-step gradient estimates — improved directly by second-order curvature.</li>\n'
    '        </ul>\n'
    '        <div class="p-callout-soft">Both weaknesses share one root — a first-order guess — fixable with curvature.</div>'
))

# Method (3 bullets + 2 equations + 2 figures)
REPL.append((
    '        <ul>\n          <li>{{METHOD_1}}</li>\n          <li>{{METHOD_2}}</li>\n          <li>{{METHOD_3}}</li>\n        </ul>\n'
    '        <figure><img src="{{METHOD_FIGURE}}" alt="half"><figcaption>{{METHOD_CAPTION}}</figcaption></figure>',
    '        <ul>\n'
    '          <li>On any interval where the active set is fixed, the lasso solution is <strong>linear in λ</strong>, so the Hessian gives a <strong>second-order</strong> estimate of the next-step correlation.</li>\n'
    '          <li>The same Hessian inverse gives a <strong>warm start that is exact</strong> while the active set is fixed, so a <span class="hi">single coordinate-descent sweep</span> usually suffices per path step.</li>\n'
    '          <li>Restrict inner products to the strong-rule set for cost; maintain <strong>H</strong> and <strong>H⁻¹</strong> by low-rank updates; place the λ grid by approximate homotopy.</li>\n'
    '        </ul>\n'
    '        <div class="p-eq">\n'
    '          $$\\hat{c}_H(\\lambda_{k+1}) = c(\\lambda_k) + (\\lambda_{k+1}-\\lambda_k)\\, X^{\\mathsf{T}} X_{A_k}\\,(X_{A_k}^{\\mathsf{T}} X_{A_k})^{-1}\\,\\operatorname{sign}\\hat{\\beta}(\\lambda_k)_{A_k}$$\n'
    '          <span class="where">second-order screening estimate of the next-step correlation</span>\n'
    '          $$\\hat{\\beta}(\\lambda_{k+1})_{A_k} = \\hat{\\beta}(\\lambda_k)_{A_k} + (\\lambda_k-\\lambda_{k+1})\\,H_{A_k}^{-1}\\,\\operatorname{sign}\\hat{\\beta}(\\lambda_k)_{A_k}$$\n'
    '          <span class="where">Hessian warm start — exact while the active set is fixed</span>\n'
    '        </div>\n'
    '        <figure><img src="assets/figures/figure1.png" alt="half"><figcaption>Predictors screened vs. path step at correlation ρ ∈ {0, 0.4, 0.8} (n = 200, p = 20000). The Hessian rule (black) hugs the true active-set floor (dashed); rivals keep orders of magnitude more.</figcaption></figure>\n'
    '        <figure><img src="assets/figures/figure2.png" alt="half"><figcaption>Coordinate-descent passes along the path on colon-cancer and YearPredictionMSD: Hessian warm starts (orange) collapse to ~one pass per step vs. standard warm starts (black).</figcaption></figure>'
))

# Key Results (multi-col table + callout + fig3 + conclusion + stat-strip)
REPL.append((
    '        <table class="results">\n'
    '          <tr><th>Method</th><th>Metric</th></tr>\n'
    '          <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>\n'
    '          <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>\n'
    '        </table>\n'
    '        <div class="callout">{{HEADLINE_DELTA}}</div>\n'
    '        <p class="conclusion">{{KEY_RESULT_CONCLUSION}}</p>',
    '        <table class="p-table">\n'
    '          <tr><th>Path-fit time (s)</th><th>Hessian</th><th>Working</th><th>Celer</th><th>Blitz</th></tr>\n'
    '          <tr class="best"><td>YearPredictionMSD</td><td>78.8</td><td>541</td><td>712</td><td>706</td></tr>\n'
    '          <tr><td>e2006-tfidf</td><td>14.3</td><td>143</td><td>335</td><td>277</td></tr>\n'
    '          <tr><td>e2006-log1p</td><td>205</td><td>438</td><td>835</td><td>756</td></tr>\n'
    '          <tr><td>bcTCGA</td><td>3.00</td><td>7.67</td><td>10.6</td><td>11.7</td></tr>\n'
    '          <tr><td>scheetz</td><td>0.369</td><td>0.643</td><td>0.801</td><td>0.706</td></tr>\n'
    '          <tr><td>colon-cancer</td><td>0.054</td><td>0.134</td><td>0.169</td><td>0.177</td></tr>\n'
    '          <tr><td>duke-breast-cancer</td><td>0.111</td><td>0.210</td><td>0.262</td><td>0.251</td></tr>\n'
    '          <tr><td>arcene</td><td>4.35</td><td>3.27</td><td>3.99</td><td>4.42</td></tr>\n'
    '        </table>\n'
    '        <div class="callout">≈ 7–10× faster than the best prior method on the largest real data sets, and fastest in every simulated configuration</div>\n'
    '        <figure><img src="assets/figures/figure3.png" alt="half"><figcaption>Relative path-fit time vs. correlation ρ for ℓ₁ least-squares and logistic regression; time is relative to the fastest per group. Hessian (grey) is lowest in every panel.</figcaption></figure>\n'
    '        <p class="conclusion">Fastest in every simulated setting and on nearly all 12 real data sets: on YearPredictionMSD, 78.8 s vs 541 s for the runner-up — in all but one least-squares case, under half its time.</p>\n'
    '        <div class="p-stat-strip">\n'
    '          <div class="cell"><div class="v">5/5</div><div class="l">least-squares sets won</div></div>\n'
    '          <div class="cell"><div class="v">&lt;½</div><div class="l">runner-up time (4/5)</div></div>\n'
    '          <div class="cell"><div class="v">3×2</div><div class="l">sim. settings, all won</div></div>\n'
    '        </div>'
))

# Ablation (key-stat + conclusion)
REPL.append((
    '        <ul>\n          <li>{{ABLATION_1}}</li>\n          <li>{{ABLATION_2}}</li>\n        </ul>\n'
    '        <p class="conclusion">{{ABLATION_CONCLUSION}}</p>',
    '        <div class="p-key-stat">\n'
    '          <div class="num">10³–10⁴×</div>\n'
    '          <div class="label">fewer predictors screened than rivals</div>\n'
    '        </div>\n'
    '        <p class="conclusion"><strong>Warm start:</strong> also cuts coordinate descent to ~1 pass/step.</p>'
))

# Takeaway (p + callout-primary)
REPL.append((
    "        <p>{{TAKEAWAY}}</p>",
    '        <p>Reusing second-order Hessian information pays off twice — tighter screening and near-exact warm starts.</p>\n'
    '        <div class="p-callout-primary">One Hessian, double duty — the fastest lasso &amp; ℓ₁-logistic path solver, especially under high correlation.</div>'
))

# Scan directory: add a Contact link beside the (empty) Project link
REPL.append((
    '      <div class="scan-links">\n        <div class="scan-link" data-url="{{URL_PROJECT}}"><span class="lk-label">Project</span><span class="lk-url">{{URL_PROJECT}}</span></div>\n      </div>',
    '      <div class="scan-links">\n'
    '        <div class="scan-link" data-url="{{URL_PROJECT}}"><span class="lk-label">Project</span><span class="lk-url">{{URL_PROJECT}}</span></div>\n'
    '        <div class="scan-link" data-url="johan.larsson@stat.lu.se"><span class="lk-label">Contact</span><span class="lk-url">johan.larsson@stat.lu.se</span></div>\n'
    '      </div>'
))

for old, new in REPL:
    if old not in h:
        sys.exit(f"BLOCK NOT FOUND:\n{old[:120]}...")
    h = h.replace(old, new, 1)

# --- simple token fills (header/meta + headline numbers) ---
SUBS = {
    "{{TITLE}}": "The Hessian Screening Rule",
    "{{AUTHORS}}": "Johan Larsson<sup>1</sup>, Jonas Wallin<sup>1</sup>",
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> Department of Statistics, Lund University",
    "{{VENUE_NAME}}": "NeurIPS", "{{VENUE_YEAR}}": "2022",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "Email: johan.larsson@stat.lu.se",
    "{{LOGO_1}}": "assets/logos/lund-university.png",
    "{{LOGO_2}}": "", "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png", "{{QR_CODE}}": "assets/qr/code.png",
    "{{URL_PROJECT}}": "",
    "{{HERO_VAL}}": "≈10×", "{{HERO_LABEL}}": "Faster · e2006-tfidf",
    "{{HERO_NOTE}}": "14.3 s vs 143 s — the biggest real-data speedup",
    "{{STAT_2_VAL}}": "6.9×", "{{STAT_2_LBL}}": "YearPredMSD",
    "{{STAT_3_VAL}}": "2.6×", "{{STAT_3_LBL}}": "bcTCGA",
    "{{STAT_4_VAL}}": "4.8×", "{{STAT_4_LBL}}": "madelon",
}
for k, v in SUBS.items():
    h = h.replace(k, v)

# --- drop unused optional sections + PLAYLIST ids ---
for sec in ["contribution", "dataset-benchmark"]:
    h = drop_section(h, sec)
    h = re.sub(rf'"{re.escape(sec)}"\s*,?\s*', "", h)

# PLAYLIST: keep title..takeaway incl ablation-study, drop contribution/dataset
h = h.replace(
    'const PLAYLIST = ["title", "problem", "motivation", "contribution", "method", "dataset-benchmark", "key-result", "ablation-study", "takeaway"];',
    'const PLAYLIST = ["title", "problem", "motivation", "method", "key-result", "ablation-study", "takeaway"];')

# --- CSS tweaks that balanced col3 / scan in the fill loop ---
h = h.replace(
    "  .col {\n    display: flex;\n    flex-direction: column;\n    gap: 28pt;\n    min-height: 0;\n  }",
    "  .col {\n    display: flex;\n    flex-direction: column;\n    gap: 28pt;\n    min-height: 0;\n  }\n"
    "  .columns > .col:last-child { gap: 7pt; }\n"
    "  .columns > .col:first-child { gap: 20pt; }")
h = h.replace(
    '  .section[data-section="scan-to-read"] .scan-dir .qr-img { height: 270pt; max-height: 100%; width: auto; }',
    '  .section[data-section="scan-to-read"] .scan-dir .qr-img { height: 270pt; max-height: 100%; width: auto; }\n'
    '  .section[data-section="scan-to-read"] { padding-top: 16pt; padding-bottom: 12pt; }')

# sanity
leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", h)))
if leftover:
    sys.exit(f"unreplaced placeholders: {leftover}")

p.write_text(h, encoding="utf-8")
print(f"wrote {p} ({len(h)} bytes)")
