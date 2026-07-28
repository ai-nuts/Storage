#!/usr/bin/env python3
"""Disk-to-disk substitution for the composed 3col poster. Emits only small
paper-specific strings; the ~100KB template is read from disk, never printed."""
import re
import sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# 1. Strip instructional HTML comments that still carry {{...}} example tokens
#    (ablation block, key-equation note, optional-figure/dataset guidance).
html = re.sub(r'<!--(?:(?!-->).)*?\{\{(?:(?!-->).)*?-->', '', html, flags=re.S)

# 2. Exact-substring block replacements (section bodies + widgets).
BLOCKS = [
    # --- Problem ---
    ("        <p>{{PROBLEM}}</p>",
     "        <p>Underwater salient instance segmentation must find and mask the visually most "
     "important objects in a scene &mdash; yet complex underwater conditions distort images, and no "
     "large-scale pixel-level salient dataset exists to train modern models.</p>\n"
     "        <div class=\"p-banner\"><div class=\"tag\">Gap</div><div>SAM generalizes poorly "
     "underwater and needs manual point/box prompts &mdash; unavailable in automatic salient "
     "segmentation.</div></div>"),

    # --- Motivation bullets + callout-bar ---
    ("        <ul>\n          <li>{{MOTIVATION_1}}</li>\n          <li>{{MOTIVATION_2}}</li>\n        </ul>",
     "        <ul>\n"
     "          <li>Foundation models like <strong>SAM</strong> segment strongly, but without "
     "underwater adaptation they underperform in murky, low-contrast marine scenes.</li>\n"
     "          <li>Prior salient-instance datasets are small and class-agnostic, limiting both "
     "training and the study of multi-class underwater saliency.</li>\n"
     "        </ul>\n"
     "        <div class=\"p-callout-bar\">Unlock SAM underwater needs both at once: a large-scale "
     "dataset and an architecture that sees underwater and prompts itself.</div>"),

    ("<figure><img src=\"{{TEASER_FIGURE}}\" alt=\"\"><figcaption>{{TEASER_CAPTION}}</figcaption></figure>",
     "<figure><img src=\"assets/figures/figure1.png\" alt=\"\"><figcaption>USIS-SAM vs. "
     "state-of-the-art on USIS10K: prior methods show extra predictions, localization faults, and "
     "instance confusion.</figcaption></figure>"),

    # --- Method bullets + equation ---
    ("        <ul>\n          <li>{{METHOD_1}}</li>\n          <li>{{METHOD_2}}</li>\n        </ul>",
     "        <ul>\n"
     "          <li><strong>UA-ViT encoder</strong> injects underwater visual prompts into a frozen "
     "SAM through a channel adapter and multi-scale convolutions (3&times;3, 5&times;5, 7&times;7) "
     "balanced by average residuals.</li>\n"
     "          <li><strong>SFPG</strong> fuses multi-layer UA-ViT features to auto-generate salient "
     "prompt embeddings &mdash; replacing SAM's manual prompts &mdash; for end-to-end "
     "segmentation.</li>\n"
     "        </ul>\n"
     "        <div class=\"p-eq\">$$F_i^{m}=\\!\\!\\sum_{s\\in\\{3,5,7\\}}\\!\\!\\mathrm{Conv}_{s\\times s}"
     "(\\mathrm{CA}(F_i)),\\quad F_i^{a}=\\lambda F_i^{m}+(1-\\lambda)\\,\\mathrm{Avg}(F_i^{m})$$"
     "<span class=\"where\">Multi-scale, channel-adapted features; &lambda;&nbsp;=&nbsp;0.8 balances "
     "noise suppression.</span></div>"),

    ("<figure><img src=\"{{METHOD_FIGURE}}\" alt=\"half\"><figcaption>{{METHOD_CAPTION}}</figcaption></figure>",
     "<figure><img src=\"assets/figures/figure6.png\" alt=\"half\"><figcaption>USIS-SAM: a frozen "
     "SAM augmented with the Underwater Adaptive ViT encoder and the Salient Feature Prompt "
     "Generator; (b) the UA-ViT block.</figcaption></figure>"),

    # --- Dataset bullets + chips ---
    ("        <ul>\n          <li>{{DATASET_1}}</li>\n          <li>{{DATASET_2}}</li>\n        </ul>",
     "        <ul>\n"
     "          <li><strong>USIS10K</strong>: 10,632 underwater images with pixel-level "
     "salient-instance annotations across 7 categories &mdash; the first and largest underwater "
     "salient-instance dataset.</li>\n"
     "          <li>Diverse scenes with both class-agnostic and multi-class labels; a sharper "
     "low-contrast challenge than the prior land SIS10K benchmark.</li>\n"
     "        </ul>\n"
     "        <div class=\"p-chips\">\n"
     "          <span>Fish</span><span>Reefs</span><span>Aquatic plants</span><span>Wrecks/ruins</span>"
     "<span>Human divers</span><span>Robots</span><span>Sea-floor</span>\n"
     "        </div>"),

    # --- Key Results table (2-col -> 3-col) ---
    ("        <table class=\"results\">\n          <tr><th>Method</th><th>Metric</th></tr>\n"
     "          <tr><td class=\"method\">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>\n"
     "          <tr class=\"best\"><td class=\"method\">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>\n"
     "        </table>",
     "        <table class=\"results\">\n"
     "          <tr><th>Method</th><th>Class-agnostic mAP</th><th>Multi-class mAP</th></tr>\n"
     "          <tr><td class=\"method\">RSPrompter (TGARS'24)</td><td>58.2</td><td>38.0</td></tr>\n"
     "          <tr><td class=\"method\">WaterMask (ICCV'23)</td><td>59.0</td><td>38.7</td></tr>\n"
     "          <tr class=\"best\"><td class=\"method\">USIS-SAM (Ours)</td><td>59.7</td><td>43.1</td></tr>\n"
     "        </table>"),

    ("<div class=\"callout\">{{HEADLINE_DELTA}}</div>",
     "<div class=\"callout\">New SOTA: +1.5 mAP over RSPrompter &amp; +0.7 over WaterMask "
     "(class-agnostic); +5.1 / +4.4 mAP (multi-class).</div>"),

    ("<figure><img src=\"{{SECONDARY_FIGURE}}\" alt=\"\"><figcaption>{{SECONDARY_CAPTION}}</figcaption></figure>",
     "<figure><img src=\"assets/figures/figure7.png\" alt=\"\"><figcaption>SFPG feature maps "
     "concentrate on salient instances, unlike the model without SFPG.</figcaption></figure>"),

    ("<p class=\"conclusion\">{{KEY_RESULT_CONCLUSION}}</p>",
     "<p class=\"conclusion\">USIS-SAM sets a new state of the art on both tasks and still leads prior "
     "methods when retrained on the land SIS10K dataset.</p>"),

    # --- Takeaway prose + callout-primary ---
    ("        <p>{{TAKEAWAY}}</p>",
     "        <p>Pairing the first large-scale underwater salient dataset (USIS10K) with a SAM adapted "
     "through underwater visual prompts and automatic salient prompting sets a new state of the art "
     "for segmenting salient objects underwater.</p>\n"
     "        <div class=\"p-callout-primary\">Adapt the foundation model, give it the right data, and "
     "let it prompt itself.</div>"),
]

