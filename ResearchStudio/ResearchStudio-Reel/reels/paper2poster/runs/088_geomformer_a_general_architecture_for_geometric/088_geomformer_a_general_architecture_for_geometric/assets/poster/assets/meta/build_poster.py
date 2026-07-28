#!/usr/bin/env python3
"""Fill GeoMFormer poster.html — reads template from disk, emits only SUBS."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    # ---------- header (v5) ----------
    "{{VENUE_LINK}}": "https://github.com/c-tl/GeoMFormer",
    "{{VENUE_NAME}}": "ICML",
    "{{VENUE_YEAR}}": "2024",
    "{{VENUE_TAG}}": "",
    "{{TITLE}}": "GeoMFormer: A General Architecture for Geometric Molecular Representation Learning",
    "{{AUTHORS}}": ("Tianlang Chen<sup>1</sup>, Shengjie Luo<sup>2</sup>, Di He<sup>2</sup>, "
                    "Shuxin Zheng<sup>3</sup>, Tie-Yan Liu<sup>3</sup>, Liwei Wang<sup>2,4</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> School of EECS, Peking University &nbsp;&nbsp; "
                          "<sup>2</sup> Nat. Key Lab of General AI, Peking University &nbsp;&nbsp; "
                          "<sup>3</sup> Microsoft Research AI4Science &nbsp;&nbsp; "
                          "<sup>4</sup> Center for ML Research, Peking University"),
    "{{CONTACT}}": "Email: luosj@stu.pku.edu.cn",
    "{{LOGO_1}}": "assets/logos/peking-university.png",
    "{{LOGO_2}}": "assets/logos/microsoft-research-ai4science.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{HDR_QR_PAPER}}": "assets/qr/paper.png",
    "{{HDR_QR_CODE}}": "assets/qr/code.png",
    # section QR suppressed (v5 header carries QR)
    "{{QR_PAPER}}": "", "{{QR_CODE}}": "",
    # contribution tokens live in a commented-out block; neutralize
    "{{CONTRIBUTION_1}}": "", "{{CONTRIBUTION_2}}": "", "{{CONTRIBUTION_3}}": "",

    # ---------- Problem (add callout-bar widget) ----------
    "        <p>{{PROBLEM}}</p>":
        ("        <p>Molecular modeling must respect physical law: predictions stay "
         "<strong>invariant</strong> to coordinate rotation &amp; translation for scalars "
         "(energy) and <strong>equivariant</strong> for vectors (forces).</p>\n"
         "        <div class=\"p-callout-bar\">Yet no general framework learns strong invariant "
         "<em>and</em> equivariant representations well at once.</div>"),

    # ---------- Motivation (bullets + callout-bar, drop teaser figure) ----------
    ("        <ul>\n"
     "          <li>{{MOTIVATION_1}}</li>\n"
     "          <li>{{MOTIVATION_2}}</li>\n"
     "        </ul>\n"
     "        <!-- OPTIONAL: half-column Motivation figure. If the spec's Motivation figure line is `**Figure:** none`, REMOVE this entire <figure> block. -->\n"
     "        <figure><img src=\"{{TEASER_FIGURE}}\" alt=\"\"><figcaption>{{TEASER_CAPTION}}</figcaption></figure>"):
        ("        <ul>\n"
         "          <li><strong>Hand-crafted equivariant modules.</strong> Prior geometric nets rely "
         "on costly, specialized operations that scale poorly or sacrifice expressive power.</li>\n"
         "          <li><strong>One model, both jobs.</strong> Applications increasingly need a single "
         "network strong at both invariant and equivariant prediction.</li>\n"
         "        </ul>\n"
         "        <div class=\"p-callout-bar\">We need a general, flexible principle built from standard "
         "components, not one-off heuristic modules.</div>"),

    # ---------- Method (bullets + equation + figure) ----------
    ("        <ul>\n"
     "          <li>{{METHOD_1}}</li>\n"
     "          <li>{{METHOD_2}}</li>\n"
     "          <li>{{METHOD_3}}</li>\n"
     "        </ul>\n"
     "        <figure><img src=\"{{METHOD_FIGURE}}\" alt=\"half\"><figcaption>{{METHOD_CAPTION}}</figcaption></figure>"):
        ("        <ul>\n"
         "          <li><strong>Two parallel streams.</strong> Every atom carries an "
         "<strong>invariant</strong> feature and an <strong>equivariant</strong> 3D feature, each run "
         "through its own standard Transformer stream.</li>\n"
         "          <li><strong>Cross-attention bridge.</strong> Each stream queries the other "
         "(Inv&larr;Equ, Equ&larr;Inv), fusing the two kinds of geometric information &mdash; the key innovation.</li>\n"
         "          <li><strong>Equivariance by construction.</strong> Equivariant attention sums dot "
         "products over the 3D Query/Key, provably preserving equivariance; self-attention + FFN complete each block.</li>\n"
         "        </ul>\n"
         "        <div class=\"p-eq\">\n"
         "          $\\alpha_{ij} = \\sum_{k=1}^{d} {Q^{E}_{[i,:,k]}}^{\\top} K^{E}_{[j,:,k]}$\n"
         "          <span class=\"where\">equivariant attention score, summed over the 3-D Query/Key &mdash; provably equivariant</span>\n"
         "        </div>\n"
         "        <figure><img src=\"assets/figures/figure1.png\" alt=\"half\">"
         "<figcaption>The GeoMFormer block: parallel invariant / equivariant Transformer streams bridged by self- and cross-attention.</figcaption></figure>"),

    # ---------- Dataset / Benchmark (chips) ----------
    ("        <ul>\n"
     "          <li>{{DATASET_1}}</li>\n"
     "          <li>{{DATASET_2}}</li>\n"
     "        </ul>"):
        ("        <ul>\n"
         "          <li>A broad suite stressing <strong>both</strong> invariant (energy, HOMO-LUMO gap) "
         "and equivariant (structure, position, force) prediction.</li>\n"
         "        </ul>\n"
         "        <div class=\"p-chips\">\n"
         "          <span>OC20 &middot; 460K</span><span>PCQM4Mv2 &middot; 3.37M</span><span>Molecule3D &middot; 2.34M</span>\n"
         "          <span class=\"alt\">N-body sim</span><span class=\"alt\">MD17 forces</span>\n"
         "        </div>"),

    # ---------- Key Result (3-col highlight table) ----------
    ("        <table class=\"results\">\n"
     "          <tr><th>Method</th><th>Metric</th></tr>\n"
     "          <tr><td class=\"method\">{{BASELINE}}</td><td>{{BASELINE_NUM}}</td></tr>\n"
     "          <tr class=\"best\"><td class=\"method\">{{OURS}}</td><td>{{OURS_NUM}}</td></tr>\n"
     "        </table>\n"
     "        <div class=\"callout\">{{HEADLINE_DELTA}}</div>\n"
     "        <p class=\"conclusion\">{{KEY_RESULT_CONCLUSION}}</p>"):
        ("        <table class=\"p-table\">\n"
         "          <tr><th>Benchmark (metric &darr;)</th><th>Prev. best</th><th>GeoMFormer</th></tr>\n"
         "          <tr><td>OC20 IS2RE &middot; MAE (eV)</td><td>0.4410</td><td>0.4141</td></tr>\n"
         "          <tr><td>Molecule3D &middot; MAE (rand.)</td><td>0.0301</td><td>0.0252</td></tr>\n"
         "          <tr><td>Molecule3D &middot; MAE (scaf.)</td><td>0.1182</td><td>0.1045</td></tr>\n"
         "          <tr class=\"best\"><td>N-body &middot; MSE</td><td>0.0071</td><td>0.0047</td></tr>\n"
         "        </table>\n"
         "        <div class=\"callout\">New SOTA on OC20, Molecule3D, PCQM4Mv2 &amp; N-body &mdash; all at O(n&sup2;) cost.</div>\n"
         "        <p class=\"conclusion\">A single Transformer wins on both invariant and equivariant tasks at O(n&sup2;) complexity.</p>"),

    # ---------- Ablation (stat-strip) ----------
    ("        <ul>\n"
     "          <li>{{ABLATION_1}}</li>\n"
     "          <li>{{ABLATION_2}}</li>\n"
     "        </ul>\n"
     "        <p class=\"conclusion\">{{ABLATION_CONCLUSION}}</p>"):
        ("        <ul>\n"
         "          <li>Removing the cross-attention bridge degrades every task sharply &mdash; it is the heart of the design.</li>\n"
         "        </ul>\n"
         "        <div class=\"p-stat-strip\">\n"
         "          <div class=\"cell\"><div class=\"v\">+20.8%</div><div class=\"l\">MD17 energy</div></div>\n"
         "          <div class=\"cell\"><div class=\"v\">+60.8%</div><div class=\"l\">MD17 forces</div></div>\n"
         "          <div class=\"cell\"><div class=\"v\">+17.5%</div><div class=\"l\">N-body MSE</div></div>\n"
         "        </div>\n"
         "        <p class=\"conclusion\">Relative gains from adding both cross-attention modules; each of the four attention blocks contributes.</p>"),

    # ---------- Headline Numbers ----------
    "{{HERO_VAL}}": "&minus;33.8%",
    "{{HERO_LABEL}}": "N-body MSE vs prior best",
    "{{HERO_NOTE}}": "0.0071 &rarr; 0.0047",
    "{{STAT_2_VAL}}": "0.0734", "{{STAT_2_LBL}}": "PCQM4Mv2 MAE",
    "{{STAT_3_VAL}}": "&minus;16.3%", "{{STAT_3_LBL}}": "Molecule3D MAE",
    "{{STAT_4_VAL}}": "+60.8%", "{{STAT_4_LBL}}": "MD17 force (abl.)",

    # ---------- Takeaway (callout-primary) ----------
    "        <p>{{TAKEAWAY}}</p>":
        ("        <p>Two standard Transformer streams &mdash; one invariant, one equivariant &mdash; "
         "bridged by cross-attention form a single general architecture that learns both representation "
         "types and beats specialized geometric models across the board.</p>\n"
         "        <div class=\"p-callout-primary\">Many prior geometric models are special cases of "
         "GeoMFormer &mdash; a unifying, scalable design principle.</div>"),
}

missing = [k for k in SUBS if k not in html]
if missing:
    sys.exit("substring(s) not found:\n" + "\n".join(repr(m) for m in missing))
for token, value in SUBS.items():
    html = html.replace(token, value)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
