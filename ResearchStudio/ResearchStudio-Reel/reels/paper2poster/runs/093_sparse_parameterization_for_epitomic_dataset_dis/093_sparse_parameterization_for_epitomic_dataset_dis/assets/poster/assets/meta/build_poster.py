#!/usr/bin/env python3
"""Fill the composed 3col poster.html for SPEED (paper 093). Disk-to-disk."""
import re
import sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# ---- block replacements (add content-pattern widgets) ----
BLOCKS = []

# Problem: <p> + callout-bar
BLOCKS.append((
    "<p>{{PROBLEM}}</p>",
    '<p>Dataset distillation compresses a large dataset into a small synthetic set '
    'that still trains high-accuracy models. But prior work pours effort into the '
    '<strong>matching objective</strong> while parameterizing each synthetic image '
    '<strong>independently</strong> &mdash; a naive scheme that ignores the heavy '
    '<strong>spatial redundancy</strong> within and across images.</p>\n'
    '        <div class="p-callout-bar">Wasted redundancy caps how much informative data '
    'fits the tiny budget &mdash; worst on high-resolution images.</div>'
))

# Motivation: ul (2) + vs   (drop teaser figure -> col1 text-only)
MOT_OLD = '''<ul>
          <li>{{MOTIVATION_1}}</li>
          <li>{{MOTIVATION_2}}</li>
        </ul>
        <!-- OPTIONAL teaser figure. If the spec's Motivation figure line is `**Figure:** none`, REMOVE this entire <figure> block. -->
        <figure><img src="{{TEASER_FIGURE}}" alt=""><figcaption>{{TEASER_CAPTION}}</figcaption></figure>'''
MOT_NEW = '''<ul>
          <li><strong>Images are redundant.</strong> Patches, textures, and structures recur within and across images &mdash; exactly what dictionary learning and sparse coding were built to exploit.</li>
          <li><strong>Spend the budget wisely.</strong> A compact shared dictionary plus sparse per-image codes packs far more informative synthetic images than one-image-per-parameter.</li>
        </ul>
        <div class="p-vs">
          <div class="side bad"><h4>Naive parameterization</h4><p>Optimize each synthetic image independently &mdash; redundancy repeated, budget wasted.</p></div>
          <div class="sep">vs.</div>
          <div class="side good"><h4>Sparse &amp; shared (SPEED)</h4><p>One epitomic-token dictionary + sparse codes, reused by every image.</p></div>
        </div>'''
BLOCKS.append((MOT_OLD, MOT_NEW))

# Method: 3-bullet ul, real equation, figure
MET_OLD = '''<ul>
          <li>{{METHOD_1}}</li>
          <li>{{METHOD_2}}</li>
        </ul>'''
MET_NEW = '''<ul>
          <li><strong>Epitomic tokens (SAETs).</strong> A shared multi-head dictionary <em>E</em> of spatial-agnostic tokens reused by every synthetic image patch.</li>
          <li><strong>Sparse coding (SCMs).</strong> Each image keeps a sparse matrix <em>A<sub>i</sub></em> selecting only its most significant tokens; an &#8467;<sub>1</sub> penalty drives sparsity, then each SCM is pruned to top-<em>k</em>.</li>
          <li><strong>FReeNet synthesis.</strong> A recurrent transformer-style network &Phi;<sub>&phi;</sub> (shared across <em>R</em> blocks) assembles the tokens into hierarchical high-resolution image patches.</li>
        </ul>'''
BLOCKS.append((MET_OLD, MET_NEW))

# Method equation (replace the KEY EQUATION comment)
MET_EQ_OLD = '''<!-- ★ KEY EQUATION (strongly preferred — most papers have one). Render the paper's core
             formula with the `equation` widget from references/content_patterns.md, e.g.
               <div class="eqn">$$ {{KEY_EQUATION}} $$<span class="eqn-note">{{KEY_EQUATION_NOTE}}</span></div>
             Integrate it HERE in Method, OR split it into its own "Formulation" .section if the
             math is central. A rendered section must never be contentless. Remove ONLY if the paper
             genuinely has no formula (pure systems / empirical). -->'''
MET_EQ_NEW = '''<div class="eqn">$$ \\tilde{X}_i = \\Phi_\\phi(E,\\, A_i) $$<span class="eqn-note">Each synthetic image is factorized into shared tokens <em>E</em> and a sparse code <em>A<sub>i</sub></em>; trained with a matching loss + &#8467;<sub>1</sub> sparsity, SCMs are stored as top-<em>k</em> in sparse uint8 &mdash; O(NHk), k&#8810;KJ.</span></div>'''
BLOCKS.append((MET_EQ_OLD, MET_EQ_NEW))

# Dataset / Benchmark: p + color-coded chips
DS_OLD = '''<ul>
          <li>{{DATASET_1}}</li>
          <li>{{DATASET_2}}</li>
        </ul>'''
DS_NEW = '''<p>Everything is compared under <strong>equal storage</strong> (parameters-per-class) at IPC 1/10/50, with a ConvNet backbone and trajectory matching by default; cross-arch eval on MLP, ResNet18, ViT.</p>
        <div class="p-chips">
          <span>CIFAR-10</span><span>CIFAR-100</span><span>TinyImageNet</span>
          <span class="alt">ImageNette</span><span class="alt">ImageWoof</span><span class="alt">ImageFruit</span><span class="alt">ImageMeow</span><span class="alt">ImageSquawk</span><span class="alt">ImageYellow</span>
          <span class="muted">CIFAR-100-C</span>
        </div>'''
BLOCKS.append((DS_OLD, DS_NEW))

