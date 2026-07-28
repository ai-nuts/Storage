# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_introduces_first_order_repulsive_dee`

- Preferred role: `content`
- Cue keywords: `introduces, first-order, repulsive, deep, ensembles, forde, new, way, train, neural`
- Narration: This paper introduces First-order Repulsive Deep Ensembles, or FoRDE, a new way to train neural network ensembles.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_introduces_first_order_repulsive_dee" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, first-order, repulsive, deep, ensembles, forde in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_deep_ensembles_work_well_because`

- Preferred role: `method`
- Cue keywords: `deep, ensembles, work, well, because, their, members, learn, diverse, functions`
- Narration: Deep ensembles work well because their members learn diverse functions, but existing methods that repel members in weight space or function space have struggled to improve on plain deep ensembles. The key idea here is to instead repel ensemble members in the space of their input gradients.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_deep_ensembles_work_well_because" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deep, ensembles, work, well, because, their in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_because_input_gradients_uniquely_cha`

- Preferred role: `content`
- Cue keywords: `because, input, gradients, uniquely, characterize, function, translation, far, smaller, weights`
- Narration: Because input gradients uniquely characterize a function up to translation and are far smaller than the weights, this guarantees members become functionally different and encourages each network to learn distinct features.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_because_input_gradients_uniquely_cha" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, input, gradients, uniquely, characterize, function in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_result_ensemble_markedly_more_robust`

- Preferred role: `result`
- Cue keywords: `result, ensemble, markedly, more, robust, better, calibrated, under, input, corruptions`
- Narration: The result is an ensemble that is markedly more robust and better calibrated under input corruptions.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c4_result_ensemble_markedly_more_robust" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, ensemble, markedly, more, robust, better in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_ensembles_neural_networks_powerful_b`

- Preferred role: `guidance`
- Cue keywords: `ensembles, neural, networks, powerful, because, different, members, capture, different, explanations`
- Narration: Ensembles of neural networks are powerful because different members capture different explanations of the data. Particle-based variational inference tries to make this diversity explicit by adding a repulsion term that pushes members apart. But where you apply that repulsion matters.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s02_c1_ensembles_neural_networks_powerful_b" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ensembles, neural, networks, powerful, because, different in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_repelling_weight_space_wasteful_beca`

- Preferred role: `content`
- Cue keywords: `repelling, weight, space, wasteful, because, neural, networks, heavily, over-parameterized, many`
- Narration: Repelling in weight space is wasteful, because neural networks are heavily over-parameterized and many different weights encode the same function.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_repelling_weight_space_wasteful_beca" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords repelling, weight, space, wasteful, because, neural in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_repelling_directly_function_space_so`

- Preferred role: `method`
- Cue keywords: `repelling, directly, function, space, sounds, appealing, but, requires, comparing, entire`
- Narration: Repelling directly in function space sounds appealing, but it requires comparing entire functions, which is computationally hard, and the shortcuts used in prior work led to underfitting.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_repelling_directly_function_space_so" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords repelling, directly, function, space, sounds, appealing in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_neither_weight_space_nor_function_sp`

- Preferred role: `result`
- Cue keywords: `neither, weight-space, nor, function-space, repulsion, had, delivered, meaningful, gains, over`
- Narration: So neither weight-space nor function-space repulsion had delivered meaningful gains over standard deep ensembles.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c4_neither_weight_space_nor_function_sp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords neither, weight-space, nor, function-space, repulsion, had in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_authors_take_third_view_neural`

- Preferred role: `method`
- Cue keywords: `authors, take, third, view, neural, network, beyond, its, weights, its`
- Narration: The authors take a third view of a neural network. Beyond its weights and its function values, a model can be represented, up to a translation, by its first-order input gradients, that is, the derivatives of the output with respect to the input.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_authors_take_third_view_neural" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, take, third, view, neural, network in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_representation_two_attractive_proper`

