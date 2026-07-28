# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_semidefinite_programming_powerful_to`

- Preferred role: `content`
- Cue keywords: `semidefinite, programming, powerful, tool, combinatorial, optimization, but, long, been, considered`
- Narration: Semidefinite programming is a powerful tool for combinatorial optimization, but it has long been considered too expensive to run at real-world scale.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_semidefinite_programming_powerful_to" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords semidefinite, programming, powerful, tool, combinatorial, optimization in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_introduces_usbs_unified_spectral_bun`

- Preferred role: `content`
- Cue keywords: `introduces, usbs, unified, spectral, bundling, sketching, provably, correct, solver, fast`
- Narration: This paper introduces USBS, Unified Spectral Bundling with Sketching, a provably correct solver that is fast, scales to billions of decision variables, and, crucially, can reuse a previous solution as a warm start.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_introduces_usbs_unified_spectral_bun" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, usbs, unified, spectral, bundling, sketching in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_maxcut_instance_over_two_billion`

- Preferred role: `content`
- Cue keywords: `maxcut, instance, over, two, billion, variables, usbs, delivers, five-hundred-times, speedup`
- Narration: On a MaxCut instance with over two billion variables, USBS delivers a five-hundred-times speedup over the previous state of the art, and warm-starting alone can accelerate convergence by more than one hundred times.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_maxcut_instance_over_two_billion" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords maxcut, instance, over, two, billion, variables in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_semidefinite_programs_enormous_range`

- Preferred role: `content`
- Cue keywords: `semidefinite, programs, enormous, range, practical, problems, combinatorial, optimization, neural, network`
- Narration: Semidefinite programs can model an enormous range of practical problems, from combinatorial optimization to neural network verification and control. But solving them at scale is hard.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_semidefinite_programs_enormous_range" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords semidefinite, programs, enormous, range, practical, problems in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_classic_approaches_require_projectin`

- Preferred role: `content`
- Cue keywords: `classic, approaches, require, projecting, onto, semidefinite, cone, which, needs, full`
- Narration: The classic approaches require projecting onto the semidefinite cone, which needs a full eigendecomposition that scales cubically with problem size.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_classic_approaches_require_projectin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords classic, approaches, require, projecting, onto, semidefinite in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_recent_sketching_methods_like_cgal`

- Preferred role: `method`
- Cue keywords: `recent, sketching, methods, like, cgal, avoid, storing, full, matrix, scale`
- Narration: Recent sketching methods, like CGAL, avoid storing the full matrix and scale much further, but they pay for it: as the problem grows they need more and more iterations, so convergence slows down.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_recent_sketching_methods_like_cgal" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords recent, sketching, methods, like, cgal, avoid in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_worse_they_rely_iteration_dependent`

- Preferred role: `content`
- Cue keywords: `worse, they, rely, iteration-dependent, parameter, schedules, prevent, them, reliably, reusing`
- Narration: Worse, they rely on iteration-dependent parameter schedules that prevent them from reliably reusing a previous solution as a warm start, which is exactly what many real applications need.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_worse_they_rely_iteration_dependent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords worse, they, rely, iteration-dependent, parameter, schedules in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_practice_you_rarely_solve_single`

- Preferred role: `content`
- Cue keywords: `practice, you, rarely, solve, single, sdp, isolation, arrives, incrementally, you`
- Narration: In practice, you rarely solve a single SDP in isolation. Data arrives incrementally, or you solve a sequence of tightly-related subproblems inside a mixed-integer or interactive loop.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_practice_you_rarely_solve_single" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords practice, you, rarely, solve, single, sdp in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_all_these_settings_new_problem`

- Preferred role: `content`
- Cue keywords: `all, these, settings, new, problem, nearly, identical, last, being, able`
- Narration: In all these settings, each new problem is nearly identical to the last, so being able to warm-start from the previous solution should give a huge speedup.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_all_these_settings_new_problem" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords all, these, settings, new, problem, nearly in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_spectral_bundle_methods_appealing_fr`

