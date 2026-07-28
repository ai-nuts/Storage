#!/usr/bin/env python3
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

def drop_section(doc, sec):
    m = re.search(rf'<div\b[^>]*\bdata-section="{re.escape(sec)}"', doc)
    if not m: return doc
    start = doc.rfind("<div", 0, m.end())
    i, depth = start, 0
    while i < len(doc):
        o, c = doc.find("<div", i), doc.find("</div>", i)
        if c == -1: return doc
        if o != -1 and o < c:
            depth += 1; i = o + 4
        else:
            depth -= 1; i = c + len("</div>")
            if depth == 0:
                while i < len(doc) and doc[i] in " \t\r\n": i += 1
                return doc[:start] + doc[i:]
    return doc

# ---- 1. structural block replacements (widgets inline) ----
BLOCKS = []

# Problem
BLOCKS.append((
"""        <p>{{PROBLEM}}</p>""",
"""        <p>Recurrent neural networks (RNNs) reliably fail to learn sequence relationships that carry <strong>long-term memory</strong>. A basic question was left open: is this merely an <em>optimization</em> failure, or a <strong>fundamental limit</strong> of the RNN model class itself?</p>
        <div class="p-callout-bar">The only prior inverse guarantee covered purely <strong>linear</strong> RNNs and linear targets, leaving the nonlinear case wide open.</div>"""))

# Motivation bullets -> bullets + vs
BLOCKS.append((
"""        <ul>
          <li>{{MOTIVATION_1}}</li>
          <li>{{MOTIVATION_2}}</li>
        </ul>""",
"""        <ul>
          <li>Most ML approximation results are <strong>forward</strong> (Jackson-type): they bound achievable error given a regular target.</li>
          <li>The reverse question &mdash; what a target <em>must</em> look like to be efficiently and stably learnable &mdash; exposes architectural limits far more directly.</li>
        </ul>
        <div class="p-vs">
          <div class="side bad"><h4>Forward (Jackson)</h4><p>Assume a regular target &rarr; bound the error.</p></div>
          <div class="sep">vs.</div>
          <div class="side good"><h4>Inverse (Bernstein)</h4><p>Assume efficient approx. &rarr; deduce the target's regularity.</p></div>
        </div>"""))

# Method bullets -> steps + equation
BLOCKS.append((
"""        <ul>
          <li>{{METHOD_1}}</li>
          <li>{{METHOD_2}}</li>
        </ul>""",
"""        <div class="p-steps">
          <div class="step"><strong>Memory function.</strong> Over Heaviside step inputs, measure how strongly the output at time <em>t</em> still depends on the input &mdash; a task-independent, <strong>numerically queryable</strong> notion of memory.</div>
          <div class="step"><strong>Stable approximation.</strong> The worst-case perturbation error under a weight ball of radius &beta; must stay continuous up to some positive &beta;<sub>0</sub> &mdash; exactly what gradient training needs.</div>
          <div class="step"><strong>Stable reparameterization.</strong> Replace the recurrent weight with a map into stable, negative-real-part matrices (exp / softplus) to escape the limit.</div>
        </div>
        <div class="p-eq">
          $\\mathcal{M}(\\mathbf{H})(t) := \\sup_{x\\neq 0}\\frac{1}{\\lVert x\\rVert_\\infty}\\left|\\tfrac{d}{dt}H_t(u_x)\\right|$
          <span class="where">Stable approximation forces $\\lim_{t\\to\\infty} e^{\\beta t}\\,\\mathcal{M}(\\mathbf{H})(t)=0$ &mdash; the memory must decay exponentially.</span>
        </div>"""))

# Key Results table + callout
BLOCKS.append((
"""        <table class="results">
          <tr><th>Method</th><th>Metric</th></tr>
          <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>
          <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>
        </table>
        <div class="callout">{{HEADLINE_DELTA}}</div>""",
"""        <table class="results">
          <tr><th>MNIST &middot; recurrent param.</th><th>Test acc.</th></tr>
          <tr><td class="method">Direct g(M)=M (unstable)</td><td>68.47%</td></tr>
          <tr><td class="method">Exp reparameterization</td><td>70.55%</td></tr>
          <tr><td class="method">Inverse reparameterization</td><td>70.77%</td></tr>
          <tr class="best"><td class="method">Softplus reparameterization</td><td>71.36%</td></tr>
        </table>
        <div class="callout">Main theorem: any target <strong>stably</strong> approximated by nonlinear RNNs must have <strong>exponentially decaying memory</strong>.</div>"""))

