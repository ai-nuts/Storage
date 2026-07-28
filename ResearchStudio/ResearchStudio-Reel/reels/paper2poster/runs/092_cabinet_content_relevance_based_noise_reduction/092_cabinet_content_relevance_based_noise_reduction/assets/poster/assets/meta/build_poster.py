#!/usr/bin/env python3
"""Disk-to-disk 3col poster build for CABINET.
Authors the three columns explicitly (balanced 3-figure distribution) and fills
the header tokens. Never emits the full template through the model output channel."""
import re
import sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# ---- author the three columns (real content, content-pattern widgets) ----
COLUMNS = '''<div class="columns">

    <!-- Column 1: Problem (grow), Motivation, Dataset/Benchmark. -->
    <div class="col">
      <div class="section" data-section="problem">
        <h2>Problem <button class="listen-btn" data-section="problem">Listen</button></h2>
        <p>In table question answering, only a handful of cells hold the answer to a given question; the rest act as <strong>noise</strong>. LLMs are highly susceptible to this irrelevant content and give sub-optimal answers, and the problem <strong>worsens as tables grow larger</strong>.</p>
        <div class="p-callout-bar">Most of a table is irrelevant to any one question, yet the LLM reads all of it, and gets distracted.</div>
      </div>
      <div class="section" data-section="motivation">
        <h2>Motivation <button class="listen-btn" data-section="motivation">Listen</button></h2>
        <p>A natural fix is to shrink the table first, but hard decomposition is unforgiving: pick the wrong sub-table and useful cells are lost for good.</p>
        <div class="p-vs">
          <div class="side bad"><h4>DATER: hard decompose</h4><p>Extracts a sub-table; a wrong pick discards useful cells and locks in the error.</p></div>
          <div class="sep">vs.</div>
          <div class="side good"><h4>CABINET: soft weight</h4><p>Weighs relevant cells higher, removes nothing, keeps the whole table.</p></div>
        </div>
        <div class="p-callout-soft">Soft weighting de-emphasises noise while keeping every cell available.</div>
      </div>
      <div class="section grow" data-section="dataset-benchmark">
        <h2>Dataset / Benchmark <button class="listen-btn" data-section="dataset-benchmark">Listen</button></h2>
        <p>Evaluated on three challenging table-QA benchmarks; WikiTQ is among the most complex, requiring compositional multi-step reasoning over tables.</p>
        <div class="p-chips">
          <span>WikiTQ</span><span>FeTaQA</span><span>WikiSQL</span>
          <span class="alt">~300 parsing statements &middot; released</span>
        </div>
        <div class="p-banner"><div class="tag">Metrics</div><div>WikiTQ &amp; WikiSQL scored by exact-match accuracy; FeTaQA by Sacre-BLEU for long, free-form answers.</div></div>
        <div class="p-callout-soft">The ~300 released parsing statements bootstrap the weakly-supervised cell highlighter.</div>
      </div>
    </div>

    <!-- Column 2 (centerpiece): Method (+fig2 + key equation, grow), Ablation. -->
    <div class="col">
      <div class="section grow" data-section="method">
        <h2>Method <button class="listen-btn" data-section="method">Listen</button></h2>
        <ul>
          <li><strong>Linearize &amp; embed</strong> the table together with the question through the QA LLM's shared embedding.</li>
          <li><strong>Unsupervised Relevance Scorer</strong> (transformer encoder, variational inference with clustering + separation + sparsification losses) scores every table token.</li>
          <li><strong>Parsing-statement module</strong> (Flan-T5-XL, ~300 annotations) highlights relevant cells; the two scores are fused and multiply token embeddings before decoding.</li>
        </ul>
        <div class="p-eq">$\\mathcal{L} = \\mathcal{L}_{CE} + \\lambda_{clu}\\mathcal{L}_{clu} + \\lambda_{sep}\\mathcal{L}_{sep} + \\lambda_{sparse}\\mathcal{L}_{sparse}$<span class="where">fused weight $\\eta_p = \\lambda_{uns}\\,\\eta_p^{uns} + \\lambda_{cell}\\,\\eta_p^{cell}$ softly scales each token &mdash; nothing is deleted</span></div>
        <figure><img src="assets/figures/figure2.png" alt="half"><figcaption>CABINET architecture: the unsupervised relevance score and the parsing-statement cell score are fused (steps 6&ndash;7) to weigh the table content passed to the QA LLM.</figcaption></figure>
      </div>
      <div class="section" data-section="ablation-study">
        <h2>Ablation Study <button class="listen-btn" data-section="ablation-study">Listen</button></h2>
        <ul>
          <li><strong>URS losses work only together:</strong> clustering + centroid-separation + sparsification lift WikiTQ 60.8 &rarr; 65.6; any subset barely helps.</li>
          <li><strong>Fuse both signals:</strong> &lambda;<sub>uns</sub>=0.7, &lambda;<sub>cell</sub>=0.3 gives 69.1; the cell-based signal alone collapses to 37.6.</li>
        </ul>
        <div class="p-callout-soft">The unsupervised scorer is the primary driver, and the weakly-supervised parsing-statement module is a complementary aid.</div>
      </div>
    </div>

    <!-- Column 3: Key Results (+fig3 robustness, grow), Headline Numbers, Takeaway. -->
    <div class="col">
      <div class="section grow" data-section="key-result">
        <h2>Key Results <button class="listen-btn" data-section="key-result">Listen</button></h2>
        <table class="p-table">
          <tr><th>Method (WikiTQ)</th><th>Acc.</th><th>&Delta;</th></tr>
          <tr><td>OmniTab</td><td>62.7</td><td>&minus;6.4</td></tr>
          <tr><td>DATER (GPT-3, in-context)</td><td>65.9</td><td>&minus;3.2</td></tr>
          <tr class="best"><td>CABINET (Ours)</td><td>69.1</td><td>&mdash;</td></tr>
        </table>
        <figure><img src="assets/figures/figure3.png" alt=""><figcaption>Performance drop under table perturbations: CABINET (green) is far more robust to noise than OmniTab (red).</figcaption></figure>
      </div>
      <div class="section" data-section="headline-numbers">
        <h2>Headline Numbers</h2>
        <div class="headline-hero">
          <div class="hero-main"><div class="hero-val">69.1%</div>
          <div class="hero-label">WikiTQ accuracy · new SoTA</div>
          <div class="hero-note">+6.4% over OmniTab</div></div>
          <div class="supporting">
            <div class="stat-mini"><div class="val">40.5</div><div class="lbl">FeTaQA Sacre-BLEU</div></div>
            <div class="stat-mini"><div class="val">89.5%</div><div class="lbl">WikiSQL accuracy</div></div>
            <div class="stat-mini"><div class="val">560M</div><div class="lbl">model parameters</div></div>
          </div>
        </div>
      </div>
      <div class="section" data-section="takeaway">
        <h2>Takeaway <button class="listen-btn" data-section="takeaway">Listen</button></h2>
        <p>Softly weighting table content by learned relevance, instead of hard-decomposing the table, lets an LLM focus on the cells that matter while keeping full access to the data.</p>
        <div class="p-callout-primary">Don't cut the table down &mdash; weight it. Soft relevance sets new state of the art on three table-QA benchmarks with a compact 560M model.</div>
      </div>
    </div>

  </div>'''

