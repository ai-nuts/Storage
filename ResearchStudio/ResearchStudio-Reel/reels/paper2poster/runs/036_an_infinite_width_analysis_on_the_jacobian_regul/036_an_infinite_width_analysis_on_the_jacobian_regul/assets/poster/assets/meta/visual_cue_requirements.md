# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_infinite_width_theory_built_tools_li`

- Preferred role: `method`
- Cue keywords: `infinite-width, theory, built, tools, like, neural, tangent, kernel, transformed, how`
- Narration: Infinite-width theory, built on tools like the Neural Tangent Kernel, has transformed how we understand deep network initialisation and training, but it has only ever described a network's output.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_infinite_width_theory_built_tools_li" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords infinite-width, theory, built, tools, like, neural in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_extends_theory_network_input_output`

- Preferred role: `content`
- Cue keywords: `extends, theory, network, input-output, jacobian`
- Narration: This paper extends that theory to the network's input-output Jacobian.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_extends_theory_network_input_output" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords extends, theory, network, input-output, jacobian in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_authors_show_multilayer_perceptron_i`

- Preferred role: `method`
- Cue keywords: `authors, show, multilayer, perceptron, its, jacobian, jointly, converge, gaussian, process`
- Narration: The authors show that a multilayer perceptron and its Jacobian jointly converge to a Gaussian process as width grows, define a Jacobian Neural Tangent Kernel that governs training, and prove that training with a Jacobian regulariser, so-called robust training, behaves in the infinite-width limit like a simple kernel regression.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_authors_show_multilayer_perceptron_i" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, show, multilayer, perceptron, its, jacobian in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_along_way_they_explain_first`

- Preferred role: `content`
- Cue keywords: `along, way, they, explain, first, time, angle, why, jacobian, regularisation`
- Narration: Along the way they explain, for the first time from this angle, why Jacobian regularisation makes networks both accurate and robust.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c4_along_way_they_explain_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords along, way, they, explain, first, time in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_over_last_few_years_infinite_width`

- Preferred role: `title`
- Cue keywords: `over, last, few, years, infinite-width, theory, given, remarkably, clean, answers`
- Narration: Over the last few years, infinite-width theory has given us remarkably clean answers about deep networks. Tools like the Neural Tangent Kernel tell us how a network initialises, how it trains, and where gradient descent ends up.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c1_over_last_few_years_infinite_width" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords over, last, few, years, infinite-width, theory in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_catch_all_describes_network`

- Preferred role: `content`
- Cue keywords: `but, catch, all, describes, network, output, says, nothing, about, network`
- Narration: But there is a catch: all of this describes a network's output. It says nothing about the network's input-output Jacobian, the object that captures how smooth the network is.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_but_catch_all_describes_network" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, catch, all, describes, network, output in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_smoothness_exactly_what_care_about`

- Preferred role: `content`
- Cue keywords: `smoothness, exactly, what, care, about, when, want, robustness, noise, adversarial`
- Narration: And smoothness is exactly what we care about when we want robustness to noise or to adversarial attacks.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_smoothness_exactly_what_care_about" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords smoothness, exactly, what, care, about, when in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_natural_question_left_wide_open`

- Preferred role: `method`
- Cue keywords: `natural, question, left, wide, open, extend, infinite-width, theory, jacobian, itself`
- Narration: So a natural question is left wide open: can we extend infinite-width theory to the Jacobian itself, and to training that deliberately regularises it?
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_natural_question_left_wide_open" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords natural, question, left, wide, open, extend in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_jacobian_regularisation_one_those_me`

- Preferred role: `method`
- Cue keywords: `jacobian, regularisation, one, those, methods, just, works`
- Narration: Jacobian regularisation is one of those methods that just works.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_jacobian_regularisation_one_those_me" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords jacobian, regularisation, one, those, methods, just in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_add_penalty_network_input_output_jac`

