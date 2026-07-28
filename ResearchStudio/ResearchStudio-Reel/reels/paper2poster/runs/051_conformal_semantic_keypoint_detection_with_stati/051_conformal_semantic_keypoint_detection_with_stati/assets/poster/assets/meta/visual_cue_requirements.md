# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_nvidia_research_cvpr_2023_work`

- Preferred role: `method`
- Cue keywords: `nvidia, research, cvpr, 2023, work, closes, safety-critical, gap, object, pose`
- Narration: From NVIDIA Research at CVPR 2023, this work closes a safety-critical gap in object pose estimation. Standard two-stage pipelines detect keypoints, then solve for the 6D pose, but give no guarantee on how wrong the answer might be. The authors add two pieces.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_nvidia_research_cvpr_2023_work" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords nvidia, research, cvpr, 2023, work, closes in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_conformal_keypoint_detection_turns_h`

- Preferred role: `result`
- Cue keywords: `conformal, keypoint, detection, turns, heatmap, detections, circular, elliptical, prediction, sets`
- Narration: Conformal keypoint detection turns heatmap detections into circular or elliptical prediction sets that provably cover the true keypoints with a chosen probability, say ninety percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c2_conformal_keypoint_detection_turns_h" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords conformal, keypoint, detection, turns, heatmap, detections in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_geometric_uncertainty_propagation_pu`

- Preferred role: `content`
- Cue keywords: `geometric, uncertainty, propagation, pushes, those, sets, through, geometry, form, pose`
- Narration: Geometric uncertainty propagation pushes those sets through the geometry to form a Pose Uncertainty Set, or PURSE, covering the true pose.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_geometric_uncertainty_propagation_pu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords geometric, uncertainty, propagation, pushes, those, sets in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_purse_they_compute_average_pose`

- Preferred role: `result`
- Cue keywords: `purse, they, compute, average, pose, semidefinite, relaxation, bound, worst-case, error`
- Narration: From PURSE they compute an average pose and use semidefinite relaxation to bound the worst-case error. On LineMOD Occlusion, coverage is valid and the bounds hold.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c4_purse_they_compute_average_pose" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords purse, they, compute, average, pose, semidefinite in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_estimating_object_6_pose_image`

- Preferred role: `content`
- Cue keywords: `estimating, object, 6, pose, image, underlies, augmented, reality, autonomous, driving`
- Narration: Estimating an object's 6D pose from an image underlies augmented reality, autonomous driving, robotic manipulation, and space robotics.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_estimating_object_6_pose_image" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords estimating, object, 6, pose, image, underlies in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_dominant_recipe_two_stages_first`

- Preferred role: `result`
- Cue keywords: `dominant, recipe, two, stages, first, detect, semantic, keypoints, recover, pose`
- Narration: The dominant recipe is two stages: first detect semantic keypoints, then recover the pose by minimizing reprojection error through Perspective-n-Points.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c2_dominant_recipe_two_stages_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dominant, recipe, two, stages, first, detect in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_these_methods_score_well_benchmarks`

- Preferred role: `method`
- Cue keywords: `these, methods, score, well, benchmarks, yet, they, return, single, pose`
- Narration: These methods score well on benchmarks, yet they return a single pose with no statement about how trustworthy it is.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_these_methods_score_well_benchmarks" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, methods, score, well, benchmarks, yet in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_safety_critical_systems_serious_gap`

- Preferred role: `result`
- Cue keywords: `safety-critical, systems, serious, gap, guarantee, keypoints, guarantee, optimizer, found, right`
- Narration: For safety-critical systems that is a serious gap: no guarantee on the keypoints, no guarantee the optimizer found the right pose, and no formal bound on the worst-case error against the truth.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c4_safety_critical_systems_serious_gap" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords safety-critical, systems, serious, gap, guarantee, keypoints in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_why_hard_authors_name_three`

- Preferred role: `content`
- Cue keywords: `why, hard, authors, name, three, challenges, first, neural, keypoint, detectors`
- Narration: Why is this hard? The authors name three challenges. First, neural keypoint detectors can be arbitrarily wrong, producing outliers.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_why_hard_authors_name_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords why, hard, authors, name, three, challenges in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_second_rejecting_those_outliers_nonc`

- Preferred role: `content`
- Cue keywords: `second, rejecting, those, outliers, nonconvex, optimization, fast, heuristics, like, ransac`
- Narration: Second, rejecting those outliers is a nonconvex optimization; fast heuristics like RANSAC are common but cannot guarantee global optimality and can fail silently.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_second_rejecting_those_outliers_nonc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, rejecting, those, outliers, nonconvex, optimization in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_third_most_fundamental_provably_corr`