# replace the template's <div class="columns"> ... </div> (balanced) with ours
_i = html.find('<div class="columns">')
assert _i != -1, "columns wrapper not found"
j, depth = _i, 0
while j < len(html):
    o, c = html.find("<div", j), html.find("</div>", j)
    if c == -1:
        raise SystemExit("unbalanced columns div")
    if o != -1 and o < c:
        depth += 1; j = o + 4
    else:
        depth -= 1; j = c + 6
        if depth == 0:
            break
html = html[:_i] + COLUMNS + html[j:]

# ---- header / meta tokens (outside .columns) ----
SUBS = {
    "{{TITLE}}": "CABINET: Content Relevance-Based Noise Reduction for Table Question Answering",
    "{{AUTHORS}}": ("Sohan Patnaik<sup>1,2</sup>, Heril Changwal<sup>1,3</sup>, "
                    "Milan Aggarwal<sup>1</sup>, Sumit Bhatia<sup>1</sup>, "
                    "Yaman Kumar Singla<sup>1</sup>, Balaji Krishnamurthy<sup>1</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> MDSR Lab, Adobe &nbsp;&nbsp; "
                          "<sup>2</sup> IIT Kharagpur &nbsp;&nbsp; <sup>3</sup> IIT Roorkee"),
    "{{CONTACT}}": "",
    "{{VENUE_NAME}}": "ICLR",
    "{{VENUE_YEAR}}": "2024",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{LOGO_1}}": "assets/logos/adobe.png",
    "{{LOGO_2}}": "assets/logos/iit-kharagpur.png",
    "{{LOGO_3}}": "assets/logos/iit-roorkee.png",
    "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
}
missing = [k for k in SUBS if k not in html]
if missing:
    sys.exit(f"tokens not in template: {missing}")
for k, v in SUBS.items():
    html = html.replace(k, v)

# ---- PLAYLIST (drop scan; robustness folded into key-result) ----
html = re.sub(r'PLAYLIST = \[[^\]]*\]',
              'PLAYLIST = ["title", "problem", "motivation", "dataset-benchmark", "method", "ablation-study", "key-result", "takeaway"]',
              html)

# ---- remove any leftover standalone Scan-to-Read section div (3col: no QR) ----
_i = html.find('data-section="scan-to-read">')
if _i != -1:
    _start = html.rfind('<div class="section"', 0, _i)
    j, depth = _start, 0
    while j < len(html):
        o, c = html.find("<div", j), html.find("</div>", j)
        if c == -1:
            break
        if o != -1 and o < c:
            depth += 1; j = o + 4
        else:
            depth -= 1; j = c + 6
            if depth == 0:
                html = html[:_start] + html[j:]; break

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
