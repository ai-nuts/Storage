#!/usr/bin/env python3
"""Fill poster.html for the Bayesian Inverse Transition Learning poster.
Structural section-body edits + metadata substitution. Template read from disk,
never emitted whole. Run: python build_poster.py <outdir>/poster.html"""
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

# ---- 1. drop optional sections (keep ablation; it carries real content for col4) ----
for sec in ("contribution", "dataset-benchmark", "scan-to-read"):
    html = drop_section(html, sec)

# ---- 2. PLAYLIST in sync ----
html = html.replace(
    'const PLAYLIST = ["title", "problem", "motivation", "method", "dataset-benchmark", "key-result", "ablation-study", "takeaway"];',
    'const PLAYLIST = ["title", "problem", "motivation", "method", "key-result", "ablation-study", "takeaway"];')

# ---- 3. structural section-body rewrites (block-for-block) ----
BLOCKS = []

# Problem: paragraph + P3 callout-bar
BLOCKS.append((
    '''      <div class="section" data-section="problem">
        <h2>Problem <button class="listen-btn" data-section="problem">Listen</button></h2>
        <p>{{PROBLEM}}</p>
      </div>''',
    '''      <div class="section" data-section="problem">
        <h2>Problem <button class="listen-btn" data-section="problem">Listen</button></h2>
        <p>In offline RL for <strong>healthcare and education</strong>, the transition dynamics <em>T</em> must be estimated from a fixed batch of data. Standard <strong>MLE</strong> of <em>T</em> yields <span class="hi">high-variance</span> policies that take <span class="hi">unsafe actions</span> wherever the data gives poor state&ndash;action coverage.</p>
        <div class="p-callout-bar">Expert-only data leaves much of the state&ndash;action space unseen &mdash; no amount of it fills the gap.</div>
      </div>'''))

# Motivation: bullets + P7 vs (remove teaser figure)
BLOCKS.append((
    '''      <div class="section grow" data-section="motivation">
        <h2>Motivation <button class="listen-btn" data-section="motivation">Listen</button></h2>
        <ul>
          <li>{{MOTIVATION_1}}</li>
          <li>{{MOTIVATION_2}}</li>
        </ul>
        <!-- OPTIONAL: half-column Motivation figure. If the spec's Motivation figure line is `**Figure:** none`, REMOVE this entire <figure> block. -->
        <figure><img src="{{TEASER_FIGURE}}" alt=""><figcaption>{{TEASER_CAPTION}}</figcaption></figure>
      </div>''',
    '''      <div class="section grow" data-section="motivation">
        <h2>Motivation <button class="listen-btn" data-section="motivation">Listen</button></h2>
        <ul>
          <li>The users who generate offline trajectories &mdash; <strong>clinicians, teachers</strong> &mdash; are usually <strong>near-optimal</strong>, so their choices encode which actions are good.</li>
          <li>A plain MLE of <em>T</em> throws that signal away; prior gradient-based inverse RL recovers an expert's <em>belief</em> of <em>T</em> but never ties it to the true <em>T</em>, and inherits gradient instability in tabular MDPs.</li>
        </ul>
        <div class="p-vs">
          <div class="side bad"><h4>Plain MLE of T</h4><p>Ignores the expert; high variance; unsafe where data is thin.</p></div>
          <div class="sep">vs.</div>
          <div class="side good"><h4>ITL (Ours)</h4><p>Turns the near-optimal expert into gradient-free constraints on T.</p></div>
        </div>
      </div>'''))

