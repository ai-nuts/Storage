# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_reinforcement_learning_promises_opti`

- Preferred role: `content`
- Cue keywords: `reinforcement, learning, promises, optimal, decisions, but, almost, every, algorithm, quietly`
- Narration: Reinforcement learning promises optimal decisions, but almost every algorithm quietly assumes the world never changes. In real settings like mobile health, traffic control, and robotics, that stationarity assumption breaks down over time and quietly poisons the learned policy.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_reinforcement_learning_promises_opti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reinforcement, learning, promises, optimal, decisions, but in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_introduces_doubly_robust_statistical`

- Preferred role: `content`
- Cue keywords: `introduces, doubly, robust, statistical, test, checks, whether, offline, markov, decision`
- Narration: This paper introduces a doubly robust statistical test that checks whether an offline Markov decision process is actually stationary, and pinpoints where it changes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_introduces_doubly_robust_statistical" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, doubly, robust, statistical, test, checks in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_test_pairs_modern_machine_learning`

- Preferred role: `content`
- Cue keywords: `test, pairs, modern, machine, learning, estimators, semiparametric, statistics, controls, false`
- Narration: The test pairs modern machine learning estimators with semiparametric statistics, so it controls false alarms while staying powerful even when the state space is high dimensional.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_test_pairs_modern_machine_learning" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords test, pairs, modern, machine, learning, estimators in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_across_four_simulations_real_intern`

- Preferred role: `content`
- Cue keywords: `across, four, simulations, real, intern, health, study, detects, change, points`
- Narration: Across four simulations and a real intern health study, it detects change points others miss and lets policies recover the reward that non stationarity would otherwise cost.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c4_across_four_simulations_real_intern" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, four, simulations, real, intern, health in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_reinforcement_learning_agents_traine`

- Preferred role: `method`
- Cue keywords: `reinforcement, learning, agents, trained, find, optimal, policy, but, nearly, every`
- Narration: Reinforcement learning agents are trained to find the optimal policy, but nearly every algorithm leans on one fragile assumption: that the environment never changes.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_reinforcement_learning_agents_traine" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reinforcement, learning, agents, trained, find, optimal in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_stationarity_assumption_requiring_st`

- Preferred role: `content`
- Cue keywords: `stationarity, assumption, requiring, state, transition, reward, functions, stay, fixed, over`
- Narration: This is the stationarity assumption, requiring the state transition and reward functions to stay fixed over time. In the real world, that rarely holds.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_stationarity_assumption_requiring_st" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stationarity, assumption, requiring, state, transition, reward in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_robotics_healthcare_digital_marketin`

- Preferred role: `content`
- Cue keywords: `robotics, healthcare, digital, marketing, all, drift, over, long, horizons, policy`
- Narration: Robotics, healthcare, and digital marketing all drift over long horizons, and a policy learned as if the world were frozen quietly becomes suboptimal, sometimes even harmful.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_robotics_healthcare_digital_marketin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords robotics, healthcare, digital, marketing, all, drift in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_problem_tackles_how_reliably_tell`

- Preferred role: `content`
- Cue keywords: `problem, tackles, how, reliably, tell, whether, offline, decision-making, system, actually`
- Narration: The problem this paper tackles is how to reliably tell whether an offline decision-making system is actually stationary before you trust the policy it produced.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_problem_tackles_how_reliably_tell" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords problem, tackles, how, reliably, tell, whether in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_why_does_matter_now_consider`

- Preferred role: `content`
- Cue keywords: `why, does, matter, now, consider, intern, health, study, year-long, mobile-health`
- Narration: Why does this matter now? Consider the Intern Health Study, a year-long mobile-health trial that nudges first-year physicians toward healthier habits through push notifications.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_why_does_matter_now_consider" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords why, does, matter, now, consider, intern in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_effect_those_nudges_wanes_over`

- Preferred role: `content`
- Cue keywords: `effect, those, nudges, wanes, over, time, textbook, case, non-stationarity, similar`
- Narration: The effect of those nudges wanes over time, a textbook case of non-stationarity. Similar drift shows up in traffic signal control, where flow patterns swing between peak and off-peak hours.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_effect_those_nudges_wanes_over" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords effect, those, nudges, wanes, over, time in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_ignoring_these_shifts_leads_policies`

- Preferred role: `content`
- Cue keywords: `ignoring, these, shifts, leads, policies, send, prompts, wrong, moments, erode`
- Narration: Ignoring these shifts leads to policies that send prompts at the wrong moments and erode long-term reward.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_ignoring_these_shifts_leads_policies" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ignoring, these, shifts, leads, policies, send in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_prior_stationarity_tests_either_dema`

- Preferred role: `content`
- Cue keywords: `prior, stationarity, tests, either, demand, knowledge, true, fall, back, linear`
- Narration: Prior stationarity tests either demand knowledge of the true model, or fall back on linear approximations that collapse in high dimensions, leaving a real gap for modern applications.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_prior_stationarity_tests_either_dema" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, stationarity, tests, either, demand, knowledge in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_core_contribution_model_based_doubly`

