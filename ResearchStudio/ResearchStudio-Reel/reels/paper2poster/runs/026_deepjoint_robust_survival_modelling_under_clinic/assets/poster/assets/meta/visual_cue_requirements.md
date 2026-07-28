# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_deepjoint_robust_survival_clinical`

- Preferred role: `content`
- Cue keywords: `deepjoint, robust, survival, clinical`
- Narration: DeepJoint is a robust survival model for clinical data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_deepjoint_robust_survival_clinical" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deepjoint, robust, survival, clinical in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_medicine_when_which_tests_get`

- Preferred role: `content`
- Cue keywords: `medicine, when, which, tests, get, ordered, itself, informative, reflecting, how`
- Narration: In medicine, when and which tests get ordered is itself informative, reflecting how clinicians treat patients, a phenomenon the authors call clinical presence.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_medicine_when_which_tests_get" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords medicine, when, which, tests, get, ordered in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_when_these_patterns_shift_standard`

- Preferred role: `content`
- Cue keywords: `when, these, patterns, shift, standard, prediction, models, degrade`
- Narration: When these patterns shift, standard prediction models degrade.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_when_these_patterns_shift_standard" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, these, patterns, shift, standard, prediction in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_deepjoint_multi_task_recurrent_netwo`

- Preferred role: `method`
- Cue keywords: `deepjoint, multi-task, recurrent, network, models, three, clinical, presence, processes, jointly`
- Narration: DeepJoint is a multi-task recurrent network that models three clinical presence processes jointly with survival, delivering both strong discrimination and greater robustness.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_deepjoint_multi_task_recurrent_netwo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deepjoint, multi-task, recurrent, network, models, three in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_observational_medical_arise_interact`

- Preferred role: `content`
- Cue keywords: `observational, medical, arise, interaction, between, patients, healthcare, system`
- Narration: Observational medical data arise from the interaction between patients and the healthcare system.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_observational_medical_arise_interact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords observational, medical, arise, interaction, between, patients in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_when_clinician_orders_test_its`

- Preferred role: `content`
- Cue keywords: `when, clinician, orders, test, its, timing, its, existence, carry, information`
- Narration: When a clinician orders a test, its timing and its existence carry information about the patient.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_when_clinician_orders_test_its" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, clinician, orders, test, its, timing in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_most_models_ignore_assuming_sampling`

- Preferred role: `content`
- Cue keywords: `most, models, ignore, assuming, sampling, non-informative`
- Narration: Most models ignore this, assuming sampling is non-informative.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_most_models_ignore_assuming_sampling" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords most, models, ignore, assuming, sampling, non-informative in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_ignoring_clinical_presence_yields_su`

- Preferred role: `content`
- Cue keywords: `ignoring, clinical, presence, yields, sub-optimal, non-transportable, models, modelling, explicitly, fix`
- Narration: Ignoring clinical presence yields sub-optimal, non-transportable models; modelling it explicitly is the fix.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_ignoring_clinical_presence_yields_su" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ignoring, clinical, presence, yields, sub-optimal, non-transportable in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_key_challenge_heterogeneity_same_pat`

- Preferred role: `content`
- Cue keywords: `key, challenge, heterogeneity, same, patient, population, appear, very, differently, depending`
- Narration: A key challenge is heterogeneity: the same patient population can appear very differently depending on the observation process, and that process shifts across countries, over time, and even between weekdays and weekends.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_key_challenge_heterogeneity_same_pat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, challenge, heterogeneity, same, patient, population in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_literature_studied_covariate_label_s`

- Preferred role: `content`
- Cue keywords: `literature, studied, covariate, label, shift, but, shift, observation, process, itself`
- Narration: The literature has studied covariate and label shift, but shift in the observation process itself is under-explored.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_literature_studied_covariate_label_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords literature, studied, covariate, label, shift, but in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_deepjoint_asks_how_explicitly_modell`

- Preferred role: `title`
- Cue keywords: `deepjoint, asks, how, explicitly, modelling, clinical, presence, makes, survival, models`
- Narration: DeepJoint asks how explicitly modelling clinical presence makes survival models more robust to it.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s03_c3_deepjoint_asks_how_explicitly_modell" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deepjoint, asks, how, explicitly, modelling, clinical in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_contributes_deep_joint_treats_clinic`

