#!/usr/bin/env python3
"""Indirect fill of poster.html — keeps the ~100KB template on disk."""
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
    "{{TITLE}}": "The Hessian Screening Rule",
    "{{AUTHORS}}": "Johan Larsson<sup>1</sup>, Jonas Wallin<sup>1</sup>",
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> Department of Statistics, Lund University",
    "{{VENUE_NAME}}": "NeurIPS",
    "{{VENUE_YEAR}}": "2022",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "Email: johan.larsson@stat.lu.se",
    "{{LOGO_1}}": "assets/logos/lund-university.png",
    "{{LOGO_2}}": "", "{{LOGO_3}}": "", "{{LOGO_4}}": "",
    "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",
    "{{URL_PROJECT}}": "",
    # Problem
    "{{PROBLEM}}": "Fitting the lasso along a full regularization path is costly: the optimal penalty λ is unknown, so practitioners tune it by cross-validation, refitting the whole path over high-dimensional data again and again.",
    # Motivation
    "{{MOTIVATION_1}}": "Sequential rules (the <strong>strong rule</strong>, <strong>working-set</strong>) both reduce to a <em>first-order</em> estimate of the next-step correlation — crude when predictors are highly correlated.",
    "{{MOTIVATION_2}}": "That crudeness <strong>over-screens</strong> and yields <strong>inaccurate warm starts</strong>, forcing costly KKT re-checks and extra solver passes — exactly where speed matters most.",
    # Method (bullets; equation widget + figure injected via Edit)
    "{{METHOD_1}}": "On any interval where the active set is fixed, the lasso solution is <strong>linear in λ</strong>, so the Hessian gives a <strong>second-order</strong> estimate of the next-step correlation.",
    "{{METHOD_2}}": "The same Hessian inverse yields a <strong>warm start that is exact</strong> when the active set is unchanged — the solver often converges in a <span class=\"hi\">single pass</span>.",
    "{{METHOD_3}}": "Restrict inner products to the strong-rule set for cost; maintain <strong>H</strong> and <strong>H⁻¹</strong> by low-rank updates; place the λ grid by approximate homotopy.",
    "{{METHOD_FIGURE}}": "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": "Predictors screened vs. path step at correlation ρ ∈ {0, 0.4, 0.8} (n = 200, p = 20000). The Hessian rule (black) hugs the true active-set floor (dashed); rivals keep orders of magnitude more.",
    # Key Results (table restructured + fig3 injected via Edit)
    "{{BASELINE}}": "Working+",
    "{{BASELINE_NUM}}": "541 s",
    "{{OURS}}": "Hessian",
    "{{OURS_NUM}}": "78.8 s",
    "{{HEADLINE_DELTA}}": "≈ 7–10× faster than the best prior method on large real data",
    "{{KEY_RESULT_CONCLUSION}}": "Fastest in every simulated setting and on nearly all 12 real data sets — in all but one least-squares case, under half the runner-up’s time.",
    # Headline Numbers
    "{{HERO_VAL}}": "≈10×",
    "{{HERO_LABEL}}": "Faster · e2006-tfidf",
    "{{HERO_NOTE}}": "14.3 s vs 143 s prior best",
    "{{STAT_2_VAL}}": "6.9×", "{{STAT_2_LBL}}": "YearPredMSD",
    "{{STAT_3_VAL}}": "2.6×", "{{STAT_3_LBL}}": "bcTCGA",
    "{{STAT_4_VAL}}": "4.8×", "{{STAT_4_LBL}}": "madelon",
    # Takeaway
    "{{TAKEAWAY}}": "Reusing second-order Hessian information pays off twice — tighter screening and near-exact warm starts — making the Hessian Screening Rule the fastest way to fit lasso and ℓ₁-logistic paths, especially under high correlation.",
    # Motivation figure not used
    "{{TEASER_FIGURE}}": "",
    "{{TEASER_CAPTION}}": "",
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
