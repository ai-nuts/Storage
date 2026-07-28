#!/usr/bin/env python3
"""Fill leaf placeholders in the composed poster.html. Widgets injected via Edits after."""
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    # titlebar / metadata
    "{{TITLE}}": "Parallel Sampling of Diffusion Models",
    "{{AUTHORS}}": ("Andy Shih<sup>1</sup>, Suneel Belkhale<sup>1</sup>, Stefano Ermon<sup>1</sup>, "
                    "Dorsa Sadigh<sup>1</sup>, Nima Anari<sup>1</sup>"),
    "{{AUTHOR_LEGEND}}": '<sup>1</sup> Stanford University',
    "{{VENUE_NAME}}": "NeurIPS",
    "{{VENUE_YEAR}}": "2023",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "",
    # logos
    "{{LOGO_1}}": "assets/logos/stanford-university.png",
    "{{LOGO_2}}": "", "{{LOGO_3}}": "", "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    # QR
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",
    # Problem
    "{{PROBLEM}}": ("Diffusion models generate high-quality samples but sample <strong>slowly</strong> — "
                    "a single sample can require up to <span class=\"num\">1000</span> sequential denoising "
                    "steps, far too slow for interactive use."),
    # Motivation
    "{{MOTIVATION_1}}": ("Instead of trading <em>quality</em> for speed by cutting steps, spend extra "
                          "<strong>parallel compute</strong> to run all the steps in less wall-clock time."),
    "{{MOTIVATION_2}}": ("The bottleneck is single-sample <strong>latency</strong>, not throughput — "
                          "denoising is inherently sequential, so this looks hard."),
    "{{TEASER_FIGURE}}": "assets/figures/figure_compgraph.png",
    "{{TEASER_CAPTION}}": ("Sequential sampling (left) vs. Picard iterations (right), which add skip "
                            "dependencies so information propagates down the chain in parallel."),
    # Method
    "{{METHOD_1}}": ("Reframe denoising as solving an <strong>ODE by Picard iteration</strong>: guess the "
                      "entire trajectory, then refine every timestep in parallel."),
    "{{METHOD_2}}": ("Iterate to a <strong>fixed point</strong> — empirically converging in far fewer "
                      "iterations than there are denoising steps."),
    "{{METHOD_3}}": ("Process a sliding <strong>batch window</strong> of size <em>p</em> to fit GPU memory, "
                      "advancing it once the leading timesteps converge."),
    "{{METHOD_FIGURE}}": "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": ("ParaDiGMS computes the drift at multiple timesteps in parallel over a batch window "
                            "of size p, then slides the window forward once the error falls below tolerance."),
    # Dataset
    "{{DATASET_1}}": ("Robotics diffusion policies, scored by task reward over 200 episodes."),
    "{{DATASET_2}}": ("Image generation judged by CLIP score (COCO) and FID (LSUN)."),
    # Key Results (2-col defaults, upgraded to 3-col via Edit)
    "{{BASELINE}}": "Sequential DDPM", "{{BASELINE_NUM}}": "50.0s",
    "{{OURS}}": "ParaDDPM", "{{OURS_NUM}}": "14.6s",
    "{{HEADLINE_DELTA}}": "2–4× faster sampling — no measurable quality loss",
    "{{KEY_RESULT_CONCLUSION}}": ("A consistent 2–4× latency reduction across robotics and image tasks, "
                                   "holding reward, FID, and CLIP score unchanged."),
    # Ablation (bullets replaced by table via Edit)
    "{{ABLATION_1}}": ("Error tolerance τ is the speed–quality knob: looser τ needs fewer Picard iterations."),
    "{{ABLATION_2}}": ("On LSUN Church, ParaDDPM matches DDPM FID at 3.9×; 500-step DDIM alone is worse."),
    "{{ABLATION_CONCLUSION}}": ("A relaxed tolerance preserves quality while delivering most of the speedup."),
    # Headline Numbers
    "{{HERO_VAL}}": "2–4×",
    "{{HERO_LABEL}}": "sampling speedup, no quality loss",
    "{{HERO_NOTE}}": "across every task &amp; sampler",
    "{{STAT_2_VAL}}": "14.6s", "{{STAT_2_LBL}}": "SD-v2 (from 50.0s)",
    "{{STAT_3_VAL}}": "3.9×", "{{STAT_3_LBL}}": "LSUN Church, FID 12.8→12.9",
    "{{STAT_4_VAL}}": "20×", "{{STAT_4_LBL}}": "fewer parallel iters vs steps",
    # Takeaway
    "{{TAKEAWAY}}": ("By reformulating denoising as parallel Picard iteration, ParaDiGMS trades extra compute "
                     "for <strong>2–4× lower sampling latency</strong> with no quality loss — and layers on "
                     "top of DDIM and DPMSolver."),
    # Contribution (commented-out in template) — empty to clear tokens
    "{{CONTRIBUTION_1}}": "", "{{CONTRIBUTION_2}}": "", "{{CONTRIBUTION_3}}": "",
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