- Preferred role: `content`
- Cue keywords: `contributes, deep, joint, treats, clinical, presence, multi-task, learning`
- Narration: The paper contributes a deep joint model that treats clinical presence as multi-task learning.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_contributes_deep_joint_treats_clinic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords contributes, deep, joint, treats, clinical, presence in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_shared_recurrent_embedding_feeds_fou`

- Preferred role: `method`
- Cue keywords: `shared, recurrent, embedding, feeds, four, heads, longitudinal, inter-observation, timing, missingness`
- Narration: A shared recurrent embedding feeds four heads: longitudinal, inter-observation timing, missingness, and survival, all trained together by maximising a combined likelihood with dynamic weighting.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_shared_recurrent_embedding_feeds_fou" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords shared, recurrent, embedding, feeds, four, heads in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_result_representation_encodes_observ`

- Preferred role: `result`
- Cue keywords: `result, representation, encodes, observation, process, giving, both, predictive, edge, robustness`
- Narration: The result is a representation that encodes the observation process, giving both a predictive edge and robustness when that process changes.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c3_result_representation_encodes_observ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, representation, encodes, observation, process, giving in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_long_short_term_memory_network`

- Preferred role: `content`
- Cue keywords: `long, short, term, memory, network, extracts, embedding, patient, irregular, sequence`
- Narration: A Long Short Term Memory network extracts an embedding from each patient's irregular sequence of laboratory tests.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_long_short_term_memory_network" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords long, short, term, memory, network, extracts in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_embedding_drives_three_clinical_pres`

- Preferred role: `method`
- Cue keywords: `embedding, drives, three, clinical-presence, heads, longitudinal, head, predicting, next, test`
- Narration: This embedding drives three clinical-presence heads: a longitudinal head predicting next test values under a Gaussian likelihood, a missingness head predicting which tests appear under a Bernoulli likelihood, and a timing head modelling the inter-observation intensity.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_embedding_drives_three_clinical_pres" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords embedding, drives, three, clinical-presence, heads, longitudinal in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_deepsurv_head_models_survival_under`

- Preferred role: `content`
- Cue keywords: `deepsurv, head, models, survival, under, cox, proportional, hazards`
- Narration: A DeepSurv head models survival under Cox proportional hazards.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_deepsurv_head_models_survival_under" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deepsurv, head, models, survival, under, cox in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_four_losses_combined_dynamic_weighti`

- Preferred role: `figure`
- Cue keywords: `four, losses, combined, dynamic, weighting, balanced, hyperparameter, alpha, optimised, end`
- Narration: The four losses are combined by dynamic weighting, balanced by a hyperparameter alpha, and optimised end to end.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c4_four_losses_combined_dynamic_weighti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords four, losses, combined, dynamic, weighting, balanced in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_mimic_three_intensive_ca`

- Preferred role: `content`
- Cue keywords: `experiments, mimic-three, intensive-care, database, anonymised, laboratory, tests, over, thirty-eight, thousand`
- Narration: Experiments use MIMIC-three, an intensive-care database of anonymised laboratory tests for over thirty-eight thousand patients at Beth Israel Deaconess between 2001 and 2012.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_experiments_mimic_three_intensive_ca" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, mimic-three, intensive-care, database, anonymised, laboratory in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_restricting_those_surviving_first_tw`

- Preferred role: `method`
- Cue keywords: `restricting, those, surviving, first, twenty-four, hours, leaves, cohort, 30, 834`
- Narration: Restricting to those surviving the first twenty-four hours leaves a cohort of 30,834 patients.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_restricting_those_surviving_first_tw" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords restricting, those, surviving, first, twenty-four, hours in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_models_predict_in_hospital_survival`

- Preferred role: `method`
- Cue keywords: `models, predict, in-hospital, survival, embedding, last, observation, first, day, compared`
- Narration: Models predict in-hospital survival from the embedding at the last observation in that first day, compared by time-dependent concordance index and Brier score at one, seven, and fourteen days.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_models_predict_in_hospital_survival" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords models, predict, in-hospital, survival, embedding, last in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_random_population_split_three_propos`

- Preferred role: `method`
- Cue keywords: `random, population, split, three, proposed, methods, deliver, competitive-to-best, discrimination, against`
- Narration: On a random population split, the three proposed methods deliver competitive-to-best discrimination against models using the same inputs.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_random_population_split_three_propos" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords random, population, split, three, proposed, methods in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_strikingly_deepjoint_which_sees_only`

