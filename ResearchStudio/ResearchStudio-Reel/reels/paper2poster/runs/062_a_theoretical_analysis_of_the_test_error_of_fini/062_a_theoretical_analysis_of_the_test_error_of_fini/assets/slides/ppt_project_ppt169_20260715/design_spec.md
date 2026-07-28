# Design Specification — A Theoretical Analysis of the Test Error of Finite-Rank Kernel Ridge Regression

## I. Project Overview
- Source: NeurIPS 2023 paper (Cheng, Lucchi, Dokmanić, Kratsios, Belius).
- Deliverable: 10-slide narrated video deck matching the paper2assets narration order.
- content_divergence: faithful — every claim, number, and figure comes from the paper.
- Register: academic, precise, confident.

## II. Audience & Message
- Audience: ML researchers and theoreticians familiar with kernel methods.
- Core message: finite-rank KRR (the model behind last-layer fine-tuning) now has sharp, two-sided, non-asymptotic test-error bounds that stay tight for any ridge, including ridgeless.

## III. Color Scheme
- Background white `#FFFFFF`, panels `#F4F6FB`.
- Primary cobalt `#2540D9` = the new/tight bounds and key concepts.
- Secondary accent warm red `#E0552D` = prior/loose (Bach) and upper-bound contrast.
- Deep navy `#16205C` for headings/structure; positive green `#1F9D6B` for tightness/lower bound.
- Text `#141A33`, secondary text `#5A6079`, hairlines `#DCE1EE`.

## IV. Font Plan
- Per-role font stacks: heading/body/kicker all `Inter, Arial, sans-serif`; code `"DejaVu Sans Mono", Consolas, monospace`.
- Note: Inter is used for on-screen video fidelity (installed on the render host). PowerPoint substitutes to Arial if Inter is absent; this is acceptable for the editable deliverable.
- Sizes (px): body 24, title 44, subtitle 30, kicker 18, annotation 18, footnote 15, hero_number 60.
- Formula policy: render-all-worthy expressions as PNG (latex_render.py); listed in §VIII.

## V. Visual Style
- swiss-minimal: strong grid, generous whitespace, hairline rules, one accent color plus one contrast color, no decorative gradients. Each slide carries a numbered kicker, a bold title, a thin accent rule, and a clean content zone.

## VI. Narrative Mode
- narrative: title → problem → motivation → contribution → method → dataset → key result → ablation → headline numbers → takeaway.

## VII. Visualizations
- Figure 1 (KRR on a finite-rank kernel: training + test error vs N) on the dataset/benchmark slide.
- Figure 2 (comparison of test-error bounds vs N and vs 1/λ, log scale) on the key-result slide.
- Figure 3 (our bounds vs test error with residues dropped) on the ablation slide.
- Rendered LaTeX for the estimator, bias/variance split, variance bound, decay rate, and ridgeless limit.

## VIII. Image Resource List
| File | Type | Acquire Via | Status |
|---|---|---|---|
| images/figure1.png | Figure | user | Ready |
| images/figure2.png | Figure | user | Ready |
| images/figure3.png | Figure | user | Ready |
| images/f_estimator.png | Latex Formula | formula | Rendered |
| images/f_split.png | Latex Formula | formula | Rendered |
| images/f_variance.png | Latex Formula | formula | Rendered |
| images/f_rate.png | Latex Formula | formula | Rendered |
| images/f_ridgeless.png | Latex Formula | formula | Rendered |
| images/logo_basel.png | Logo | user | Ready |
| images/logo_mcmaster.png | Logo | user | Ready |
| images/logo_vector.png | Logo | user | Ready |
| images/logo_unidistance.png | Logo | user | Ready |
| images/qr_paper.png | QR | user | Ready |

## IX. Content Outline
- P01 title — paper title, authors, institutes, venue, one-line result; logos + paper QR. (anchor)
- P02 problem — KRR explains generalization / last-layer = finite-rank kernel; classical bounds too loose. (dense)
- P03 motivation — freeze backbone + retrain head is everywhere; theory lags, no lower bound. (dense)
- P04 contribution — threefold: improve as ridge→0; matching lower bound; large empirical gain; eigenfunction-basis trick. (dense)
- P05 method — estimator, bias/variance split, key ingredients, holds for any ridge. (dense)
- P06 dataset — controlled synthetic; two kernels tNTK + LK; sweep N and ridge; Figure 1. (dense)
- P07 key-result — bounds bracket error; stark gain vs Bach; ridgeless limit; Figure 2. (dense)
- P08 ablation — ablate bound; finite-rank floor + residues; dropped residues fail small-N; ridge sweep; Figure 3. (dense)
- P09 headline-numbers — prob ≥ 1−2/N; logN/N decay; variance σ²·2M/N; first lower bound. (dense)
- P10 takeaway — sharp two-sided bounds; eigenfunction-basis template. (anchor)

## X. Execution Notes
- Each content region discussed by narration carries a stable `cue_sNN_cM_*` group id with `<title>`/`<desc>` keywords for video visual-cue matching.
- pptx_structure: flat (free design). Export materializes one Master + Blank Layout.
