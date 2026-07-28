# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_vectormapnet_first_end_to_end_pipeli`

- Preferred role: `method`
- Cue keywords: `vectormapnet, first, end-to-end, pipeline, reads, onboard, camera, lidar, directly, predicts`
- Narration: VectorMapNet is the first end-to-end pipeline that reads onboard camera and LiDAR data and directly predicts a sparse set of polylines, the vectorized map primitive planners actually use.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_vectormapnet_first_end_to_end_pipeli" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords vectormapnet, first, end-to-end, pipeline, reads, onboard in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_skips_rasterization_entirely_sets_ne`

- Preferred role: `content`
- Cue keywords: `skips, rasterization, entirely, sets, new, state, art`
- Narration: It skips rasterization entirely and sets a new state of the art.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_skips_rasterization_entirely_sets_ne" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords skips, rasterization, entirely, sets, new, state in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_self_driving_cars_need_maps_marking`

- Preferred role: `content`
- Cue keywords: `self-driving, cars, need, maps, marking, lanes, boundaries, crosswalks`
- Narration: Self-driving cars need HD maps marking lanes, boundaries, and crosswalks.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_self_driving_cars_need_maps_marking" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords self-driving, cars, need, maps, marking, lanes in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_today_these_annotated_hand_which`

- Preferred role: `content`
- Cue keywords: `today, these, annotated, hand, which, costly, does, not, scale`
- Narration: Today these are annotated by hand, which is costly and does not scale.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_today_these_annotated_hand_which" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords today, these, annotated, hand, which, costly in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_learning_methods_instead_predict_den`

- Preferred role: `method`
- Cue keywords: `learning, methods, instead, predict, dense, pixel, grid, but, grid, carries`
- Narration: Learning methods instead predict a dense pixel grid, but a grid carries no individual elements and needs brittle post-processing before a planner can use it.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_learning_methods_instead_predict_den" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords learning, methods, instead, predict, dense, pixel in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_authors_argue_mapping_should_happen`

- Preferred role: `result`
- Cue keywords: `authors, argue, mapping, should, happen, online, car, own, sensors, avoiding`
- Narration: The authors argue mapping should happen online, from the car's own sensors, avoiding the annotation burden and localization errors, and the model should output the final representation directly.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c1_authors_argue_mapping_should_happen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, argue, mapping, should, happen, online in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_prior_methods_rasterize_vectorize_ha`

- Preferred role: `method`
- Cue keywords: `prior, methods, rasterize, vectorize, hand-designed, step, vectormapnet, removes, detour, predicts`
- Narration: Prior methods rasterize then vectorize with a hand-designed step; VectorMapNet removes that detour and predicts geometry end to end.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_prior_methods_rasterize_vectorize_ha" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, methods, rasterize, vectorize, hand-designed, step in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_vectormapnet_makes_three_contributio`

- Preferred role: `content`
- Cue keywords: `vectormapnet, makes, three, contributions`
- Narration: VectorMapNet makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_vectormapnet_makes_three_contributio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords vectormapnet, makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_predicts_vectorized_outputs_directly`

- Preferred role: `content`
- Cue keywords: `predicts, vectorized, outputs, directly, sensors, rasterization, post-processing`
- Narration: It predicts vectorized outputs directly from sensors, with no rasterization or post-processing.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_predicts_vectorized_outputs_directly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords predicts, vectorized, outputs, directly, sensors, rasterization in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_polyline_one_flexible_primitive_poin`

- Preferred role: `figure`
- Cue keywords: `polyline, one, flexible, primitive, points, lines, curves, polygons, whose, vertex`
- Narration: It uses the polyline as one flexible primitive for points, lines, curves, and polygons, whose vertex order encodes direction.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c3_polyline_one_flexible_primitive_poin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords polyline, one, flexible, primitive, points, lines in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_adapts_detection_transformers_locate`

- Preferred role: `method`
- Cue keywords: `adapts, detection, transformers, locate, elements, bird, s-eye, view`
- Narration: And it adapts detection transformers to locate elements in bird's-eye view.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_adapts_detection_transformers_locate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords adapts, detection, transformers, locate, elements, bird in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_vectormapnet_three_stages`

