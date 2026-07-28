#!/usr/bin/env python3
"""Fill RetoMaton poster.html (full layout) disk-to-disk."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

BLOCKS = [
    # Problem body
    ("""        <p>{{PROBLEM}}</p>""",
     """        <p>Retrieval-based LMs improve quality by searching an external datastore, but that <strong>nearest-neighbor search runs as often as every time step</strong> &mdash; the dominant computational cost at inference.</p>
        <div class="p-callout-bar">The search is far slower than the LM's forward pass, blocking retrieval LMs from deployment despite their accuracy, domain-adaptability, and provenance.</div>"""),

    # Motivation: richer bullets (fills grow col0) + callout; DROP teaser figure
    ("""        <ul>
          <li>{{MOTIVATION_1}}</li>
          <li>{{MOTIVATION_2}}</li>
        </ul>
        <!-- OPTIONAL: half-column Motivation figure. If the spec's Motivation figure line is `**Figure:** none`, REMOVE this entire <figure> block. -->
        <figure><img src="{{TEASER_FIGURE}}" alt=""><figcaption>{{TEASER_CAPTION}}</figcaption></figure>""",
     """        <ul>
          <li>kNN-LM treats the datastore as a <strong>flat list</strong> and searches it token by token, ignoring that consecutive retrieved entries are highly correlated in time.</li>
          <li>Nearby key vectors tend to be followed by the <em>same</em> token, yet a flat search rediscovers those same neighbors from scratch at every step.</li>
          <li>Prior search-saving work (AdaptRet) skips searches but backs off to the base LM alone &mdash; discarding the retrieval signal exactly when it helps most.</li>
        </ul>
        <div class="p-callout-soft">If a retrieved entry helps now, the entry that <em>followed</em> it in the text is very likely useful next &mdash; structure a flat datastore throws away.</div>"""),

    # Method: 2 compact steps + equation (keeps the wide figure's height budget)
    ("""          <ul>
            <li>{{METHOD_1}}</li>
            <li>{{METHOD_2}}</li>
            <li>{{METHOD_3}}</li>
          </ul>""",
     """          <div class="p-steps">
            <div class="step"><strong>Build:</strong> store each entry as <em>(key, value, pointer)</em> &mdash; pointer to its successor in the corpus &mdash; and cluster close keys into states that share pointers.</div>
            <div class="step"><strong>Decode:</strong> traverse the automaton alongside the LM via near-free matching-value pointers; launch a fresh kNN search only when valid transitions fall below threshold &tau;, then restart.</div>
          </div>
          <div class="p-eq">$$p(w \\mid c, S) = \\lambda\\, p_{\\text{auto}}(w \\mid c, S) + (1-\\lambda)\\, p_{\\text{LM}}(w \\mid c)$$<span class="where">Automaton distribution interpolated with the base LM; weights from key&ndash;hidden-state distances.</span></div>"""),

    # Dataset: compact bullets + chips
    ("""          <ul>
            <li>{{DATASET_1}}</li>
            <li>{{DATASET_2}}</li>
          </ul>""",
     """          <ul>
            <li><strong>In-domain:</strong> WikiText-103 &mdash; 103M tokens, 247M-param LM; 103M-entry datastore &rarr; 1M states.</li>
            <li><strong>Adaptation:</strong> Law-MT (English) &mdash; 19M tokens, 656M-param LM; 19M entries &rarr; 200K states.</li>
          </ul>
          <div class="p-chips"><span>WikiText-103</span><span>Law-MT</span><span class="muted">kNN-LM</span><span class="muted">AdaptRet</span></div>"""),

    # Key Results: 3-col compact
    ("""          <table class="results">
            <tr><th>Method</th><th>Metric</th></tr>
            <tr><td class="method">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>
            <tr class="best"><td class="method">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>
          </table>
          <div class="callout">{{HEADLINE_DELTA}}</div>
          <p class="conclusion">{{KEY_RESULT_CONCLUSION}}</p>""",
     """          <table class="results">
            <tr><th>Perplexity (FoSS=0)</th><th>WikiText-103</th><th>Law-MT*</th></tr>
            <tr><td class="method">kNN-LM</td><td>16.65</td><td>7.93</td></tr>
            <tr><td class="method">AdaptRet</td><td>16.35</td><td>7.81</td></tr>
            <tr class="best"><td class="method">RetoMaton</td><td>16.08</td><td>7.10</td></tr>
          </table>
          <div class="callout">Matches kNN-LM perplexity while skipping <strong>81%</strong> of searches; &minus;17.5% perplexity on fine-tuned Law-MT (8.61 &rarr; 7.10).</div>
          <p class="conclusion">RetoMaton wins at every budget and barely degrades as searches are saved, while kNN-LM's perplexity rises sharply. <span style="color:var(--muted)">*fine-tuned LM.</span></p>"""),

    # Ablation: table
    ("""        <ul>
          <li>{{ABLATION_1}}</li>
          <li>{{ABLATION_2}}</li>
        </ul>
        <p class="conclusion">{{ABLATION_CONCLUSION}}</p>""",
     """        <table class="p-table">
          <tr><th>WikiText-103</th><th>PPL (FoSS=0)</th><th>Saved</th></tr>
          <tr><td>Pointers only</td><td>16.12</td><td>&gt;60%</td></tr>
          <tr class="best"><td>+ Clustering (full)</td><td>16.08</td><td>81%</td></tr>
        </table>
        <p class="conclusion">Pointers drive most of the gain at low FoSS; clustering pays off at high FoSS (&ge;0.7), enabling longer search-free runs.</p>"""),

    # Takeaway body
    ("""        <p>{{TAKEAWAY}}</p>""",
     """        <p>Turning a retrieval datastore into a <strong>pointer-and-cluster automaton</strong> lets an LM reuse retrieval across time steps, skipping most costly nearest-neighbor searches while matching or beating perplexity.</p>
        <div class="p-callout-primary">Unsupervised, model-agnostic, cross-domain &mdash; it unifies token, chunk, and sequence retrieval in one dynamic mechanism.</div>"""),
]

