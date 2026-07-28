# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_deep_networks_memorize_memorization`

- Preferred role: `method`
- Cue keywords: `deep, networks, memorize, memorization, ties, generalization, privacy`
- Narration: Deep networks memorize training data, and memorization ties to generalization and privacy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_deep_networks_memorize_memorization" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deep, networks, memorize, memorization, ties, generalization in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_feldman_memorization_score_rigorous`

- Preferred role: `method`
- Cue keywords: `feldman, memorization, score, rigorous, but, costly, while, input, loss, curvature`
- Narration: Feldman's memorization score is rigorous but costly, while input loss curvature is a cheap proxy nobody could justify.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_feldman_memorization_score_rigorous" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords feldman, memorization, score, rigorous, but, costly in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_purdue_icml_2024_builds_missing`

- Preferred role: `result`
- Cue keywords: `purdue, icml, 2024, builds, missing, theory, linking, memorization, curvature, differential`
- Narration: This Purdue ICML 2024 paper builds the missing theory linking memorization, curvature, and differential privacy on CIFAR and ImageNet.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c3_purdue_icml_2024_builds_missing" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords purdue, icml, 2024, builds, missing, theory in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_deep_networks_memorize_which_matters`

- Preferred role: `method`
- Cue keywords: `deep, networks, memorize, which, matters, generalization, noisy, learning, privacy, leakage`
- Narration: Deep networks memorize training data, which matters for generalization, noisy learning, and privacy leakage.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_deep_networks_memorize_which_matters" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deep, networks, memorize, which, matters, generalization in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_feldman_memorization_score_quantifie`

- Preferred role: `method`
- Cue keywords: `feldman, memorization, score, quantifies, rigorously, but, far, too, expensive`
- Narration: Feldman's memorization score quantifies this rigorously but is far too expensive.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_feldman_memorization_score_quantifie" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords feldman, memorization, score, quantifies, rigorously, but in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_input_loss_curvature_trace_input_los`

- Preferred role: `figure`
- Cue keywords: `input, loss, curvature, trace, input-loss, hessian, tracks, memorization, roughly, thousand`
- Narration: Input loss curvature, the trace of the input-loss Hessian, tracks memorization roughly a thousand times cheaper, yet the connection was purely empirical, with no theory linking either to differential privacy.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s02_c3_input_loss_curvature_trace_input_los" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords input, loss, curvature, trace, input-loss, hessian in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_proving_curvature_bounds_memorizatio`

- Preferred role: `method`
- Cue keywords: `proving, curvature, bounds, memorization, would, license, cheap, proxy, over, expensive`
- Narration: Proving curvature bounds memorization would license the cheap proxy over the expensive score.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_proving_curvature_bounds_memorizatio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords proving, curvature, bounds, memorization, would, license in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_because_memorization_privacy_risk_li`

- Preferred role: `content`
- Cue keywords: `because, memorization, privacy, risk, linking, differential, privacy, curvature, explains, why`
- Narration: Because memorization is a privacy risk, linking differential privacy to curvature explains why privacy reduces leakage.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_because_memorization_privacy_risk_li" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, memorization, privacy, risk, linking, differential in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_unlike_influence_functions_which_ass`

- Preferred role: `guidance`
- Cue keywords: `unlike, influence, functions, which, assume, hessian, convexity, fails, deep, nets`
- Narration: Unlike influence functions, which assume Hessian convexity that fails for deep nets, this framework needs no such assumptions.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s03_c3_unlike_influence_functions_which_ass" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unlike, influence, functions, which, assume, hessian in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_proves_three_links_triangle_connecti`

- Preferred role: `figure`
- Cue keywords: `proves, three, links, triangle, connecting, memorization, input, loss, curvature, differential`
- Narration: The paper proves three links in a triangle connecting memorization, input loss curvature, and differential privacy.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c1_proves_three_links_triangle_connecti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords proves, three, links, triangle, connecting, memorization in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_curvature_upper_bounds_memoriz`

- Preferred role: `result`
- Cue keywords: `first, curvature, upper-bounds, memorization, second, privacy, parameter, upper-bounds, average, curvature`
- Narration: First, curvature upper-bounds memorization. Second, the privacy parameter upper-bounds average curvature.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c2_first_curvature_upper_bounds_memoriz" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, curvature, upper-bounds, memorization, second, privacy in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_privacy_bounds_memorization_di`

