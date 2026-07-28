#!/usr/bin/env python3
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    # titlebar / metadata
    "{{TITLE}}": "How Do Nonlinear Transformers Learn and Generalize in In-Context Learning?",
    "{{AUTHORS}}": ("Hongkang Li<sup>1</sup>, Meng Wang<sup>1</sup>, Songtao Lu<sup>2</sup>, "
                    "Xiaodong Cui<sup>2</sup>, Pin-Yu Chen<sup>2</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> Rensselaer Polytechnic Institute &nbsp;&nbsp; "
                          "<sup>2</sup> IBM Thomas J. Watson Research Center"),
    "{{VENUE_NAME}}": "ICML",
    "{{VENUE_YEAR}}": "2024",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "Email: lih35@rpi.edu",
    "{{LOGO_1}}": "assets/logos/rensselaer-polytechnic-institute.png",
    "{{LOGO_2}}": "assets/logos/ibm-thomas-j-watson-research-center.jpg",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{URL_PAPER}}": "arxiv.org/abs/2402.15607",

    # Problem (col1)
    "{{PROBLEM}}": ("In-context learning (ICL) lets a pretrained Transformer solve brand-new tasks from a "
                    "handful of prompt examples, with <strong>no fine-tuning</strong>. Yet <strong>why training "
                    "yields ICL</strong> and <strong>how far it generalizes</strong> stay largely unknown: the "
                    "<span class=\"hi\">softmax self-attention</span> and <span class=\"hi\">ReLU MLP</span> make "
                    "the training objective nonconvex and resistant to existing analysis."),

    # Motivation (col1) + figure4
    "{{MOTIVATION_1}}": ("Prior ICL theory <strong>drops the hard parts</strong> — it removes nonlinear "
                         "attention or uses a linear MLP, and studies only linear regression."),
    "{{MOTIVATION_2}}": ("None explain <strong>training under distribution shift</strong>, nor how "
                         "<strong>model pruning</strong> (routinely used to cut LLM inference cost) affects ICL."),
    "{{TEASER_FIGURE}}": "assets/figures/figure4.png",
    "{{TEASER_CAPTION}}": ("ICL vs. logistic regression, SVM, and k-NN: in-context learning is the most "
                           "sample-efficient classifier, filtering irrelevant data and resisting label noise."),

    # Contribution (col1, commented block — prepared)
    "{{CONTRIBUTION_1}}": ("<strong>First</strong> training-dynamics analysis of a fully nonlinear (softmax + "
                           "ReLU) Transformer, with provable in- and out-of-domain ICL generalization."),
    "{{CONTRIBUTION_2}}": ("Quantifies the required data, iterations, and context length, and explains the "
                           "internal attention + MLP mechanism of the trained model."),
    "{{CONTRIBUTION_3}}": ("<strong>First</strong> theoretical analysis of magnitude-based pruning for "
                           "in-context learning."),

    # Method (col2) + figure1 + (equation & figure2 added via Edit)
    "{{METHOD_1}}": ("A <strong>single-head, one-layer Transformer</strong> — softmax self-attention plus a "
                     "two-layer <strong>ReLU MLP</strong> — is trained by minimizing hinge loss over prompts "
                     "drawn from a subset of binary classification tasks."),
    "{{METHOD_2}}": ("Each input carries label-deciding <span class=\"hi\">IDR patterns</span> plus irrelevant "
                     "patterns; we follow the <strong>gradient-descent trajectory</strong> of the attention and "
                     "MLP weights and test both in-domain and out-of-domain."),
    "{{METHOD_3}}": ("Two quantities drive every guarantee: <strong>α</strong>, the fraction of context sharing "
                     "the query's IDR pattern, and <strong>β</strong>, the norm of the relevant patterns."),
    "{{METHOD_FIGURE}}": "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": ("Trained-model mechanism: attention concentrates on context tokens sharing the "
                           "query's IDR pattern (score 0.8); the ReLU MLP's large-magnitude neurons then "
                           "promote the matching label."),

    # Dataset / Benchmark (col3) — converted to chips via Edit
    "{{DATASET_1}}": "placeholder-dataset-1",
    "{{DATASET_2}}": "placeholder-dataset-2",

    # Key Result (col3) — table replaced + figure3 added via Edit
    "{{BASELINE}}": "b", "{{BASELINE_NUM}}": "b",
    "{{OURS}}": "o", "{{OURS_NUM}}": "o",
    "{{HEADLINE_DELTA}}": ("Out-of-domain error drops <strong>below 0.01</strong> the moment combination "
                           "strength <strong>S₁ ≥ 1</strong> — provable generalization to shifted tasks."),
    "{{KEY_RESULT_CONCLUSION}}": ("One trained model generalizes both in-domain and to distribution-shifted tasks "
                                  "whose relevant patterns are linear combinations of the training ones."),

    # Ablation Study (col4, commented block — prepared)
    "{{ABLATION_1}}": ("Magnitude-based pruning of up to <strong>~15%</strong> of W<sub>O</sub> neurons leaves "
                       "out-of-domain accuracy intact; pruning large-magnitude neurons raises error ≥ Ω(R)."),
    "{{ABLATION_2}}": ("Required context length scales as <strong>α<sup>−1</sup></strong> and iterations / "
                       "samples as <strong>α<sup>−2/3</sup></strong> — richer relevant context converges faster."),
    "{{ABLATION_CONCLUSION}}": ("Only large-magnitude neurons carry the ICL signal, so magnitude-based pruning "
                                "is essentially free — a principled reason it preserves in-context learning."),

    # Headline Numbers (col4)
    "{{HERO_VAL}}": "~15%",
    "{{HERO_LABEL}}": "Wₒ neurons prunable",
    "{{HERO_NOTE}}": "near-lossless ICL",
    "{{STAT_2_VAL}}": "α<sup>−2/3</sup>", "{{STAT_2_LBL}}": "iters &amp; samples scale",
    "{{STAT_3_VAL}}": "α<sup>−1</sup>", "{{STAT_3_LBL}}": "context length scales",
    "{{STAT_4_VAL}}": "&lt;0.01", "{{STAT_4_LBL}}": "OOD error, S₁≥1",

    # Takeaway (col4)
    "{{TAKEAWAY}}": ("A one-layer Transformer with genuinely nonlinear attention and MLP can be "
                     "<strong>provably trained</strong> to perform ICL that generalizes in-domain and under "
                     "distribution shift — with training cost set by the fraction of relevant context, and its "
                     "<span class=\"hi\">low-magnitude MLP neurons pruned almost for free</span>."),
}

missing = [k for k in SUBS if k not in html]
if missing:
    sys.exit(f"placeholder(s) not in template: {missing}")
for token, value in SUBS.items():
    html = html.replace(token, value)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