- Preferred role: `result`
- Cue keywords: `third, most, fundamental, provably, correct, uncertainty, quantification, formal, worst-case, error`
- Narration: Third, and most fundamental, there is no provably correct uncertainty quantification, no formal worst-case error bound between estimate and groundtruth.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c3_third_most_fundamental_provably_corr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, most, fundamental, provably, correct, uncertainty in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_certifying_optimizer_globally_optima`

- Preferred role: `content`
- Cue keywords: `certifying, optimizer, globally, optimal, still, gives, probabilistic, guarantee, pose, itself`
- Narration: Certifying that the optimizer is globally optimal still gives no probabilistic guarantee on the pose itself. This paper delivers exactly that guarantee, end to end.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_certifying_optimizer_globally_optima" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords certifying, optimizer, globally, optimal, still, gives in title/desc so the matcher can verify semantic overlap.

## Slide 04: method

Heading: Method

### Cue 1: `cue_s04_c1_method_two_stages_conformal_keypoint`

- Preferred role: `method`
- Cue keywords: `method, two, stages, conformal, keypoint, detection, calibration, set, labeled, images`
- Narration: The method has two stages. In conformal keypoint detection, a calibration set of labeled images gives nonconformity scores for the heatmap detector.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_method_two_stages_conformal_keypoint" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, two, stages, conformal, keypoint, detection in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_two_designs_offered_peak_score`

- Preferred role: `method`
- Cue keywords: `two, designs, offered, peak, score, scaled, distance, true, keypoint, most`
- Narration: Two designs are offered: a peak score, the scaled distance from the true keypoint to the most probable pixel, and a covariance score, a Mahalanobis distance over top detections, yielding circular and elliptical sets.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_two_designs_offered_peak_score" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, designs, offered, peak, score, scaled in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_sorting_scores_gives_threshold_true`

- Preferred role: `method`
- Cue keywords: `sorting, scores, gives, threshold, true, keypoint, lies, its, set, probability`
- Narration: Sorting the scores gives a threshold so each true keypoint lies in its set with probability one minus epsilon. In geometric uncertainty propagation, these sets become quadratic constraints on the pose, defining the Pose Uncertainty Set.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_sorting_scores_gives_threshold_true" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sorting, scores, gives, threshold, true, keypoint in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_since_nonconvex_ransag_samples_three`

- Preferred role: `result`
- Cue keywords: `since, nonconvex, ransag, samples, three, keypoints, solves, minimal, p3p, problem`
- Narration: Since it is nonconvex, RANSAG samples three keypoints, solves the minimal P3P problem, keeps poses inside the set, and averages them. Finally, maximizing the distance to the farthest pose still inside PURSE, relaxed as a semidefinite program, certifies worst-case rotation and translation bounds.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c4_since_nonconvex_ransag_samples_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords since, nonconvex, ransag, samples, three, keypoints in title/desc so the matcher can verify semantic overlap.

## Slide 05: key-result

Heading: Key Result

### Cue 1: `cue_s05_c1_results_confirm_theory_three_fronts`

- Preferred role: `result`
- Cue keywords: `results, confirm, theory, three, fronts`
- Narration: The results confirm the theory on three fronts.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c1_results_confirm_theory_three_fronts" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, confirm, theory, three, fronts in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_first_coverage_valid_ninety_percent`

- Preferred role: `content`
- Cue keywords: `first, coverage, valid, ninety, percent, target, empirical, coverage, across, objects`
- Narration: First, coverage is valid: at a ninety percent target, empirical coverage across objects sits right around ninety percent and tightens as the calibration set grows.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_first_coverage_valid_ninety_percent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, coverage, valid, ninety, percent, target in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_second_bounds_correct_scatter_plots`

- Preferred role: `result`
- Cue keywords: `second, bounds, correct, scatter, plots, certified, bound, versus, actual, error`
- Narration: Second, the bounds are correct: in scatter plots of certified bound versus actual error, every case where PURSE covers the true pose stays below the diagonal, so the bound is never violated when the guarantee holds.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c3_second_bounds_correct_scatter_plots" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, bounds, correct, scatter, plots, certified in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_third_average_pose_accurate_beating`

- Preferred role: `method`
- Cue keywords: `third, average, pose, accurate, beating, prior, methods, two-dimensional, projection, metric`
- Narration: Third, the average pose is accurate, beating prior methods on the two-dimensional projection metric with groundtruth boxes and staying comparable with Faster-RCNN detections.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_third_average_pose_accurate_beating" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, average, pose, accurate, beating, prior in title/desc so the matcher can verify semantic overlap.

## Slide 06: takeaway

Heading: Takeaway

### Cue 1: `cue_s06_c1_lasting_message_you_turn_standard`

- Preferred role: `result`
- Cue keywords: `lasting, message, you, turn, standard, two-stage, pose, estimator, one, tells`
- Narration: The lasting message: you can turn a standard two-stage pose estimator into one that tells you how wrong it might be, with a real statistical guarantee, and pay little in accuracy.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_lasting_message_you_turn_standard" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, you, turn, standard, two-stage in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_conformal_prediction_supplies_covera`

- Preferred role: `content`
- Cue keywords: `conformal, prediction, supplies, coverage, keypoints, geometry, propagates, pose, purse, semidefinite`
- Narration: Conformal prediction supplies coverage on the keypoints, geometry propagates it to the pose as PURSE, and semidefinite relaxation converts the set into concrete worst-case bounds.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_conformal_prediction_supplies_covera" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords conformal, prediction, supplies, coverage, keypoints, geometry in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_because_wraps_any_heatmap_keypoint`

- Preferred role: `content`
- Cue keywords: `because, wraps, any, heatmap, keypoint, detector, approach, points, toward, provably`
- Narration: Because it wraps any heatmap keypoint detector, the approach points toward provably correct perception wherever safety matters.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_because_wraps_any_heatmap_keypoint" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, wraps, any, heatmap, keypoint, detector in title/desc so the matcher can verify semantic overlap.
