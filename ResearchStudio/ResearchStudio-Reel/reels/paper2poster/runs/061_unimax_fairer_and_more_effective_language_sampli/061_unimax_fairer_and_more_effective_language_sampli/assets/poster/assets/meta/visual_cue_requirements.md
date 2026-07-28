# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_multilingual_language_models_must_de`

- Preferred role: `title`
- Cue keywords: `multilingual, language, models, must, decide, how, much, train, language, standard`
- Narration: Multilingual language models must decide how much to train on each language, and the standard answer has been temperature-based sampling.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s01_c1_multilingual_language_models_must_de" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords multilingual, language, models, must, decide, how in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_google_research_introduces_unimax_si`

- Preferred role: `method`
- Cue keywords: `google, research, introduces, unimax, simple, sampling, method, gives, more, uniform`
- Narration: This paper from Google Research introduces UniMax, a simple sampling method that gives more uniform coverage to high-resource languages while explicitly capping how many times any low-resource language's data is repeated.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_google_research_introduces_unimax_si" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords google, research, introduces, unimax, simple, sampling in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_across_many_benchmarks_scales_unimax`

- Preferred role: `result`
- Cue keywords: `across, many, benchmarks, scales, unimax, beats, temperature, sampling, gains, persist`
- Narration: Across many benchmarks and model scales, UniMax beats temperature sampling, and the gains persist as models grow.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c3_across_many_benchmarks_scales_unimax" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, many, benchmarks, scales, unimax, beats in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_authors_also_release_refreshed_mc4`

- Preferred role: `method`
- Cue keywords: `authors, also, release, refreshed, mc4, corpus, twenty-nine, trillion, characters, across`
- Narration: The authors also release a refreshed mC4 corpus of twenty-nine trillion characters across one hundred seven languages, along with umT5 checkpoints trained with UniMax.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_authors_also_release_refreshed_mc4" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, also, release, refreshed, mc4, corpus in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_why_does_language_sampling_matter`

- Preferred role: `content`
- Cue keywords: `why, does, language, sampling, matter, much, massively, multilingual, corpora, wildly`
- Narration: So why does language sampling matter so much? Massively multilingual corpora are wildly imbalanced.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_why_does_language_sampling_matter" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords why, does, language, sampling, matter, much in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_mc4_dataset_english_alone_about`

- Preferred role: `content`
- Cue keywords: `mc4, dataset, english, alone, about, nine, point, seven, trillion, characters`
- Narration: In the mC4 dataset, English alone has about nine point seven trillion characters, more than ninety-two thousand times the data available for the lowest-resource language, Yoruba.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_mc4_dataset_english_alone_about" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mc4, dataset, english, alone, about, nine in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_you_train_proportion_raw_tail`

- Preferred role: `content`
- Cue keywords: `you, train, proportion, raw, tail, languages, barely, register, all`
- Narration: If you train in proportion to the raw data, the tail languages barely register at all.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_you_train_proportion_raw_tail" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords you, train, proportion, raw, tail, languages in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_deciding_how_balance_them_open`

- Preferred role: `title`
- Cue keywords: `deciding, how, balance, them, open, expensive, question, field, default, answer`
- Narration: Deciding how to balance them is an open and expensive question, and the field's default answer, temperature-based sampling, had never actually been evaluated systematically across model scales.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c4_deciding_how_balance_them_open" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deciding, how, balance, them, open, expensive in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_temperature_sampling_reshapes_distri`

- Preferred role: `method`
- Cue keywords: `temperature, sampling, reshapes, distribution, single, exponent, tau, but, catch`
- Narration: Temperature sampling reshapes the data distribution using a single exponent, tau. But there is a catch.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_temperature_sampling_reshapes_distri" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords temperature, sampling, reshapes, distribution, single, exponent in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_when_you_tune_tau_give`

- Preferred role: `content`
- Cue keywords: `when, you, tune, tau, give, head, languages, more, presence, you`
- Narration: When you tune tau to give the head languages more presence, you end up over-repeating the tail.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_when_you_tune_tau_give" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, you, tune, tau, give, head in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_tau_equals_three_point_three`

- Preferred role: `content`
- Cue keywords: `tau, equals, three, point, three, three, trillion-token, budget, lowest-resource, languages`
- Narration: At tau equals three point three three, with a trillion-token budget, the lowest-resource languages get repeated more than a hundred times.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_tau_equals_three_point_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tau, equals, three, point, three, three in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_much_repetition_causes_overfitting_h`

- Preferred role: `method`
- Cue keywords: `much, repetition, causes, overfitting, hurts, downstream, tasks, raises, risk, memorizing`
- Narration: That much repetition causes overfitting that hurts downstream tasks, it raises the risk of memorizing private content, and it wastes compute on duplicate examples, and every one of these harms only gets worse as models scale.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_much_repetition_causes_overfitting_h" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords much, repetition, causes, overfitting, hurts, downstream in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_unimax_makes_four_contributions_firs`

