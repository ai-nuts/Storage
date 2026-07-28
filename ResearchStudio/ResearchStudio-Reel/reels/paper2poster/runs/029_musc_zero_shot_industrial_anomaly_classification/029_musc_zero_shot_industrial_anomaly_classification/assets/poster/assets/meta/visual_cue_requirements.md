# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_musc_zero_shot_method_industrial_ano`

- Preferred role: `method`
- Cue keywords: `musc, zero-shot, method, industrial, anomaly, detection, segmentation, prompts, normal, reference`
- Narration: MuSc is a zero-shot method for industrial anomaly detection and segmentation, with no training, no prompts, and no normal reference images.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_musc_zero_shot_method_industrial_ano" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords musc, zero-shot, method, industrial, anomaly, detection in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_its_insight_unlabeled_test_images`

- Preferred role: `method`
- Cue keywords: `its, insight, unlabeled, test, images, hold, enough, cues, score, one`
- Narration: Its insight: unlabeled test images hold enough cues to score one another.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_its_insight_unlabeled_test_images" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, insight, unlabeled, test, images, hold in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_published_iclr_2024_tops_mvtec`

- Preferred role: `content`
- Cue keywords: `published, iclr, 2024, tops, mvtec, visa`
- Narration: Published at ICLR 2024, it tops MVTec AD and VisA.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_published_iclr_2024_tops_mvtec" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords published, iclr, 2024, tops, mvtec, visa in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_detecting_defects_core_vision_task`

- Preferred role: `method`
- Cue keywords: `detecting, defects, core, vision, task, but, existing, methods, demanding`
- Narration: Detecting defects is a core vision task, but existing methods are demanding.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_detecting_defects_core_vision_task" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords detecting, defects, core, vision, task, but in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_one_class_approaches_need_bank_norma`

- Preferred role: `method`
- Cue keywords: `one-class, approaches, need, bank, normal, images, per, product, clip-based, zero-shot`
- Narration: One-class approaches need a bank of normal images per product; CLIP-based zero-shot methods rely on hand-written prompts.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_one_class_approaches_need_bank_norma" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one-class, approaches, need, bank, normal, images in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_many_factories_neither`

- Preferred role: `content`
- Cue keywords: `many, factories, neither`
- Narration: Many factories have neither.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_many_factories_neither" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords many, factories, neither in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_goal_segment_anomalies_prompts_refer`

- Preferred role: `method`
- Cue keywords: `goal, segment, anomalies, prompts, references`
- Narration: The goal: segment anomalies with no training, prompts, or references.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_goal_segment_anomalies_prompts_refer" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords goal, segment, anomalies, prompts, references in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_authors_make_simple_observation`

- Preferred role: `content`
- Cue keywords: `authors, make, simple, observation`
- Narration: The authors make a simple observation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_authors_make_simple_observation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, make, simple, observation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_batch_unlabeled_test_images_one`

- Preferred role: `content`
- Cue keywords: `batch, unlabeled, test, images, one, product, normal, patch, finds, many`
- Narration: In a batch of unlabeled test images of one product, a normal patch finds many similar patches across the others, because normal appearance repeats.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_batch_unlabeled_test_images_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords batch, unlabeled, test, images, one, product in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_abnormal_patch_finds_only_few`

- Preferred role: `content`
- Cue keywords: `abnormal, patch, finds, only, few, since, defects, rare`
- Narration: An abnormal patch finds only a few, since defects are rare.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_abnormal_patch_finds_only_few" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords abnormal, patch, finds, only, few, since in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_asymmetry_signal_already_inside_test`

- Preferred role: `content`
- Cue keywords: `asymmetry, signal, already, inside, test, set`
- Narration: That asymmetry is a signal already inside the test set.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_asymmetry_signal_already_inside_test" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords asymmetry, signal, already, inside, test, set in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_musc_training_free_prompt_free_pipel`

- Preferred role: `method`
- Cue keywords: `musc, training-free, prompt-free, pipeline, three, pieces`
- Narration: MuSc is a training-free, prompt-free pipeline with three pieces.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_musc_training_free_prompt_free_pipel" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords musc, training-free, prompt-free, pipeline, three, pieces in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_local_neighborhood_aggregation`

