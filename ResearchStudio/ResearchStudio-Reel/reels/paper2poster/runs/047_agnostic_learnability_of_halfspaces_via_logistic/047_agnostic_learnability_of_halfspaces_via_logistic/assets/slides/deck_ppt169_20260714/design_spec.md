# Design Specification — Agnostic Learnability of Halfspaces via Logistic Loss

## I. Overview
A 10-slide research briefing deck for the ICML 2022 paper "Agnostic Learnability of
Halfspaces via Logistic Loss" (Ji, Ahn, Awasthi, Kale, Karp). Audience: ML theory
researchers and graduate students. Goal: explain how the paper closes the √OPT-vs-OPT
gap for logistic regression and introduces a simple two-phase logistic + perceptron fix.

## II. Canvas
PPT 16:9, 1280×720, viewBox `0 0 1280 720`.

## III. Color Scheme
Swiss-minimal on white. Deep navy `#12233B` for headings/structure, cobalt `#2563EB`
as the primary accent, red `#DC2626` for the negative/lower-bound result, green
`#059669` for the positive/near-optimal result. Neutral text `#1A202C` / `#55606E`,
hairline borders `#E2E8F0`, soft panel fill `#F4F6FA`.

## IV. Font Plan
Georgia serif for slide titles and display math emphasis; Arial for body and labels;
Consolas for algorithmic/update expressions. Body 16 px baseline; title 34; subtitle 20;
annotation 13; footnote 11; hero number 52. Formula policy: text-only — expressions are
rendered as editable SVG text with Unicode math (no external formula PNGs), keeping the
deck self-contained.

## V. Structure (one slide per narration section)
1 Title · 2 Problem · 3 Motivation · 4 Contribution · 5 Method · 6 Distribution class /
Setting · 7 Key Result · 8 Analysis (ablation) · 9 Headline Numbers · 10 Takeaway.

## VI. Visual cue anchors
Each slide carries 2–4 semantic content groups whose SVG `id`, `<title>`, `<desc>`, and
`data-cue-label` match the paper2video anchor contract (`cue_sNN_cM_*`) so video highlights
land on the exact region the narration discusses.

## VII. Images
None. Theory paper — all visuals are authored SVG (diagrams, bound bars, equation panels).
No AI/web/formula image rows.
