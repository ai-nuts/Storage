#!/usr/bin/env python3
import re, sys
from pathlib import Path

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
            depth -= 1; i = c + len("</div>")
            if depth == 0:
                while i < len(doc) and doc[i] in " \t\r\n":
                    i += 1
                return doc[:start] + doc[i:]
    return doc

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# --- lean render: drop Contribution (redundant with Method/Key-result; crushes col0). ---
html = drop_section(html, "contribution")
html = re.sub(r'"contribution"\s*,?\s*', "", html)  # remove from PLAYLIST
# col0 bottom is now Motivation -> keep its grow (template already has it). Nothing to do.

# --- Motivation: swap the unused teaser <figure> for a vs widget. ---
html = re.sub(
    r'<figure><img src="\{\{TEASER_FIGURE\}\}"[^>]*>.*?</figure>',
    '<div class="p-vs">\n'
    '  <div class="side bad"><h4>Binary (prior work)</h4><p>Optimal robust loss known &mdash; but only two classes.</p></div>\n'
    '  <div class="sep">vs.</div>\n'
    '  <div class="side good"><h4>Multi-class (ours)</h4><p>Higher-order conflicts; the optimum was uncharacterized.</p></div>\n'
    '</div>',
    html, flags=re.S)

# --- Method: insert the key-equation widget between the bullets and Fig 1. ---
html = html.replace(
    '<figure><img src="{{METHOD_FIGURE}}" alt="half">',
    '<div class="p-eq">\n'
    r'$$1 - L^{*}(P,N,\mathcal{H}) \;=\; \max_{q\ge 0}\; p^{\top}q \quad\text{s.t.}\quad Bq \le 1$$'
    '\n  <span class="where">LP form: maximize correctly-classified mass p&middot;q under the hyperedge-incidence constraints B</span>\n'
    '</div>\n'
    '        <figure><img src="{{METHOD_FIGURE}}" alt="half">')

# --- Dataset: chips + one prose line. ---
html = re.sub(
    r'<ul>\s*<li>\{\{DATASET_1\}\}</li>\s*<li>\{\{DATASET_2\}\}</li>\s*</ul>',
    '<div class="p-chips">\n'
    '  <span>MNIST</span><span>CIFAR-10</span>\n'
    '  <span class="alt">3-class</span><span class="alt">Full 10-class</span>\n'
    '  <span class="muted">L2 attacker</span><span class="muted">TRADES / APGD-CE</span>\n'
    '</div>\n'
    '        <p>3-class studies use 1000 samples/class (MNIST digits 1&middot;4&middot;7; CIFAR-10 plane&middot;bird&middot;ship). Baselines: TRADES adversarial training (3-layer CNN / WRN-28-10) evaluated with strong APGD-CE.</p>',
    html, flags=re.S)

# --- Key Results: Fig 2 + gap table + callout + Fig 3 + conclusion (both result figures here). ---
html = re.sub(
    r'<table class="results">.*?</table>',
    '<figure><img src="assets/figures/page8_figure2.png" alt=""><figcaption>Fig 2 &middot; Optimal error L*(3) for 3-class MNIST &amp; CIFAR-10 vs adversarially trained (AT) models across attack budget &epsilon;.</figcaption></figure>\n'
    '        <table class="p-table">\n'
    '          <tr><th>Best robust model</th><th>0-1 loss</th><th>Optimal L*</th></tr>\n'
    '          <tr><td>MNIST cert &middot; &epsilon;=2.0</td><td>0.44</td><td>&asymp;0</td></tr>\n'
    '          <tr class="best"><td>CIFAR-10 cert &middot; &epsilon;=2.0</td><td>0.80</td><td>&asymp;0</td></tr>\n'
    '        </table>\n'
    '        <div class="callout">{{HEADLINE_DELTA}}</div>\n'
    '        <figure><img src="assets/figures/page9_figure3.png" alt=""><figcaption>Fig 3 &middot; Lower bounds L*(2/3/4) and coupling L*<sub>CO</sub>(2) vs the Caro-Wei upper bound L<sub>CW</sub> tightly localize the true 10-class optimum (grey band).</figcaption></figure>',
    html, flags=re.S)
# remove the now-duplicate standalone callout line left by the template (keep our inline one)
html = html.replace('<div class="callout">{{HEADLINE_DELTA}}</div>\n        <p class="conclusion">{{KEY_RESULT_CONCLUSION}}</p>',
                    '<p class="conclusion">{{KEY_RESULT_CONCLUSION}}</p>')

# --- Ablation: text-only (2 bullets + soft callout + conclusion); no wide figure here. ---
html = html.replace(
    '<p class="conclusion">{{ABLATION_CONCLUSION}}</p>',
    '<div class="p-callout-soft">Edge-only bounds are both cheap and accurate in the practical regime.</div>\n'
    '        <p class="conclusion">{{ABLATION_CONCLUSION}}</p>')

# --- Unwrap Problem / Takeaway so their values carry prose + widget cleanly. ---
html = html.replace('<p>{{PROBLEM}}</p>', '{{PROBLEM}}')
html = html.replace('<p>{{TAKEAWAY}}</p>', '{{TAKEAWAY}}')

