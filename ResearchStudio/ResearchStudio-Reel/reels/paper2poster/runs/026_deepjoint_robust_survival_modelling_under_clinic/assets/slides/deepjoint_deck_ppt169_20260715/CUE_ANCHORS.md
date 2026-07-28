# CUE_ANCHORS — exact anchor ids to embed per slide

For each chunk create a top-level `<g id="<anchor_id>">` wrapping the visible content region it describes, with a child `<desc>` containing the keywords.

## Slide 01 — title (Title)
- `cue_s01_c1_deepjoint_robust_survival_clinical`
  - talks about: DeepJoint is a robust survival model for clinical data.
  - <desc> keywords: deepjoint, robust, survival, clinical
- `cue_s01_c2_medicine_when_which_tests_get`
  - talks about: In medicine, when and which tests get ordered is itself informative, reflecting how clinicians treat patients, a phenomenon the authors call clinical presence.
  - <desc> keywords: medicine, when, which, tests, get, ordered, itself, informative, reflecting, how
- `cue_s01_c3_when_these_patterns_shift_standard`
  - talks about: When these patterns shift, standard prediction models degrade.
  - <desc> keywords: when, these, patterns, shift, standard, prediction, models, degrade
- `cue_s01_c4_deepjoint_multi_task_recurrent_netwo`
  - talks about: DeepJoint is a multi-task recurrent network that models three clinical presence processes jointly with survival, delivering both strong discrimination and greater robustness.
  - <desc> keywords: deepjoint, multi-task, recurrent, network, models, three, clinical, presence, processes, jointly

## Slide 02 — problem (Problem)
- `cue_s02_c1_observational_medical_arise_interact`
  - talks about: Observational medical data arise from the interaction between patients and the healthcare system.
  - <desc> keywords: observational, medical, arise, interaction, between, patients, healthcare, system
- `cue_s02_c2_when_clinician_orders_test_its`
  - talks about: When a clinician orders a test, its timing and its existence carry information about the patient.
  - <desc> keywords: when, clinician, orders, test, its, timing, its, existence, carry, information
- `cue_s02_c3_most_models_ignore_assuming_sampling`
  - talks about: Most models ignore this, assuming sampling is non-informative.
  - <desc> keywords: most, models, ignore, assuming, sampling, non-informative
- `cue_s02_c4_ignoring_clinical_presence_yields_su`
  - talks about: Ignoring clinical presence yields sub-optimal, non-transportable models; modelling it explicitly is the fix.
  - <desc> keywords: ignoring, clinical, presence, yields, sub-optimal, non-transportable, models, modelling, explicitly, fix

## Slide 03 — motivation (Motivation)
- `cue_s03_c1_key_challenge_heterogeneity_same_pat`
  - talks about: A key challenge is heterogeneity: the same patient population can appear very differently depending on the observation process, and that process shifts across countries, over time, and even between weekdays and weekends.
  - <desc> keywords: key, challenge, heterogeneity, same, patient, population, appear, very, differently, depending
- `cue_s03_c2_literature_studied_covariate_label_s`
  - talks about: The literature has studied covariate and label shift, but shift in the observation process itself is under-explored.
  - <desc> keywords: literature, studied, covariate, label, shift, but, shift, observation, process, itself
- `cue_s03_c3_deepjoint_asks_how_explicitly_modell`
  - talks about: DeepJoint asks how explicitly modelling clinical presence makes survival models more robust to it.
  - <desc> keywords: deepjoint, asks, how, explicitly, modelling, clinical, presence, makes, survival, models

## Slide 04 — contribution (Contribution)
- `cue_s04_c1_contributes_deep_joint_treats_clinic`
  - talks about: The paper contributes a deep joint model that treats clinical presence as multi-task learning.
  - <desc> keywords: contributes, deep, joint, treats, clinical, presence, multi-task, learning
- `cue_s04_c2_shared_recurrent_embedding_feeds_fou`
  - talks about: A shared recurrent embedding feeds four heads: longitudinal, inter-observation timing, missingness, and survival, all trained together by maximising a combined likelihood with dynamic weighting.
  - <desc> keywords: shared, recurrent, embedding, feeds, four, heads, longitudinal, inter-observation, timing, missingness
- `cue_s04_c3_result_representation_encodes_observ`
  - talks about: The result is a representation that encodes the observation process, giving both a predictive edge and robustness when that process changes.
  - <desc> keywords: result, representation, encodes, observation, process, giving, both, predictive, edge, robustness

## Slide 05 — method (Method)
- `cue_s05_c1_long_short_term_memory_network`
  - talks about: A Long Short Term Memory network extracts an embedding from each patient's irregular sequence of laboratory tests.
  - <desc> keywords: long, short, term, memory, network, extracts, embedding, patient, irregular, sequence
- `cue_s05_c2_embedding_drives_three_clinical_pres`
  - talks about: This embedding drives three clinical-presence heads: a longitudinal head predicting next test values under a Gaussian likelihood, a missingness head predicting which tests appear under a Bernoulli likelihood, and a timing head modelling the inter-observation intensity.
  - <desc> keywords: embedding, drives, three, clinical-presence, heads, longitudinal, head, predicting, next, test
- `cue_s05_c3_deepsurv_head_models_survival_under`
  - talks about: A DeepSurv head models survival under Cox proportional hazards.
  - <desc> keywords: deepsurv, head, models, survival, under, cox, proportional, hazards
