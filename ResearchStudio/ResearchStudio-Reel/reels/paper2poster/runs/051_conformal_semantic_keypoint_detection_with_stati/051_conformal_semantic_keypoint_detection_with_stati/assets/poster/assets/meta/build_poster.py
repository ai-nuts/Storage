#!/usr/bin/env python3
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# ---- structural (anchor) replacements: restructure section bodies with widgets ----
REPL = []

# remove empty venue logo img (no _venue.png on disk)
REPL.append((
    '      <img src="{{VENUE_LOGO}}" alt="" onerror="this.remove()">\n',
    ''
))

# Problem body -> paragraph + soft callout
REPL.append((
    '        <p>{{PROBLEM}}</p>\n',
    '        <p>Two-stage object pose estimators (detect semantic keypoints, then solve PnP) score well on '
    'benchmarks but return a single 6D pose with <strong>no provable guarantee</strong> on its quality or uncertainty.</p>\n'
    '        <div class="p-callout-soft">Safety-critical uses &mdash; autonomous driving, robotic manipulation, '
    'space robotics &mdash; need formal worst-case error bounds that prior pipelines never provide.</div>\n'
))

# Motivation body -> intro + numbered challenges (p-steps)
REPL.append((
    '        <ul>\n'
    '          <li>{{MOTIVATION_1}}</li>\n'
    '          <li>{{MOTIVATION_2}}</li>\n'
    '        </ul>\n'
    '        <!-- OPTIONAL: half-column Motivation figure. If the spec\'s Motivation figure line is `**Figure:** none`, REMOVE this entire <figure> block. -->\n'
    '        <figure><img src="{{TEASER_FIGURE}}" alt=""><figcaption>{{TEASER_CAPTION}}</figcaption></figure>\n',
    '        <p>Provably-correct pose estimation faces three challenges that block any worst-case guarantee:</p>\n'
    '        <div class="p-steps">\n'
    '          <div class="step"><strong>Outlier keypoints.</strong> Neural heatmap detectors can be arbitrarily wrong, corrupting the geometry.</div>\n'
    '          <div class="step"><strong>Nonconvex back-end.</strong> Outlier rejection is nonconvex; RANSAC-style heuristics give no global-optimality guarantee and can fail silently.</div>\n'
    '          <div class="step"><strong>No certified uncertainty.</strong> No prior method bounds the worst-case error between the estimate and the groundtruth.</div>\n'
    '        </div>\n'
))

# Method: inject key-equation widget between bullets and figure
REPL.append((
    '          </ul>\n          <figure class="method-figure">',
    '          </ul>\n'
    '          <div class="p-eq">$\\;\\mathbb{P}\\big[\\,y_{l+1}\\in F^{\\epsilon}(x_{l+1})\\,\\big]\\ge 1-\\epsilon\\;$'
    '<span class="where">conformal calibration guarantees every groundtruth keypoint lies in its prediction set with probability $1-\\epsilon$</span></div>\n'
    '          <figure class="method-figure">'
))

# Dataset / Benchmark -> bullets + setup chips + coverage-concentration figure (figure3)
REPL.append((
    '          <ul>\n'
    '            <li>{{DATASET_1}}</li>\n'
    '            <li>{{DATASET_2}}</li>\n'
    '          </ul>\n',
    '          <ul>\n'
    '            <li><strong>LineMOD-Occlusion (LM-O):</strong> 1214 test images, 8 heavily-occluded objects on a table.</li>\n'
    '            <li>200 BOP-selected images form the calibration set; uniform pose sampling keeps conformal <em>exchangeability</em> plausible.</li>\n'
    '          </ul>\n'
    '          <div class="p-chips">\n'
    '            <span>gt-ball</span><span>gt-ellipse</span>\n'
    '            <span class="alt">frcnn-ball</span><span class="alt">frcnn-ellipse</span>\n'
    '          </div>\n'
    '          <figure><img src="assets/figures/figure3.png" alt=""><figcaption>Conditional coverage concentrates around $1-\\epsilon$ as calibration size $n$ grows ($\\epsilon=0.1$).</figcaption></figure>\n'
))

# Key Results -> empirical-coverage figure (figure4) + insight callout-bar
REPL.append((
    '          <table class="results">\n'
    '            <tr><th>Method</th><th>Metric</th></tr>\n'
    '            <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>\n'
    '            <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>\n'
    '          </table>\n'
    '          <div class="callout">{{HEADLINE_DELTA}}</div>\n'
    '          <p class="conclusion">{{KEY_RESULT_CONCLUSION}}</p>\n',
    '          <figure><img src="assets/figures/figure4.png" alt=""><figcaption>Empirical coverage per LM-O object across all four setups &mdash; every object meets the 90% target ($\\epsilon=0.1$).</figcaption></figure>\n'
    '          <div class="p-callout-bar">Whenever PURSE covers the true pose, the certified bound is never violated &mdash; correct in 100% of covered cases, exactly the $1-\\epsilon$ guarantee.</div>\n'
))

