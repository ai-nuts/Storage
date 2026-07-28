# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_asks_fundamental_question_learning_t`

- Preferred role: `result`
- Cue keywords: `asks, fundamental, question, learning, theory, how, well, does, plain, logistic`
- Narration: This paper asks a fundamental question in learning theory: how well does plain logistic regression solve the problem of agnostically learning halfspaces? A halfspace is a linear classifier, and in the agnostic setting an adversary corrupts an OPT fraction of the labels, so the best any linear classifier can do is a zero-one error of OPT.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c1_asks_fundamental_question_learning_t" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords asks, fundamental, question, learning, theory, how in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_prior_work_left_wide_gap`

- Preferred role: `content`
- Cue keywords: `prior, work, left, wide, gap, lower, bound, saying, convex, surrogate`
- Narration: Prior work left a wide gap: a lower bound saying no convex surrogate can beat order OPT, and an upper bound showing logistic regression achieves only order square-root of OPT.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_prior_work_left_wide_gap" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, work, left, wide, gap, lower in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_authors_close_gap_they_construct`

- Preferred role: `method`
- Cue keywords: `authors, close, gap, they, construct, well-behaved, distribution, which, global, minimizer`
- Narration: The authors close this gap. They construct a well-behaved distribution on which the global minimizer of the logistic risk provably suffers square-root OPT error, matching the known upper bound exactly. They then show that adding a natural radial-Lipschitzness assumption lets logistic regression reach near-optimal order-OPT error.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_authors_close_gap_they_construct" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, close, gap, they, construct, well-behaved in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_finally_they_give_strikingly_simple`

- Preferred role: `method`
- Cue keywords: `finally, they, give, strikingly, simple, two-phase, algorithm, logistic, regression, followed`
- Narration: Finally, they give a strikingly simple two-phase algorithm, logistic regression followed by a perceptron step, that attains near-optimal error for any well-behaved distribution, replacing the many rounds of optimization that prior methods required.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_finally_they_give_strikingly_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finally, they, give, strikingly, simple, two-phase in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_studies_agnostic_learning_homogeneou`

- Preferred role: `guidance`
- Cue keywords: `studies, agnostic, learning, homogeneous, halfspaces, one, most, fundamental, problems, machine`
- Narration: The paper studies the agnostic learning of homogeneous halfspaces, one of the most fundamental problems in machine learning.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s02_c1_studies_agnostic_learning_homogeneou" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords studies, agnostic, learning, homogeneous, halfspaces, one in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_given_samples_unknown_distribution_o`

- Preferred role: `method`
- Cue keywords: `given, samples, unknown, distribution, over, feature-label, pairs, want, linear, classifier`
- Narration: We are given samples from an unknown distribution over feature-label pairs, and we want a linear classifier whose zero-one error is close to OPT, the best error achievable by any homogeneous halfspace.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_given_samples_unknown_distribution_o" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords given, samples, unknown, distribution, over, feature-label in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_equivalently_adversary_allowed_flip`

- Preferred role: `content`
- Cue keywords: `equivalently, adversary, allowed, flip, opt, fraction, labels, otherwise, perfectly, linearly`
- Narration: Equivalently, an adversary is allowed to flip an OPT fraction of the labels of an otherwise perfectly linearly separable dataset. Logistic regression is the natural, ubiquitous heuristic here, yet its theoretical guarantees for this problem were poorly understood.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_equivalently_adversary_allowed_flip" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords equivalently, adversary, allowed, flip, opt, fraction in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_prior_results_left_frustrating_gap`

- Preferred role: `method`
- Cue keywords: `prior, results, left, frustrating, gap, lower, bound, saying, convex, surrogate`
- Narration: Prior results left a frustrating gap: a lower bound saying no convex surrogate loss can beat order OPT error, against an upper bound showing logistic regression reaches only order square-root of OPT. The central question is which of these bounds reflects the truth for logistic regression.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_prior_results_left_frustrating_gap" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, results, left, frustrating, gap, lower in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_logistic_regression_arguably_most_wi`

- Preferred role: `result`
- Cue keywords: `logistic, regression, arguably, most, widely, deployed, classification, algorithm, understanding, its`
- Narration: Logistic regression is arguably the most widely deployed classification algorithm, so understanding its statistical guarantees is not merely academic.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c1_logistic_regression_arguably_most_wi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords logistic, regression, arguably, most, widely, deployed in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_worry_logistic_regression_behave_ter`

- Preferred role: `method`
- Cue keywords: `worry, logistic, regression, behave, terribly, worst, case, earlier, work, showed`
- Narration: The worry is that logistic regression can behave terribly in the worst case; earlier work showed its risk minimizer can be wrong on nearly a one-minus-OPT fraction of examples on an adversarially built distribution.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_worry_logistic_regression_behave_ter" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords worry, logistic, regression, behave, terribly, worst in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_rule_out_such_pathologies_community`

