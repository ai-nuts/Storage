#!/usr/bin/env python3
"""Fill poster.html for the LPLR paper — disk-to-disk (template never emitted).

Layout (landscape full, header v5, scan hidden):
  col0            : Problem, Motivation(grow)
  col1 mid-wide   : Method(grow, fig1 + key equation) + mid-sub[Key Results | Ablation]
  col2            : Results/fig2 (qualitative), Headline Numbers, Takeaway(grow)
"""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")


def replace_section(doc, sec, new_html):
    m = re.search(rf'<div\b[^>]*\bdata-section="{re.escape(sec)}"', doc)
    if not m:
        sys.exit(f"section not found: {sec}")
    start = doc.rfind("<div", 0, m.end())
    i, depth = start, 0
    while i < len(doc):
        o, c = doc.find("<div", i), doc.find("</div>", i)
        if c == -1:
            sys.exit(f"malformed section: {sec}")
        if o != -1 and o < c:
            depth += 1; i = o + 4
        else:
            depth -= 1; i = c + len("</div>")
            if depth == 0:
                return doc[:start] + new_html + doc[i:]
    sys.exit(f"unbalanced: {sec}")


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


# ---- section blocks ----
PROBLEM = r'''<div class="section" data-section="problem">
        <h2>Problem <button class="listen-btn" data-section="problem">Listen</button></h2>
        <p>Modern matrices can hold <strong>billions of entries</strong>, so storing and processing them strains memory and compute — yet they are frequently <strong>approximately low rank</strong>.</p>
        <div class="p-callout-bar">Low-rank approximation or low-precision quantization <em>alone</em> each leaves compression on the table — the two structures are rarely exploited jointly, with error guarantees.</div>
      </div>'''

MOTIVATION = r'''<div class="section grow" data-section="motivation">
        <h2>Motivation <button class="listen-btn" data-section="motivation">Listen</button></h2>
        <ul>
          <li>A low-rank matrix factorizes into a tall and a wide factor with far fewer entries; storing those in <strong>low precision</strong> multiplies the savings.</li>
          <li>Done crudely at low bit budgets this degrades fast, and the exact <strong>SVD route costs O(nd&sup2;)</strong> — prohibitive at scale.</li>
          <li>Needed: a fast, <em>randomized</em> way to get low-rank <em>and</em> low-precision factors together, with small, analyzable error.</li>
          <li>Payoff: compression to <strong>~1 bit per coordinate</strong> whose error provably tracks the best rank-<em>k</em> approximation.</li>
        </ul>
        <div class="p-callout-soft">Low rank and low precision are complementary — jointly exploited, they compound.</div>
      </div>'''

METHOD = r'''<div class="section grow" data-section="method">
        <h2>Method <button class="listen-btn" data-section="method">Listen</button></h2>
        <div class="p-eq">
          $W^\star=\arg\min_{W}\,\lVert Q(AS)\,W-A\rVert_F^2,\quad L=Q(AS),\ R=Q'(W^\star)$
          <span class="where">error $\le(1+\tfrac{k}{m-k-1})\lVert A_k-A\rVert_F^2+\epsilon$</span>
        </div>
        <div class="method-body">
          <ul>
            <li><strong>Sketch.</strong> Multiply A by a Gaussian matrix S to approximate its column space, then quantize the basis: <span class="num">L = Q(AS)</span>.</li>
            <li><strong>Project.</strong> Solve the least-squares fit of A onto that basis for W&#8902;, then quantize: <span class="num">R = Q&prime;(W&#8902;)</span>.</li>
            <li><strong>Equalization.</strong> Gaussian JL embeddings keep the quantization error <span class="num">O(1)</span>, not O(d) — so LPLR holds up even at <strong>1-bit</strong> precision.</li>
          </ul>
          <figure class="method-figure"><img src="assets/figures/figure1.png" alt="full" data-fill-scale="0.95"><figcaption>Shepp-Logan at ~2 bits/pixel: LPLR / LSVD (ours) preserve detail lost by na&iuml;ve quant. and DSVD.</figcaption></figure>
        </div>
      </div>'''

# mid-sub LEFT (slot: dataset-benchmark) -> Key Results
KEY_RESULT = r'''<div class="section" data-section="key-result">
          <h2>Key Results <button class="listen-btn" data-section="key-result">Listen</button></h2>
          <table class="results">
            <tr><th>Method &middot; 1-bit</th><th>CIFAR-10 Acc</th><th>CIFAR-100 Acc</th></tr>
            <tr><td class="method">Na&iuml;ve quant.</td><td>11%</td><td>~1%</td></tr>
            <tr class="best"><td class="method">LPLR (ours)</td><td>92%</td><td>79%</td></tr>
            <tr><td class="method">Unquantized</td><td>91%</td><td>76%</td></tr>
          </table>
          <div class="callout">LPLR matches unquantized accuracy at ~1 bit/coord, exactly where na&iuml;ve quant. collapses.</div>
          <p class="conclusion">Low rank + low precision keeps the task accuracy that plain quantization destroys — on CIFAR-100 at a single bit, LPLR holds 79% where na&iuml;ve quant. falls to ~1%.</p>
        </div>'''

