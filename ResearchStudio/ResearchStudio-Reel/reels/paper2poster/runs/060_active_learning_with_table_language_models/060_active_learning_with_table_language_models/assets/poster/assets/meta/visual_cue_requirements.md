# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_tabular_language_models_could_unlock`

- Preferred role: `method`
- Cue keywords: `tabular, language, models, could, unlock, spreadsheets, buried, inside, industrial, companies`
- Narration: Tabular language models could unlock the spreadsheets buried inside industrial companies, but they need labeled data, and only scarce experts can annotate these technical tables.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_tabular_language_models_could_unlock" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tabular, language, models, could, unlock, spreadsheets in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_presented_neurips_2022_ringsquandl_k`

- Preferred role: `title`
- Cue keywords: `presented, neurips, 2022, ringsquandl, koleva, siemens, asks, active, learning, cut`
- Narration: Presented at NeurIPS 2022 by Ringsquandl and Koleva from Siemens, this paper asks: can active learning cut that labeling cost for sub-cell entity recognition?
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s01_c2_presented_neurips_2022_ringsquandl_k" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords presented, neurips, 2022, ringsquandl, koleva, siemens in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_their_headline_finding_batch_diverse`

- Preferred role: `method`
- Cue keywords: `their, headline, finding, batch-diverse, gradient, method, badge, matches, full-training, performance`
- Narration: Their headline finding is that a batch-diverse gradient method, BADGE, matches full-training performance with far fewer labels, while forcing maximum table diversity actually hurts.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_their_headline_finding_batch_diverse" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords their, headline, finding, batch-diverse, gradient, method in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_industry_runs_spreadsheets`

- Preferred role: `method`
- Cue keywords: `industry, runs, spreadsheets`
- Narration: Industry runs on spreadsheets.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_industry_runs_spreadsheets" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords industry, runs, spreadsheets in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_operators_track_equipment_sensors_ve`

- Preferred role: `method`
- Cue keywords: `operators, track, equipment, sensors, vessels, loosely, structured, tables, extracting, information`
- Narration: Operators track equipment, sensors, and vessels in loosely structured tables, and extracting that information automatically means fine-tuning tabular language models on labeled examples.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_operators_track_equipment_sensors_ve" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords operators, track, equipment, sensors, vessels, loosely in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_but_these_tables_highly_technical`

- Preferred role: `content`
- Cue keywords: `but, these, tables, highly, technical, language, only, few, experts, annotate`
- Narration: But these tables use highly technical language only a few experts can annotate, so labeling gets expensive fast.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_but_these_tables_highly_technical" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, these, tables, highly, technical, language in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_frames_sub_cell_named_entity_recogni`

- Preferred role: `content`
- Cue keywords: `frames, sub-cell, named, entity, recognition, genuinely, new, active, learning, problem`
- Narration: The paper frames this as sub-cell named entity recognition, a genuinely new active learning problem, since each cell carries multiple token-level labels at once.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_frames_sub_cell_named_entity_recogni" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords frames, sub-cell, named, entity, recognition, genuinely in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_active_learning_built_setting_plenti`

- Preferred role: `content`
- Cue keywords: `active, learning, built, setting, plentiful, unlabeled, expensive, labels, squeezing, most`
- Narration: Active learning is built for this setting: plentiful unlabeled data and expensive labels, squeezing the most performance from every annotation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_active_learning_built_setting_plenti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords active, learning, built, setting, plentiful, unlabeled in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_but_big_transformer_models_learn`

- Preferred role: `method`
- Cue keywords: `but, big, transformer, models, learn, one, example, time, they, train`
- Narration: But big transformer models can't learn one example at a time; they train in batches over several epochs, so the acquisition function must choose a whole batch at once.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_but_big_transformer_models_learn" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, big, transformer, models, learn, one in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_pure_uncertainty_sampling_grabs_very`

- Preferred role: `content`
- Cue keywords: `pure, uncertainty, sampling, grabs, very, similar, correlated, cells, often, same`
- Narration: Pure uncertainty sampling grabs very similar, correlated cells, often from the same table, wasting budget.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_pure_uncertainty_sampling_grabs_very" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pure, uncertainty, sampling, grabs, very, similar in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_yet_one_had_studied_active`

