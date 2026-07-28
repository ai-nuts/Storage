# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_time_series_pre_training_promises_cu`

- Preferred role: `method`
- Cue keywords: `time, series, pre-training, promises, cut, labeling, costs, boost, many, downstream`
- Narration: Time series pre-training promises to cut labeling costs and boost many downstream tasks, but the standard recipes borrowed from vision and language fall short.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_time_series_pre_training_promises_cu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords time, series, pre-training, promises, cut, labeling in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_randomly_masking_series_computing_se`

- Preferred role: `result`
- Cue keywords: `randomly, masking, series, computing, series-wise, similarity, tends, distort, ignore, temporal`
- Narration: Randomly masking a series or computing series-wise similarity tends to distort or ignore the temporal correlations that make time series meaningful. This paper introduces TimeSiam, a simple but effective self-supervised framework built on Siamese networks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c2_randomly_masking_series_computing_se" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords randomly, masking, series, computing, series-wise, similarity in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_instead_masking_isolation_timesiam_s`

- Preferred role: `method`
- Cue keywords: `instead, masking, isolation, timesiam, samples, past, current, subseries, same, sequence`
- Narration: Instead of masking in isolation, TimeSiam samples a past and a current subseries from the same sequence and trains Siamese encoders to reconstruct the masked current series from the past one, explicitly modeling how observations correlate across time.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_instead_masking_isolation_timesiam_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, masking, isolation, timesiam, samples, past in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_learnable_lineage_embeddings_let_sin`

- Preferred role: `method`
- Cue keywords: `learnable, lineage, embeddings, let, single, capture, correlations, many, different, time`
- Narration: Learnable lineage embeddings let a single model capture correlations at many different time distances. Across thirteen benchmarks and two mainstream tasks, forecasting and classification, TimeSiam sets a new state of the art in both in-domain and cross-domain settings.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_learnable_lineage_embeddings_let_sin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords learnable, lineage, embeddings, let, single, capture in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_self_supervised_pre_training_transfo`

- Preferred role: `method`
- Cue keywords: `self-supervised, pre-training, transformed, vision, language, researchers, naturally, reached, same, tools`
- Narration: Self-supervised pre-training has transformed vision and language, and researchers naturally reached for the same tools when working with time series. But the fit is awkward.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_self_supervised_pre_training_transfo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords self-supervised, pre-training, transformed, vision, language, researchers in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_when_you_randomly_mask_points`

- Preferred role: `method`
- Cue keywords: `when, you, randomly, mask, points, across, time, series, you, shatter`
- Narration: When you randomly mask points across a time series, you can shatter the smooth temporal structure that the signal depends on, sometimes making reconstruction so hard the model learns little.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_when_you_randomly_mask_points" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, you, randomly, mask, points, across in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_contrastive_learning_opposite_proble`

- Preferred role: `content`
- Cue keywords: `contrastive, learning, opposite, problem, comparing, whole, series, similarity, tends, ignore`
- Narration: Contrastive learning has the opposite problem: comparing whole series for similarity tends to ignore the fine-grained correlations inside them, and it hinges on augmentations that are notoriously difficult to design for temporal data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_contrastive_learning_opposite_proble" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords contrastive, learning, opposite, problem, comparing, whole in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_gap_addresses_clear_existing_recipes`

- Preferred role: `content`
- Cue keywords: `gap, addresses, clear, existing, recipes, fail, emphasize, temporal, correlations, make`
- Narration: The gap this paper addresses is clear: existing recipes fail to emphasize the temporal correlations that make time series what they are.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_gap_addresses_clear_existing_recipes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gap, addresses, clear, existing, recipes, fail in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_timing_could_not_better_method`

- Preferred role: `method`
- Cue keywords: `timing, could, not, better, method, gets, right, every, day, world`
- Narration: The timing could not be better for a method that gets this right. Every day the world's sensors, wearables, and industrial systems pour out staggering volumes of unlabeled time series through the Internet of Things.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_timing_could_not_better_method" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords timing, could, not, better, method, gets in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_gold_mine_but_only_learn`

