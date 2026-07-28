# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_fake_audio_detectors_work_well`

- Preferred role: `method`
- Cue keywords: `fake, audio, detectors, work, well, they, trained, but, their, accuracy`
- Narration: Fake audio detectors work well on the data they were trained on, but their accuracy collapses when they meet audio from a new dataset.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_fake_audio_detectors_work_well" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fake, audio, detectors, work, well, they in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_fine_tuning_new_makes_them_forget`

- Preferred role: `method`
- Cue keywords: `fine-tuning, new, makes, them, forget, old, problem, called, catastrophic, forgetting`
- Narration: Fine-tuning on the new data then makes them forget the old, a problem called catastrophic forgetting.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_fine_tuning_new_makes_them_forget" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fine-tuning, new, makes, them, forget, old in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_icml_2023_introduces_regularized_ada`

- Preferred role: `method`
- Cue keywords: `icml, 2023, introduces, regularized, adaptive, weight, modification, rawm, continual, learning`
- Narration: This ICML 2023 paper introduces Regularized Adaptive Weight Modification, or RAWM, a continual learning method that adapts how it modifies network weights based on the ratio of genuine to fake utterances, and adds a regularization term so the model remembers the feature distribution of earlier datasets.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_icml_2023_introduces_regularized_ada" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords icml, 2023, introduces, regularized, adaptive, weight in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_without_replaying_any_past_samples`

- Preferred role: `content`
- Cue keywords: `without, replaying, any, past, samples, rawm, cuts, forgetting, roughly, one`
- Narration: Without replaying any past samples, RAWM cuts forgetting to roughly one tenth of naive fine-tuning and even generalizes beyond audio to speech emotion recognition and image recognition.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c4_without_replaying_any_past_samples" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords without, replaying, any, past, samples, rawm in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_fake_audio_detection_become_critical`

- Preferred role: `result`
- Cue keywords: `fake, audio, detection, become, critical, speech, synthesis, voice, conversion, produce`
- Narration: Fake audio detection has become critical as speech synthesis and voice conversion produce human-like speech.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c1_fake_audio_detection_become_critical" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fake, audio, detection, become, critical, speech in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_detectors_perform_well_their_own`

- Preferred role: `result`
- Cue keywords: `detectors, perform, well, their, own, dataset, but, their, equal, error`
- Narration: Detectors perform well on their own dataset, but their equal error rate rises dramatically on audio from another dataset.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c2_detectors_perform_well_their_own" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords detectors, perform, well, their, own, dataset in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_obvious_fix_fine_tuning_new_causes`

- Preferred role: `content`
- Cue keywords: `obvious, fix, fine-tuning, new, causes, network, forget, what, learned, before`
- Narration: The obvious fix, fine-tuning on the new data, causes the network to forget what it learned before.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_obvious_fix_fine_tuning_new_causes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords obvious, fix, fine-tuning, new, causes, network in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_earlier_remedies_require_replaying_o`

- Preferred role: `content`
- Cue keywords: `earlier, remedies, require, replaying, old, samples, which, impractical, when, original`
- Narration: Earlier remedies require replaying old samples, which is impractical when the original data is inaccessible.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_earlier_remedies_require_replaying_o" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords earlier, remedies, require, replaying, old, samples in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_existing_weight_modification_methods`

- Preferred role: `method`
- Cue keywords: `existing, weight-modification, methods, like, owm, treat, every, input, same, when`
- Narration: Existing weight-modification methods like OWM treat every input the same when constraining updates.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_existing_weight_modification_methods" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords existing, weight-modification, methods, like, owm, treat in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_but_fake_audio_detection_genuine`

- Preferred role: `result`
- Cue keywords: `but, fake, audio, detection, genuine, speech, tends, look, similar, one`
- Narration: But in fake audio detection, genuine speech tends to look similar from one dataset to the next, while the fake speech varies.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c2_but_fake_audio_detection_genuine" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, fake, audio, detection, genuine, speech in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_regularity_opportunity_direction_wei`

- Preferred role: `content`
- Cue keywords: `regularity, opportunity, direction, weight, update, should, adapt, how, much, batch`
- Narration: That regularity is an opportunity: the direction of a weight update should adapt to how much of a batch is genuine versus fake.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_regularity_opportunity_direction_wei" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords regularity, opportunity, direction, weight, update, should in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_same_time_some_datasets_collect`

- Preferred role: `guidance`
- Cue keywords: `same, time, some, datasets, collect, genuine, audio, under, acoustic, conditions`
- Narration: At the same time, some datasets collect genuine audio under acoustic conditions so different that a naive rule backfires, motivating an extra safeguard.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s03_c4_same_time_some_datasets_collect" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords same, time, some, datasets, collect, genuine in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_authors_contribute_regularized_adapt`

- Preferred role: `content`
- Cue keywords: `authors, contribute, regularized, adaptive, weight, modification, two, essential, steps`
- Narration: The authors contribute Regularized Adaptive Weight Modification. It has two essential steps.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_authors_contribute_regularized_adapt" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, contribute, regularized, adaptive, weight, modification in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_adaptive_weight_modification_i`

