#!/usr/bin/env python3
"""Fill lean placeholders in poster.html (3col DDT poster). Disk-to-disk."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

AUTHORS = (
    'Xiong-Hui Chen<sup>1,2,*</sup>, Junyin Ye<sup>1,2,*</sup>, Hang Zhao<sup>3,2</sup>, '
    'Yi-Chen Li<sup>1,2</sup>, Xu-Hui Liu<sup>1,2</sup>, Haoran Shi<sup>2</sup>, '
    'Yu-Yan Xu<sup>2</sup>, Zhihao Ye<sup>1,2</sup>, Si-Hang Yang<sup>1,2</sup>, '
    'Yang Yu<sup>1,2,&dagger;</sup>, Anqi Huang<sup>4,2</sup>, Kai Xu<sup>3</sup>, '
    'Zongzhang Zhang<sup>1</sup>'
)
LEGEND = (
    '<sup>1</sup> Nanjing University &nbsp;&nbsp; '
    '<sup>2</sup> Polixir Technologies &nbsp;&nbsp; '
    '<sup>3</sup> National University of Defense Technology &nbsp;&nbsp; '
    '<sup>4</sup> Nanjing University of Science and Technology'
)

SUBS = {
    "{{TITLE}}": "Deep Demonstration Tracing: Learning a Generalizable Imitator Policy from a Single Demonstration",
    "{{AUTHORS}}": AUTHORS,
    "{{AUTHOR_LEGEND}}": LEGEND,
    "{{VENUE_NAME}}": "ICML",
    "{{VENUE_YEAR}}": "2024",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "Email: yuy@nju.edu.cn",
    "{{LOGO_1}}": "assets/logos/nanjing-university.png",
    "{{LOGO_2}}": "assets/logos/national-university-of-defense-technology.png",
    "{{LOGO_3}}": "assets/logos/nanjing-university-of-science-and-technology.png",
    "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "", "{{QR_CODE}}": "",

    # Problem
    "{{PROBLEM}}": ("One-shot imitation learning (OSIL) trains an agent to perform a task from a "
                    "single demonstration, but existing methods assume deployment closely resembles "
                    "demonstration collection and break down when unforeseen changes occur."),

    # Motivation
    "{{MOTIVATION_1}}": ("A human following a demonstrated route detours around an unexpected obstacle, "
                         "then rejoins the path &mdash; agents need this adaptive <strong>tracing</strong>, "
                         "not blind replay."),
    "{{MOTIVATION_2}}": ("Prior OSIL embeds a demonstration as a free context vector and clones actions, "
                         "with no guarantee of sensible behavior in states the demo never showed."),
    "{{TEASER_FIGURE}}": "assets/figures/page3_figure2.png",
    "{{TEASER_CAPTION}}": ("Humans handle OSIL under unforeseen change: detour around a temporarily parked "
                           "truck, then trace back to the expert path."),

    # Method (bullets replaced by p-steps in a later edit; keep placeholders inert)
    "{{METHOD_1}}": ("<strong>Demonstration transformer:</strong> the current state is the query; expert "
                     "state-action pairs are keys &amp; values."),
    "{{METHOD_2}}": ("Trained as context-based <strong>meta-RL</strong> with a stationary OSIL reward, "
                     "optimized by Soft Actor-Critic &mdash; not behavior cloning."),
    "{{METHOD_3}}": "",
    "{{METHOD_FIGURE}}": "assets/figures/page4_figure3.png",
    "{{METHOD_CAPTION}}": ("Demonstration transformer: the query state attends over expert state-action pairs "
                           "to identify &rarr; analyze &rarr; trace."),

    # Contribution (commented-out block in half template -> inert)
    "{{CONTRIBUTION_1}}": "", "{{CONTRIBUTION_2}}": "", "{{CONTRIBUTION_3}}": "",

    # Ablation Study (real data; kept in half col4)
    "{{ABLATION_1}}": ("Swapping the demonstration transformer for a standard transformer significantly "
                       "lowers asymptotic performance."),
    "{{ABLATION_2}}": ("Removing the OSIL reward (learning only from the sparse ending reward) sharply "
                       "reduces learning efficiency."),
    "{{ABLATION_CONCLUSION}}": ("Both the tailored architecture and the dense OSIL reward are essential "
                                "&mdash; each plays a distinct, necessary role."),

    # Dataset / Benchmark (VPAM is a first-class contribution)
    "{{DATASET_1}}": ("<strong>VPAM</strong> (Valet Parking Assist in Maze): a point agent navigates "
                      "start&rarr;target from only local 8-ray &times; 5-step views, with random obstacles "
                      "absent from the demonstration."),
    "{{DATASET_2}}": ("8 tasks vary single/multi-map, obstacle presence, and coordinate availability; DDT is "
                      "also tested on Meta-World, Reacher/Pusher, and MuJoCo manipulation."),

    # Key Results (2-col results table replaced by 4-col in a later edit)
    "{{BASELINE}}": "DCRL (best baseline)",
    "{{BASELINE_NUM}}": "0.57",
    "{{OURS}}": "DDT (ours)",
    "{{OURS_NUM}}": "0.73",
    "{{HEADLINE_DELTA}}": "+0.16 success under unforeseen obstacles vs. the best baseline",
    "{{KEY_RESULT_CONCLUSION}}": ("DDT leads in every setting and degrades only &minus;15% from train to "
                                  "unforeseen obstacles, vs. &minus;20/&minus;33/&minus;52% for baselines."),

    # Headline Numbers
    "{{HERO_VAL}}": "0.73",
    "{{HERO_LABEL}}": "Success &middot; Unforeseen Obstacles",
    "{{HERO_NOTE}}": "best baseline only 0.57",
    "{{STAT_2_VAL}}": "&minus;15%",
    "{{STAT_2_LBL}}": "drop Train&rarr;Obstacle",
    "{{STAT_3_VAL}}": "0.61",
    "{{STAT_3_LBL}}": "Meta-World unseen demos",
    "{{STAT_4_VAL}}": "~2&times;",
    "{{STAT_4_LBL}}": "gain from scaling params",

    # Takeaway
    "{{TAKEAWAY}}": ("By teaching an imitator to adaptively trace a single demonstration through a "
                     "purpose-built transformer trained with meta-RL, DDT achieves robust one-shot imitation "
                     "that survives unforeseen environmental changes where prior methods collapse."),
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
