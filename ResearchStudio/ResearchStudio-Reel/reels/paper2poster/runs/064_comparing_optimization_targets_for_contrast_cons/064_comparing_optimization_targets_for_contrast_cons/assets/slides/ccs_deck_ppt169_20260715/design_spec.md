# Design Specification & Content Outline

## I. Project Direction
- **Source**: "Comparing Optimization Targets for Contrast-Consistent Search" (Fry et al., NeurIPS 2023 ATTRIB workshop).
- **Core message**: CCS's success comes from the displacement information in contrast-pair data, not its specific loss; a simple Midpoint-Displacement (MD) loss reproduces CCS and, retuned, beats it.
- **Audience**: ML / interpretability researchers.
- **Register**: precise, academic, restrained.
- **content_divergence**: balanced — narration-driven; each slide mirrors one narration section.

## II. Canvas
- PPT 16:9, 1280×720.

## III. Color Scheme
Clean academic light theme with a two-family accent system that distinguishes **CCS (navy/blue)** from **Midpoint-Displacement (violet)**.
- bg #FFFFFF · bg_secondary #F1F5F9 · panel #F8FAFC
- primary/navy #12243B · accent/blue #2563EB · md/violet #7C3AED
- text #12243B · text_secondary #475569 · text_tertiary #94A3B8
- border #E2E8F0 · positive #059669 · warning #DC2626 · tint #EEF2FF

## IV. Typography
- Title: Georgia serif. Body/label: Arial sans. Mono: Consolas.
- body 20 · title 34 · subtitle 24 · cover_title 58 · hero_number 46 · label 13.
- Formula policy: **render-all** for the three core loss/statistic equations (rendered PNGs).

## V. Page Structure (10 slides, 1:1 with narration order)
1. **title** — cover: title, authors, venue, the driving question, MD contribution chip, QR/logos.
2. **problem** — what CCS is + the open question.
3. **motivation** — why it matters + two misleading pictures.
4. **contribution** — three contributions as three cards.
5. **method** — two statistics (σ_d², σ_m²), the sigmoid trade-off, the MD loss equation.
6. **dataset-benchmark** — four models × five datasets; contrast-pair construction.
7. **key-result** — MD↔CCS cosine 0.63 vs self 0.78; other losses ~0.15; Figure 1 geometry.
8. **ablation-study** — λ knob: MD-CCS 0.63 vs MD-Acc 0.38; accuracy lift to 0.76.
9. **headline-numbers** — KPI band: similarity row + accuracy row.
10. **takeaway** — the interchangeable-loss conclusion.

## VI. Icons
- tabler-outline, stroke 2. Used sparingly as label glyphs.

## VII. Charts / Data Visuals
- Hand-authored SVG bar comparisons (cosine similarity, accuracy) with exact values.
- Paper figures: Figure 1 (geometry) on key-result; Figure 2 (histograms) available.

## VIII. Image Resource List
| id | file | Acquire Via | Status | Type |
|---|---|---|---|---|
| fig1_geometry | images/fig1_geometry.png | user | Ready | Figure |
| fig2_histograms | images/fig2_histograms.png | user | Ready | Figure |
| formula_md_loss | images/formula_md_loss.png | formula | Rendered | Latex Formula |
| formula_sigma | images/formula_sigma.png | formula | Rendered | Latex Formula |
| formula_ccs_loss | images/formula_ccs_loss.png | formula | Rendered | Latex Formula |
| qr_code | images/qr_code.png | user | Ready | QR |
| qr_paper | images/qr_paper.png | user | Ready | QR |
| logo_oxford | images/logo_oxford.png | user | Ready | Logo |
| logo_kcl | images/logo_kcl.png | user | Ready | Logo |

## IX. Content Outline
Each slide carries the paper2video visual-anchor contract ids (`cue_sNN_cM_*`) on its
key visual regions so the post-hoc cue matcher aligns narration chunks to geometry.

## X. Execution
- Free design, mode: flat. Sequential hand-authored SVG pages → PPTX via svg_to_pptx.