- Preferred role: `method`
- Cue keywords: `strikingly, deepjoint, which, sees, only, laboratory, values, already, outperforms, both`
- Narration: Strikingly, DeepJoint, which sees only laboratory values, already outperforms both an LSTM that ignores clinical presence and GRU-D, which consumes missingness as input.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_strikingly_deepjoint_which_sees_only" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords strikingly, deepjoint, which, sees, only, laboratory in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_modelling_observation_process_even_w`

- Preferred role: `content`
- Cue keywords: `modelling, observation, process, even, without, feeding, yields, more, predictive, embedding`
- Narration: So modelling the observation process, even without feeding it in, yields a more predictive embedding.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_modelling_observation_process_even_w" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords modelling, observation, process, even, without, feeding in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_fine_tuning_adds_further_edge_reachi`

- Preferred role: `content`
- Cue keywords: `fine-tuning, adds, further, edge, reaching, one-day, c-index, 0.878`
- Narration: Fine-tuning adds a further edge, reaching a one-day C-index of 0.878.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_fine_tuning_adds_further_edge_reachi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fine-tuning, adds, further, edge, reaching, one-day in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_approach_decomposes_three_variants_a`

- Preferred role: `result`
- Cue keywords: `approach, decomposes, three, variants, against, six, baselines`
- Narration: The approach decomposes into three variants against six baselines.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c1_approach_decomposes_three_variants_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords approach, decomposes, three, variants, against, six in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_deepjointfeature_which_adds_clinical`

- Preferred role: `method`
- Cue keywords: `deepjointfeature, which, adds, clinical-presence, features, joint, improves, over, plain, deepjoint`
- Narration: DeepJointFeature, which adds clinical-presence features to the joint model, improves over plain DeepJoint and matches a strong feature baseline.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_deepjointfeature_which_adds_clinical" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deepjointfeature, which, adds, clinical-presence, features, joint in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_fine_tuned_variant_reaches_highest_p`

- Preferred role: `result`
- Cue keywords: `fine-tuned, variant, reaches, highest, population-level, discrimination, but, overfits, when, observation`
- Narration: The fine-tuned variant reaches the highest population-level discrimination but overfits when the observation process shifts.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c3_fine_tuned_variant_reaches_highest_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fine-tuned, variant, reaches, highest, population-level, discrimination in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_across_robustness_experiment_deepjoi`

- Preferred role: `method`
- Cue keywords: `across, robustness, experiment, deepjointfeature, best, combines, strong, discrimination, proximity, diagonal`
- Narration: Across the robustness experiment, DeepJointFeature best combines strong discrimination with proximity to the diagonal, transferring most reliably across settings.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_across_robustness_experiment_deepjoi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, robustness, experiment, deepjointfeature, best, combines in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_headline_numbers_concordance_index_0`

- Preferred role: `content`
- Cue keywords: `headline, numbers, concordance, index, 0.878, one-day, horizon, cohort, 30, 834`
- Narration: The headline numbers: a concordance index of 0.878 at the one-day horizon, on a cohort of 30,834 MIMIC-three patients.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_headline_numbers_concordance_index_0" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, numbers, concordance, index, 0.878, one-day in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_deepjoint_jointly_captures_three_dim`

- Preferred role: `content`
- Cue keywords: `deepjoint, jointly, captures, three, dimensions, clinical, presence, longitudinal, timing, missingness`
- Narration: DeepJoint jointly captures three dimensions of clinical presence, longitudinal, timing, and missingness, alongside survival, across horizons of one, seven, and fourteen days.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_deepjoint_jointly_captures_three_dim" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deepjoint, jointly, captures, three, dimensions, clinical in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_way_clinical_sampled_itself`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, way, clinical, sampled, itself, informative, jointly, modelling, observation, process`
- Narration: The takeaway: the way clinical data are sampled is itself informative, and jointly modelling that observation process with survival produces predictions that are both more accurate and markedly more robust when clinical practice changes.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_way_clinical_sampled_itself" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, way, clinical, sampled, itself, informative in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_clinical_presence_signal_not_noise`

- Preferred role: `content`
- Cue keywords: `clinical, presence, signal, not, noise, modelling, makes, medical, predictions, transportable`
- Narration: Clinical presence is signal, not noise, and modelling it makes medical predictions transportable.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_clinical_presence_signal_not_noise" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords clinical, presence, signal, not, noise, modelling in title/desc so the matcher can verify semantic overlap.