# mid-sub RIGHT (slot: key-result) -> Ablation
ABLATION = r'''<div class="section" data-section="ablation-study">
          <h2>Ablation Study <button class="listen-btn" data-section="ablation-study">Listen</button></h2>
          <table class="results">
            <tr><th>B<sub>nq</sub></th><th>LPLR Acc</th><th>Na&iuml;ve Acc</th></tr>
            <tr class="best"><td class="method">1 bit</td><td>79%</td><td>~1%</td></tr>
            <tr><td class="method">2 bit</td><td>80%</td><td>1.7%</td></tr>
            <tr><td class="method">4 bit</td><td>79%</td><td>75%</td></tr>
          </table>
          <p class="conclusion">Sweeping B<sub>nq</sub> at fixed compression: LPLR's edge is largest at aggressive budgets; na&iuml;ve quant. only catches up at 4 bits.</p>
        </div>'''

# mid-sub LEFT (slot: dataset-benchmark) -> secondary results figure
FIGURE2 = r'''<div class="section" data-section="qualitative-results">
          <h2>Results &middot; LLaMa-7b</h2>
          <figure class="method-figure"><img src="assets/figures/figure2.png" alt="full"><figcaption>LLaMa-7b per-layer relative Frobenius error, ordered by layer.</figcaption></figure>
          <div class="callout">Lower error, far less variance than na&iuml;ve quant.</div>
        </div>'''

HEADLINE = r'''<div class="section" data-section="headline-numbers">
        <h2>Headline Numbers</h2>
        <div class="headline-hero">
          <div class="hero-main"><div class="hero-val">~1 bit</div>
          <div class="hero-label">per matrix coordinate, task performance kept</div>
          <div class="hero-note">vs 11% accuracy for na&iuml;ve quant. on CIFAR-10</div></div>
          <div class="supporting">
            <div class="stat-mini"><div class="val">92%</div><div class="lbl">CIFAR-10 acc @ 1-bit</div></div>
            <div class="stat-mini"><div class="val">79%</div><div class="lbl">CIFAR-100 acc @ 1-bit</div></div>
            <div class="stat-mini"><div class="val">0.537</div><div class="lbl">LLaMa Frob err (LSVD)</div></div>
          </div>
        </div>
      </div>'''

TAKEAWAY = r'''<div class="section grow" data-section="takeaway">
        <h2>Takeaway <button class="listen-btn" data-section="takeaway">Listen</button></h2>
        <p>By jointly exploiting low rank and low precision, LPLR compresses matrices to <strong>~1 bit per entry</strong> with provable error bounds, matching or beating standard compression at a fraction of an SVD's cost.</p>
        <div class="p-callout-primary">Sketch &rarr; project &rarr; quantize: extreme compression with error guarantees.</div>
      </div>'''

# replacements — architecture: figure2 in the WIDE mid-sub (fills width there)
html = replace_section(html, "dataset-benchmark", FIGURE2)   # mid-sub left -> figure2
html = replace_section(html, "key-result", KEY_RESULT)        # mid-sub right -> key results
html = replace_section(html, "ablation-study", ABLATION)      # col2 top -> ablation
html = replace_section(html, "headline-numbers", HEADLINE)    # col2 mid -> headline numbers
html = replace_section(html, "takeaway", TAKEAWAY)            # col2 bottom -> takeaway (grow)
html = replace_section(html, "problem", PROBLEM)
html = replace_section(html, "motivation", MOTIVATION)
html = replace_section(html, "method", METHOD)

# ---- header / meta / scan tokens (header v5) ----
SUBS = {
    "{{TITLE}}": "Matrix Compression via Randomized Low Rank and Low Precision Factorization",
    "{{AUTHORS}}": 'Rajarshi Saha<sup>1</sup>, &nbsp;Varun Srivastava<sup>1</sup>, &nbsp;Mert Pilanci<sup>1</sup>',
    "{{AUTHOR_LEGEND}}": '<sup>1</sup> Stanford University',
    "{{CONTACT}}": "Email: rajsaha@stanford.edu",
    "{{VENUE_NAME}}": "NeurIPS",
    "{{VENUE_YEAR}}": "2023",
    "{{VENUE_TAG}}": "POSTER",
    "{{VENUE_LINK}}": "https://github.com/pilancilab/matrix-compressor",
    "{{LOGO_1}}": "assets/logos/stanford-university.png",
    "{{LOGO_2}}": "", "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{HDR_QR_PAPER}}": "assets/qr/paper.png",
    "{{HDR_QR_CODE}}": "assets/qr/code.png",
    "{{QR_PAPER}}": "", "{{QR_CODE}}": "",
    "{{URL_PROJECT}}": "",
    # only inside the commented-out Contribution block — neutralize
    "{{CONTRIBUTION_1}}": "", "{{CONTRIBUTION_2}}": "", "{{CONTRIBUTION_3}}": "",
}
for k, v in SUBS.items():
    html = html.replace(k, v)

# ---- layout tuning: narrow the figure2 sub-card so a width-filling AR-1.75
#      plot fits at lower height; give content-heavy Key Results more width.
STYLE_OVERRIDE = (
    '<style id="poster-tuning">\n'
    '  .mid-sub { grid-template-columns: 0.66fr 1.34fr; }\n'
    '  .section > *:last-child { margin-bottom: 14pt; }\n'
    '</style>\n'
)
html = html.replace('<div class="columns">', STYLE_OVERRIDE + '<div class="columns">', 1)

# ---- PLAYLIST: rendered sections that have narration audio ----
html = html.replace(
    '["title", "problem", "motivation", "method", "dataset-benchmark", "key-result", "ablation-study", "takeaway"]',
    '["title", "problem", "motivation", "method", "key-result", "ablation-study", "takeaway"]',
)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
