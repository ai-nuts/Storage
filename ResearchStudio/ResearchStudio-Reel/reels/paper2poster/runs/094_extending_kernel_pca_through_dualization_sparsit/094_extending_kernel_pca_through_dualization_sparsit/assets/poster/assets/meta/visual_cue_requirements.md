# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_leuven_presented_icml_2023_revisits`

- Preferred role: `figure`
- Cue keywords: `leuven, presented, icml, 2023, revisits, kernel, principal, component, analysis, through`
- Narration: This paper, from KU Leuven and presented at ICML 2023, revisits Kernel Principal Component Analysis through the lens of convex duality.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c1_leuven_presented_icml_2023_revisits" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords leuven, presented, icml, 2023, revisits, kernel in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_authors_reformulate_kernel_pca_diffe`

- Preferred role: `content`
- Cue keywords: `authors, reformulate, kernel, pca, difference, convex, functions, problem, dualize`
- Narration: The authors reformulate Kernel PCA as a difference of convex functions problem, then dualize it.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_authors_reformulate_kernel_pca_diffe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, reformulate, kernel, pca, difference, convex in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_single_move_unlocks_three_things`

- Preferred role: `result`
- Cue keywords: `single, move, unlocks, three, things, once, gradient-based, solvers, avoid, expensive`
- Narration: This single move unlocks three things at once: gradient-based solvers that avoid the expensive cubic singular value decomposition of the Gram matrix, a flexible framework that swaps in robust or sparse objectives through Moreau envelopes, and significant speedups on real benchmarks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c3_single_move_unlocks_three_things" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords single, move, unlocks, three, things, once in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_clean_example_how_right_optimization`

- Preferred role: `method`
- Cue keywords: `clean, example, how, right, optimization, viewpoint, extend, classical, method, several`
- Narration: It is a clean example of how the right optimization viewpoint can extend a classical method in several directions simultaneously.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_clean_example_how_right_optimization" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords clean, example, how, right, optimization, viewpoint in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_kernel_pca_one_most_widely`

- Preferred role: `figure`
- Cue keywords: `kernel, pca, one, most, widely, used, tools, unsupervised, learning, but`
- Narration: Kernel PCA is one of the most widely used tools in unsupervised learning, but it has a stubborn scaling problem.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s02_c1_kernel_pca_one_most_widely" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords kernel, pca, one, most, widely, used in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_standard_recipe_computes_singular_va`

- Preferred role: `content`
- Cue keywords: `standard, recipe, computes, singular, value, decomposition, n-by-n, gram, matrix, which`
- Narration: The standard recipe computes the singular value decomposition of the n-by-n Gram matrix, which costs order n-cubed and becomes painfully slow even for moderately sized datasets.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_standard_recipe_computes_singular_va" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords standard, recipe, computes, singular, value, decomposition in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_top_every_time_researchers_wanted`

- Preferred role: `method`
- Cue keywords: `top, every, time, researchers, wanted, robust, sparse, variant, kernel, pca`
- Narration: On top of that, every time researchers wanted a robust or a sparse variant of Kernel PCA, they reached for a different ad-hoc formulation or weighting heuristic, producing a scattered collection of unrelated optimization problems rather than one coherent method.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_top_every_time_researchers_wanted" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords top, every, time, researchers, wanted, robust in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_authors_observe_kernel_pca_written`

- Preferred role: `method`
- Cue keywords: `authors, observe, kernel, pca, written, variance, maximization, under, orthonormality, constraints`
- Narration: The authors observe that Kernel PCA can be written as variance maximization under orthonormality constraints, which puts it squarely in the family of difference-of-convex problems that optimization researchers understand well.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_authors_observe_kernel_pca_written" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, observe, kernel, pca, written, variance in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_earlier_work_had_studied_pca`

- Preferred role: `method`
- Cue keywords: `earlier, work, had, studied, pca, difference-of-convex, program, but, only, linear`
- Narration: Earlier work had studied PCA as a difference-of-convex program, but only for linear PCA, and often only for the first component where the orthogonality constraints vanish.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_earlier_work_had_studied_pca" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords earlier, work, had, studied, pca, difference-of-convex in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_meanwhile_separate_line_research_had`