- Preferred role: `content`
- Cue keywords: `gold, mine, but, only, learn, without, hand, labeling`
- Narration: That data is a gold mine, but only if we can learn from it without hand labeling.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_gold_mine_but_only_learn" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gold, mine, but, only, learn, without in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_key_insight_motivating_timesiam_time`

- Preferred role: `method`
- Cue keywords: `key, insight, motivating, timesiam, time, series, carry, special, kind, information`
- Narration: The key insight motivating TimeSiam is that time series carry a special kind of information prior methods throw away: the correlation between what happened in the past and what is happening now.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_key_insight_motivating_timesiam_time" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, insight, motivating, timesiam, time, series in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_instead_treating_window_isolation_wh`

- Preferred role: `method`
- Cue keywords: `instead, treating, window, isolation, why, not, build, pre-training, task, explicitly`
- Narration: Instead of treating each window in isolation, why not build a pre-training task that explicitly asks the model to relate distant moments in time to each other.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_instead_treating_window_isolation_wh" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, treating, window, isolation, why, not in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_main_contributions_first`

- Preferred role: `method`
- Cue keywords: `makes, three, main, contributions, first, proposes, timesiam, simple, but, effective`
- Narration: This paper makes three main contributions. First, it proposes TimeSiam, a simple but effective pre-training framework that uses Siamese networks to capture correlations among temporally distanced subseries.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_makes_three_main_contributions_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, main, contributions, first, proposes in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_introduces_learnable_lineage`

- Preferred role: `content`
- Cue keywords: `second, introduces, learnable, lineage, embeddings, lightweight, mechanism, lets, one, represent`
- Narration: Second, it introduces learnable lineage embeddings, a lightweight mechanism that lets one model represent many different past-to-current time distances.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_second_introduces_learnable_lineage" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, introduces, learnable, lineage, embeddings, lightweight in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_through_extensive_experiments`

- Preferred role: `result`
- Cue keywords: `third, through, extensive, experiments, shows, timesiam, achieves, consistent, state-of-the-art, results`
- Narration: Third, through extensive experiments it shows TimeSiam achieves consistent state-of-the-art results when fine-tuned on both forecasting and classification, and across both in-domain and cross-domain settings.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c3_third_through_extensive_experiments" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, through, extensive, experiments, shows, timesiam in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_crucially_framework_backbone_agnosti`

- Preferred role: `method`
- Cue keywords: `crucially, framework, backbone-agnostic, dropping, cleanly, onto, modern, encoders, like, itransformer`
- Narration: Crucially, the framework is backbone-agnostic, dropping cleanly onto modern encoders like iTransformer, PatchTST, and TCN.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_crucially_framework_backbone_agnosti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, framework, backbone-agnostic, dropping, cleanly, onto in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_how_timesiam_works_single_time`

- Preferred role: `result`
- Cue keywords: `how, timesiam, works, single, time, series, randomly, samples, two, windows`
- Narration: Here is how TimeSiam works. From a single time series it randomly samples two windows: a past subseries and a current subseries, together called Siamese subseries. The current window is lightly corrupted with a simple augmentation such as masking.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c1_how_timesiam_works_single_time" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, timesiam, works, single, time, series in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_two_shared_weight_siamese_encoders_p`

- Preferred role: `method`
- Cue keywords: `two, shared-weight, siamese, encoders, process, past, current, windows, decoder, cross-attention`
- Narration: Two shared-weight Siamese encoders process the past and current windows, and a decoder with cross-attention reconstructs the masked current series using the past observation as context. That single design choice, reconstructing the current from the past, forces the model to internalize how distant moments in a series relate.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_two_shared_weight_siamese_encoders_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, shared-weight, siamese, encoders, process, past in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_handle_fact_past_current_windows`

- Preferred role: `content`
- Cue keywords: `handle, fact, past, current, windows, near, far, apart, time, timesiam`
- Narration: To handle the fact that past and current windows can be near or far apart in time, TimeSiam adds learnable lineage embeddings indexed by that relative distance, so one model fluently represents many temporal gaps.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_handle_fact_past_current_windows" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords handle, fact, past, current, windows, near in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_objective_simply_squared_reconstruct`