- Preferred role: `content`
- Cue keywords: `vectormapnet, three, stages`
- Narration: VectorMapNet has three stages.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_vectormapnet_three_stages" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords vectormapnet, three, stages in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_bird_s_eye_view_extractor_maps_modal`

- Preferred role: `content`
- Cue keywords: `bird, s-eye-view, extractor, maps, modality, shared, top-down, space, cameras, through`
- Narration: A bird's-eye-view extractor maps each modality into a shared top-down space: cameras through a ResNet and inverse perspective mapping, LiDAR through PointPillars, fused by concatenation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_bird_s_eye_view_extractor_maps_modal" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords bird, s-eye-view, extractor, maps, modality, shared in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_detection_transformer_element_querie`

- Preferred role: `method`
- Cue keywords: `detection, transformer, element, queries, locates, element, keypoints`
- Narration: A detection transformer with element queries locates each element as keypoints.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_detection_transformer_element_querie" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords detection, transformer, element, queries, locates, element in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_autoregressive_polyline_generator_em`

- Preferred role: `method`
- Cue keywords: `autoregressive, polyline, generator, emits, ordered, vertices, trained, matching, detection, loss`
- Narration: An autoregressive polyline generator then emits ordered vertices, trained with a matching detection loss and a generation loss.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_autoregressive_polyline_generator_em" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords autoregressive, polyline, generator, emits, ordered, vertices in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_vectormapnet_evaluated_nuscenes_argo`

- Preferred role: `content`
- Cue keywords: `vectormapnet, evaluated, nuscenes, argoverse2`
- Narration: VectorMapNet is evaluated on nuScenes and Argoverse2.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_vectormapnet_evaluated_nuscenes_argo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords vectormapnet, evaluated, nuscenes, argoverse2 in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_following_hdmapnet_predicted_polylin`

- Preferred role: `content`
- Cue keywords: `following, hdmapnet, predicted, polylines, compared, ground, truth, crosswalks, lane, dividers`
- Narration: Following HDMapNet, predicted polylines are compared to ground truth for crosswalks, lane dividers, and road boundaries.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_following_hdmapnet_predicted_polylin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords following, hdmapnet, predicted, polylines, compared, ground in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_reports_chamfer_distance_average_pre`

- Preferred role: `result`
- Cue keywords: `reports, chamfer-distance, average, precision, new, chet-distance, respects, vertex, order, plus`
- Narration: It reports Chamfer-distance average precision and a new Fréchet-distance AP that respects vertex order, plus 3D evaluation on Argoverse2.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c3_reports_chamfer_distance_average_pre" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reports, chamfer-distance, average, precision, new, chet-distance in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_vectormapnet_sets_new_state_art`

- Preferred role: `content`
- Cue keywords: `vectormapnet, sets, new, state, art`
- Narration: VectorMapNet sets a new state of the art.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_vectormapnet_sets_new_state_art" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords vectormapnet, sets, new, state, art in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_beats_hdmapnet_14_2_map_nuscenes`

- Preferred role: `content`
- Cue keywords: `beats, hdmapnet, 14.2, map, nuscenes, 14.6, argoverse2`
- Narration: It beats HDMapNet by 14.2 mAP on nuScenes and 14.6 on Argoverse2.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_beats_hdmapnet_14_2_map_nuscenes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords beats, hdmapnet, 14.2, map, nuscenes, 14.6 in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_gains_hold_across_sensors_nearly`

- Preferred role: `result`
- Cue keywords: `gains, hold, across, sensors, nearly, eighteen, points, camera-only, about, ten`
- Narration: Gains hold across sensors: nearly eighteen points camera-only, about ten LiDAR-only, over fourteen with fusion.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_gains_hold_across_sensors_nearly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gains, hold, across, sensors, nearly, eighteen in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_two_stage_fine_tuning_pushes_fusion`

