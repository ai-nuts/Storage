#!/usr/bin/env python3
"""build_poster.py — fill the composed 3col poster.html for NeuPL."""
import re
import sys
from pathlib import Path


def drop_section(doc: str, sec: str) -> str:
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
            depth += 1
            i = o + 4
        else:
            depth -= 1
            i = c + len("</div>")
            if depth == 0:
                while i < len(doc) and doc[i] in " \t\r\n":
                    i += 1
                return doc[:start] + doc[i:]
    return doc


target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    "{{TITLE}}": "NeuPL: Neural Population Learning",
    "{{AUTHORS}}": ("Siqi Liu<sup>1,2</sup>, Luke Marris<sup>1,2</sup>, "
                    "Daniel Hennes<sup>2</sup>, Josh Merel<sup>2</sup>, "
                    "Nicolas Heess<sup>2</sup>, Thore Graepel<sup>1</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> University College London &nbsp;&nbsp; "
                          "<sup>2</sup> DeepMind"),
    "{{VENUE_NAME}}": "ICLR",
    "{{VENUE_YEAR}}": "2022",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "Email: liusiqi@google.com",
    "{{LOGO_1}}": "assets/logos/university-college-london.png",
    "{{LOGO_2}}": "assets/logos/google-deepmind.png",
    "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "", "{{QR_CODE}}": "", "{{URL_PROJECT}}": "",

    # Problem
    "{{PROBLEM}}": ("Learning in strategy games requires a diverse population of policies, "
                    "usually grown by iteratively best-responding to existing ones. "
                    "This recipe collapses under real-world compute budgets."),

    # Motivation
    "{{MOTIVATION_1}}": ("Population size and per-iteration training budget are hand-crafted "
                         "knobs in prior work, fixed before learning even begins."),
    "{{MOTIVATION_2}}": ("NeuPL instead lets the meta-game solver set the <strong>effective "
                         "population size</strong>, sharing perception, memory, and motor "
                         "skills across every policy."),

    # Method
    "{{METHOD_1}}": ("A single network &Pi;<sub>&theta;</sub>(&middot;&thinsp;|&thinsp;o,&thinsp;"
                     "&sigma;<sub>i</sub>) represents <strong>all policies at once</strong>, each "
                     "conditioned on a meta-strategy &sigma;<sub>i</sub> drawn from an interaction "
                     "graph &Sigma;."),
    "{{METHOD_2}}": ("Policies train jointly by RL to best-respond to their assigned opponent "
                     "mixtures; a learned payoff estimator &phi;<sub>&omega;</sub> ties the "
                     "population to its empirical payoff matrix."),
    "{{METHOD_FIGURE}}": "assets/figures/overview.png",
    "{{METHOD_CAPTION}}": ("Self-play, fictitious play, and PSRO-Nash all recovered as interaction "
                           "graphs &Sigma; over a 3-policy population."),
    "{{KEY_EQUATION}}": (r"J_{\sigma_i}=\mathbb{E}_{\sigma_j\sim P(\sigma_i)}\,"
                         r"\mathbb{E}\!\left[\textstyle\sum_t \gamma^t r_t\right]"),
    "{{KEY_EQUATION_NOTE}}": ("Policy i best-responds to opponent mixture &sigma;<sub>i</sub>; the "
                              "interaction graph, not a schedule, decides who trains whom."),

    # Dataset / Benchmark
    "{{DATASET_1}}": ("Validated across three domains of rising complexity: normal-form "
                      "<strong>rock-paper-scissors</strong>, spatiotemporal partially-observed "
                      "<strong>running-with-scissors</strong>, and 2-vs-2 <strong>MuJoCo "
                      "Football</strong>."),
    "{{DATASET_2}}": ("Running-with-scissors exposes only a 4&times;4 first-person view and hides "
                      "the opponent inventory; Football couples continuous motor control with team "
                      "coordination."),

    # Key Results
    "{{BASELINE}}": "cap 4", "{{BASELINE_NUM}}": "4",
    "{{OURS}}": "cap 8", "{{OURS_NUM}}": "8",
    "{{HEADLINE_DELTA}}": ("NeuPL (8 policies) exploits PSRO (8 policies) even when PSRO trains "
                           "with 2&times; the gradient updates per iteration."),
    "{{SECONDARY_FIGURE}}": "assets/figures/figure6.png",
    "{{SECONDARY_CAPTION}}": ("Relative population performance of NeuPL vs PSRO baselines; "
                              "effective population size (dashed) climbs from 5 to 8."),
    "{{KEY_RESULT_CONCLUSION}}": ("Gains coincide with a growing effective population, so improvement "
                                  "comes from discovering genuinely new strategies, not overfitting."),

    # Headline Numbers
    "{{HERO_VAL}}": "2&times;",
    "{{HERO_LABEL}}": "PSRO gradient budget, still exploited",
    "{{HERO_NOTE}}": "NeuPL(8) beats PSRO(8)",
    "{{STAT_2_VAL}}": "5&rarr;8", "{{STAT_2_LBL}}": "effective policies",
    "{{STAT_3_VAL}}": "12", "{{STAT_3_LBL}}": "effective-size plateau",
    "{{STAT_4_VAL}}": "3", "{{STAT_4_LBL}}": "eval domains",

    # Takeaway
    "{{TAKEAWAY}}": ("Hold the whole population in one opponent-conditioned network, let the "
                     "interaction graph decide who trains whom, and skills transfer for free, "
                     "making novel strategies more accessible as the population grows."),

    # Motivation teaser figure
    "{{TEASER_FIGURE}}": "assets/figures/figure4.png",
    "{{TEASER_CAPTION}}": ("Relative population performance and effective neural population size "
                           "rise together through training, saturating near 12."),

    # Ablation (kept filled inside the template comment, ready to uncomment during fill)
    "{{ABLATION_1}}": ("Transferring encoder and memory from a NeuPL network (epoch 1,000) learns "
                       "exploiters to strong Nash mixtures (n=4, n=7) that random-init agents never "
                       "counter."),
    "{{ABLATION_2}}": ("Against an easy n=2 mixture even random-init eventually succeeds, just "
                       "slower; the gap widens sharply against competent opponents. Repeated 5&times;."),
    "{{ABLATION_CONCLUSION}}": ("As the population expands, discovering new strategies becomes "
                                "easier, not harder: transfer is the mechanism."),
}

DROP_SECTIONS = []  # keep dataset-benchmark; ablation stays commented, filled and ready
for sec in DROP_SECTIONS:
    html = drop_section(html, sec)
    html = re.sub(rf'"{re.escape(sec)}"\s*,?\s*', "", html)

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
