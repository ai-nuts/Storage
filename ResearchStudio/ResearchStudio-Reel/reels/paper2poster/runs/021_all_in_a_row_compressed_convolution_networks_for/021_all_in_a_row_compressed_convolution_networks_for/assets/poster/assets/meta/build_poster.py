#!/usr/bin/env python3
import re, sys
from pathlib import Path

def drop_section(doc, sec):
    m = re.search(rf'<div\b[^>]*\bdata-section="{re.escape(sec)}"', doc)
    if not m: return doc
    start = doc.rfind("<div", 0, m.end())
    i, depth = start, 0
    while i < len(doc):
        o, c = doc.find("<div", i), doc.find("</div>", i)
        if c == -1: return doc
        if o != -1 and o < c:
            depth += 1; i = o + 4
        else:
            depth -= 1; i = c + len("</div>")
            if depth == 0:
                while i < len(doc) and doc[i] in " \t\r\n": i += 1
                return doc[:start] + doc[i:]
    return doc

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
  "{{TITLE}}": "All in a Row: Compressed Convolution Networks for Graphs",
  "{{AUTHORS}}": ("Junshu Sun<sup>1,2</sup>, Shuhui Wang<sup>1,3&dagger;</sup>, "
                  "Xinzhe Han<sup>1,2</sup>, Zhe Xue<sup>4</sup>, Qingming Huang<sup>1,2,3</sup>"),
  "{{AUTHOR_LEGEND}}": ("<sup>1</sup> Key Lab of Intelligent Information Processing, ICT, CAS "
                        "&nbsp;&nbsp; <sup>2</sup> UCAS &nbsp;&nbsp; <sup>3</sup> Peng Cheng Laboratory "
                        "&nbsp;&nbsp; <sup>4</sup> Beijing Key Lab of Intelligent Telecom Software &amp; Multimedia, BUPT"),
  "{{VENUE_NAME}}": "ICML",
  "{{VENUE_YEAR}}": "2023",
  "{{VENUE_LOGO}}": "assets/logos/_venue.png",
  "{{CONTACT}}": "Email: wangshuhui@ict.ac.cn",
  "{{LOGO_1}}": "assets/logos/key-laboratory-of-intelligent-information-processing-institute-of-computing-technology-chinese-academy-of-sciences.png",
  "{{LOGO_2}}": "assets/logos/university-of-chinese-academy-of-sciences.png",
  "{{LOGO_3}}": "assets/logos/peng-cheng-laboratory.png",
  "{{LOGO_4}}": "assets/logos/beijing-key-laboratory-of-intelligent-telecommunication-software-and-multimedia-school-of-computer-science-beijing-university-of-posts-and-telecommunications.png",
  "{{LOGO_5}}": "", "{{LOGO_6}}": "",
  "{{QR_PAPER}}": "", "{{QR_CODE}}": "",

  # Problem
  "{{PROBLEM}}": ("Convolutional GNNs built on graph polynomials are <strong>weakly expressive</strong> "
                  "under a small parameter budget, and cannot learn <strong>hierarchical representations</strong> "
                  "on their own — they need bolt-on node clustering or node-drop pooling."),
  # Motivation
  "{{MOTIVATION_1}}": ("Convolution is <strong>order-sensitive</strong>, yet GNNs must be "
                       "<strong>permutation-invariant</strong> — and prior graph regularizers are decoupled "
                       "from the convolution, so they can't be tuned per task."),
  "{{MOTIVATION_2}}": ("Earlier node-sequence-selection schemes fix an ordering independent of the objective, "
                       "producing fixed, less-informative regularized graphs."),
  # Method
  "{{METHOD_1}}": ("<strong>Permutation generation</strong> regresses each node position with a "
                   "Laplacian-smoothed MLP, then turns positions into a relaxed, differentiable permutation "
                   "matrix — lining all nodes up in a row while staying permutation-invariant."),
  "{{METHOD_2}}": ("<strong>Diagonal convolution</strong> slides one kernel along the diagonal of the permuted "
                   "node- and edge-feature matrices; <strong>compressed pooling</strong> and transposed "
                   "convolution build and invert the hierarchy for graph- and node-level tasks."),
  "{{METHOD_FIGURE}}": "assets/figures/page3_figure1.png",
  "{{METHOD_CAPTION}}": ("CoCN pipeline: permute nodes into a row, then slide a diagonal convolution across the "
                         "permuted node- and edge-feature matrices; off-diagonal features (twill) are learned in later layers."),
  # Dataset
  "{{DATASET_1}}": ("<strong>Graph classification:</strong> six TU datasets — MUTAG, PROTEINS, NCI1, "
                    "COLLAB, IMDB-BINARY, IMDB-MULTI (10-fold CV)."),
  "{{DATASET_2}}": ("<strong>Node classification:</strong> six heterophilic sets — Chameleon, Squirrel, "
                    "Cornell, Texas, Wisconsin, Actor; plus three large graphs (questions, amazon-ratings, genius) "
                    "with mini-batch training."),
  # Key results
  "{{BASELINE}}": "LINKX (prior best)", "{{BASELINE_NUM}}": "61.81%",
  "{{OURS}}": "CoCN (ours)", "{{OURS_NUM}}": "72.95%",
  "{{HEADLINE_DELTA}}": "Squirrel: 72.95% vs 61.81% (LINKX) — +11.1 pts",
  "{{KEY_RESULT_CONCLUSION}}": ("Best average rank 1.83 across six node benchmarks and wins on five of six graph "
                                "datasets; gains hold on de-duplicated Chameleon/Squirrel, so they are not leakage."),
  "{{SECONDARY_FIGURE}}": "assets/figures/page9_figure5_fig5.png",
  "{{SECONDARY_CAPTION}}": ("Accuracy rises steadily with more learnable permutations (MUTAG, Chameleon, Cornell, Wisconsin)."),
  # Headline numbers
  "{{HERO_VAL}}": "1.83",
  "{{HERO_LABEL}}": "Avg rank · 6 node-classification datasets",
  "{{HERO_NOTE}}": "Best of all baselines",
  "{{STAT_2_VAL}}": "72.95%", "{{STAT_2_LBL}}": "Squirrel accuracy",
  "{{STAT_3_VAL}}": "86.15%", "{{STAT_3_LBL}}": "COLLAB accuracy",
  "{{STAT_4_VAL}}": "O(n²)", "{{STAT_4_LBL}}": "perm. cost, was O(n!)",
  # Takeaway
  "{{TAKEAWAY}}": ("Learn a task-specific, differentiable permutation that lines all graph nodes up in a row, and "
                   "standard CNN-style diagonal convolution and hierarchical pooling apply directly to graphs — "
                   "reaching state-of-the-art node and graph classification."),
  # teaser
  # tokens living inside HTML comments (ablation block, equation example) — neutralize
  "{{KEY_EQUATION}}": "", "{{KEY_EQUATION_NOTE}}": "",
  "{{ABLATION_1}}": "", "{{ABLATION_2}}": "", "{{ABLATION_CONCLUSION}}": "",
  "{{TEASER_FIGURE}}": "assets/figures/page8_figure4.png",
  "{{TEASER_CAPTION}}": ("Learned permutations place connected / similar nodes in adjacent positions "
                         "(permuted adjacency, top; feature similarity, bottom; varying smoothness t)."),
}

for token, value in SUBS.items():
    html = html.replace(token, value)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