# Ablation -> ε trade-off vs-compare + conclusion
REPL.append((
    '        <ul>\n'
    '          <li>{{ABLATION_1}}</li>\n'
    '          <li>{{ABLATION_2}}</li>\n'
    '        </ul>\n'
    '        <p class="conclusion">{{ABLATION_CONCLUSION}}</p>\n',
    '        <div class="p-vs">\n'
    '          <div class="side"><h4>&epsilon; = 0.1</h4><p>Larger prediction sets, ~90% coverage, more conservative bounds.</p></div>\n'
    '          <div class="sep">vs.</div>\n'
    '          <div class="side good"><h4>&epsilon; = 0.4</h4><p>Smaller sets, higher average-pose success, weaker coverage.</p></div>\n'
    '        </div>\n'
    '        <p class="conclusion">Elliptical (covariance) sets match or beat circular sets; &epsilon; is one dial trading guaranteed coverage against accuracy.</p>\n'
))

# Takeaway -> paragraph + primary callout
REPL.append((
    '        <p>{{TAKEAWAY}}</p>\n',
    '        <p>Marrying conformal prediction with geometric uncertainty propagation makes the two-stage pose '
    'pipeline the <strong>first</strong> to output an estimate carrying a provable, computable worst-case error '
    'bound &mdash; with no loss in accuracy.</p>\n'
    '        <div class="p-callout-primary">Detector-agnostic: it wraps any heatmap keypoint network, pointing '
    'toward statistically guaranteed perception for other geometric-vision problems.</div>\n'
))

for old, new in REPL:
    if old not in html:
        sys.exit(f"ANCHOR NOT FOUND:\n{old!r}")
    html = html.replace(old, new, 1)

# ---- simple placeholder fills ----
SUBS = {
    "{{TITLE}}": "Object Pose Estimation with Statistical Guarantees: Conformal Keypoint Detection and Geometric Uncertainty Propagation",
    "{{AUTHORS}}": "Heng Yang<sup>1</sup>, Marco Pavone<sup>1</sup>",
    "{{AUTHOR_LEGEND}}": '<sup>1</sup> NVIDIA Research',
    "{{VENUE_NAME}}": "CVPR",
    "{{VENUE_YEAR}}": "2023",
    "{{CONTACT}}": "",
    "{{LOGO_1}}": "assets/logos/nvidia-research.png",
    "{{LOGO_2}}": "", "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",
    "{{URL_PROJECT}}": "",
    # commented-out doc/template references (inside HTML comments) -> blank so the leftover check passes
    "{{VENUE_LOGO}}": "",
    "{{CONTRIBUTION_1}}": "", "{{CONTRIBUTION_2}}": "", "{{CONTRIBUTION_3}}": "",
    # Method bullets + figure
    "{{METHOD_1}}": "<strong>Conformal keypoint detection.</strong> Calibrate heatmap nonconformity scores on 200 images to build per-keypoint prediction sets &mdash; circular (peak) or elliptical (covariance) &mdash; with 1&minus;&epsilon; coverage.",
    "{{METHOD_2}}": "<strong>Geometric uncertainty propagation.</strong> Those keypoint sets become quadratic constraints defining the nonconvex Pose UnceRtainty SEt (PURSE) over SE(3).",
    "{{METHOD_3}}": "<strong>RANSAG + SDP.</strong> RANSAG samples keypoints, solves P3P/PnP and averages accepted poses; a semidefinite relaxation certifies worst-case rotation &amp; translation bounds.",
    "{{METHOD_FIGURE}}": "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": "Pipeline: heatmaps &rarr; conformalized circular/elliptical keypoint sets &rarr; PURSE &rarr; RANSAG average pose &rarr; SDP worst-case error bounds.",
    # Headline numbers
    "{{HERO_VAL}}": "90%",
    "{{HERO_LABEL}}": "Target coverage attained &middot; LM-O &middot; &epsilon;=0.1",
    "{{HERO_NOTE}}": "with only n = 200 calibration images",
    "{{STAT_2_VAL}}": "70.6%", "{{STAT_2_LBL}}": "avg-pose success",
    "{{STAT_3_VAL}}": "61.1%", "{{STAT_3_LBL}}": "PVNet baseline",
    "{{STAT_4_VAL}}": "100%", "{{STAT_4_LBL}}": "bounds correct",
}
missing = [k for k in SUBS if k not in html]
if missing:
    sys.exit(f"placeholder(s) not in template: {missing}")
for k, v in SUBS.items():
    html = html.replace(k, v)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
