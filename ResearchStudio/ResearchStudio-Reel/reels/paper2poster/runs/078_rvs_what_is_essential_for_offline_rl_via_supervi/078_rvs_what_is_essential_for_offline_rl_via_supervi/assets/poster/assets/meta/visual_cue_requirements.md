# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_what_actually_essential_offline_rein`

- Preferred role: `content`
- Cue keywords: `what, actually, essential, offline, reinforcement, learning, done, via, supervised, learning`
- Narration: What is actually essential for offline reinforcement learning done via supervised learning?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_what_actually_essential_offline_rein" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, actually, essential, offline, reinforcement, learning in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_iclr_2022_scott_emmons_benjamin`

- Preferred role: `method`
- Cue keywords: `iclr, 2022, scott, emmons, benjamin, eysenbach, ilya, kostrikov, sergey, levine`
- Narration: This ICLR 2022 paper by Scott Emmons, Benjamin Eysenbach, Ilya Kostrikov, and Sergey Levine strips reinforcement learning via supervised learning, or RvS, down to its bare essentials.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_iclr_2022_scott_emmons_benjamin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords iclr, 2022, scott, emmons, benjamin, eysenbach in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_their_surprising_finding_plain_two_l`

- Preferred role: `method`
- Cue keywords: `their, surprising, finding, plain, two-layer, feedforward, network, trained, simply, maximize`
- Narration: Their surprising finding is that a plain two-layer feedforward network, trained simply to maximize likelihood, matches state-of-the-art results from far more complex methods built on temporal-difference learning or on Transformer sequence models.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_their_surprising_finding_plain_two_l" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords their, surprising, finding, plain, two-layer, feedforward in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_two_things_really_matter_they`

- Preferred role: `content`
- Cue keywords: `two, things, really, matter, they, show, choosing, capacity, carefully, choosing`
- Narration: The two things that really matter, they show, are choosing the model's capacity carefully and choosing what to condition on, goals or rewards. Everything else turns out to be optional.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c4_two_things_really_matter_they" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, things, really, matter, they, show in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_recent_work_showed_plain_supervised`

- Preferred role: `method`
- Cue keywords: `recent, work, showed, plain, supervised, learning, temporal-difference, bootstrapping, all, remarkably`
- Narration: Recent work showed that plain supervised learning, with no temporal-difference bootstrapping at all, can be remarkably effective for offline reinforcement learning. But the picture was muddy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_recent_work_showed_plain_supervised" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords recent, work, showed, plain, supervised, learning in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_different_papers_reached_contradicto`

- Preferred role: `method`
- Cue keywords: `different, papers, reached, contradictory, conclusions, about, what, actually, makes, these`
- Narration: Different papers reached contradictory conclusions about what actually makes these methods work: some emphasized advantage weighting, others reached for large Transformer sequence models.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_different_papers_reached_contradicto" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords different, papers, reached, contradictory, conclusions, about in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_core_question_asks_simple_yet`

- Preferred role: `title`
- Cue keywords: `core, question, asks, simple, yet, still, unanswered`
- Narration: The core question this paper asks is simple, yet still unanswered.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c3_core_question_asks_simple_yet" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, question, asks, simple, yet, still in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_when_does_supervised_learning_offlin`

- Preferred role: `method`
- Cue keywords: `when, does, supervised, learning, offline, actually, work, which, its, many`
- Narration: When does supervised learning for offline RL actually work, and which of its many algorithmic components are truly essential versus merely incidental complexity that could be stripped away without cost?
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_when_does_supervised_learning_offlin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, does, supervised, learning, offline, actually in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_value_based_methods_dominate_offline`

- Preferred role: `method`
- Cue keywords: `value-based, methods, dominate, offline, off-policy, they, come, appealing, theoretical, guarantees`
- Narration: Value-based methods dominate offline and off-policy RL, and they come with appealing theoretical guarantees.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_value_based_methods_dominate_offline" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords value-based, methods, dominate, offline, off-policy, they in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_but_practice_they_difficult_apply`

