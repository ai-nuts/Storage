#!/usr/bin/env python3
"""Disk-to-disk poster builder for the TNTK paper (3col layout)."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")


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
            depth -= 1; i = c + 6
            if depth == 0:
                while i < len(doc) and doc[i] in " \t\r\n":
                    i += 1
                return doc[:start] + doc[i:]
    return doc


# --- 1. lean render: drop optional sections ---
for sec in ["dataset-benchmark"]:
    html = drop_section(html, sec)

# --- 2. Method key-equation comment -> live .p-eq widget ---
eqn_widget = (
    '<div class="p-eq">$$ \\Theta^{(d)}(x_i,x_j) = 2^{d}\\, d\\, \\Sigma(x_i,x_j)\\,'
    '\\big(T(x_i,x_j)\\big)^{d-1}\\dot{T}(x_i,x_j) + \\big(2\\,T(x_i,x_j)\\big)^{d} $$'
    '<span class="where">Closed-form TNTK for depth-<em>d</em> perfect binary trees. '
    '<em>T</em>&nbsp;=&nbsp;split expectation, <em>&Sigma;</em>&nbsp;=&nbsp;input inner product. '
    'Constant during training &rArr; learning = kernel regression.</span></div>'
)
html = re.sub(r'<!--\s*★ KEY EQUATION.*?-->', lambda m: eqn_widget, html, flags=re.S)

# --- 3. Key Result: replace the 2-col results table with a rich 3-col p-table ---
old_table = re.search(r'<table class="results">.*?</table>', html, flags=re.S)
new_table = (
    '<table class="p-table">\n'
    '  <tr><th>Kernel</th><th>Win rate vs&nbsp;MLP-NTK</th><th>Cost in depth</th></tr>\n'
    '  <tr><td>MLP-induced NTK</td><td>&mdash; (ref)</td><td>grows &prop; d</td></tr>\n'
    '  <tr><td>RBF kernel</td><td>11.8%</td><td>n/a</td></tr>\n'
    '  <tr><td>TNTK &middot; soft (&alpha;=0.5)</td><td>13.6%</td><td>flat, O(1)</td></tr>\n'
    '  <tr class="best"><td>TNTK &middot; hard (&alpha;=32)</td><td>34.9%</td><td>flat, O(1)</td></tr>\n'
    '</table>'
)
html = html[:old_table.start()] + new_table + html[old_table.end():]

# --- 4. Problem: add a callout-bar under the prose ---
html = html.replace(
    '<p>{{PROBLEM}}</p>',
    '<p>{{PROBLEM}}</p>\n        <div class="p-callout-bar">Strong in practice, opaque in theory &mdash; '
    'gradient-trained trees had no kernel-theoretic foundation.</div>'
)

# --- 5. Motivation: add a banner between bullets and teaser figure ---
html = html.replace(
    '        <!-- OPTIONAL teaser figure.',
    '        <div class="p-banner"><div class="tag">Goal</div><div>Derive the first NTK for soft-tree '
    'ensembles &mdash; covering both ordinary and oblivious (NODE-style) trees.</div></div>\n'
    '        <!-- OPTIONAL teaser figure.'
)

# --- 6. Takeaway: render as a mic-drop callout-primary ---
html = html.replace(
    '<p>{{TAKEAWAY}}</p>',
    '<div class="p-callout-primary">{{TAKEAWAY}}</div>'
)

# --- 7. PLAYLIST sync ---
html = html.replace(
    '["title", "problem", "motivation", "method", "dataset-benchmark", "key-result", "takeaway"]',
    '["title", "problem", "motivation", "method", "key-result", "takeaway"]'
)

# --- 8. simple placeholder fills ---
SUBS = {
    "{{TITLE}}": "A Neural Tangent Kernel Perspective of Infinite Tree Ensembles",
    "{{AUTHORS}}": "Ryuichi Kanoh<sup>1,2</sup>, Mahito Sugiyama<sup>1,2</sup>",
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> National Institute of Informatics &nbsp;&nbsp; "
                         "<sup>2</sup> The Graduate University for Advanced Studies, SOKENDAI",
    "{{VENUE_NAME}}": "ICLR",
    "{{VENUE_YEAR}}": "2022",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{LOGO_1}}": "assets/logos/national-institute-of-informatics.png",
    "{{LOGO_2}}": "assets/logos/the-graduate-university-for-advanced-studies.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{CONTACT}}": "",
    "{{QR_PAPER}}": "",

    # Problem
    "{{PROBLEM}}": "Soft tree ensembles are trained by gradient descent and excel on tabular data, "
                   "yet almost no theory explains their training dynamics, generalization, or the "
                   "empirical tricks practitioners rely on.",

    # Motivation
    "{{MOTIVATION_1}}": "The Neural Tangent Kernel (NTK) explains training and generalization of "
                        "infinitely-wide networks &mdash; and every architecture induces its own distinct kernel.",
    "{{MOTIVATION_2}}": "But an NTK had never been derived for tree models, leaving infinite "
                        "soft-tree ensembles theoretically opaque.",
    "{{TEASER_FIGURE}}": "assets/figures/figure4.png",
    "{{TEASER_CAPTION}}": "Normal tree (left) vs. oblivious tree (right): oblivious trees share the "
                          "splitting rule within each depth, while leaf values stay free.",

    # Method
    "{{METHOD_1}}": "Take the number of trees to infinity (<em>M</em>&nbsp;&rarr;&nbsp;&infin;): the "
                    "Tree NTK converges in probability to a deterministic kernel with separate "
                    "inner-node and leaf contributions.",
    "{{METHOD_2}}": "Soft splits use a scaled error function (smooth sigmoid) of hardness <em>&alpha;</em>; "
                    "all split expectations are closed-form, so the kernel is analytic and non-recursive in depth.",
    "{{METHOD_FIGURE}}": "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": "An ensemble of <em>M</em> soft trees: each internal node <em>w</em> applies a "
                          "soft split, leaf outputs &pi; are averaged and scaled by 1/&radic;<em>M</em>.",

    # Key Result
    "{{HEADLINE_DELTA}}": "TNTK beats the MLP-induced NTK on <strong>&gt;30%</strong> of the 90 datasets "
                          "&mdash; at a kernel cost independent of tree depth.",
    "{{SECONDARY_FIGURE}}": "assets/figures/figure6.png",
    "{{SECONDARY_CAPTION}}": "Left: averaged test accuracy over 90 datasets vs. depth. Right: kernel "
                             "computation time &mdash; the TNTK stays flat as depth grows while the MLP-NTK rises.",
    "{{KEY_RESULT_CONCLUSION}}": "The finite-ensemble kernel converges to the closed-form TNTK, training "
                                 "dynamics match kernel regression, and harder splits win more often.",

    # Headline Numbers
    "{{HERO_VAL}}": "&gt;30%",
    "{{HERO_LABEL}}": "datasets where TNTK beats the MLP-NTK",
    "{{HERO_NOTE}}": "of 90 real-world datasets",
    "{{STAT_2_VAL}}": "34.9%", "{{STAT_2_LBL}}": "peak win (&alpha;=32)",
    "{{STAT_3_VAL}}": "11.8%", "{{STAT_3_LBL}}": "RBF baseline",
    "{{STAT_4_VAL}}": "O(1)", "{{STAT_4_LBL}}": "cost vs depth",

    # Takeaway
    "{{TAKEAWAY}}": "The Tree NTK gives the first kernel theory of infinite soft-tree ensembles &mdash; "
                    "explaining global convergence, why oblivious trees lose nothing, why deep trees "
                    "degenerate, and why harder splits help.",
}
for k, v in SUBS.items():
    html = html.replace(k, v)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    print("WARNING leftover placeholders:", leftover)

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