- Preferred role: `method`
- Cue keywords: `rule, out, such, pathologies, community, focuses, well-behaved, distributions, such, isotropic`
- Narration: To rule out such pathologies, the community focuses on well-behaved distributions, such as isotropic log-concave ones, where much stronger guarantees are possible. But even under these assumptions the precise error rate of logistic regression was unknown, sitting somewhere between order OPT and order square-root OPT.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_rule_out_such_pathologies_community" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rule, out, such, pathologies, community, focuses in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_pinning_down_rate_tells_whether`

- Preferred role: `result`
- Cue keywords: `pinning, down, rate, tells, whether, logistic, regression, near-optimal, agnostic, learner`
- Narration: Pinning down this rate tells us whether logistic regression is a near-optimal agnostic learner or whether it fundamentally leaves accuracy on the table, and if so, what minimal fix recovers optimality.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c4_pinning_down_rate_tells_whether" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pinning, down, rate, tells, whether, logistic in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_contributions_together_r`

- Preferred role: `method`
- Cue keywords: `makes, three, contributions, together, resolve, gap, first, constructs, explicit, two-dimensional`
- Narration: The paper makes three contributions that together resolve the gap. First, it constructs an explicit two-dimensional, isotropic, well-behaved distribution on which the global minimizer of the logistic risk provably attains square-root OPT zero-one error, matching the known upper bound and proving that logistic regression alone cannot do better.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_makes_three_contributions_together_r" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, contributions, together, resolve, gap in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_identifies_clean_sufficient_c`

- Preferred role: `content`
- Cue keywords: `second, identifies, clean, sufficient, condition, radial, lipschitzness, density, under, which`
- Narration: Second, it identifies a clean sufficient condition, radial Lipschitzness of the density, under which logistic regression does reach the near-optimal order-OPT rate.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_second_identifies_clean_sufficient_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, identifies, clean, sufficient, condition, radial in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_most_usefully_introduces_simpl`

- Preferred role: `method`
- Cue keywords: `third, most, usefully, introduces, simple, two-phase, algorithm, run, logistic, regression`
- Narration: Third, and most usefully, it introduces a simple two-phase algorithm: run logistic regression, then run a perceptron-style hinge-loss step from that warm start on a restricted domain.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_third_most_usefully_introduces_simpl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, most, usefully, introduces, simple, two-phase in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_attains_near_optimal_error_every_wel`

- Preferred role: `method`
- Cue keywords: `attains, near-optimal, error, every, well-behaved, distribution, without, radial-lipschitz, assumption, cost`
- Narration: This attains near-optimal error for every well-behaved distribution without the radial-Lipschitz assumption, at the cost of just one additional convex optimization, and it is far simpler than prior algorithms that required solving a logarithmic number of minimization problems.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_attains_near_optimal_error_every_wel" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords attains, near-optimal, error, every, well-behaved, distribution in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_technical_core_rests_two_convex`

- Preferred role: `result`
- Cue keywords: `technical, core, rests, two, convex, surrogate, losses, logistic, loss, log`
- Narration: The technical core rests on two convex surrogate losses. The logistic loss is the log of one plus e to the minus margin, and the hinge loss is the positive part of the negative margin; both are minimized as empirical averages over the samples.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c1_technical_core_rests_two_convex" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords technical, core, rests, two, convex, surrogate in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_lower_bound_authors_hand_design_dist`

- Preferred role: `method`
- Cue keywords: `lower, bound, authors, hand-design, distribution, plane, four, parts, construction, valid`
- Narration: For the lower bound, the authors hand-design a distribution Q on the plane with four parts, a construction valid when OPT is at most one over sixteen, engineered so that the true optimal halfspace is only wrong on a small noisy region, yet the logistic risk minimizer is pulled into a direction that misclassifies a square-root OPT fraction.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_lower_bound_authors_hand_design_dist" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lower, bound, authors, hand-design, distribution, plane in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_upper_bound_algorithm_key_object`

- Preferred role: `content`
- Cue keywords: `upper, bound, algorithm, key, object, angle, between, learned, direction, ground-truth`
- Narration: For the upper bound and the algorithm, the key object is the angle between the learned direction and the ground-truth direction. Phase one runs projected gradient descent on the logistic risk inside a ball of radius one over square-root epsilon, which under well-behaved-ness returns a direction within angle order square-root OPT of the truth.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_upper_bound_algorithm_key_object" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords upper, bound, algorithm, key, object, angle in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_phase_two_runs_projected_stochastic`