- Preferred role: `content`
- Cue keywords: `third, privacy, bounds, memorization, directly`
- Narration: Third, privacy bounds memorization directly.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_third_privacy_bounds_memorization_di" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, privacy, bounds, memorization, directly in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_none_assume_hessian_convexity_they`

- Preferred role: `takeaway`
- Cue keywords: `none, assume, hessian, convexity, they, hold, real, deep, networks, all`
- Narration: None assume Hessian convexity, so they hold for real deep networks, and all three are validated empirically.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s04_c4_none_assume_hessian_convexity_they" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords none, assume, hessian, convexity, they, hold in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_theory_starts_second_order_nesterov`

- Preferred role: `figure`
- Cue keywords: `theory, starts, second-order, nesterov-polyak, expansion, loss, introducing, input, hessian`
- Narration: The theory starts from a second-order Nesterov-Polyak expansion of the loss, introducing the input Hessian.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c1_theory_starts_second_order_nesterov" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords theory, starts, second-order, nesterov-polyak, expansion, loss in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_zero_mean_perturbation_cancels_first`

- Preferred role: `content`
- Cue keywords: `zero-mean, perturbation, cancels, first-order, terms, taking, expectations, bounds, memorization, expected`
- Narration: A zero-mean perturbation cancels first-order terms, and taking expectations bounds memorization by expected curvature plus a data-independent offset.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_zero_mean_perturbation_cancels_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords zero-mean, perturbation, cancels, first-order, terms, taking in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_definition_differential_privacy_smal`

- Preferred role: `content`
- Cue keywords: `definition, differential, privacy, smaller, epsilon, forces, lower, curvature`
- Narration: With the definition of differential privacy, a smaller epsilon forces lower curvature.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_definition_differential_privacy_smal" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords definition, differential, privacy, smaller, epsilon, forces in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_curvature_itself_estimated_cheaply_v`

- Preferred role: `content`
- Cue keywords: `curvature, itself, estimated, cheaply, via, hutchinson, trace, estimator`
- Narration: Curvature itself is estimated cheaply via Hutchinson's trace estimator.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_curvature_itself_estimated_cheaply_v" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords curvature, itself, estimated, cheaply, via, hutchinson in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_validation_cifar10_cifar100_imagenet`

- Preferred role: `result`
- Cue keywords: `validation, cifar10, cifar100, imagenet`
- Narration: Validation uses CIFAR10, CIFAR100, and ImageNet.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_validation_cifar10_cifar100_imagenet" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords validation, cifar10, cifar100, imagenet in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_memorization_relies_feldman_zhang_pr`

- Preferred role: `method`
- Cue keywords: `memorization, relies, feldman, zhang, precomputed, scores, ensembles, thousand, models, cifar100`
- Narration: Memorization relies on Feldman and Zhang's precomputed scores and ensembles, a thousand models on CIFAR100 and a hundred on ImageNet, using Small Inception and ResNet50.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_memorization_relies_feldman_zhang_pr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords memorization, relies, feldman, zhang, precomputed, scores in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_privacy_experiments_train_resnet18_d`

- Preferred role: `content`
- Cue keywords: `privacy, experiments, train, resnet18, dp-sgd, across, several, budgets`
- Narration: Privacy experiments train ResNet18 with DP-SGD across several budgets.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_privacy_experiments_train_resnet18_d" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords privacy, experiments, train, resnet18, dp-sgd, across in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_every_prediction_holds`

- Preferred role: `content`
- Cue keywords: `every, prediction, holds`
- Narration: Every prediction holds.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_every_prediction_holds" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords every, prediction, holds in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_memorization_plotted_against_input_l`

- Preferred role: `method`
- Cue keywords: `memorization, plotted, against, input, loss, curvature, shows, strong, linear, trend`
- Narration: Memorization plotted against input loss curvature shows a strong linear trend on CIFAR100 and ImageNet, especially clean on ImageNet.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_memorization_plotted_against_input_l" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords memorization, plotted, against, input, loss, curvature in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_stronger_privacy_drives_curvature_do`