- Preferred role: `method`
- Cue keywords: `meanwhile, separate, line, research, had, shown, infimal, convolution, elegant, way`
- Narration: Meanwhile, a separate line of research had shown that infimal convolution is an elegant way to build robust or sparse losses, and that these constructions behave especially nicely in dual formulations.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_meanwhile_separate_line_research_had" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords meanwhile, separate, line, research, had, shown in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_bringing_these_two_observations_toge`

- Preferred role: `content`
- Cue keywords: `bringing, these, two, observations, together, opening, exploits`
- Narration: Bringing these two observations together is the opening the paper exploits.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_bringing_these_two_observations_toge" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords bringing, these, two, observations, together, opening in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_core_contribution_general_dual_based`

- Preferred role: `content`
- Cue keywords: `core, contribution, general, dual-based, formulation, kernel, pca, built, dualization, difference`
- Narration: The core contribution is a general dual-based formulation of Kernel PCA built on the dualization of a difference of convex functions. This formulation does two things at once.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_core_contribution_general_dual_based" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, contribution, general, dual-based, formulation, kernel in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_turns_problem_one_over`

- Preferred role: `method`
- Cue keywords: `first, turns, problem, one, over, finite-dimensional, dual, matrix, which, solved`
- Narration: First, it turns the problem into one over a finite-dimensional dual matrix, which can be solved with efficient gradient-based methods and avoids the expensive singular value decomposition, even when the feature space is infinite-dimensional.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_turns_problem_one_over" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, turns, problem, one, over, finite-dimensional in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_makes_objective_modular_choos`

- Preferred role: `guidance`
- Cue keywords: `second, makes, objective, modular, choosing, objectives, expressible, moreau, envelopes, same`
- Narration: Second, it makes the objective modular: by choosing objectives expressible as Moreau envelopes, the same framework promotes robustness or sparsity without leaving the dual picture.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s04_c3_second_makes_objective_modular_choos" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, makes, objective, modular, choosing, objectives in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_authors_supply_supporting_theory_con`

- Preferred role: `content`
- Cue keywords: `authors, supply, supporting, theory, concrete, l-bfgs, difference-of-convex, algorithms, proximal, operators`
- Narration: The authors supply the supporting theory, concrete L-BFGS and difference-of-convex algorithms, and the proximal operators needed to make the robust and sparse cases practical.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_authors_supply_supporting_theory_con" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, supply, supporting, theory, concrete, l-bfgs in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_starts_writing_kernel_pca`

- Preferred role: `method`
- Cue keywords: `method, starts, writing, kernel, pca, minimization, difference, two, convex, functions`
- Narration: The method starts by writing Kernel PCA as the minimization of a difference of two convex functions over the Stiefel manifold of orthonormal frames.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_starts_writing_kernel_pca" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, starts, writing, kernel, pca, minimization in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_general_dualization_proposition_conv`

- Preferred role: `content`
- Cue keywords: `general, dualization, proposition, converts, primal, problem, whose, variables, live, possibly`
- Narration: A general dualization proposition then converts this primal problem, whose variables live in a possibly infinite-dimensional feature space, into a dual problem whose variable H is a finite n-by-s matrix, perfectly suited to gradient descent.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_general_dualization_proposition_conv" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords general, dualization, proposition, converts, primal, problem in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_indicator_function_stiefel_manifold`

- Preferred role: `content`
- Cue keywords: `indicator, function, stiefel, manifold, turns, dual, nuclear-norm, term, authors, call`
- Narration: The indicator function of the Stiefel manifold turns, in the dual, into a nuclear-norm term the authors call pi of H, equal to the trace of the square root of H-transpose G H. Its gradient only requires the singular value decomposition of a small s-by-s matrix, not the full n-by-n Gram matrix, which is the source of the speedup. For the standard problem they run L-BFGS.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_indicator_function_stiefel_manifold" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords indicator, function, stiefel, manifold, turns, dual in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_promote_robustness_sparsity_they_add`