- Preferred role: `method`
- Cue keywords: `phase, two, runs, projected, stochastic, gradient, descent, hinge, loss, which`
- Narration: Phase two then runs projected stochastic gradient descent on the hinge loss, which is exactly the classical perceptron update, starting from that warm start and confined to a restricted domain. This second convex step sharpens the angle and drives the zero-one error down to near order OPT.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_phase_two_runs_projected_stochastic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords phase, two, runs, projected, stochastic, gradient in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_because_learning_theory_benchmark_da`

- Preferred role: `method`
- Cue keywords: `because, learning-theory, benchmark, datasets, empirical, tables, distribution, classes, results, theorems`
- Narration: Because this is a learning-theory paper, there are no benchmark datasets or empirical tables; the "data" are distribution classes and the results are theorems with explicit constants.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_because_learning_theory_benchmark_da" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, learning-theory, benchmark, datasets, empirical, tables in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_positive_results_hold_standard_famil`

- Preferred role: `method`
- Cue keywords: `positive, results, hold, standard, family, well-behaved, distributions, used, prior, work`
- Narration: The positive results hold for the standard family of well-behaved distributions used in prior work, meaning the marginal on features is isotropic and satisfies soft-margin and sub-exponential regularity conditions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_positive_results_hold_standard_famil" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords positive, results, hold, standard, family, well-behaved in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_negative_result_carried_concrete_cou`

- Preferred role: `method`
- Cue keywords: `negative, result, carried, concrete, counterexample, explicit, distribution, two-dimensional, plane, built`
- Narration: The negative result is carried by a concrete counterexample: an explicit distribution Q on the two-dimensional plane, built from four parts and illustrated in the paper's single figure, that is fully well-behaved yet defeats logistic regression.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_negative_result_carried_concrete_cou" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords negative, result, carried, concrete, counterexample, explicit in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_upper_bounds_stated_two_regimes`

- Preferred role: `method`
- Cue keywords: `upper, bounds, stated, two, regimes, one, bounded, feature, distributions, where`
- Narration: The upper bounds are stated in two regimes, one for bounded feature distributions where the norm is at most B, and one for sub-exponential feature distributions, so the guarantees span the settings that matter for isotropic log-concave data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_upper_bounds_stated_two_regimes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords upper, bounds, stated, two, regimes, one in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_finding_matching_pair_bound`

- Preferred role: `content`
- Cue keywords: `headline, finding, matching, pair, bounds`
- Narration: The headline finding is a matching pair of bounds.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_headline_finding_matching_pair_bound" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, finding, matching, pair, bounds in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_constructed_well_behaved_distributio`

- Preferred role: `method`
- Cue keywords: `constructed, well-behaved, distribution, global, minimizer, population, logistic, risk, zero-one, error`
- Narration: On the constructed well-behaved distribution, the global minimizer of the population logistic risk has zero-one error at least square-root OPT divided by sixty pi, which asymptotically matches the best known upper bound and therefore proves that square-root OPT is the true rate for logistic regression alone.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_constructed_well_behaved_distributio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords constructed, well-behaved, distribution, global, minimizer, population in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_sense_which_closes_long_standing_gap`

- Preferred role: `result`
- Cue keywords: `sense, which, closes, long-standing, gap, adding, radial, lipschitzness, density, same`
- Narration: That is the sense in which the paper closes the long-standing gap. Then, by adding radial Lipschitzness of the density, the same logistic minimizer jumps to near-optimal error of order OPT, up to a constant Cκ that is bounded whenever the density is Lipschitz.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_sense_which_closes_long_standing_gap" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sense, which, closes, long-standing, gap, adding in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_without_any_such_assumption_two_phas`

- Preferred role: `method`
- Cue keywords: `without, any, such, assumption, two-phase, algorithm, achieves, order, opt, plus`
- Narration: And without any such assumption, the two-phase algorithm achieves order OPT plus epsilon error for bounded distributions and order OPT times log one over OPT for sub-exponential ones, in expectation over the run.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_without_any_such_assumption_two_phas" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords without, any, such, assumption, two-phase, algorithm in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_although_theory_without_experimental`

- Preferred role: `method`
- Cue keywords: `although, theory, without, experimental, ablations, analysis, structured, expose, which, assumptions`
- Narration: Although this is a theory paper without experimental ablations, the analysis is structured to expose which assumptions buy which guarantees, playing the role an ablation would.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_although_theory_without_experimental" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords although, theory, without, experimental, ablations, analysis in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_single_upper_bound_argument_versatil`

- Preferred role: `method`
- Cue keywords: `single, upper-bound, argument, versatile, enough, recover, earlier, square-root, opt, rate`
- Narration: The single upper-bound argument is versatile enough to recover the earlier square-root OPT rate for general well-behaved distributions as a special case, and crucially it also goes through for the hinge loss, not just the logistic loss; this dual applicability is what enables the perceptron second phase.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_single_upper_bound_argument_versatil" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords single, upper-bound, argument, versatile, enough, recover in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_theorem_cleanly_separates_bounded_su`

