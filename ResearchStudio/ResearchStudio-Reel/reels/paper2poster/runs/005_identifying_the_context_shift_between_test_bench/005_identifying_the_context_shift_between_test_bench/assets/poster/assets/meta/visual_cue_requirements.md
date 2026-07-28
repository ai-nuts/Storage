# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_machine_learning_models_often_look`

- Preferred role: `result`
- Cue keywords: `machine, learning, models, often, look, excellent, benchmark, datasets, break, moment`
- Narration: Machine learning models often look excellent on benchmark datasets, then break the moment they hit real production data.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c1_machine_learning_models_often_look" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords machine, learning, models, often, look, excellent in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_matthew_groh_mit_media_lab`

- Preferred role: `method`
- Cue keywords: `matthew, groh, mit, media, lab, argues, usual, explanation, distribution, shift`
- Narration: This paper by Matthew Groh at the MIT Media Lab argues that the usual explanation, distribution shift, is the wrong frame.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_matthew_groh_mit_media_lab" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords matthew, groh, mit, media, lab, argues in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_distribution_shift_only_measures_two`

- Preferred role: `method`
- Cue keywords: `distribution, shift, only, measures, two, datasets, differ, never, tells, you`
- Narration: Distribution shift only measures that two datasets differ; it never tells you why.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_distribution_shift_only_measures_two" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords distribution, shift, only, measures, two, datasets in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_groh_introduces_context_shift_semant`

- Preferred role: `result`
- Cue keywords: `groh, introduces, context, shift, semantically, meaningful, changes, how, created, collected`
- Narration: Groh introduces context shift, the semantically meaningful changes in how data are created, collected, and curated that actually drive those failures, and lays out three concrete ways to address it: leaning on human intuition and expert knowledge, building dynamic benchmarks, and clearly stating a model's limitations.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c4_groh_introduces_context_shift_semant" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords groh, introduces, context, shift, semantically, meaningful in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_benchmark_datasets_play_two_roles`

- Preferred role: `method`
- Cue keywords: `benchmark, datasets, play, two, roles, they, let, researchers, compare, methods`
- Narration: Benchmark datasets play two roles: they let researchers compare methods, and they stand in as an imperfect model of the real world. The trouble is that a single static benchmark can never fully capture the dynamic, high-dimensional complexity of real tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_benchmark_datasets_play_two_roles" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords benchmark, datasets, play, two, roles, they in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_models_appear_match_beat_human_level`

- Preferred role: `method`
- Cue keywords: `models, appear, match, beat, human-level, accuracy, benchmark, routinely, err, out-of-distribution`
- Narration: So models that appear to match or beat human-level accuracy on a benchmark routinely err on out-of-distribution and adversarially perturbed production data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_models_appear_match_beat_human_level" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords models, appear, match, beat, human-level, accuracy in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_field_describes_gap_distribution_shi`

- Preferred role: `method`
- Cue keywords: `field, describes, gap, distribution, shift, subcategories, like, covariate, shift, prior`
- Narration: The field describes this gap as distribution shift, with subcategories like covariate shift, prior probability shift, and concept shift.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_field_describes_gap_distribution_shi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords field, describes, gap, distribution, shift, subcategories in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_but_these_definitions_over_specified`

- Preferred role: `content`
- Cue keywords: `but, these, definitions, over-specified, comparing, two, samples, under-specified, evaluating, data-generating`
- Narration: But these definitions are over-specified for comparing two data samples and under-specified for evaluating the data-generating process that actually drives the mismatch.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_but_these_definitions_over_specified" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, these, definitions, over-specified, comparing, two in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_prior_work_treats_robustness_differe`

- Preferred role: `method`
- Cue keywords: `prior, work, treats, robustness, difference, between, two, distributions, while, disregarding`
- Narration: Prior work treats robustness as a difference between two distributions while disregarding the reasons behind that difference.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_prior_work_treats_robustness_differe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, work, treats, robustness, difference, between in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_but_difference_merely_symptom_diseas`

- Preferred role: `content`
- Cue keywords: `but, difference, merely, symptom, disease, how, created, collected, curated`
- Narration: But the difference is merely a symptom; the disease is in how data are created, collected, and curated.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_but_difference_merely_symptom_diseas" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, difference, merely, symptom, disease, how in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_figure_1_shows_interest_distribution`

- Preferred role: `method`
- Cue keywords: `figure, 1, shows, interest, distribution, shift, terminology, grown, enormously, over`
- Narration: As Figure 1 shows, interest in distribution shift terminology has grown enormously over the last decade, with covariate shift papers alone climbing toward nine thousand per year by 2021.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_figure_1_shows_interest_distribution" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords figure, 1, shows, interest, distribution, shift in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_despite_volume_vocabulary_stays_tang`

- Preferred role: `method`
- Cue keywords: `despite, volume, vocabulary, stays, tangled, rarely, points, practitioners, toward, upstream`
- Narration: Despite this volume, the vocabulary stays tangled and rarely points practitioners toward the upstream, semantically meaningful factors they can actually intervene on.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_despite_volume_vocabulary_stays_tang" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords despite, volume, vocabulary, stays, tangled, rarely in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_perspective_reframes_robustness_prob`

