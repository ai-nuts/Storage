# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_offline_reinforcement_learning_domai`

- Preferred role: `content`
- Cue keywords: `offline, reinforcement, learning, domains, like, healthcare, education, must, estimate, environment`
- Narration: Offline reinforcement learning in domains like healthcare and education must estimate the environment's transition dynamics from fixed batch data, yet standard maximum likelihood estimates give high variance policies that make dangerous mistakes where data is sparse.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_offline_reinforcement_learning_domai" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords offline, reinforcement, learning, domains, like, healthcare in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_introduces_bayesian_inverse_transiti`

- Preferred role: `method`
- Cue keywords: `introduces, bayesian, inverse, transition, learning, gradient, free, constraint, based, method`
- Narration: This paper introduces Bayesian Inverse Transition Learning, a gradient free, constraint based method that uses an expert's near optimal demonstrations to clip a Bayesian posterior over the transition dynamics.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_introduces_bayesian_inverse_transiti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, bayesian, inverse, transition, learning, gradient in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_result_distribution_dynamics_guarant`

- Preferred role: `method`
- Cue keywords: `result, distribution, dynamics, guarantees, safe, high, performing, policies, recovering, one`
- Narration: The result is a distribution of dynamics that guarantees safe, high performing policies, recovering one hundred percent accuracy on states where the best action is known and cutting policy variance dramatically across datasets.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_result_distribution_dynamics_guarant" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, distribution, dynamics, guarantees, safe, high in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_fields_like_healthcare_education_can`

- Preferred role: `content`
- Cue keywords: `fields, like, healthcare, education, cannot, experiment, freely, offline, reinforcement, learning`
- Narration: In fields like healthcare and education we cannot experiment freely, so offline reinforcement learning must learn the environment's transition dynamics purely from a fixed batch of collected experience.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_fields_like_healthcare_education_can" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fields, like, healthcare, education, cannot, experiment in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_trouble_only_covers_actions_original`

- Preferred role: `content`
- Cue keywords: `trouble, only, covers, actions, original, users, actually, took, leaving, much`
- Narration: The trouble is that this data only covers the actions the original users actually took, leaving much of the state and action space unseen.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_trouble_only_covers_actions_original" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trouble, only, covers, actions, original, users in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_standard_maximum_likelihood_estimate`

- Preferred role: `content`
- Cue keywords: `standard, maximum, likelihood, estimates, dynamics, therefore, produce, policies, swing, wildly`
- Narration: Standard maximum likelihood estimates of the dynamics therefore produce policies that swing wildly from dataset to dataset and can recommend genuinely unsafe actions in the regions where data is thin.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_standard_maximum_likelihood_estimate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords standard, maximum, likelihood, estimates, dynamics, therefore in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_key_insight_people_who_generate`

- Preferred role: `content`
- Cue keywords: `key, insight, people, who, generate, offline, such, clinicians, usually, acting`
- Narration: The key insight is that the people who generate this offline data, such as clinicians, are usually acting near optimally.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_key_insight_people_who_generate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, insight, people, who, generate, offline in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_their_choices_quietly_encode_which`

- Preferred role: `content`
- Cue keywords: `their, choices, quietly, encode, which, actions, good, which, bad, yet`
- Narration: Their choices quietly encode which actions are good and which are bad, yet a plain maximum likelihood fit of the dynamics throws that information away.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_their_choices_quietly_encode_which" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords their, choices, quietly, encode, which, actions in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_earlier_gradient_based_inverse_reinf`

- Preferred role: `method`
- Cue keywords: `earlier, gradient, based, inverse, reinforcement, learning, methods, try, recover, expert`
- Narration: Earlier gradient based inverse reinforcement learning methods try to recover an expert's belief about the dynamics, but they never connect their estimate back to the true environment and they suffer from the fragility of gradient optimization.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_earlier_gradient_based_inverse_reinf" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords earlier, gradient, based, inverse, reinforcement, learning in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_want_exploit_expert_signal_directly`

- Preferred role: `content`
- Cue keywords: `want, exploit, expert, signal, directly, without, gradients`
- Narration: We want to exploit the expert signal directly and without gradients.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_want_exploit_expert_signal_directly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords want, exploit, expert, signal, directly, without in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_work_introduces_inverse_transition_l`

- Preferred role: `method`
- Cue keywords: `work, introduces, inverse, transition, learning, gradient, free, constraint, based, approach`
- Narration: This work introduces Inverse Transition Learning, a gradient free and constraint based approach.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_work_introduces_inverse_transition_l" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, introduces, inverse, transition, learning, gradient in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_converts_near_optimal_expert_policy`

