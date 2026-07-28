#!/usr/bin/env python3
"""Indirect poster builder for VectorMapNet (3col, framed, v4, burgundy)."""
import re
import sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# ---------- header / metadata placeholders ----------
SUBS = {
    "{{TITLE}}": "VectorMapNet: End-to-end Vectorized HD Map Learning",
    "{{AUTHORS}}": ("Yicheng Liu<sup>1,2</sup>, Tianyuan Yuan<sup>2</sup>, "
                    "Yue Wang<sup>3</sup>, Yilun Wang<sup>4</sup>, Hang Zhao<sup>1,2&dagger;</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> Shanghai Qi Zhi Institute &nbsp;&nbsp; "
                          "<sup>2</sup> Tsinghua University &nbsp;&nbsp; "
                          "<sup>3</sup> MIT &nbsp;&nbsp; <sup>4</sup> Li Auto"),
    "{{CONTACT}}": "Email: zhaohang0124@gmail.com",
    "{{VENUE_NAME}}": "ICML",
    "{{VENUE_YEAR}}": "2023",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{LOGO_1}}": "assets/logos/shanghai-qi-zhi-institute.png",
    "{{LOGO_2}}": "assets/logos/tsinghua-university.png",
    "{{LOGO_3}}": "assets/logos/massachusetts-institute-of-technology.png",
    "{{LOGO_4}}": "assets/logos/li-auto.png",
    "{{LOGO_5}}": "",
    "{{LOGO_6}}": "",
}

