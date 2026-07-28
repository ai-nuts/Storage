#!/usr/bin/env python3
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    # titlebar / metadata
    "{{TITLE}}": "Bisimulation Makes Analogies in Goal-Conditioned Reinforcement Learning",
    "{{AUTHORS}}": "Philippe Hansen-Estruch<sup>1</sup>, Amy Zhang<sup>1,2</sup>, Ashvin Nair<sup>1</sup>, Patrick Yin<sup>1</sup>, Sergey Levine<sup>1</sup>",
    "{{AUTHOR_LEGEND}}": "<sup>1</sup> University of California, Berkeley &nbsp;&nbsp; <sup>2</sup> Meta AI Research",
    "{{CONTACT}}": "Email: hansenpmeche@berkeley.edu",
    "{{VENUE_NAME}}": "ICML",
    "{{VENUE_YEAR}}": "2022",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{LOGO_1}}": "assets/logos/university-of-california-berkeley.png",
    "{{LOGO_2}}": "assets/logos/meta-ai-research.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",

    # ── Problem ──
    "{{PROBLEM}}": "Goal-conditioned RL assumes the agent is handed the <strong>exact goal configuration</strong> &mdash; yet the precise goal state is usually unknown before a task is even attempted.",

    # ── Motivation ──
    "{{MOTIVATION_1}}": "Humans solve whole <strong>families of tasks</strong> (dicing any vegetable) because their goal representation is <strong>invariant</strong> to irrelevant details and <strong>equivariant</strong> to what differs.",
    "{{MOTIVATION_2}}": "Prior bisimulation methods made a representation robust to distractors for a <strong>single task</strong> &mdash; not transferable across analogous goals.",
    "{{TEASER_FIGURE}}": "assets/figures/figure1.png",
    "{{TEASER_CAPTION}}": "Analogous tasks: dicing carrots vs. radishes share the same skill and the same functional change from start to goal.",

    # ── Method ──
    "{{METHOD_1}}": "Learn two encoders jointly: a <strong>state-goal encoder &phi;</strong> whose &#8467;<sub>1</sub> distance matches an on-policy <strong>goal-conditioned bisimulation metric</strong>, and a Siamese <strong>state encoder &psi;</strong>.",
    "{{METHOD_2}}": "Train &psi; so that &psi;(g) &minus; &psi;(s) = &phi;(s,g). At test time, add an analogous pair &mdash; <strong>&psi;(s) + &phi;(s<sub>a</sub>,g<sub>a</sub>)</strong> &mdash; and take the nearest neighbour in &psi; space as the inferred goal.",
    "{{METHOD_FIGURE}}": "assets/figures/figure3.png",
    "{{METHOD_CAPTION}}": "Representation learning in GCB: a Siamese state encoder &psi; and a state-goal encoder &phi;, trained so goals are composable in latent space.",
    "{{KEY_EQUATION}}": "\\psi(g)-\\psi(s)=\\phi(s,g)",
    "{{KEY_EQUATION_NOTE}}": "composability identity",

    # ── Dataset / Benchmark ──
    "{{DATASET_1}}": "PyBullet simulated manipulation: randomly generated workspaces built from <strong>84 object geometries</strong>, spanning Drawer, Button-and-Drawer (BD), and Analogy tasks.",
    "{{DATASET_2}}": "Every task is also run with added <strong>Video Distractors (VD)</strong>; success is measured against the true goal over <strong>5 seeds</strong> in an offline RL (IQL) setting.",

    # ── Key Results ──
    "{{BASELINE}}": "CPV (next best)",
    "{{BASELINE_NUM}}": "0.176",
    "{{OURS}}": "GCB (ours)",
    "{{OURS_NUM}}": "0.403",
    "{{HEADLINE_DELTA}}": "Analogy task: 2.3&times; the next-best baseline &middot; best on 5 / 6 settings",
    "{{SECONDARY_FIGURE}}": "assets/figures/figure4.png",
    "{{SECONDARY_CAPTION}}": "Analogy arithmetic: &psi;(s) + &phi;(s<sub>a</sub>,g<sub>a</sub>) composes a goal; the rightmost frame is its nearest neighbour in &psi; space.",
    "{{KEY_RESULT_CONCLUSION}}": "GCB is the only representation that infers goals from an analogy, and it isolates task-relevant structure even under distractors.",

    # ── Headline Numbers ──
    "{{HERO_VAL}}": "0.403",
    "{{HERO_LABEL}}": "Analogy success (GCB)",
    "{{HERO_NOTE}}": "2.3&times; the next-best baseline (0.176)",
    "{{STAT_2_VAL}}": "0.448", "{{STAT_2_LBL}}": "Drawer + VD",
    "{{STAT_3_VAL}}": "0.322", "{{STAT_3_LBL}}": "BD + VD",
    "{{STAT_4_VAL}}": "5 / 6", "{{STAT_4_LBL}}": "settings won",

    # ── Ablation (kept in commented block — filled to satisfy leftover check) ──
    "{{ABLATION_1}}": "Adding the grounding term &phi;(g<sub>i</sub>,g<sub>i</sub>) as a normalizing constant in &psi;'s objective improves performance.",
    "{{ABLATION_2}}": "An &#8467;<sub>1</sub> metric loss for &phi; outperforms &#8467;<sub>2</sub>; latent dimension (32&ndash;512) barely affects control.",
    "{{ABLATION_CONCLUSION}}": "The grounded &#8467;<sub>1</sub> objective is the key design choice; the method is insensitive to latent size.",

    # ── Takeaway ──
    "{{TAKEAWAY}}": "Treating bisimulation as an equivalence over <strong>tasks</strong>, not just states, gives a representation where analogous tasks line up &mdash; so goals become composable by simple <strong>latent arithmetic</strong> and skills generalize to new, unseen goals.",
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