- Preferred role: `method`
- Cue keywords: `objective, simply, squared, reconstruction, error, between, true, predicted, current, series`
- Narration: The training objective is simply the squared reconstruction error between the true and predicted current series.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_objective_simply_squared_reconstruct" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords objective, simply, squared, reconstruction, error, between in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_evaluation_deliberately_broad_spanni`

- Preferred role: `method`
- Cue keywords: `evaluation, deliberately, broad, spanning, thirteen, benchmarks, two, mainstream, tasks`
- Narration: The evaluation is deliberately broad, spanning thirteen benchmarks and two mainstream tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_evaluation_deliberately_broad_spanni" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, deliberately, broad, spanning, thirteen, benchmarks in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_forecasting_four_ett_subsets_plus`

- Preferred role: `result`
- Cue keywords: `forecasting, four, ett, subsets, plus, weather, electricity, traffic, exchange, classification`
- Narration: For forecasting there are the four ETT subsets, plus Weather, Electricity, Traffic, and Exchange. For classification there are two EEG datasets, AD and TDBrain, and an ECG dataset, PTB.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_forecasting_four_ett_subsets_plus" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords forecasting, four, ett, subsets, plus, weather in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_top_these_eleven_established_benchma`

- Preferred role: `method`
- Cue keywords: `top, these, eleven, established, benchmarks, authors, construct, two, new, large-scale`
- Narration: On top of these eleven established benchmarks, the authors construct two new large-scale, multi-domain datasets called TSLD-500M and TSLD-1G.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_top_these_eleven_established_benchma" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords top, these, eleven, established, benchmarks, authors in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_larger_one_packs_nearly_fourteen`

- Preferred role: `method`
- Cue keywords: `larger, one, packs, nearly, fourteen, million, examples, drawn, diverse, non-overlapping`
- Narration: The larger one packs nearly fourteen million examples drawn from diverse, non-overlapping domains, which lets the paper stress-test cross-domain transfer where pre-training and fine-tuning data come from entirely different sources.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_larger_one_packs_nearly_fourteen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords larger, one, packs, nearly, fourteen, million in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_results_consistent_strong`

- Preferred role: `method`
- Cue keywords: `results, consistent, strong`
- Narration: The results are consistent and strong.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_results_consistent_strong" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, consistent, strong in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_in_domain_forecasting_timesiam_cuts`

- Preferred role: `method`
- Cue keywords: `in-domain, forecasting, timesiam, cuts, average, mean, squared, error, five, point`
- Narration: On in-domain forecasting, TimeSiam cuts average mean squared error by five point seven percent with a PatchTST backbone and two point five percent with iTransformer, and remember these backbones already forecast very well from scratch.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_in_domain_forecasting_timesiam_cuts" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords in-domain, forecasting, timesiam, cuts, average, mean in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_in_domain_classification_lifts_avera`

- Preferred role: `method`
- Cue keywords: `in-domain, classification, lifts, average, accuracy, eleven, point, five, percent, over`
- Narration: On in-domain classification, it lifts average accuracy by eleven point five percent over random initialization. Across all these settings TimeSiam beats eight strong self-supervised baselines.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_in_domain_classification_lifts_avera" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords in-domain, classification, lifts, average, accuracy, eleven in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_perhaps_most_striking_finding_cross`

- Preferred role: `method`
- Cue keywords: `perhaps, most, striking, finding, cross-domain, transfer, pre-training, large, diverse, tsld-1g`
- Narration: Perhaps the most striking finding is in cross-domain transfer: pre-training on the large, diverse TSLD-1G dataset and fine-tuning elsewhere sometimes beats even in-domain pre-training, which confirms that scale and diversity of pre-training data really pay off.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_perhaps_most_striking_finding_cross" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords perhaps, most, striking, finding, cross-domain, transfer in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_careful_ablations_traffic_benchmark`

- Preferred role: `result`
- Cue keywords: `careful, ablations, traffic, benchmark, tell, which, design, choices, matter`
- Narration: Careful ablations on the Traffic benchmark tell us which design choices matter.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c1_careful_ablations_traffic_benchmark" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords careful, ablations, traffic, benchmark, tell, which in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_reconstructing_current_window_past_o`

