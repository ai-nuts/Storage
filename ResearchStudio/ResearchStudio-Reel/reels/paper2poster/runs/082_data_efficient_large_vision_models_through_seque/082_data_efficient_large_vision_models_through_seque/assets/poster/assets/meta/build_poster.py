#!/usr/bin/env python3
"""Indirect poster builder: swap whole section blocks + fill metadata tokens.
Reads poster.html from disk, never emits it through the model channel."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")


def find_section_span(doc, sec):
    m = re.search(rf'<div\b[^>]*\bdata-section="{re.escape(sec)}"', doc)
    if not m:
        return None
    start = doc.rfind("<div", 0, m.end())
    i, depth = start, 0
    while i < len(doc):
        o, c = doc.find("<div", i), doc.find("</div>", i)
        if c == -1:
            return None
        if o != -1 and o < c:
            depth += 1; i = o + 4
        else:
            depth -= 1; i = c + len("</div>")
            if depth == 0:
                return (start, i)
    return None


def replace_section(doc, sec, new_html):
    span = find_section_span(doc, sec)
    if not span:
        sys.exit(f"section not found: {sec}")
    return doc[:span[0]] + new_html.strip() + doc[span[1]:]


SECTIONS = {
"problem": '''
<div class="section" data-section="problem">
  <h2>Problem <button class="listen-btn" data-section="problem">Listen</button></h2>
  <p>Autoregressive large vision models (LVMs) generalize across tasks, but rely on <strong>colossal models (3B+ parameters)</strong> and <strong>~400B visual tokens from 1.64B images</strong> — costly to train and impractical to deploy.</p>
  <div class="p-callout-bar">Vision is long-tailed: naively mixing benchmarks lets data-rich segmentation swamp data-poor keypoint tasks, which the model then never learns.</div>
</div>''',

"motivation": '''
<div class="section grow" data-section="motivation">
  <h2>Motivation <button class="listen-btn" data-section="motivation">Listen</button></h2>
  <ul>
    <li>Vision lacks NLP's massive uniform corpora, so the <strong>one-epoch, data-abundant</strong> training recipe of LLMs cannot transfer to data-limited vision tasks.</li>
    <li>Prior LVMs chase ever-larger models and data; classical remedies — <strong>augmentation</strong> and <strong>distillation</strong> — stay unexplored for autoregressive vision.</li>
  </ul>
  <div class="p-callout-soft">Rebalance and compress instead of scaling up.</div>
  <figure><img src="assets/figures/figure2.png" alt=""><figcaption>Fig. 2 — On data-limited pose estimation, augmentation matches the gain of adding real training data (validation loss &amp; perplexity vs. tokens).</figcaption></figure>
</div>''',

"method": '''
<div class="section grow" data-section="method">
  <h2>Method <button class="listen-btn" data-section="method">Listen</button></h2>
  <div class="method-body">
    <ul>
      <li><strong>Tokenize.</strong> An off-the-shelf VQGAN encodes each image into <strong>256 discrete tokens</strong>, assembled into "visual sentences".</li>
      <li><strong>Train.</strong> A causal LLaMA transformer learns by next-token prediction; random crop/flip augmentation rebalances scarce tasks.</li>
      <li><strong>Distill.</strong> A LLaMA-1B teacher guides a compact <strong>300M / 80M</strong> student across single- and multi-task settings.</li>
    </ul>
    <div class="p-eq">$\\mathcal{L} = \\mathrm{CrossEntropy}(s_o,\\, \\hat{s}_o)$<span class="where">Next-token objective over the shifted visual sentence: input $s_i=\\{x_1,\\dots,x_L\\}$ predicts $s_o=\\{x_2,\\dots,x_L,\\varnothing\\}$.</span></div>
    <figure class="method-figure"><img src="assets/figures/figure1.png" alt="full"><figcaption>Fig. 1 — DeLVM overview: (a) autoregressive training and (b) inference over visual sentences, (c) augmentation to rebalance long-tailed tasks, and (d) distillation into a compact student.</figcaption></figure>
  </div>
</div>''',

"dataset-benchmark": '''
<div class="section" data-section="dataset-benchmark">
  <h2>Dataset / Benchmark <button class="listen-btn" data-section="dataset-benchmark">Listen</button></h2>
  <p>Three core long-tailed tasks, plus two transfer benchmarks:</p>
  <div class="p-chips">
    <span>SA-1B (seg)</span><span>COCO-Pose</span><span>Rain13K (derain)</span>
    <span class="alt">Pascal-5i</span><span class="alt">ImageNet</span>
    <span class="muted">MPII</span><span class="muted">Test2800</span><span class="muted">Laion (VQGAN)</span>
  </div>
  <div class="p-stat-strip">
    <div class="cell"><div class="v">3</div><div class="l">core tasks</div></div>
    <div class="cell"><div class="v">1&ndash;10%</div><div class="l">SA-1B used</div></div>
    <div class="cell"><div class="v">256</div><div class="l">tokens / image</div></div>
  </div>
</div>''',

"key-result": '''
<div class="section" data-section="key-result">
  <h2>Key Results <button class="listen-btn" data-section="key-result">Listen</button></h2>
  <table class="p-table">
    <tr><th>SA-1B subset</th><th>Tokens</th><th>Val loss &darr;</th><th>Perplexity &darr;</th></tr>
    <tr><td>1%</td><td>0.34B</td><td>4.83</td><td>125.6</td></tr>
    <tr class="best"><td>10%</td><td>3.43B</td><td>4.64</td><td>103.2</td></tr>
  </table>
  <div class="callout">&minus;0.19 val loss &middot; &minus;22.4 perplexity (1%&rarr;10%)</div>
  <p class="conclusion">Augmentation reproduces this scaling gain with zero new data; distillation then lifts the compact student on every task.</p>
</div>''',

"ablation-study": '''
<div class="section" data-section="ablation-study">
  <h2>Ablation Study <button class="listen-btn" data-section="ablation-study">Listen</button></h2>
  <div class="p-banner"><div class="tag">Warns</div><div>Without task shuffling the model catastrophically forgets — perplexity on earlier tasks explodes past <strong>1000</strong>.</div></div>
  <ul>
    <li><strong>Prompt background matters:</strong> black-background prompts make grayscale-threshold post-processing reliable.</li>
    <li><strong>KD scales down:</strong> distillation still improves the LLaMA-80M student on all three tasks.</li>
  </ul>
</div>''',

"takeaway": '''
<div class="section grow" data-section="takeaway">
  <h2>Takeaway <button class="listen-btn" data-section="takeaway">Listen</button></h2>
  <div class="p-callout-primary">Classical augmentation and distillation make autoregressive LVMs data- and parameter-efficient — strong multi-task performance from compact models on limited data.</div>
  <p>A tiny 80M model reaching 83% ImageNet accuracy points toward unified, deployable generalist vision models that jointly learn generation and understanding.</p>
</div>''',
}

for sec, new_html in SECTIONS.items():
    html = replace_section(html, sec, new_html)

TOKENS = {
  "{{TITLE}}": "Data-efficient Large Vision Models through Sequential Autoregression",
  "{{AUTHORS}}": ("Jianyuan Guo<sup>1</sup>, Zhiwei Hao<sup>2</sup>, Chengcheng Wang<sup>3</sup>, "
                  "Yehui Tang<sup>3</sup>, Han Wu<sup>1</sup>, Han Hu<sup>2</sup>, "
                  "Kai Han<sup>3</sup>, Chang Xu<sup>1</sup>"),
  "{{AUTHOR_LEGEND}}": ("<sup>1</sup> University of Sydney &nbsp;&nbsp; "
                        "<sup>2</sup> Beijing Institute of Technology &nbsp;&nbsp; "
                        "<sup>3</sup> Huawei Noah's Ark Lab"),
  "{{VENUE_NAME}}": "ICML",
  "{{VENUE_YEAR}}": "2024",
  "{{VENUE_TAG}}": "",
  "{{VENUE_LINK}}": "https://github.com/ggjy/DeLVM",
  "{{CONTACT}}": "",
  "{{LOGO_1}}": "assets/logos/university-of-sydney.png",
  "{{LOGO_2}}": "assets/logos/beijing-institute-of-technology.png",
  "{{LOGO_3}}": "assets/logos/huawei-noah-s-ark-lab.png",
  "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
  "{{HDR_QR_PAPER}}": "assets/qr/paper.png",
  "{{HDR_QR_CODE}}": "assets/qr/code.png",
  "{{QR_PAPER}}": "", "{{QR_CODE}}": "",
  "{{HERO_VAL}}": "83.04%",
  "{{HERO_LABEL}}": "ImageNet top-1 &middot; LLaMA-80M",
  "{{HERO_NOTE}}": "augmentation + distillation",
  "{{STAT_2_VAL}}": "80M", "{{STAT_2_LBL}}": "params (from 3B)",
  "{{STAT_3_VAL}}": "&minus;22.4", "{{STAT_3_LBL}}": "perplexity &darr;",
  "{{STAT_4_VAL}}": "256", "{{STAT_4_LBL}}": "tokens / image",
  # commented-out contribution block still carries these tokens — blank them
  "{{CONTRIBUTION_1}}": "", "{{CONTRIBUTION_2}}": "", "{{CONTRIBUTION_3}}": "",
}
for tok, val in TOKENS.items():
    html = html.replace(tok, val)

# sync PLAYLIST to sections we render that have audio clips (method/headline have none)
html = html.replace(
  '["title", "problem", "motivation", "method", "dataset-benchmark", "key-result", "ablation-study", "takeaway"]',
  '["title", "problem", "motivation", "dataset-benchmark", "key-result", "ablation-study", "takeaway"]')

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
