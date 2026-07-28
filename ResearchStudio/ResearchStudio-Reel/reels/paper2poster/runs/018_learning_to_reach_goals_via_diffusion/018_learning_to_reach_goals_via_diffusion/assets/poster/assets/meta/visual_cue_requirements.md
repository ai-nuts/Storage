# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_what_reaching_goal_just_reverse`

- Preferred role: `content`
- Cue keywords: `what, reaching, goal, just, reverse, diffusion, process`
- Narration: What if reaching a goal were just the reverse of a diffusion process?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_what_reaching_goal_just_reverse" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, reaching, goal, just, reverse, diffusion in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_icml_2024_vineet_jain_siamak`

- Preferred role: `content`
- Cue keywords: `icml, 2024, vineet, jain, siamak, ravanbakhsh, mcgill, university, mila, reframe`
- Narration: In this ICML 2024 paper, Vineet Jain and Siamak Ravanbakhsh from McGill University and Mila reframe goal-conditioned reinforcement learning through the lens of denoising diffusion.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_icml_2024_vineet_jain_siamak" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords icml, 2024, vineet, jain, siamak, ravanbakhsh in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_their_method_called_merlin_builds`

- Preferred role: `method`
- Cue keywords: `their, method, called, merlin, builds, trajectories, drift, away, goal, states`
- Narration: Their method, called Merlin, builds trajectories that drift away from goal states and then trains a policy to reverse that drift, exactly as a diffusion model denoises noise back into data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_their_method_called_merlin_builds" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords their, method, called, merlin, builds, trajectories in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_result_value_function_free_approach`

- Preferred role: `method`
- Cue keywords: `result, value-function-free, approach, reaches, goals, arbitrary, starting, states, needs, only`
- Narration: The result is a value-function-free approach that reaches goals from arbitrary starting states, needs only a single denoising step per environment step, and runs an order of magnitude faster than other diffusion-based reinforcement learning methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_result_value_function_free_approach" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, value-function-free, approach, reaches, goals, arbitrary in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_goal_conditioned_reinforcement_learn`

- Preferred role: `content`
- Cue keywords: `goal-conditioned, reinforcement, learning, aims, train, single, agent, reach, any, target`
- Narration: Goal-conditioned reinforcement learning aims to train a single agent that can reach any target state within an environment, using only a sparse reward of one when the goal is reached and zero otherwise.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_goal_conditioned_reinforcement_learn" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords goal-conditioned, reinforcement, learning, aims, train, single in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_offline_setting_agent_must_learn`

- Preferred role: `content`
- Cue keywords: `offline, setting, agent, must, learn, purely, pre-collected, dataset, without, any`
- Narration: In the offline setting, the agent must learn purely from a pre-collected dataset, without any further interaction.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_offline_setting_agent_must_learn" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords offline, setting, agent, must, learn, purely in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_trouble_most_methods_rely_estimating`

- Preferred role: `method`
- Cue keywords: `trouble, most, methods, rely, estimating, value, function, offline, goal-conditioned, setting`
- Narration: The trouble is that most methods rely on estimating a value function, and in the offline goal-conditioned setting this estimate is fragile.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_trouble_most_methods_rely_estimating" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trouble, most, methods, rely, estimating, value in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_policies_generate_actions_not_presen`

- Preferred role: `result`
- Cue keywords: `policies, generate, actions, not, present, value, estimates, those, actions, wrong`
- Narration: Policies generate actions not present in the data, the value estimates for those actions are wrong, and these errors compound over time until the policy diverges. Sparse binary rewards only make the estimation problem harder.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c4_policies_generate_actions_not_presen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords policies, generate, actions, not, present, value in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_diffusion_models_become_powerful_cla`

- Preferred role: `method`
- Cue keywords: `diffusion, models, become, powerful, class, generative, models, they, work, defining`
- Narration: Diffusion models have become a powerful class of generative models. They work by defining a forward process that gradually destroys data into Gaussian noise, then learning a reverse process that denoises noise back into realistic samples, without ever estimating a value function.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_diffusion_models_become_powerful_cla" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords diffusion, models, become, powerful, class, generative in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_authors_ask_simple_question_what`

