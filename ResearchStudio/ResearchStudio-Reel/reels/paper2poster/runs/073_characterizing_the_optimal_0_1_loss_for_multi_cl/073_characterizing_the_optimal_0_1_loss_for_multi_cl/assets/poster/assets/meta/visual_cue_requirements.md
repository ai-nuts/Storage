# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_how_robust_any_classifier_possibly`

- Preferred role: `result`
- Cue keywords: `how, robust, any, classifier, possibly, against, adversary, perturbs, inputs, test`
- Narration: How robust can any classifier possibly be against an adversary that perturbs inputs at test time? This paper answers that question for the multi-class setting.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c1_how_robust_any_classifier_possibly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, robust, any, classifier, possibly, against in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_authors_derive_achievable_informatio`

- Preferred role: `figure`
- Cue keywords: `authors, derive, achievable, information-theoretic, lower, bounds, 0, 1, loss, best`
- Narration: The authors derive achievable information-theoretic lower bounds on the 0-1 loss of the best possible classifier under a test-time attacker, for any discrete dataset.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c2_authors_derive_achievable_informatio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, derive, achievable, information-theoretic, lower, bounds in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_their_framework_builds_conflict_hype`

- Preferred role: `method`
- Cue keywords: `their, framework, builds, conflict, hypergraph, attacker, constraints, solves, linear, program`
- Narration: Their framework builds a conflict hypergraph from the data and the attacker's constraints, then solves a linear program whose optimum is the lowest loss any classifier can attain.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_their_framework_builds_conflict_hype" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords their, framework, builds, conflict, hypergraph, attacker in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_because_exact_problem_often_too`

- Preferred role: `method`
- Cue keywords: `because, exact, problem, often, too, large, solve, they, introduce, efficient`
- Narration: Because the exact problem is often too large to solve, they introduce efficient bounds that pin down the range of the optimal loss, and use them to reveal a striking gap between today's adversarially trained models and what is theoretically achievable.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_because_exact_problem_often_too" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, exact, problem, often, too, large in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_determining_whether_classifier_truly`

- Preferred role: `content`
- Cue keywords: `determining, whether, classifier, truly, robust, adversarial, examples, requires, knowing, best`
- Narration: Determining whether a classifier is truly robust to adversarial examples requires knowing the best that is even possible.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_determining_whether_classifier_truly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords determining, whether, classifier, truly, robust, adversarial in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_binary_classification_prior_work_cha`

- Preferred role: `result`
- Cue keywords: `binary, classification, prior, work, characterized, optimal, robust, loss, giving, reference`
- Narration: For binary classification, prior work characterized this optimal robust loss, giving a reference point to measure progress against.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c2_binary_classification_prior_work_cha" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords binary, classification, prior, work, characterized, optimal in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_but_real_problems_many_classes`

- Preferred role: `content`
- Cue keywords: `but, real, problems, many, classes, multi-class, case, left, open`
- Narration: But real problems have many classes, and the multi-class case was left open.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_but_real_problems_many_classes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, real, problems, many, classes, multi-class in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_way_compute_lowest_0_1`

- Preferred role: `result`
- Cue keywords: `way, compute, lowest, 0, 1, loss, achievable, any, classifier, against`
- Narration: There was no way to compute the lowest 0-1 loss achievable by any classifier against a test-time attacker on a multi-class dataset, so practitioners had no way to know how far current defenses sit from the theoretical limit.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c4_way_compute_lowest_0_1" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords way, compute, lowest, 0, 1, loss in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_comparing_robustness_best_possible_c`

- Preferred role: `method`
- Cue keywords: `comparing, robustness, best, possible, classifier, what, state-of-the-art, achieves, powerful, diagnostic`
- Narration: Comparing the robustness of the best possible classifier to what state-of-the-art training achieves is a powerful diagnostic.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_comparing_robustness_best_possible_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords comparing, robustness, best, possible, classifier, what in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_tells_you_whether_bottleneck_your`

- Preferred role: `method`
- Cue keywords: `tells, you, whether, bottleneck, your, method, fundamental, limit, threat`
- Narration: It tells you whether the bottleneck is your training method or a fundamental limit of the data and threat model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_tells_you_whether_bottleneck_your" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tells, you, whether, bottleneck, your, method in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_past_work_delivered_only_two`