- Preferred role: `method`
- Cue keywords: `add, penalty, network, input-output, jacobian, you, get, simple, strong, defence`
- Narration: Add a penalty on the network's input-output Jacobian and you get a simple, strong defence against adversarial examples. The problem is that nobody could really explain why.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_add_penalty_network_input_output_jac" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords add, penalty, network, input-output, jacobian, you in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_theory_had_cracked_open_ordinary`

- Preferred role: `method`
- Cue keywords: `theory, had, cracked, open, ordinary, infinite-width, limit, had, never, been`
- Narration: The theory that had cracked open ordinary training, the infinite-width limit, had never been pushed to cover the Jacobian, let alone training that penalises it.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_theory_had_cracked_open_ordinary" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords theory, had, cracked, open, ordinary, infinite-width in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_asks_whether_same_lens_finally`

- Preferred role: `title`
- Cue keywords: `asks, whether, same, lens, finally, explain, what, jacobian, regularisation, doing`
- Narration: This paper asks whether that same lens can finally explain what Jacobian regularisation is doing.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s03_c4_asks_whether_same_lens_finally" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords asks, whether, same, lens, finally, explain in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_four_moves_first_proves`

- Preferred role: `content`
- Cue keywords: `makes, four, moves, first, proves, initialisation, multilayer, perceptron, its, jacobian`
- Narration: The paper makes four moves. First, it proves that at initialisation a multilayer perceptron and its Jacobian jointly converge to a zero-mean Gaussian process, and it writes down that limiting kernel, the Jacobian NNGP kernel, inductively over depth.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_four_moves_first_proves" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, four, moves, first, proves, initialisation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_defines_jacobian_neural_tange`

- Preferred role: `method`
- Cue keywords: `second, defines, jacobian, neural, tangent, kernel, jntk, proves, becomes, deterministic`
- Narration: Second, it defines a Jacobian Neural Tangent Kernel, the JNTK, and proves it becomes deterministic at initialisation and then stays constant throughout robust training as width grows.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_second_defines_jacobian_neural_tange" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, defines, jacobian, neural, tangent, kernel in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_because_kernel_constant_dynami`

- Preferred role: `method`
- Cue keywords: `third, because, kernel, constant, dynamics, collapse, linear, first-order, differential, equation`
- Narration: Third, because the kernel is constant, the training dynamics collapse to a linear first-order differential equation whose infinite-time solution is a plain kernel regressor.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_third_because_kernel_constant_dynami" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, because, kernel, constant, dynamics, collapse in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_fourth_validates_all_empirically_sol`

- Preferred role: `result`
- Cue keywords: `fourth, validates, all, empirically, solution, study, when, accuracy, robustness, together`
- Narration: And fourth, it validates all of this empirically and uses the solution to study when accuracy and robustness go together.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c4_fourth_validates_all_empirically_sol" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fourth, validates, all, empirically, solution, study in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_how_works_robust_minimises_usual`

- Preferred role: `method`
- Cue keywords: `how, works, robust, minimises, usual, mean-squared, error, plus, lambda, times`
- Narration: Here is how it works. Robust training minimises the usual mean-squared error plus lambda times a penalty on the network's Jacobian at each training point.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_how_works_robust_minimises_usual" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, works, robust, minimises, usual, mean-squared in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_handle_joint_object_network_its`

- Preferred role: `title`
- Cue keywords: `handle, joint, object, network, its, jacobian, together, authors, recast, convergence`
- Narration: To handle the joint object, the network and its Jacobian together, the authors recast the convergence question as a tensor program and apply the Master theorem.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s05_c2_handle_joint_object_network_its" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords handle, joint, object, network, its, jacobian in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_they_define_finite_jntk_parameter_gr`

- Preferred role: `content`
- Cue keywords: `they, define, finite, jntk, parameter-gradients, both, output, jacobian, component`
- Narration: They then define the finite JNTK from the parameter-gradients of both the output and each Jacobian component.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_they_define_finite_jntk_parameter_gr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, define, finite, jntk, parameter-gradients, both in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_crucial_step_showing_kernel_does`

- Preferred role: `method`
- Cue keywords: `crucial, step, showing, kernel, does, not, move, during, turns, learning`
- Narration: The crucial step is showing this kernel does not move during training; that turns the learning dynamics into a linear differential equation, and its infinite-time solution is a kernel regression using the limiting JNTK, rescaled by a simple diagonal matrix that carries the regularisation strength lambda.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_crucial_step_showing_kernel_does" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucial, step, showing, kernel, does, not in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_deliberately_small_contr`