- Preferred role: `figure`
- Cue keywords: `promote, robustness, sparsity, they, add, moreau-envelope, term, objective, optimize, difference-of-convex`
- Narration: To promote robustness or sparsity, they add a Moreau-envelope term to the objective and optimize with a difference-of-convex algorithm, plugging in closed-form proximal operators for the Huber and epsilon-insensitive losses.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c4_promote_robustness_sparsity_they_add" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords promote, robustness, sparsity, they, add, moreau-envelope in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_span_synthetic_real_worl`

- Preferred role: `content`
- Cue keywords: `experiments, span, synthetic, real-world`
- Narration: The experiments span synthetic and real-world data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_experiments_span_synthetic_real_worl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, span, synthetic, real-world in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_efficiency_authors_time_kernel_pca`

- Preferred role: `result`
- Cue keywords: `efficiency, authors, time, kernel, pca, synthetic, 7, 000, point, problem`
- Narration: For efficiency, the authors time Kernel PCA on a synthetic 7,000-point problem, the Protein dataset with about 15,000 points, the RCV1 text collection with roughly 20,000 points, and CIFAR-10 with 60,000 images.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_efficiency_authors_time_kernel_pca" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords efficiency, authors, time, kernel, pca, synthetic in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_robustness_tested_artificially_conta`

- Preferred role: `method`
- Cue keywords: `robustness, tested, artificially, contaminating, iris, dataset, multiplicative, gaussian, outliers, sparsity`
- Narration: Robustness is tested by artificially contaminating the Iris dataset with multiplicative Gaussian outliers, and sparsity is measured through reconstruction error under epsilon-insensitive losses.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_robustness_tested_artificially_conta" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords robustness, tested, artificially, contaminating, iris, dataset in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_all_solvers_compared_fairly_shared`

- Preferred role: `method`
- Cue keywords: `all, solvers, compared, fairly, shared, relative, dual-cost, residual, stopping, criterion`
- Narration: All solvers are compared fairly using a shared relative dual-cost residual as the stopping criterion at two tolerance levels, and the timing results are averaged over five runs.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_all_solvers_compared_fairly_shared" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords all, solvers, compared, fairly, shared, relative in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_efficiency_benchmarks_proposed_solve`

- Preferred role: `result`
- Cue keywords: `efficiency, benchmarks, proposed, solver, wins, across, board`
- Narration: On the efficiency benchmarks, the proposed solver wins across the board.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_efficiency_benchmarks_proposed_solve" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords efficiency, benchmarks, proposed, solver, wins, across in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_looser_tolerance_ten_to_the_minus_tw`

- Preferred role: `result`
- Cue keywords: `looser, tolerance, ten-to-the-minus-two, faster, full, svd, lanczos, randomized, svd, every`
- Narration: At the looser tolerance of ten-to-the-minus-two, it is faster than full SVD, Lanczos, and randomized SVD on every task, and it is at least three times faster than randomized SVD, peaking at a nine-point-one-seven times speedup on CIFAR-10 with its sixty thousand images, where full SVD could not even finish within thirty minutes.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_looser_tolerance_ten_to_the_minus_tw" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords looser, tolerance, ten-to-the-minus-two, faster, full, svd in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_just_importantly_method_robust_prope`

- Preferred role: `method`
- Cue keywords: `just, importantly, method, robust, property, hurts, randomized, svd, badly, eigenspectrum`
- Narration: Just as importantly, the method is robust to a property that hurts randomized SVD badly: as the eigenspectrum of the Gram matrix decays more slowly, randomized SVD needs many more oversamples, while the proposed solver's iteration count barely changes.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_just_importantly_method_robust_prope" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords just, importantly, method, robust, property, hurts in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_several_controlled_studies_dissect_b`

- Preferred role: `content`
- Cue keywords: `several, controlled, studies, dissect, behavior`
- Narration: Several controlled studies dissect the behavior.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_several_controlled_studies_dissect_b" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords several, controlled, studies, dissect, behavior in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_sweeping_huber_loss_parameter_kappa`