- Preferred role: `method`
- Cue keywords: `spectral, bundle, methods, appealing, framework, they, low, per-iteration, cost, fast`
- Narration: Spectral bundle methods are an appealing framework here: they have low per-iteration cost and fast empirical convergence.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_spectral_bundle_methods_appealing_fr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords spectral, bundle, methods, appealing, framework, they in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_but_previous_spectral_bundle_methods`

- Preferred role: `method`
- Cue keywords: `but, previous, spectral, bundle, methods, handled, either, only, equality, constraints`
- Narration: But previous spectral bundle methods handled either only equality constraints or only inequality constraints, and none had an efficient standalone implementation that could be evaluated on truly massive SDPs.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_but_previous_spectral_bundle_methods" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, previous, spectral, bundle, methods, handled in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_presents_usbs_unified_spectral_bundl`

- Preferred role: `method`
- Cue keywords: `presents, usbs, unified, spectral, bundle, method, sketching, makes, several, contributions`
- Narration: This paper presents USBS, a unified spectral bundle method with sketching. It makes several contributions. First, it handles general SDPs with both equality and inequality constraints, unlike prior spectral bundle methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_presents_usbs_unified_spectral_bundl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords presents, usbs, unified, spectral, bundle, method in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_augmented_optional_matrix_ske`

- Preferred role: `content`
- Cue keywords: `second, augmented, optional, matrix, sketching, technique, dramatically, improves, scalability, while`
- Narration: Second, it can be augmented with an optional matrix sketching technique that dramatically improves scalability while keeping convergence fast. Third, it reliably leverages warm-start initializations.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_second_augmented_optional_matrix_ske" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, augmented, optional, matrix, sketching, technique in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_method_comes_provable_non_asymptotic`

- Preferred role: `method`
- Cue keywords: `method, comes, provable, non-asymptotic, convergence, guarantees, exposes, parameters, let, user`
- Narration: The method comes with provable non-asymptotic convergence guarantees, and it exposes parameters that let the user trade off per-iteration cost against convergence speed.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_method_comes_provable_non_asymptotic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, comes, provable, non-asymptotic, convergence, guarantees in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_finally_authors_release_standalone_i`

- Preferred role: `content`
- Cue keywords: `finally, authors, release, standalone, implementation, pure, jax, runs, efficiently, cpus`
- Narration: Finally, the authors release a standalone implementation in pure JAX that runs efficiently on CPUs, GPUs, and TPUs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_finally_authors_release_standalone_i" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finally, authors, release, standalone, implementation, pure in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_how_usbs_works_starts_dual`

- Preferred role: `method`
- Cue keywords: `how, usbs, works, starts, dual, semidefinite, program, rewrites, single, unconstrained`
- Narration: Here is how USBS works. It starts from the dual semidefinite program and rewrites it as a single unconstrained objective, a penalized dual that combines the largest eigenvalue of C minus A-star y with a linear term and an indicator for the inequality constraints.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_how_usbs_works_starts_dual" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, usbs, works, starts, dual, semidefinite in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_penalized_objective_minimized_proxim`

- Preferred role: `method`
- Cue keywords: `penalized, objective, minimized, proximal, bundle, method, iteration, instead, full, objective`
- Narration: This penalized objective is then minimized with a proximal bundle method. At each iteration, instead of the full objective, USBS builds a cheap lower model over a low-dimensional subspace spanned by the current maximum eigenvectors and a few directions carrying past spectral information.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_penalized_objective_minimized_proxim" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords penalized, objective, minimized, proximal, bundle, method in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_proposes_candidate_iterate_taking_pr`

