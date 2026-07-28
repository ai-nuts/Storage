# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_given_two_partially_overlapping_imag`

- Preferred role: `content`
- Cue keywords: `given, two, partially, overlapping, images, keypoint, first, where, does, its`
- Narration: Given two partially overlapping images and a keypoint in the first, where does its match land in the second?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_given_two_partially_overlapping_imag" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords given, two, partially, overlapping, images, keypoint in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_local_feature_matching_only_answers`

- Preferred role: `title`
- Cue keywords: `local, feature, matching, only, answers, when, point, visible`
- Narration: Local feature matching only answers when the point is visible.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s01_c2_local_feature_matching_only_answers" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords local, feature, matching, only, answers, when in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_but_humans_also_guess_hallucinate`

- Preferred role: `content`
- Cue keywords: `but, humans, also, guess, hallucinate, where, occluded, out, frame, point`
- Narration: But humans can also guess, or hallucinate, where an occluded or out of frame point should be, using geometric reasoning.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_but_humans_also_guess_hallucinate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, humans, also, guess, hallucinate, where in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_visual_correspondence_hallucination`

- Preferred role: `method`
- Cue keywords: `visual, correspondence, hallucination, iclr, 2022, trains, single, network, called, neurhal`
- Narration: This paper, Visual Correspondence Hallucination from ICLR 2022, trains a single network called NeurHal to output a peaked probability distribution over the correspondent's location whether it is visible, occluded, or outside the field of view, and shows this makes absolute camera pose estimation far more robust.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_visual_correspondence_hallucination" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords visual, correspondence, hallucination, iclr, 2022, trains in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_establishing_correspondences_between`

- Preferred role: `method`
- Cue keywords: `establishing, correspondences, between, two, overlapping, images, underlies, much, computer, vision`
- Narration: Establishing correspondences between two overlapping images underlies much of computer vision, from localization to reconstruction.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_establishing_correspondences_between" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords establishing, correspondences, between, two, overlapping, images in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_local_feature_matching_only`

- Preferred role: `content`
- Cue keywords: `but, local, feature, matching, only, works, when, keypoint, actually, visible`
- Narration: But local feature matching only works when a keypoint is actually visible in both images.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_but_local_feature_matching_only" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, local, feature, matching, only, works in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_when_correspondent_occluded_when_fal`

- Preferred role: `method`
- Cue keywords: `when, correspondent, occluded, when, falls, outside, field, view, second, image`
- Narration: When the correspondent is occluded, or when it falls outside the field of view of the second image, these methods have nothing to say, and they simply treat those regions as noise.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_when_correspondent_occluded_when_fal" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, correspondent, occluded, when, falls, outside in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_whenever_two_images_share_little`

- Preferred role: `content`
- Cue keywords: `whenever, two, images, share, little, overlap, matching, breaks, down`
- Narration: So whenever two images share little overlap, matching breaks down.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_whenever_two_images_share_little" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords whenever, two, images, share, little, overlap in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_humans_not_give_these_situations`

- Preferred role: `content`
- Cue keywords: `humans, not, give, these, situations`
- Narration: Humans do not give up in these situations.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_humans_not_give_these_situations" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords humans, not, give, these, situations in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_faced_occluded_out_frame_point`

- Preferred role: `content`
- Cue keywords: `faced, occluded, out, frame, point, person, reasons, about, geometry, scene`
- Narration: Faced with an occluded or out of frame point, a person reasons about the geometry of the scene and predicts, or hallucinates, where the match should be.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_faced_occluded_out_frame_point" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords faced, occluded, out, frame, point, person in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_classical_vision_does_geometric_reas`

- Preferred role: `content`
- Cue keywords: `classical, vision, does, geometric, reasoning, but, only, after, fact, filter`
- Narration: Classical vision does use geometric reasoning, but only after the fact, to filter out bad matches with models like epipolar geometry.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_classical_vision_does_geometric_reas" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords classical, vision, does, geometric, reasoning, but in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_prior_method_actually_predicts_corre`

- Preferred role: `method`
- Cue keywords: `prior, method, actually, predicts, correspondences, locations, not, covisible, gap, exactly`
- Narration: No prior method actually predicts correspondences at locations that are not covisible. That gap is exactly what this work targets.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_prior_method_actually_predicts_corre" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, method, actually, predicts, correspondences, locations in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_introduces_task_visual_correspondenc`

- Preferred role: `content`
- Cue keywords: `introduces, task, visual, correspondence, hallucination, network, solve, called, neurhal, neural`
- Narration: The paper introduces the task of visual correspondence hallucination and a network to solve it, called NeurHal, for Neural Hallucinations.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_introduces_task_visual_correspondenc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, task, visual, correspondence, hallucination, network in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_given_pair_overlapping_images_keypoi`

- Preferred role: `method`
- Cue keywords: `given, pair, overlapping, images, keypoints, source, image, neurhal, outputs, keypoint`
- Narration: Given a pair of overlapping images and keypoints in the source image, NeurHal outputs, for each keypoint, a probability distribution over its correspondent's location in the target image, whether that location is visible, occluded, or outside the field of view.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_given_pair_overlapping_images_keypoi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords given, pair, overlapping, images, keypoints, source in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_unifies_three_tasks_authors_name`

