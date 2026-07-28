#!/usr/bin/env python3
"""Build IGP poster — disk-to-disk, fills titlebar + rewrites section bodies with widgets."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# ---------- 1. titlebar / metadata tokens ----------
TOK = {
    "{{TITLE}}": "Information Gain Propagation: A New Way to Graph Active Learning with Soft Labels",
    "{{AUTHORS}}": ("Wentao Zhang<sup>1</sup>, Yexin Wang<sup>1</sup>, Zhenbang You<sup>1</sup>, "
                    "Meng Cao<sup>2</sup>, Ping Huang<sup>2</sup>, Jiulong Shan<sup>2</sup>, "
                    "Zhi Yang<sup>1,3</sup>, Bin Cui<sup>1,3,4</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> Peking University &nbsp;&nbsp; <sup>2</sup> Apple &nbsp;&nbsp; "
                          "<sup>3</sup> Nat'l Eng. Lab for Big Data &nbsp;&nbsp; <sup>4</sup> Inst. Computational Social Science, PKU"),
    "{{CONTACT}}": "",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{VENUE_NAME}}": "ICLR",
    "{{VENUE_YEAR}}": "2022",
    "{{LOGO_1}}": "assets/logos/peking-university.png",
    "{{LOGO_2}}": "assets/logos/apple.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    # 3col suppresses scan-to-read → no QR
    "{{QR_PAPER}}": "", "{{QR_CODE}}": "", "{{URL_PAPER}}": "",
}
for k, v in TOK.items():
    html = html.replace(k, v)

# ---------- 2. section body rewrites (block replacement) ----------
def replace_block(html, anchor, new_inner):
    """Replace inner HTML of a data-section block's content region."""
    if anchor not in html:
        sys.exit(f"anchor not found: {anchor[:60]}")
    return html.replace(anchor, new_inner)

# --- Problem ---
html = replace_block(html,
    '        <h2>Problem <button class="listen-btn" data-section="problem">Listen</button></h2>\n        <p>{{PROBLEM}}</p>',
    '''        <h2>Problem <button class="listen-btn" data-section="problem">Listen</button></h2>
        <p>GNNs need many labeled nodes, yet every prior graph <strong>active-learning</strong> method assumes an oracle can name the <strong>exact class</strong> of each selected node.</p>
        <div class="p-callout-bar">Exact multi-class labeling is costly, especially when categories are many or out-of-domain (e.g. ogbn-papers100M has 172 classes) — the budget is spent inefficiently.</div>''')

# --- Motivation ---
html = replace_block(html,
    '''        <h2>Motivation <button class="listen-btn" data-section="motivation">Listen</button></h2>
        <ul>
          <li>{{MOTIVATION_1}}</li>
          <li>{{MOTIVATION_2}}</li>
        </ul>
        <!-- OPTIONAL teaser figure. If the spec's Motivation figure line is `**Figure:** none`, REMOVE this entire <figure> block. -->
        <figure><img src="{{TEASER_FIGURE}}" alt=""><figcaption>{{TEASER_CAPTION}}</figcaption></figure>''',
    '''        <h2>Motivation <button class="listen-btn" data-section="motivation">Listen</button></h2>
        <ul>
          <li><strong>Confirming a guess is cheap.</strong> A binary yes/no query costs far less per node than naming the exact class, especially with many categories.</li>
          <li><strong>Labels propagate.</strong> In a GNN, one labeled node influences its k-hop neighbors — yet prior criteria score only single-node uncertainty.</li>
        </ul>
        <div class="p-vs">
          <div class="side bad"><h4>Prior AL query</h4><p>"Which exact category?" — a hard multi-class question, ~c&minus;1&times; the cost.</p></div>
          <div class="sep">vs.</div>
          <div class="side good"><h4>Our relaxed query</h4><p>"Is the predicted label correct?" — one binary yes/no &rarr; a soft label.</p></div>
        </div>
        <figure><img src="assets/figures/figure1.png" alt=""><figcaption>Figure 1: A relaxed binary query yields a soft label, versus the exact-class query of prior work.</figcaption></figure>''')

# --- Method ---
html = replace_block(html,
    '''        <h2>Method <button class="listen-btn" data-section="method">Listen</button></h2>
        <ul>
          <li>{{METHOD_1}}</li>
          <li>{{METHOD_2}}</li>
        </ul>''',
    '''        <h2>Method <button class="listen-btn" data-section="method">Listen</button></h2>
        <div class="p-steps">
          <div class="step"><strong>Train</strong> a GNN on the currently labeled nodes with their <strong>soft labels</strong>.</div>
          <div class="step"><strong>Score</strong> each node's <strong>influence magnitude</strong> on its k-hop neighbors via graph propagation.</div>
          <div class="step"><strong>Select</strong> the budget-limited set maximizing <strong>information gain propagation</strong> (IGP).</div>
          <div class="step"><strong>Relabel</strong> via a binary query &rarr; normalized soft label, then update &amp; repeat.</div>
        </div>
        <div class="eqn">$$\\max_{V_l} F(V_l)=\\sum_{v_i\\in V_l}\\sum_{v_j\\in RF(v_i)} IGP(v_j,v_i,k),\\;\\; |V_l|=B$$<span class="eqn-note">Select nodes whose expected information gain propagates farthest across each receptive field RF, within labeling budget B.</span></div>''')

