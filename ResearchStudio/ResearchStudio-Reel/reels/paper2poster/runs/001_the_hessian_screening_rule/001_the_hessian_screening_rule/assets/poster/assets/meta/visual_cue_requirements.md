# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_work_presented_neurips_2022_johan`

- Preferred role: `guidance`
- Cue keywords: `work, presented, neurips, 2022, johan, larsson, jonas, wallin, lund, university`
- Narration: This work, presented at NeurIPS 2022 by Johan Larsson and Jonas Wallin of Lund University, introduces the Hessian Screening Rule, a new way to speed up fitting the lasso regularization path.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s01_c1_work_presented_neurips_2022_johan" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, presented, neurips, 2022, johan, larsson in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_screening_rules_discard_predictors_b`

- Preferred role: `guidance`
- Cue keywords: `screening, rules, discard, predictors, before, fit, shrinking, problem`
- Narration: Screening rules discard predictors before a model is fit, shrinking the problem.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s01_c2_screening_rules_discard_predictors_b" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords screening, rules, discard, predictors, before, fit in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_authors_show_second_order_hessian_in`

- Preferred role: `method`
- Cue keywords: `authors, show, second-order, hessian, information, yields, both, far, tighter, screening`
- Narration: The authors show that using second-order Hessian information yields both far tighter screening and much more accurate warm starts, especially when predictors are highly correlated, where existing rules struggle most.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_authors_show_second_order_hessian_in" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, show, second-order, hessian, information, yields in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_result_method_fastest_across_nearly`

- Preferred role: `method`
- Cue keywords: `result, method, fastest, across, nearly, every, simulated, real, benchmark, they`
- Narration: The result is a method that is the fastest across nearly every simulated and real benchmark they tested.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_result_method_fastest_across_nearly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, method, fastest, across, nearly, every in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_sparse_regression_lasso_workhorse_hi`

- Preferred role: `content`
- Cue keywords: `sparse, regression, lasso, workhorse, high-dimensional, but, fitting, expensive`
- Narration: Sparse regression with the lasso is a workhorse for high-dimensional data, but fitting it is expensive.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_sparse_regression_lasso_workhorse_hi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sparse, regression, lasso, workhorse, high-dimensional, but in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_best_penalty_strength_never_known`

- Preferred role: `method`
- Cue keywords: `best, penalty, strength, never, known, advance, practitioners, fit, entire, path`
- Narration: The best penalty strength is never known in advance, so practitioners fit an entire path of models across many penalty values and tune by cross-validation, refitting again and again.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_best_penalty_strength_never_known" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords best, penalty, strength, never, known, advance in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_screening_rules_help_discarding_pred`

- Preferred role: `guidance`
- Cue keywords: `screening, rules, help, discarding, predictors, before, solver, even, runs, shrinking`
- Narration: Screening rules help by discarding predictors before the solver even runs, shrinking each subproblem.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s02_c3_screening_rules_help_discarding_pred" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords screening, rules, help, discarding, predictors, before in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_trouble_widely_used_rules_become`

- Preferred role: `method`
- Cue keywords: `trouble, widely, used, rules, become, conservative, inefficient, precisely, when, predictors`
- Narration: The trouble is that the widely used rules become conservative and inefficient precisely when predictors are strongly correlated, which is exactly the regime where speed matters most.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_trouble_widely_used_rules_become" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trouble, widely, used, rules, become, conservative in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_authors_start_unifying_observation_p`

- Preferred role: `method`
- Cue keywords: `authors, start, unifying, observation, popular, strong, rule, working-set, strategy, both`
- Narration: The authors start from a unifying observation: the popular strong rule and the working-set strategy can both be expressed as estimates of the gradient, or correlation, at the next step of the path.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_authors_start_unifying_observation_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, start, unifying, observation, popular, strong in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_when_they_lean_only_first_order`

- Preferred role: `content`
- Cue keywords: `when, they, lean, only, first-order, information, these, estimates, crude, especially`
- Narration: When they lean only on first-order information, these estimates are crude, especially under high correlation. That crudeness has two costs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_when_they_lean_only_first_order" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, they, lean, only, first-order, information in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_screening_becomes_conservative_keepi`

- Preferred role: `content`
- Cue keywords: `screening, becomes, conservative, keeping, far, more, predictors, necessary, warm, starts`
- Narration: Screening becomes conservative, keeping far more predictors than necessary, and the warm starts that seed each optimization are inaccurate, so the solver needs many more passes to converge.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_screening_becomes_conservative_keepi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords screening, becomes, conservative, keeping, far, more in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_both_problems_point_same_fix`

- Preferred role: `content`
- Cue keywords: `both, problems, point, same, fix, richer, curvature, information, hessian`
- Narration: Both problems point to the same fix, richer curvature information from the Hessian.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_both_problems_point_same_fix" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords both, problems, point, same, fix, richer in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_their_contribution_hessian_screening`