- Preferred role: `method`
- Cue keywords: `converts, near, optimal, expert, policy, set, constraints, transition, dynamics, clips`
- Narration: It converts a near optimal expert policy into a set of constraints on the transition dynamics, and then clips a Bayesian posterior over the dynamics so that every sampled model yields a safe and high performing policy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_converts_near_optimal_expert_policy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords converts, near, optimal, expert, policy, set in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_beyond_method_itself_carefully_analy`

- Preferred role: `method`
- Cue keywords: `beyond, method, itself, carefully, analyzes, when, why, maximum, likelihood, estimation`
- Narration: Beyond the method itself, the paper carefully analyzes when and why maximum likelihood estimation of the dynamics breaks down under uneven data coverage, and it shows how combining the constraints with uncertainty produces an informative ranking of actions in the states where the expert is unsure.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_beyond_method_itself_carefully_analy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords beyond, method, itself, carefully, analyzes, when in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_given_rewards_epsilon_optimal_expert`

- Preferred role: `method`
- Cue keywords: `given, rewards, epsilon, optimal, expert, policy, batch, closed, form, bellman`
- Narration: Given the rewards, an epsilon optimal expert policy, and the batch data, we use the closed form Bellman equations to write constraints that demand the value of actions the expert takes exceed the value of actions the expert never took.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_given_rewards_epsilon_optimal_expert" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords given, rewards, epsilon, optimal, expert, policy in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_any_dynamics_satisfying_these_constr`

- Preferred role: `method`
- Cue keywords: `any, dynamics, satisfying, these, constraints, recovers, what, call, expert, epsilon`
- Narration: Any dynamics satisfying these constraints recovers what we call the expert's epsilon ball structure.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_any_dynamics_satisfying_these_constr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords any, dynamics, satisfying, these, constraints, recovers in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_place_dirichlet_multinomial_posterio`

- Preferred role: `method`
- Cue keywords: `place, dirichlet, multinomial, posterior, over, dynamics, rejection, sampling, keeping, only`
- Narration: We then place a Dirichlet multinomial posterior over the dynamics and use rejection sampling, keeping only the samples that satisfy the constraints. The surviving samples form a clipped posterior that respects the expert's knowledge.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_place_dirichlet_multinomial_posterio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords place, dirichlet, multinomial, posterior, over, dynamics in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_separate_constraint_sets_handle_full`

- Preferred role: `method`
- Cue keywords: `separate, constraint, sets, handle, fully, optimal, expert, partially, uncertain, one`
- Narration: Separate constraint sets handle a fully optimal expert and a partially uncertain one, with a tunable slack term that enforces the structure even where action non linearity would otherwise break it.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_separate_constraint_sets_handle_full" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords separate, constraint, sets, handle, fully, optimal in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_all_experiments_run_synthetic_tabula`

- Preferred role: `content`
- Cue keywords: `all, experiments, run, synthetic, tabular, markov, decision, process, fifteen, states`
- Narration: All experiments run on a synthetic tabular Markov decision process with fifteen states plus a terminal state and six actions, using a discount factor of zero point nine five.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_all_experiments_run_synthetic_tabula" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords all, experiments, run, synthetic, tabular, markov in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_true_dynamics_deliberately_mixed_som`

- Preferred role: `content`
- Cue keywords: `true, dynamics, deliberately, mixed, sometimes, uniform, sometimes, highly, skewed, toward`
- Narration: The true dynamics are deliberately mixed, sometimes uniform and sometimes highly skewed toward a few states, to create rich and varied behavior.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_true_dynamics_deliberately_mixed_som" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords true, dynamics, deliberately, mixed, sometimes, uniform in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_study_two_coverage_regimes_low`

- Preferred role: `content`
- Cue keywords: `study, two, coverage, regimes, low, setting, fifteen, episodes, high, setting`
- Narration: We study two coverage regimes, a low data setting of fifteen episodes and a high data setting of three hundred, crossed with three levels of expert optimality that create zero, three, and six uncertain policy states.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_study_two_coverage_regimes_low" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords study, two, coverage, regimes, low, setting in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_every_reported_number_averaged_over`

- Preferred role: `result`
- Cue keywords: `every, reported, number, averaged, over, one, thousand, independently, generated, datasets`
- Narration: Every reported number is averaged over one thousand independently generated datasets.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_every_reported_number_averaged_over" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords every, reported, number, averaged, over, one in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_clipped_posterior_dominates_both_max`

- Preferred role: `content`
- Cue keywords: `clipped, posterior, dominates, both, maximum, likelihood, clipped, bayesian, posterior`
- Narration: The clipped posterior dominates both maximum likelihood and the un clipped Bayesian posterior.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_clipped_posterior_dominates_both_max" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords clipped, posterior, dominates, both, maximum, likelihood in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_guarantees_one_hundred_percent_accur`

