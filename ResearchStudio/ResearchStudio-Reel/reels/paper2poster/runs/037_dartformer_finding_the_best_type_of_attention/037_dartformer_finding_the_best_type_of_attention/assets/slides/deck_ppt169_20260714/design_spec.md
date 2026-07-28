# Design Specification — DARTFormer paper explainer

## I. Project
- Source: DARTFormer: Finding the Best Type of Attention (Brown, Zhao, Shumailov, Mullins, 2022; arXiv:2210.00641)
- Purpose: 10-slide narrated video deck (paper2video), ~6 min, one slide per narration section.
- Audience: ML researchers and practitioners familiar with Transformers / attention / NAS.
- Content divergence: faithful to the paper; narration text is the canonical `assets/audio/script.json`.

## II. Mode & Style
- Mode: narrative — problem → intuition → method → the twist result → cautionary takeaway.
- Visual style: swiss-minimal — modular grid, sharp geometry, vast whitespace, single indigo accent, one restrained red for the negative finding.

## III. Color
- bg #FFFFFF; secondary_bg #F5F4F1; primary/indigo #2440D9; accent/red #D8402A; secondary_accent/green #12805C; text #14171F; text_secondary #6E7178; border #DBDBD6.

## IV. Font Plan
- Family: Arial, "Helvetica Neue", sans-serif (neo-grotesque; installed, PPT-safe).
- Sizes (px): display_title 62, hero_number 120, title 44, subtitle 30, lead 28, body 24, annotation 18, kicker 16, footnote 15.

## VIII. Image Resource List
- page2_figure1.png — Figure 1: single-layer supernetwork (left) + derived heterogeneous architecture (right). Acquire Via: user. Status: Existing. no-crop.
- page9_figure3.png — Figure 3: NAS Prune worst-first removal. Acquire Via: user. Status: Existing. no-crop.
- page10_figure4.png — Figure 4: multi-head attention search space. Acquire Via: user. Status: Existing. no-crop.
- formula_avg.png — fixed-alpha supernetwork averaging. Acquire Via: formula. Status: Rendered. Type: Latex Formula. no-crop.
- formula_score.png — masked validation accuracy drop score. Acquire Via: formula. Status: Rendered. Type: Latex Formula. no-crop.

## IX. Content Outline (10 pages, one per narration section)
- P01 title (anchor/cover): Title, authors, institutes; one-line hook "Search for the best attention — and test whether mixing several is even better."
- P02 problem (dense): Quadratic attention → many efficient variants; no single one wins; how to pick efficiently?
- P03 motivation (breathing): The intuition — heads specialize, so a mixture might beat any single attention. Does it hold?
- P04 contribution (dense): 3 contributions — DARTFormer search; heterogeneous extension (NAS Prune / NAS One-shot); empirical result that mixing cannot beat the best homogeneous.
- P05 method (dense): Single-layer supernetwork, fixed-alpha averaging (eq), masked-validation-drop score (eq), homogeneous vs heterogeneous selection; Figure 1.
- P06 dataset-benchmark (dense): Three LRA tasks (IMDb 1k, ListOps 2k, doc-matching 4k); nine candidate attentions.
- P07 key-result (breathing): The finding splits in two — search works for homogeneous selection; heterogeneous never beats the best single. "Beat the average, not the best."
- P08 ablation-study (dense): NAS Prune vs NAS One-shot — expensive pruning gives no consistent edge; tilting the mixture doesn't help; Figure 3.
- P09 headline-numbers (dense): ListOps Reformer 11.85 vs <0.5; doc-matching 71.1 vs 67.0/64.7; text 64.5 vs 63.9/64.4.
- P10 takeaway (anchor/ending): Cheap reliable recipe + warning on low drop scores; cautionary lesson — diverse attentions don't add complementary biases.