html = replace_block(html,
    '        <figure><img src="{{METHOD_FIGURE}}" alt="half"><figcaption>{{METHOD_CAPTION}}</figcaption></figure>',
    '        <figure><img src="assets/figures/figure3.png" alt="half"><figcaption>Figure 3: The IGP framework — train on soft labels, select by propagated information gain, relabel via relaxed queries.</figcaption></figure>')

# --- Dataset / Benchmark ---
html = replace_block(html,
    '''        <h2>Dataset / Benchmark <button class="listen-btn" data-section="dataset-benchmark">Listen</button></h2>
        <ul>
          <li>{{DATASET_1}}</li>
          <li>{{DATASET_2}}</li>
        </ul>''',
    '''        <h2>Dataset / Benchmark <button class="listen-btn" data-section="dataset-benchmark">Listen</button></h2>
        <ul>
          <li><strong>Cost-based budget.</strong> The budget is true annotation <em>cost</em>, not label count — an exact query costs ~c&minus;1&times; a relaxed one.</li>
          <li>Budgets swept from <strong>2C to 20C</strong> labels (C = #classes) across five standard graph benchmarks.</li>
        </ul>
        <div class="p-chips">
          <span>Cora</span><span>Citeseer</span><span>PubMed</span>
          <span class="alt">Reddit</span><span class="alt">ogbn-arxiv</span>
        </div>''')

# --- Key Results: replace 2-col table with 4-col highlight-table ---
html = replace_block(html,
    '''        <table class="results">
          <tr><th>Method</th><th>Metric</th></tr>
          <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>
          <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>
        </table>
        <div class="callout">{{HEADLINE_DELTA}}</div>
        <!-- ★ SECONDARY figure slot (figure-rich): a Key Result plot / qualitative samples / ablation
             chart — the second of ≥3 figure slots in this layout. REMOVE the <figure> if no secondary
             figure carries real signal. -->
        <figure><img src="{{SECONDARY_FIGURE}}" alt=""><figcaption>{{SECONDARY_CAPTION}}</figcaption></figure>
        <p class="conclusion">{{KEY_RESULT_CONCLUSION}}</p>''',
    '''        <table class="p-table">
          <tr><th>Method</th><th>Cora</th><th>Citeseer</th><th>PubMed</th></tr>
          <tr><td>Random</td><td>78.8</td><td>70.8</td><td>78.9</td></tr>
          <tr><td>GRAIN</td><td>84.2</td><td>74.2</td><td>81.8</td></tr>
          <tr class="best"><td>IGP (ours)</td><td>86.4</td><td>75.8</td><td>83.6</td></tr>
        </table>
        <div class="callout">+1.6&ndash;2.2 pts over the best baseline (GRAIN) on all three citation networks, at equal labeling budget.</div>
        <figure><img src="assets/figures/figure4.png" alt=""><figcaption>Figure 4: Test accuracy vs labeling budget on Cora — IGP (pink) leads at every budget.</figcaption></figure>
        <p class="conclusion">IGP wins across every dataset and every budget, and its accuracy climbs fastest as the budget grows.</p>''')

# --- Headline Numbers ---
for k, v in {
    "{{HERO_VAL}}": "86.4%",
    "{{HERO_LABEL}}": "Test accuracy · Cora · 20 labels/class",
    "{{HERO_NOTE}}": "+2.2 pts over the best baseline",
    "{{STAT_2_VAL}}": "+2.2", "{{STAT_2_LBL}}": "pts vs GRAIN (Cora)",
    "{{STAT_3_VAL}}": "5", "{{STAT_3_LBL}}": "datasets, all SOTA",
    "{{STAT_4_VAL}}": "4", "{{STAT_4_LBL}}": "GNN backbones win",
}.items():
    html = html.replace(k, v)

# --- Takeaway ---
html = replace_block(html,
    '''        <h2>Takeaway <button class="listen-btn" data-section="takeaway">Listen</button></h2>
        <p>{{TAKEAWAY}}</p>''',
    '''        <h2>Takeaway <button class="listen-btn" data-section="takeaway">Listen</button></h2>
        <div class="p-callout-primary">Ask a cheap yes/no question and pick nodes whose information gain propagates farthest — graph active learning gets more accurate <em>and</em> far cheaper to label.</div>''')

# ---------- 3. PLAYLIST (drop headline-numbers not present; keep dataset-benchmark) ----------
# current PLAYLIST already: title, problem, motivation, method, dataset-benchmark, key-result, takeaway — good.

# ---------- 3b. blank placeholders that live only inside HTML comments (ablation block, key-eqn hint) ----------
for k in ("{{ABLATION_1}}", "{{ABLATION_2}}", "{{ABLATION_CONCLUSION}}",
          "{{KEY_EQUATION}}", "{{KEY_EQUATION_NOTE}}"):
    html = html.replace(k, "")

# ---------- 4. leftover check ----------
leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