- Preferred role: `result`
- Cue keywords: `guarantees, one, hundred, percent, accuracy, states, where, expert, knows, single`
- Narration: It guarantees one hundred percent accuracy on states where the expert knows the single best action, in every data and optimality setting, whereas maximum likelihood ranges from sixty seven to ninety two percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_guarantees_one_hundred_percent_accur" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords guarantees, one, hundred, percent, accuracy, states in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_also_never_selects_action_outside`

- Preferred role: `method`
- Cue keywords: `also, never, selects, action, outside, expert, epsilon, ball, makes, truly`
- Narration: It also never selects an action outside the expert's epsilon ball, so it makes no truly bad mistakes.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_also_never_selects_action_outside" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords also, never, selects, action, outside, expert in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_strikingly_even_though_constraints_s`

- Preferred role: `method`
- Cue keywords: `strikingly, even, though, constraints, say, nothing, explicit, about, which, action`
- Narration: Strikingly, even though the constraints say nothing explicit about which action to pick in uncertain states, our method is still more accurate there than the baselines, which means the constraints implicitly transfer the expert's uncertainty structure.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_strikingly_even_though_constraints_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords strikingly, even, though, constraints, say, nothing in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_central_finding_analysis_more_does`

- Preferred role: `figure`
- Cue keywords: `central, finding, analysis, more, does, not, rescue, maximum, likelihood`
- Narration: A central finding of the analysis is that more data does not rescue maximum likelihood.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c1_central_finding_analysis_more_does" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords central, finding, analysis, more, does, not in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_even_high_regime_keeps_making`

- Preferred role: `content`
- Cue keywords: `even, high, regime, keeps, making, bad, mistakes, choosing, actions, outside`
- Narration: Even in the high data regime it keeps making bad mistakes, choosing actions outside the epsilon ball, because expert only data leaves large parts of the state and action space unexplored no matter how many episodes we collect.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_even_high_regime_keeps_making" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords even, high, regime, keeps, making, bad in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_sweeping_optimality_level_zero_throu`

- Preferred role: `method`
- Cue keywords: `sweeping, optimality, level, zero, through, four, confirms, our, method, holds`
- Narration: Sweeping the optimality level from zero through four confirms that our method holds across degrees of expert optimality, recovering policies that can even beat the expert while keeping variance close to zero.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_sweeping_optimality_level_zero_throu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sweeping, optimality, level, zero, through, four in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_numbers_tell_clear_story`

- Preferred role: `content`
- Cue keywords: `numbers, tell, clear, story`
- Narration: The numbers tell a clear story.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_numbers_tell_clear_story" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords numbers, tell, clear, story in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_fully_optimal_expert_our_method`

- Preferred role: `method`
- Cue keywords: `fully, optimal, expert, our, method, reaches, star, metric, exactly, zero`
- Narration: With a fully optimal expert, our method reaches a Q star metric of exactly zero with zero variance, in both low and high data, compared to fifty nine point seven five for maximum likelihood and one hundred forty two for the plain posterior.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_fully_optimal_expert_our_method" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fully, optimal, expert, our, method, reaches in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_hardest_setting_epsilon_equals_four`

- Preferred role: `method`
- Cue keywords: `hardest, setting, epsilon, equals, four, high, score, eight, point, seven`
- Narration: At the hardest setting, epsilon equals four with high data, we score eight point seven nine, beating maximum likelihood's twenty point one one and roughly matching the near optimal expert.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_hardest_setting_epsilon_equals_four" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords hardest, setting, epsilon, equals, four, high in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_accuracy_deterministic_states_consta`

- Preferred role: `result`
- Cue keywords: `accuracy, deterministic, states, constant, one, hundred, percent, policy, variance, collapses`
- Narration: Accuracy on deterministic states is a constant one hundred percent, and the policy variance collapses from a standard deviation near fifty two down to essentially zero.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c4_accuracy_deterministic_states_consta" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords accuracy, deterministic, states, constant, one, hundred in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_clipping_bayesian_posterior_over_tra`

- Preferred role: `method`
- Cue keywords: `clipping, bayesian, posterior, over, transition, dynamics, constraints, derived, near, optimal`
- Narration: By clipping a Bayesian posterior over the transition dynamics with constraints derived from a near optimal expert, you obtain gradient free offline policies that are provably safe, can outperform the expert who generated the data, and carry dramatically lower variance than maximum likelihood.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_clipping_bayesian_posterior_over_tra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords clipping, bayesian, posterior, over, transition, dynamics in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_same_recipe_constraints_plus_uncerta`

- Preferred role: `method`
- Cue keywords: `same, recipe, constraints, plus, uncertainty, also, yields, ranking, actions, uncertain`
- Narration: The same recipe of constraints plus uncertainty also yields a ranking of actions in the uncertain states, making the learned policies more informative for high stakes planning such as clinical decision making.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_same_recipe_constraints_plus_uncerta" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords same, recipe, constraints, plus, uncertainty, also in title/desc so the matcher can verify semantic overlap.