- Preferred role: `content`
- Cue keywords: `theorem, cleanly, separates, bounded, sub-exponential, regimes, showing, only, price, moving`
- Narration: The theorem cleanly separates the bounded and sub-exponential regimes, showing that the only price of moving from bounded to heavier sub-exponential tails is an extra logarithmic factor in one over OPT.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_theorem_cleanly_separates_bounded_su" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords theorem, cleanly, separates, bounded, sub-exponential, regimes in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_likewise_constant_integral_radial_li`

- Preferred role: `content`
- Cue keywords: `likewise, constant, integral, radial-lipschitzness, modulus, isolates, exactly, how, much, density`
- Narration: Likewise, the constant Cκ, an integral of the radial-Lipschitzness modulus, isolates exactly how much the density's radial smoothness matters, vanishing when the density is radially symmetric.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_likewise_constant_integral_radial_li" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords likewise, constant, integral, radial-lipschitzness, modulus, isolates in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact_lower`

- Preferred role: `result`
- Cue keywords: `few, numbers, capture, impact, lower, bound, gives, zero-one, error, least`
- Narration: A few numbers capture the impact. The lower bound gives a zero-one error of at least square-root OPT over sixty pi for the logistic minimizer, valid whenever OPT is at most one one-hundredth.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact_lower" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact, lower, bound in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_under_radial_lipschitzness_logistic`

- Preferred role: `method`
- Cue keywords: `under, radial, lipschitzness, logistic, regression, reaches, near-optimal, order-opt, error, two-phase`
- Narration: Under radial Lipschitzness, logistic regression reaches near-optimal order-OPT error. The two-phase algorithm achieves order OPT plus epsilon error for bounded distributions and order OPT times log one over OPT for sub-exponential ones.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_under_radial_lipschitzness_logistic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords under, radial, lipschitzness, logistic, regression, reaches in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_does_sample_complexity_order_over`

- Preferred role: `method`
- Cue keywords: `does, sample, complexity, order, over, epsilon, squared, quadratic, improvement, over`
- Narration: It does so with a sample complexity of order d over epsilon squared, a quadratic improvement over the d over epsilon to the fourth required by prior nonconvex methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_does_sample_complexity_order_over" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords does, sample, complexity, order, over, epsilon in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_structurally_whereas_earlier_algorit`

- Preferred role: `method`
- Cue keywords: `structurally, whereas, earlier, algorithms, hit, order, opt, error, had, solve`
- Narration: And structurally, whereas earlier algorithms that hit order OPT error had to solve a logarithmic number of minimization problems while guessing OPT by binary search, this method needs only two convex steps.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_structurally_whereas_earlier_algorit" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords structurally, whereas, earlier, algorithms, hit, order in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_message_twofold_first_logist`

- Preferred role: `method`
- Cue keywords: `lasting, message, twofold, first, logistic, regression, itself, cannot, beat, square-root`
- Narration: The lasting message is twofold. First, logistic regression by itself cannot beat square-root OPT error for agnostically learning halfspaces, and the paper proves this rate is exactly tight by constructing a distribution that forces it.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_lasting_message_twofold_first_logist" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, twofold, first, logistic, regression in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_second_fix_remarkably_cheap_appendin`

- Preferred role: `method`
- Cue keywords: `second, fix, remarkably, cheap, appending, one, perceptron-style, convex, minimization, warm-started`
- Narration: Second, the fix is remarkably cheap: appending one perceptron-style convex minimization, warm-started from the logistic solution and confined to a bounded domain, provably boosts the guarantee to near-optimal order-OPT error for every well-behaved distribution.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_second_fix_remarkably_cheap_appendin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, fix, remarkably, cheap, appending, one in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_along_way_also_identifies_radial`

- Preferred role: `content`
- Cue keywords: `along, way, also, identifies, radial, lipschitzness, feature, density, natural, condition`
- Narration: Along the way the paper also identifies radial Lipschitzness of the feature density as the natural condition under which logistic regression alone already succeeds.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_along_way_also_identifies_radial" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords along, way, also, identifies, radial, lipschitzness in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_short_passerby_remember_logistic_reg`

- Preferred role: `method`
- Cue keywords: `short, passerby, remember, logistic, regression, half, answer, single, extra, convex`
- Narration: In short, a passerby can remember that logistic regression is half the answer, and a single extra convex step completes it, more simply and with better sample complexity than any prior method.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c4_short_passerby_remember_logistic_reg" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords short, passerby, remember, logistic, regression, half in title/desc so the matcher can verify semantic overlap.