- Preferred role: `method`
- Cue keywords: `stronger, privacy, drives, curvature, down, along, predicted, curve, most-memorized, examples`
- Narration: Stronger privacy drives curvature down along the predicted curve, and for the most-memorized examples, memorization rises with the privacy budget while staying under the theoretical bound.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_stronger_privacy_drives_curvature_do" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stronger, privacy, drives, curvature, down, along in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_curvature_hutchinson_trace_estimator`

- Preferred role: `content`
- Cue keywords: `curvature, hutchinson, trace, estimator, step, 1, e-3, ten, rademacher, vectors`
- Narration: Curvature uses Hutchinson's trace estimator with step 1e-3 and ten Rademacher vectors, cheap enough to run at scale.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_curvature_hutchinson_trace_estimator" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords curvature, hutchinson, trace, estimator, step, 1 in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_privacy_sweeps_epsilon_over_one`

- Preferred role: `content`
- Cue keywords: `privacy, sweeps, epsilon, over, one, ten, twenty, thirty, forty, fifty`
- Narration: Privacy sweeps epsilon over one, ten, twenty, thirty, forty, and fifty at delta 1e-5, averaging ten seeds.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_privacy_sweeps_epsilon_over_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords privacy, sweeps, epsilon, over, one, ten in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_five_hundred_most_memorized_cifar100`

- Preferred role: `method`
- Cue keywords: `five, hundred, most-memorized, cifar100, examples, collapse, under, strong, privacy, recover`
- Narration: The five hundred most-memorized CIFAR100 examples collapse under strong privacy and recover as epsilon grows.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_five_hundred_most_memorized_cifar100" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords five, hundred, most-memorized, cifar100, examples, collapse in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_work`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, work`
- Narration: A few numbers capture the work.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_work" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, work in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_input_loss_curvature_about_three`

- Preferred role: `method`
- Cue keywords: `input, loss, curvature, about, three, orders, magnitude, cheaper, feldman, score`
- Narration: Input loss curvature is about three orders of magnitude cheaper than the Feldman score.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_input_loss_curvature_about_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords input, loss, curvature, about, three, orders in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_ground_truth_averages_thousand_model`

- Preferred role: `result`
- Cue keywords: `ground, truth, averages, thousand, models, cifar100, hundred, imagenet`
- Narration: Ground truth averages a thousand models on CIFAR100 and a hundred on ImageNet.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_ground_truth_averages_thousand_model" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ground, truth, averages, thousand, models, cifar100 in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_privacy_sweeps_epsilon_one_fifty`

- Preferred role: `content`
- Cue keywords: `privacy, sweeps, epsilon, one, fifty, delta, 1, e-5, three, theorems`
- Narration: Privacy sweeps epsilon from one to fifty at delta 1e-5. Three theorems tie the triangle together.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_privacy_sweeps_epsilon_one_fifty" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords privacy, sweeps, epsilon, one, fifty, delta in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_empirical_curvature_memorization_lin`

- Preferred role: `qr`
- Cue keywords: `empirical, curvature-memorization, link, now, rests, firm, theory`
- Narration: The empirical curvature-memorization link now rests on firm theory.
- Authoring: Create or label one visible qr region for this narration chunk. Use id="cue_s10_c1_empirical_curvature_memorization_lin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords empirical, curvature-memorization, link, now, rests, firm in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_curvature_provably_upper_bounds_memo`

- Preferred role: `takeaway`
- Cue keywords: `curvature, provably, upper-bounds, memorization, itself, bounded, differential, privacy, parameter, closing`
- Narration: Curvature provably upper-bounds memorization and is itself bounded by the differential privacy parameter, closing the triangle.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c2_curvature_provably_upper_bounds_memo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords curvature, provably, upper-bounds, memorization, itself, bounded in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_needing_hessian_convexity_assumption`

- Preferred role: `content`
- Cue keywords: `needing, hessian-convexity, assumptions, applies, real, deep, networks, cheap, curvature, justified`
- Narration: Needing no Hessian-convexity assumptions, it applies to real deep networks, so cheap curvature is a justified proxy, and privacy provably suppresses both.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_needing_hessian_convexity_assumption" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords needing, hessian-convexity, assumptions, applies, real, deep in title/desc so the matcher can verify semantic overlap.
