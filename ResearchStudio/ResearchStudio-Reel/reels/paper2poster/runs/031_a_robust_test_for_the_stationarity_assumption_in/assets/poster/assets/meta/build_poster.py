#!/usr/bin/env python3
"""Fill poster.html placeholders for the Double-CUSUM stationarity-test paper."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    # titlebar / metadata
    "{{TITLE}}": "A Robust Test for the Stationarity Assumption in Sequential Decision Making",
    "{{AUTHORS}}": "Jitao Wang<sup>1</sup>, Chengchun Shi<sup>2</sup>, Zhenke Wu<sup>1</sup>",
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> Department of Biostatistics, University of Michigan, Ann Arbor &nbsp;&nbsp; <sup>2</sup> Department of Statistics, London School of Economics and Political Science",
    "{{VENUE_NAME}}": "ICML",
    "{{VENUE_YEAR}}": "2023",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "Email: c.shi7@lse.ac.uk",
    "{{LOGO_1}}": "assets/logos/university-of-michigan.png",
    "{{LOGO_2}}": "assets/logos/london-school-of-economics-and-political-science.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",

    # Problem
    "{{PROBLEM}}": "Most RL algorithms assume a <strong>stationary MDP</strong> with time-invariant transition and reward functions. Real offline systems <strong>drift over time</strong>, so a policy learned as if the world were frozen becomes suboptimal, sometimes harmful.",

    # Motivation
    "{{MOTIVATION_1}}": "Non-stationarity is pervasive in <strong>mobile health, traffic control, and robotics</strong> &mdash; e.g. waning push-notification effects in the Intern Health Study erode long-term reward.",
    "{{MOTIVATION_2}}": "Prior tests need a <strong>known MDP model</strong>, rely on <strong>linear approximation</strong> that fails in high dimensions, or waste samples learning a policy per time step.",

    # Method
    "{{METHOD_1}}": "At each candidate change point <span class=\"num\">t</span>, compare pooled transition dynamics before vs. after via a <strong>CUSUM-type statistic</strong>.",
    "{{METHOD_2}}": "Add a <strong>mean-zero augmentation</strong> to get a <strong>doubly robust</strong> estimating function &psi;, so neural nets / random forests / lasso can estimate the nuisances without spoiling inference; a <strong>Gaussian multiplier bootstrap</strong> gives the p-value.",
    "{{METHOD_FIGURE}}": "assets/figures/page7_figure1.png",
    "{{METHOD_CAPTION}}": "Double robustness in action: empirical size (left) stays at the nominal 0.05 whenever at least one nuisance model M<sub>1</sub> or M<sub>2</sub> is correct; power (right) stays high.",

    # Dataset / Benchmark
    "{{DATASET_1}}": "Four numerical studies &mdash; a discrete toy example, high-dim synthetic data (state dim d<sub>S</sub> &isin; {1,10,20,30}), a 4&times;4 grid world, and a batch-online semi-synthetic study.",
    "{{DATASET_2}}": "Real-world <strong>Intern Health Study</strong> (IHS): a 21-week mobile-health micro-randomized trial of U.S. medical interns; baselines are ODCP and CUSUM-RL.",

    # Key Results
    "{{BASELINE}}": "CUSUM-RL", "{{BASELINE_NUM}}": "d<sub>S</sub>=1",
    "{{OURS}}": "Proposed test", "{{OURS_NUM}}": "d<sub>S</sub> &le; 30",
    "{{HEADLINE_DELTA}}": "Correct change-point detection sustained up to state dim d<sub>S</sub>=30 &mdash; vs d<sub>S</sub>=1 for CUSUM-RL.",
    "{{SECONDARY_FIGURE}}": "assets/figures/page8_figure2.png",
    "{{SECONDARY_CAPTION}}": "Rejection probability vs &kappa; across state dimensions d<sub>S</sub>=1,10,20,30: the proposed test (orange) locks onto the true change point at every dimension; baselines collapse as d<sub>S</sub> grows.",
    "{{KEY_RESULT_CONCLUSION}}": "The test controls type-I error everywhere and pinpoints the change point even at d<sub>S</sub>&ge;10, where CUSUM-RL and ODCP fail.",

    # Headline Numbers
    "{{HERO_VAL}}": "30",
    "{{HERO_LABEL}}": "Max state dim &middot; correct detection",
    "{{HERO_NOTE}}": "30&times; the CUSUM-RL limit (d<sub>S</sub>=1)",
    "{{STAT_2_VAL}}": "0.05", "{{STAT_2_LBL}}": "type-I level held",
    "{{STAT_3_VAL}}": "wk 16", "{{STAT_3_LBL}}": "IHS change point",
    "{{STAT_4_VAL}}": "5000", "{{STAT_4_LBL}}": "bootstrap samples",

    # Takeaway
    "{{TAKEAWAY}}": "A doubly robust CUSUM test unites <strong>ML flexibility</strong> with <strong>valid inference</strong> to reliably flag when an offline RL environment stops being stationary &mdash; even in high dimensions &mdash; so policies can be relearned on the right data segment.",

    # teaser figure (Motivation)
    "{{TEASER_FIGURE}}": "assets/figures/page9_figure4.png",
    "{{TEASER_CAPTION}}": "Real IHS data: p-values across &kappa; flag a change point for Internal Medicine interns (around week 16); none for Family Practice.",

    # comment-only placeholders (ablation block is commented out; equation guidance comment)
    "{{ABLATION_1}}": "", "{{ABLATION_2}}": "", "{{ABLATION_CONCLUSION}}": "",
    "{{KEY_EQUATION}}": "", "{{KEY_EQUATION_NOTE}}": "",
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