# Method: bullets + P15 equation (no figure)
BLOCKS.append((
    '''      <div class="section grow" data-section="method">
        <h2>Method <button class="listen-btn" data-section="method">Listen</button></h2>
        <ul>
          <li>{{METHOD_1}}</li>
          <li>{{METHOD_2}}</li>
          <li>{{METHOD_3}}</li>
        </ul>
        <figure><img src="{{METHOD_FIGURE}}" alt="half"><figcaption>{{METHOD_CAPTION}}</figcaption></figure>
      </div>''',
    '''      <div class="section grow" data-section="method">
        <h2>Method <button class="listen-btn" data-section="method">Listen</button></h2>
        <ul>
          <li><strong>Key idea:</strong> a near-optimal expert's choices are informative <strong>constraints on the dynamics <em>T</em></strong> &mdash; recover <em>T</em> without gradients.</li>
          <li>Separate constraint sets handle a fully-optimal vs. a sub-optimal (stochastic) expert; a per-(s,a) slack <em>&delta;</em> enforces the <span class="hi">&epsilon;-ball</span> property (Algorithm&nbsp;1).</li>
        </ul>
        <div class="p-steps">
          <div class="step"><strong>Take</strong> an <em>&epsilon;</em>-optimal expert <em>&pi;<sub>&epsilon;</sub></em> and batch data <em>D</em>.</div>
          <div class="step"><strong>Constrain:</strong> closed-form Bellman &rArr; expert actions out-value the actions never taken.</div>
          <div class="step"><strong>Model:</strong> place a <strong>Dirichlet&ndash;Multinomial</strong> posterior <em>P(T&#8239;|&#8239;D)</em> over the dynamics.</div>
          <div class="step"><strong>Clip:</strong> rejection-sample, keep only <em>T</em> meeting the constraints &rarr; <em>P(T&#8239;|&#8239;D,&#8239;&pi;<sub>&epsilon;</sub>)</em>.</div>
        </div>
        <div class="p-eq">
          $V^{\\pi} = R_{\\pi} + \\gamma\\, T_{\\pi} V^{\\pi} = (I-\\gamma T_{\\pi})^{-1} R_{\\pi}$
          <span class="where">Closed-form policy value &mdash; the algebra the constraints are written on.</span>
        </div>
        <div class="p-eq">
          $T_{a^*}(I-\\gamma \\hat{T}_{\\pi_\\epsilon})^{-1} R_{\\pi_\\epsilon} = \\tfrac{1}{\\gamma}\\big((I-\\gamma \\hat{T}_{\\pi_\\epsilon})^{-1} R_{\\pi_\\epsilon} - R_{a^*}\\big)$
          <span class="where">The constraint pins each transition row <em>T<sub>a*</sub></em> so every expert action dominates the actions the expert never took.</span>
        </div>
      </div>'''))

# Key Results: 3-col table + figure + callout + conclusion
BLOCKS.append((
    '''      <div class="section grow" data-section="key-result">
        <h2>Key Results <button class="listen-btn" data-section="key-result">Listen</button></h2>
        <table class="results">
          <tr><th>Method</th><th>Metric</th></tr>
          <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>
          <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>
        </table>
        <div class="callout">{{HEADLINE_DELTA}}</div>
        <p class="conclusion">{{KEY_RESULT_CONCLUSION}}</p>
      </div>''',
    '''      <div class="section grow" data-section="key-result">
        <h2>Key Results <button class="listen-btn" data-section="key-result">Listen</button></h2>
        <table class="p-table">
          <tr><th>Method</th><th>Q*<sub>metric</sub> &epsilon;=0</th><th>Det-state Acc.</th></tr>
          <tr><td>MLE</td><td>59.75 &plusmn;52</td><td>67&ndash;92%</td></tr>
          <tr><td><em>P(T&#8239;|&#8239;D)</em></td><td>142.17 &plusmn;8.7</td><td>&mdash;</td></tr>
          <tr class="best"><td><em>P(T&#8239;|&#8239;D,&#8239;&pi;<sub>&epsilon;</sub>)</em> (Ours)</td><td>0 &plusmn;0</td><td>100%</td></tr>
        </table>
        <figure><img src="assets/figures/figure1.png" alt="Q* metric across 1000 datasets"><figcaption>Q*<sub>metric</sub> across 1000 datasets for &epsilon;&isin;{0,3,4} &times; low/high data. Our method <strong>(red)</strong> hugs zero with the least variance; MLE (blue) and <em>P(T&#8239;|&#8239;D)</em> (orange) stay high and noisy.</figcaption></figure>
        <div class="callout"><strong>0&nbsp;&plusmn;&nbsp;0</strong> Q*<sub>metric</sub> &mdash; dominates both baselines with the least variance.</div>
        <p class="conclusion">The clipped posterior never picks an action outside the expert's &epsilon;-ball, so it makes no bad mistakes.</p>
      </div>'''))

# Ablation Study: P17 banner + one bullet + conclusion
BLOCKS.append((
    '''      <div class="section" data-section="ablation-study">
        <h2>Ablation Study <button class="listen-btn" data-section="ablation-study">Listen</button></h2>
        <ul>
          <li>{{ABLATION_1}}</li>
          <li>{{ABLATION_2}}</li>
        </ul>
        <p class="conclusion">{{ABLATION_CONCLUSION}}</p>
      </div>''',
    '''      <div class="section" data-section="ablation-study">
        <h2>Ablation Study <button class="listen-btn" data-section="ablation-study">Listen</button></h2>
        <div class="p-banner">
          <div class="tag">Warns</div>
          <div>More data does <strong>not</strong> rescue MLE &mdash; even at <em>K</em>=300 episodes it keeps making <span class="hi">bad mistakes</span> (actions outside the &epsilon;-ball).</div>
        </div>
        <ul>
          <li>Sweeping <em>&epsilon;</em>=0/3/4 confirms the method holds across degrees of expert optimality &mdash; recovering policies that can <strong>beat the expert</strong> while keeping near-zero variance.</li>
        </ul>
        <p class="conclusion">Expert-only data leaves large regions unexplored &mdash; an aleatoric uncertainty more episodes cannot overcome.</p>
      </div>'''))

