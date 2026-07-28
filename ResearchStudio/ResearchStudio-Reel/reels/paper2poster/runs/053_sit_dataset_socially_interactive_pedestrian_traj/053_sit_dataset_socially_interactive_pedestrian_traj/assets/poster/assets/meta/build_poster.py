#!/usr/bin/env python3
"""Disk-to-disk poster fill for the SiT dataset poster (3col). Keeps the 100KB
template off the model output channel."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# ---- simple/global tokens ----
TOK = {
    "{{TITLE}}": "SiT Dataset: Socially Interactive Pedestrian Trajectory Dataset for Social Navigation Robots",
    "{{AUTHORS}}": "Jongwook Bae, Jungho Kim, Junyong Yun, Changwon Kang, Jeongseon Choi, Chanhyeok Kim, Junho Lee, Jungwook Choi, Jun Won Choi",
    "{{AUTHOR_LEGEND}}": "Hanyang University",
    "{{VENUE_NAME}}": "NeurIPS",
    "{{VENUE_YEAR}}": "2023",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "",
    "{{LOGO_1}}": "assets/logos/hanyang-university.png",
    "{{LOGO_2}}": "", "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "", "{{QR_CODE}}": "",
    "{{KEY_EQUATION}}": "", "{{KEY_EQUATION_NOTE}}": "",
    "{{ABLATION_1}}": "", "{{ABLATION_2}}": "", "{{ABLATION_CONCLUSION}}": "",
    # headline numbers
    "{{HERO_VAL}}": "320K", "{{HERO_LABEL}}": "3D annotations",
    "{{HERO_NOTE}}": "+ 470K 2D boxes across 60 scenes",
    "{{STAT_2_VAL}}": "60K", "{{STAT_2_LBL}}": "images",
    "{{STAT_3_VAL}}": "12K", "{{STAT_3_LBL}}": "point clouds",
    "{{STAT_4_VAL}}": "0.531", "{{STAT_4_LBL}}": "best mAP",
    "{{TEASER_FIGURE}}": "assets/figures/page2_figure1.png",
    "{{TEASER_CAPTION}}": "SiT captures full 360° pedestrian trajectories, point clouds, and ego-robot motion in real crowds (Cafe_Street_3).",
    "{{METHOD_FIGURE}}": "assets/figures/page4_figure2.png",
    "{{METHOD_CAPTION}}": "Husky UGV platform: five 360°-coverage cameras, two 16-channel LiDARs, two IMUs, and RTK.",
    "{{SECONDARY_FIGURE}}": "assets/figures/page7_figure7.png",
    "{{SECONDARY_CAPTION}}": "Pedestrian spatial density around the ego-robot: SiT (left) clusters people close and all-around vs. Waymo Open and nuScenes.",
    "{{HEADLINE_DELTA}}": "Semantic map cuts NSP-SFM error ≈18%: ADE₂₀ 0.634 → 0.517, FDE₂₀ 1.087 → 0.925.",
    "{{KEY_RESULT_CONCLUSION}}": "SiT captures the close human–robot interaction driving datasets miss, and the semantic map consistently improves prediction.",
}

# ---- block replacements (unique multi-line substrings) ----
BLOCKS = {}

BLOCKS["        <p>{{PROBLEM}}</p>"] = (
    "        <p>Social navigation robots must perceive and predict nearby pedestrian trajectories to move safely through shared spaces. Yet existing trajectory datasets never capture the close, dynamic human–robot interaction a navigating robot actually experiences.</p>\n"
    "        <div class=\"p-callout-soft\">Rooftop-camera sets (ETH, UCY, SDD) and driving sets (nuScenes, Waymo, Argoverse) keep people and the sensor on <strong>separate paths</strong> — never sharing space.</div>"
)

BLOCKS["""        <ul>
          <li>{{MOTIVATION_1}}</li>
          <li>{{MOTIVATION_2}}</li>
        </ul>"""] = (
    "        <ul>\n"
    "          <li>A robot sharing the same path at close range provokes interactive walking behaviors that only appear up close.</li>\n"
    "          <li>Training data must therefore come from a robot moving inside real crowds, with fully time-synchronized multi-modal sensors.</li>\n"
    "        </ul>\n"
    "        <div class=\"p-chips\">\n"
    "          <span class=\"muted\">STCrowd · fixed viewpoint</span>\n"
    "          <span class=\"muted\">JRDB · no trajectory form</span>\n"
    "          <span class=\"muted\">JRDB · sensors not synced</span>\n"
    "        </div>"
)

BLOCKS["""        <ul>
          <li>{{METHOD_1}}</li>
          <li>{{METHOD_2}}</li>
        </ul>"""] = (
    "        <ul>\n"
    "          <li>Remotely operated Clearpath Husky UGV carrying 2× Velodyne VLP-16 LiDARs, 5 Basler cameras (360° view), 2 IMUs, and RTK.</li>\n"
    "          <li>A pulse-per-second (PPS) signal generator triggers every LiDAR and camera for precise cross-sensor time synchronization.</li>\n"
    "        </ul>\n"
    "        <div class=\"p-steps\">\n"
    "          <div class=\"step\"><strong>Localize</strong> — RTK outdoors, LiDAR-inertial SLAM indoors, to cancel the robot's ego-motion.</div>\n"
    "          <div class=\"step\"><strong>Annotate</strong> — expert 3D cuboids at 5 Hz interpolated to 10 Hz; 2D boxes derived from shared object IDs.</div>\n"
    "          <div class=\"step\"><strong>Map &amp; anonymize</strong> — 12-layer semantic maps from point clouds; faces &amp; license plates blurred.</div>\n"
    "        </div>"
)

BLOCKS["""        <ul>
          <li>{{DATASET_1}}</li>
          <li>{{DATASET_2}}</li>
        </ul>"""] = (
    "        <ul>\n"
    "          <li>60 scenes ≈ 60K images + 12K point-cloud frames; ~470K 2D and ~320K 3D annotations.</li>\n"
    "          <li>Each 20 s clip at 10 Hz yields a 9 s trajectory; classes span pedestrian, car, bus, truck, cyclist, motorcyclist.</li>\n"
    "        </ul>\n"
    "        <table class=\"p-table\">\n"
    "          <tr><th>Benchmark task</th><th>Metric</th></tr>\n"
    "          <tr><td>3D pedestrian detection</td><td>distance-AP</td></tr>\n"
    "          <tr><td>3D multi-object tracking</td><td>sAMOTA / AMOTA</td></tr>\n"
    "          <tr><td>Trajectory prediction</td><td>ADE / FDE</td></tr>\n"
    "          <tr><td>End-to-end motion prediction</td><td>joint</td></tr>\n"
    "        </table>"
)

BLOCKS["""        <table class="results">
          <tr><th>Method</th><th>Metric</th></tr>
          <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>
          <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>
        </table>"""] = (
    "        <table class=\"results\">\n"
    "          <tr><th>Trajectory model</th><th>ADE₂₀ ↓</th><th>FDE₂₀ ↓</th></tr>\n"
    "          <tr><td class=\"method\">Y-Net</td><td>0.836</td><td>1.878</td></tr>\n"
    "          <tr><td class=\"method\">Y-Net + map</td><td>0.675</td><td>1.547</td></tr>\n"
    "          <tr><td class=\"method\">NSP-SFM</td><td>0.634</td><td>1.087</td></tr>\n"
    "          <tr class=\"best\"><td class=\"method\">NSP-SFM + map</td><td>0.517</td><td>0.925</td></tr>\n"
    "        </table>"
)

BLOCKS["        <p>{{TAKEAWAY}}</p>"] = (
    "        <p>SiT is the first pedestrian trajectory dataset recorded by a robot moving through real crowds with fully synchronized multi-modal sensors, semantic maps, and a unified perception-to-prediction benchmark.</p>\n"
    "        <div class=\"p-banner\"><div class=\"tag\">First</div><div>Close human–robot interaction data that fixed-camera and driving datasets lack — dataset, dev-kit, and trained baselines all public.</div></div>"
)

for old, new in BLOCKS.items():
    if old not in html:
        sys.exit(f"BLOCK not found:\n{old!r}")
    html = html.replace(old, new)

for t, v in TOK.items():
    html = html.replace(t, v)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
