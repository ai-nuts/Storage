#!/usr/bin/env python3
"""Fill poster.html placeholders for CMO-NRT (079). Reads template from disk."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    "{{TITLE}}": "Near-Real-Time Monitoring of the Global Ocean Carbon Sink",
    "{{AUTHORS}}": ("Piyu Ke<sup>1,2,3</sup>, Xiaofan Gui<sup>3</sup>, Wei Cao<sup>3</sup>, "
                    "Dezhi Wang<sup>4</sup>, Ce Hou<sup>5,6</sup>, Lixing Wang<sup>1</sup>, "
                    "Xuanren Song<sup>1</sup>, Yun Li<sup>7</sup>, Biqing Zhu<sup>8</sup>, "
                    "Jiang Bian<sup>3</sup>, Stephen Sitch<sup>2</sup>, Philippe Ciais<sup>9,10</sup>, "
                    "Pierre Friedlingstein<sup>2</sup>, Zhu Liu<sup>1,11</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> Tsinghua University &nbsp; <sup>2</sup> University of Exeter &nbsp; "
                          "<sup>3</sup> Microsoft Research &nbsp; <sup>4</sup> Lanzhou University &nbsp; "
                          "<sup>5</sup> HKUST &nbsp; <sup>6</sup> Peking University &nbsp; "
                          "<sup>7</sup> KU Leuven &nbsp; <sup>8</sup> IIASA &nbsp; "
                          "<sup>9</sup> LSCE &nbsp; <sup>10</sup> The Cyprus Institute &nbsp; "
                          "<sup>11</sup> The University of Hong Kong"),
    "{{VENUE_NAME}}": "ICLR",
    "{{VENUE_YEAR}}": "2024",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "Email: zhuliu@tsinghua.edu.cn",
    "{{LOGO_1}}": "assets/logos/tsinghua-university.png",
    "{{LOGO_2}}": "assets/logos/university-of-exeter.jpg",
    "{{LOGO_3}}": "assets/logos/microsoft-research.png",
    "{{LOGO_4}}": "assets/logos/peking-university.png",
    "{{LOGO_5}}": "assets/logos/ku-leuven.png",
    "{{LOGO_6}}": "assets/logos/the-university-of-hong-kong.png",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",
    "{{URL_PROJECT}}": "carbonsink.microsoft.com",

    # Problem
    "{{PROBLEM}}": ("Official estimates of the global ocean carbon sink from the annual "
                    "<strong>Global Carbon Budget</strong> lag actual conditions by roughly "
                    "<span class=\"num\">one year</span>, so recent shifts in ocean CO&#8322; uptake "
                    "cannot be monitored in time."),

    # Motivation
    "{{MOTIVATION_1}}": ("The Paris-Agreement <strong>global stocktake</strong> and intensifying "
                         "mitigation demand ocean carbon-sink data at far lower latency than a one-year delay."),
    "{{MOTIVATION_2}}": ("Existing fCO&#8322; and air&#8211;sea flux databases (GOBMs, data products) are "
                         "spatially detailed but <strong>always historical</strong> &mdash; no timely, near-present view."),

    # Method
    "{{METHOD_1}}": ("A <strong>CNN&#8202;+&#8202;linear</strong> model learns the non-linear map from observed "
                     "predictors &#8212; year, month, lat, lon and <span class=\"num\">9</span> environmental factors "
                     "(SST, ICE, CHL, MLD, CO&#8322;, SSS, SSH, SLP, wind) &#8212; to each GOBM / data-product estimate."),
    "{{METHOD_2}}": ("Global <span class=\"num\">180&#215;360</span> grids are cut into 18&#215;18 patches; "
                     "<strong>semi-supervised</strong> training pairs a supervised RMSE loss with an unsupervised "
                     "consistency loss between weakly (10% masked) and strongly (30% masked) views, then K-fold ensembling."),
    "{{METHOD_FIGURE}}": "assets/figures/page3_figure1.png",
    "{{METHOD_CAPTION}}": ("Schematic overview of the CMO-NRT methodology and data sources: clean &amp; align data, "
                           "crop to 18&#215;18 patches, CNN + semi-supervised model, K-fold ensemble &#8594; prediction."),

    # Motivation teaser figure (Fig 3)
    "{{TEASER_FIGURE}}": "assets/figures/page8_figure3.png",
    "{{TEASER_CAPTION}}": ("Monthly fCO&#8322; (A) and air&#8211;sea CO&#8322; flux (B): GCB&nbsp;2022 history (black) "
                           "extended to Jul&nbsp;2023 by CMO-NRT near-real-time predictions (red); global maps (C, D)."),

    # Key Results table (replaced by richer table via Edit; fallback values here)
    "{{BASELINE}}": "Data products (8)",
    "{{BASELINE_NUM}}": "R&#178; &gt; 0.85",
    "{{OURS}}": "GOBMs (10)",
    "{{OURS_NUM}}": "R&#178; &gt; 0.9",
    "{{HEADLINE_DELTA}}": "~1-year reporting lag &#8594; near-real-time monthly maps (Jan 2022 &#8211; Jul 2023)",
    "{{KEY_RESULT_CONCLUSION}}": ("CMO-NRT reproduces the trusted model and data-product outputs closely, so it can "
                                  "extend the ocean carbon sink to the present month."),
    "{{SECONDARY_FIGURE}}": "assets/figures/page9_figure5.png",
    "{{SECONDARY_CAPTION}}": ("Prediction-vs-original correlation for each of the 10 GOBMs (held-out 2020&#8211;2021); "
                              "most R&#178; &gt; 0.9 (MRI-ESM2-1 R&#178;=0.97, CESM2 R&#178;=0.96)."),

    # Headline Numbers
    "{{HERO_VAL}}": "18",
    "{{HERO_LABEL}}": "source estimates updated to near-real-time",
    "{{HERO_NOTE}}": "10 GOBMs + 8 data products",
    "{{STAT_2_VAL}}": "R&#178;&gt;0.9",
    "{{STAT_2_LBL}}": "pred vs original",
    "{{STAT_3_VAL}}": "&lt;3 &#181;atm",
    "{{STAT_3_LBL}}": "global fCO&#8322; diff",
    "{{STAT_4_VAL}}": "1.74",
    "{{STAT_4_LBL}}": "xCO&#8322; RMSE (~0.5%)",

    # Dataset / Benchmark
    "{{DATASET_1}}": ("<strong>CMO-NRT</strong>: monthly gridded global surface-ocean fCO&#8322; and air&#8211;sea "
                      "CO&#8322; flux, <span class=\"num\">Jan 2022 &#8211; Jul 2023</span>, derived from the 10 GOBMs "
                      "+ 8 data products of GCB&nbsp;2022."),
    "{{DATASET_2}}": ("Released openly on Figshare (doi:10.6084/m9.figshare.24658494) and refreshed at "
                      "carbonsink.microsoft.com."),

    # Takeaway
    "{{TAKEAWAY}}": ("By pairing CNNs with semi-supervised learning to update trusted models and data products, "
                     "<strong>CMO-NRT</strong> turns the once year-delayed global ocean carbon sink into a "
                     "<strong>near-real-time, monthly, gridded</strong> monitor."),
}

missing = [k for k in SUBS if k not in html]
if missing:
    print(f"WARN placeholders not in template: {missing}", file=sys.stderr)
for token, value in SUBS.items():
    html = html.replace(token, value)

# Empty any leftover {{...}} (commented ablation/key-equation stubs, hidden scan slots)
html = re.sub(r"\{\{[A-Z0-9_]+\}\}", "", html)

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