- Preferred role: `content`
- Cue keywords: `experiments, deliberately, small, controlled`
- Narration: The experiments are deliberately small and controlled.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_experiments_deliberately_small_contr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, deliberately, small, controlled in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_test_kernel_convergence_claims_autho`

- Preferred role: `content`
- Cue keywords: `test, kernel-convergence, claims, authors, synthetic, 256, point, dataset, four, dimensions`
- Narration: To test the kernel-convergence claims, the authors use a synthetic 256-point dataset in four dimensions, built to approximate an even covering of the sphere, and sweep every combination of width from 64 up to 8192 and depth one, two, and three.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_test_kernel_convergence_claims_autho" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords test, kernel-convergence, claims, authors, synthetic, 256 in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_test_kernel_really_stays_constant`

- Preferred role: `method`
- Cue keywords: `test, kernel, really, stays, constant, during, robust, they, switch, algerian`
- Narration: To test that the kernel really stays constant during robust training, they switch to the Algerian forest fire dataset from the UCI repository, 224 points with eleven input features, treated as a plus-or-minus-one regression problem.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_test_kernel_really_stays_constant" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords test, kernel, really, stays, constant, during in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_same_setups_let_them_line`

- Preferred role: `method`
- Cue keywords: `same, setups, let, them, line, robust, against, standard, head, head`
- Narration: The same setups let them line up robust training against standard training head to head.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_same_setups_let_them_line" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords same, setups, let, them, line, robust in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_theory_holds`

- Preferred role: `content`
- Cue keywords: `theory, holds`
- Narration: The theory holds up.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_theory_holds" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords theory, holds in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_network_gets_wider_finite_jacobian`

- Preferred role: `content`
- Cue keywords: `network, gets, wider, finite, jacobian, nngp, kernel, closes, its, predicted`
- Narration: As the network gets wider, the finite Jacobian NNGP kernel closes in on its predicted deterministic limit, and the scaled finite JNTK converges to the limiting JNTK, matching the two initialisation theorems.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_network_gets_wider_finite_jacobian" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords network, gets, wider, finite, jacobian, nngp in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_during_robust_gap_between_finite`

- Preferred role: `method`
- Cue keywords: `during, robust, gap, between, finite, jntk, its, limit, shrinks, monotonically`
- Narration: And during robust training, the gap between the finite JNTK and its limit shrinks monotonically with width at every training step we checked, which is exactly what the constancy theorem predicts.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_during_robust_gap_between_finite" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords during, robust, gap, between, finite, jntk in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_largest_networks_tested_don_fully`

- Preferred role: `content`
- Cue keywords: `largest, networks, tested, don, fully, nail, bound, because, compute, limits`
- Narration: The largest networks tested don't fully nail the bound because of compute limits, but the trend is unmistakable: wider is closer, in precisely the way the theory says.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_largest_networks_tested_don_fully" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords largest, networks, tested, don, fully, nail in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_most_striking_finding_comes_analysin`

- Preferred role: `method`
- Cue keywords: `most, striking, finding, comes, analysing, kernel-regression, solution, jacobian, regularisation, eigenfeatures`
- Narration: The most striking finding comes from analysing the kernel-regression solution. With Jacobian regularisation, the eigenfeatures that are more accurate are also more robust; accuracy and robustness move together.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_most_striking_finding_comes_analysin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords most, striking, finding, comes, analysing, kernel-regression in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_standard_shows_almost_such_link`

- Preferred role: `method`
- Cue keywords: `standard, shows, almost, such, link, never, produces, accurate-but-fragile, features, seen`
- Narration: Standard training shows almost no such link, and it never produces the accurate-but-fragile features seen in earlier finite-NTK work.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_standard_shows_almost_such_link" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords standard, shows, almost, such, link, never in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_regulariser_isn_just_trading_little`