- Preferred role: `content`
- Cue keywords: `but, practice, they, difficult, apply, they, require, complex, tricks, stabilize`
- Narration: But in practice they are difficult to apply. They require complex tricks to stabilize learning and careful tuning of many interacting hyperparameters.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_but_practice_they_difficult_apply" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, practice, they, difficult, apply, they in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_attractive_alternative_convert_reinf`

- Preferred role: `content`
- Cue keywords: `attractive, alternative, convert, reinforcement, learning, problem, conditional, filtered, weighted, imitation`
- Narration: An attractive alternative is to convert the reinforcement learning problem into a conditional, filtered, or weighted imitation learning problem, using the insight that experience that is suboptimal for one task may be optimal for another.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_attractive_alternative_convert_reinf" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords attractive, alternative, convert, reinforcement, learning, problem in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_minimal_supervised_recipe_match_thes`

- Preferred role: `method`
- Cue keywords: `minimal, supervised, recipe, match, these, complex, value-based, methods, would, give`
- Narration: If a minimal supervised recipe can match these complex value-based methods, it would give practitioners a dependable field guide, and it would also reveal exactly where such supervised methods still break down.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_minimal_supervised_recipe_match_thes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords minimal, supervised, recipe, match, these, complex in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, contributions`
- Narration: The paper makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_does_not_propose_brand_new`

- Preferred role: `method`
- Cue keywords: `first, does, not, propose, brand-new, algorithm, instead, places, many, existing`
- Narration: First, it does not propose a brand-new algorithm; instead it places many existing goal-conditioned and reward-conditioned methods under one common framework, which the authors call RvS, reinforcement learning via supervised learning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_does_not_propose_brand_new" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, does, not, propose, brand-new, algorithm in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_through_extensive_experiments`

- Preferred role: `method`
- Cue keywords: `second, through, extensive, experiments, boils, these, methods, down, their, essential`
- Narration: Second, through extensive experiments it boils these methods down to their essential elements, showing that a two-layer feedforward network trained to maximize likelihood is competitive with far more complex state-of-the-art methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_through_extensive_experiments" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, through, extensive, experiments, boils, these in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_identifies_exactly_which_desig`

- Preferred role: `result`
- Cue keywords: `third, identifies, exactly, which, design, choices, matter, namely, capacity, regularization`
- Narration: Third, it identifies exactly which design choices matter, namely model capacity, regularization, and what you condition on, and it honestly probes the limits, showing that RvS is comparatively weak on purely random data.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c4_third_identifies_exactly_which_desig" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, identifies, exactly, which, design, choices in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_deliberately_simple_rvs_assum`

- Preferred role: `method`
- Cue keywords: `method, deliberately, simple, rvs, assumes, agent, markov, decision, process, trains`
- Narration: The method is deliberately simple. RvS assumes an agent in a Markov decision process and trains a policy conditioned on an outcome, which can be either a future goal state or an average future return.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_deliberately_simple_rvs_assum" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, deliberately, simple, rvs, assumes, agent in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_given_offline_dataset_trajectories_a`

- Preferred role: `method`
- Cue keywords: `given, offline, dataset, trajectories, applies, hindsight, relabeling, every, observed, action`
- Narration: Given an offline dataset of trajectories, it applies hindsight relabeling: every observed action becomes a demonstration for whatever outcome actually occurred later in that same trajectory.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_given_offline_dataset_trajectories_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords given, offline, dataset, trajectories, applies, hindsight in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_policy_itself_just_feedforward_multi`

- Preferred role: `content`
- Cue keywords: `policy, itself, just, feedforward, multilayer, perceptron, two, fully, connected, layers`
- Narration: The policy itself is just a feedforward multilayer perceptron with two fully connected layers, and the outcome is fed in simply by concatenating it onto the input state.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_policy_itself_just_feedforward_multi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords policy, itself, just, feedforward, multilayer, perceptron in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_maximizes_log_likelihood_observed_ac`