- Preferred role: `method`
- Cue keywords: `unimax, makes, four, contributions, first, method, itself, which, allocates, budget`
- Narration: UniMax makes four contributions. First, the method itself, which allocates the training budget uniformly while capping how many times any single language repeats.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_unimax_makes_four_contributions_firs" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unimax, makes, four, contributions, first, method in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_extensive_ablation_sampling_s`

- Preferred role: `method`
- Cue keywords: `second, extensive, ablation, sampling, strategies, run, across, scales, systematic, study`
- Narration: Second, an extensive ablation of sampling strategies run across model scales, the systematic study the field had been missing.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_second_extensive_ablation_sampling_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, extensive, ablation, sampling, strategies, run in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_refreshed_mc4_corpus_twenty_ni`

- Preferred role: `content`
- Cue keywords: `third, refreshed, mc4, corpus, twenty-nine, trillion, characters, spanning, one, hundred`
- Narration: Third, a refreshed mC4 corpus of twenty-nine trillion characters spanning one hundred seven languages.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_third_refreshed_mc4_corpus_twenty_ni" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, refreshed, mc4, corpus, twenty-nine, trillion in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_fourth_released_umt5_checkpoints_tra`

- Preferred role: `method`
- Cue keywords: `fourth, released, umt5, checkpoints, trained, unimax, practitioners, build, work, directly`
- Narration: And fourth, released umT5 checkpoints trained with UniMax, so practitioners can build on this work directly.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_fourth_released_umt5_checkpoints_tra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fourth, released, umt5, checkpoints, trained, unimax in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_how_unimax_works_name_means`

- Preferred role: `method`
- Cue keywords: `how, unimax, works, name, means, uniform, plus, max, you, start`
- Narration: Here is how UniMax works. The name means uniform plus max. You start from a fixed character budget, C, and distribute it as uniformly as possible across the languages, processing them from lowest to highest resource.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_how_unimax_works_name_means" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, unimax, works, name, means, uniform in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_step_algorithm_checks_whether_remain`

- Preferred role: `content`
- Cue keywords: `step, algorithm, checks, whether, remaining, per-language, budget, still, split, evenly`
- Narration: At each step, the algorithm checks whether the remaining per-language budget can still be split evenly.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_step_algorithm_checks_whether_remain" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords step, algorithm, checks, whether, remaining, per-language in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_language_would_exceed_epochs_over`

- Preferred role: `method`
- Cue keywords: `language, would, exceed, epochs, over, its, own, corpus, capped, epochs`
- Narration: If a language would exceed N epochs over its own corpus, it is capped at N epochs, and the freed budget is redistributed uniformly among the languages that remain.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_language_would_exceed_epochs_over" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords language, would, exceed, epochs, over, its in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_result_more_uniform_coverage_head`

- Preferred role: `result`
- Cue keywords: `result, more, uniform, coverage, head, languages, while, tail, language, ever`
- Narration: The result is more uniform coverage of the head languages, while no tail language is ever repeated more than N times. With the default of N equals one, nothing repeats at all.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c4_result_more_uniform_coverage_head" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, more, uniform, coverage, head, languages in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset and Benchmark

### Cue 1: `cue_s06_c1_evaluation_pretraining_refreshed_mc4`

- Preferred role: `method`
- Cue keywords: `evaluation, pretraining, refreshed, mc4, corpus, twenty-nine, trillion, characters, across, one`
- Narration: For evaluation, pretraining uses that refreshed mC4 corpus, twenty-nine trillion characters across one hundred seven languages.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_evaluation_pretraining_refreshed_mc4" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, pretraining, refreshed, mc4, corpus, twenty-nine in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_trained_models_tested_broad_suite`

- Preferred role: `method`
- Cue keywords: `trained, models, tested, broad, suite, tasks, tydi, goldp, wmt21, multilingual`
- Narration: The trained models are then tested on a broad suite of tasks: TyDi QA GoldP, WMT21 multilingual translation, XNLI, XQuAD, MLQA, and PAWS-X.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_trained_models_tested_broad_suite" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trained, models, tested, broad, suite, tasks in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_crucially_every_sampling_strategy_co`

- Preferred role: `method`
- Cue keywords: `crucially, every, sampling, strategy, compared, while, sweeping, scale, small, all`
- Narration: Crucially, every sampling strategy is compared while sweeping the model scale from Small all the way up to XXL, so the study can isolate whether the benefits actually persist as the models get bigger.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_crucially_every_sampling_strategy_co" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, every, sampling, strategy, compared, while in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_results_remarkably_consistent`

- Preferred role: `result`
- Cue keywords: `results, remarkably, consistent`
- Narration: And the results are remarkably consistent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_results_remarkably_consistent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, remarkably, consistent in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_unimax_outperforms_both_temperature`

- Preferred role: `result`
- Cue keywords: `unimax, outperforms, both, temperature, settings, tau, equals, one, tau, equals`
- Narration: UniMax outperforms both temperature settings, tau equals one and tau equals three point three three, on average TyDi QA across all three model sizes, and it beats temperature sampling on WMT21 translation at every scale, with the majority of language pairs improving.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_unimax_outperforms_both_temperature" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unimax, outperforms, both, temperature, settings, tau in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_high_resource_languages_beats_tau_eq`

