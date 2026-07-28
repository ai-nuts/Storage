#!/usr/bin/env python3
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# ---- 1. logo grid: keep only the one institution logo ----
logo_old = """  <div class="logo-grid" data-section="inst-logos">
    <span class="chip"><img src="{{LOGO_1}}" alt="" onerror="this.closest('.chip').remove()"></span>
    <span class="chip"><img src="{{LOGO_2}}" alt="" onerror="this.closest('.chip').remove()"></span>
    <span class="chip"><img src="{{LOGO_3}}" alt="" onerror="this.closest('.chip').remove()"></span>
    <span class="chip"><img src="{{LOGO_4}}" alt="" onerror="this.closest('.chip').remove()"></span>
    <span class="chip"><img src="{{LOGO_5}}" alt="" onerror="this.closest('.chip').remove()"></span>
    <span class="chip"><img src="{{LOGO_6}}" alt="" onerror="this.closest('.chip').remove()"></span>"""
logo_new = """  <div class="logo-grid" data-section="inst-logos">
    <span class="chip"><img src="assets/logos/university-of-hawai-i-at-m-noa.png" alt="" onerror="this.closest('.chip').remove()"></span>"""
assert logo_old in html, "logo grid not found"
html = html.replace(logo_old, logo_new)

# ---- 2. Problem section ----
problem_old = """      <div class="section" data-section="problem">
        <h2>Problem <button class="listen-btn" data-section="problem">Listen</button></h2>
        <p>{{PROBLEM}}</p>
      </div>"""
problem_new = """      <div class="section" data-section="problem">
        <h2>Problem <button class="listen-btn" data-section="problem">Listen</button></h2>
        <p>Machine learning on <strong>Sentinel-1 SAR</strong> ocean imagery is bottlenecked by <strong>sparse expert labels</strong>: only trained analysts can annotate radar vignettes, capping labeled datasets at a few thousand images.</p>
        <div class="p-callout-bar">Prior classifiers trained on a biased, single-label dataset &mdash; exemplary images, one label each &mdash; that misrepresents the true ocean population.</div>
      </div>"""
assert problem_old in html, "problem not found"
html = html.replace(problem_old, problem_new)

# ---- 3. Motivation section (drop grow, drop figure, add banner) ----
moti_old = """      <div class="section grow" data-section="motivation">
        <h2>Motivation <button class="listen-btn" data-section="motivation">Listen</button></h2>
        <ul>
          <li>{{MOTIVATION_1}}</li>
          <li>{{MOTIVATION_2}}</li>
        </ul>
        <!-- OPTIONAL: half-column Motivation figure. If the spec's Motivation figure line is `**Figure:** none`, REMOVE this entire <figure> block. -->
        <figure><img src="{{TEASER_FIGURE}}" alt=""><figcaption>{{TEASER_CAPTION}}</figcaption></figure>
      </div>"""
moti_new = """      <div class="section" data-section="motivation">
        <h2>Motivation <button class="listen-btn" data-section="motivation">Listen</button></h2>
        <ul>
          <li><strong>Contrastive self-supervised learning</strong> turns vast unlabeled pools into reusable embeddings &mdash; proven on natural and medical images, yet barely tested on remote-sensing SAR.</li>
          <li>Can it convert that unlabeled stream into a strong SAR representation and overcome the labeling bottleneck?</li>
        </ul>
        <div class="p-banner"><div class="tag">Untapped</div><div>Sentinel-1 alone collects <strong>~120,000</strong> Wave-mode ocean images <em>every month</em> &mdash; an enormous free resource contrastive learning could exploit.</div></div>
      </div>"""
assert moti_old in html, "motivation not found"
html = html.replace(moti_old, moti_new)

# ---- 4. Contribution (uncomment the commented block -> active section, grow) ----
contrib_new = """      <div class="section grow" data-section="contribution">
        <h2>Contribution <button class="listen-btn" data-section="contribution">Listen</button></h2>
        <ol>
          <li><strong>New unbiased benchmark:</strong> ~2,300 randomly-sampled, multi-label, expert-consensus SAR vignettes across 4 classes.</li>
          <li><strong>SwAV on SAR:</strong> a contrastive ResNet-50 embedding trained on ~3M unlabeled Sentinel-1 images.</li>
          <li><strong>Rigorous comparison:</strong> self-supervised vs. ImageNet transfer vs. the prior CmWV classifier, under three protocols.</li>
        </ol>
        <div class="p-chips"><span>Multi-label dataset</span><span class="alt">SwAV embedding</span><span class="muted">kNN &middot; linear &middot; fine-tune</span></div>
      </div>"""
html = re.sub(r'      <!-- ═+\n           CONTRIBUTION SECTION.*?═+ -->', contrib_new, html, flags=re.DOTALL)
assert 'data-section="contribution"' in html and '{{CONTRIBUTION_1}}' not in html, "contribution uncomment failed"

