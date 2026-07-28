#!/usr/bin/env python3
import re, sys
from pathlib import Path


def drop_section(doc: str, sec: str) -> str:
    m = re.search(rf'<div\b[^>]*\bdata-section="{re.escape(sec)}"', doc)
    if not m:
        return doc
    start = doc.rfind("<div", 0, m.end())
    i, depth = start, 0
    while i < len(doc):
        o, c = doc.find("<div", i), doc.find("</div>", i)
        if c == -1:
            return doc
        if o != -1 and o < c:
            depth += 1; i = o + 4
        else:
            depth -= 1; i = c + len("</div>")
            if depth == 0:
                while i < len(doc) and doc[i] in " \t\r\n":
                    i += 1
                return doc[:start] + doc[i:]
    return doc


target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    "{{TITLE}}": "InfinityGAN: Towards Infinite-Pixel Image Synthesis",
    "{{AUTHORS}}": ("Chieh Hubert Lin<sup>1</sup>, Hsin-Ying Lee<sup>2</sup>, "
                    "Yen-Chi Cheng<sup>3</sup>, Sergey Tulyakov<sup>2</sup>, "
                    "Ming-Hsuan Yang<sup>1,4,5</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> UC Merced &nbsp;&nbsp; <sup>2</sup> Snap Inc. "
                          "&nbsp;&nbsp; <sup>3</sup> Carnegie Mellon University &nbsp;&nbsp; "
                          "<sup>4</sup> Yonsei University &nbsp;&nbsp; <sup>5</sup> Google Research"),
    "{{CONTACT}}": "",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{VENUE_NAME}}": "ICLR",
    "{{VENUE_YEAR}}": "2022",
    "{{LOGO_1}}": "assets/logos/uc-merced.png",
    "{{LOGO_2}}": "assets/logos/snap-inc.png",
    "{{LOGO_3}}": "assets/logos/carnegie-mellon-university.png",
    "{{LOGO_4}}": "assets/logos/yonsei-university.png",
    "{{LOGO_5}}": "assets/logos/google.png",
    "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",

    # Problem
    "{{PROBLEM}}": ("Generating arbitrarily large &mdash; even infinite-pixel &mdash; images is "
                    "bottlenecked because existing high-resolution GANs tie <strong>computation, "
                    "memory, and training-data field-of-view</strong> directly to the output resolution."),

    # Motivation
    "{{MOTIVATION_1}}": ("Large images must stay <strong>locally and globally consistent</strong>, "
                         "avoid repetitive patterns, and look realistic."),
    "{{MOTIVATION_2}}": ("Yet prior generators lean on <strong>zero-padding</strong> for positional "
                         "cues that break down once the output size differs from training."),
    "{{TEASER_FIGURE}}": "assets/figures/figure1.png",
    "{{TEASER_CAPTION}}": ("Conventional generators (left) produce inconsistent pixels from zero-padding; "
                           "our padding-free generator (right) yields consistent values at any position."),

    # Method
    "{{METHOD_1}}": ("<strong>Structure synthesizer</strong> G<sub>S</sub> &mdash; a coordinate-driven "
                     "neural implicit function &mdash; maps global latent z<sub>g</sub>, local latent "
                     "z<sub>l</sub>, and coordinate grid c to a structural latent z<sub>S</sub>."),
    "{{METHOD_2}}": ("<strong>Padding-free texture synthesizer</strong> G<sub>T</sub> renders each patch "
                     "p<sub>c</sub> from z<sub>S</sub>, z<sub>g</sub>, and noise z<sub>n</sub>, with all "
                     "position encoding removed."),
    "{{METHOD_3}}": ("No padding + implicit coordinates &rArr; patches at the same coordinate are "
                     "<strong>identical</strong>, so independent patches tile seamlessly at "
                     "<strong>O(1) memory</strong>."),
    "{{METHOD_FIGURE}}": "assets/figures/arch_overview.png",
    "{{METHOD_CAPTION}}": ("Overview. A neural-implicit structure synthesizer G<sub>S</sub> and a "
                           "padding-free texture synthesizer G<sub>T</sub> take global/local latents, a "
                           "continuous coordinate, and noise to synthesize arbitrary-size images."),

    # Dataset / Benchmark
    "{{DATASET_1}}": ("<strong>Flickr-Landscape</strong> &mdash; a new dataset of <strong>450,000</strong> "
                      "high-quality landscape images &mdash; evaluates arbitrary-size synthesis."),
    "{{DATASET_2}}": ("Outpainting uses <strong>Places365</strong> (62,500) and <strong>Flickr-Scenery</strong> "
                      "(54,710); all models train on 101&times;101 patches from 197&times;197 images."),

    # Key Result (table replaced by a 3-col widget below)
    "{{BASELINE}}": "StyleGAN2+NCI",
    "{{BASELINE_NUM}}": "79.83",
    "{{OURS}}": "InfinityGAN",
    "{{OURS_NUM}}": "61.41",
    "{{HEADLINE_DELTA}}": "&minus;18.4 ScaleInv FID vs. best baseline at 4&times; extension",
    "{{KEY_RESULT_CONCLUSION}}": ("Beyond 4&times; extension InfinityGAN beats the strongest baseline while "
                                  "holding constant memory as image size grows."),

    # Ablation
    "{{ABLATION_1}}": ("Stripping <strong>all padding</strong> from StyleGAN2+NCI removes positional cues and "
                       "collapses structure across every FID setting."),
    "{{ABLATION_2}}": ("Adding the implicit structure synthesizer <strong>G<sub>S</sub></strong> restores "
                       "position via z<sub>S</sub> and recovers quality."),
    "{{ABLATION_CONCLUSION}}": ("Confirms conventional generators depend on zero-padding for position &mdash; a "
                                "coordinate-driven implicit function is a valid, extensible replacement."),

    # Headline Numbers
    "{{HERO_VAL}}": "61.41",
    "{{HERO_LABEL}}": "ScaleInv FID &middot; 4&times; extension",
    "{{HERO_NOTE}}": "vs 79.83 best baseline",
    "{{STAT_2_VAL}}": "&gt;90%", "{{STAT_2_LBL}}": "human preference",
    "{{STAT_3_VAL}}": "7.20&times;", "{{STAT_3_LBL}}": "faster inference",
    "{{STAT_4_VAL}}": "O(1)", "{{STAT_4_LBL}}": "memory &middot; any size",

    # Takeaway
    "{{TAKEAWAY}}": ("By disentangling global appearance, structure, and texture and removing all padding, "
                     "InfinityGAN synthesizes seamless, globally-consistent images of arbitrary or infinite "
                     "size from small patches at constant memory, with parallelizable inference."),
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