- Preferred role: `guidance`
- Cue keywords: `their, contribution, hessian, screening, rule, exploits, second-order, information, two, complementary`
- Narration: Their contribution is the Hessian Screening Rule. It exploits second-order information in two complementary ways.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s04_c1_their_contribution_hessian_screening" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords their, contribution, hessian, screening, rule, exploits in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_hessian_gives_sharper_estimate`

- Preferred role: `content`
- Cue keywords: `first, hessian, gives, sharper, estimate, correlation, next, penalty, value, which`
- Narration: First, the Hessian gives a sharper estimate of the correlation at the next penalty value, which translates into far tighter screening.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_first_hessian_gives_sharper_estimate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, hessian, gives, sharper, estimate, correlation in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_same_hessian_its_inverse`

- Preferred role: `content`
- Cue keywords: `second, same, hessian, its, inverse, yield, warm, start, nearly, exact`
- Narration: Second, the same Hessian and its inverse yield a warm start that is nearly the exact solution whenever the active set does not change, cutting the number of solver passes dramatically.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_second_same_hessian_its_inverse" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, same, hessian, its, inverse, yield in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_authors_also_show_how_update`

- Preferred role: `method`
- Cue keywords: `authors, also, show, how, update, hessian, its, inverse, efficiently, active`
- Narration: The authors also show how to update the Hessian and its inverse efficiently as the active set changes, extend the method to general smooth convex losses like logistic regression, and release a full C++ and R implementation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_authors_also_show_how_update" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, also, show, how, update, hessian in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_rests_simple_fact_any`

- Preferred role: `method`
- Cue keywords: `method, rests, simple, fact, any, interval, where, active, set, nonzero`
- Narration: The method rests on a simple fact: on any interval where the active set of nonzero coefficients is unchanged, the lasso solution is a linear function of the penalty λ.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_rests_simple_fact_any" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, rests, simple, fact, any, interval in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_linearity_lets_authors_write_down`

- Preferred role: `content`
- Cue keywords: `linearity, lets, authors, write, down, second-order, estimate, correlation, next, penalty`
- Narration: That linearity lets the authors write down a second-order estimate of the correlation at the next penalty value using the Hessian of the active predictors.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_linearity_lets_authors_write_down" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords linearity, lets, authors, write, down, second-order in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_keep_cheap_they_restrict_expensive`

- Preferred role: `method`
- Cue keywords: `keep, cheap, they, restrict, expensive, inner, products, strong-rule, set, add`
- Narration: To keep it cheap, they restrict the expensive inner products to the strong-rule set and add a small fraction of the unit bound as a safety margin. The very same Hessian inverse provides the warm start, which is exact when the active set does not change, so the solver often converges in a single pass.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_keep_cheap_they_restrict_expensive" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords keep, cheap, they, restrict, expensive, inner in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_efficient_low_rank_updates_keep_hess`

- Preferred role: `content`
- Cue keywords: `efficient, low-rank, updates, keep, hessian, its, inverse, current, predictors, enter`
- Narration: Efficient low-rank updates keep the Hessian and its inverse current as predictors enter and leave, and an approximate-homotopy scheme adaptively chooses the penalty grid.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_efficient_low_rank_updates_keep_hess" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords efficient, low-rank, updates, keep, hessian, its in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_cover_both_simulated_rea`

- Preferred role: `content`
- Cue keywords: `experiments, cover, both, simulated, real`
- Narration: The experiments cover both simulated and real data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_experiments_cover_both_simulated_rea" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, cover, both, simulated, real in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_simulated_gaussian_designs_they_swee`

- Preferred role: `result`
- Cue keywords: `simulated, gaussian, designs, they, sweep, low-dimensional, regime, ten, thousand, observations`
- Narration: On simulated Gaussian designs, they sweep a low-dimensional regime with ten thousand observations and a hundred predictors and a high-dimensional regime with four hundred observations and forty thousand predictors, each at three correlation levels, zero, point four, and point eight, averaged over twenty repetitions.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_simulated_gaussian_designs_they_swee" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords simulated, gaussian, designs, they, sweep, low-dimensional in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_they_test_twelve_real_sets`

- Preferred role: `content`
- Cue keywords: `they, test, twelve, real, sets, both, 1, regularized, least-squares, logistic`
- Narration: They then test twelve real data sets for both ℓ1-regularized least-squares and logistic regression, ranging from small gene-expression matrices up to problems with millions of features such as news20 and rcv1.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_they_test_twelve_real_sets" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, test, twelve, real, sets, both in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_baselines_working_set_strategy_celer`