- Preferred role: `title`
- Cue keywords: `unifies, three, tasks, authors, name, identifying, inpainting, outpainting`
- Narration: This unifies three tasks the authors name identifying, inpainting, and outpainting.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s04_c3_unifies_three_tasks_authors_name" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unifies, three, tasks, authors, name, identifying in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_because_learning_hallucinate_unexplo`

- Preferred role: `figure`
- Cue keywords: `because, learning, hallucinate, unexplored, territory, they, first, analyze, what, makes`
- Narration: Because learning to hallucinate is unexplored territory, they first analyze what makes the task distinctive, and let that analysis drive the choice of loss and architecture.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c4_because_learning_hallucinate_unexplo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, learning, hallucinate, unexplored, territory, they in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_how_neurhal_works_siamese_convolutio`

- Preferred role: `content`
- Cue keywords: `how, neurhal, works, siamese, convolutional, backbone, turns, both, images, dense`
- Narration: Here is how NeurHal works. A siamese convolutional backbone turns both images into dense descriptor maps. To allow correspondents outside the target's field of view, the target map is padded with a learnable vector, initializing descriptors beyond the image borders.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_how_neurhal_works_siamese_convolutio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, neurhal, works, siamese, convolutional, backbone in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_cross_attention_backbone_positional`

- Preferred role: `method`
- Cue keywords: `cross, attention, backbone, positional, encoding, lets, source, target, descriptors, exchange`
- Narration: A cross attention backbone with positional encoding then lets source and target descriptors exchange information, which is what enables the network to hallucinate peaked distributions for occluded and out of frame points.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_cross_attention_backbone_positional" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cross, attention, backbone, positional, encoding, lets in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_keypoint_feature_convolved_over_targ`

- Preferred role: `content`
- Cue keywords: `keypoint, feature, convolved, over, target, features, passed, through, two, softmax`
- Narration: Each keypoint's feature is convolved over the target features and passed through a two D softmax to produce a correspondence map.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_keypoint_feature_convolved_over_targ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords keypoint, feature, convolved, over, target, features in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_minimizes_sum_neural_reprojection_er`

- Preferred role: `method`
- Cue keywords: `minimizes, sum, neural, reprojection, error, terms, negative, log, likelihood, true`
- Narration: Training minimizes a sum of Neural Reprojection Error terms, the negative log likelihood of the true reprojected location, with no covisibility assumption and no need to label points as visible or hidden.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_minimizes_sum_neural_reprojection_er" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords minimizes, sum, neural, reprojection, error, terms in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_method_evaluated_across_both_indoor`

- Preferred role: `method`
- Cue keywords: `method, evaluated, across, both, indoor, outdoor, domains`
- Narration: The method is evaluated across both indoor and outdoor domains.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_method_evaluated_across_both_indoor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, evaluated, across, both, indoor, outdoor in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_indoors_neurhal_trained_scannet_also`

- Preferred role: `method`
- Cue keywords: `indoors, neurhal, trained, scannet, also, tested, nyu, depth, dataset, outdoors`
- Narration: Indoors, NeurHal is trained on ScanNet and also tested on the NYU Depth dataset; outdoors, it is trained on MegaDepth and tested on ETH three D.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_indoors_neurhal_trained_scannet_also" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords indoors, neurhal, trained, scannet, also, tested in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_crucially_every_evaluation_scenes_ne`

- Preferred role: `method`
- Cue keywords: `crucially, every, evaluation, scenes, never, seen, during, results, measure, genuine`
- Narration: Crucially, every evaluation uses scenes that were never seen during training, so the results measure genuine generalization.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_crucially_every_evaluation_scenes_ne" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, every, evaluation, scenes, never, seen in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_downstream_application_absolute_came`

- Preferred role: `method`
- Cue keywords: `downstream, application, absolute, camera, pose, estimation, measured, twenty, five, hundred`
- Narration: For the downstream application, absolute camera pose estimation is measured on twenty five hundred source and target image pairs from held out ScanNet scenes.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_downstream_application_absolute_came" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords downstream, application, absolute, camera, pose, estimation in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_experiments_confirm_both_research_qu`

- Preferred role: `title`
- Cue keywords: `experiments, confirm, both, research, questions`
- Narration: The experiments confirm both research questions.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s07_c1_experiments_confirm_both_research_qu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, confirm, both, research, questions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_neurhal_successfully_hallucinates_co`

- Preferred role: `method`
- Cue keywords: `neurhal, successfully, hallucinates, correspondences, scenes, never, saw, during, occluded, points`
- Narration: NeurHal successfully hallucinates correspondences on scenes it never saw during training, for occluded points that must be inpainted and for out of frame points that must be outpainted, with prediction errors concentrated well below what random guessing would give.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_neurhal_successfully_hallucinates_co" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords neurhal, successfully, hallucinates, correspondences, scenes, never in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_state_art_matching_methods_like`

