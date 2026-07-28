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
            depth -= 1; i = c + 6
            if depth == 0:
                while i < len(doc) and doc[i] in " \t\r\n": i += 1
                return doc[:start] + doc[i:]
    return doc

target = Path(sys.argv[1])
html = target.read_text(encoding="utf-8")

# ---- drop lean-omitted sections + their PLAYLIST ids ----
for sec in ["contribution", "dataset-benchmark", "ablation-study"]:
    html = drop_section(html, sec)
    html = re.sub(rf'"{re.escape(sec)}"\s*,?\s*', "", html)

# ---- whole-block section replacements (rich widgets) ----
BLOCKS = {}

BLOCKS['<p>{{PROBLEM}}</p>'] = (
    '<p>Differentially private (DP) deep learning depends on <strong>per-example gradient '
    'clipping</strong>, but the clipping threshold <strong>R</strong> is a fragile, task-specific '
    'hyperparameter whose value strongly determines final accuracy.</p>\n'
    '        <div class="p-callout-bar">On ImageNet, ResNet18 accuracy collapses from 45% to 31% '
    'when R is merely doubled.</div>'
)

BLOCKS['''<ul>
          <li>{{MOTIVATION_1}}</li>
          <li>{{MOTIVATION_2}}</li>
        </ul>
        <!-- OPTIONAL: half-column Motivation figure. If the spec's Motivation figure line is `**Figure:** none`, REMOVE this entire <figure> block. -->
        <figure><img src="{{TEASER_FIGURE}}" alt=""><figcaption>{{TEASER_CAPTION}}</figcaption></figure>'''] = (
    '<ul>\n'
    '          <li>Tuning the pair <strong>(R, learning rate)</strong> for large models costs '
    '<strong>days to months</strong> of compute.</li>\n'
    '          <li>Because it inspects private data, the search also <strong>spends extra privacy '
    'budget</strong>, making DP training far harder than standard training.</li>\n'
    '        </ul>\n'
    '        <div class="p-callout-soft">Best thresholds are so small that nearly every gradient is '
    'clipped every step, so R’s exact value stops carrying magnitude information.</div>\n'
    '        <figure><img src="assets/figures/figure1.png" alt=""><figcaption>Test accuracy over '
    'clipping norm R and learning rate: accuracy swings sharply with R, so joint (R, η) '
    'tuning is costly.</figcaption></figure>'
)

BLOCKS['''<ul>
          <li>{{METHOD_1}}</li>
          <li>{{METHOD_2}}</li>
          <li>{{METHOD_3}}</li>
        </ul>
        <figure><img src="{{METHOD_FIGURE}}" alt="half"><figcaption>{{METHOD_CAPTION}}</figcaption></figure>'''] = (
    '<ul>\n'
    '          <li><strong>AUTO-V:</strong> replace Abadi’s factor min(R/‖g‖, 1) with '
    'pure normalization R/‖g‖.</li>\n'
    '          <li><strong>AUTO-S:</strong> divide by ‖g‖ + γ (small stability '
    'constant) to keep magnitude and escape the “lazy region.”</li>\n'
    '          <li>Any constant R rescales into the learning rate, so <strong>R is fixed to '
    '1</strong> — a threshold-free optimizer.</li>\n'
    '        </ul>\n'
    '        <div class="p-eq">\n'
    '          $\\mathrm{Clip}_{\\text{AUTO-S}}(g_i)=R/(\\lVert g_i\\rVert+\\gamma)$\n'
    '          <span class="where">γ = 0.01 default; as ‖g‖→0 the clipped '
    'gradient → g/γ, enabling convergence to zero gradient norm</span>\n'
    '        </div>\n'
    '        <figure><img src="assets/figures/figure2.png" alt="half"><figcaption>Per-step '
    'dot-product similarity of the private vs. true gradient: AUTO-V magnifies alignment far above '
    'Abadi’s clipping.</figcaption></figure>'
)

BLOCKS['''<table class="results">
          <tr><th>Method</th><th>Metric</th></tr>
          <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>
          <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>
        </table>
        <div class="callout">{{HEADLINE_DELTA}}</div>
        <p class="conclusion">{{KEY_RESULT_CONCLUSION}}</p>'''] = (
    '<table class="p-table">\n'
    '          <tr><th>Task (ε)</th><th>Prior SOTA</th><th>AUTO-S (Ours)</th></tr>\n'
    '          <tr class="best"><td>GPT2 · E2E BLEU (3)</td><td>63.85</td><td>64.18</td></tr>\n'
    '          <tr><td>RoBERTa · SST-2 (3)</td><td>91.86</td><td>92.32</td></tr>\n'
    '          <tr><td>CIFAR10 · SimCLRv2 (2)</td><td>92.44</td><td>92.70</td></tr>\n'
    '        </table>\n'
    '        <div class="callout">Matches or beats tuned SOTA on every task — with no R search.</div>\n'
    '        <figure><img src="assets/figures/figure3.png" alt=""><figcaption>RoBERTa-base accuracy '
    'over R and learning rate (DP-Adam, ε=3): the AUTO-S column (red) matches the best tuned R '
    'while searching η only, cutting tuning cost ~5×.</figcaption></figure>'
)

BLOCKS['<p>{{TAKEAWAY}}</p>'] = (
    '<div class="p-callout-primary">Per-sample clipping needs no tuned threshold: normalize each '
    'gradient, add a tiny stability constant, and get a threshold-free optimizer as private, fast, '
    'and accurate as the best hand-tuned DP methods.</div>\n'
    '        <p>A one-line change in existing DP libraries (Opacus, ObJAX), backed by a convergence '
    'guarantee matching standard SGD.</p>'
)

for k, v in BLOCKS.items():
    if k not in html:
        sys.exit(f"BLOCK not found (markup drift): {k[:60]!r}")
    html = html.replace(k, v)

# ---- simple token substitutions (header / scan / headline) ----
SUBS = {
    "{{TITLE}}": "Automatic Clipping: Differentially Private Deep Learning Made Easier and Stronger",
    "{{AUTHORS}}": ("Zhiqi Bu<sup>1</sup>, Yu-Xiang Wang<sup>1,2</sup>, "
                    "Sheng Zha<sup>1</sup>, George Karypis<sup>1</sup>"),
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> AWS AI &nbsp;&nbsp; <sup>2</sup> UC Santa Barbara",
    "{{VENUE_NAME}}": "NeurIPS",
    "{{VENUE_YEAR}}": "2023",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "Email: zhiqibu@amazon.com",
    "{{LOGO_1}}": "assets/logos/aws-ai.png",
    "{{LOGO_2}}": "assets/logos/uc-santa-barbara.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",
    "{{HERO_VAL}}": "64.18",
    "{{HERO_LABEL}}": "BLEU · GPT2 on E2E · ε=3",
    "{{HERO_NOTE}}": "new SOTA, no threshold tuning",
    "{{STAT_2_VAL}}": "92.32%", "{{STAT_2_LBL}}": "SST-2 · ε=3",
    "{{STAT_3_VAL}}": "92.70%", "{{STAT_3_LBL}}": "CIFAR10 · ε=2",
    "{{STAT_4_VAL}}": "~5×", "{{STAT_4_LBL}}": "less tuning cost",
}
for k, v in SUBS.items():
    html = html.replace(k, v)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
