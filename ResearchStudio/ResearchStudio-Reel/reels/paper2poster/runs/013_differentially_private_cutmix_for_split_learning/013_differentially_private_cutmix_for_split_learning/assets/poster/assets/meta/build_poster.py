#!/usr/bin/env python3
"""Fill this paper's content into the composed poster.html (disk-to-disk)."""
import re
import sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    # titlebar / metadata
    "{{TITLE}}":         "Differentially Private CutMix for Split Learning with Vision Transformer",
    "{{AUTHORS}}":       ("Seungeun Oh<sup>1</sup>, Sihun Baek<sup>1</sup>, Hyelin Nam<sup>1</sup>, "
                          "Seong-Lyun Kim<sup>1</sup>, Jihong Park<sup>2</sup>, Praneeth Vepakomma<sup>3</sup>, "
                          "Ramesh Raskar<sup>3</sup>, Mehdi Bennis<sup>4</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> Yonsei University &nbsp;&nbsp; <sup>2</sup> Deakin University "
                          "&nbsp;&nbsp; <sup>3</sup> Massachusetts Institute of Technology "
                          "&nbsp;&nbsp; <sup>4</sup> University of Oulu"),
    "{{VENUE_NAME}}":    "NeurIPS",
    "{{VENUE_YEAR}}":    "2022",
    "{{VENUE_TAG}}":     "",
    "{{VENUE_LINK}}":    "https://arxiv.org/abs/2210.15986",
    "{{CONTACT}}":       "",
    "{{LOGO_1}}": "assets/logos/yonsei-university.png",
    "{{LOGO_2}}": "assets/logos/massachusetts-institute-of-technology.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    # v5 titlebar QR (single paper QR); section scan-to-read is suppressed by v5
    "{{HDR_QR_PAPER}}": "assets/qr/paper.png",
    "{{HDR_QR_CODE}}":  "",
    "{{QR_PAPER}}":     "",
    "{{URL_PAPER}}":    "",
    # contribution stays commented-out in template; blank the tokens
    "{{CONTRIBUTION_1}}": "", "{{CONTRIBUTION_2}}": "", "{{CONTRIBUTION_3}}": "",

    # ---- section bodies (widgets injected via Edit after this pass) ----
    "{{PROBLEM}}": ("In split learning with a Vision Transformer, the cut-layer <strong>smashed data</strong> "
                    "stays highly similar to the raw input — ViT has no pooling or convolution — so it "
                    "<strong>leaks privacy</strong> and inflates communication cost."),
    "{{MOTIVATION_1}}": ("ViT is displacing CNN in vision, so privacy-preserving distributed training must be "
                         "rethought for pooling-free, patch-level transformer architectures."),
    "{{MOTIVATION_2}}": ("Three ViT traits — low cut-layer distortion, noise-robust global attention, patch-level "
                         "operation — point to one fix: a <strong>patch-scale regularizer</strong>."),
    "{{TEASER_FIGURE}}":  "assets/figures/figure2.png",
    "{{TEASER_CAPTION}}": "Interpolation schemes on raw images vs. smashed data: Cutout, Patch CutMix, CutMix, Mixup.",
    "{{METHOD_1}}": ("A <strong>mixer</strong> draws Dirichlet ratios &lambda;<sub>i</sub> and shares a "
                     "pseudorandom binary mask M<sub>i</sub> to each client (&Sigma;&lambda;<sub>i</sub> = 1)."),
    "{{METHOD_2}}": ("Each client masks its smashed data (Cutout), adds Gaussian noise &rarr; "
                     "<strong>DP-Cutout</strong> smashed data, and uploads it."),
    "{{METHOD_3}}": ("The server sums complementary masked patches across clients &rarr; <strong>DP-CutMix</strong> "
                     "smashed data; propagation proceeds as in vanilla SL."),
    "{{METHOD_FIGURE}}":  "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": ("DP-CutMixSL: a shared mask &rarr; Gaussian-DP Cutout at clients &rarr; the server "
                           "stitches surviving patches into DP-CutMix smashed data."),
    "{{DATASET_1}}": ("<strong>CIFAR-10</strong> &amp; <strong>Fashion-MNIST</strong> on ViT-Tiny, PiT-Tiny "
                      "(pooling transformer) and VGG-16 — spanning the CNN-to-transformer spectrum."),
    "{{DATASET_2}}": ("|C| = 10 clients, cut-layer after the embedding; RDP at N = 64, &Delta; = 0.2, "
                      "uniform &lambda;, order &alpha; = 2."),
    "{{BASELINE}}": "SplitFed", "{{BASELINE_NUM}}": "67.88",
    "{{OURS}}": "CutMixSL (ours)", "{{OURS_NUM}}": "73.77",
    "{{HEADLINE_DELTA}}": "+16.56 pp over plain SL &middot; +5.89 pp over SplitFed — CIFAR-10, ViT-Tiny",
    "{{KEY_RESULT_CONCLUSION}}": ("Patch CutMix helps transformers most; its only loss is VGG-16, where whole-patch "
                                  "swaps cost a CNN more information."),
    "{{ABLATION_1}}": ("Sweeping noise variance (Fig. 3a), DP-CutMixSL leads accuracy at almost every level with a "
                       "tighter RDP &epsilon; than DP-SL."),
    "{{ABLATION_2}}": ("Reconstruction MSE ranks robustness Cutout &gt; Patch CutMix &gt; Mixup &gt; raw — patch "
                       "mixing is ~8&times; harder to invert."),
    "{{ABLATION_CONCLUSION}}": ("An accuracy&ndash;privacy trade-off: DP-CutMix sits between DP-SL and DP-MixSL, "
                                "upper-bounded by the Mixup baseline."),
    "{{HERO_VAL}}": "73.77%",
    "{{HERO_LABEL}}": "Top-1 &middot; CIFAR-10 &middot; ViT-Tiny",
    "{{HERO_NOTE}}": "+16.56 pp over plain SL",
    "{{STAT_2_VAL}}": "71.26%", "{{STAT_2_LBL}}": "PiT-Tiny top-1",
    "{{STAT_3_VAL}}": "89.75%", "{{STAT_3_LBL}}": "F-MNIST &middot; ViT",
    "{{STAT_4_VAL}}": "~8&times;", "{{STAT_4_LBL}}": "harder to invert",
    "{{TAKEAWAY}}": ("For Vision Transformers, DP-CutMixSL breaks the privacy&ndash;accuracy trade-off: mixing "
                     "noisy masked patches across clients both tightens the DP guarantee over vanilla split "
                     "learning and improves accuracy."),
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