- Preferred role: `content`
- Cue keywords: `core, contribution, model-based, doubly, robust, procedure, tests, stationarity, assumption, locates`
- Narration: The paper's core contribution is a model-based, doubly robust procedure that tests the stationarity assumption and locates change points in offline reinforcement learning.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_core_contribution_model_based_doubly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, contribution, model-based, doubly, robust, procedure in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_doubly_robust_means_test_controls`

- Preferred role: `method`
- Cue keywords: `doubly, robust, means, test, controls, type-one, error, long, either, transition`
- Narration: Doubly robust means the test controls the type-one error as long as either the transition function or the marginal state-action distribution is correctly specified, so you get valid inference even when one nuisance model is wrong.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_doubly_robust_means_test_controls" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords doubly, robust, means, test, controls, type-one in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_top_method_authors_prove_size`

- Preferred role: `method`
- Cue keywords: `top, method, authors, prove, size, control, double, robustness, under, bidirectional`
- Narration: On top of the method, the authors prove size control and double robustness under a bidirectional asymptotic framework, where either the number of trajectories or the length of the horizon may grow to infinity, and they supply a Gaussian multiplier bootstrap to compute honest p-values.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_top_method_authors_prove_size" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords top, method, authors, prove, size, control in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_how_test_works_candidate_change`

- Preferred role: `content`
- Cue keywords: `how, test, works, candidate, change, point, compares, pooled, transition, dynamics`
- Narration: Here is how the test works. At each candidate change point, it compares the pooled transition dynamics before and after that time using a CUSUM-style statistic.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_how_test_works_candidate_change" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, test, works, candidate, change, point in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_naively_plugging_modern_machine_lear`

- Preferred role: `content`
- Cue keywords: `naively, plugging, modern, machine-learning, estimators, comparison, introduces, heavy, bias, authors`
- Narration: Naively plugging modern machine-learning estimators into this comparison introduces heavy bias, so the authors add a mean-zero augmentation term, producing a doubly robust estimating function.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_naively_plugging_modern_machine_lear" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords naively, plugging, modern, machine-learning, estimators, comparison in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_lets_flexible_models_like_neural`

- Preferred role: `method`
- Cue keywords: `lets, flexible, models, like, neural, networks, random, forests, estimate, transition`
- Narration: That lets flexible models like neural networks and random forests estimate the transition and state-action distributions without spoiling the inference.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_lets_flexible_models_like_neural" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lets, flexible, models, like, neural, networks in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_sample_splitting_cross_fitting_norma`

- Preferred role: `method`
- Cue keywords: `sample, splitting, cross-fitting, normalize, statistic, across, candidate, points, test, functions`
- Narration: Sample splitting and cross-fitting normalize the statistic across candidate points and test functions, and a Gaussian multiplier bootstrap approximates its null distribution to yield the final p-value. The maximum over time and test functions of the normalized, CUSUM-weighted statistic gives the test statistic gamma-hat.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_sample_splitting_cross_fitting_norma" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sample, splitting, cross-fitting, normalize, statistic, across in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_method_stress_tested_across_four_num`

- Preferred role: `method`
- Cue keywords: `method, stress-tested, across, four, numerical, studies, one, real, dataset, discrete-state`
- Narration: The method is stress-tested across four numerical studies and one real dataset. A discrete-state toy example illustrates the double robustness property directly.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_method_stress_tested_across_four_num" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, stress-tested, across, four, numerical, studies in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_high_dimensional_synthetic_pushes_st`

- Preferred role: `result`
- Cue keywords: `high-dimensional, synthetic, pushes, state, dimension, one, thirty, pits, test, against`
- Narration: High-dimensional synthetic data pushes the state dimension from one up to thirty and pits the test against two existing baselines, ODCP and CUSUM-RL.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_high_dimensional_synthetic_pushes_st" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords high-dimensional, synthetic, pushes, state, dimension, one in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_four_by_four_grid_world_shows_how`

- Preferred role: `method`
- Cue keywords: `four-by-four, grid, world, shows, how, detecting, change, point, improves, policy`
- Narration: A four-by-four grid world shows how detecting the change point improves policy learning, and a batch-online semi-synthetic study mimics the structure of the real trial.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_four_by_four_grid_world_shows_how" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords four-by-four, grid, world, shows, how, detecting in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_finally_authors_apply_test_intern`

- Preferred role: `result`
- Cue keywords: `finally, authors, apply, test, intern, health, study, twenty-one-week, mobile-health, micro-randomized`
- Narration: Finally, the authors apply the test to the Intern Health Study, a twenty-one-week mobile-health micro-randomized trial of medical interns in the United States.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_finally_authors_apply_test_intern" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finally, authors, apply, test, intern, health in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_finding_about_robustness_di`

- Preferred role: `content`
- Cue keywords: `headline, finding, about, robustness, dimensionality`
- Narration: The headline finding is about robustness to dimensionality.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_headline_finding_about_robustness_di" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, finding, about, robustness, dimensionality in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_every_setting_proposed_test_keeps`