- Preferred role: `content`
- Cue keywords: `first, local, neighborhood, aggregation, multiple, degrees, representing, patch, several, scales`
- Narration: First, local neighborhood aggregation at multiple degrees, representing each patch at several scales to capture tiny and large defects.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_first_local_neighborhood_aggregation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, local, neighborhood, aggregation, multiple, degrees in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_mutual_scoring_where_every`

- Preferred role: `method`
- Cue keywords: `second, mutual, scoring, where, every, test, image, scores, every, other`
- Narration: Second, mutual scoring, where every test image scores every other.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_mutual_scoring_where_every" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, mutual, scoring, where, every, test in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_re_scoring_constrained_image_l`

- Preferred role: `method`
- Cue keywords: `third, re-scoring, constrained, image-level, neighborhood, cleans, final, decision`
- Narration: Third, re-scoring with a constrained image-level neighborhood that cleans the final decision.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_third_re_scoring_constrained_image_l" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, re-scoring, constrained, image-level, neighborhood, cleans in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_backbone_frozen_vision_transformer`

- Preferred role: `method`
- Cue keywords: `backbone, frozen, vision, transformer`
- Narration: The backbone is a frozen vision transformer.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_backbone_frozen_vision_transformer" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords backbone, frozen, vision, transformer in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_patch_tokens_several_stages_aggregat`

- Preferred role: `content`
- Cue keywords: `patch, tokens, several, stages, aggregated, multiple, neighborhood, degrees, represent, defect`
- Narration: Patch tokens from several stages are aggregated at multiple neighborhood degrees to represent defect sizes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_patch_tokens_several_stages_aggregat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords patch, tokens, several, stages, aggregated, multiple in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_mutual_scoring_patch_scored_its`

- Preferred role: `method`
- Cue keywords: `mutual, scoring, patch, scored, its, nearest, match, every, other, image`
- Narration: In mutual scoring, each patch is scored by its nearest match in every other image, and only the smallest score interval is averaged, sharpening the gap.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_mutual_scoring_patch_scored_its" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mutual, scoring, patch, scored, its, nearest in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_image_score_refined_constrained_neig`

- Preferred role: `method`
- Cue keywords: `image, score, refined, constrained, neighborhood, graph, class, tokens`
- Narration: The image score is refined with a constrained neighborhood graph on class tokens.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_image_score_refined_constrained_neig" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords image, score, refined, constrained, neighborhood, graph in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_musc_evaluated_two_most_used_industr`

- Preferred role: `method`
- Cue keywords: `musc, evaluated, two, most-used, industrial, benchmarks`
- Narration: MuSc is evaluated on the two most-used industrial benchmarks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_musc_evaluated_two_most_used_industr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords musc, evaluated, two, most-used, industrial, benchmarks in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_mvtec_spans_fifteen_categories_ten`

- Preferred role: `content`
- Cue keywords: `mvtec, spans, fifteen, categories, ten, objects, five, textures`
- Narration: MVTec AD spans fifteen categories, ten objects and five textures.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_mvtec_spans_fifteen_categories_ten" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mvtec, spans, fifteen, categories, ten, objects in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_visa_covers_twelve_object_categories`

- Preferred role: `content`
- Cue keywords: `visa, covers, twelve, object, categories, across, three, domains, both, mix`
- Narration: VisA covers twelve object categories across three domains. Both mix normal and defective images.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_visa_covers_twelve_object_categories" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords visa, covers, twelve, object, categories, across in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_classification_auroc_f1_max_segmenta`

- Preferred role: `result`
- Cue keywords: `classification, auroc, f1-max, segmentation, adds, pixel-level, metrics, per-region, overlap`
- Narration: Classification uses AUROC and F1-max; segmentation adds pixel-level metrics and per-region overlap.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_classification_auroc_f1_max_segmenta" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords classification, auroc, f1-max, segmentation, adds, pixel-level in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_results_striking_label_free_method`

- Preferred role: `method`
- Cue keywords: `results, striking, label-free, method`
- Narration: Results are striking for a label-free method.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_results_striking_label_free_method" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, striking, label-free, method in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_mvtec_musc_reaches_ninety_seven_poin`