- Preferred role: `method`
- Cue keywords: `authors, ask, simple, question, what, treat, goal, states, distribution, want`
- Narration: The authors ask a simple question: what if we treat goal states as the data distribution we want to model?
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_authors_ask_simple_question_what" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, ask, simple, question, what, treat in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_diffusion_noise_walks_away_manifold`

- Preferred role: `method`
- Cue keywords: `diffusion, noise, walks, away, manifold, goal-conditioned, reinforcement, learning, construct, trajectories`
- Narration: In a diffusion model, noise walks away from the data manifold; in goal-conditioned reinforcement learning, we can construct trajectories that walk away from potential goals.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_diffusion_noise_walks_away_manifold" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords diffusion, noise, walks, away, manifold, goal-conditioned in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_learning_reverse_those_deviations_di`

- Preferred role: `method`
- Cue keywords: `learning, reverse, those, deviations, directly, analogous, learning, score, function, sidesteps`
- Narration: Learning to reverse those deviations is directly analogous to learning the score function, and it sidesteps the value-estimation problems that plague offline methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_learning_reverse_those_deviations_di" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords learning, reverse, those, deviations, directly, analogous in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_main_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, main, contributions`
- Narration: The paper makes three main contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_main_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, main, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_presents_merlin_fresh_perspect`

- Preferred role: `content`
- Cue keywords: `first, presents, merlin, fresh, perspective, casts, goal-conditioned, reinforcement, learning, reverse`
- Narration: First, it presents Merlin, a fresh perspective that casts goal-conditioned reinforcement learning as a reverse diffusion process operating directly over the state space of the environment.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_first_presents_merlin_fresh_perspect" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, presents, merlin, fresh, perspective, casts in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_proves_reverse_process_learne`

- Preferred role: `content`
- Cue keywords: `second, proves, reverse, process, learned, simple, goal-conditioned, behavior, cloning, hindsight`
- Narration: Second, it proves that this reverse process can be learned by simple goal-conditioned behavior cloning with hindsight relabeling, eliminating the need for a value function entirely.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_second_proves_reverse_process_learne" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, proves, reverse, process, learned, simple in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_develops_three_ways_construct`

- Preferred role: `method`
- Cue keywords: `third, develops, three, ways, construct, forward, goal-departing, trajectories, fixed, heuristic`
- Narration: Third, it develops three ways to construct the forward, goal-departing trajectories: a fixed heuristic version, a parametric learned forward model called Merlin-P, and a non-parametric version called Merlin-NP that stitches together nearby states in a learned latent space.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_third_develops_three_ways_construct" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, develops, three, ways, construct, forward in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_how_merlin_works_take_trajectory`

- Preferred role: `figure`
- Cue keywords: `how, merlin, works, take, trajectory, offline, dataset, read, backwards, starting`
- Narration: Here is how Merlin works. Take a trajectory from the offline dataset and read it backwards, starting from its final goal state.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c1_how_merlin_works_take_trajectory" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, merlin, works, take, trajectory, offline in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_applying_forward_diffusion_transform`

- Preferred role: `content`
- Cue keywords: `applying, forward, diffusion, transformation, step, produces, states, drift, progressively, away`
- Narration: Applying a forward diffusion transformation at each step produces states that drift progressively away from the goal, exactly like adding noise in an image diffusion model. Merlin then trains a goal-conditioned policy to reverse this drift, step by step, back toward the goal.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_applying_forward_diffusion_transform" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords applying, forward, diffusion, transformation, step, produces in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_key_theoretical_result_maximizing_li`