- Preferred role: `content`
- Cue keywords: `two-stage, fine-tuning, pushes, fusion, 53.7, map, versus, 31.0`
- Narration: Two-stage fine-tuning pushes fusion to 53.7 mAP versus 31.0.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_two_stage_fine_tuning_pushes_fusion" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two-stage, fine-tuning, pushes, fusion, 53.7, map in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_two_ablations_stand_out`

- Preferred role: `content`
- Cue keywords: `two, ablations, stand, out`
- Narration: Two ablations stand out.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_two_ablations_stand_out" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, ablations, stand, out in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_representing_element_bounding_box_tw`

- Preferred role: `content`
- Cue keywords: `representing, element, bounding, box, two, keypoints, beats, start-middle-end, extreme-point, alternatives`
- Narration: Representing each element by a bounding box with two keypoints beats start-middle-end and extreme-point alternatives by two Fréchet and over seven Chamfer points.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_representing_element_bounding_box_tw" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords representing, element, bounding, box, two, keypoints in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_two_stage_teacher_forcing_fine_tunin`

- Preferred role: `method`
- Cue keywords: `two-stage, teacher, forcing, fine-tuning, predicted, keypoints, adds, about, seven, map`
- Narration: Two-stage training, teacher forcing then fine-tuning on predicted keypoints, adds about seven mAP for camera and over eight for fusion.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_two_stage_teacher_forcing_fine_tunin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two-stage, teacher, forcing, fine-tuning, predicted, keypoints in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_summarize_vectormapnet_exceeds_previ`

- Preferred role: `content`
- Cue keywords: `summarize, vectormapnet, exceeds, previous, state, art, 14.2, map, nuscenes, 14.6`
- Narration: To summarize: VectorMapNet exceeds the previous state of the art by 14.2 mAP on nuScenes and 14.6 on Argoverse2.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_summarize_vectormapnet_exceeds_previ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords summarize, vectormapnet, exceeds, previous, state, art in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_its_best_configuration_fusion_fine_t`

- Preferred role: `result`
- Cue keywords: `its, best, configuration, fusion, fine-tuning, reaches, 53.7, map, where, hdmapnet`
- Narration: Its best configuration, fusion with fine-tuning, reaches 53.7 mAP where HDMapNet reaches 31.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_its_best_configuration_fusion_fine_t" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, best, configuration, fusion, fine-tuning, reaches in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_gains_span_sensors_about_eighteen`

- Preferred role: `result`
- Cue keywords: `gains, span, sensors, about, eighteen, camera, ten, lidar, fourteen, fusion`
- Narration: Gains span sensors: about eighteen for camera, ten for LiDAR, fourteen for fusion.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_gains_span_sensors_about_eighteen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gains, span, sensors, about, eighteen, camera in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_mapping_needs_rasterize_the`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, mapping, needs, rasterize-then-vectorize, detour`
- Narration: The takeaway: HD mapping needs no rasterize-then-vectorize detour.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_mapping_needs_rasterize_the" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, mapping, needs, rasterize-then-vectorize, detour in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_treating_mapping_detection_plus_auto`

- Preferred role: `method`
- Cue keywords: `treating, mapping, detection, plus, autoregressive, polyline, generation, vectormapnet, produces, directional`
- Narration: Treating mapping as detection plus autoregressive polyline generation, VectorMapNet produces directional vector maps directly from sensors, beats rasterized pipelines by double digits, and even extends to centerlines with no architectural change.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_treating_mapping_detection_plus_auto" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords treating, mapping, detection, plus, autoregressive, polyline in title/desc so the matcher can verify semantic overlap.