for old, new in BLOCKS:
    if old not in html:
        sys.exit(f"BLOCK anchor not found:\n{old[:160]}")
    html = html.replace(old, new)

SUBS = {
    "{{TITLE}}": "Neuro-Symbolic Language Modeling with Automaton-augmented Retrieval",
    "{{AUTHORS}}": ("Uri Alon<sup>1</sup>, Frank F. Xu<sup>1</sup>, Junxian He<sup>1</sup>, "
                    "Sudipta Sengupta<sup>2</sup>, Dan Roth<sup>3</sup>, Graham Neubig<sup>1</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> Carnegie Mellon University &nbsp;&nbsp; "
                          "<sup>2</sup> Amazon AWS &nbsp;&nbsp; <sup>3</sup> AWS AI Labs"),
    "{{CONTACT}}": "Email: ualon@cs.cmu.edu",
    "{{VENUE_NAME}}": "ICML",
    "{{VENUE_YEAR}}": "2022",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{LOGO_1}}": "assets/logos/carnegie-mellon-university.png",
    "{{LOGO_2}}": "assets/logos/amazon-aws.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",
    "{{URL_PROJECT}}": "",
    "{{METHOD_FIGURE}}": "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": ("RetoMaton at inference: parallel automaton traversals reuse datastore entries via saved "
                           "pointers, avoiding a full kNN search at most decoding steps."),
    "{{HERO_VAL}}": "83%",
    "{{HERO_LABEL}}": "kNN searches saved, no perplexity loss",
    "{{HERO_NOTE}}": "or up to 1.85 lower perplexity if the budget is kept",
    "{{STAT_2_VAL}}": "81%", "{{STAT_2_LBL}}": "searches saved &middot; WikiText-103",
    "{{STAT_3_VAL}}": "16.08", "{{STAT_3_LBL}}": "PPL vs 16.65 kNN-LM",
    "{{STAT_4_VAL}}": "7.10", "{{STAT_4_LBL}}": "Law-MT PPL, &minus;17.5%",
    "{{CONTRIBUTION_1}}": "", "{{CONTRIBUTION_2}}": "", "{{CONTRIBUTION_3}}": "",
}
missing = [k for k in SUBS if k not in html]
if missing:
    sys.exit(f"token(s) not in template: {missing}")
for k, v in SUBS.items():
    html = html.replace(k, v)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