- Preferred role: `content`
- Cue keywords: `representation, two, attractive, properties, first, input, gradients, same, size, input`
- Narration: This representation has two attractive properties. First, input gradients are the same size as the input, which is far smaller than the enormous weight vector, so they are much cheaper to compare with a kernel.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_representation_two_attractive_proper" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords representation, two, attractive, properties, first, input in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_second_forcing_members_different_inp`

- Preferred role: `content`
- Cue keywords: `second, forcing, members, different, input, gradients, means, forcing, them, depend`
- Narration: Second, forcing members to have different input gradients means forcing them to depend on different input features.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_second_forcing_members_different_inp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, forcing, members, different, input, gradients in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_intuitively_should_make_ensemble_mor`

- Preferred role: `content`
- Cue keywords: `intuitively, should, make, ensemble, more, robust, because, members, react, complementary`
- Narration: Intuitively, this should make the ensemble more robust, because if members react to complementary patterns, corrupting one pattern will not fool all of them at once.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_intuitively_should_make_ensemble_mor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords intuitively, should, make, ensemble, more, robust in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_main_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, main, contributions`
- Narration: The paper makes three main contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_main_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, main, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_introduces_first_order_repulsi`

- Preferred role: `method`
- Cue keywords: `first, introduces, first-order, repulsive, deep, ensembles, method, adds, repulsion, term`
- Narration: First, it introduces First-order Repulsive Deep Ensembles, a method that adds a repulsion term defined on input gradients rather than weights or function outputs.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_introduces_first_order_repulsi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, introduces, first-order, repulsive, deep, ensembles in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_develops_practical_kernel_com`

- Preferred role: `method`
- Cue keywords: `second, develops, practical, kernel, compares, normalized, input, gradients, true, label`
- Narration: Second, it develops a practical kernel that compares the normalized input gradients of the true label across training data, keeping computation linear in the number of samples.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_develops_practical_kernel_com" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, develops, practical, kernel, compares, normalized in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_proposes_principled_way_choose`

- Preferred role: `content`
- Cue keywords: `third, proposes, principled, way, choose, kernel, lengthscales, principal, components, which`
- Narration: Third, it proposes a principled way to choose the kernel lengthscales using the principal components of the data, which lets FoRDE emphasize high-variance features and become especially robust to input corruptions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_third_proposes_principled_way_choose" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, proposes, principled, way, choose, kernel in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_forde_built_wasserstein_gradient_des`

- Preferred role: `method`
- Cue keywords: `forde, built, wasserstein, gradient, descent, particle-based, variational, inference, method, network`
- Narration: FoRDE is built on Wasserstein gradient descent, a particle-based variational inference method. Each network in the ensemble is a particle, and its update has two terms.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_forde_built_wasserstein_gradient_des" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords forde, built, wasserstein, gradient, descent, particle-based in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_driving_force_pulls_particle_toward`

- Preferred role: `method`
- Cue keywords: `driving, force, pulls, particle, toward, high-density, regions, bayesian, posterior, just`
- Narration: The driving force pulls the particle toward high-density regions of the Bayesian posterior, just like ordinary training. The repulsion force, weighted by a kernel, pushes particles apart. The crucial design choice is the kernel.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_driving_force_pulls_particle_toward" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords driving, force, pulls, particle, toward, high-density in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_instead_comparing_weights_outputs_fo`

- Preferred role: `method`
- Cue keywords: `instead, comparing, weights, outputs, forde, compares, input, gradients, true, label`
- Narration: Instead of comparing weights or outputs, FoRDE compares the input gradients of the true label, normalized to the unit sphere, using a radial basis function kernel. The gradients are normalized because their magnitude shrinks as training converges, and comparing directions teaches members to rely on complementary features.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_instead_comparing_weights_outputs_fo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, comparing, weights, outputs, forde, compares in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_finally_lengthscales_kernel_chosen_p`

- Preferred role: `method`
- Cue keywords: `finally, lengthscales, kernel, chosen, principal, components, repulsion, strongest, along, most`
- Narration: Finally, the lengthscales of the kernel are chosen from the principal components of the data, so repulsion is strongest along the most informative input directions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_finally_lengthscales_kernel_chosen_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finally, lengthscales, kernel, chosen, principal, components in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_method_tested_across_broad_range`

