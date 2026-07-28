#!/usr/bin/env python3
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

def sub1(pattern, repl, s, flags=re.S):
    new, n = re.subn(pattern, lambda m: repl, s, count=1, flags=flags)
    if n != 1:
        sys.exit(f"STRUCT MISS ({n}): {pattern[:60]}")
    return new

# --- structural: Problem callout ---
html = sub1(r'<p>\{\{PROBLEM\}\}</p>',
    '<p>{{PROBLEM}}</p>\n        <div class="p-callout-bar">Sub-cell NER is <strong>nested multi-instance</strong>: many cells per table, many token labels per cell &mdash; acquire at which level?</div>',
    html)

# --- structural: Motivation figure -> banner ---
html = sub1(r'<figure><img src="\{\{TEASER_FIGURE\}\}"[^>]*><figcaption>\{\{TEASER_CAPTION\}\}</figcaption></figure>',
    '<div class="p-banner"><div class="tag">First</div><div>No prior work combines active learning with tabular language models.</div></div>',
    html)

# --- structural: Method equation between bullets and figure ---
_EQ = ('<div class="p-eq">$$f^{\\mathrm{MNLP}}_{acq}(c_{i,j})=\\tfrac{1}{t}\\sum_{z=1}^{t}'
       '\\log y^{*}_{i,j,z}\\qquad f^{\\mathrm{BADGE}}_{acq}(c_{i,j})=\\text{k-MEANS++}'
       '\\!\\Big(\\tfrac{1}{t}\\sum_z g_{i,j,z}\\Big)$$'
       '<span class="where">MNLP: uncertainty; BADGE: gradient-embedding batch diversity</span></div>')
_ANCHOR = '<figure><img src="{{METHOD_FIGURE}}" alt="half">'
if _ANCHOR not in html:
    sys.exit("STRUCT MISS: method figure anchor")
html = html.replace(_ANCHOR, _EQ + _ANCHOR, 1)

# --- structural: Dataset key-stat after bullets ---
html = sub1(r'<li>\{\{DATASET_2\}\}</li>\s*</ul>',
    '<li>{{DATASET_2}}</li>\n          </ul>\n'
    '          <div class="p-key-stat"><div class="num">~77%</div>'
    '<div class="label">of cells contain no entity (label-O only) &mdash; extreme class imbalance</div></div>',
    html)

# --- structural: Key Result table+callout -> figure2 + soft callout ---
html = sub1(
    r'<table class="results">.*?</table>\s*<div class="callout">\{\{HEADLINE_DELTA\}\}</div>\s*<p class="conclusion">\{\{KEY_RESULT_CONCLUSION\}\}</p>',
    '<figure><img src="assets/figures/figure2.png" alt="results"><figcaption>Micro-F1 at each active-learning iteration, averaged over 5 seeds.</figcaption></figure>\n          <div class="p-callout-soft">BADGE beats random and even <strong>exceeds full-training F1</strong> with far fewer labels; MNLP+ (forced max table diversity) is the worst.</div>',
    html)

# --- structural: Ablation ul -> 3-col table ---
html = sub1(
    r'<ul>\s*<li>\{\{ABLATION_1\}\}</li>\s*<li>\{\{ABLATION_2\}\}</li>\s*</ul>\s*<p class="conclusion">\{\{ABLATION_CONCLUSION\}\}</p>',
    '<table class="p-table">\n'
    '          <tr><th>Acquisition</th><th>Table diversity</th><th>Outcome</th></tr>\n'
    '          <tr><td>Rand</td><td>uniform</td><td>baseline</td></tr>\n'
    '          <tr><td>MNLP</td><td>few tables</td><td>&asymp; Rand @500</td></tr>\n'
    '          <tr><td>MNLP+</td><td>forced max</td><td>worst, &lt; Rand</td></tr>\n'
    '          <tr class="best"><td>BADGE</td><td>balanced</td><td>&gt; full-train</td></tr>\n'
    '        </table>',
    html)