- Preferred role: `content`
- Cue keywords: `past, work, delivered, only, two, classes`
- Narration: Past work delivered this only for two classes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_past_work_delivered_only_two" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords past, work, delivered, only, two, classes in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_moving_many_classes_not_trivial`

- Preferred role: `figure`
- Cue keywords: `moving, many, classes, not, trivial, extension, three, more, classes, examples`
- Narration: Moving to many classes is not a trivial extension: with three or more classes, examples can interact in higher-order ways that binary analysis simply cannot capture, and these interactions can change what optimal robustness looks like.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s03_c4_moving_many_classes_not_trivial" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords moving, many, classes, not, trivial, extension in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, contributions`
- Narration: The paper makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_generalizes_conflict_graph_fra`

- Preferred role: `result`
- Cue keywords: `first, generalizes, conflict-graph, framework, binary, multi-class, classification, showing, optimal, 0`
- Narration: First, it generalizes the conflict-graph framework from binary to multi-class classification, showing the optimal 0-1 loss is the solution of a linear program built on a conflict hypergraph.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c2_first_generalizes_conflict_graph_fra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, generalizes, conflict-graph, framework, binary, multi-class in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_because_exact_program_become`

- Preferred role: `figure`
- Cue keywords: `second, because, exact, program, become, computationally, prohibitive, develops, several, more`
- Narration: Second, because that exact program can become computationally prohibitive, it develops several more efficient bounds, both lower and upper, that bracket the range in which the true optimal loss must lie.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c3_second_because_exact_program_become" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, because, exact, program, become, computationally in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_delivers_extensive_empirical_s`

- Preferred role: `result`
- Cue keywords: `third, delivers, extensive, empirical, study, giving, first, analysis, gap, optimal`
- Narration: Third, it delivers an extensive empirical study, giving the first analysis of the gap to optimal robustness for classifiers in the multi-class setting on benchmark datasets.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c4_third_delivers_extensive_empirical_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, delivers, extensive, empirical, study, giving in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_core_idea_represent_classification_p`

- Preferred role: `result`
- Cue keywords: `core, idea, represent, classification, problem, conflict, hypergraph`
- Narration: The core idea is to represent the classification problem as a conflict hypergraph.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c1_core_idea_represent_classification_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, idea, represent, classification, problem, conflict in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_vertex_point_set_points_forms`

- Preferred role: `content`
- Cue keywords: `vertex, point, set, points, forms, hyperedge, when, they, belong, different`
- Narration: Each vertex is a data point, and a set of points forms a hyperedge when they belong to different classes yet share overlapping adversarial neighborhoods, meaning an attacker could push any of them to the same confusing input.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_vertex_point_set_points_forms" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords vertex, point, set, points, forms, hyperedge in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_optimal_0_1_loss_becomes`

- Preferred role: `method`
- Cue keywords: `optimal, 0, 1, loss, becomes, linear, program, maximize, probability, mass`
- Narration: The optimal 0-1 loss then becomes a linear program: maximize the probability mass of correctly classified points subject to constraints encoded by the hypergraph's incidence matrix. The dual program is a fractional covering of vertices by hyperedges, and it directly yields the optimal adversarial strategy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_optimal_0_1_loss_becomes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords optimal, 0, 1, loss, becomes, linear in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_because_computing_all_hyperedges_deg`

- Preferred role: `figure`
- Cue keywords: `because, computing, all, hyperedges, degree, ten, infeasible, authors, truncate, hypergraph`
- Narration: Because computing all hyperedges up to degree ten is infeasible, the authors truncate the hypergraph to lower degrees for tractable lower bounds, aggregate binary one-versus-one losses for an even cheaper bound, and apply a generalized Caro-Wei bound for a matching upper bound.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c4_because_computing_all_hyperedges_deg" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, computing, all, hyperedges, degree, ten in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_two_standard_vision_benc`