- Preferred role: `method`
- Cue keywords: `method, tested, across, broad, range, settings, illustrative, one-dimensional, regression, two-dimensional`
- Narration: The method is tested across a broad range of settings. Illustrative one-dimensional regression and two-dimensional classification tasks show how input-gradient repulsion increases uncertainty away from the data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_method_tested_across_broad_range" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, tested, across, broad, range, settings in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_main_image_classification_experiment`

- Preferred role: `result`
- Cue keywords: `main, image, classification, experiments, cifar-10, cifar-100, tinyimagenet, resnet, preactresnet, backbones`
- Narration: The main image classification experiments use CIFAR-10, CIFAR-100, and TinyImageNet, with ResNet and PreActResNet backbones and an ensemble of ten members.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_main_image_classification_experiment" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords main, image, classification, experiments, cifar-10, cifar-100 in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_measure_robustness_authors_corrupted`

- Preferred role: `result`
- Cue keywords: `measure, robustness, authors, corrupted, benchmarks, cifar-10-c, cifar-100-c, tinyimagenet-c, which, apply`
- Narration: To measure robustness, the authors use the corrupted benchmarks CIFAR-10-C, CIFAR-100-C, and TinyImageNet-C, which apply nineteen types of image corruption at five severity levels.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c3_measure_robustness_authors_corrupted" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords measure, robustness, authors, corrupted, benchmarks, cifar-10-c in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_they_report_accuracy_negative_log_li`

- Preferred role: `result`
- Cue keywords: `they, report, accuracy, negative, log-likelihood, expected, calibration, error, both, clean`
- Narration: They report accuracy, negative log-likelihood, and expected calibration error, both on clean data and averaged over all corruptions.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_they_report_accuracy_negative_log_li" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, report, accuracy, negative, log-likelihood, expected in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_across_corrupted_image_benchmarks_fo`

- Preferred role: `method`
- Cue keywords: `across, corrupted, image, benchmarks, forde, pca, lengthscales, strongest, method, every`
- Narration: Across the corrupted image benchmarks, FoRDE with PCA lengthscales is the strongest method on every metric, while remaining competitive on clean images.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_across_corrupted_image_benchmarks_fo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, corrupted, image, benchmarks, forde, pca in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_compared_second_best_method_improves`

- Preferred role: `method`
- Cue keywords: `compared, second-best, method, improves, accuracy, about, two, point, four, percent`
- Narration: Compared to the second-best method, it improves accuracy by about two point four percent on CIFAR-10-C and about one point three percent on CIFAR-100-C.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_compared_second_best_method_improves" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords compared, second-best, method, improves, accuracy, about in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_toy_experiments_tell_consistent_stor`

- Preferred role: `method`
- Cue keywords: `toy, experiments, tell, consistent, story, one, two, dimensions, forde, places`
- Narration: The toy experiments tell a consistent story: in one and two dimensions, FoRDE places higher uncertainty in regions away from the training data than deep ensembles and other repulsive methods, which is direct evidence that repelling input gradients yields greater functional diversity.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_toy_experiments_tell_consistent_stor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords toy, experiments, tell, consistent, story, one in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_carefully_ablates_kernel_lengthscale`

- Preferred role: `method`
- Cue keywords: `carefully, ablates, kernel, lengthscales, which, govern, how, repulsion, distributed, across`
- Narration: The paper carefully ablates the kernel lengthscales, which govern how repulsion is distributed across input dimensions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_carefully_ablates_kernel_lengthscale" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords carefully, ablates, kernel, lengthscales, which, govern in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_pca_lengthscales_give_best_robustnes`