- Preferred role: `method`
- Cue keywords: `first, adaptive, weight, modification, introduces, extra, projector, adjusts, update, direction`
- Narration: First, adaptive weight modification introduces an extra projector that adjusts the update direction according to the ratio of classes with similar feature distribution, such as genuine utterances, to the others.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_adaptive_weight_modification_i" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, adaptive, weight, modification, introduces, extra in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_regularization_term_inspired`

- Preferred role: `method`
- Cue keywords: `second, regularization, term, inspired, learning, without, forgetting, keeps, new, inference`
- Narration: Second, a regularization term, inspired by learning without forgetting, keeps the new inference distribution close to the old one.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_regularization_term_inspired" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, regularization, term, inspired, learning, without in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_method_needs_previous_samples_author`

- Preferred role: `method`
- Cue keywords: `method, needs, previous, samples, authors, show, transfers, speech, emotion, recognition`
- Narration: The method needs no previous samples, and the authors show it transfers to speech emotion recognition and image recognition.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_method_needs_previous_samples_author" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, needs, previous, samples, authors, show in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_rawm_starts_orthogonal_projector_owm`

- Preferred role: `method`
- Cue keywords: `rawm, starts, orthogonal, projector, owm, which, points, update, away, subspace`
- Narration: RAWM starts from the orthogonal projector P of OWM, which points the update away from the subspace spanned by previous inputs. On top of it, the method builds a second projector Q that is orthogonal to P and scaled by the ratio beta of genuine to fake utterances in the batch.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_rawm_starts_orthogonal_projector_owm" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rawm, starts, orthogonal, projector, owm, which in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_two_projectors_normalized_combined_m`

- Preferred role: `content`
- Cue keywords: `two, projectors, normalized, combined, modified, direction, when, batch, mostly, genuine`
- Narration: The two projectors are normalized and combined into a modified direction R, so when a batch is mostly genuine the update leans toward preserving old knowledge, and otherwise it leans toward learning the new data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_two_projectors_normalized_combined_m" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, projectors, normalized, combined, modified, direction in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_datasets_recorded_under_very_differe`

- Preferred role: `method`
- Cue keywords: `datasets, recorded, under, very, different, conditions, regularization, term, treats, frozen`
- Narration: For datasets recorded under very different conditions, a regularization term treats the frozen pre-trained model as a teacher and forces the fine-tuned student to match its softened outputs, remembering the old inference distribution.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_datasets_recorded_under_very_differe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords datasets, recorded, under, very, different, conditions in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_crucially_none_replays_past_samples`

- Preferred role: `content`
- Cue keywords: `crucially, none, replays, past, samples`
- Narration: Crucially, none of this replays past samples.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_crucially_none_replays_past_samples" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, none, replays, past, samples in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_run_four_fake_audio`

- Preferred role: `content`
- Cue keywords: `experiments, run, four, fake, audio, datasets, continual-learning, sequence, asvspoof, 2019`
- Narration: Experiments run on four fake audio datasets in a continual-learning sequence: ASVspoof 2019 LA as the source, then ASVspoof 2015, the Voice Conversion Challenge 2020 set, and the In-the-Wild dataset.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_experiments_run_four_fake_audio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, run, four, fake, audio, datasets in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_distinct_acoustic_linguistic_conditi`

- Preferred role: `figure`
- Cue keywords: `distinct, acoustic, linguistic, condition, in-the-wild, being, real-world, deepfakes, public, figures`
- Narration: Each is a distinct acoustic and linguistic condition, with In-the-Wild being real-world deepfakes of public figures.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s06_c2_distinct_acoustic_linguistic_conditi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords distinct, acoustic, linguistic, condition, in-the-wild, being in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_detection_quality_reported_equal_err`

- Preferred role: `result`
- Cue keywords: `detection, quality, reported, equal, error, rate`
- Narration: Detection quality is reported as Equal Error Rate.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c3_detection_quality_reported_equal_err" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords detection, quality, reported, equal, error, rate in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_show_breadth_method_also_evaluated`

- Preferred role: `method`
- Cue keywords: `show, breadth, method, also, evaluated, speech, emotion, recognition, clear-10, image`
- Narration: To show breadth, the method is also evaluated on speech emotion recognition and on the CLEAR-10 image recognition benchmark.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_show_breadth_method_also_evaluated" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords show, breadth, method, also, evaluated, speech in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_finding_rawm_cuts_catastrop`

- Preferred role: `method`
- Cue keywords: `headline, finding, rawm, cuts, catastrophic, forgetting, roughly, one, tenth, naive`
- Narration: The headline finding is that RAWM cuts catastrophic forgetting to roughly one tenth of naive fine-tuning, while also halving the error on the new dataset.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_headline_finding_rawm_cuts_catastrop" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, finding, rawm, cuts, catastrophic, forgetting in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_across_two_dataset_four_dataset_sequ`