# Takeaway
BLOCKS.append((
"""        <p>{{TAKEAWAY}}</p>""",
"""        <p>Plain nonlinear RNNs can only <strong>stably</strong> learn targets whose memory decays exponentially, so their well-known struggle with long-term dependencies is a <strong>fundamental architectural limit</strong>, not just an optimizer artifact.</p>
        <div class="p-callout-primary">But a principled stable reparameterization provably and empirically relaxes the curse of memory &mdash; faster training, higher accuracy.</div>"""))

for old, new in BLOCKS:
    if old not in html:
        sys.exit(f"BLOCK anchor not found:\n{old[:120]}")
    html = html.replace(old, new)

# ---- 2. drop optional dataset-benchmark section + PLAYLIST id ----
html = drop_section(html, "dataset-benchmark")
html = html.replace('"dataset-benchmark", ', '').replace(', "dataset-benchmark"', '')

# ---- 3. simple token fills ----
SUBS = {
    "{{TITLE}}": "Inverse Approximation Theory for Nonlinear Recurrent Neural Networks",
    "{{AUTHORS}}": 'Zhong Li<sup>1</sup>, Shida Wang<sup>2</sup>, Qianxiao Li<sup>2,3</sup>',
    "{{AUTHOR_LEGEND}}": '<sup>1</sup> Microsoft Research Asia &nbsp;&nbsp; <sup>2</sup> National University of Singapore &nbsp;&nbsp; <sup>3</sup> Institute for Functional Intelligent Materials',
    "{{VENUE_NAME}}": "ICLR", "{{VENUE_YEAR}}": "2024",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{LOGO_1}}": "assets/logos/microsoft-research.png",
    "{{LOGO_2}}": "assets/logos/national-university-of-singapore.png",
    "{{LOGO_3}}": "assets/logos/institute-for-functional-intelligent-materials.png",
    "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{CONTACT}}": "", "{{QR_PAPER}}": "", "{{URL_PAPER}}": "",
    # figures
    "{{TEASER_FIGURE}}": "assets/figures/figure1.png",
    "{{TEASER_CAPTION}}": "Fig 1 &middot; Linear functional with <em>exponential</em> memory: a positive stability radius &beta;<sub>0</sub> exists (curves converge before diverging).",
    "{{METHOD_FIGURE}}": "assets/figures/figure3.png",
    "{{METHOD_CAPTION}}": "Fig 3 &middot; Filtering random RNN teachers (m=256) by stable approximability leaves only those with exponentially decaying memory functions (right).",
    "{{SECONDARY_FIGURE}}": "assets/figures/figure2.png",
    "{{SECONDARY_CAPTION}}": "Fig 2 &middot; Nonlinear functional with <em>polynomial</em> memory: intersections shift left as m grows &mdash; no stability radius survives.",
    "{{KEY_RESULT_CONCLUSION}}": "Polynomial-memory targets show no stability radius; filtering teacher models by stability leaves only exponential-memory ones.",
    # headline numbers
    "{{HERO_VAL}}": "71.36%",
    "{{HERO_LABEL}}": "Softplus stable reparam. &middot; MNIST",
    "{{HERO_NOTE}}": "+2.9 pts over the unstable baseline",
    "{{STAT_2_VAL}}": "68.47%", "{{STAT_2_LBL}}": "Direct baseline",
    "{{STAT_3_VAL}}": "~10", "{{STAT_3_LBL}}": "Epochs, exp target",
    "{{STAT_4_VAL}}": "~1000", "{{STAT_4_LBL}}": "Epochs, poly target",
    # commented-out placeholders (kept inert) -> empty
    "{{KEY_EQUATION}}": "", "{{KEY_EQUATION_NOTE}}": "",
    "{{ABLATION_1}}": "", "{{ABLATION_2}}": "", "{{ABLATION_CONCLUSION}}": "",
}
missing = [k for k in SUBS if k not in html]
if missing:
    sys.exit(f"tokens not in template: {missing}")
for k, v in SUBS.items():
    html = html.replace(k, v)

# ---- 4. leftover check ----
leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
