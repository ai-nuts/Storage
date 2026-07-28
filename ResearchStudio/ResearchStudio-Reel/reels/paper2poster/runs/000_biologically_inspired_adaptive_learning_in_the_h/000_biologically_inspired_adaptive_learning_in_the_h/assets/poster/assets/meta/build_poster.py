#!/usr/bin/env python3
"""Fill poster.html for the (figure-free, conceptual) Hopfield SO paper.
Reads the big template from disk, does surgical string replacements, writes back.
The template never passes through the model output channel."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2] / "poster.html"
html = target.read_text(encoding="utf-8")

def sub(old, new):
    global html
    if old not in html:
        sys.exit(f"FRAGMENT NOT FOUND:\n{old[:200]}")
    html = html.replace(old, new, 1)

# ------------------------------------------------------------------ COL 1
# Problem
sub(
"""      <div class="section" data-section="problem">
        <h2>Problem <button class="listen-btn" data-section="problem">Listen</button></h2>
        <p>{{PROBLEM}}</p>
      </div>""",
"""      <div class="section" data-section="problem">
        <h2>Problem <button class="listen-btn" data-section="problem">Listen</button></h2>
        <p>Deep learning attains high accuracy but leans on <strong>massive datasets</strong>, supervised or reward-based rules, and heavy energy &mdash; and it suffers <strong>catastrophic forgetting</strong> when tasks are trained in sequence. Living systems instead learn and adapt from <strong>sparse data</strong>, with minimal energy and few iterations.</p>
        <div class="p-callout-soft">Hopfield networks offer unsupervised, associative, one-shot learning &mdash; yet basic forms store only <span class="num">~0.14N</span> patterns and rarely exploit the biology that inspired them.</div>
      </div>""")

# Motivation (drop grow + figure) + enable Contribution (grow, bottom)
sub(
"""      <!-- Non-bottom section: size to content (no `.grow`). -->
      <div class="section grow" data-section="motivation">
        <h2>Motivation <button class="listen-btn" data-section="motivation">Listen</button></h2>
        <ul>
          <li>{{MOTIVATION_1}}</li>
          <li>{{MOTIVATION_2}}</li>
        </ul>
        <!-- OPTIONAL: half-column Motivation figure. If the spec's Motivation figure line is `**Figure:** none`, REMOVE this entire <figure> block. -->
        <figure><img src="{{TEASER_FIGURE}}" alt=""><figcaption>{{TEASER_CAPTION}}</figcaption></figure>
      </div>""",
"""      <div class="section" data-section="motivation">
        <h2>Motivation <button class="listen-btn" data-section="motivation">Listen</button></h2>
        <ul>
          <li>Adaptation requires <strong>integrating new information while staying stable</strong> &mdash; too much destabilization blocks learning; too much memory locks in stale patterns.</li>
          <li>Biology resolves this robustness-vs-flexibility tension through <strong>metaplasticity, homeostasis, inhibition, and resets</strong>, acting across many timescales.</li>
          <li>The <strong>self-optimization (SO) model</strong> &mdash; a Hopfield net with Hebbian updates and periodic resets &mdash; already echoes biological attractor dynamics: a natural substrate to enrich.</li>
        </ul>
        <div class="p-chips">
          <span>Metaplasticity</span><span>Homeostasis</span><span>Inhibition</span><span>Forgetting / resets</span>
        </div>
      </div>
      <div class="section grow" data-section="contribution">
        <h2>Contribution <button class="listen-btn" data-section="contribution">Listen</button></h2>
        <ul>
          <li><strong>Distills</strong> the core mechanisms of biological adaptation &mdash; metaplasticity and homeostasis, plus inhibition and forgetting.</li>
          <li><strong>Translates</strong> them into the SO model and Hopfield networks via an adaptive learning rate, enhanced modularity, and a modified activation rule.</li>
          <li><strong>Reframes</strong> biological constraints as scaffolding that lets added degrees of freedom expand productively rather than collapse into noise.</li>
        </ul>
        <div class="p-callout-bar">Constraints and degrees of freedom are complementary: the architecture gives shape, and within it higher freedom becomes adaptive behavior.</div>
      </div>""")

# ------------------------------------------------------------------ COL 2 : Method
sub(
"""      <div class="section grow" data-section="method">
        <h2>Method <button class="listen-btn" data-section="method">Listen</button></h2>
        <ul>
          <li>{{METHOD_1}}</li>
          <li>{{METHOD_2}}</li>
          <li>{{METHOD_3}}</li>
        </ul>
        <figure><img src="{{METHOD_FIGURE}}" alt="half"><figcaption>{{METHOD_CAPTION}}</figcaption></figure>
      </div>""",
"""      <div class="section grow" data-section="method">
        <h2>Method <button class="listen-btn" data-section="method">Listen</button></h2>
        <p>The core idea: raise the network's <strong>degrees of freedom without adding parameters</strong> &mdash; let existing components do more work, the way biology does.</p>
        <div class="p-steps">
          <div class="step"><strong>Local metaplasticity.</strong> Make the learning rate <span class="num">&alpha;</span> a function of the connection weight, so the fixed-rate Hebbian rule becomes weight-dependent &mdash; potentiating co-active synapses faster, depressing opposing ones more slowly.</div>
          <div class="step"><strong>Network metaplasticity.</strong> Tie <span class="num">&alpha;</span> to the energy change <span class="num">&Delta;E</span> (akin to gradient descent on the energy landscape) &mdash; learning slows on shallow slopes and speeds on steep ones, helping escape local minima.</div>
          <div class="step"><strong>Homeostasis.</strong> Approximate regulation around a set point with oscillatory (e.g. trigonometric) activation functions.</div>
          <div class="step"><strong>Modularity + inhibition.</strong> Adaptive intra- and inter-module connections with inhibition support temporal integration, degeneracy, and continuous learning &mdash; echoing synaptic tagging and capture.</div>
        </div>
        <div class="p-eq">
          $w_{ij}(t{+}1) = w_{ij}(t) + f(w_{ij})\\, s_i s_j, \\qquad \\alpha = f(w_{ij})$
          <span class="where">weight-dependent Hebbian update; network-level metaplasticity instead sets $\\alpha = f(\\Delta E)$</span>
        </div>
      </div>""")

# ------------------------------------------------------------------ COL 3 : Dataset + Key Result
sub(
"""      <div class="section" data-section="dataset-benchmark">
        <h2>Dataset / Benchmark <button class="listen-btn" data-section="dataset-benchmark">Listen</button></h2>
        <ul>
          <li>{{DATASET_1}}</li>
          <li>{{DATASET_2}}</li>
        </ul>
      </div>""",
"""      <div class="section" data-section="dataset-benchmark">
        <h2>Grounding <button class="listen-btn" data-section="dataset-benchmark">Listen</button></h2>
        <p>A <strong>conceptual proposal</strong> paper &mdash; it introduces no dataset and runs no benchmarks, instead building on prior computational work with the SO model.</p>
        <div class="p-banner">
          <div class="tag">Grounded in</div>
          <div>An SO model of the <em>C.&nbsp;elegans</em> connectome (inhibitory inter-cluster links) and SO models that solve combinatorial satisfiability problems.</div>
        </div>
      </div>""")

sub(
"""      <div class="section grow" data-section="key-result">
        <h2>Key Results <button class="listen-btn" data-section="key-result">Listen</button></h2>
        <table class="results">
          <tr><th>Method</th><th>Metric</th></tr>
          <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>
          <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>
        </table>
        <div class="callout">{{HEADLINE_DELTA}}</div>
        <p class="conclusion">{{KEY_RESULT_CONCLUSION}}</p>
      </div>""",
"""      <div class="section grow" data-section="key-result">
        <h2>Key Result <button class="listen-btn" data-section="key-result">Listen</button></h2>
        <p>The outcome is a <strong>coherent design framework</strong>: concrete, biologically grounded modifications to the SO model's learning rate, modularity, and activation rule &mdash; a unified map from mechanism to implementation, rather than measured performance.</p>
        <div class="p-callout-primary">Biological constraints and increased degrees of freedom are complementary &mdash; constraints give shape to flexibility that would otherwise collapse into noise.</div>
        <p class="conclusion">Each mechanism maps onto a specific change: an adaptive learning rate driven by weights or energy, oscillatory activations, and adaptive modularity with inhibition. These proposals still require algorithmic definition and testing.</p>
      </div>""")

# ------------------------------------------------------------------ COL 4 : Ablation + Headline + Takeaway
sub(
"""      <div class="section" data-section="ablation-study">
        <h2>Ablation Study <button class="listen-btn" data-section="ablation-study">Listen</button></h2>
        <ul>
          <li>{{ABLATION_1}}</li>
          <li>{{ABLATION_2}}</li>
        </ul>
        <p class="conclusion">{{ABLATION_CONCLUSION}}</p>
      </div>""",
"""      <div class="section" data-section="ablation-study">
        <h2>Design Variants <button class="listen-btn" data-section="ablation-study">Listen</button></h2>
        <table class="p-table">
          <tr><th>Design axis</th><th>Variants to explore</th></tr>
          <tr><td>Learning-rate <em>f</em></td><td>linear &middot; nonlinear</td></tr>
          <tr><td>Activation rule</td><td>sigmoid &middot; Heaviside &middot; trig</td></tr>
          <tr><td>Modular structure</td><td>intra-/inter-module + inhibition</td></tr>
        </table>
        <p class="conclusion">No model is trained; these variants are expected to yield qualitatively different dynamics &mdash; modeling normal vs pathological modes &mdash; and form the agenda for future study.</p>
      </div>""")

# Headline Numbers
sub(
"""        <div class="headline-hero">
          <div class="hero-main"><div class="hero-val">{{HERO_VAL}}</div>
          <div class="hero-label">{{HERO_LABEL}}</div>
          <div class="hero-note">{{HERO_NOTE}}</div></div>
          <div class="supporting">
            <div class="stat-mini"><div class="val">{{STAT_2_VAL}}</div><div class="lbl">{{STAT_2_LBL}}</div></div>
            <div class="stat-mini"><div class="val">{{STAT_3_VAL}}</div><div class="lbl">{{STAT_3_LBL}}</div></div>
            <div class="stat-mini"><div class="val">{{STAT_4_VAL}}</div><div class="lbl">{{STAT_4_LBL}}</div></div>
          </div>
        </div>""",
"""        <div class="headline-hero">
          <div class="hero-main"><div class="hero-val">0.14N</div>
          <div class="hero-label">Hopfield storage capacity</div>
          <div class="hero-note">the limit that motivates biological extensions</div></div>
          <div class="supporting">
            <div class="stat-mini"><div class="val">3</div><div class="lbl">mechanisms distilled</div></div>
            <div class="stat-mini"><div class="val">2</div><div class="lbl">metaplasticity levels</div></div>
            <div class="stat-mini"><div class="val">3</div><div class="lbl">SO-model levers</div></div>
          </div>
        </div>""")

# Takeaway
sub(
"""      <div class="section grow" data-section="takeaway">
        <h2>Takeaway <button class="listen-btn" data-section="takeaway">Listen</button></h2>
        <p>{{TAKEAWAY}}</p>
      </div>""",
"""      <div class="section grow" data-section="takeaway">
        <h2>Takeaway <button class="listen-btn" data-section="takeaway">Listen</button></h2>
        <p>Metaplasticity, homeostasis, and inhibition can be folded into Hopfield-network self-optimization by making the <strong>learning rate adaptive</strong>, <strong>enhancing modularity</strong>, and <strong>modifying the activation rule</strong> &mdash; a route toward associative-memory models that learn adaptively from sparse data, closer to how living systems do.</p>
        <div class="p-callout-bar">The right constraints let added degrees of freedom become useful flexibility instead of noise.</div>
      </div>""")

# ------------------------------------------------------------------ PLAYLIST (add contribution)
sub(
'''const PLAYLIST = ["title", "problem", "motivation", "method", "dataset-benchmark", "key-result", "ablation-study", "takeaway"];''',
'''const PLAYLIST = ["title", "problem", "motivation", "contribution", "method", "dataset-benchmark", "key-result", "ablation-study", "takeaway"];''')

# ------------------------------------------------------------------ metadata (replace-all)
meta = {
    "{{TITLE}}": "Biologically-inspired adaptive learning in the Hopfield-network based self-optimization model",
    "{{AUTHORS}}": "Aisha Belhadi<sup>1</sup>",
    "{{AUTHOR_LEGEND}}": '<sup>1</sup> Okinawa Institute of Science and Technology Graduate University',
    "{{VENUE_NAME}}": "NeurIPS",
    "{{VENUE_YEAR}}": "2023",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "Email: aisha.belhadi@gmail.com",
    "{{LOGO_1}}": "assets/logos/okinawa-institute-of-science-and-technology-graduate-university.png",
    "{{LOGO_2}}": "", "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{URL_PAPER}}": "openreview.net/forum?id=WjHYgEfXiV",
}
for k, v in meta.items():
    html = html.replace(k, v)

# strip HTML comments that still carry {{...}} tokens (commented-out optional
# blocks + placeholder explainer comments) so no token survives inside a comment.
html = re.sub(r"<!--.*?-->", lambda m: "" if "{{" in m.group(0) else m.group(0), html, flags=re.DOTALL)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"UNREPLACED PLACEHOLDERS: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