- Preferred role: `content`
- Cue keywords: `yet, one, had, studied, active, learning, tabular, language, models, gap`
- Narration: Yet no one had studied active learning with tabular language models, the gap this work fills.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_yet_one_had_studied_active" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords yet, one, had, studied, active, learning in title/desc so the matcher can verify semantic overlap.

## Slide 04: method

Heading: Method

### Cue 1: `cue_s04_c1_tabular_language_transformer_encoder`

- Preferred role: `method`
- Cue keywords: `tabular, language, transformer, encoder, swaps, vanilla, attention, row-column, visibility, matrix`
- Narration: The model is a tabular language model: a transformer encoder that swaps vanilla attention for a row-column visibility matrix with within-cell positional encoding, so every token is aware of the whole table.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_tabular_language_transformer_encoder" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tabular, language, transformer, encoder, swaps, vanilla in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_decoder_tags_token_over_four`

- Preferred role: `method`
- Cue keywords: `decoder, tags, token, over, four, entity, types, equipment, tags, equipment`
- Narration: A decoder tags each token over four entity types: equipment tags, equipment names, physical quantities, and units.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_decoder_tags_token_over_four" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords decoder, tags, token, over, four, entity in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_top_sits_pool_based_active_learning`

- Preferred role: `content`
- Cue keywords: `top, sits, pool-based, active, learning, repeatedly, picking, most, informative, cells`
- Narration: On top sits pool-based active learning, repeatedly picking the most informative cells for an expert to label.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_top_sits_pool_based_active_learning" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords top, sits, pool-based, active, learning, repeatedly in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_four_acquisition_functions_compete_m`

- Preferred role: `method`
- Cue keywords: `four, acquisition, functions, compete, mnlp, scores, normalized, log-probability, uncertainty, mnlp-plus`
- Narration: Four acquisition functions compete: MNLP scores normalized log-probability uncertainty; MNLP-plus forces round-robin table diversity; BADGE clusters per-cell gradient embeddings with k-means-plus-plus for uncertain, diverse batches; and Rand samples uniformly.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_four_acquisition_functions_compete_m" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords four, acquisition, functions, compete, mnlp, scores in title/desc so the matcher can verify semantic overlap.

## Slide 05: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s05_c1_evaluation_real_industrial_dataset_n`

- Preferred role: `method`
- Cue keywords: `evaluation, real, industrial, dataset, not, academic, benchmark`
- Narration: Evaluation uses a real industrial dataset, not an academic benchmark.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_evaluation_real_industrial_dataset_n" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, real, industrial, dataset, not, academic in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_spreadsheets_several_plants_downsamp`

- Preferred role: `content`
- Cue keywords: `spreadsheets, several, plants, downsampled, most, five, rows, expert, annotators, labeled`
- Narration: Spreadsheets from several plants were downsampled to at most five rows each, and expert annotators labeled every cell with the Prodigy span-based tool.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_spreadsheets_several_plants_downsamp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords spreadsheets, several, plants, downsampled, most, five in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_random_split_gives_55_tables`

- Preferred role: `method`
- Cue keywords: `random, split, gives, 55, tables, 24, testing`
- Narration: A random split gives 55 training tables and 24 for testing.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_random_split_gives_55_tables" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords random, split, gives, 55, tables, 24 in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_set_holds_4_774_cells`

- Preferred role: `method`
- Cue keywords: `set, holds, 4, 774, cells, but, only, about, 1, 100`
- Narration: The training set holds 4,774 cells but only about 1,100 entity labels, just 0.23 per cell, meaning roughly 77 percent of cells contain no entity, an extreme imbalance typical of industrial data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_set_holds_4_774_cells" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords set, holds, 4, 774, cells, but in title/desc so the matcher can verify semantic overlap.

## Slide 06: key-result

Heading: Key Result

### Cue 1: `cue_s06_c1_performance_micro_averaged_1_held_ou`

- Preferred role: `result`
- Cue keywords: `performance, micro-averaged, 1, held-out, test, set, across, active, learning, iterations`
- Narration: Performance is micro-averaged F1 on the held-out test set across active learning iterations.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_performance_micro_averaged_1_held_ou" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords performance, micro-averaged, 1, held-out, test, set in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_badge_standout_beats_random_selectio`