- Preferred role: `result`
- Cue keywords: `proposes, candidate, iterate, taking, proximal, step, against, solving, small, minimax`
- Narration: It proposes a candidate iterate by taking a proximal step against this model, solving a small minimax problem. If the true objective decreases by at least a fixed fraction of what the model predicted, it accepts the step, a descent step; otherwise it takes a null step but still refines the model.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c3_proposes_candidate_iterate_taking_pr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords proposes, candidate, iterate, taking, proximal, step in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_because_only_small_set_eigenvectors`

- Preferred role: `content`
- Cue keywords: `because, only, small, set, eigenvectors, optionally, low-rank, sketch, primal, matrix`
- Narration: Because only a small set of eigenvectors and, optionally, a low-rank sketch of the primal matrix are ever stored, the whole procedure scales to enormous problems.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_because_only_small_set_eigenvectors" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, only, small, set, eigenvectors, optionally in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_method_tested_across_three_very`

- Preferred role: `method`
- Cue keywords: `method, tested, across, three, very, different, application, areas`
- Narration: The method is tested across three very different application areas.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_method_tested_across_three_very" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, tested, across, three, very, different in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_first_maxcut_ten_graphs_dimacs10`

- Preferred role: `content`
- Cue keywords: `first, maxcut, ten, graphs, dimacs10, collection, ranging, sixteen, thousand, three`
- Narration: The first is MaxCut, using ten graphs from the DIMACS10 collection ranging from sixteen thousand up to three point seven million vertices, the largest yielding more than ten to the thirteenth decision variables.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_first_maxcut_ten_graphs_dimacs10" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, maxcut, ten, graphs, dimacs10, collection in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_second_quadratic_assignment_problem`

- Preferred role: `content`
- Cue keywords: `second, quadratic, assignment, problem, notoriously, hard, combinatorial, problem, instances, qaplib`
- Narration: The second is the quadratic assignment problem, a notoriously hard combinatorial problem, using instances from QAPLIB and TSPLIB with sizes up to one hundred ninety-eight, whose SDP relaxation has on the order of n-to-the-fourth variables, reaching one point five billion.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_second_quadratic_assignment_problem" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, quadratic, assignment, problem, notoriously, hard in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_third_interactive_entity_resolution`

- Preferred role: `method`
- Cue keywords: `third, interactive, entity, resolution, existential, constraints, three, author-coreference, datasets, pubmed`
- Narration: The third is interactive entity resolution using existential constraints, on three author-coreference datasets: PubMed, QIAN, and SCAD-zbMATH. In each case, warm starts are constructed naturally from a slightly smaller, closely related problem.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_third_interactive_entity_resolution" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, interactive, entity, resolution, existential, constraints in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_results_striking`

- Preferred role: `method`
- Cue keywords: `results, striking`
- Narration: The results are striking.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_results_striking" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, striking in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_maxcut_usbs_reaches_accurate_solutio`

- Preferred role: `result`
- Cue keywords: `maxcut, usbs, reaches, accurate, solution, all, ten, instances, twenty-eight, hours`
- Narration: On MaxCut, USBS reaches an accurate solution on all ten instances in twenty-eight hours or less, even without a warm start, while the previous state-of-the-art solver, CGAL, fails to reach an accurate solution on seven of the ten instances within seventy-two hours.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_maxcut_usbs_reaches_accurate_solutio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords maxcut, usbs, reaches, accurate, solution, all in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_instance_over_two_billion_decision`

- Preferred role: `content`
- Cue keywords: `instance, over, two, billion, decision, variables, usbs, five, hundred, times`
- Narration: On an instance with over two billion decision variables, USBS is five hundred times faster than CGAL.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_instance_over_two_billion_decision" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instance, over, two, billion, decision, variables in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_quadratic_assignment_entity_resoluti`