- Preferred role: `method`
- Cue keywords: `experiments, two, standard, vision, benchmarks, mnist, cifar-10, under, l-two, constrained`
- Narration: The experiments use two standard vision benchmarks, MNIST and CIFAR-10, under an L-two constrained attacker evaluated across a sweep of perturbation budgets.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_experiments_two_standard_vision_benc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, two, standard, vision, benchmarks, mnist in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_3_class_studies_they_take`

- Preferred role: `result`
- Cue keywords: `3, class, studies, they, take, one, thousand, samples, per, class`
- Narration: For the 3-class studies they take one thousand samples per class, using digits one, four, and seven for MNIST and the plane, bird, and ship classes for CIFAR-10.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_3_class_studies_they_take" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords 3, class, studies, they, take, one in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_they_also_compute_bounds_full`

- Preferred role: `method`
- Cue keywords: `they, also, compute, bounds, full, 10, class, problem, complete, sets`
- Narration: They also compute bounds for the full 10-class problem on the complete training sets.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_they_also_compute_bounds_full" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, also, compute, bounds, full, 10 in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_reference_defenses_they_train_classi`

- Preferred role: `method`
- Cue keywords: `reference, defenses, they, train, classifiers, trades, adversarial, small, convolutional, network`
- Narration: As reference defenses, they train classifiers with TRADES adversarial training, a small convolutional network for MNIST and a wide residual network for CIFAR-10, and evaluate them with the strong APGD attack from AutoAttack.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_reference_defenses_they_train_classi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reference, defenses, they, train, classifiers, trades in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_finding_large_previously_un`

- Preferred role: `method`
- Cue keywords: `headline, finding, large, previously, unquantified, gap, adversarially, trained, classifiers, perform`
- Narration: The headline finding is a large, previously unquantified gap. Adversarially trained classifiers perform far worse than the theoretical optimum, and this gap is much wider than what prior work observed for binary classification.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_headline_finding_large_previously_un" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, finding, large, previously, unquantified, gap in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_3_class_cifar_10_trades_adversarial`

- Preferred role: `method`
- Cue keywords: `3, class, cifar-10, trades, adversarial, cannot, achieve, loss, much, better`
- Narration: On 3-class CIFAR-10, TRADES adversarial training cannot achieve a loss much better than 0.6 at a perturbation strength where the optimal achievable loss is essentially zero.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_3_class_cifar_10_trades_adversarial" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords 3, class, cifar-10, trades, adversarial, cannot in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_10_class_setting_efficient_lower`

- Preferred role: `figure`
- Cue keywords: `10, class, setting, efficient, lower, upper, bounds, sandwich, optimal, loss`
- Narration: In the 10-class setting, the efficient lower and upper bounds sandwich the optimal loss tightly for the budgets used in practice, so the gap is not an artifact of loose bounds.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s07_c3_10_class_setting_efficient_lower" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords 10, class, setting, efficient, lower, upper in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_suggests_current_robust_struggles_fa`

- Preferred role: `method`
- Cue keywords: `suggests, current, robust, struggles, far, more, number, classes, grows`
- Narration: This suggests current robust training struggles far more as the number of classes grows.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_suggests_current_robust_struggles_fa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords suggests, current, robust, struggles, far, more in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_key_ablation_examines_how_much`

- Preferred role: `content`
- Cue keywords: `key, ablation, examines, how, much, higher-order, hyperedges, actually, matter`
- Narration: A key ablation examines how much the higher-order hyperedges actually matter.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_key_ablation_examines_how_much" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, ablation, examines, how, much, higher-order in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_surprisingly_small_perturbation_budg`

- Preferred role: `method`
- Cue keywords: `surprisingly, small, perturbation, budgets, lower, bound, computed, only, edges, nearly`
- Narration: Surprisingly, at small perturbation budgets the lower bound computed with only edges is nearly identical to bounds that add degree-three and degree-four hyperedges, even though the graph contains millions of these higher-order structures.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_surprisingly_small_perturbation_budg" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords surprisingly, small, perturbation, budgets, lower, bound in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_cifar_10_budget_three_roughly_three`