# --- structural: Takeaway p -> callout-primary ---
html = sub1(r'<p>\{\{TAKEAWAY\}\}</p>',
    '<div class="p-callout-primary">{{TAKEAWAY}}</div>', html)

# --- neutralize commented-out contribution tokens ---
for t in ("{{CONTRIBUTION_1}}", "{{CONTRIBUTION_2}}", "{{CONTRIBUTION_3}}"):
    html = html.replace(t, "")

# --- structural: add a URL line to the sparse scan-contact card ---
_scan_a = '<div class="scan-contact">{{CONTACT}}</div>'
if _scan_a in html:
    html = html.replace(_scan_a,
        _scan_a + '\n      <div class="scan-contact">arxiv.org/abs/2211.04128</div>', 1)

SUBS = {
    "{{TITLE}}": "Active Learning with Tabular Language Models",
    "{{AUTHORS}}": 'Martin Ringsquandl<sup>1</sup>, Aneta Koleva<sup>1,2</sup>',
    "{{AUTHOR_LEGEND}}": '<sup>1</sup> Siemens AG &nbsp;&nbsp; <sup>2</sup> LMU Munich',
    "{{VENUE_NAME}}": "NeurIPS",
    "{{VENUE_YEAR}}": "2022",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{LOGO_1}}": "assets/logos/siemens-ag.png",
    "{{LOGO_2}}": "assets/logos/lmu-munich.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{CONTACT}}": "Email: martin.ringsquandl@siemens.com",
    "{{PROBLEM}}": "Fine-tuning tabular language models for industrial tasks needs many labels, but only scarce experts can annotate the technical tables &mdash; making labels prohibitively expensive.",
    "{{MOTIVATION_1}}": "Plentiful unlabeled tables paired with costly expert labels are a natural fit for <strong>active learning</strong>.",
    "{{MOTIVATION_2}}": "Transformers need <strong>batch</strong> acquisition; naive uncertainty sampling grabs correlated, redundant cells.",
    "{{METHOD_1}}": "<strong>Table-biased encoder:</strong> a row&ndash;column visibility matrix + within-cell positional encoding give tokens full-table context.",
    "{{METHOD_2}}": "<strong>Decoder</strong> assigns IO NER tags over four entity types: TAG, EQ, QUANT, UoM.",
    "{{METHOD_3}}": "<strong>Pool-based active learning</strong> iteratively selects batches of the most informative cells for an oracle to label.",
    "{{METHOD_FIGURE}}": "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": "Overview of the industrial sub-cell NER problem and the active-learning candidate acquisition.",
    "{{DATASET_1}}": "Real industrial spreadsheets from multiple plants, downsampled to &le;5 rows per table, expert-annotated cell-by-cell with prodi.gy.",
    "{{DATASET_2}}": "Random split &rarr; <strong>55</strong> training tables (4,774 cells, 1,112 labels) and <strong>24</strong> test tables.",
    "{{HERO_VAL}}": "0.23",
    "{{HERO_LABEL}}": "NER labels per cell",
    "{{HERO_NOTE}}": "",
    "{{STAT_2_VAL}}": "55 / 24", "{{STAT_2_LBL}}": "train / test tables",
    "{{STAT_3_VAL}}": "100 + 50", "{{STAT_3_LBL}}": "seed + per-iter cells",
    "{{STAT_4_VAL}}": "5", "{{STAT_4_LBL}}": "seeds averaged",
    "{{TAKEAWAY}}": "Cell-level acquisition with built-in batch diversity (BADGE) reaches full-training F1 with far fewer labels; forcing maximum table diversity backfires.",
}

missing = [k for k in SUBS if k not in html]
if missing:
    sys.exit(f"placeholder(s) not in template: {missing}")
for k, v in SUBS.items():
    html = html.replace(k, v)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