- Preferred role: `result`
- Cue keywords: `quadratic, assignment, entity-resolution, tasks, usbs, reaches, better, relative, gaps, lower`
- Narration: On the quadratic assignment and entity-resolution tasks, USBS reaches better relative gaps and lower cumulative solve times, and the gap in its favor grows as the problems get larger. Across all three settings, USBS reliably takes advantage of warm starts, whereas CGAL often cannot.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c4_quadratic_assignment_entity_resoluti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords quadratic, assignment, entity-resolution, tasks, usbs, reaches in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_two_ablations_especially_informative`

- Preferred role: `content`
- Cue keywords: `two, ablations, especially, informative`
- Narration: Two ablations are especially informative.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_two_ablations_especially_informative" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, ablations, especially, informative in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_first_warm_starting_usbs_initializin`

- Preferred role: `content`
- Cue keywords: `first, warm-starting, usbs, initializing, previous, solution, speed, convergence, more, one`
- Narration: First, warm-starting: for USBS, initializing from the previous solution can speed up convergence by more than one hundred times compared with cold-starting, and, importantly, USBS actually realizes this benefit while CGAL usually cannot.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_first_warm_starting_usbs_initializin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, warm-starting, usbs, initializing, previous, solution in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_second_parameters_number_current_eig`

- Preferred role: `method`
- Cue keywords: `second, parameters, number, current, eigenvectors, matters, lot, larger, values, give`
- Narration: Second, the model parameters: the number of current eigenvectors, kc, matters a lot, and larger values give better convergence in general. This contrasts with the original spectral bundle method, which fixed kc to one.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_second_parameters_number_current_eig" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, parameters, number, current, eigenvectors, matters in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_number_past_spectral_vectors_turns`

- Preferred role: `content`
- Cue keywords: `number, past, spectral, vectors, turns, out, much, less, helpful, sometimes`
- Narration: The number of past spectral vectors, kp, turns out to be much less helpful and can sometimes even harm convergence, so the recommended settings keep kc large and kp small.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_number_past_spectral_vectors_turns" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords number, past, spectral, vectors, turns, out in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_summarize_numbers_matter_most_five_h`

- Preferred role: `content`
- Cue keywords: `summarize, numbers, matter, most, five-hundred-times, speedup, over, previous, state, art`
- Narration: To summarize the numbers that matter most: a five-hundred-times speedup over the previous state of the art on a problem with more than two billion decision variables; more than a one-hundred-times convergence speedup just from warm-starting; ten out of ten MaxCut instances solved by USBS in twenty-eight hours or less, versus only three out of ten for CGAL even given seventy-two hours.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_summarize_numbers_matter_most_five_h" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords summarize, numbers, matter, most, five-hundred-times, speedup in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_usbs_scales_problems_over_ten_to_the`

- Preferred role: `content`
- Cue keywords: `usbs, scales, problems, over, ten-to-the-thirteenth, decision, variables, solves, quadratic-assignment, relaxations`
- Narration: USBS scales to problems with over ten-to-the-thirteenth decision variables and solves quadratic-assignment relaxations with one point five billion variables.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_usbs_scales_problems_over_ten_to_the" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords usbs, scales, problems, over, ten-to-the-thirteenth, decision in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple`
- Narration: The takeaway is simple.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_usbs_shows_large_scale_semidefinite`

- Preferred role: `method`
- Cue keywords: `usbs, shows, large-scale, semidefinite, programming, does, not, slow, restricted, narrow`
- Narration: USBS shows that large-scale semidefinite programming does not have to be slow or restricted to a narrow class of problems.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_usbs_shows_large_scale_semidefinite" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords usbs, shows, large-scale, semidefinite, programming, does in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_unifying_equality_inequality_constra`

- Preferred role: `method`
- Cue keywords: `unifying, equality, inequality, constraints, single, spectral, bundle, method, adding, optional`
- Narration: By unifying equality and inequality constraints in a single spectral bundle method, adding optional sketching for scalability, and making warm-starting actually work, it turns SDPs that were previously considered intractable into a practical tool, complete with an open, hardware-flexible JAX implementation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_unifying_equality_inequality_constra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unifying, equality, inequality, constraints, single, spectral in title/desc so the matcher can verify semantic overlap.
