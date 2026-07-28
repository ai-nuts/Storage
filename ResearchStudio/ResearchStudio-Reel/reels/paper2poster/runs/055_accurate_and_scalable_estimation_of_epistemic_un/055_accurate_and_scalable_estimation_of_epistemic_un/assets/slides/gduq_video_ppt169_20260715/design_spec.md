# G-ΔUQ Video Deck — Design Specification

## I. Project
Narrated 10-slide deck for the paper "Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural Networks" (ICLR 2024). Slides map 1:1 to the paper2assets narration sections and carry per-chunk semantic cue anchors (`cue_sNN_cM_*`) for the video highlight track.

## II. Audience & Purpose
Graph ML researchers and practitioners deploying GNNs in safety-critical settings. Purpose: convey why GNN confidence degrades under distribution shift, why bigger/more expressive models do not fix it, and how G-ΔUQ (stochastic anchoring + partial stochasticity) delivers reliable, well-calibrated uncertainty at single-model cost.

## III. Color Scheme
Editorial-tech on white. Cobalt `#2453D6` (primary), teal `#0E9E8F` (method/positive), coral `#E4572E` (problem/gaps). Ink `#12172A`, secondary `#5A6675`, hairline borders `#E2E7EF`. Tints for card fills.

## IV. Font Plan
Arial family throughout (PPT-safe), Consolas for code/math tokens. Body 17px baseline; title 34; cover title 76; hero/KPI numbers 40–46. Sizes per `spec_lock.md`. Formula policy: text-only (Unicode Δ, subscripts as text).

## V. Visual Style
Swiss-minimal: generous whitespace, hairline rules, inset accents, numbered/iconed cards, restrained data marks drawn as native shapes.

## VI. Narrative (mode: narrative)
Title → Problem → Motivation → Contribution → Method → Dataset/Benchmark → Key Result → Ablation → Headline Numbers → Takeaway.

## VII. Figures
- Figure 1 (calibration under structural distortion; ECE grows, GPS doesn't help, G-ΔUQ fixes) → Motivation (P03).
- Figure 2 / figure3.png (overview of three G-ΔUQ stochastic-centering variants) → Method (P05).
- Figure 5 / figure5.png (concept & covariate shift accuracy + calibration) → Key Result (P07).
- Figure 4 / figure4.png (size-shift predictive uncertainty) → Ablation (P08).

## VIII. Image Resource List
| File | Type | Acquire Via | Status |
|---|---|---|---|
| images/figure1.png | Chart | user | Ready |
| images/figure3.png | Diagram | user | Ready |
| images/figure5.png | Chart | user | Ready |
| images/figure4.png | Chart | user | Ready |
| images/qr_code.png | QR | user | Ready |
| images/qr_paper.png | QR | user | Ready |
| images/logo_umich.png | Logo | user | Ready |
| images/logo_llnl.png | Logo | user | Ready |

## IX. Content Outline
P01 title · P02 problem · P03 motivation · P04 contribution · P05 method · P06 dataset-benchmark · P07 key-result · P08 ablation-study · P09 headline-numbers · P10 takeaway. Each content page hosts 3–4 chunk groups carrying `cue_sNN_cM_*` anchor ids with narration keywords in `<title>`/`<desc>`.
