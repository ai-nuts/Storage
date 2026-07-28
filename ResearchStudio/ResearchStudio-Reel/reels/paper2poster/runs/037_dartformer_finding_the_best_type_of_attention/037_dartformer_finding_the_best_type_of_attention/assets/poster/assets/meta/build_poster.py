#!/usr/bin/env python3
"""Fill DARTFormer poster.html — disk-to-disk, template never emitted through model output."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# --- remove the commented-out CONTRIBUTION block (carries {{CONTRIBUTION_*}} tokens) ---
html = re.sub(r'<!--\s*═+\s*\n\s*CONTRIBUTION SECTION.*?═+\s*-->', '', html, flags=re.DOTALL)

# ---- structural block replacements ----
BLOCKS = []

# Motivation: bullets + remove teaser figure + callout-primary
BLOCKS.append(("""        <ul>
          <li>{{MOTIVATION_1}}</li>
          <li>{{MOTIVATION_2}}</li>
        </ul>
        <!-- OPTIONAL: half-column Motivation figure. If the spec's Motivation figure line is `**Figure:** none`, REMOVE this entire <figure> block. -->
        <figure><img src="{{TEASER_FIGURE}}" alt=""><figcaption>{{TEASER_CAPTION}}</figcaption></figure>""",
"""        <ul>
          <li>Attention heads are widely believed to learn <strong>different relational biases</strong> — so a <em>mixture</em> of attention types might beat any single one.</li>
          <li>Brute-force training of every attention (and every combination) is prohibitively expensive, motivating a cheap <strong>search-based</strong> selection.</li>
        </ul>
        <div class="p-callout-primary">Is the optimal attention for a task actually a mixture of different attentions? DARTFormer tests the intuition directly.</div>"""))

# Method: bullets + figure + equation
BLOCKS.append(("""          <ul>
            <li>{{METHOD_1}}</li>
            <li>{{METHOD_2}}</li>
            <li>{{METHOD_3}}</li>
          </ul>
          <figure class="method-figure"><img src="{{METHOD_FIGURE}}" alt="full"><figcaption>{{METHOD_CAPTION}}</figcaption></figure>
        </div>
      </div>""",
"""          <ul>
            <li>Build a single-layer <strong>supernetwork</strong> holding one candidate block per efficient attention type, trained to convergence.</li>
            <li><strong>Fixed-&alpha; DARTS</strong>: simply average the candidate block outputs — no learnable softmax edges, no bi-level optimization.</li>
            <li>Score each attention by its <strong>masked validation accuracy drop</strong>; keep the top block (homogeneous) or stack the best (heterogeneous).</li>
          </ul>
          <figure class="method-figure"><img src="assets/figures/page2_figure1.png" alt="full"><figcaption>Figure 1: The searched supernetwork (left) and an example derived architecture (right) — heterogeneous across heads, homogeneous across layers; block outputs are averaged.</figcaption></figure>
        </div>
        <div class="p-eq">
          $\\bar{o} = \\frac{1}{N}\\sum_{i=1}^{N} o_i$ &nbsp;&nbsp;&middot;&nbsp;&nbsp; $s_j = \\mathrm{Acc}_{\\mathrm{val}} - \\mathrm{Acc}_{\\mathrm{val}}^{(-j)}$
          <span class="where">Fixed-&alpha; averages the $N$ block outputs; block score $s_j$ = validation-accuracy drop when block $j$ is masked out.</span>
        </div>
      </div>"""))

# Dataset / Benchmark: bullets + stat-strip
BLOCKS.append(("""          <ul>
            <li>{{DATASET_1}}</li>
            <li>{{DATASET_2}}</li>
          </ul>""",
"""          <ul>
            <li>Three <strong>Long Range Arena</strong> tasks: byte-level IMDb text classification, ListOps 10-way, and byte-level document matching.</li>
            <li>Nine candidate attentions searched; each homogeneous model trained 3&times; and averaged, hyperparameters following LRA.</li>
          </ul>
          <div class="p-stat-strip">
            <div class="cell"><div class="v">1k</div><div class="l">IMDb seq len</div></div>
            <div class="cell"><div class="v">2k</div><div class="l">ListOps seq len</div></div>
            <div class="cell"><div class="v">4k</div><div class="l">Doc-match seq len</div></div>
          </div>"""))

# Key Result: 4-col table + callout + conclusion
BLOCKS.append(("""          <table class="results">
            <tr><th>Method</th><th>Metric</th></tr>
            <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>
            <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>
          </table>
          <div class="callout">{{HEADLINE_DELTA}}</div>
          <p class="conclusion">{{KEY_RESULT_CONCLUSION}}</p>""",
"""          <table class="results">
            <tr><th>Task</th><th>Best Homog.</th><th>NAS Prune</th><th>NAS 1-shot</th></tr>
            <tr><td class="method">Text classif.</td><td class="best">64.5</td><td>63.9</td><td>64.4</td></tr>
            <tr><td class="method">Doc. matching</td><td class="best">71.1</td><td>67.0</td><td>64.7</td></tr>
          </table>
          <div class="callout">Heterogeneous Transformers never beat the best homogeneous model on any task</div>
          <p class="conclusion">The masked-drop search reliably finds the best single attention (Reformer on ListOps, score 11.85); mixing types beats only the average, never the best.</p>"""))

# Ablation: bullets + callout-soft
BLOCKS.append(("""        <ul>
          <li>{{ABLATION_1}}</li>
          <li>{{ABLATION_2}}</li>
        </ul>
        <p class="conclusion">{{ABLATION_CONCLUSION}}</p>""",
"""        <ul>
          <li><strong>NAS Prune</strong> (iterative worst-first removal + fine-tuning) gives <strong>no consistent gain</strong> over the far cheaper <strong>NAS One-shot</strong> (top-4 in one pass).</li>
          <li>Weighting the mix toward the strongest attentions, or giving them more heads, also failed to improve consistently.</li>
        </ul>
        <div class="p-callout-soft">When good attentions are correctly identified, the cheap one-shot method is good enough.</div>"""))

# Problem: paragraph + callout-bar + chips
BLOCKS.append(("""        <p>{{PROBLEM}}</p>""",
"""        <p>Efficient Transformer attention mechanisms have proliferated, but <strong>no single one is best across tasks</strong> — leaving practitioners without a cheap way to pick the right attention for a given long-range task.</p>
        <div class="p-callout-bar">Attention performance is highly task-dependent when models train from scratch, without pretraining — the choice stays unclear.</div>
        <div class="p-chips"><span>Bigbird</span><span>Linear</span><span>Linformer</span><span>Local</span><span>Longformer</span><span>Performer</span><span>Reformer</span><span>Sparse</span><span>Synthesizer</span></div>"""))

# Takeaway: banner
BLOCKS.append(("""        <p>{{TAKEAWAY}}</p>""",
"""        <div class="p-banner">
          <div class="tag">Takeaway</div>
          <div>A cheap DARTS-like search with a masked-validation-drop metric reliably finds the single best attention — but combining attention types yields Transformers that beat only the <em>average</em> homogeneous model, never the best one.</div>
        </div>"""))

for old, new in BLOCKS:
    if old not in html:
        sys.exit(f"BLOCK not found:\n{old[:120]}...")
    html = html.replace(old, new, 1)

# ---- simple token substitutions ----
SUBS = {
    "{{TITLE}}": "DARTFormer: Finding the Best Type of Attention",
    "{{AUTHORS}}": "Jason Ross Brown<sup>1</sup>, Yiren Zhao<sup>2,1</sup>, Ilia Shumailov<sup>3</sup>, Robert D Mullins<sup>1</sup>",
    "{{AUTHOR_LEGEND}}": '<sup>1</sup> University of Cambridge &nbsp;&nbsp; <sup>2</sup> Imperial College London &nbsp;&nbsp; <sup>3</sup> University of Oxford',
    "{{VENUE_LOGO}}": "",
    "{{VENUE_NAME}}": "arXiv",
    "{{VENUE_YEAR}}": "2022",
    "{{CONTACT}}": "Email: jrb239@cam.ac.uk",
    "{{LOGO_1}}": "assets/logos/university-of-cambridge.png",
    "{{LOGO_2}}": "assets/logos/imperial-college-london.png",
    "{{LOGO_3}}": "assets/logos/university-of-oxford.png",
    "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    # headline numbers
    "{{HERO_VAL}}": "11.85",
    "{{HERO_LABEL}}": "Reformer drop-score &middot; ListOps",
    "{{HERO_NOTE}}": "vs &lt; 0.5 for all 8 other attentions",
    "{{STAT_2_VAL}}": "9", "{{STAT_2_LBL}}": "attentions",
    "{{STAT_3_VAL}}": "3", "{{STAT_3_LBL}}": "LRA tasks",
    "{{STAT_4_VAL}}": "0", "{{STAT_4_LBL}}": "hetero wins",
}
for k, v in SUBS.items():
    if k not in html:
        sys.exit(f"token not found: {k}")
    html = html.replace(k, v)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