- Preferred role: `method`
- Cue keywords: `reconstructing, current, window, past, one, clearly, beats, plain, self-reconstruction, validating`
- Narration: Reconstructing the current window from a past one clearly beats plain self-reconstruction, validating the core Siamese idea.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_reconstructing_current_window_past_o" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reconstructing, current, window, past, one, clearly in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_masking_ratio_sweet_spot_around`

- Preferred role: `content`
- Cue keywords: `masking, ratio, sweet, spot, around, twenty-five, percent, masking, only, fifteen`
- Narration: The masking ratio has a sweet spot around twenty-five percent: masking only fifteen percent makes the task too easy to teach anything useful, while masking seventy-five percent makes it too hard.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_masking_ratio_sweet_spot_around" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords masking, ratio, sweet, spot, around, twenty-five in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_lineage_embeddings_deliver_consisten`

- Preferred role: `result`
- Cue keywords: `lineage, embeddings, deliver, consistent, gains, over, random, initialization, adding, more`
- Narration: Lineage embeddings deliver consistent gains over random initialization, and adding more of them keeps improving results on Electricity and Traffic up to a point, confirming that explicitly modeling multiple temporal distances is worthwhile.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_lineage_embeddings_deliver_consisten" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lineage, embeddings, deliver, consistent, gains, over in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_put_impact_numbers_timesiam_reduces`

- Preferred role: `method`
- Cue keywords: `put, impact, numbers, timesiam, reduces, average, forecasting, error, five, point`
- Narration: To put the impact in numbers: TimeSiam reduces average forecasting error by five point seven percent on PatchTST and two point five percent on iTransformer, and raises classification accuracy by eleven point five percent in the in-domain setting, all relative to training from scratch.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_put_impact_numbers_timesiam_reduces" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords put, impact, numbers, timesiam, reduces, average in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_does_across_thirteen_benchmarks_cove`

- Preferred role: `result`
- Cue keywords: `does, across, thirteen, benchmarks, covering, forecasting, classification, both, in-domain, cross-domain`
- Narration: It does this across thirteen benchmarks covering forecasting and classification in both in-domain and cross-domain settings, and it outperforms eight state-of-the-art self-supervised baselines.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_does_across_thirteen_benchmarks_cove" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords does, across, thirteen, benchmarks, covering, forecasting in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_backing_cross_domain_story_tsld_1g_n`

- Preferred role: `method`
- Cue keywords: `backing, cross-domain, story, tsld-1g, newly, built, pre-training, dataset, nearly, fourteen`
- Narration: Backing the cross-domain story is TSLD-1G, a newly built pre-training dataset with nearly fourteen million examples spanning multiple domains.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_backing_cross_domain_story_tsld_1g_n" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords backing, cross-domain, story, tsld-1g, newly, built in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_takeaway_reframing`

- Preferred role: `takeaway`
- Cue keywords: `lasting, takeaway, reframing`
- Narration: The lasting takeaway is a reframing.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_lasting_takeaway_reframing" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, takeaway, reframing in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_posing_time_series_pre_training_past`

- Preferred role: `method`
- Cue keywords: `posing, time, series, pre-training, past-to-current, reconstruction, between, siamese, subseries, equipping`
- Narration: By posing time series pre-training as past-to-current reconstruction between Siamese subseries, and equipping the model with learnable lineage embeddings to span different temporal distances, TimeSiam captures exactly the correlations that masking and contrastive methods leave on the table.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_posing_time_series_pre_training_past" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords posing, time, series, pre-training, past-to-current, reconstruction in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_payoff_simple_general_framework_drop`

- Preferred role: `title`
- Cue keywords: `payoff, simple, general, framework, drops, onto, modern, backbones, scales, larger`
- Narration: The payoff is a simple, general framework that drops onto modern backbones, scales with larger and more diverse data, and sets a new state of the art for transfer across tasks and domains.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s10_c3_payoff_simple_general_framework_drop" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords payoff, simple, general, framework, drops, onto in title/desc so the matcher can verify semantic overlap.
