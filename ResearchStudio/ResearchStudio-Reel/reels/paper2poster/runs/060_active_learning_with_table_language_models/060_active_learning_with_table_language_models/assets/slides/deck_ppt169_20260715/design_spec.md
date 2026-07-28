# Design Spec — Active Learning with Tabular Language Models

## Source
- Paper: Active Learning with Tabular Language Models (Ringsquandl & Koleva, Siemens / LMU Munich)
- Venue: Table Representation Learning Workshop, NeurIPS 2022 — arXiv:2211.04128
- Narration source: assets/audio/script.json (8 sections, video-aligned)

## Audience & Goal
Research-explainer deck backing a ~4-minute narrated video. One slide per narration section, in narration order.

## Visual System
- Canvas: 1280×720 (PPT 16:9), white background, generous margins.
- Palette: navy primary (#16324F), teal accent (#1F9E8F); series colors mirror Figure 2 (rand red, mnlp blue, badge green, mnlp+ purple, full orange).
- Type: Georgia serif for titles/emphasis, Arial for body, Consolas for numbers.
- Every content slide: accent header bar + kicker, a dominant visual (figure, table, chart, or diagram), and a single takeaway strip.

## Slide Plan (order matches script.json)
1. title — cover: paper title, authors, venue, headline finding, paper QR.
2. problem — industrial spreadsheets, expensive expert labels, sub-cell NER framing.
3. motivation — active learning fit, batch acquisition, correlated-cell pitfall, the gap.
4. method — tabular LM encoder + IO decoder + pool-based AL + four acquisition functions.
5. dataset-benchmark — real industrial dataset, split, extreme label sparsity numbers.
6. key-result — Figure 2 F1-vs-labels curve; BADGE beats full-training ceiling.
7. ablation-study — diversity trade-off; table-coverage behavior of MNLP / MNLP+ / BADGE.
8. takeaway — recipe (balance diversity vs uncertainty) + two open frontiers.

## Anchors
Each content group carries a `cue_sNN_cM_*` id plus a `<desc>` of narration keywords for video visual-cue alignment (see assets/meta/visual_anchor_contract.json).
