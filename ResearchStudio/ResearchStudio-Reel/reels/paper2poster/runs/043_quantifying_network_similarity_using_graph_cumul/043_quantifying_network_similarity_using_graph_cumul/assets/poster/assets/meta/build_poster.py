#!/usr/bin/env python3
"""Fill the composed 3col poster.html for the Graph Cumulants paper."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# --- remove the commented-out Ablation Study block so its {{...}} tokens don't linger ---
html = re.sub(r"<!--[\s═]*ABLATION STUDY.*?-->", "", html, flags=re.S)
# --- remove the commented-out KEY EQUATION example (we inject an active .p-eq widget instead) ---
html = re.sub(r"<!-- ★ KEY EQUATION.*?-->", "", html, flags=re.S)

# --- inject an ACTIVE key-equation widget into the Method section (before its figure) ---
EQN = (
    '<div class="p-eq">$$\\hat{d}^2_\\kappa=(\\hat{\\kappa}_A-\\hat{\\kappa}_B)^{\\!\\top}'
    '\\big(\\hat{\\Sigma}^{(\\kappa)}_A+\\hat{\\Sigma}^{(\\kappa)}_B\\big)^{-1}'
    '(\\hat{\\kappa}_A-\\hat{\\kappa}_B)$$'
    '<span class="where">squared Mahalanobis distance between the two samples’ '
    'cumulant vectors κ, weighted by analytic covariances Σ</span></div>\n        '
    '<figure><img src="{{METHOD_FIGURE}}"'
)
html = html.replace('<figure><img src="{{METHOD_FIGURE}}"', EQN, 1)

# --- inject figure4 (real-data ROC sweep) into the Dataset / Benchmark section ---
DATA_FIG = (
    '</ul>\n        <figure><img src="assets/figures/figure4.png" alt="">'
    '<figcaption>Arabidopsis vs. Mouse (density-matched): at r=1 neither test separates them; '
    'adding r=2,3 subgraphs sharpens cumulants but makes moments overfit.</figcaption></figure>'
)
html = html.replace(
    '<li>{{DATASET_2}}</li>\n        </ul>', '<li>{{DATASET_2}}</li>' + DATA_FIG, 1)


SUBS = {
    # titlebar / metadata
    "{{TITLE}}": "Quantifying Network Similarity using Graph Cumulants",
    "{{AUTHORS}}": ("Gecia Bravo-Hermsdorff<sup>1</sup>, "
                    "Lee M. Gunderson<sup>1</sup>, "
                    "Pierre-Andr&eacute; Maugis<sup>2</sup>, "
                    "Carey E. Priebe<sup>3</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> University College London &nbsp;&nbsp; "
                          "<sup>2</sup> Google Research &nbsp;&nbsp; "
                          "<sup>3</sup> Johns Hopkins University"),
    "{{VENUE_NAME}}": "JMLR",
    "{{VENUE_YEAR}}": "2023",
    "{{VENUE_LOGO}}": "",
    "{{CONTACT}}": "Email: gecia.bravo@gmail.com",
    "{{LOGO_1}}": "assets/logos/university-college-london.png",
    "{{LOGO_2}}": "assets/logos/google.png",
    "{{LOGO_3}}": "assets/logos/johns-hopkins-university.jpg",
    "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{URL_PAPER}}": "arxiv.org/abs/2107.11403",

    # ---- Problem ----
    "{{PROBLEM}}": ("Given two samples of graphs drawn i.i.d. from <strong>unknown "
                    "distributions</strong>, decide whether those distributions "
                    "<strong>differ</strong> — using only statistics of their "
                    "exchangeable, <em>unlabeled</em> edges."),

    # ---- Motivation ----
    "{{MOTIVATION_1}}": ("Networks are routinely summarized by <strong>subgraph / motif "
                         "densities</strong>, but these raw densities are strongly "
                         "<strong>correlated across orders</strong>, yielding statistically "
                         "weak comparisons — especially with few observed graphs."),
    "{{MOTIVATION_2}}": ("Prior tests often need <strong>expensive resampling</strong> from "
                         "fitted models to judge significance; a better coordinate system "
                         "that removes lower-order redundancy could make tests both "
                         "<strong>stronger and cheaper</strong>."),
    "{{TEASER_FIGURE}}": "assets/figures/figure2.png",
    "{{TEASER_CAPTION}}": ("ROC for a density-matched heterogeneous vs. assortative SBM: the "
                           "cumulant test dominates the moment test at every false-positive "
                           "rate α."),

    # ---- Method ----
    "{{METHOD_1}}": ("Both tests turn subgraph counts into a coordinate vector — "
                     "<strong>graph moments</strong> (injective-homomorphism densities) vs. "
                     "<strong>graph cumulants</strong> — and compare two samples with the "
                     "<strong>squared Mahalanobis distance</strong> using analytic covariances."),
    "{{METHOD_2}}": ("Cumulants come from moments via a connectivity-respecting "
                     "<strong>Möbius transform</strong> over edge partitions, capturing a "
                     "subgraph's <em>excess propensity</em> beyond what its smaller pieces "
                     "predict. Using subgraphs up to <span class=\"num\">r=3</span> edges, both "
                     "tests share the same <span class=\"num\">O(n<sup>ω</sup>)</span> cost."),
    "{{METHOD_FIGURE}}": "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": ("Graph cumulants κ expand graph moments μ over "
                           "connectivity-respecting partitions of a subgraph's edges "
                           "(analogous to classical moments ↔ cumulants)."),

    # ---- Dataset / Benchmark ----
    "{{DATASET_1}}": ("<strong>Synthetic:</strong> density-matched pairs of two-community "
                      "SBMs — one heterogeneous (ε<sub>h</sub>), one assortative "
                      "(ε<sub>a</sub>) — with <span class=\"num\">n=128</span> and "
                      "<span class=\"num\">256</span> nodes."),
    "{{DATASET_2}}": ("<strong>Real:</strong> genetic-interaction networks from FunCoup "
                      "(Persson et&nbsp;al., 2021) — Arabidopsis, Mouse, Human, Rat "
                      "(≈10<sup>4</sup> nodes, ≈10<sup>6</sup> edges), all adjusted "
                      "to equal edge density."),

    # ---- Key Results ----
    "{{BASELINE}}": "Graph moments",
    "{{BASELINE_NUM}}": "undefined for s&lt;4",
    "{{OURS}}": "Graph cumulants",
    "{{OURS_NUM}}": "works down to s=1",
    "{{HEADLINE_DELTA}}": ("Cumulants achieve consistently higher AUC — largest gains when "
                           "graphs-per-sample s is small"),
    "{{SECONDARY_FIGURE}}": "assets/figures/figure3.png",
    "{{SECONDARY_CAPTION}}": ("AUC vs. graphs-per-sample s (n=128 and n=256): cumulants (solid) "
                              "beat moments (dashed); moments fail for s&lt;4, cumulants work at s=1."),
    "{{KEY_RESULT_CONCLUSION}}": ("Swapping moments for cumulants raises statistical power at "
                                  "identical cost, and works even with a single observed graph."),

    # ---- Headline Numbers ----
    "{{HERO_VAL}}": "s = 1",
    "{{HERO_LABEL}}": "Cumulant test works with a single observed graph",
    "{{HERO_NOTE}}": "moment test undefined for s &lt; 4",
    "{{STAT_2_VAL}}": "r = 3",
    "{{STAT_2_LBL}}": "subgraph edges used",
    "{{STAT_3_VAL}}": "O(n<sup>ω</sup>)",
    "{{STAT_3_LBL}}": "same cost as moments",
    "{{STAT_4_VAL}}": "χ²₅",
    "{{STAT_4_LBL}}": "accurate analytic null",

    # ---- Takeaway ----
    "{{TAKEAWAY}}": ("When comparing networks with subgraph or motif densities, convert them to "
                     "<strong>graph cumulants</strong>: more statistical power, an accurate "
                     "analytic χ² null, and testing even a <strong>single graph</strong> "
                     "— all at <strong>no extra computational cost</strong>."),
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