- Preferred role: `content`
- Cue keywords: `perspective, reframes, robustness, problem`
- Narration: This is a perspective paper that reframes the robustness problem.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_perspective_reframes_robustness_prob" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords perspective, reframes, robustness, problem in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_its_central_contribution_concept_con`

- Preferred role: `method`
- Cue keywords: `its, central, contribution, concept, context, shift, which, describes, semantically, meaningful`
- Narration: Its central contribution is the concept of context shift, which describes the semantically meaningful upstream factors, sample selection bias, adversarial perturbation, and non-stationarity, that drive the distribution shifts we observe.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_its_central_contribution_concept_con" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, central, contribution, concept, context, shift in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_top_framing_groh_identifies_three`

- Preferred role: `method`
- Cue keywords: `top, framing, groh, identifies, three, practical, methods, closing, benchmark-to-production, gap`
- Narration: On top of that framing, Groh identifies three practical methods for closing the benchmark-to-production gap, and illustrates all of them through three recurring case-study domains: facial expression recognition, deepfake detection, and medical diagnosis.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_top_framing_groh_identifies_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords top, framing, groh, identifies, three, practical in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_context_refers_semantically_meaningf`

- Preferred role: `method`
- Cue keywords: `context, refers, semantically, meaningful, upstream, factors, drive, distribution, shift`
- Narration: Context refers to the semantically meaningful upstream factors that drive a distribution shift.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_context_refers_semantically_meaningf" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords context, refers, semantically, meaningful, upstream, factors in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_rather_fixating_difference_between_t`

- Preferred role: `method`
- Cue keywords: `rather, fixating, difference, between, two, distributions, groh, asks, researchers, reason`
- Narration: Rather than fixating on the difference between two distributions, Groh asks researchers to reason about the three processes that generate that difference: sample selection bias, for example a new dataset drawn from a demographic absent from the old one; adversarial perturbations, imperceptible noise injections that change model behavior; and non-stationarity, where the world itself moves on, like smartphones after 2018 versus flip phones before 2010.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_rather_fixating_difference_between_t" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rather, fixating, difference, between, two, distributions in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_three_methods_follow_first_human`

- Preferred role: `method`
- Cue keywords: `three, methods, follow, first, human, intuition, expert, knowledge, identify, semantically`
- Narration: Three methods follow. First, human intuition and expert knowledge can identify the semantically meaningful features on which models are likely to fail.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_three_methods_follow_first_human" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords three, methods, follow, first, human, intuition in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_second_dynamic_benchmarking_replaces`

- Preferred role: `method`
- Cue keywords: `second, dynamic, benchmarking, replaces, single, static, test, set, continual, evaluation`
- Narration: Second, dynamic benchmarking replaces a single static test set with continual evaluation against a well-specified, quality-controlled data-generation process, producing corroborated accuracy, the distribution of scores across many benchmarks. Third, authors should clarify a model's limitations, explicitly stating the contexts in which performance is known and unknown.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_second_dynamic_benchmarking_replaces" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, dynamic, benchmarking, replaces, single, static in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_rather_introducing_new_dataset_disse`

- Preferred role: `result`
- Cue keywords: `rather, introducing, new, dataset, dissects, existing, benchmarks, across, three, domains`
- Narration: Rather than introducing a new dataset, the paper dissects existing benchmarks across three domains. In facial expression recognition it examines seven benchmarks, from SFEW and MMI to CK+ and MultiPie.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_rather_introducing_new_dataset_disse" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rather, introducing, new, dataset, dissects, existing in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_deepfake_detection_centers_dfdc_data`

- Preferred role: `result`
- Cue keywords: `deepfake, detection, centers, dfdc, dataset, largest, date, over, one, hundred`
- Narration: In deepfake detection it centers on the DFDC dataset, the largest to date, with over one hundred twenty-eight thousand videos from nine hundred sixty consenting actors.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_deepfake_detection_centers_dfdc_data" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deepfake, detection, centers, dfdc, dataset, largest in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_medical_diagnosis_looks_store_and_fo`

- Preferred role: `content`
- Cue keywords: `medical, diagnosis, looks, store-and-forward, teledermatology, diverse, dermatology, images, dataset`
- Narration: In medical diagnosis it looks at store-and-forward teledermatology and the Diverse Dermatology Images dataset.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_medical_diagnosis_looks_store_and_fo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords medical, diagnosis, looks, store-and-forward, teledermatology, diverse in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_throughout_holds_context_aware_bench`

- Preferred role: `result`
- Cue keywords: `throughout, holds, context-aware, benchmarks, like, breeds, wilds, dynabench, models, capturing`
- Narration: Throughout, it holds up context-aware benchmarks like BREEDS, WILDS, and Dynabench as models for capturing the data-generation process instead of a single static snapshot.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_throughout_holds_context_aware_bench" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords throughout, holds, context-aware, benchmarks, like, breeds in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_evidence_how_wildly_perform`