- Preferred role: `method`
- Cue keywords: `badge, standout, beats, random, selection, even, surpasses, ceiling, full, dataset`
- Narration: BADGE is the standout: it beats random selection and even surpasses the ceiling from training on the full dataset, using far fewer labels.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_badge_standout_beats_random_selectio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords badge, standout, beats, random, selection, even in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_pure_uncertainty_sampling_mnlp_disap`

- Preferred role: `result`
- Cue keywords: `pure, uncertainty, sampling, mnlp, disappoints, edging, past, random, only, after`
- Narration: Pure uncertainty sampling with MNLP disappoints, edging past random only after around 500 labels, and with high variance.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c3_pure_uncertainty_sampling_mnlp_disap" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pure, uncertainty, sampling, mnlp, disappoints, edging in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_most_striking_mnlp_plus_which_forces`

- Preferred role: `method`
- Cue keywords: `most, striking, mnlp-plus, which, forces, maximum, table, diversity, worst, all`
- Narration: Most striking, MNLP-plus, which forces maximum table diversity, is the worst of all.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_most_striking_mnlp_plus_which_forces" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords most, striking, mnlp-plus, which, forces, maximum in title/desc so the matcher can verify semantic overlap.

## Slide 07: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s07_c1_four_acquisition_functions_effective`

- Preferred role: `guidance`
- Cue keywords: `four, acquisition, functions, effectively, ablate, diversity, lesson, right, amount, matters`
- Narration: The four acquisition functions effectively ablate diversity, and the lesson is that the right amount matters enormously.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s07_c1_four_acquisition_functions_effective" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords four, acquisition, functions, effectively, ablate, diversity in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_badge_built_in_batch_diversity_helps`

- Preferred role: `result`
- Cue keywords: `badge, built-in, batch, diversity, helps, but, mnlp-plus, forced, maximum, diversity`
- Narration: BADGE's built-in batch diversity helps, but MNLP-plus's forced maximum diversity hurts, falling below even random.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_badge_built_in_batch_diversity_helps" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords badge, built-in, batch, diversity, helps, but in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_tracking_how_many_distinct_tables`

- Preferred role: `method`
- Cue keywords: `tracking, how, many, distinct, tables, method, draws, explains, why, mnlp`
- Narration: Tracking how many distinct tables each method draws from explains why: MNLP fixates on a few tables, MNLP-plus spreads across as many as possible, and BADGE lands in between.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_tracking_how_many_distinct_tables" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tracking, how, many, distinct, tables, method in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_goal_isn_maximum_diversity_but`

- Preferred role: `guidance`
- Cue keywords: `goal, isn, maximum, diversity, but, careful, trade-off, per-cell, uncertainty`
- Narration: The goal isn't maximum diversity but a careful trade-off with per-cell uncertainty.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s07_c4_goal_isn_maximum_diversity_but" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords goal, isn, maximum, diversity, but, careful in title/desc so the matcher can verify semantic overlap.

## Slide 08: takeaway

Heading: Takeaway

### Cue 1: `cue_s08_c1_lasting_message_active_learning_real`

- Preferred role: `guidance`
- Cue keywords: `lasting, message, active, learning, really, slash, expert-labeling, cost, tabular, language`
- Narration: The lasting message: active learning really can slash the expert-labeling cost of tabular language models, but only if diversity is handled with care.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s08_c1_lasting_message_active_learning_real" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, active, learning, really, slash in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_cell_level_acquisition_built_in_batc`

- Preferred role: `method`
- Cue keywords: `cell-level, acquisition, built-in, batch, diversity, like, badge, reaches, full-training, performance`
- Narration: Cell-level acquisition with built-in batch diversity, like BADGE, reaches full-training performance using a fraction of the labels, while bluntly maximizing table diversity backfires.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_cell_level_acquisition_built_in_batc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cell-level, acquisition, built-in, batch, diversity, like in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_balance_diversity_against_uncertaint`

- Preferred role: `result`
- Cue keywords: `balance, diversity, against, uncertainty, rather, maximize, either, alone`
- Narration: Balance diversity against uncertainty rather than maximize either alone.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c3_balance_diversity_against_uncertaint" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords balance, diversity, against, uncertainty, rather, maximize in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_first_work_flags_two_frontiers`

- Preferred role: `content`
- Cue keywords: `first, work, flags, two, frontiers, acquisition, compute, cost, annotator, cognitive`
- Narration: As the first work here, it flags two frontiers: acquisition compute cost, and annotator cognitive load.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_first_work_flags_two_frontiers" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, work, flags, two, frontiers, acquisition in title/desc so the matcher can verify semantic overlap.
