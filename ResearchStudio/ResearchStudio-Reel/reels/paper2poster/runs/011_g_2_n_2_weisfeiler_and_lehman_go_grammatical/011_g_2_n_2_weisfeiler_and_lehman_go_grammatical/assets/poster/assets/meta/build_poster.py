#!/usr/bin/env python3
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    "{{TITLE}}": "G²N²: Weisfeiler and Lehman Go Grammatical",
    "{{AUTHORS}}": ("Jason Piquenot<sup>1</sup>, Aldo Moscatelli<sup>1</sup>, "
                    "Maxime Bérar<sup>1</sup>, Pierre Héroux<sup>1</sup>, "
                    "Jean-Yves Ramel<sup>2</sup>, Romain Raveaux<sup>2</sup>, "
                    "Sébastien Adam<sup>1</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> LITIS Lab, University of Rouen Normandy "
                          "&nbsp;&nbsp; <sup>2</sup> LIFAT Lab, University of Tours"),
    "{{CONTACT}}": "",
    "{{VENUE_LOGO}}": "",
    "{{VENUE_NAME}}": "ICLR",
    "{{VENUE_YEAR}}": "2024",
    "{{LOGO_1}}": "assets/logos/litis-lab-university-of-rouen-normandy.png",
    "{{LOGO_2}}": "assets/logos/lifat-lab-university-of-tours.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",
    "{{URL_PROJECT}}": "",
    "{{METHOD_FIGURE}}": "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": ("Overview of the framework instantiated on ML(L₃): the language "
                           "fragment → exhaustive CFG → reduced grammar r-G(L₃), whose rules "
                           "become the G²N² layer."),
    # hero placeholders survive only inside a doc comment; fill for the leftover check
    "{{HERO_VAL}}": "0.342", "{{HERO_LABEL}}": "QM9 R² MAE", "{{HERO_NOTE}}": "",
    # contribution block stays commented (not rendered); fill so no {{...}} leaks
    "{{CONTRIBUTION_1}}": "A generic framework turning any fragment of an algebraic language into a GNN via context-free grammars.",
    "{{CONTRIBUTION_2}}": "An instantiation on ML(L₃) yielding G²N², a provably 3-WL GNN.",
    "{{CONTRIBUTION_3}}": "Experiments: G²N² beats existing 3-WL GNNs on regression, classification, and spectral tasks.",
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