- Preferred role: `method`
- Cue keywords: `baselines, working-set, strategy, celer, blitz`
- Narration: Baselines are the working-set strategy, Celer, and Blitz.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_baselines_working_set_strategy_celer" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords baselines, working-set, strategy, celer, blitz in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_results_decisive_across_every_simula`

- Preferred role: `method`
- Cue keywords: `results, decisive, across, every, simulated, configuration, hessian, rule, takes, least`
- Narration: The results are decisive. Across every simulated configuration, the Hessian rule takes the least time, and its advantage is largest exactly where competitors struggle, the high-correlation, low-dimensional setting.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_results_decisive_across_every_simula" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, decisive, across, every, simulated, configuration in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_real_wins_nearly_all_twelve`

- Preferred role: `content`
- Cue keywords: `real, wins, nearly, all, twelve, sets`
- Narration: On real data it wins on nearly all twelve sets.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_real_wins_nearly_all_twelve" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords real, wins, nearly, all, twelve, sets in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_1_regularized_least_squares_fastest`

- Preferred role: `method`
- Cue keywords: `1, regularized, least-squares, fastest, all, five, all, but, one, case`
- Narration: For ℓ1-regularized least-squares it is fastest on all five, and in all but one case it finishes in under half the time of the next-best method, the working-set strategy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_1_regularized_least_squares_fastest" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords 1, regularized, least-squares, fastest, all, five in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_yearpredictionmsd_fits_full_path_sev`

- Preferred role: `result`
- Cue keywords: `yearpredictionmsd, fits, full, path, seventy-nine, seconds, against, five, hundred, forty-one`
- Narration: On YearPredictionMSD it fits the full path in seventy-nine seconds against five hundred forty-one for the runner-up, and on e2006-tfidf in fourteen seconds against one hundred forty-three, speedups of roughly seven to ten times.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c4_yearpredictionmsd_fits_full_path_sev" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords yearpredictionmsd, fits, full, path, seventy-nine, seconds in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_two_component_studies_show_where`

- Preferred role: `result`
- Cue keywords: `two, component, studies, show, where, gains, come`
- Narration: Two component studies show where the gains come from.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c1_two_component_studies_show_where" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, component, studies, show, where, gains in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_looking_warm_start_isolation_colon_c`

- Preferred role: `content`
- Cue keywords: `looking, warm, start, isolation, colon-cancer, yearpredictionmsd, hessian, warm, start, collapses`
- Narration: Looking at the warm start in isolation, on colon-cancer and YearPredictionMSD the Hessian warm start collapses the number of coordinate-descent passes, frequently to a single pass per step, because when the active set does not change the warm start is essentially the exact solution.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_looking_warm_start_isolation_colon_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords looking, warm, start, isolation, colon-cancer, yearpredictionmsd in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_looking_screening_isolation_hessian`

- Preferred role: `method`
- Cue keywords: `looking, screening, isolation, hessian, rule, keeps, number, retained, predictors, close`
- Narration: Looking at screening in isolation, the Hessian rule keeps the number of retained predictors close to the true active-set floor, while alternatives like Celer, Blitz, the strong rule, EDPP, Gap Safe, and Sasvi retain orders of magnitude more predictors, and the gap widens as correlation increases.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_looking_screening_isolation_hessian" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords looking, screening, isolation, hessian, rule, keeps in title/desc so the matcher can verify semantic overlap.

## Slide 09: takeaway

Heading: Takeaway

### Cue 1: `cue_s09_c1_takeaway_single_idea_reusing_second`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, single, idea, reusing, second-order, hessian, information, pays, off, twice`
- Narration: The takeaway is that a single idea, reusing second-order Hessian information, pays off twice over.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s09_c1_takeaway_single_idea_reusing_second" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, single, idea, reusing, second-order, hessian in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_tightens_screening_solver_sees_far`

- Preferred role: `content`
- Cue keywords: `tightens, screening, solver, sees, far, fewer, predictors, supplies, warm, starts`
- Narration: It tightens screening so the solver sees far fewer predictors, and it supplies warm starts so accurate that many path steps converge in one pass.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_tightens_screening_solver_sees_far" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tightens, screening, solver, sees, far, fewer in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_together_these_make_hessian_screenin`

- Preferred role: `method`
- Cue keywords: `together, these, make, hessian, screening, rule, fastest, method, fitting, lasso`
- Narration: Together these make the Hessian Screening Rule the fastest method for fitting lasso and ℓ1-regularized logistic regression paths across the benchmarks tested, with the biggest edge in the high-correlation regime that has historically been the hardest for screening rules.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_together_these_make_hessian_screenin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, these, make, hessian, screening, rule in title/desc so the matcher can verify semantic overlap.