- Preferred role: `method`
- Cue keywords: `maximizes, log-likelihood, observed, actions, under, conditioned, policy, advantage, weighting, temporal-difference`
- Narration: Training then maximizes the log-likelihood of the observed actions under the conditioned policy. There is no advantage weighting, no temporal-difference bootstrapping, and no Transformer, only a maximum-likelihood objective over relabeled experience.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_maximizes_log_likelihood_observed_ac" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords maximizes, log-likelihood, observed, actions, under, conditioned in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_evaluation_deliberately_broad`

- Preferred role: `result`
- Cue keywords: `evaluation, deliberately, broad`
- Narration: The evaluation is deliberately broad.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_evaluation_deliberately_broad" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, deliberately, broad in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_d4rl_benchmark_authors_three_suites`

- Preferred role: `method`
- Cue keywords: `d4rl, benchmark, authors, three, suites, antmaze, which, requires, eight-degree-of-freedom, quadruped`
- Narration: On the D4RL benchmark, the authors use three suites: AntMaze, which requires an eight-degree-of-freedom quadruped to navigate a maze; Gym Locomotion, with HalfCheetah, Hopper, and Walker across random, medium, medium-replay, and medium-expert datasets; and Franka Kitchen, a nine-degree-of-freedom manipulation task built from human demonstrations.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_d4rl_benchmark_authors_three_suites" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords d4rl, benchmark, authors, three, suites, antmaze in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_they_also_gcsl_suite_goal_conditione`

- Preferred role: `method`
- Cue keywords: `they, also, gcsl, suite, goal-conditioned, tasks, including, two-dimensional, navigation, sawyer`
- Narration: They also use the GCSL suite of goal-conditioned tasks, including two-dimensional navigation, Sawyer arm control, Lunar Lander, and a robotic claw, which they adapt for offline RL by collecting data with a random policy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_they_also_gcsl_suite_goal_conditione" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, also, gcsl, suite, goal-conditioned, tasks in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_all_scores_normalized_zero_to_one_hu`

- Preferred role: `method`
- Cue keywords: `all, scores, normalized, zero-to-one-hundred, range, methods, compared, directly`
- Narration: All scores are normalized into a zero-to-one-hundred range so methods can be compared directly.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_all_scores_normalized_zero_to_one_hu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords all, scores, normalized, zero-to-one-hundred, range, methods in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_result_striking_nothing_but`

- Preferred role: `method`
- Cue keywords: `headline, result, striking, nothing, but, two-layer, feedforward, network, trained, maximum`
- Narration: The headline result is striking. Using nothing but a two-layer feedforward network trained with maximum likelihood, RvS reaches state-of-the-art performance across several suites.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_headline_result_striking_nothing_but" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, result, striking, nothing, but, two-layer in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_antmaze_goal_conditioned_rvs_scores`

- Preferred role: `method`
- Cue keywords: `antmaze, goal-conditioned, rvs, scores, fifty-three, point, five, average, edging, out`
- Narration: On AntMaze, goal-conditioned RvS scores fifty-three point five on average, edging out the best value-based baseline at fifty point six.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_antmaze_goal_conditioned_rvs_scores" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords antmaze, goal-conditioned, rvs, scores, fifty-three, point in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_franka_kitchen_reaches_fifty_four_gc`

- Preferred role: `method`
- Cue keywords: `franka, kitchen, reaches, fifty-four, gcsl, suite, scores, sixty-two, beating, online`
- Narration: On Franka Kitchen it reaches fifty-four. On the GCSL suite it scores sixty-two, beating the online GCSL method at fifty-eight, despite using only offline data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_franka_kitchen_reaches_fifty_four_gc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords franka, kitchen, reaches, fifty-four, gcsl, suite in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_gym_locomotion_reward_conditioned_rv`

- Preferred role: `method`
- Cue keywords: `gym, locomotion, reward-conditioned, rvs, matches, decision, transformer, while, simple, multilayer`
- Narration: And on Gym Locomotion, reward-conditioned RvS matches Decision Transformer while using a simple multilayer perceptron instead of a large Transformer. Even on stitching tasks, long thought to demand dynamic programming, goal-conditioned RvS keeps pace.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_gym_locomotion_reward_conditioned_rv" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gym, locomotion, reward-conditioned, rvs, matches, decision in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablations_pin_down_what_actually`

