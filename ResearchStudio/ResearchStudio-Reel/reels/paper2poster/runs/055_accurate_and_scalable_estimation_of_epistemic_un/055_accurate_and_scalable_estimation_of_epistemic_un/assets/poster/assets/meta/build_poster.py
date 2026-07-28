#!/usr/bin/env python3
"""Paper-specific poster build: fill composed 3col poster.html (disk-to-disk)."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# ---- 1. structural BLOCK replacements (add content-pattern widgets) ----
BLOCKS = []

# Problem: prose + callout-bar (P3)
BLOCKS.append((
    "        <p>{{PROBLEM}}</p>",
    "        <p>Under distribution shift, graph neural networks emit <strong>unreliable confidence indicators</strong> — miscalibrated softmax / entropy scores — yet how and why GNN confidence degrades is far less studied than in vision.</p>\n"
    "        <div class=\"p-callout-bar\">Safety-critical GNNs lean on these scores for calibration, OOD rejection, and generalization-gap estimates — so their degradation directly undermines safe deployment.</div>",
))

# Motivation: lead + vs (P7)
BLOCKS.append((
    "        <ul>\n          <li>{{MOTIVATION_1}}</li>\n          <li>{{MOTIVATION_2}}</li>\n        </ul>",
    "        <p>Does a more <em>expressive</em> architecture fix calibration? A controlled structural-distortion study says <strong>no</strong>.</p>\n"
    "        <div class=\"p-vs\">\n"
    "          <div class=\"side bad\"><h4>Scale expressivity</h4><p>Graph transformers, positional encodings, deeper / wider nets — calibration stays poor, sometimes worse.</p></div>\n"
    "          <div class=\"sep\">vs.</div>\n"
    "          <div class=\"side good\"><h4>Model uncertainty</h4><p>Directly quantify epistemic uncertainty to modulate the confidence indicators — the path we take.</p></div>\n"
    "        </div>",
))

# Method bullets: 3 items
BLOCKS.append((
    "        <ul>\n          <li>{{METHOD_1}}</li>\n          <li>{{METHOD_2}}</li>\n        </ul>",
    "        <ul>\n"
    "          <li><strong>Stochastic anchoring for graphs.</strong> Recast each input as a relative representation against a random training anchor <span class=\"num\">[X − c ‖ c]</span>; varying <span class=\"num\">c</span> emulates sampling a distribution of hypotheses.</li>\n"
    "          <li><strong>Three anchoring sites.</strong> Node features, an intermediate MPNN layer, or after READOUT — trading how much of the network is made stochastic. Anchoring stays in node/hidden space (a graph anchor would add spurious edges).</li>\n"
    "          <li><strong>Pretrained variant.</strong> Freeze the backbone, train only an anchored classifier head — cheap <em>partial</em> stochasticity that reuses existing models.</li>\n"
    "        </ul>",
))

# Method equation (P15 p-eq) + Method figure (figure3)
BLOCKS.append((
    "        <!-- ★ KEY EQUATION (strongly preferred — most papers have one). Render the paper's core\n"
    "             formula with the `equation` widget from references/content_patterns.md, e.g.\n"
    "               <div class=\"eqn\">$$ {{KEY_EQUATION}} $$<span class=\"eqn-note\">{{KEY_EQUATION_NOTE}}</span></div>\n"
    "             Integrate it HERE in Method, OR split it into its own \"Formulation\" .section if the\n"
    "             math is central. A rendered section must never be contentless. Remove ONLY if the paper\n"
    "             genuinely has no formula (pure systems / empirical). -->\n"
    "        <figure><img src=\"{{METHOD_FIGURE}}\" alt=\"half\"><figcaption>{{METHOD_CAPTION}}</figcaption></figure>",
    "        <div class=\"p-eq\">\n"
    "          $$\\mu(y\\mid\\mathcal{G}_i)=\\tfrac{1}{K}\\sum_{k=1}^{K} f_\\theta([\\mathcal{G}_i, c_k]),\\qquad \\sigma(y\\mid\\mathcal{G}_i)=\\sqrt{\\tfrac{1}{K-1}\\sum_{k=1}^{K}\\big(f_\\theta([\\mathcal{G}_i, c_k])-\\mu\\big)^2}$$\n"
    "          <span class=\"where\">Average over K anchors gives the prediction and its epistemic uncertainty; calibrated score μ<sub>calib</sub>&nbsp;=&nbsp;μ(1−σ), node anchor c<sub>n</sub>&nbsp;∼&nbsp;𝒩(μ,σ).</span>\n"
    "        </div>\n"
    "        <figure><img src=\"assets/figures/figure3.png\" alt=\"half\"><figcaption>Fig 2 — G-∆UQ: three stochastic-centering variants (node-feature, intermediate-MPNN, READOUT) plus anchored inference over K anchors.</figcaption></figure>",
))

# Dataset / Benchmark: lead + chips (P10)
BLOCKS.append((
    "        <ul>\n          <li>{{DATASET_1}}</li>\n          <li>{{DATASET_2}}</li>\n        </ul>",
    "        <p>Evaluated across <strong>three shift regimes</strong> (structural, size, concept/covariate) with GCN&nbsp;·&nbsp;GIN&nbsp;·&nbsp;PNA backbones, against strong single-model UQ baselines:</p>\n"
    "        <div class=\"p-chips\">\n"
    "          <span>Rotated Superpixel-MNIST</span><span>D&amp;D</span><span>NCI1</span><span>NCI109</span><span>PROTEINS</span>\n"
    "          <span class=\"alt\">GOODCMNIST-color</span><span class=\"alt\">GOODMotif-basis</span><span class=\"alt\">GOODMotif-size</span><span class=\"alt\">GOODSST2-length</span>\n"
    "          <span class=\"muted\">Vanilla</span><span class=\"muted\">Deep Ens</span><span class=\"muted\">Temp</span><span class=\"muted\">MC-Dropout</span>\n"
    "        </div>",
))

# Key Results: bullets + callout-primary (P1) + secondary figure (figure7) + conclusion
BLOCKS.append((
    "        <table class=\"results\">\n"
    "          <tr><th>Method</th><th>Metric</th></tr>\n"
    "          <tr><td class=\"method\">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>\n"
    "          <tr class=\"best\"><td class=\"method\">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>\n"
    "        </table>\n"
    "        <div class=\"callout\">{{HEADLINE_DELTA}}</div>\n"
    "        <!-- ★ SECONDARY figure slot (figure-rich): a Key Result plot / qualitative samples / ablation\n"
    "             chart — the second of ≥3 figure slots in this layout. REMOVE the <figure> if no secondary\n"
    "             figure carries real signal. -->\n"
    "        <figure><img src=\"{{SECONDARY_FIGURE}}\" alt=\"\"><figcaption>{{SECONDARY_CAPTION}}</figcaption></figure>\n"
    "        <p class=\"conclusion\">{{KEY_RESULT_CONCLUSION}}</p>",
    "        <ul>\n"
    "          <li><strong>Better-calibrated CIs</strong> than popular single-model UQ methods across size, concept, and covariate shifts — with accuracy maintained or improved.</li>\n"
    "          <li><strong>Downstream wins.</strong> Among the lowest-MAE single-model estimators for generalization-gap prediction, and highly competitive for OOD detection.</li>\n"
    "        </ul>\n"
    "        <div class=\"p-callout-primary\">The pretrained variant is frequently the strongest — notably under covariate shift, where it significantly outperforms all baselines.</div>\n"
    "        <figure><img src=\"assets/figures/figure7.png\" alt=\"\"><figcaption>Fig 7 — OOD-detection AUROC across concept &amp; covariate shifts; pretrained G-∆UQ (light blue) leads under covariate shift.</figcaption></figure>\n"
    "        <p class=\"conclusion\">Reliable confidence estimates translate into concrete gains on the safety tasks that consume them.</p>",
))

# Takeaway: callout-primary (P1)
BLOCKS.append((
    "        <p>{{TAKEAWAY}}</p>",
    "        <div class=\"p-callout-primary\">Bigger or more expressive GNNs don't fix calibration under shift. Extending stochastic centering to graphs with partial stochasticity (G-∆UQ) gives a scalable, single-model route to reliable, well-calibrated uncertainty — and a pretrained variant makes it cheap to add to models you already have.</div>",
))

for old, new in BLOCKS:
    if old not in html:
        sys.exit("BLOCK old-string not found:\n" + old[:200])
    if html.count(old) != 1:
        sys.exit("BLOCK old-string not unique (%d): %s" % (html.count(old), old[:120]))
    html = html.replace(old, new)

# ---- 2. simple 1:1 token replacements ----
TOK = {
    "{{TITLE}}": "Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural Networks",
    "{{AUTHORS}}": "Puja Trivedi<sup>1</sup>, Mark Heimann<sup>2</sup>, Rushil Anirudh<sup>2</sup>, Danai Koutra<sup>1</sup>, Jayaraman J. Thiagarajan<sup>2</sup>",
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> University of Michigan &nbsp;&nbsp; <sup>2</sup> Lawrence Livermore National Laboratory",
    "{{VENUE_NAME}}": "ICLR",
    "{{VENUE_YEAR}}": "2024",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "Email: pujat@umich.edu",
    "{{LOGO_1}}": "assets/logos/university-of-michigan.png",
    "{{LOGO_2}}": "assets/logos/lawrence-livermore-national-laboratory.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "", "{{QR_CODE}}": "",
    "{{TEASER_FIGURE}}": "assets/figures/figure1.png",
    "{{TEASER_CAPTION}}": "Fig 1 — Under structural distortion, ECE grows sharply for every architecture; G-∆UQ (blue) cuts ECE with minimal accuracy loss.",
    "{{HERO_VAL}}": "3×3",
    "{{HERO_LABEL}}": "shift regimes × safety tasks",
    "{{HERO_NOTE}}": "covered by one single-model method",
    "{{STAT_2_VAL}}": "4", "{{STAT_2_LBL}}": "UQ baselines",
    "{{STAT_3_VAL}}": "4", "{{STAT_3_LBL}}": "anchoring variants",
    "{{STAT_4_VAL}}": "0", "{{STAT_4_LBL}}": "extra models",
    # commented-out ablation tokens -> blank (section stays inside its comment)
    "{{ABLATION_1}}": "", "{{ABLATION_2}}": "", "{{ABLATION_CONCLUSION}}": "",
}
for t, v in TOK.items():
    html = html.replace(t, v)

# ---- 3. leftover check ----
leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit("unreplaced placeholders remain: %s" % leftover)

target.write_text(html, encoding="utf-8")
print("wrote %s (%d bytes)" % (target, len(html)))