- Preferred role: `content`
- Cue keywords: `high-resource, languages, beats, tau, equals, three, point, three, three, only`
- Narration: On high-resource languages it beats tau equals three point three three, and only trails tau equals one at the very largest scale.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_high_resource_languages_beats_tau_eq" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords high-resource, languages, beats, tau, equals, three in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_low_resource_languages_wins_outright`

- Preferred role: `result`
- Cue keywords: `low-resource, languages, wins, outright, even, outperforming, tau, equals, three, point`
- Narration: On low-resource languages it wins outright, even outperforming tau equals three point three three on Swahili despite seeing fewer Swahili examples.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c4_low_resource_languages_wins_outright" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords low-resource, languages, wins, outright, even, outperforming in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_what_about_max_epoch_parameter_ablat`

- Preferred role: `method`
- Cue keywords: `what, about, max-epoch, parameter, ablating, over, one, five, ten, large`
- Narration: What about that max-epoch parameter, N? Ablating N over one, five, and ten on Large models gives TyDi QA scores of eighty-two point two, eighty-one point five, and eighty-one point eight.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_what_about_max_epoch_parameter_ablat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, about, max-epoch, parameter, ablating, over in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_disallowing_repeats_entirely_equals`

- Preferred role: `content`
- Cue keywords: `disallowing, repeats, entirely, equals, one, comes, out, best, though, effect`
- Narration: Disallowing repeats entirely, N equals one, comes out best, though the effect is small.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_disallowing_repeats_entirely_equals" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords disallowing, repeats, entirely, equals, one, comes in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_four_times_larger_budget_unimax_scor`

- Preferred role: `method`
- Cue keywords: `four-times-larger, budget, unimax, scores, eighty-three, point, one, versus, eighty-two, point`
- Narration: At a four-times-larger budget, UniMax scores eighty-three point one, versus eighty-two point eight for temperature and eighty-one point two for tau equals one.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_four_times_larger_budget_unimax_scor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords four-times-larger, budget, unimax, scores, eighty-three, point in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_loss_curves_tell_story_high_temperat`

- Preferred role: `figure`
- Cue keywords: `loss, curves, tell, story, high-temperature, overfitting, grows, more, severe, scale`
- Narration: The loss curves tell the story: high-temperature overfitting grows more severe with scale, while UniMax stays stable.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c4_loss_curves_tell_story_high_temperat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords loss, curves, tell, story, high-temperature, overfitting in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_let_put_headline_numbers_together`

- Preferred role: `content`
- Cue keywords: `let, put, headline, numbers, together`
- Narration: Let us put the headline numbers together.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_let_put_headline_numbers_together" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords let, put, headline, numbers, together in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_refreshed_mc4_twenty_nine_trillion_c`

- Preferred role: `content`
- Cue keywords: `refreshed, mc4, twenty-nine, trillion, characters, across, one, hundred, seven, languages`
- Narration: The refreshed mC4 has twenty-nine trillion characters across one hundred seven languages, a thirty-five percent size increase.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_refreshed_mc4_twenty_nine_trillion_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords refreshed, mc4, twenty-nine, trillion, characters, across in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_tydi_larger_budget_unimax_scores`

- Preferred role: `method`
- Cue keywords: `tydi, larger, budget, unimax, scores, eighty-three, point, one, ahead, both`
- Narration: On TyDi QA at the larger budget, UniMax scores eighty-three point one, ahead of both baselines. The umT5 XXL checkpoint beats the earlier mT5 XXL on TyDi QA.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_tydi_larger_budget_unimax_scores" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tydi, larger, budget, unimax, scores, eighty-three in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_remember_tau_equals_three_point`

- Preferred role: `content`
- Cue keywords: `remember, tau, equals, three, point, three, three, lowest-resource, languages, being`
- Narration: And remember, at tau equals three point three three, the lowest-resource languages were being repeated more than a hundred times over.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_remember_tau_equals_three_point" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords remember, tau, equals, three, point, three in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple`
- Narration: The takeaway is simple.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_capping_per_language_repeats_spreadi`

- Preferred role: `method`
- Cue keywords: `capping, per-language, repeats, spreading, rest, budget, uniformly, beats, temperature, sampling`
- Narration: Capping per-language repeats, and spreading the rest of the budget uniformly, beats temperature sampling for multilingual pretraining, and that advantage holds as models scale.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_capping_per_language_repeats_spreadi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords capping, per-language, repeats, spreading, rest, budget in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_unimax_drop_in_hyperparameter_light`

- Preferred role: `content`
- Cue keywords: `unimax, drop-in, hyperparameter-light, replacement, temperature, sampling, ships, refreshed, corpus, umt5`
- Narration: UniMax is a drop-in, hyperparameter-light replacement for temperature sampling, and it ships with a refreshed corpus and umT5 checkpoints you can use today.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_unimax_drop_in_hyperparameter_light" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unimax, drop-in, hyperparameter-light, replacement, temperature, sampling in title/desc so the matcher can verify semantic overlap.
