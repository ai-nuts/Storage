#!/usr/bin/env python3
"""build_poster.py — indirect poster fill for StyleMorph (3col)."""
import re
import sys
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
            depth += 1
            i = o + 4
        else:
            depth -= 1
            i = c + len("</div>")
            if depth == 0:
                while i < len(doc) and doc[i] in " \t\r\n":
                    i += 1
                return doc[:start] + doc[i:]
    return doc


target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    # titlebar / metadata
    "{{TITLE}}": "StyleMorph: Disentangled 3D-Aware Image Synthesis with a 3D Morphable StyleGAN",
    "{{AUTHORS}}": "Eric-Tuan Le<sup>1</sup>, Edward Bartrum<sup>1,2</sup>, Iasonas Kokkinos<sup>1</sup>",
    "{{AUTHOR_LEGEND}}": '<sup>1</sup> University College London &nbsp;&nbsp; <sup>2</sup> Alan Turing Institute',
    "{{CONTACT}}": "",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{VENUE_NAME}}": "ICLR",
    "{{VENUE_YEAR}}": "2023",
    "{{LOGO_1}}": "assets/logos/university-college-london.png",
    "{{LOGO_2}}": "assets/logos/alan-turing-institute.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    # scan-to-read (hidden in 3col) — leave empty
    "{{QR_PAPER}}": "", "{{QR_CODE}}": "", "{{URL_PROJECT}}": "",
    # Problem
    "{{PROBLEM}}": "Existing 3D-aware GANs render high-quality images but <strong>entangle geometry with appearance</strong> — shape, camera pose, object texture, and background cannot be controlled independently during synthesis.",
    # Motivation
    "{{MOTIVATION_1}}": "3D morphable models (3DMMs) give VFX and AR creators clean, separate dials for pose, shape, and appearance — but classically demand <strong>3D scanning and manual alignment</strong>.",
    "{{MOTIVATION_2}}": "Bringing that disentangled control to 3D-aware GANs <strong>without any 3D supervision</strong> would unlock editable, category-general synthesis beyond human faces.",
    "{{TEASER_FIGURE}}": "assets/figures/page2_figure1.png",
    "{{TEASER_CAPTION}}": "Disentangled control: from a synthesized sample we change one factor at a time — pose, shape, foreground, background — then compound all.",
    # Method
    "{{METHOD_1}}": "A <strong>Morphable Renderer</strong> warps camera rays into a canonical template space via a SIREN deformation field, integrating template coordinates into a low-res <strong>2D TOCS map</strong> that bottlenecks all geometric variation (shape, pose, projection).",
    "{{METHOD_2}}": "The TOCS map plus separate <strong>foreground</strong> and <strong>background</strong> appearance codes condition a StyleGAN2 <strong>deferred neural renderer</strong>, which synthesizes and alpha-composites the final high-resolution image.",
    "{{METHOD_FIGURE}}": "assets/figures/page3_figure2.png",
    "{{METHOD_CAPTION}}": "Overview: geometric modelling (template shape, deformation z<sub>s</sub>, pose φ,θ, projection) yields a 2D TOCS map that, with foreground/background codes, conditions the Deferred Neural Renderer.",
    "{{KEY_EQUATION}}": r"\hat{\mathbf{r}}(t) = f_s(\mathbf{r}(t)) = \mathbf{r}(t) + g_s(\mathbf{r}(t))",
    "{{KEY_EQUATION_NOTE}}": "A shape-code-driven offset field g<sub>s</sub> warps each world-space ray into deformation-free template space.",
    # Key Results (default 2-col tokens; table restructured to 3-col via Edit after)
    "{{BASELINE}}": "Disentangled3D",
    "{{BASELINE_NUM}}": "28.18",
    "{{OURS}}": "StyleMorph (Ours)",
    "{{OURS_NUM}}": "7.91",
    "{{HEADLINE_DELTA}}": "FFHQ FID 7.91 vs 28.18 — the only other template-based 3D-GAN",
    "{{KEY_RESULT_CONCLUSION}}": "Disentanglement costs no image quality: StyleMorph matches the strongest non-disentangled 3D-GANs while adding four-way control.",
    "{{SECONDARY_FIGURE}}": "assets/figures/page6_figure6.png",
    "{{SECONDARY_CAPTION}}": "Disentangled appearance control from a source sample (yellow) over shape (green), foreground (blue) and background (red).",
    # Headline Numbers
    "{{HERO_VAL}}": "7.91",
    "{{HERO_LABEL}}": "FFHQ FID · 256²",
    "{{HERO_NOTE}}": "vs 28.18 for Disentangled3D",
    "{{STAT_2_VAL}}": "4.29", "{{STAT_2_LBL}}": "Cats FID",
    "{{STAT_3_VAL}}": "3.49", "{{STAT_3_LBL}}": "Wild FID",
    "{{STAT_4_VAL}}": "4", "{{STAT_4_LBL}}": "factors disentangled",
    # Takeaway
    "{{TAKEAWAY}}": "By morphing a learned canonical 3D template into a purely geometric TOCS map that conditions a StyleGAN renderer, StyleMorph delivers state-of-the-art-quality synthesis with fully disentangled control over shape, pose, and foreground/background appearance — learned from 2D images alone.",
    # ablation tokens live inside a comment block — neutralize
    "{{ABLATION_1}}": "", "{{ABLATION_2}}": "", "{{ABLATION_CONCLUSION}}": "",
}

DROP_SECTIONS = ["dataset-benchmark"]
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
