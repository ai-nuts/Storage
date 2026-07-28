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
    "{{TITLE}}":         "Truly Scale-Equivariant Deep Nets with Fourier Layers",
    "{{AUTHORS}}":       "Md Ashiqur Rahman<sup>1</sup>, Raymond A. Yeh<sup>1</sup>",
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> Department of Computer Science, Purdue University",
    "{{VENUE_NAME}}":    "NeurIPS",
    "{{VENUE_YEAR}}":    "2023",
    "{{VENUE_LOGO}}":    "assets/logos/_venue.png",
    "{{CONTACT}}":       "",
    "{{LOGO_1}}": "assets/logos/purdue-university.png",
    "{{LOGO_2}}": "", "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png", "{{QR_CODE}}": "assets/qr/code.png",

    "{{PROBLEM}}": "Existing scale-equivariant CNNs are not <em>truly</em> scale-equivariant: they enforce equivariance through weight-sharing and kernel resizing, yet still incur a <strong>non-negligible equivariance error</strong> in practice.",

    "{{MOTIVATION_1}}": "Down-scaling a discrete signal is a signal-processing operation: the Nyquist theorem <strong>requires an anti-aliasing filter</strong> before subsampling.",
    "{{MOTIVATION_2}}": "Prior methods derive resizing in the <strong>continuous domain</strong>, leaving no place for anti-aliasing, so high frequencies alias into low ones and break equivariance.",
    "{{TEASER_FIGURE}}": "assets/figures/figure2.png",
    "{{TEASER_CAPTION}}": "Ideal low-pass (anti-aliasing) filter H zeros frequencies above the new Nyquist limit before subsampling.",

    "{{METHOD_1}}": "Define down-scaling as <strong>ideal downsampling</strong> $D_R(x)=\\mathrm{Sub}_R(h\\circledast x)$: an ideal low-pass filter, then subsampling.",
    "{{METHOD_2}}": "<strong>Claim 1:</strong> a net is scale-equivariant iff every output frequency $Y[k]$ depends only on equal-or-lower input frequencies $X[-k{:}k]$.",
    "{{METHOD_3}}": "Redesign every module &mdash; a spatially-local <strong>Fourier convolution</strong>, a frequency-aware non-linearity, and Fourier pooling &mdash; to satisfy the condition.",
    "{{METHOD_FIGURE}}": "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": "Downsampling our high-res feature reproduces the low-res feature exactly; a regular CNN's features diverge across resolutions.",

    "{{BASELINE}}": "DISCO", "{{BASELINE_NUM}}": "0.9856",
    "{{OURS}}": "Ours", "{{OURS_NUM}}": "0.9889",
    "{{HEADLINE_DELTA}}": "0.00 equivariance error &mdash; exact, by construction",
    "{{KEY_RESULT_CONCLUSION}}": "Our model tops every MNIST-scale metric; the gain widens to ~15 pts on natural STL10-scale images.",

    "{{HERO_VAL}}": "0.00",
    "{{HERO_LABEL}}": "End-to-end scale-equivariance error",
    "{{HERO_NOTE}}": "exact, by construction",
    "{{STAT_2_VAL}}": "0.9889", "{{STAT_2_LBL}}": "MNIST-scale acc",
    "{{STAT_3_VAL}}": "0.7332", "{{STAT_3_LBL}}": "STL10-scale acc",
    "{{STAT_4_VAL}}": "0.9716", "{{STAT_4_LBL}}": "scale-consistency",

    "{{TAKEAWAY}}": "Formulate down-scaling as ideal, anti-aliased downsampling and enforce the frequency-dependency rule via Fourier layers: the network becomes <em>exactly</em> scale-equivariant, not merely approximately, while staying accurate and data-efficient.",
}

DROP_SECTIONS = ["contribution", "dataset-benchmark", "ablation-study"]
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