- Preferred role: `result`
- Cue keywords: `headline, evidence, how, wildly, performance, swings, benchmark, one, facial, expression`
- Narration: The headline evidence is how wildly performance swings with the benchmark. One facial expression model, built on AlexNet, ranges from just 48.6 percent accuracy on SFEW to 94.8 percent on MultiPie, against a random baseline of 14.2 percent, so which benchmark you pick determines the story you tell.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_headline_evidence_how_wildly_perform" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, evidence, how, wildly, performance, swings in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_pattern_generalizes_when_researchers`

- Preferred role: `result`
- Cue keywords: `pattern, generalizes, when, researchers, faithfully, recreated, imagenet, cifar-10, test, sets`
- Narration: The pattern generalizes: when researchers faithfully recreated the ImageNet and CIFAR-10 test sets, state-of-the-art accuracy fell by three to fifteen percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_pattern_generalizes_when_researchers" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pattern, generalizes, when, researchers, faithfully, recreated in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_leading_dfdc_deepfake_detector_assig`

- Preferred role: `content`
- Cue keywords: `leading, dfdc, deepfake, detector, assigned, only, two, eight, percent, likelihood`
- Narration: And a leading DFDC deepfake detector assigned only two and eight percent likelihood to genuine deepfakes of Kim Jong-un and Vladimir Putin, precisely the high-context videos that matter in the real world.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_leading_dfdc_deepfake_detector_assig" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords leading, dfdc, deepfake, detector, assigned, only in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_dermatology_benchmarks_barely_includ`

- Preferred role: `result`
- Cue keywords: `dermatology, benchmarks, barely, include, dark, skin, let, systematic, errors, hide`
- Narration: In dermatology, benchmarks that barely include dark skin let systematic errors hide in plain sight.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c4_dermatology_benchmarks_barely_includ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dermatology, benchmarks, barely, include, dark, skin in title/desc so the matcher can verify semantic overlap.

## Slide 08: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s08_c1_few_numbers_anchor_argument_single`

- Preferred role: `result`
- Cue keywords: `few, numbers, anchor, argument, single, facial, expression, spans, 48.6, 94.8`
- Narration: A few numbers anchor the argument. A single facial expression model spans 48.6 to 94.8 percent accuracy across seven benchmarks, next to a 14.2 percent random baseline.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c1_few_numbers_anchor_argument_single" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, anchor, argument, single, facial in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_faithfully_recreated_imagenet_cifar`

- Preferred role: `result`
- Cue keywords: `faithfully, recreated, imagenet, cifar-10, test, sets, cut, state-of-the-art, accuracy, three`
- Narration: Faithfully recreated ImageNet and CIFAR-10 test sets cut state-of-the-art accuracy by three to fifteen percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_faithfully_recreated_imagenet_cifar" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords faithfully, recreated, imagenet, cifar-10, test, sets in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_leading_deepfake_detector_gave_only`

- Preferred role: `result`
- Cue keywords: `leading, deepfake, detector, gave, only, two, eight, percent, likelihood, real`
- Narration: A leading deepfake detector gave only two and eight percent likelihood to real deepfakes of world leaders. The DFDC benchmark holds 128,154 videos from 960 actors.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c3_leading_deepfake_detector_gave_only" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords leading, deepfake, detector, gave, only, two in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_one_dermatology_benchmark_included_j`

- Preferred role: `result`
- Cue keywords: `one, dermatology, benchmark, included, just, 2.7, percent, second-darkest, skin, type`
- Narration: And one dermatology benchmark included just 2.7 percent of the second-darkest skin type, and a single person of the darkest.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_one_dermatology_benchmark_included_j" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one, dermatology, benchmark, included, just, 2.7 in title/desc so the matcher can verify semantic overlap.

## Slide 09: takeaway

Heading: Takeaway

### Cue 1: `cue_s09_c1_lasting_message_shift_perspective_st`

- Preferred role: `result`
- Cue keywords: `lasting, message, shift, perspective, stop, treating, benchmark-to-production, gap, mere, statistical`
- Narration: The lasting message is a shift in perspective: stop treating the benchmark-to-production gap as a mere statistical distance between two datasets and start treating it as context shift, the semantically meaningful changes in how data are generated.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_lasting_message_shift_perspective_st" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, shift, perspective, stop, treating in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_address_pairing_machine_learning_hum`

- Preferred role: `result`
- Cue keywords: `address, pairing, machine, learning, human, intuition, expertise, moving, static, dynamic`
- Narration: Address it by pairing machine learning with human intuition and expertise, by moving from static to dynamic benchmarks that evaluate the data-generation process, and by clearly clarifying each model's limitations.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_address_pairing_machine_learning_hum" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords address, pairing, machine, learning, human, intuition in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_simplest_most_immediately_effective`

- Preferred role: `content`
- Cue keywords: `simplest, most, immediately, effective, step, honesty, state, plainly, contexts, which`
- Narration: The simplest and most immediately effective step is honesty: state plainly the contexts in which a model has been evaluated and the contexts in which its behavior remains unknown.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_simplest_most_immediately_effective" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords simplest, most, immediately, effective, step, honesty in title/desc so the matcher can verify semantic overlap.