- Preferred role: `method`
- Cue keywords: `across, two-dataset, four-dataset, sequences, achieves, lowest, equal, error, rate, both`
- Narration: Across two-dataset and four-dataset sequences, it achieves the lowest equal error rate on both old and new datasets compared with mainstream continual learning methods including EWC, LwF, OWM, and the fake-audio-specific DFWF.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_across_two_dataset_four_dataset_sequ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, two-dataset, four-dataset, sequences, achieves, lowest in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_regularization_coefficient_set_one_h`

- Preferred role: `method`
- Cue keywords: `regularization, coefficient, set, one, half, giving, equal, attention, old, new`
- Narration: With the regularization coefficient set to one half, giving equal attention to old and new data, RAWM keeps error low across all four datasets even as a baseline collapses.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_regularization_coefficient_set_one_h" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords regularization, coefficient, set, one, half, giving in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablation_separates_two_components`

- Preferred role: `content`
- Cue keywords: `ablation, separates, two, components`
- Narration: An ablation separates the two components.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_ablation_separates_two_components" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablation, separates, two, components in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_when_old_new_datasets_share`

- Preferred role: `method`
- Cue keywords: `when, old, new, datasets, share, similar, feature, distribution, adaptive, weight`
- Narration: When old and new datasets share a similar feature distribution, adaptive weight modification does most of the work, and removing it sharply raises error.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_when_old_new_datasets_share" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, old, new, datasets, share, similar in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_when_datasets_recorded_under_very`

- Preferred role: `content`
- Cue keywords: `when, datasets, recorded, under, very, different, conditions, regularization, term, becomes`
- Narration: When the datasets are recorded under very different conditions, the regularization term becomes the key to overcoming forgetting.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_when_datasets_recorded_under_very" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, datasets, recorded, under, very, different in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_across_full_four_dataset_sequence_re`

- Preferred role: `content`
- Cue keywords: `across, full, four-dataset, sequence, removing, adaptive, weight, modification, hurts, more`
- Narration: Across the full four-dataset sequence, removing adaptive weight modification hurts more than removing regularization, so it is the primary driver, with regularization a valuable complement.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_across_full_four_dataset_sequence_re" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, full, four-dataset, sequence, removing, adaptive in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_numbers_forgetting_drops_about_one`

- Preferred role: `result`
- Cue keywords: `numbers, forgetting, drops, about, one, tenth, fine-tuning, new-dataset, error, about`
- Narration: In numbers: forgetting drops to about one tenth of fine-tuning, and new-dataset error to about one half.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_numbers_forgetting_drops_about_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords numbers, forgetting, drops, about, one, tenth in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_few_sample_regime_only_one_hundred`

- Preferred role: `method`
- Cue keywords: `few-sample, regime, only, one, hundred, new, samples, rawm, scores, equal`
- Narration: In the few-sample regime with only one hundred new samples, RAWM scores an equal error rate of zero point nine two on the old set and zero point three one on the new, far ahead of fine-tuning's near eight.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_few_sample_regime_only_one_hundred" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few-sample, regime, only, one, hundred, new in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_speech_emotion_recognition_reaches_a`

- Preferred role: `method`
- Cue keywords: `speech, emotion, recognition, reaches, about, forty-two, percent, accuracy, msp-podcast, fifty-four`
- Narration: On speech emotion recognition it reaches about forty-two percent accuracy on MSP-Podcast and fifty-four percent on IEMOCAP, the best of all continual learning methods tested.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_speech_emotion_recognition_reaches_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords speech, emotion, recognition, reaches, about, forty-two in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_optimal_regularization_weight_one_ha`

- Preferred role: `content`
- Cue keywords: `optimal, regularization, weight, one, half`
- Narration: The optimal regularization weight is one half.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_optimal_regularization_weight_one_ha" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords optimal, regularization, weight, one, half in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple_you_teach_fake`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple, you, teach, fake, audio, detector, new, datasets, without`
- Narration: The takeaway is simple: you can teach a fake audio detector new datasets without it forgetting the old, and without keeping any of the old data around.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple_you_teach_fake" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple, you, teach, fake, audio in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_rawm_does_making_weight_update`

- Preferred role: `content`
- Cue keywords: `rawm, does, making, weight, update, adapt, how, genuine-heavy, batch, regularizing`
- Narration: RAWM does this by making the weight update adapt to how genuine-heavy each batch is and by regularizing the model to remember its previous behavior.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_rawm_does_making_weight_update" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rawm, does, making, weight, update, adapt in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_because_underlying_regularity_some_c`

- Preferred role: `content`
- Cue keywords: `because, underlying, regularity, some, classes, staying, similar, across, datasets, appears`
- Narration: Because the underlying regularity, some classes staying similar across datasets, appears in many problems, the same recipe extends to speech emotion recognition and image recognition.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_because_underlying_regularity_some_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, underlying, regularity, some, classes, staying in title/desc so the matcher can verify semantic overlap.
