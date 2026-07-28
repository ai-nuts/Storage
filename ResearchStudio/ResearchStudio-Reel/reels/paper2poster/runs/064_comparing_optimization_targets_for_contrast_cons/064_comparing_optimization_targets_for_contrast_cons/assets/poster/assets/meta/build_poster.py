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
    "{{TITLE}}": "Comparing Optimization Targets for Contrast-Consistent Search",
    "{{AUTHORS}}": "Hugo Fry<sup>1</sup>, Seamus Fallows<sup>1</sup>, Ian Fan<sup>1</sup>, Jamie Wright<sup>2</sup>, Nandi Schoots<sup>3</sup>",
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> Independent &nbsp;&nbsp; <sup>2</sup> Oxford University &nbsp;&nbsp; <sup>3</sup> King's College London",
    "{{CONTACT}}": "",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{VENUE_NAME}}": "NeurIPS",
    "{{VENUE_YEAR}}": "2023",
    "{{LOGO_1}}": "assets/logos/oxford-university.png",
    "{{LOGO_2}}": "assets/logos/king-s-college-london.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",
    # contribution comment block still carries these tokens -> fill empty so leftover-check passes
    "{{CONTRIBUTION_1}}": "", "{{CONTRIBUTION_2}}": "", "{{CONTRIBUTION_3}}": "",

    "{{PROBLEM}}": "Contrast-Consistent Search (CCS) recovers a language model's internal &ldquo;truth&rdquo; direction without labels, using only the constraint that a statement and its negation must disagree. Yet <strong>what its loss actually optimizes for &mdash; and whether that target is optimal &mdash; is poorly understood.</strong>",

    "{{MOTIVATION_1}}": "Safely deploying LLMs means reliably reading their <strong>latent knowledge of truth</strong>; understanding <em>why</em> a probe like CCS works is a prerequisite for trusting and improving it.",
    "{{MOTIVATION_2}}": "Prior work framed CCS around <strong>clustering activations</strong> and learning <strong>calibrated probabilities</strong>. The authors show both pictures are misleading.",
    "{{TEASER_FIGURE}}": "assets/figures/page8_figure2.png",
    "{{TEASER_CAPTION}}": "CCS prober outputs on UnifiedQA T5-Large: the encoder (a) is highly <em>confident</em> yet only 52.3% accurate, while the decoder (b) piles near 0.5 yet reaches 97.8% &mdash; confident &ldquo;probabilities&rdquo; can mislead.",

    "{{METHOD_1}}": "Decompose CCS along a unit direction <span class=\"num\">&theta;&#770;</span> into two statistics: <strong>displacement variance</strong> &sigma;<sub>d</sub><sup>2</sup> (how far a statement and its negation are pushed apart) and <strong>midpoint variance</strong> &sigma;<sub>m</sub><sup>2</sup> (how far their midpoint sits from the origin).",
    "{{METHOD_2}}": "CCS&rsquo;s double-saturating sigmoid forces a <strong>trade-off</strong> &mdash; maximize &sigma;<sub>d</sub><sup>2</sup> while minimizing &sigma;<sub>m</sub><sup>2</sup> &mdash; so CCS implicitly optimizes a balance of the two.",
    "{{METHOD_3}}": "The new <strong>Midpoint-Displacement (MD)</strong> loss makes this trade-off explicit via one knob &lambda;: <span class=\"hi\">MD-CCS</span> (&lambda; mimics CCS) and <span class=\"hi\">MD-Acc</span> (&lambda; tuned for accuracy).",
    "{{METHOD_FIGURE}}": "assets/figures/page7_figure1.png",
    "{{METHOD_CAPTION}}": "Activations projected onto PC&#8201;1 (x) and the CCS direction &theta;&#770; (y), coloured by ground-truth label. CCS classifies by <strong>displacement</strong> along &theta;&#770;, not a separating hyperplane.",

    "{{BASELINE}}": "CCS", "{{BASELINE_NUM}}": "0.7105",
    "{{OURS}}": "MD-Acc", "{{OURS_NUM}}": "0.7557",
    "{{HEADLINE_DELTA}}": "+4% avg accuracy over CCS &middot; wins on 3 of 4 models",
    "{{KEY_RESULT_CONCLUSION}}": "MD-CCS&rsquo;s 0.63 similarity (vs 0.14&ndash;0.17 for other accurate losses) is specific to MD &mdash; it faithfully recovers CCS&rsquo;s target.",

    "{{HERO_VAL}}": "0.63",
    "{{HERO_LABEL}}": "MD-CCS &harr; CCS cosine similarity",
    "{{HERO_NOTE}}": "vs 0.78 CCS self-similarity",
    "{{STAT_2_VAL}}": "0.7557", "{{STAT_2_LBL}}": "MD-Acc test acc (CCS 0.71)",
    "{{STAT_3_VAL}}": "10<sup>&minus;237</sup>", "{{STAT_3_LBL}}": "odds of 0.63 by chance",
    "{{STAT_4_VAL}}": "4&times;5", "{{STAT_4_LBL}}": "models &times; datasets",

    "{{TAKEAWAY}}": "CCS works because of the <strong>displacement information</strong> in its contrast-pair data, not its specific loss formula &mdash; a simple Midpoint-Displacement loss reproduces CCS and, retuned, beats it.",
}

DROP_SECTIONS = ["dataset-benchmark", "ablation-study"]
for sec in DROP_SECTIONS:
    html = drop_section(html, sec)
    html = re.sub(rf'"{re.escape(sec)}"\s*,?\s*', "", html)

missing = [k for k in SUBS if k not in html]
if missing: sys.exit(f"missing: {missing}")
for t, v in SUBS.items(): html = html.replace(t, v)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover: sys.exit(f"leftover: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