# ---------- authored 3-column body (4 figures, balanced) ----------
COLUMNS = r'''  <div class="columns">

    <!-- Column 1: Problem, Motivation (+Fig1 overview), Ablation (+Fig3 keypoints). -->
    <div class="col">
      <div class="section" data-section="problem">
        <h2>Problem <button class="listen-btn" data-section="problem">Listen</button></h2>
        <p>Autonomous driving needs <strong>vectorized</strong> HD semantic maps, yet manual annotation does not scale and existing learners output only <strong>dense rasterized</strong> segmentations needing brittle post-processing.</p>
        <div class="p-banner">
          <div class="tag">First</div>
          <div>The first <strong>end-to-end</strong> vectorized HD-map learner: no rasterization, no post-processing.</div>
        </div>
      </div>

      <div class="section" data-section="motivation">
        <h2>Motivation <button class="listen-btn" data-section="motivation">Listen</button></h2>
        <div class="p-vs">
          <div class="side bad"><h4>Rasterize &rarr; Vectorize</h4><p>Dense pixel grid + fragile post-processing.</p></div>
          <div class="sep">vs.</div>
          <div class="side good"><h4>VectorMapNet</h4><p>Sparse directional polylines.</p></div>
        </div>
        <ul>
          <li>Online mapping from onboard sensors sidesteps the labor and meter-level localization error of offline HD maps.</li>
          <li>Prior SOTA (HDMapNet) still rasterizes, then post-processes vectors by hand, capping accuracy and scalability.</li>
        </ul>
      </div>

      <div class="section grow" data-section="ablation-study">
        <h2>Ablation Study <button class="listen-btn" data-section="ablation-study">Listen</button></h2>
        <ul>
          <li><strong>Bounding Box (k=2)</strong> keypoints beat SME (k=3) and Extreme Points (k=4) by <strong>+2.0</strong> Fréchet mAP and <strong>+7.3</strong> Chamfer mAP.</li>
          <li>Two-stage training (teacher forcing, then fine-tuning on predicted keypoints) adds <strong>+6.9</strong> mAP (Camera) and <strong>+8.5</strong> mAP (Fusion).</li>
        </ul>
        <div class="p-stat-strip">
          <div class="cell"><div class="v">+7.3</div><div class="l">Chamfer mAP &middot; box vs alt</div></div>
          <div class="cell"><div class="v">+8.5</div><div class="l">mAP &middot; 2-stage (Fusion)</div></div>
          <div class="cell"><div class="v">0.826</div><div class="l">minADE &middot; pred map</div></div>
        </div>
        <div class="p-callout-soft">Predicted maps sharpen a downstream motion-forecasting baseline &mdash; near the GT-map ceiling.</div>
      </div>
    </div>

    <!-- Column 2 (centerpiece): Method + Fig1 + key equation; Headline Numbers. -->
    <div class="col">
      <div class="section grow" data-section="method">
        <h2>Method <button class="listen-btn" data-section="method">Listen</button></h2>
        <div class="p-steps">
          <div class="step"><strong>BEV feature extractor</strong> lifts camera (ResNet + IPM) and LiDAR (PointPillars) into a shared BEV space.</div>
          <div class="step"><strong>Map element detector</strong> — a DETR-style decoder with element queries predicts each element's keypoints + class.</div>
          <div class="step"><strong>Polyline generator</strong> — an autoregressive Transformer decodes each element into ordered vertices.</div>
        </div>
        <div class="p-eq">$$p(V^{poly}_i)=\prod_{n=1}^{2N_v} p\!\left(v_{i,n}\mid v_{i,\lt n}, A_i, l_i, \mathcal{F}_{BEV}\right)$$<span class="where">$\mathcal{L}=\mathcal{L}_{det}+\mathcal{L}_{gen}$</span></div>
        <figure><img src="assets/figures/figure1.png" alt=""><figcaption>Fig 1 &middot; End-to-end pipeline: sensors &rarr; BEV features &rarr; element keypoints &rarr; polylines.</figcaption></figure>
      </div>

      <div class="section" data-section="dataset-benchmark">
        <h2>Dataset / Benchmark <button class="listen-btn" data-section="dataset-benchmark">Listen</button></h2>
        <ul>
          <li>Evaluated on <strong>nuScenes</strong> and <strong>Argoverse2</strong> (z-axis annotations enable 2D <em>and</em> 3D evaluation), scoring polylines with an order-aware <strong>Fréchet AP</strong> alongside Chamfer AP.</li>
        </ul>
        <div class="p-chips">
          <span>nuScenes</span><span>Argoverse2</span>
          <span class="alt">Ped Crossing</span><span class="alt">Lane Divider</span><span class="alt">Road Boundary</span>
        </div>
      </div>
    </div>

    <!-- Column 3: Key Results (hero numbers + Fig4), Takeaway. -->
    <div class="col">
      <div class="section grow" data-section="key-result">
        <h2>Key Results <button class="listen-btn" data-section="key-result">Listen</button></h2>
        <div class="headline-hero">
          <div class="hero-main"><div class="hero-val">53.7</div>
          <div class="hero-label">mAP &middot; nuScenes (Fusion + fine-tune)</div>
          <div class="hero-note">vs 31.0 HDMapNet &middot; +14.2 mAP</div></div>
          <div class="supporting">
            <div class="stat-mini"><div class="val">+14.6</div><div class="lbl">mAP Argoverse2</div></div>
            <div class="stat-mini"><div class="val">+17.9</div><div class="lbl">mAP camera-only</div></div>
            <div class="stat-mini"><div class="val">+9.9</div><div class="lbl">mAP LiDAR-only</div></div>
          </div>
        </div>
        <figure><img src="assets/figures/figure4.png" alt=""><figcaption>Fig 4 &middot; Camera-only: sharp corners, no self-loops (red = missing in GT).</figcaption></figure>
        <div class="callout">+14.2 mAP vs HDMapNet (nuScenes) &middot; +14.6 mAP (Argoverse2)</div>
      </div>

      <div class="section" data-section="takeaway">
        <h2>Takeaway <button class="listen-btn" data-section="takeaway">Listen</button></h2>
        <div class="p-callout-primary">Frame HD mapping as detection &rarr; polyline generation: one end-to-end network predicts clean, directional vector maps straight from sensors.</div>
        <p>Polylines are a versatile primitive: the same model extends to centerline prediction with no structural change, and its predicted maps measurably sharpen a downstream motion-forecasting baseline (minADE 0.909 &rarr; 0.826).</p>
      </div>
    </div>

  </div>
</div>
</div>

'''

# splice: replace from `<div class="columns">` up to the Narration comment
html = re.sub(
    r'  <div class="columns">.*?\n\n<!-- Narration:',
    lambda m: COLUMNS + "<!-- Narration:",
    html,
    count=1,
    flags=re.DOTALL,
)

# PLAYLIST: add ablation-study
html = html.replace(
    '["title", "problem", "motivation", "method", "dataset-benchmark", "key-result", "takeaway"]',
    '["title", "problem", "motivation", "method", "dataset-benchmark", "key-result", "ablation-study", "takeaway"]',
)

# header/meta substitutions
for k, v in SUBS.items():
    html = html.replace(k, v)

# sanity: no leftover placeholders
leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