- `cue_s05_c4_four_losses_combined_dynamic_weighti`
  - talks about: The four losses are combined by dynamic weighting, balanced by a hyperparameter alpha, and optimised end to end.
  - <desc> keywords: four, losses, combined, dynamic, weighting, balanced, hyperparameter, alpha, optimised, end

## Slide 06 — dataset-benchmark (Dataset / Benchmark)
- `cue_s06_c1_experiments_mimic_three_intensive_ca`
  - talks about: Experiments use MIMIC-three, an intensive-care database of anonymised laboratory tests for over thirty-eight thousand patients at Beth Israel Deaconess between 2001 and 2012.
  - <desc> keywords: experiments, mimic-three, intensive-care, database, anonymised, laboratory, tests, over, thirty-eight, thousand
- `cue_s06_c2_restricting_those_surviving_first_tw`
  - talks about: Restricting to those surviving the first twenty-four hours leaves a cohort of 30,834 patients.
  - <desc> keywords: restricting, those, surviving, first, twenty-four, hours, leaves, cohort, 30, 834
- `cue_s06_c3_models_predict_in_hospital_survival`
  - talks about: Models predict in-hospital survival from the embedding at the last observation in that first day, compared by time-dependent concordance index and Brier score at one, seven, and fourteen days.
  - <desc> keywords: models, predict, in-hospital, survival, embedding, last, observation, first, day, compared

## Slide 07 — key-result (Key Result)
- `cue_s07_c1_random_population_split_three_propos`
  - talks about: On a random population split, the three proposed methods deliver competitive-to-best discrimination against models using the same inputs.
  - <desc> keywords: random, population, split, three, proposed, methods, deliver, competitive-to-best, discrimination, against
- `cue_s07_c2_strikingly_deepjoint_which_sees_only`
  - talks about: Strikingly, DeepJoint, which sees only laboratory values, already outperforms both an LSTM that ignores clinical presence and GRU-D, which consumes missingness as input.
  - <desc> keywords: strikingly, deepjoint, which, sees, only, laboratory, values, already, outperforms, both
- `cue_s07_c3_modelling_observation_process_even_w`
  - talks about: So modelling the observation process, even without feeding it in, yields a more predictive embedding.
  - <desc> keywords: modelling, observation, process, even, without, feeding, yields, more, predictive, embedding
- `cue_s07_c4_fine_tuning_adds_further_edge_reachi`
  - talks about: Fine-tuning adds a further edge, reaching a one-day C-index of 0.878.
  - <desc> keywords: fine-tuning, adds, further, edge, reaching, one-day, c-index, 0.878

## Slide 08 — ablation-study (Ablation Study)
- `cue_s08_c1_approach_decomposes_three_variants_a`
  - talks about: The approach decomposes into three variants against six baselines.
  - <desc> keywords: approach, decomposes, three, variants, against, six, baselines
- `cue_s08_c2_deepjointfeature_which_adds_clinical`
  - talks about: DeepJointFeature, which adds clinical-presence features to the joint model, improves over plain DeepJoint and matches a strong feature baseline.
  - <desc> keywords: deepjointfeature, which, adds, clinical-presence, features, joint, improves, over, plain, deepjoint
- `cue_s08_c3_fine_tuned_variant_reaches_highest_p`
  - talks about: The fine-tuned variant reaches the highest population-level discrimination but overfits when the observation process shifts.
  - <desc> keywords: fine-tuned, variant, reaches, highest, population-level, discrimination, but, overfits, when, observation
- `cue_s08_c4_across_robustness_experiment_deepjoi`
  - talks about: Across the robustness experiment, DeepJointFeature best combines strong discrimination with proximity to the diagonal, transferring most reliably across settings.
  - <desc> keywords: across, robustness, experiment, deepjointfeature, best, combines, strong, discrimination, proximity, diagonal

## Slide 09 — headline-numbers (Headline Numbers)
- `cue_s09_c1_headline_numbers_concordance_index_0`
  - talks about: The headline numbers: a concordance index of 0.878 at the one-day horizon, on a cohort of 30,834 MIMIC-three patients.
  - <desc> keywords: headline, numbers, concordance, index, 0.878, one-day, horizon, cohort, 30, 834
- `cue_s09_c2_deepjoint_jointly_captures_three_dim`
  - talks about: DeepJoint jointly captures three dimensions of clinical presence, longitudinal, timing, and missingness, alongside survival, across horizons of one, seven, and fourteen days.
  - <desc> keywords: deepjoint, jointly, captures, three, dimensions, clinical, presence, longitudinal, timing, missingness

## Slide 10 — takeaway (Takeaway)
- `cue_s10_c1_takeaway_way_clinical_sampled_itself`
  - talks about: The takeaway: the way clinical data are sampled is itself informative, and jointly modelling that observation process with survival produces predictions that are both more accurate and markedly more robust when clinical practice changes.
  - <desc> keywords: takeaway, way, clinical, sampled, itself, informative, jointly, modelling, observation, process
- `cue_s10_c2_clinical_presence_signal_not_noise`
  - talks about: Clinical presence is signal, not noise, and modelling it makes medical predictions transportable.
  - <desc> keywords: clinical, presence, signal, not, noise, modelling, makes, medical, predictions, transportable
