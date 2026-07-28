#!/usr/bin/env python3
import re, sys
from pathlib import Path

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

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    "{{TITLE}}": "VideoComposer: Compositional Video Synthesis with Motion Controllability",
    "{{AUTHORS}}": ("Xiang Wang<sup>1*</sup>, Hangjie Yuan<sup>1*</sup>, Shiwei Zhang<sup>1*</sup>, "
                    "Dayou Chen<sup>1*</sup>, Jiuniu Wang<sup>1</sup>, Yingya Zhang<sup>1</sup>, "
                    "Yujun Shen<sup>2</sup>, Deli Zhao<sup>1</sup>, Jingren Zhou<sup>1</sup>"),
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> Alibaba Group &nbsp;&nbsp; <sup>2</sup> Ant Group",
    "{{CONTACT}}": "",
    "{{VENUE_NAME}}": "NeurIPS",
    "{{VENUE_YEAR}}": "2023",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{LOGO_1}}": "assets/logos/alibaba-group.png",
    "{{LOGO_2}}": "assets/logos/ant-group.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",

    "{{PROBLEM}}": ("Controllable video synthesis is far harder than controllable image synthesis: "
                    "temporal dynamics vary widely across clips and every generated frame must stay "
                    "temporally consistent, so image-style spatial controls do not transfer directly."),

    "{{MOTIVATION_1}}": ("Use <strong>motion vectors</strong> from compressed video as a temporal "
                         "condition — direct, explicit guidance on the dynamics other conditions lack."),
    "{{MOTIVATION_2}}": ("Naively fusing heterogeneous conditions breaks cross-frame consistency, "
                         "motivating one unified encoder that captures space-time relations."),

    "{{METHOD_1}}": ("Decompose each video into <strong>textual</strong>, <strong>spatial</strong> and "
                     "<strong>temporal</strong> conditions that can be freely composed."),
    "{{METHOD_2}}": ("Sequential conditions pass through the <strong>STC-encoder</strong> "
                     "(2× 2D conv → avg-pool → temporal Transformer), fused by element-wise addition."),
    "{{METHOD_3}}": ("Fused controls are concatenated with the noisy latent; text &amp; style enter via "
                     "cross-attention. Two-stage training; DDIM + classifier-free guidance at inference."),
    "{{METHOD_FIGURE}}": "assets/figures/figure2.png",
    "{{METHOD_CAPTION}}": ("Overall architecture: a video is decomposed into textual, spatial and temporal "
                           "conditions, embedded by the unified STC-encoder or CLIP, then jointly guide the VLDM denoiser."),

    "{{DATASET_1}}": ("Trained on <strong>WebVid10M</strong> (10.3M web video–caption pairs) + "
                      "<strong>LAION-400M</strong> (CLIP-filtered image–caption pairs)."),
    "{{DATASET_2}}": ("Text-to-video quality on <strong>MSR-VTT</strong> (FVD, CLIPSIM); motion "
                      "controllability on 1000 caption–video pairs."),

    "{{BASELINE}}": "Stage-1 T2V pre-train", "{{BASELINE_NUM}}": "803",
    "{{OURS}}": "VideoComposer", "{{OURS_NUM}}": "580",
    "{{HEADLINE_DELTA}}": "−223 FVD from compositional training",
    "{{KEY_RESULT_CONCLUSION}}": ("Adding multi-condition compositional control costs nothing in raw "
                                  "text-to-video quality — it even improves over stage-1 pre-training."),

    "{{ABLATION_1}}": ("Adding <strong>motion vectors</strong> as a temporal condition cuts motion-control "
                       "error <span class=\"num\">4.03 → 2.67</span>."),
    "{{ABLATION_2}}": ("The <strong>STC-encoder</strong> lowers it further to "
                       "<span class=\"num\">2.18</span> — both ingredients matter."),
    "{{ABLATION_CONCLUSION}}": ("Motion vectors supply the temporal signal; the STC-encoder makes the "
                                "model actually use it, sharpening motion control and consistency."),

    "{{HERO_VAL}}": "580", "{{HERO_LABEL}}": "FVD · MSR-VTT (zero-shot)",
    "{{HERO_NOTE}}": "vs 803 stage-1 pre-training",
    "{{STAT_2_VAL}}": "0.2932", "{{STAT_2_LBL}}": "CLIPSIM ↑",
    "{{STAT_3_VAL}}": "2.18", "{{STAT_3_LBL}}": "motion-ctrl error ↓",
    "{{STAT_4_VAL}}": "8+", "{{STAT_4_LBL}}": "condition types",

    "{{TAKEAWAY}}": ("By treating a video as a composition of textual, spatial and temporal conditions — "
                     "and pairing compressed-video motion vectors with a unified STC-encoder — VideoComposer "
                     "delivers flexible, controllable video synthesis with strong inter-frame consistency and no "
                     "loss in text-to-video quality."),

    "{{TEASER_FIGURE}}": "assets/figures/figure1.png",
    "{{TEASER_CAPTION}}": ("Compositional video synthesis: VideoComposer obeys textual, spatial and temporal "
                           "conditions or their subsets — even two simple strokes prescribing motion &amp; shape."),
}

DROP_SECTIONS = ["contribution"]
for sec in DROP_SECTIONS:
    html = drop_section(html, sec)
    html = re.sub(rf'"{re.escape(sec)}"\s*,?\s*', "", html)

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
