#!/usr/bin/env python3
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    "{{TITLE}}": "Unveiling Privacy, Memorization, and Input Curvature Links",
    "{{AUTHORS}}": ("Deepak Ravikumar<sup>1</sup>, Efstathia Soufleri<sup>1</sup>, "
                    "Abolfazl Hashemi<sup>1</sup>, Kaushik Roy<sup>1</sup>"),
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> Purdue University",
    "{{VENUE_NAME}}": "ICML",
    "{{VENUE_YEAR}}": "2024",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "Email: dravikum@purdue.edu",
    "{{LOGO_1}}": "assets/logos/purdue-university.png",
    "{{LOGO_2}}": "", "{{LOGO_3}}": "", "{{LOGO_4}}": "",
    "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "", "{{URL_PAPER}}": "",

    # ---- Problem (col 1) ----
    "{{PROBLEM}}": (
        "Input loss curvature &mdash; the trace of the loss Hessian w.r.t. the input &mdash; "
        "is a widely-used <strong>cheap proxy</strong> for memorization in deep nets. Yet "
        "<em>why</em> curvature and memorization track together, and how either links to "
        "differential privacy, had no theory."
        "</p><div class=\"p-callout-bar\">Feldman&rsquo;s memorization score is principled but "
        "compute-prohibitive; the curvature proxy was purely empirical &mdash; until now.</div>"
    ),

    # ---- Motivation (col 1, grow) ----
    "{{MOTIVATION_1}}": (
        "A rigorous curvature&ndash;memorization&ndash;privacy link would give a "
        "<strong>theoretical license</strong> to use cheap curvature as a memorization proxy, "
        "and explain how privacy mechanisms suppress leakage."
    ),
    "{{MOTIVATION_2}}": (
        "Influence functions assume Hessian convexity &amp; positive-definiteness &mdash; "
        "conditions that fail for deep nets; input curvature needs no such assumptions."
        "</li></ul><div class=\"p-callout-soft\">Low-curvature samples are prototypical of their "
        "class; high-curvature ones are rare, hard, and more likely memorized.</div>"
    ),
    "{{TEASER_FIGURE}}": "assets/figures/figure2.png",
    "{{TEASER_CAPTION}}": (
        "ImageNet samples ranked by input curvature: lowest (left) are prototypical, "
        "highest (right) are rare, hard, and more likely memorized."
    ),

    # ---- Method (col 2, grow) ----
    "{{METHOD_1}}": (
        "A second-order <strong>Nesterov&ndash;Polyak</strong> expansion of the loss with a "
        "zero-mean perturbation cancels first-order terms, leaving input curvature as the "
        "leading term."
    ),
    "{{METHOD_2}}": (
        "Under error-stability, generalization, uniform-model-bias &amp; dataset-adjacency "
        "assumptions (bounded loss), taking expectations yields the three bounds. Curvature is "
        "estimated with <strong>Hutchinson&rsquo;s trace estimator</strong> "
        "(<span class=\"num\">h=10<sup>&minus;3</sup></span>, <span class=\"num\">n=10</span> "
        "Rademacher vectors)."
    ),
    "{{KEY_EQUATION}}": (
        r"\begin{aligned}"
        r"|\mathrm{mem}(A,S,i)| &\le \tfrac{1}{L}\,\mathbb{E}_\phi\!\left[\mathrm{Curv}_\phi(z_i,S^{\setminus i})\right] + c_1 \\[3pt]"
        r"\mathbb{E}_{z,\phi}\!\left[\mathrm{Curv}_\phi(z,S)\right] &\le L(m{+}1)\!\left(1-e^{-\epsilon}\right) + c_2"
        r"\end{aligned}"
    ),
    "{{KEY_EQUATION_NOTE}}": (
        "Thm 5.1: curvature upper-bounds memorization. Thm 5.3: the DP budget ε upper-bounds average curvature."
    ),
    "{{METHOD_FIGURE}}": "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": (
        "Theoretical framework: three upper bounds (Thms 5.1, 5.3, 5.4) link Differential "
        "Privacy, Memorization, and Input Loss Curvature."
    ),

    # ---- Dataset / Benchmark (col 2) ----
    "{{DATASET_1}}": (
        "Feldman &amp; Zhang (2020) precomputed memorization scores + released ensembles: "
        "<strong>1000</strong> Small Inception (CIFAR100), <strong>100</strong> ResNet50 (ImageNet)."
    ),
    "{{DATASET_2}}": (
        "Privacy models: ResNet18 trained with DP-SGD across ε budgets at δ=10<sup>&minus;5</sup>."
        "</li></ul><div class=\"p-chips\">"
        "<span>CIFAR-10</span><span>CIFAR-100</span><span>ImageNet</span>"
        "<span class=\"alt\">Small Inception</span><span class=\"alt\">ResNet50</span>"
        "<span class=\"alt\">ResNet18</span></div>"
    ),

    # ---- Key Results (col 3, grow) ----
    "{{BASELINE}}": "Memorization score (Feldman)",
    "{{BASELINE_NUM}}": "1&times; (reference)",
    "{{OURS}}": "Input loss curvature",
    "{{OURS_NUM}}": "~10<sup>3</sup>&times; faster",
    "{{HEADLINE_DELTA}}": "Curvature is ~3 orders of magnitude cheaper to compute than the memorization score.",
    "{{SECONDARY_FIGURE}}": "assets/figures/figure4.png",
    "{{SECONDARY_CAPTION}}": (
        "Memorization score vs. input loss curvature at end of training &mdash; strong linear "
        "trend (CIFAR100: 1000 Small Inception; ImageNet: 100 ResNet50)."
    ),
    "{{KEY_RESULT_CONCLUSION}}": (
        "Every theoretical prediction holds empirically: curvature tracks memorization linearly, "
        "and stronger privacy drives both down along the predicted best-fit curves."
    ),

    # ---- Headline Numbers (col 3) ----
    "{{HERO_VAL}}": "~10³×",
    "{{HERO_LABEL}}": "cheaper than the memorization score",
    "{{HERO_NOTE}}": "same signal, a fraction of the compute",
    "{{STAT_2_VAL}}": "3", "{{STAT_2_LBL}}": "theorems proved",
    "{{STAT_3_VAL}}": "1000", "{{STAT_3_LBL}}": "CIFAR100 models",
    "{{STAT_4_VAL}}": "ε=1–50", "{{STAT_4_LBL}}": "DP budgets swept",

    # ---- Ablation placeholders live inside a commented-out block; blank them ----
    "{{ABLATION_1}}": "", "{{ABLATION_2}}": "", "{{ABLATION_CONCLUSION}}": "",

    # ---- Takeaway (col 3) ----
    "{{TAKEAWAY}}": (
        "Input loss curvature <strong>provably upper-bounds memorization</strong> and is itself "
        "bounded by the differential-privacy parameter &mdash; a rigorous, assumption-light "
        "theory that justifies cheap curvature as a memorization proxy and links both to privacy."
    ),
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