for old, new in BLOCKS:
    if old not in html:
        sys.exit(f"BLOCK not found (whitespace mismatch?):\n{old[:120]!r}")
    html = html.replace(old, new, 1)

# 3. Simple token fills (header + hero numbers + QR empties).
SUBS = {
    "{{TITLE}}": "Diving into Underwater: Segment Anything Model Guided Underwater Salient Instance "
                 "Segmentation and A Large-Scale Dataset",
    "{{AUTHORS}}": ("Shijie Lian<sup>1</sup>, Ziyi Zhang<sup>2</sup>, Hua Li<sup>1,3,&dagger;</sup>, "
                    "Wenjie Li<sup>1</sup>, Laurence Tianruo Yang<sup>1,4,5</sup>, "
                    "Sam Kwong<sup>6</sup>, Runmin Cong<sup>7,8</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> Hainan University &nbsp;&nbsp; <sup>2</sup> HKUST (Guangzhou) "
                          "&nbsp;&nbsp; <sup>3</sup> Southeast University &nbsp;&nbsp; "
                          "<sup>4</sup> Huazhong Univ. of Science &amp; Technology &nbsp;&nbsp; "
                          "<sup>5</sup> St. Francis Xavier University &nbsp;&nbsp; "
                          "<sup>6</sup> Lingnan University &nbsp;&nbsp; <sup>7</sup> Shandong University "
                          "&nbsp;&nbsp; <sup>8</sup> MoE Key Lab of Machine Intelligence &amp; System Control"),
    "{{CONTACT}}": "Email: lihua@hainanu.edu.cn",
    "{{VENUE_NAME}}": "ICML",
    "{{VENUE_YEAR}}": "2024",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{LOGO_1}}": "assets/logos/hainan-university.png",
    "{{LOGO_2}}": "assets/logos/the-hong-kong-university-of-science-and-technology.png",
    "{{LOGO_3}}": "assets/logos/southeast-university.png",
    "{{LOGO_4}}": "assets/logos/huazhong-university-of-science-and-technology.png",
    "{{LOGO_5}}": "assets/logos/shandong-university.png",
    "{{LOGO_6}}": "assets/logos/lingnan-university.png",
    "{{HERO_VAL}}": "59.7",
    "{{HERO_LABEL}}": "mAP &middot; class-agnostic USIS (SOTA)",
    "{{HERO_NOTE}}": "+1.5 over SAM-based RSPrompter",
    "{{STAT_2_VAL}}": "43.1", "{{STAT_2_LBL}}": "mAP &middot; multi-class",
    "{{STAT_3_VAL}}": "10,632", "{{STAT_3_LBL}}": "images &middot; 7 categories",
    "{{STAT_4_VAL}}": "81.6", "{{STAT_4_LBL}}": "AP<sub>50</sub> &middot; class-agnostic",
    "{{QR_PAPER}}": "", "{{QR_CODE}}": "",
}
for tok, val in SUBS.items():
    html = html.replace(tok, val)

# 4. Sanity: no {{...}} may survive.
leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