# ---- 5. Method: fill bullets + figure, add eval-protocol steps after method-body ----
html = html.replace("{{METHOD_1}}", "<strong>Backbone:</strong> a standard ResNet-50 pretrained with <strong>SwAV</strong> &mdash; a clustering-based contrastive framework that predicts swapped cluster assignments between two augmented views.")
html = html.replace("{{METHOD_2}}", "<strong>Modest batches:</strong> a feature queue (16 batches, 1000 centroids) removes the giant-batch requirement of methods like SimCLR.")
html = html.replace("{{METHOD_3}}", "<strong>Compute:</strong> batch 1024 on 8&times; V100, 65 epochs / ~10 days over ~3M unlabeled images; fine-tuning on a single V100.")
html = html.replace("{{METHOD_FIGURE}}", "assets/figures/page2_figure1.png")
html = html.replace("{{METHOD_CAPTION}}", "Example 20&times;20 km SAR scenes along the atmospheric-stability continuum: (a) MC, (b) MC/WS, (c) WS, (d) NV, and (e) a biological slick (OT).")

method_anchor = """          <figure class="method-figure"><img src="assets/figures/page2_figure1.png" alt="full"><figcaption>Example 20&times;20 km SAR scenes along the atmospheric-stability continuum: (a) MC, (b) MC/WS, (c) WS, (d) NV, and (e) a biological slick (OT).</figcaption></figure>
        </div>
      </div>
      <div class="mid-sub">"""
method_new = """          <figure class="method-figure"><img src="assets/figures/page2_figure1.png" alt="full"><figcaption>Example 20&times;20 km SAR scenes along the atmospheric-stability continuum: (a) MC, (b) MC/WS, (c) WS, (d) NV, and (e) a biological slick (OT).</figcaption></figure>
        </div>
        <div class="p-timeline-cards">
          <div class="card"><div class="n">1</div><div class="l">Weighted kNN</div><div class="s">frozen backbone</div></div>
          <div class="arrow">&rsaquo;</div>
          <div class="card"><div class="n">2</div><div class="l">Linear probe</div><div class="s">frozen + softmax</div></div>
          <div class="arrow">&rsaquo;</div>
          <div class="card"><div class="n">3</div><div class="l">Fine-tune</div><div class="s">all weights</div></div>
        </div>
      </div>
      <div class="mid-sub">"""
assert method_anchor in html, "method anchor not found"
html = html.replace(method_anchor, method_new)

# ---- 6. Dataset / Benchmark ----
ds_old = """        <div class="section" data-section="dataset-benchmark">
          <h2>Dataset / Benchmark <button class="listen-btn" data-section="dataset-benchmark">Listen</button></h2>
          <ul>
            <li>{{DATASET_1}}</li>
            <li>{{DATASET_2}}</li>
          </ul>
        </div>"""
ds_new = """        <div class="section" data-section="dataset-benchmark">
          <h2>Dataset / Benchmark <button class="listen-btn" data-section="dataset-benchmark">Listen</button></h2>
          <ul>
            <li><strong>Pretraining pool:</strong> 2,943,550 unlabeled Sentinel-1 A/B Wave-mode images (2017&ndash;2019), each 20&times;20 km at 5 m resolution.</li>
            <li><strong>Labeled benchmark:</strong> 2,300 expert-consensus, multi-label vignettes, split 60/20/20 for train / val / test.</li>
          </ul>
          <div class="p-chips"><span>MC</span><span>WS</span><span>NV</span><span class="muted">OT</span></div>
        </div>"""
assert ds_old in html, "dataset not found"
html = html.replace(ds_old, ds_new)

# ---- 7. Key Result: 4-column comparison table ----
kr_old = """        <div class="section" data-section="key-result">
          <h2>Key Results <button class="listen-btn" data-section="key-result">Listen</button></h2>
          <table class="results">
            <tr><th>Method</th><th>Metric</th></tr>
            <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>
            <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>
          </table>
          <div class="callout">{{HEADLINE_DELTA}}</div>
          <p class="conclusion">{{KEY_RESULT_CONCLUSION}}</p>
        </div>"""
kr_new = """        <div class="section" data-section="key-result">
          <h2>Key Results <button class="listen-btn" data-section="key-result">Listen</button></h2>
          <table class="p-table">
            <tr><th>Class &middot; AUROC</th><th>CmWV</th><th>ImageNet</th><th>SwAV</th></tr>
            <tr><td>Wind streaks (WS)</td><td>0.727</td><td>0.850</td><td>0.831</td></tr>
            <tr><td>Convection (MC)</td><td>0.793</td><td>0.873</td><td>0.872</td></tr>
            <tr><td>Negligible var. (NV)</td><td>~0.95</td><td>~0.95</td><td>~0.95</td></tr>
          </table>
          <div class="callout">Best fine-tuned micro-AUROC = 0.93 &middot; +0.10&ndash;0.12 over CmWV on the two hardest classes</div>
          <p class="conclusion">Both contrastive and ImageNet models comfortably beat the prior state of the art on wind streaks and convection cells.</p>
        </div>"""