- Preferred role: `content`
- Cue keywords: `pca, lengthscales, give, best, robustness, corruptions, because, they, emphasize, high-variance`
- Narration: The PCA lengthscales give the best robustness to corruptions, because they emphasize high-variance features.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_pca_lengthscales_give_best_robustnes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pca, lengthscales, give, best, robustness, corruptions in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_identity_lengthscales_instead_give_b`

- Preferred role: `method`
- Cue keywords: `identity, lengthscales, instead, give, best, clean, accuracy, cifar-100, best, likelihood`
- Narration: The identity lengthscales instead give the best clean accuracy on CIFAR-100 and the best likelihood on CIFAR-10, but sacrifice some robustness. Tuning between the two extremes yields the best of both worlds in most cases.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_identity_lengthscales_instead_give_b" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords identity, lengthscales, instead, give, best, clean in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_separate_study_varies_ensemble_size`

- Preferred role: `result`
- Cue keywords: `separate, study, varies, ensemble, size, finds, forde, ten, members, matches`
- Narration: A separate study varies the ensemble size and finds that a FoRDE with ten members matches or exceeds the corruption robustness of a deep ensemble with thirty members, showing that the diversity gain is substantial.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_separate_study_varies_ensemble_size" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords separate, study, varies, ensemble, size, finds in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, impact`
- Narration: A few numbers capture the impact.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_under_input_corruptions_forde_pca`

- Preferred role: `method`
- Cue keywords: `under, input, corruptions, forde, pca, lengthscales, improves, accuracy, about, two`
- Narration: Under input corruptions, FoRDE with PCA lengthscales improves accuracy by about two point four percent on CIFAR-10-C and one point three percent on CIFAR-100-C over the next-best method.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_under_input_corruptions_forde_pca" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords under, input, corruptions, forde, pca, lengthscales in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_its_diversity_efficient_too_ten_memb`

- Preferred role: `result`
- Cue keywords: `its, diversity, efficient, too, ten-member, forde, reaches, same, corruption, robustness`
- Narration: Its diversity is efficient too: a ten-member FoRDE reaches the same corruption robustness as a thirty-member deep ensemble.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_its_diversity_efficient_too_ten_memb" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, diversity, efficient, too, ten-member, forde in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_these_gains_hold_across_demanding`

- Preferred role: `result`
- Cue keywords: `these, gains, hold, across, demanding, benchmark, nineteen, corruption, types, five`
- Narration: And these gains hold across a demanding benchmark of nineteen corruption types at five severity levels each.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c4_these_gains_hold_across_demanding" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, gains, hold, across, demanding, benchmark in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_message_space_which_you`

- Preferred role: `guidance`
- Cue keywords: `lasting, message, space, which, you, enforce, diversity, matters, much, amount`
- Narration: The lasting message of this paper is that the space in which you enforce diversity matters as much as the amount.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s10_c1_lasting_message_space_which_you" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, space, which, you, enforce in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_repelling_ensemble_members_compact_s`

- Preferred role: `content`
- Cue keywords: `repelling, ensemble, members, compact, space, their, input, gradients, forde, guarantees`
- Narration: By repelling ensemble members in the compact space of their input gradients, FoRDE guarantees that members become genuinely different functions that rely on complementary features, without the waste of weight-space repulsion or the intractability of function-space repulsion.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_repelling_ensemble_members_compact_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords repelling, ensemble, members, compact, space, their in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_combined_data_driven_lengthscales_pr`

- Preferred role: `figure`
- Cue keywords: `combined, data-driven, lengthscales, principal, component, analysis, yields, ensembles, more, robust`
- Narration: Combined with data-driven lengthscales from principal component analysis, this yields ensembles that are more robust and better calibrated under the kinds of input corruptions that matter in the real world.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s10_c3_combined_data_driven_lengthscales_pr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords combined, data-driven, lengthscales, principal, component, analysis in title/desc so the matcher can verify semantic overlap.
