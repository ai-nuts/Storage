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
    "{{TITLE}}": "Mechanistic Mode Connectivity",
    "{{AUTHORS}}": ('Ekdeep Singh Lubana<sup>1,2,3</sup>, Eric J. Bigelow<sup>2</sup>, '
                    'Robert P. Dick<sup>1</sup>, David Krueger<sup>4</sup>, Hidenori Tanaka<sup>2,3</sup>'),
    "{{AUTHOR_LEGEND}}": ('<sup>1</sup> University of Michigan &nbsp;&nbsp; '
                          '<sup>2</sup> Harvard University &nbsp;&nbsp; '
                          '<sup>3</sup> NTT Research, Inc. &nbsp;&nbsp; '
                          '<sup>4</sup> University of Cambridge'),
    "{{VENUE_NAME}}": "ICML", "{{VENUE_YEAR}}": "2023",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "Email: lubana@umich.edu",
    "{{LOGO_1}}": "assets/logos/university-of-michigan.png",
    "{{LOGO_2}}": "assets/logos/harvard-university.png",
    "{{LOGO_3}}": "assets/logos/physics-informatics-laboratories-ntt-research-inc.png",
    "{{LOGO_4}}": "assets/logos/university-of-cambridge.png",
    "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    # 3col suppresses scan-to-read -> leave QR/URL empty
    "{{QR_PAPER}}": "", "{{QR_CODE}}": "", "{{URL_PROJECT}}": "", "{{CONTACT}}": "Email: lubana@umich.edu",

    # ---- Problem ----
    "{{PROBLEM}}": ('Mode-connectivity theory shows a network’s many low-loss minimizers are joined by '
                    'simple paths — but it ignores <strong>what mechanism</strong> each minimizer uses, '
                    'so it cannot say whether two solutions predict from the same or different input attributes.'),

    # ---- Motivation ----
    "{{MOTIVATION_1}}": ('Two models can both reach low loss yet rely on <strong>entirely different cues</strong> '
                         '— an object’s background vs. its shape.'),
    "{{MOTIVATION_2}}": ('Fine-tuned models stay <em>linearly connected</em> to their pretraining solution, hinting '
                         'that naive fine-tuning may never remove reliance on a spurious attribute.'),
    "{{TEASER_FIGURE}}": "assets/figures/figure1.png",
    "{{TEASER_CAPTION}}": ("Are mechanistically dissimilar minimizers (background- vs. shape-reliant) connected by "
                           "simple low-loss paths — and can we exploit this to switch mechanisms?"),

    # ---- Method ----
    "{{METHOD_1}}": ('<strong>Mechanistic similarity.</strong> Two models are similar if invariant to the same '
                     'unit interventions on the data-generating latents (e.g. shape vs. background).'),
    "{{METHOD_2}}": ('<strong>Connectivity theorem.</strong> A loss barrier on the <em>linear</em> path between two '
                     'minimizers (even after permutation symmetries) implies they are mechanistically dissimilar.'),
    "{{METHOD_FIGURE}}": "assets/figures/figure2.png",
    "{{METHOD_CAPTION}}": ("Mechanistic similarity: models are compared by how their predictions respond to unit "
                           "interventions on latent factors of the data-generating process."),

    # ---- Dataset / Benchmark (first-class: paper introduces them) ----
    "{{DATASET_1}}": ('Three synthetic cue-augmented benchmarks embed an easily separable spurious cue whose '
                      'value is conditioned on the label.'),
    "{{DATASET_2}}": ('Every dataset ships <strong>counterfactual splits</strong> (No / With / Randomized cue, '
                      'Randomized image) that directly measure reliance on spurious vs. natural attributes.'),

    # ---- Key Results (2-col fallback; upgraded to 3-col table by a follow-up edit) ----
    "{{BASELINE}}": "Fine-tune", "{{BASELINE_NUM}}": "17.5%",
    "{{OURS}}": "CBFT (ours)", "{{OURS_NUM}}": "73.4%",
    "{{HEADLINE_DELTA}}": "+55.9 pts Randomized-Cue accuracy — CBFT stays cue-invariant where fine-tuning collapses",
    "{{SECONDARY_FIGURE}}": "assets/figures/figure4.png",
    "{{SECONDARY_CAPTION}}": ("ResNet-18 minimizers trained with vs. without cues: quadratic paths connect them, "
                              "but linear paths cannot — even after permutation — confirming dissimilar mechanisms."),
    "{{KEY_RESULT_CONCLUSION}}": ("Linear disconnection is a reliable signal of differing mechanisms; naive "
                                  "fine-tuning stays connected and keeps its cue reliance."),

    # ---- Headline Numbers ----
    "{{HERO_VAL}}": "73.4%", "{{HERO_LABEL}}": "CBFT accuracy · Randomized-Cue · CIFAR-10",
    "{{HERO_NOTE}}": "vs. 17.5% for fine-tuning — 4× higher",
    "{{STAT_2_VAL}}": "74.1%", "{{STAT_2_LBL}}": "CBFT No-Cue acc.",
    "{{STAT_3_VAL}}": "8.8%", "{{STAT_3_LBL}}": "Rand-Image ≈ chance",
    "{{STAT_4_VAL}}": "60–100%", "{{STAT_4_LBL}}": "cue proportion swept",

    # ---- Takeaway ----
    "{{TAKEAWAY}}": ("Whether two low-loss models are linearly connected tells you whether they share mechanisms "
                     "— a practical lever to deliberately edit a model and strip spurious-attribute reliance."),
}

# Activate the KEY EQUATION: replace the Method equation comment block with a live .p-eq widget.
EQN = (r'<div class="p-eq">$$\mathcal{L}_{\text{CBFT}} = \mathcal{L}_{CE}\!\left(f(D_{NC};\theta),y\right) '
       r'+ \mathcal{L}_{B} + \tfrac{1}{K}\,\mathcal{L}_{I}$$'
       r'<span class="where">CBFT objective: cross-entropy on cue-free data + a <b>barrier loss</b> '
       r'$\mathcal{L}_B$ that raises loss along the linear path to the cue-relying model + an '
       r'<b>invariance loss</b> $\mathcal{L}_I$ aligning counterfactual representations.</span></div>')
html = re.sub(r'<!-- ★ KEY EQUATION.*?-->', lambda m: EQN, html, count=1, flags=re.S)

# Drop optional sections not rendered at lean stage (keep dataset-benchmark: first-class).
for sec in ["contribution", "ablation-study"]:
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