# Headline Numbers: hero + 3 uniform stat tiles
BLOCKS.append((
    '''        <div class="headline-hero">
          <div class="hero-main"><div class="hero-val">{{HERO_VAL}}</div>
          <div class="hero-label">{{HERO_LABEL}}</div>
          <div class="hero-note">{{HERO_NOTE}}</div></div>
          <div class="supporting">
            <div class="stat-mini"><div class="val">{{STAT_2_VAL}}</div><div class="lbl">{{STAT_2_LBL}}</div></div>
            <div class="stat-mini"><div class="val">{{STAT_3_VAL}}</div><div class="lbl">{{STAT_3_LBL}}</div></div>
            <div class="stat-mini"><div class="val">{{STAT_4_VAL}}</div><div class="lbl">{{STAT_4_LBL}}</div></div>
          </div>
        </div>''',
    '''        <div class="headline-hero">
          <div class="hero-main"><div class="hero-val">0 &plusmn; 0</div>
          <div class="hero-label">Q*<sub>metric</sub> at &epsilon;=0, low &amp; high data</div>
          <div class="hero-note">vs MLE 59.75 &middot; P(T|D) 142.17</div></div>
          <div class="supporting">
            <div class="stat-mini"><div class="val">100%</div><div class="lbl">det-state accuracy</div></div>
            <div class="stat-mini"><div class="val">8.79</div><div class="lbl">Q* &epsilon;=4 high (MLE 20.11)</div></div>
            <div class="stat-mini"><div class="val">&plusmn;0</div><div class="lbl">policy std (was &plusmn;52)</div></div>
          </div>
        </div>'''))

# Takeaway: paragraph + P1 callout-primary
BLOCKS.append((
    '''      <div class="section grow" data-section="takeaway">
        <h2>Takeaway <button class="listen-btn" data-section="takeaway">Listen</button></h2>
        <p>{{TAKEAWAY}}</p>
      </div>''',
    '''      <div class="section grow" data-section="takeaway">
        <h2>Takeaway <button class="listen-btn" data-section="takeaway">Listen</button></h2>
        <p>Clipping a Bayesian posterior over transition dynamics with <strong>expert-derived constraints</strong> yields gradient-free offline policies that are <span class="hi">provably safe</span>, can <strong>outperform the expert</strong>, and carry dramatically lower variance than MLE.</p>
        <div class="p-callout-primary">Constraints + uncertainty also rank actions in uncertain states &mdash; more informative policies for high-stakes planning like healthcare.</div>
      </div>'''))

for old, new in BLOCKS:
    if old not in html:
        sys.exit("BLOCK not found (template drift?):\n" + old[:160])
    html = html.replace(old, new, 1)

# ---- 4. metadata / header placeholders ----
SUBS = {
    "{{TITLE}}": "Bayesian Inverse Transition Learning for Offline Settings",
    "{{AUTHORS}}": 'Leo Benac<sup>1</sup>, Sonali Parbhoo<sup>2</sup>, Finale Doshi-Velez<sup>1</sup>',
    "{{AUTHOR_LEGEND}}": '<sup>1</sup> Harvard University &nbsp;&nbsp; <sup>2</sup> Imperial College London',
    "{{VENUE_NAME}}": "ICML",
    "{{VENUE_YEAR}}": "2023",
    "{{VENUE_TAG}}": "",
    "{{VENUE_LINK}}": "https://arxiv.org/abs/2308.05075",
    "{{CONTACT}}": "Email: lbenac@g.harvard.edu",
    "{{LOGO_1}}": "assets/logos/harvard-university.png",
    "{{LOGO_2}}": "assets/logos/imperial-college-london.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    # v5 header carries the titlebar QR; the standalone scan section auto-hides.
    "{{HDR_QR_PAPER}}": "assets/qr/paper.png",
    "{{HDR_QR_CODE}}": "",
}
for k, v in SUBS.items():
    if k not in html:
        sys.exit("missing placeholder: " + k)
    html = html.replace(k, v)

# scan-section tokens vary by composed variant (v5 hides the section anyway) — blank any present
for tok in ("{{QR_PAPER}}", "{{QR_CODE}}", "{{URL_PAPER}}", "{{URL_CODE}}",
            "{{URL_PROJECT}}"):
    html = html.replace(tok, "")

# ---- 4b. strip placeholder tokens that only survive inside HTML comments ----
html = re.sub(r"<!--[^>]*?\{\{[A-Z0-9_]+\}\}.*?-->",
              lambda m: re.sub(r"\{\{[A-Z0-9_]+\}\}", "value", m.group(0), flags=re.S),
              html, flags=re.S)

# ---- 5. sanity ----
leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
leftover = [x for x in leftover if x != "{{FIG_MIN_RATIO}}"]
if leftover:
    sys.exit("unreplaced placeholders remain: " + str(leftover))

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