- Preferred role: `result`
- Cue keywords: `cifar-10, budget, three, roughly, three, million, degree-three, ten, million, degree-four`
- Narration: For CIFAR-10 at budget three, there are roughly three million degree-three and ten million degree-four hyperedges, yet they have no impact on the computed bound.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c3_cifar_10_budget_three_roughly_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-10, budget, three, roughly, three, million in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_means_edge_only_bounds_both_cheap`

- Preferred role: `result`
- Cue keywords: `means, edge-only, bounds, both, cheap, accurate, practical, regime, aggregated, binary`
- Narration: This means edge-only bounds are both cheap and accurate in the practical regime. The aggregated binary bound is the fastest to compute but much looser, and scaling up model architecture yields only minor gains at low budgets.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_means_edge_only_bounds_both_cheap" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords means, edge-only, bounds, both, cheap, accurate in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_numbers_make_gap_concrete_3`

- Preferred role: `method`
- Cue keywords: `numbers, make, gap, concrete, 3, class, cifar-10, adversarial, plateaus, near`
- Narration: The numbers make the gap concrete. On 3-class CIFAR-10, adversarial training plateaus near 0.6 loss at a budget where the optimal loss is essentially zero.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_numbers_make_gap_concrete_3" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords numbers, make, gap, concrete, 3, class in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_state_of_the_art_certifiably_robust`

- Preferred role: `result`
- Cue keywords: `state-of-the-art, certifiably, robust, models, fare, better, against, optimum, best, mnist`
- Narration: State-of-the-art certifiably robust models fare no better against the optimum: the best MNIST model has 0-1 loss of 0.27 at budget one-point-five-two and 0.44 at budget two, while the achievable optimal lower bound is zero in both cases.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_state_of_the_art_certifiably_robust" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords state-of-the-art, certifiably, robust, models, fare, better in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_cifar_10_best_certified_reaches_0_6`

- Preferred role: `result`
- Cue keywords: `cifar-10, best, certified, reaches, 0.6, loss, budget, one, 0.8, budget`
- Narration: On CIFAR-10, the best certified model reaches 0.6 loss at budget one and 0.8 at budget two, again against an optimal lower bound of zero.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_cifar_10_best_certified_reaches_0_6" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-10, best, certified, reaches, 0.6, loss in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_structural_side_millions_higher_degr`

- Preferred role: `method`
- Cue keywords: `structural, side, millions, higher-degree, hyperedges, three, million, degree, three, ten`
- Narration: And on the structural side, millions of higher-degree hyperedges, three million of degree three and ten million of degree four at budget three, leave the bound completely unchanged.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_structural_side_millions_higher_degr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords structural, side, millions, higher-degree, hyperedges, three in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_multi_class_robust_classifi`

- Preferred role: `result`
- Cue keywords: `takeaway, multi-class, robust, classification, large, now-measurable, gap, between, what, current`
- Narration: The takeaway is that multi-class robust classification has a large and now-measurable gap between what current defenses achieve and what is theoretically possible, a gap that is far worse than in the binary case.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c1_takeaway_multi_class_robust_classifi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, multi-class, robust, classification, large, now-measurable in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_conflict_hypergraph_framework_comput`

- Preferred role: `figure`
- Cue keywords: `conflict-hypergraph, framework, computes, optimal, 0, 1, loss, linear, program, its`
- Narration: The paper's conflict-hypergraph framework computes the optimal 0-1 loss as a linear program, and its efficient truncated bounds pin that optimum down tightly using only edges in the practical low-budget regime.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s10_c2_conflict_hypergraph_framework_comput" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords conflict-hypergraph, framework, computes, optimal, 0, 1 in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_gives_practitioners_fast_diagnostic`

- Preferred role: `takeaway`
- Cue keywords: `gives, practitioners, fast, diagnostic, tool, see, how, much, robustness, still`
- Narration: This gives practitioners a fast diagnostic tool to see how much robustness is still on the table, and it points future research toward closing the gap rather than endlessly iterating attacks and defenses.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c3_gives_practitioners_fast_diagnostic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gives, practitioners, fast, diagnostic, tool, see in title/desc so the matcher can verify semantic overlap.