# Key Results: 3-col table
KR_OLD = '''<table class="results">
          <tr><th>Method</th><th>Metric</th></tr>
          <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>
          <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>
        </table>'''
KR_NEW = '''<table class="results">
          <tr><th>IPC 1 &middot; test acc (%)</th><th>Prior SOTA</th><th>SPEED</th></tr>
          <tr><td class="method">CIFAR-100</td><td>34.0</td><td>40.0</td></tr>
          <tr><td class="method">TinyImageNet</td><td>16.0</td><td>26.9</td></tr>
        </table>'''
BLOCKS.append((KR_OLD, KR_NEW))

# Ablation: uncomment + p-table + fig4
ABL_NEW = '''<div class="section" data-section="ablation-study">
        <h2>Ablation Study <button class="listen-btn" data-section="ablation-study">Listen</button></h2>
        <table class="p-table">
          <tr><th>Feature sparsification</th><th>Params</th><th>Acc</th></tr>
          <tr><td>Full model</td><td>15M</td><td>74.0</td></tr>
          <tr class="best"><td>k = 48 (~0.3% density)</td><td>307K</td><td>73.5</td></tr>
          <tr><td>k = 12</td><td>106K</td><td>57.8</td></tr>
        </table>
        <figure><img src="assets/figures/page8_figure4.png" alt=""><figcaption>ImageSquawk synthetic samples before (left) and after (right) sparsification to 0.3% density &mdash; visually near-identical.</figcaption></figure>
        <p class="conclusion">Sparsification is nearly free at moderate <em>k</em>; too-small <em>k</em> collapses accuracy. Best: R=2 blocks, H=3 heads.</p>
      </div>'''
html = re.sub(r'<!--\s*═.*?═\s*-->', lambda m: ABL_NEW, html, flags=re.DOTALL)

# Takeaway: callout-primary + p
BLOCKS.append((
    "<p>{{TAKEAWAY}}</p>",
    '<div class="p-callout-primary">How you parameterize the synthetic dataset matters as much as the matching objective.</div>\n'
    '        <p>A shared epitomic-token dictionary with sparse per-image codes and a recurrent synthesizer removes spatial redundancy '
    '&mdash; delivering SOTA distillation at a fraction of the storage, plus better cross-architecture generalization and corruption robustness.</p>'
))

for old, new in BLOCKS:
    if old not in html:
        sys.exit(f"BLOCK anchor not found:\n{old[:80]}")
    html = html.replace(old, new, 1)

# ---- simple token substitutions ----
SUBS = {
    "{{TITLE}}": "Sparse Parameterization for Epitomic Dataset Distillation",
    "{{AUTHORS}}": "Xing Wei<sup>1</sup>, Anjia Cao<sup>1</sup>, Funing Yang<sup>1</sup>, Zhiheng Ma<sup>2</sup>",
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> School of Software Engineering, Xi'an Jiaotong University &nbsp;&nbsp; <sup>2</sup> Shenzhen Institute of Advanced Technology, CAS",
    "{{CONTACT}}": "Email: weixing@mail.xjtu.edu.cn",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{VENUE_NAME}}": "NeurIPS",
    "{{VENUE_YEAR}}": "2023",
    "{{LOGO_1}}": "assets/logos/xi-an-jiaotong-university.png",
    "{{LOGO_2}}": "assets/logos/chinese-academy-of-sciences.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "", "{{QR_CODE}}": "",
    # Key Results tail
    "{{HEADLINE_DELTA}}": "New SOTA on all 3 standard benchmarks + all 6 ImageNet subsets &mdash; averaging +11.2% at IPC 1",
    "{{SECONDARY_FIGURE}}": "assets/figures/page7_figure2_a.png",
    "{{SECONDARY_CAPTION}}": "Continual learning on ConvNet and ResNet18: SPEED (red) stays best at every step as classes accumulate.",
    "{{KEY_RESULT_CONCLUSION}}": "SPEED's IPC 1 results rival prior methods' IPC 10 using only ~10% of their parameters.",
    # Headline Numbers
    "{{HERO_VAL}}": "+11.2%",
    "{{HERO_LABEL}}": "avg gain &middot; 6 ImageNet subsets &middot; IPC 1",
    "{{HERO_NOTE}}": "new state-of-the-art",
    "{{STAT_2_VAL}}": "40.0%", "{{STAT_2_LBL}}": "CIFAR-100 IPC 1 (+6.0)",
    "{{STAT_3_VAL}}": "26.9%", "{{STAT_3_LBL}}": "TinyImageNet IPC 1 (+10.9)",
    "{{STAT_4_VAL}}": "~10%", "{{STAT_4_LBL}}": "params vs prior IPC 10",
    # Method figure
    "{{METHOD_FIGURE}}": "assets/figures/page2_figure1.png",
    "{{METHOD_CAPTION}}": "SPEED overview: sparse combinations of shared epitomic tokens feed feature-recurrent blocks that synthesize image patches for dataset matching.",
}
missing = [k for k in SUBS if k not in html]
if missing:
    sys.exit(f"token(s) not in template: {missing}")
for tok, val in SUBS.items():
    html = html.replace(tok, val)

# ---- PLAYLIST: mp3-backed sections in poster order ----
html = html.replace(
    'const PLAYLIST = ["title", "problem", "motivation", "method", "dataset-benchmark", "key-result", "takeaway"];',
    'const PLAYLIST = ["title", "problem", "motivation", "dataset-benchmark", "key-result", "ablation-study", "takeaway"];'
)

# ---- sanity: no {{...}} may survive ----
leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