- Preferred role: `result`
- Cue keywords: `key, theoretical, result, maximizing, likelihood, goal, states, under, reverse, process`
- Narration: The key theoretical result is that maximizing the likelihood of the goal states under this reverse process is equivalent to plain behavior cloning on the relabeled data, so no value function is ever needed. Because the state space itself is the diffusion space, the policy needs only one denoising iteration for each environment step, instead of the many iterations typical diffusion policies require.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c3_key_theoretical_result_maximizing_li" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, theoretical, result, maximizing, likelihood, goal in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_authors_offer_three_ways_build`

- Preferred role: `method`
- Cue keywords: `authors, offer, three, ways, build, goal-departing, trajectories, fixed, construction, learned`
- Narration: The authors offer three ways to build the goal-departing trajectories: a fixed construction, a learned parametric forward model in Merlin-P, and a non-parametric model in Merlin-NP that connects nearby states through nearest-neighbor stitching in a learned latent space.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_authors_offer_three_ways_build" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, offer, three, ways, build, goal-departing in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_authors_evaluate_merlin_standard_off`

- Preferred role: `result`
- Cue keywords: `authors, evaluate, merlin, standard, offline, goal-conditioned, benchmark, ten, control, tasks`
- Narration: The authors evaluate Merlin on a standard offline goal-conditioned benchmark of ten control tasks, ranging from simple point navigation and reacher tasks to harder Fetch manipulation tasks like pushing, picking, and sliding, plus the high-dimensional HandReach task.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_authors_evaluate_merlin_standard_off" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, evaluate, merlin, standard, offline, goal-conditioned in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_every_task_sparse_binary_reward`

- Preferred role: `figure`
- Cue keywords: `every, task, sparse, binary, reward, maximum, trajectory, length, fifty, steps`
- Narration: Every task uses a sparse binary reward and a maximum trajectory length of fifty steps.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s06_c2_every_task_sparse_binary_reward" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords every, task, sparse, binary, reward, maximum in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_task_comes_two_flavors_expert`

- Preferred role: `method`
- Cue keywords: `task, comes, two, flavors, expert, dataset, collected, trained, policy, added`
- Narration: Each task comes in two flavors: an expert dataset collected by a trained policy with added noise for diversity, and a random dataset collected by sampling random actions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_task_comes_two_flavors_expert" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords task, comes, two, flavors, expert, dataset in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_they_test_both_low_dimensional_state`

- Preferred role: `result`
- Cue keywords: `they, test, both, low-dimensional, state, observations, high-dimensional, pixel, observations, average`
- Narration: They test both low-dimensional state observations and high-dimensional pixel observations, and average all results over ten random seeds.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_they_test_both_low_dimensional_state" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, test, both, low-dimensional, state, observations in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_results_strong_across_board_basic`

- Preferred role: `method`
- Cue keywords: `results, strong, across, board, basic, version, merlin, already, outperforms, baselines`
- Narration: The results are strong across the board. The basic version of Merlin already outperforms the baselines on most tasks, and the two improved variants, Merlin-P and Merlin-NP, push performance further to achieve the highest discounted returns on most tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_results_strong_across_board_basic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, strong, across, board, basic, version in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_measured_average_rank_across_all`

- Preferred role: `method`
- Cue keywords: `measured, average, rank, across, all, ten, methods, ten, tasks, merlin-np`
- Narration: Measured by average rank across all ten methods and ten tasks, Merlin-NP comes out on top, with an average rank around one point seven on state observations and about one point two five on pixel observations.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_measured_average_rank_across_all" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords measured, average, rank, across, all, ten in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_crucially_because_merlin_performs_on`

- Preferred role: `method`
- Cue keywords: `crucially, because, merlin, performs, only, single, denoising, step, per, environment`
- Narration: Crucially, because Merlin performs only a single denoising step per environment step, its training and inference are roughly an order of magnitude faster than the other diffusion-based methods like Decision Diffuser and BESO.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_crucially_because_merlin_performs_on" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, because, merlin, performs, only, single in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_high_dimensional_pixel_observations`