- Preferred role: `figure`
- Cue keywords: `ablations, pin, down, what, actually, matters, first, capacity, best, architectures`
- Narration: The ablations pin down what actually matters. First, capacity: the best architectures are notably larger than those used in standard online RL or imitation learning, and widening the network up to about a thousand hidden units generally helps.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c1_ablations_pin_down_what_actually" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, pin, down, what, actually, matters in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_second_regularization_dropout_not_un`

- Preferred role: `method`
- Cue keywords: `second, regularization, dropout, not, universally, good, boosts, performance, small, human-demonstration`
- Narration: Second, regularization: dropout is not universally good. It boosts performance on the small, human-demonstration kitchen-complete dataset, but it hurts on hopper-medium-expert and on antmaze-medium-play.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_second_regularization_dropout_not_un" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, regularization, dropout, not, universally, good in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_third_output_distribution_categorica`

- Preferred role: `method`
- Cue keywords: `third, output, distribution, categorical, distribution, over, discretized, actions, matches, beats`
- Narration: Third, the output distribution: a categorical distribution over discretized actions matches or beats a unimodal Gaussian across the GCSL tasks, which fits the broader theme that more policy capacity helps.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_third_output_distribution_categorica" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, output, distribution, categorical, distribution, over in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_finally_validation_loss_correlates_o`

- Preferred role: `figure`
- Cue keywords: `finally, validation, loss, correlates, only, loosely, final, performance, not, reliable`
- Narration: Finally, validation loss correlates only loosely with final performance, so it is not a reliable tuning signal on its own.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c4_finally_validation_loss_correlates_o" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finally, validation, loss, correlates, only, loosely in title/desc so the matcher can verify semantic overlap.

## Slide 09: takeaway

Heading: Takeaway

### Cue 1: `cue_s09_c1_takeaway_essentially_practitioner_fi`

- Preferred role: `method`
- Cue keywords: `takeaway, essentially, practitioner, field, guide, you, not, need, advantage, weighting`
- Narration: The takeaway is essentially a practitioner's field guide. You do not need advantage weighting or a Transformer to do offline RL by supervised learning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_takeaway_essentially_practitioner_fi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, essentially, practitioner, field, guide, you in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_plain_two_layer_feedforward_network`

- Preferred role: `method`
- Cue keywords: `plain, two-layer, feedforward, network, trained, simply, maximize, likelihood, competitive, state`
- Narration: A plain two-layer feedforward network, trained simply to maximize likelihood, is competitive with the state of the art, as long as you get two things right: carefully tune the model's capacity and its regularization, and choose the right thing to condition on, goals or rewards.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_plain_two_layer_feedforward_network" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords plain, two-layer, feedforward, network, trained, simply in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_concrete_recipe_grow_network_width`

- Preferred role: `content`
- Cue keywords: `concrete, recipe, grow, network, width, until, performance, saturates, add, little`
- Narration: The concrete recipe is to grow the network width until performance saturates, then add a little dropout.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_concrete_recipe_grow_network_width" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords concrete, recipe, grow, network, width, until in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_honest_caveat_purely_random_temporal`

- Preferred role: `method`
- Cue keywords: `honest, caveat, purely, random, temporal-difference, methods, still, win, which, authors`
- Narration: The honest caveat is that on purely random data, temporal-difference methods still win, which the authors flag as an open problem for future work.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_honest_caveat_purely_random_temporal" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords honest, caveat, purely, random, temporal-difference, methods in title/desc so the matcher can verify semantic overlap.