SUBS = {
    "{{TITLE}}": "Characterizing the Optimal 0-1 Loss for Multi-class Classification with a Test-time Attacker",
    "{{AUTHORS}}": ("Sihui Dai<sup>1</sup>, Wenxin Ding<sup>2</sup>, Arjun Nitin Bhagoji<sup>2</sup>, "
                    "Daniel Cullina<sup>3</sup>, Ben Y. Zhao<sup>2</sup>, Haitao Zheng<sup>2</sup>, Prateek Mittal<sup>1</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> Princeton University &nbsp;&nbsp; <sup>2</sup> University of Chicago "
                          "&nbsp;&nbsp; <sup>3</sup> Pennsylvania State University"),
    "{{CONTACT}}": "Email: cullina@psu.edu",
    "{{VENUE_NAME}}": "NeurIPS",
    "{{VENUE_YEAR}}": "2023",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{LOGO_1}}": "assets/logos/princeton-university.png",
    "{{LOGO_2}}": "assets/logos/university-of-chicago.png",
    "{{LOGO_3}}": "assets/logos/pennsylvania-state-university.png",
    "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",

    "{{PROBLEM}}": ("<p>No method existed to compute the <strong>lowest achievable 0-1 loss</strong> under a "
                    "test-time (adversarial) attacker for <strong>multi-class</strong> classification &mdash; prior "
                    "optimal-loss results covered only the <strong>binary</strong> case.</p>\n"
                    '        <div class="p-callout-bar">Without an absolute optimum, one cannot tell whether a robust '
                    "model is near-optimal or how much headroom remains &mdash; keeping defenses stuck in an arms race.</div>"),

    "{{MOTIVATION_1}}": ("A dataset- and attacker-specific lower bound makes robustness an <strong>absolute</strong> "
                         "measure &mdash; progress against the true optimum, not just against other defenses."),
    "{{MOTIVATION_2}}": ("With three or more classes, examples interact in <strong>higher-order</strong> ways that "
                         "binary analysis cannot capture, changing what optimal robustness looks like."),

    "{{METHOD_1}}": ("Build a <strong>conflict hypergraph</strong>: vertices are data points; a hyperedge links "
                     "same-neighborhood examples of <em>different</em> classes that an attacker can collapse."),
    "{{METHOD_2}}": ("The optimal robust loss is a <strong>linear program</strong> over achievable "
                     "correct-classification probabilities; its <strong>dual</strong> is a fractional vertex cover "
                     "that yields the adversary&rsquo;s optimal strategy."),
    "{{METHOD_3}}": ("To scale, <strong>truncate</strong> the hypergraph to degree m for lower bounds L*(m), "
                     "aggregate binary bounds L*<sub>CO</sub>(2), and bound above via <strong>Caro-Wei</strong>."),
    "{{METHOD_FIGURE}}": "assets/figures/page4_figure1.png",
    "{{METHOD_CAPTION}}": ("Fig 1 &middot; Two conflict structures over three examples of different classes; the "
                           "size-three hyperedge (right) changes the optimal loss only when all example probabilities "
                           "are near-balanced."),

    "{{HEADLINE_DELTA}}": "TRADES plateaus near 0.6 loss on 3-class CIFAR-10 where the optimal loss is &asymp; 0.",
    "{{KEY_RESULT_CONCLUSION}}": "The gap to optimal is large even at small &epsilon; &mdash; and far wider than in the binary case.",

    "{{ABLATION_1}}": ("Adding higher-degree hyperedges barely moves the bound: <strong>L*(2), L*(3), L*(4) nearly "
                       "coincide</strong> until the loss exceeds ~0.4."),
    "{{ABLATION_2}}": ("For CIFAR-10 at &epsilon;=3, ~3M degree-3 and ~10M degree-4 hyperedges leave the computed "
                       "bound <strong>unchanged</strong>."),
    "{{ABLATION_CONCLUSION}}": "So in the practical low-&epsilon; regime, cheap edge-only bounds pin the optimum tightly.",

    "{{HERO_VAL}}": "0.60",
    "{{HERO_LABEL}}": "AT loss &middot; 3-class CIFAR-10",
    "{{HERO_NOTE}}": "while optimal L* &asymp; 0",
    "{{STAT_2_VAL}}": "0.44", "{{STAT_2_LBL}}": "MNIST cert &middot; &epsilon;=2.0",
    "{{STAT_3_VAL}}": "0.80", "{{STAT_3_LBL}}": "CIFAR cert &middot; &epsilon;=2.0",
    "{{STAT_4_VAL}}": "13M",  "{{STAT_4_LBL}}": "hyperedges, no effect",

    "{{TAKEAWAY}}": ("<p>Multi-class robust classification has a <strong>large, now-measurable gap</strong> between "
                     "current defenses and the optimum &mdash; far worse than the binary case.</p>\n"
                     '        <div class="p-callout-primary">Edge-only conflict-hypergraph bounds pin down the optimum '
                     "efficiently in the practical low-&epsilon; regime &mdash; a fast diagnostic for how much "
                     "robustness headroom remains.</div>"),
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
