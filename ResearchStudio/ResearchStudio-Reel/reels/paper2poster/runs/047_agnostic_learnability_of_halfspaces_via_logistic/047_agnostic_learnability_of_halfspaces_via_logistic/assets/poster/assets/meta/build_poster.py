#!/usr/bin/env python3
"""Disk-to-disk poster fill for paper 047 (theory paper, landscape half)."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# ------------------------------------------------------------------ #
# 1. Remove the commented-out Contribution block (carries {{CONTRIBUTION_*}}).
html = re.sub(
    r'\n\s*<!-- ═+\n\s*CONTRIBUTION SECTION.*?═+ -->',
    '', html, flags=re.DOTALL)

# ------------------------------------------------------------------ #
# 2. PROBLEM — prose + P3 callout-bar
problem_old = '''      <div class="section" data-section="problem">
        <h2>Problem <button class="listen-btn" data-section="problem">Listen</button></h2>
        <p>{{PROBLEM}}</p>
      </div>'''
problem_new = '''      <div class="section" data-section="problem">
        <h2>Problem <button class="listen-btn" data-section="problem">Listen</button></h2>
        <p>How well does plain <strong>logistic regression</strong> agnostically learn homogeneous halfspaces? An adversary corrupts an <span class="hi">OPT</span> fraction of labels, and we must compete with the best linear classifier &mdash; whose zero-one risk is exactly OPT.</p>
        <div class="p-callout-bar">Prior work left a wide gap: an $\\widetilde\\Omega(\\mathrm{OPT})$ lower bound for <em>all</em> convex surrogates, versus an $\\widetilde{O}(\\sqrt{\\mathrm{OPT}})$ upper bound for logistic regression.</div>
      </div>'''
assert problem_old in html; html = html.replace(problem_old, problem_new)

# ------------------------------------------------------------------ #
# 3. MOTIVATION — bullets + P17 banner (replaces the absent teaser figure)
mot_fig_old = '''        <!-- OPTIONAL: half-column Motivation figure. If the spec's Motivation figure line is `**Figure:** none`, REMOVE this entire <figure> block. -->
        <figure><img src="{{TEASER_FIGURE}}" alt=""><figcaption>{{TEASER_CAPTION}}</figcaption></figure>'''
mot_banner = '''        <div class="p-banner">
          <div class="tag">Warns</div>
          <div>Ben-David et&nbsp;al. (2012): the logistic-risk minimizer can suffer zero-one risk as bad as $1-\\mathrm{OPT}$ on adversarial distributions.</div>
        </div>'''
assert mot_fig_old in html; html = html.replace(mot_fig_old, mot_banner)
html = html.replace('<li>{{MOTIVATION_1}}</li>',
    '<li>Logistic regression is the <strong>default</strong> classifier in practice, so its agnostic guarantees are far from academic.</li>')
html = html.replace('<li>{{MOTIVATION_2}}</li>',
    '<li>Restricting to <strong>well-behaved</strong> (isotropic log-concave) distributions makes the problem tractable &mdash; yet the exact rate logistic regression attains there stayed open.</li>\n          <li>The rate sat unknown between $\\widetilde{O}(\\mathrm{OPT})$ and $\\widetilde{O}(\\sqrt{\\mathrm{OPT}})$.</li>')

# ------------------------------------------------------------------ #
# 4. METHOD — P8 numbered steps (two-phase algorithm) + P15 equation + figure
method_ul_old = '''        <ul>
          <li>{{METHOD_1}}</li>
          <li>{{METHOD_2}}</li>
          <li>{{METHOD_3}}</li>
        </ul>'''
method_new = '''        <div class="p-eq">
          $\\ell_{\\log}(z)=\\ln(1+e^{-z}) \\qquad \\ell_{h}(z)=\\max\\{-z,0\\}$
          <span class="where">two convex surrogates; minimize the empirical risk $\\widehat{R}_{\\ell}(w)=\\tfrac{1}{n}\\sum_{i}\\ell(y_i\\langle w,x_i\\rangle)$</span>
        </div>
        <div class="p-steps">
          <div class="step"><strong>Phase&nbsp;1 &mdash; Logistic GD.</strong> Projected gradient descent on the logistic risk inside a ball of radius $1/\\sqrt{\\epsilon}$ returns a direction within angle $\\widetilde{O}(\\sqrt{\\mathrm{OPT}}+\\epsilon)$ of the target $\\bar{u}$.</div>
          <div class="step"><strong>Phase&nbsp;2 &mdash; Perceptron.</strong> Projected SGD on the hinge loss (the classical perceptron update), warm-started from Phase&nbsp;1 over a bounded domain $D$, sharpening the angle to $\\widetilde{O}(\\mathrm{OPT})$.</div>
        </div>'''
assert method_ul_old in html; html = html.replace(method_ul_old, method_new)
html = html.replace('{{METHOD_FIGURE}}', 'assets/figures/page4_figure1.png')
html = html.replace('{{METHOD_CAPTION}}',
    'Figure&nbsp;1: the explicit 2-D well-behaved distribution $Q$ (parts $Q_1$&ndash;$Q_4$) that forces the logistic minimizer to $\\sqrt{\\mathrm{OPT}}$ error.')

# ------------------------------------------------------------------ #
# 5. SETTING (was Dataset / Benchmark) — bullets + P10 chips
ds_old = '''      <div class="section" data-section="dataset-benchmark">
        <h2>Dataset / Benchmark <button class="listen-btn" data-section="dataset-benchmark">Listen</button></h2>
        <ul>
          <li>{{DATASET_1}}</li>
          <li>{{DATASET_2}}</li>
        </ul>
      </div>'''
ds_new = '''      <div class="section" data-section="dataset-benchmark">
        <h2>Setting <button class="listen-btn" data-section="dataset-benchmark">Listen</button></h2>
        <ul>
          <li>No empirical datasets &mdash; a learning-theory paper. Positive results hold for every <strong>well-behaved</strong> distribution.</li>
          <li>The lower bound is a concrete counterexample: an explicit $Q$ over $\\mathbb{R}^2\\times\\{-1,+1\\}$ with four parts, valid when $\\mathrm{OPT}\\le 1/100$.</li>
        </ul>
        <div class="p-chips">
          <span>isotropic</span><span>log-concave</span><span>soft-margin</span><span>sub-exponential</span><span>bounded &#8214;x&#8214;&#8804;B</span>
        </div>
      </div>'''
assert ds_old in html; html = html.replace(ds_old, ds_new)

# ------------------------------------------------------------------ #
# 6. KEY RESULTS — 3-column P12 bounds table + delta + conclusion
kr_table_old = '''        <table class="results">
          <tr><th>Method</th><th>Metric</th></tr>
          <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>
          <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>
        </table>'''
kr_table_new = '''        <table class="p-table">
          <tr><th>Method</th><th>0&#8211;1 error</th><th>Assumption</th></tr>
          <tr><td class="method">Logistic regression</td><td>$\\Theta(\\sqrt{\\mathrm{OPT}})$</td><td>well-behaved <em>(tight)</em></td></tr>
          <tr><td class="method">LR + radial-Lipschitz</td><td>$\\widetilde{O}(\\mathrm{OPT})$</td><td>Lipschitz density</td></tr>
          <tr class="best"><td class="method">Two-phase (LR + perceptron)</td><td>$\\widetilde{O}(\\mathrm{OPT})$</td><td>well-behaved only</td></tr>
        </table>'''
assert kr_table_old in html; html = html.replace(kr_table_old, kr_table_new)
html = html.replace('{{HEADLINE_DELTA}}',
    'Matching lower bound $R_{0\\text{-}1}(w^*)\\ge \\sqrt{\\mathrm{OPT}}/(60\\pi)$ &mdash; proving $\\sqrt{\\mathrm{OPT}}$ is <strong>tight</strong> for logistic regression.')
html = html.replace('{{KEY_RESULT_CONCLUSION}}',
    'A single perceptron phase closes the long-standing gap: near-optimal $\\widetilde{O}(\\mathrm{OPT})$ error on every well-behaved distribution.')
# grow Key Result to fill col2: add the two-phase expected-error detail (P2 callout-soft)
kr_conc = '''        <p class="conclusion">A single perceptron phase closes the long-standing gap: near-optimal $\\widetilde{O}(\\mathrm{OPT})$ error on every well-behaved distribution.</p>'''
kr_conc_new = kr_conc + '''
        <div class="p-callout-soft">Two-phase error: $O(\\mathrm{OPT}+\\epsilon)$ (bounded) / $O(\\mathrm{OPT}\\ln\\tfrac{1}{\\mathrm{OPT}}+\\epsilon)$ (sub-exp).</div>'''
assert kr_conc in html; html = html.replace(kr_conc, kr_conc_new)

# ------------------------------------------------------------------ #
# 7. ANALYSIS (ablation-study) — kept in col3 (fills the grow column). Trimmed
#    to fit alongside Headline + Takeaway + Scan.
ab_old = '''      <div class="section" data-section="ablation-study">
        <h2>Ablation Study <button class="listen-btn" data-section="ablation-study">Listen</button></h2>
        <ul>
          <li>{{ABLATION_1}}</li>
          <li>{{ABLATION_2}}</li>
        </ul>
        <p class="conclusion">{{ABLATION_CONCLUSION}}</p>
      </div>'''
ab_new = '''      <div class="section" data-section="ablation-study">
        <h2>Analysis <button class="listen-btn" data-section="ablation-study">Listen</button></h2>
        <div class="p-callout-soft">The versatile argument extends to the <strong>hinge loss</strong>, enabling the perceptron phase.</div>
        <p>The same guarantee also covers general well-behaved distributions.</p>
      </div>'''
assert ab_old in html; html = html.replace(ab_old, ab_new)

# ------------------------------------------------------------------ #
# 8. HEADLINE NUMBERS — hero + 3 supporting tiles
html = html.replace('{{HERO_VAL}}', '&#213;(OPT)')
html = html.replace('{{HERO_LABEL}}', 'Two-phase algorithm error')
html = html.replace('{{HERO_NOTE}}', '')
html = html.replace('{{STAT_2_VAL}}', '&#8730;OPT'); html = html.replace('{{STAT_2_LBL}}', 'LR lower bound (tight)')
html = html.replace('{{STAT_3_VAL}}', '&#213;(d/&#949;&#178;)'); html = html.replace('{{STAT_3_LBL}}', 'sample complexity')
html = html.replace('{{STAT_4_VAL}}', '2'); html = html.replace('{{STAT_4_LBL}}', 'convex steps')

# ------------------------------------------------------------------ #
# 9. TAKEAWAY — prose + P1 callout-primary
tk_old = '''      <div class="section grow" data-section="takeaway">
        <h2>Takeaway <button class="listen-btn" data-section="takeaway">Listen</button></h2>
        <p>{{TAKEAWAY}}</p>
      </div>'''
tk_new = '''      <div class="section grow" data-section="takeaway">
        <h2>Takeaway <button class="listen-btn" data-section="takeaway">Listen</button></h2>
        <div class="p-callout-primary">Logistic regression alone is provably <strong>tight</strong> at $\\sqrt{\\mathrm{OPT}}$; one perceptron step from its solution restores near-optimal $\\widetilde{O}(\\mathrm{OPT})$ error on any well-behaved distribution.</div>
        <p>Radial-Lipschitzness alone already lets logistic regression reach $\\widetilde{O}(\\mathrm{OPT})$.</p>
      </div>'''
assert tk_old in html; html = html.replace(tk_old, tk_new)

# ------------------------------------------------------------------ #
# 10. HEADER (v4) — title / authors / venue / logos / contact
html = html.replace('{{TITLE}}', 'Agnostic Learnability of Halfspaces via Logistic Loss')
html = html.replace('{{AUTHORS}}',
    'Ziwei Ji<sup>1</sup>, Kwangjun Ahn<sup>2</sup>, Pranjal Awasthi<sup>3</sup>, Satyen Kale<sup>3</sup>, Stefani Karp<sup>3,4</sup>')
html = html.replace('{{AUTHOR_LEGEND}}',
    '<sup>1</sup> UIUC &nbsp;&nbsp; <sup>2</sup> MIT &nbsp;&nbsp; <sup>3</sup> Google Research &nbsp;&nbsp; <sup>4</sup> CMU')
html = html.replace('{{VENUE_NAME}}', 'ICML')
html = html.replace('{{VENUE_YEAR}}', '2022')
html = html.replace('{{VENUE_LOGO}}', 'assets/logos/_venue.png')
html = html.replace('{{LOGO_1}}', 'assets/logos/university-of-illinois-urbana-champaign.png')
html = html.replace('{{LOGO_2}}', 'assets/logos/massachusetts-institute-of-technology.png')
html = html.replace('{{LOGO_3}}', 'assets/logos/google.png')
html = html.replace('{{LOGO_4}}', 'assets/logos/carnegie-mellon-university.png')
html = html.replace('{{LOGO_5}}', '')
html = html.replace('{{LOGO_6}}', '')
html = html.replace('{{CONTACT}}', 'Email: ziweiji2@illinois.edu')

# ------------------------------------------------------------------ #
# 11. SCAN-TO-READ (hero) — single paper QR
html = html.replace('{{QR_PAPER}}', 'assets/qr/paper.png')
html = html.replace('{{URL_PAPER}}', 'arxiv.org/abs/2201.13419')

# ------------------------------------------------------------------ #
# 11b. col0 stays Problem + Motivation (Motivation grows). Contribution is
#      dropped (it overlaps Method / Key Result / Headline). Motivation keeps
#      its `grow` from the template.

# ------------------------------------------------------------------ #
# 11c. Continuous lever: col3 (4 painted-ending sections in a narrow column)
#      packs tight. Trim ONLY its inter-section gap so the painted widgets
#      sit within padding — no content change.
col3_gap = ('<style>'
            '.col:has([data-section="ablation-study"]){gap:8pt;}'
            '.col:has([data-section="ablation-study"]) [data-section="headline-numbers"] .headline-hero{margin-bottom:14pt;}'
            '</style>\n</head>')
assert '</head>' in html; html = html.replace('</head>', col3_gap, 1)

# ------------------------------------------------------------------ #
# leftover check
leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")
target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