- Preferred role: `result`
- Cue keywords: `sweeping, huber, loss, parameter, kappa, shows, both, huber, variants, consistently`
- Narration: Sweeping the Huber loss parameter kappa shows that both Huber variants consistently reduce mean squared error on the contaminated Iris data compared to the ordinary squared loss, confirming the robustness the framework is designed to induce.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_sweeping_huber_loss_parameter_kappa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sweeping, huber, loss, parameter, kappa, shows in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_varying_number_components_shows_l_bf`

- Preferred role: `result`
- Cue keywords: `varying, number, components, shows, l-bfgs, solver, keeps, its, speed, advantage`
- Narration: Varying the number of components shows that the L-BFGS solver keeps its speed advantage over randomized SVD across a wide range, and only at very large numbers of components does the per-iteration small SVD start to slow it down.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c3_varying_number_components_shows_l_bf" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords varying, number, components, shows, l-bfgs, solver in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_eigenspectrum_study_pinpoints_scalin`

- Preferred role: `result`
- Cue keywords: `eigenspectrum, study, pinpoints, scaling, advantage, spectrum, decays, more, slowly, randomized`
- Narration: And the eigenspectrum study pinpoints the scaling advantage: as the spectrum decays more slowly, randomized SVD's oversample count climbs sharply while the proposed solver's iteration count stays essentially flat.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_eigenspectrum_study_pinpoints_scalin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords eigenspectrum, study, pinpoints, scaling, advantage, spectrum in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact_cifar_10`

- Preferred role: `method`
- Cue keywords: `few, numbers, capture, impact, cifar-10, method, delivers, nine-point-one-seven, times, speedup`
- Narration: A few numbers capture the impact. On CIFAR-10 the method delivers a nine-point-one-seven times speedup over randomized SVD, and it is at least three times faster than randomized SVD on every efficiency task.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact_cifar_10" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact, cifar-10, method in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_key_complexity_change_iteration_cost`

- Preferred role: `content`
- Cue keywords: `key, complexity, change, iteration, costs, order, s-cubed, small, s-by-s, singular`
- Narration: The key complexity change is that each iteration costs order s-cubed for a small s-by-s singular value decomposition, replacing the classical order n-cubed decomposition of the full Gram matrix.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_key_complexity_change_iteration_cost" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, complexity, change, iteration, costs, order in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_robustness_side_huber_loss_cuts`

- Preferred role: `result`
- Cue keywords: `robustness, side, huber, loss, cuts, mean, squared, error, contaminated, iris`
- Narration: On the robustness side, the Huber loss cuts the mean squared error on contaminated Iris from about seven-point-five-nine down to six-point-eight-three at the tested corruption level.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_robustness_side_huber_loss_cuts" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords robustness, side, huber, loss, cuts, mean in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_these_results_scale_datasets_sixty`

- Preferred role: `result`
- Cue keywords: `these, results, scale, datasets, sixty, thousand, points, where, full, svd`
- Narration: And these results scale to datasets with sixty thousand points, where full SVD could not finish within thirty minutes.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c4_these_results_scale_datasets_sixty" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, results, scale, datasets, sixty, thousand in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_message_single_change_viewpo`

- Preferred role: `content`
- Cue keywords: `lasting, message, single, change, viewpoint, pays, off, three, directions, once`
- Narration: The lasting message is that a single change of viewpoint pays off in three directions at once.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c1_lasting_message_single_change_viewpo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, single, change, viewpoint, pays in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_writing_kernel_pca_difference_convex`

- Preferred role: `result`
- Cue keywords: `writing, kernel, pca, difference, convex, functions, moving, dual, authors, get`
- Narration: By writing Kernel PCA as a difference of convex functions and moving to the dual, the authors get a solver that avoids the expensive singular value decomposition and runs up to nine times faster than randomized SVD, and in the same breath they gain a modular way to demand robustness or sparsity just by picking the right Moreau-envelope objective.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c2_writing_kernel_pca_difference_convex" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords writing, kernel, pca, difference, convex, functions in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_because_dual_variable_always_finite`

- Preferred role: `result`
- Cue keywords: `because, dual, variable, always, finite-dimensional, framework, even, reaches, infinite-dimensional, feature`
- Narration: Because the dual variable is always finite-dimensional, the framework even reaches infinite-dimensional feature maps that classical Kernel PCA simply cannot handle.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c3_because_dual_variable_always_finite" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, dual, variable, always, finite-dimensional, framework in title/desc so the matcher can verify semantic overlap.