- Preferred role: `method`
- Cue keywords: `mvtec, musc, reaches, ninety-seven, point, eight, percent, image, auroc, lifts`
- Narration: On MVTec AD, MuSc reaches ninety-seven point eight percent image AUROC and lifts per-region overlap segmentation by over twenty-one points versus the best prior zero-shot method.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_mvtec_musc_reaches_ninety_seven_poin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mvtec, musc, reaches, ninety-seven, point, eight in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_visa_gains_over_ten_points`

- Preferred role: `result`
- Cue keywords: `visa, gains, over, ten, points`
- Narration: On VisA it gains over ten points.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_visa_gains_over_ten_points" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords visa, gains, over, ten, points in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_even_beats_most_four_shot_methods`

- Preferred role: `method`
- Cue keywords: `even, beats, most, four-shot, methods, rivals, full-shot, approaches`
- Narration: It even beats most four-shot methods and rivals full-shot approaches.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_even_beats_most_four_shot_methods" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords even, beats, most, four-shot, methods, rivals in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablations_confirm_choice`

- Preferred role: `content`
- Cue keywords: `ablations, confirm, choice`
- Narration: Ablations confirm each choice.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_ablations_confirm_choice" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, confirm, choice in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_combining_three_aggregation_degrees`

- Preferred role: `content`
- Cue keywords: `combining, three, aggregation, degrees, works, best, small, neighborhoods, catch, tiny`
- Narration: Combining three aggregation degrees works best: small neighborhoods catch tiny VisA defects, large ones catch big MVTec defects.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_combining_three_aggregation_degrees" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords combining, three, aggregation, degrees, works, best in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_averaging_smallest_thirty_percent_in`

- Preferred role: `content`
- Cue keywords: `averaging, smallest, thirty, percent, interval, beats, max, range, lifting, auroc`
- Narration: Averaging the smallest thirty percent interval beats the max or range, lifting AUROC to ninety-seven point eight percent.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_averaging_smallest_thirty_percent_in" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords averaging, smallest, thirty, percent, interval, beats in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_re_scoring_raises_visa_image_auroc`

- Preferred role: `content`
- Cue keywords: `re-scoring, raises, visa, image, auroc, ninety, ninety-two, point, eight`
- Narration: Re-scoring raises VisA image AUROC from ninety to ninety-two point eight.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_re_scoring_raises_visa_image_auroc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords re-scoring, raises, visa, image, auroc, ninety in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_headline_terms_musc_reaches_ninety_s`

- Preferred role: `result`
- Cue keywords: `headline, terms, musc, reaches, ninety-seven, point, eight, percent, image, auroc`
- Narration: In headline terms, MuSc reaches ninety-seven point eight percent image AUROC on MVTec AD and ninety-two point eight on VisA, with pixel AUROC of ninety-seven point three and ninety-eight point eight.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_headline_terms_musc_reaches_ninety_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, terms, musc, reaches, ninety-seven, point in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_adds_over_twenty_one_points_mvtec`

- Preferred role: `method`
- Cue keywords: `adds, over, twenty-one, points, mvtec, segmentation, all, prompts, references`
- Narration: It adds over twenty-one points on MVTec segmentation, all with no training, prompts, or references.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_adds_over_twenty_one_points_mvtec" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords adds, over, twenty-one, points, mvtec, segmentation in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_idea_set_unlabeled_test`

- Preferred role: `content`
- Cue keywords: `lasting, idea, set, unlabeled, test, images, supervise, itself`
- Narration: The lasting idea: a set of unlabeled test images can supervise itself.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c1_lasting_idea_set_unlabeled_test" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, idea, set, unlabeled, test, images in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_letting_images_score_one_another`

- Preferred role: `method`
- Cue keywords: `letting, images, score, one, another, repeating, normal, structure, separated, rare`
- Narration: By letting images score one another, repeating normal structure is separated from rare defects, with no training or prompts, giving state-of-the-art zero-shot detection that rivals full-shot methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_letting_images_score_one_another" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords letting, images, score, one, another, repeating in title/desc so the matcher can verify semantic overlap.