- Preferred role: `result`
- Cue keywords: `regulariser, isn, just, trading, little, accuracy, robustness, aligns, two`
- Narration: So the regulariser isn't just trading a little accuracy for robustness; it aligns the two.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c3_regulariser_isn_just_trading_little" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords regulariser, isn, just, trading, little, accuracy in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_separate_check_key_full_rank_assumpt`

- Preferred role: `content`
- Cue keywords: `separate, check, key, full-rank, assumption, shows, fragile, jntk, smallest, eigenvalue`
- Narration: A separate check on the key full-rank assumption shows it is fragile: the JNTK's smallest eigenvalue is far below the NTK's and only becomes positive for deeper networks, depth eleven for GeLU but just six for the erf activation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_separate_check_key_full_rank_assumpt" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords separate, check, key, full-rank, assumption, shows in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_anchor_study_widths`

- Preferred role: `content`
- Cue keywords: `few, numbers, anchor, study, widths, span, 64, 8192, powers, two`
- Narration: A few numbers anchor the study. Widths span 64 to 8192, powers of two from six to thirteen.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_anchor_study_widths" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, anchor, study, widths, span in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_every_experiment_repeated_ten_times`

- Preferred role: `method`
- Cue keywords: `every, experiment, repeated, ten, times, reported, ninety-five, percent, bootstrap, confidence`
- Narration: Every experiment is repeated ten times and reported with ninety-five percent bootstrap confidence intervals, and the covariance estimates rest on a full million Monte-Carlo samples.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_every_experiment_repeated_ten_times" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords every, experiment, repeated, ten, times, reported in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_robust_jacobian_coefficient_0_01_sca`

- Preferred role: `method`
- Cue keywords: `robust, jacobian, coefficient, 0.01, scaling, kappa, 0.1, learning, rate, one`
- Narration: Robust training uses a Jacobian coefficient of 0.01, a scaling kappa of 0.1, and a learning rate of one.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_robust_jacobian_coefficient_0_01_sca" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords robust, jacobian, coefficient, 0.01, scaling, kappa in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_full_rank_condition_first_kicks_dept`

- Preferred role: `content`
- Cue keywords: `full-rank, condition, first, kicks, depth, eleven, gelu, depth, six, erf`
- Narration: The full-rank condition first kicks in at depth eleven for GeLU and depth six for erf, and the theory's width requirement scales like N-squared times log-N to the twelve-L.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_full_rank_condition_first_kicks_dept" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords full-rank, condition, first, kicks, depth, eleven in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_bottom_line_infinite_width_theory_no`

- Preferred role: `result`
- Cue keywords: `bottom, line, infinite-width, theory, now, reaches, jacobian`
- Narration: The bottom line is that infinite-width theory now reaches the Jacobian.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c1_bottom_line_infinite_width_theory_no" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords bottom, line, infinite-width, theory, now, reaches in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_train_wide_network_jacobian_regulari`

- Preferred role: `content`
- Cue keywords: `train, wide, network, jacobian, regulariser, limit, behaves, like, kernel, regression`
- Narration: Train a wide network with a Jacobian regulariser and, in the limit, it behaves like kernel regression with a Jacobian Neural Tangent Kernel.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_train_wide_network_jacobian_regulari" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords train, wide, network, jacobian, regulariser, limit in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_same_regulariser_makes_accuracy_robu`

- Preferred role: `result`
- Cue keywords: `same, regulariser, makes, accuracy, robustness, pull, same, direction, instead, fighting`
- Narration: And that same regulariser makes accuracy and robustness pull in the same direction instead of fighting each other, giving us the first principled explanation, from the infinite-width viewpoint, of why penalising the Jacobian yields networks that are both accurate and robust.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c3_same_regulariser_makes_accuracy_robu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords same, regulariser, makes, accuracy, robustness, pull in title/desc so the matcher can verify semantic overlap.