- Preferred role: `content`
- Cue keywords: `high-dimensional, pixel, observations, efficiency, gap, becomes, even, more, pronounced`
- Narration: With high-dimensional pixel observations, that efficiency gap becomes even more pronounced.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_high_dimensional_pixel_observations" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords high-dimensional, pixel, observations, efficiency, gap, becomes in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_authors_study_two_key_hyperparameter`

- Preferred role: `result`
- Cue keywords: `authors, study, two, key, hyperparameters, hindsight, relabeling, ratio, evaluation, time`
- Narration: The authors study two key hyperparameters: the hindsight relabeling ratio and the evaluation time horizon, which sets how far ahead the policy aims. Across all tasks, conditioning on a time horizon clearly beats leaving it out.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c1_authors_study_two_key_hyperparameter" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, study, two, key, hyperparameters, hindsight in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_best_value_depends_task_easier`

- Preferred role: `title`
- Cue keywords: `best, value, depends, task, easier, tasks, like, pointreach, well, short`
- Narration: The best value depends on the task: easier tasks like PointReach do well with a short horizon of one or five steps, while harder tasks benefit from longer horizons because they need more steps to reach the goal.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s08_c2_best_value_depends_task_easier" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords best, value, depends, task, easier, tasks in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_handreach_task_particularly_sensitiv`

- Preferred role: `content`
- Cue keywords: `handreach, task, particularly, sensitive, working, dramatically, better, horizon, one, any`
- Narration: The HandReach task is particularly sensitive, working dramatically better with a horizon of one than with any longer setting.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_handreach_task_particularly_sensitiv" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords handreach, task, particularly, sensitive, working, dramatically in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_these_trends_visualized_heatmaps_ret`

- Preferred role: `result`
- Cue keywords: `these, trends, visualized, heatmaps, returns, across, horizons, both, expert, random`
- Narration: These trends are visualized as heatmaps of returns across horizons for both expert and random datasets.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_these_trends_visualized_heatmaps_ret" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, trends, visualized, heatmaps, returns, across in title/desc so the matcher can verify semantic overlap.

## Slide 09: takeaway

Heading: Takeaway

### Cue 1: `cue_s09_c1_big_takeaway_goal_conditioned_reinfo`

- Preferred role: `takeaway`
- Cue keywords: `big, takeaway, goal-conditioned, reinforcement, learning, reframed, reverse, diffusion, process, reframing`
- Narration: The big takeaway is that goal-conditioned reinforcement learning can be reframed as the reverse of a diffusion process, and that this reframing makes the problem remarkably simple.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s09_c1_big_takeaway_goal_conditioned_reinfo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords big, takeaway, goal-conditioned, reinforcement, learning, reframed in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_constructing_trajectories_walk_away`

- Preferred role: `method`
- Cue keywords: `constructing, trajectories, walk, away, goals, learning, reverse, them, merlin, reduces`
- Narration: By constructing trajectories that walk away from goals and learning to reverse them, Merlin reduces goal-reaching to plain behavior cloning, with no value function to estimate and no instability to fight.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_constructing_trajectories_walk_away" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords constructing, trajectories, walk, away, goals, learning in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_matches_beats_state_of_the_art_metho`

- Preferred role: `method`
- Cue keywords: `matches, beats, state-of-the-art, methods, across, ten, tasks, yet, runs, order`
- Narration: It matches or beats state-of-the-art methods across ten tasks, yet runs an order of magnitude faster than other diffusion-based approaches.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_matches_beats_state_of_the_art_metho" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords matches, beats, state-of-the-art, methods, across, ten in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_suggests_diffusion_state_space_simpl`

- Preferred role: `content`
- Cue keywords: `suggests, diffusion, state, space, simple, scalable, practical, new, direction, sequential`
- Narration: This suggests that diffusion in the state space is a simple, scalable, and practical new direction for sequential decision making.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_suggests_diffusion_state_space_simpl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords suggests, diffusion, state, space, simple, scalable in title/desc so the matcher can verify semantic overlap.
