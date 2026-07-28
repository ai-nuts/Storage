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
    "{{TITLE}}": "DeepJoint: Robust Survival Modelling Under Clinical Presence Shift",
    "{{AUTHORS}}": ("Vincent Jeanselme<sup>1</sup>, Glen Martin<sup>2</sup>, Niels Peek<sup>2</sup>, "
                    "Matthew Sperrin<sup>2</sup>, Brian Tom<sup>1</sup>, Jessica Barrett<sup>1</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> University of Cambridge (MRC Biostatistics Unit) &nbsp;&nbsp; "
                          "<sup>2</sup> University of Manchester (Health e-Research Centre)"),
    "{{VENUE_NAME}}": "NeurIPS",
    "{{VENUE_YEAR}}": "2022",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "Email: vincent.jeanselme@mrc-bsu.cam.ac.uk",
    "{{LOGO_1}}": "assets/logos/university-of-cambridge.png",
    "{{LOGO_2}}": "assets/logos/university-of-manchester.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "", "{{QR_CODE}}": "",  # scan-to-read is CSS-hidden in 3col

    # Problem
    "{{PROBLEM}}": ("Clinical data arise from an <strong>informative</strong> sampling process, when, which, and how "
                    "often tests are ordered, yet survival models treat this <strong>clinical presence</strong> as "
                    "noise, hurting both accuracy and transportability when practice evolves."),

    # Motivation
    "{{MOTIVATION_1}}": ("The same patients present differently under different observation processes, so a model "
                         "overfit to one clinical-presence regime fails when practice shifts."),
    "{{MOTIVATION_2}}": ("The <strong>weekend effect</strong>, differing test intensity and mortality for weekend vs "
                         "weekday admissions, gives a controllable observation-process shift to stress-test robustness."),
    "{{TEASER_FIGURE}}": "assets/figures/figure2.png",
    "{{TEASER_CAPTION}}": ("Robustness setup: a model trained on one admission regime (weekday / weekend) is "
                           "transferred and tested on the other."),

    # Method
    "{{METHOD_1}}": ("An <strong>LSTM</strong> encodes each patient's irregular sequence of ICU laboratory tests "
                     "into a shared embedding <em>h</em>."),
    "{{METHOD_2}}": ("Three heads model clinical presence, longitudinal values <em>(Gaussian)</em>, missingness "
                     "<em>(Bernoulli)</em>, and inter-observation timing <em>(cumulative intensity)</em>, while a "
                     "<strong>DeepSurv</strong> Cox head models survival, all trained jointly."),
    "{{METHOD_FIGURE}}": "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": ("Deep Joint Model: an LSTM embedding <em>h</em> drives the longitudinal (L), "
                           "inter-observation (I), missingness (M) and survival (S) networks."),
    "{{KEY_EQUATION}}": (r"\ell(e) = (1-\alpha)\,\ell_S + \alpha \!\!\sum_{\text{task}\in\{L,I,M\}}\!\! "
                         r"w_{\text{task}}(e)\,\ell_{\text{task}}(e)"),
    "{{KEY_EQUATION_NOTE}}": ("Joint loss: survival term &#8467;<sub>S</sub> plus dynamically-weighted "
                              "clinical-presence tasks; &alpha; balances the two."),

    # Key Results (table converted to prose in a post-build edit; fill tokens honestly / empty)
    "{{BASELINE}}": "", "{{BASELINE_NUM}}": "", "{{OURS}}": "", "{{OURS_NUM}}": "",
    "{{HEADLINE_DELTA}}": ("Even lab-only DeepJoint beats GRU-D &amp; the &ldquo;Ignore&rdquo; LSTM, modelling the "
                           "process helps without feeding it in."),
    "{{SECONDARY_FIGURE}}": "assets/figures/figure3.png",
    "{{SECONDARY_CAPTION}}": ("Time-dependent C-Index at 1 / 7 / 14-day horizons (higher is better). Proposed "
                              "models (bold) lead at short horizons."),
    "{{KEY_RESULT_CONCLUSION}}": ("The edge fades at longer horizons, clinical presence chiefly signals "
                                  "short-term instability."),

    # Headline Numbers
    "{{HERO_VAL}}": "0.878",
    "{{HERO_LABEL}}": "C-Index &middot; 1-day horizon &middot; MIMIC-III",
    "{{HERO_NOTE}}": "State-of-the-art vs input-matched models",
    "{{STAT_2_VAL}}": "30,834", "{{STAT_2_LBL}}": "ICU patients",
    "{{STAT_3_VAL}}": "3", "{{STAT_3_LBL}}": "presence processes",
    "{{STAT_4_VAL}}": "1/7/14", "{{STAT_4_LBL}}": "day horizons",

    # Takeaway
    "{{TAKEAWAY}}": ("Explicitly modelling <strong>how</strong> clinical data are observed, not just their values, "
                     "yields survival models that are both more accurate and far more <strong>transportable</strong> "
                     "when clinical practice shifts."),
}

DROP_SECTIONS = ["dataset-benchmark", "ablation-study"]
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