- Preferred role: `method`
- Cue keywords: `state, art, matching, methods, like, loftr, drc, net, two, net`
- Narration: State of the art matching methods like LoFTR, DRC Net, and S two D Net do poorly on inpainting and essentially cannot outpaint at all, since they only ever search inside the image boundaries.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_state_art_matching_methods_like" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords state, art, matching, methods, like, loftr in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_absolute_camera_pose_estimation_neur`

- Preferred role: `method`
- Cue keywords: `absolute, camera, pose, estimation, neurhal, correct, far, more, often, any`
- Narration: And on absolute camera pose estimation, NeurHal is correct far more often than any competitor on low overlap pairs, precisely because it is the only method that can outpaint.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_absolute_camera_pose_estimation_neur" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords absolute, camera, pose, estimation, neurhal, correct in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablation_scannet_isolates_what_task`

- Preferred role: `method`
- Cue keywords: `ablation, scannet, isolates, what, task, contributes, pose, robustness, neurhal, all`
- Narration: An ablation on ScanNet isolates what each task contributes to pose robustness. Training NeurHal on all three tasks together, identification, inpainting, and outpainting, gives the best results.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_ablation_scannet_isolates_what_task" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablation, scannet, isolates, what, task, contributes in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_key_finding_adding_outpainting_task`

- Preferred role: `result`
- Cue keywords: `key, finding, adding, outpainting, task, what, drives, improvement, low, overlap`
- Narration: The key finding is that adding the outpainting task is what drives the improvement on low overlap pairs, where most correspondents fall outside the target's field of view.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_key_finding_adding_outpainting_task" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, finding, adding, outpainting, task, what in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_adding_inpainting_contrast_brings_li`

- Preferred role: `content`
- Cue keywords: `adding, inpainting, contrast, brings, little, additional, benefit, camera, pose, estimation`
- Narration: Adding inpainting, by contrast, brings little additional benefit to camera pose estimation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_adding_inpainting_contrast_brings_li" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords adding, inpainting, contrast, brings, little, additional in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_pose_counts_correct_when_rotation`

- Preferred role: `result`
- Cue keywords: `pose, counts, correct, when, rotation, error, under, twenty, degrees, translation`
- Narration: Here a pose counts as correct when rotation error is under twenty degrees and translation error under one point five meters.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_pose_counts_correct_when_rotation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pose, counts, correct, when, rotation, error in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_anchor_setup`

- Preferred role: `content`
- Cue keywords: `few, numbers, anchor, setup`
- Narration: A few numbers anchor the setup.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_anchor_setup" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, anchor, setup in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_pose_estimates_judged_correct_under`

- Preferred role: `content`
- Cue keywords: `pose, estimates, judged, correct, under, rotation, threshold, twenty, degrees, translation`
- Narration: Pose estimates are judged correct under a rotation threshold of twenty degrees and a translation threshold of one point five meters, measured over twenty five hundred held out ScanNet image pairs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_pose_estimates_judged_correct_under" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pose, estimates, judged, correct, under, rotation in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_neurhal_produces_deliberately_low_re`

- Preferred role: `method`
- Cue keywords: `neurhal, produces, deliberately, low, resolution, correspondence, maps, effective, stride, eight`
- Narration: NeurHal produces deliberately low resolution correspondence maps, using an effective stride of eight and an output ratio of fifty percent, so a six hundred forty by four hundred eighty target yields a one hundred sixty by one hundred twenty map.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_neurhal_produces_deliberately_low_re" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords neurhal, produces, deliberately, low, resolution, correspondence in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_across_all_methods_tested_neurhal`

- Preferred role: `method`
- Cue keywords: `across, all, methods, tested, neurhal, only, one, able, outpaint, place`
- Narration: And across all the methods tested, NeurHal is the only one able to outpaint, to place correspondents beyond the target image's borders.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_across_all_methods_tested_neurhal" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, all, methods, tested, neurhal, only in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple_but_powerful`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple, but, powerful`
- Narration: The takeaway is simple but powerful.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple_but_powerful" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple, but, powerful in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_single_network_learn_hallucinate_key`

- Preferred role: `content`
- Cue keywords: `single, network, learn, hallucinate, keypoint, correspondences, whether, match, visible, occluded`
- Narration: A single network can learn to hallucinate keypoint correspondences whether the match is visible, occluded, or entirely outside the field of view, and this ability makes absolute camera pose estimation much more robust when images barely overlap.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_single_network_learn_hallucinate_key" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords single, network, learn, hallucinate, keypoint, correspondences in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_effect_neurhal_reframes_non_covisibl`

- Preferred role: `content`
- Cue keywords: `effect, neurhal, reframes, non, covisible, regions, not, noise, thrown, away`
- Narration: In effect, NeurHal reframes non covisible regions not as noise to be thrown away, but as signal to be predicted through learned geometric reasoning.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_effect_neurhal_reframes_non_covisibl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords effect, neurhal, reframes, non, covisible, regions in title/desc so the matcher can verify semantic overlap.