assert kr_old in html, "key-result not found"
html = html.replace(kr_old, kr_new)

# ---- 8. Ablation Study: protocol comparison table ----
abl_old = """      <div class="section" data-section="ablation-study">
        <h2>Ablation Study <button class="listen-btn" data-section="ablation-study">Listen</button></h2>
        <ul>
          <li>{{ABLATION_1}}</li>
          <li>{{ABLATION_2}}</li>
        </ul>
        <p class="conclusion">{{ABLATION_CONCLUSION}}</p>
      </div>"""
abl_new = """      <div class="section" data-section="ablation-study">
        <h2>Ablation Study <button class="listen-btn" data-section="ablation-study">Listen</button></h2>
        <table class="p-table">
          <tr><th>Protocol &middot; micro-AUROC</th><th>ImageNet</th><th>SwAV (SSL)</th></tr>
          <tr><td>Weighted kNN</td><td>0.859</td><td>0.864</td></tr>
          <tr><td>Linear probe</td><td>0.836</td><td>0.841</td></tr>
          <tr class="best"><td>Full fine-tune</td><td>0.931</td><td>0.929</td></tr>
        </table>
        <p class="conclusion">SSL holds a small edge only with a frozen backbone; once all weights adapt end-to-end, initialization barely matters.</p>
      </div>"""
assert abl_old in html, "ablation not found"
html = html.replace(abl_old, abl_new)

# ---- 9. Takeaway ----
tk_old = """      <div class="section grow" data-section="takeaway">
        <h2>Takeaway <button class="listen-btn" data-section="takeaway">Listen</button></h2>
        <p>{{TAKEAWAY}}</p>
      </div>"""
tk_new = """      <div class="section grow" data-section="takeaway">
        <h2>Takeaway <button class="listen-btn" data-section="takeaway">Listen</button></h2>
        <p>On this preliminary benchmark, self-supervised contrastive pretraining on massive unlabeled SAR <strong>matches but does not beat</strong> plain ImageNet transfer &mdash; while both deliver a large jump over the prior state of the art.</p>
        <div class="p-callout-primary">The promise of SSL for SAR is real but unproven &mdash; longer training and remote-sensing-specific pretext tasks are the next step.</div>
      </div>"""
assert tk_old in html, "takeaway not found"
html = html.replace(tk_old, tk_new)

# ---- 10. Headline Numbers hero + supporting ----
subs = {
    "{{HERO_VAL}}":   "0.93",
    "{{HERO_LABEL}}": "Best micro-AUROC &middot; fine-tuned",
    "{{HERO_NOTE}}":  "honest tie: SSL &asymp; ImageNet",
    "{{STAT_2_VAL}}": "2.9M",  "{{STAT_2_LBL}}": "unlabeled SAR images",
    "{{STAT_3_VAL}}": "2,300", "{{STAT_3_LBL}}": "labeled vignettes",
    "{{STAT_4_VAL}}": "+0.10", "{{STAT_4_LBL}}": "WS AUROC vs CmWV",
    # titlebar / metadata
    "{{TITLE}}":         "Self-supervised detection of atmospheric phenomena from Sentinel-1 SAR imagery",
    "{{AUTHORS}}":       "Yannik Glaser<sup>1</sup>, Peter Sadowski<sup>1</sup>, Justin E. Stopa<sup>2</sup>",
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> Information &amp; Computer Sciences, Univ. of Hawai&#699;i at M&#257;noa &nbsp;&nbsp; <sup>2</sup> Ocean Engineering, Univ. of Hawai&#699;i at M&#257;noa",
    "{{VENUE_LOGO}}":    "assets/logos/_venue.png",
    "{{VENUE_NAME}}":    "NeurIPS",
    "{{VENUE_YEAR}}":    "2022",
    "{{CONTACT}}":       "Email: yglaser@hawaii.edu",
    "{{QR_PAPER}}":      "assets/qr/paper.png",
    "{{URL_PAPER}}":     "ml4physicalsciences.github.io",
}
for k, v in subs.items():
    assert k in html, f"missing token {k}"
    html = html.replace(k, v)

# ---- 11. PLAYLIST: add contribution ----
html = html.replace(
    '["title", "problem", "motivation", "method",',
    '["title", "problem", "motivation", "contribution", "method",')

# ---- neutralize header doc-comment placeholder list ----
html = html.replace("{{LOGO_1}}..{{LOGO_6}}", "LOGO_1..6")

# ---- sanity ----
leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")
target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