- Preferred role: `result`
- Cue keywords: `every, setting, proposed, test, keeps, type-one, error, nominal, level, crucially`
- Narration: In every setting, the proposed test keeps the type-one error at the nominal level, and crucially it still pinpoints the true change point even when the state has ten, twenty, or thirty dimensions.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_every_setting_proposed_test_keeps" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords every, setting, proposed, test, keeps, type-one in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_contrast_cusum_rl_baseline_only_reco`

- Preferred role: `method`
- Cue keywords: `contrast, cusum-rl, baseline, only, recovers, change, point, when, state, one-dimensional`
- Narration: By contrast, the CUSUM-RL baseline only recovers the change point when the state is one-dimensional, and the ODCP method fails to control the type-one error at all in high dimensions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_contrast_cusum_rl_baseline_only_reco" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords contrast, cusum-rl, baseline, only, recovers, change in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_toy_example_confirms_double_robustne`

- Preferred role: `method`
- Cue keywords: `toy, example, confirms, double, robustness, action, size, power, hold, long`
- Narration: The toy example confirms the double robustness in action: size and power hold as long as at least one of the two nuisance models is right, with the strongest power when both are correct.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_toy_example_confirms_double_robustne" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords toy, example, confirms, double, robustness, action in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_most_informative_ablation_varies_mis`

- Preferred role: `content`
- Cue keywords: `most, informative, ablation, varies, misspecification, level, mild, severe, across, five`
- Narration: The most informative ablation varies the model misspecification level from mild to severe, across five hundred replications.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_most_informative_ablation_varies_mis" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords most, informative, ablation, varies, misspecification, level in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_shows_empirical_size_staying_pinned`

- Preferred role: `method`
- Cue keywords: `shows, empirical, size, staying, pinned, nominal, level, whenever, least, one`
- Narration: It shows the empirical size staying pinned at the nominal level whenever at least one of the two nuisance models remains correctly specified, a clean demonstration of the double robustness property.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_shows_empirical_size_staying_pinned" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords shows, empirical, size, staying, pinned, nominal in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_second_sweep_varies_kappa_length`

- Preferred role: `content`
- Cue keywords: `second, sweep, varies, kappa, length, tested, interval, actually, locate, single`
- Narration: A second sweep varies kappa, the length of the tested interval, to actually locate the single change point: the test correctly holds its size while the null is true and its power climbs once the interval crosses the true change point at twenty-five.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_second_sweep_varies_kappa_length" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, sweep, varies, kappa, length, tested in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_anchor_impact_test`

- Preferred role: `result`
- Cue keywords: `few, numbers, anchor, impact, test, sustains, correct, change-point, detection, all`
- Narration: A few numbers anchor the impact. The test sustains correct change-point detection all the way up to a state dimension of thirty, whereas the closest competitor works only at dimension one.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_few_numbers_anchor_impact_test" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, anchor, impact, test, sustains in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_maintains_nominal_five_percent_signi`

- Preferred role: `content`
- Cue keywords: `maintains, nominal, five-percent, significance, level, across, all, four, simulations, both`
- Narration: It maintains the nominal five-percent significance level across all four simulations and both real-data specialties.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_maintains_nominal_five_percent_signi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords maintains, nominal, five-percent, significance, level, across in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_real_intern_health_study_flags`

- Preferred role: `content`
- Cue keywords: `real, intern, health, study, flags, genuine, change, point, internal, medicine`
- Narration: And on the real Intern Health Study data, it flags a genuine change point for Internal Medicine interns at week sixteen, while correctly finding no change for the Family Practice group.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_real_intern_health_study_flags" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords real, intern, health, study, flags, genuine in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_these_results_come_thousands_bootstr`

- Preferred role: `method`
- Cue keywords: `these, results, come, thousands, bootstrap, samples, hundreds, replications, per, setting`
- Narration: These results come from thousands of bootstrap samples and hundreds of replications per setting.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_these_results_come_thousands_bootstr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, results, come, thousands, bootstrap, samples in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple`
- Narration: The takeaway is simple.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_marrying_flexibility_modern_machine`

- Preferred role: `content`
- Cue keywords: `marrying, flexibility, modern, machine, learning, rigor, semiparametric, statistics, doubly, robust`
- Narration: By marrying the flexibility of modern machine learning with the rigor of semiparametric statistics, this doubly robust CUSUM test reliably flags when an offline reinforcement-learning environment stops being stationary, even in high dimensions, so that policies can be relearned on the correct, stationary segment of data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_marrying_flexibility_modern_machine" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords marrying, flexibility, modern, machine, learning, rigor in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_when_some_homogeneity_present_detect`

- Preferred role: `method`
- Cue keywords: `when, some, homogeneity, present, detecting, adapting, change, points, recovers, near-oracle`
- Narration: When some homogeneity is present, detecting and adapting to change points recovers near-oracle reward that stationary or sliding-window strategies simply leave on the table.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_when_some_homogeneity_present_detect" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, some, homogeneity, present, detecting, adapting in title/desc so the matcher can verify semantic overlap.
