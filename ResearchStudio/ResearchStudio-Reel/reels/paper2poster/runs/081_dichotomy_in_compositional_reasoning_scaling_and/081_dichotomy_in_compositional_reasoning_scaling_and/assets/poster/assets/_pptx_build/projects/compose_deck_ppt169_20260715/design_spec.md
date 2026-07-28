# Design Specification & Content Outline

## I. Project Overview
A 10-slide, 16:9 research explainer deck for the COLM 2024 paper *"Do Large Language Models Have Compositional Ability? An Investigation into Limitations and Scalability"* (Xu, Shi, Liang; University of Wisconsin-Madison). The deck backs a ~3-minute narrated video. Narrative arc: pose the composition question, show the failure, define the test suite, reveal the separable-vs-compose-by-step dichotomy through the paper's own figures, and land the practical takeaway.

## II. Audience & Message
- Audience: ML researchers and practitioners scanning the paper's core finding.
- Core message: LLMs compose two learned skills only when the sub-tasks act on separate parts of the input (separable, scales); genuinely chained multi-step tasks fail and do not benefit from scale.

## III. Color Scheme
See `spec_lock.md`. Deep slate primary (#1E293B) with indigo accent (#4F46E5). A running semantic dichotomy motif: emerald (#059669) = separable / composition works; red (#DC2626) = compose-by-step / composition fails.

## IV. Typography
Georgia for titles/emphasis, Arial for body, Consolas for code/tokens. Body 20px baseline; title 34; cover 56; hero numbers 44.

## V. Visual Style
Swiss-minimal: generous whitespace, a 6px accent rule beside each title, restrained cards with 1.5px borders and a soft shadow, no gradients.

## VI. Narrative Mode
narrative — each page advances one beat of the argument.

## VII. Figures
- figure1.png — illustrative simple-vs-composite in-context example (Problem, P02).
- figure2.png — exact-match accuracy vs model scale for Capitalization & Swap (Key Result, P07).
- figure3.png — word error rate vs scale on translation composites (Ablation, P08).

## VIII. Image Resource List
| id | file | Type | Acquire Via | Status |
|---|---|---|---|---|
| figure1 | images/figure1.png | Figure | user | Rendered |
| figure2 | images/figure2.png | Figure | user | Rendered |
| figure3 | images/figure3.png | Figure | user | Rendered |
| logo_uw | images/logo_uw.png | Logo | user | Rendered |
| qr_paper | images/qr_paper.png | QR | user | Rendered |
| qr_code | images/qr_code.png | QR | user | Rendered |

## IX. Content Outline
1. Title — question + paper identity + dichotomy teaser.
2. Problem — simple tasks solved, composite fails (figure1).
3. Motivation — why composition matters, prior gaps, easy-to-reproduce failure.
4. Contribution — three contributions.
5. Method — empirical four settings + linear self-attention theory (confined support).
6. Dataset / Benchmark — building blocks, task families, separable vs compose-by-step.
7. Key Result — the sharp split (figure2).
8. Ablation — scale sweep + demonstration swap (figure3).
9. Headline Numbers — 90% / <20% / 44% / 66%.
10. Takeaway — separable scales, entangled multi-step does not.

## X. Cue Anchors
Each narration chunk maps to a stable `cue_sNN_cM_*` anchor placed on the relevant visible card/figure (id + data-cue-label), per `assets/meta/visual_anchor_contract.json`.
