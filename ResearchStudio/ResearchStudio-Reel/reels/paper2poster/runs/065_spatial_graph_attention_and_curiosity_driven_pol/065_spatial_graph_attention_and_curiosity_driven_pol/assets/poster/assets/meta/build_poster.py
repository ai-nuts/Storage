#!/usr/bin/env python3
import re, sys
from pathlib import Path

def drop_section(doc, sec):
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
    "{{TITLE}}": "Spatial Graph Attention and Curiosity-driven Policy for Antiviral Drug Discovery",
    "{{AUTHORS}}": ("Yulun Wu<sup>1,2</sup>, Mikaela Cashman<sup>3,2</sup>, Nicholas Choma<sup>4,2</sup>, "
                    "Érica T. Prates<sup>3,2</sup>, Verónica Melesse Vergara<sup>5,3</sup>, Manesh Shah<sup>5</sup>, "
                    "Andrew Chen<sup>4,2</sup>, Austin Clyde<sup>6</sup>, Thomas S. Brettin<sup>7</sup>, "
                    "Wibe A. de Jong<sup>4,2</sup>, Neeraj Kumar<sup>8,2</sup>, Martha S. Head<sup>3,2</sup>, "
                    "Rick L. Stevens<sup>6,7</sup>, Peter Nugent<sup>4,2</sup>, Daniel A. Jacobson<sup>5,3,2</sup>, "
                    "James B. Brown<sup>1,4,2</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> UC Berkeley &nbsp;&nbsp; <sup>2</sup> National Virtual Biotechnology Lab, US DOE "
                          "&nbsp;&nbsp; <sup>3</sup> Oak Ridge Nat. Lab &nbsp;&nbsp; <sup>4</sup> Lawrence Berkeley Nat. Lab "
                          "&nbsp;&nbsp; <sup>5</sup> Univ. of Tennessee, Knoxville &nbsp;&nbsp; <sup>6</sup> Univ. of Chicago "
                          "&nbsp;&nbsp; <sup>7</sup> Argonne Nat. Lab &nbsp;&nbsp; <sup>8</sup> Pacific Northwest Nat. Lab"),
    "{{VENUE_NAME}}": "ICLR",
    "{{VENUE_YEAR}}": "2022",
    "{{VENUE_TAG}}": "",
    "{{VENUE_LINK}}": "https://github.com/yulun-rayn/DGAPN",
    "{{CONTACT}}": "Email: yulun_wu@berkeley.edu",
    "{{LOGO_1}}": "assets/logos/university-of-california-berkeley.png",
    "{{LOGO_2}}": "assets/logos/oak-ridge-national-laboratory.png",
    "{{LOGO_3}}": "assets/logos/lawrence-berkeley-national-laboratory.jpg",
    "{{LOGO_4}}": "assets/logos/university-of-tennessee-knoxville.png",
    "{{LOGO_5}}": "assets/logos/university-of-chicago.png",
    "{{LOGO_6}}": "assets/logos/argonne-national-laboratory.png",
    # v5 header: titlebar QR
    "{{HDR_QR_PAPER}}": "assets/qr/paper.png",
    "{{HDR_QR_CODE}}": "assets/qr/code.png",
    # scan section suppressed under v5
    "{{QR_PAPER}}": "",
    "{{QR_CODE}}": "",

    "{{PROBLEM}}": ("Automatically designing graph-structured molecules that optimize a target property is hard: "
                    "chemical space is discrete and astronomically large, and compressing a connected molecular "
                    "graph into a faithful, learnable representation is nontrivial."),

    "{{MOTIVATION_1}}": ("Prior generative models under-encode molecules, ignoring bond attributes and 3D spatial "
                         "structure, though shape and complementarity to the receptor pocket decide binding."),
    "{{MOTIVATION_2}}": ("Atom-by-atom action spaces yield long, unstable trajectories, hard-to-synthesize "
                         "molecules, and poor exploration of chemical space."),
    "{{TEASER_FIGURE}}": "assets/figures/figure1.png",
    "{{TEASER_CAPTION}}": ("Spatial Graph Attention (sGAT): node-centric self-attention over atom and bond attributes, "
                           "plus a spatial channel from a sparsified inverse-distance matrix, aggregated per layer."),

    "{{METHOD_1}}": ("<strong>Fragment MDP.</strong> The CReM library proposes valid fragment-swap candidates; an "
                     "attentional policy picks the next molecule, so every step stays chemically valid and synthesizable."),
    "{{METHOD_2}}": ("<strong>sGAT state encoder.</strong> Attends over node/edge attributes and adds a spatial "
                     "convolution on a sparsified inverse-distance matrix, so chemistry and geometry both inform the state."),
    "{{METHOD_3}}": ("<strong>Curiosity-driven RL.</strong> Trained with PPO (actor-critic); random network distillation "
                     "supplies an innovation reward that drives exploration toward novel states."),
    "{{METHOD_FIGURE}}": "assets/figures/figure2.png",
    "{{METHOD_CAPTION}}": ("DGAPN in one generation step: CReM proposes candidates, a shared sGAT encoder feeds graph "
                           "query/key encoders, the policy samples the next molecule, and reward combines evaluation "
                           "with an RND curiosity score."),

    "{{DATASET_1}}": ("<strong>Primary task:</strong> design novel inhibitors of the SARS-CoV-2 NSP15 site; binding "
                      "affinity estimated by GPU-accelerated molecular docking on the 3D protein structure."),
    "{{DATASET_2}}": ("Starts from purchasable molecules with NSP15 docking scores (Kiss et al., 2012); also evaluated "
                      "on standard QED and penalized-LogP optimization tasks."),

    "{{BASELINE}}": "MolDQN",
    "{{BASELINE_NUM}}": "−8.01",
    "{{OURS}}": "DGAPN (ours)",
    "{{OURS_NUM}}": "−10.07",
    "{{HEADLINE_DELTA}}": "−10.07 best docking vs MolDQN's −8.01 &nbsp;·&nbsp; p = 8.55×10⁻²⁰⁹ (Welch's t-test)",
    "{{KEY_RESULT_CONCLUSION}}": ("DGAPN beats all five SOTA generators on binding affinity while producing more "
                                  "synthesizable molecules."),

    "{{ABLATION_1}}": ("<strong>Spatial channel matters.</strong> Spatial convolution strongly improves supervised "
                       "molecular representation learning (loss curves over 40 runs)."),
    "{{ABLATION_2}}": ("<strong>Curiosity helps.</strong> Removing innovation rewards (GAPN) worsens top docking "
                       "−9.19 vs −10.07; DGAPN even beats a CReM greedy oracle that sees intermediate rewards."),
    "{{ABLATION_CONCLUSION}}": ("Both the spatial channel and the RND curiosity bonus contribute; innovation trades a "
                                "little synthetic accessibility for better docking."),

    "{{HERO_VAL}}": "−10.07",
    "{{HERO_LABEL}}": "Best docking score · NSP15",
    "{{HERO_NOTE}}": "vs −8.01 for MolDQN (2nd best)",
    "{{STAT_2_VAL}}": "−6.77",
    "{{STAT_2_LBL}}": "mean docking",
    "{{STAT_3_VAL}}": "10⁻²⁰⁹",
    "{{STAT_3_LBL}}": "p-value vs 2nd best",
    "{{STAT_4_VAL}}": "0.72",
    "{{STAT_4_LBL}}": "QED (ω = 0.6)",

    "{{TAKEAWAY}}": ("By encoding 3D molecular structure with spatial graph attention and driving exploration with an "
                     "RND curiosity bonus over a fragment-based action space, DGAPN generates higher-affinity, more "
                     "synthesizable drug candidates than prior state-of-the-art generators."),
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
