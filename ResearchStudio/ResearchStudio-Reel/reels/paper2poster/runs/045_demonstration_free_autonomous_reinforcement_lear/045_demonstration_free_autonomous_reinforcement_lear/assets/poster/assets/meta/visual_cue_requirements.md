# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_reinforcement_learning_mastered_comp`

- Preferred role: `content`
- Cue keywords: `reinforcement, learning, mastered, complex, skills, but, almost, always, assuming, environment`
- Narration: Reinforcement learning has mastered complex skills, but almost always by assuming the environment resets to a fixed initial state after every episode.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_reinforcement_learning_mastered_comp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reinforcement, learning, mastered, complex, skills, but in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_real_world_especially_robotics_those`

- Preferred role: `content`
- Cue keywords: `real, world, especially, robotics, those, resets, expensive, requiring, human, supervision`
- Narration: In the real world, especially in robotics, those resets are expensive, requiring human supervision or scripted routines. This work, presented at ICML 2023 by Jigang Kim, Daesol Cho, and H.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_real_world_especially_robotics_those" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords real, world, especially, robotics, those, resets in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_jin_kim_seoul_national_university`

- Preferred role: `method`
- Cue keywords: `jin, kim, seoul, national, university, tackles, autonomous, reinforcement, learning, without`
- Narration: Jin Kim from Seoul National University, tackles autonomous reinforcement learning without any resets and, crucially, without any demonstrations. Their method, called IBC, combines an auxiliary agent that fades away as the main agent improves with a bidirectional goal curriculum built on optimal transport.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_jin_kim_seoul_national_university" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords jin, kim, seoul, national, university, tackles in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_result_state_of_the_art_performance`

- Preferred role: `method`
- Cue keywords: `result, state-of-the-art, performance, non-episodic, benchmarks, matching, methods, rely, expert, even`
- Narration: The result is state-of-the-art performance on non-episodic benchmarks, matching methods that rely on expert data and even approaching episodic oracle reinforcement learning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_result_state_of_the_art_performance" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, state-of-the-art, performance, non-episodic, benchmarks, matching in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_standard_reinforcement_learning_quie`

- Preferred role: `content`
- Cue keywords: `standard, reinforcement, learning, quietly, assumes, something, rarely, holds, outside, simulator`
- Narration: Standard reinforcement learning quietly assumes something that rarely holds outside a simulator: that at the end of every episode, the environment magically resets to its starting state.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_standard_reinforcement_learning_quie" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords standard, reinforcement, learning, quietly, assumes, something in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_physical_robot_resetting_means_human`

- Preferred role: `method`
- Cue keywords: `physical, robot, resetting, means, human, intervention, scripted, reset, policies, custom`
- Narration: For a physical robot, resetting means human intervention, scripted reset policies, or custom rigs, all of which are slow and costly. Autonomous reinforcement learning tries to remove that assumption by learning from one long uninterrupted stream of experience.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_physical_robot_resetting_means_human" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords physical, robot, resetting, means, human, intervention in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_but_existing_autonomous_methods_chea`

- Preferred role: `method`
- Cue keywords: `but, existing, autonomous, methods, cheat, different, way, they, rely, prior`
- Narration: But the existing autonomous methods cheat in a different way: they rely on prior data, like expert demonstrations or example states of interest, and they struggle badly in environments where the interactions that matter are sparse and almost never happen by chance.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_but_existing_autonomous_methods_chea" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, existing, autonomous, methods, cheat, different in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_what_been_missing_agent_learns`

- Preferred role: `method`
- Cue keywords: `what, been, missing, agent, learns, truly, scratch, resets, demonstrations`
- Narration: What has been missing is an agent that learns truly from scratch, with no resets and no demonstrations.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_what_been_missing_agent_learns" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, been, missing, agent, learns, truly in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_why_demonstration_free_autonomous_le`

- Preferred role: `method`
- Cue keywords: `why, demonstration-free, autonomous, learning, hard, non-episodic, setting, untrained, forward, agent`
- Narration: Why is demonstration-free autonomous learning so hard? In the non-episodic setting, an untrained forward agent wanders off to arbitrary states, so every new attempt starts from a wildly different, often useless initial condition.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_why_demonstration_free_autonomous_le" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords why, demonstration-free, autonomous, learning, hard, non-episodic in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_instability_makes_learning_collapse`

- Preferred role: `method`
- Cue keywords: `instability, makes, learning, collapse, prior, work, patched, ways, reintroduce, human`
- Narration: That instability makes learning collapse. Prior work patched this in ways that reintroduce human effort. Some methods still ask for occasional manual resets. Others only succeed when the useful interactions happen to occur by chance.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_instability_makes_learning_collapse" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instability, makes, learning, collapse, prior, work in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_two_most_directly_comparable_methods`

- Preferred role: `method`
- Cue keywords: `two, most, directly, comparable, methods, vaprl, medal, both, lean, demonstration`
- Narration: And the two most directly comparable methods, VaPRL and MEDAL, both lean on demonstration data, either to seed a subgoal curriculum or to define what the backward agent should return to.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_two_most_directly_comparable_methods" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, most, directly, comparable, methods, vaprl in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_motivation_build_agent_provides_its`

- Preferred role: `content`
- Cue keywords: `motivation, build, agent, provides, its, own, anchor, its, own, curriculum`
- Narration: The motivation here is to build an agent that provides its own anchor and its own curriculum, using nothing but the experience it collects.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_motivation_build_agent_provides_its" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords motivation, build, agent, provides, its, own in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_core_contribution_method_called_ibc`

- Preferred role: `method`
- Cue keywords: `core, contribution, method, called, ibc, short, implicit, bidirectional, curriculum, far`
- Narration: The core contribution is a method called IBC, short for Implicit and Bidirectional Curriculum. As far as the authors know, it is the first algorithm for non-episodic reinforcement learning that consistently learns without any manual resets and without any demonstrations. It brings together two ideas.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_core_contribution_method_called_ibc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, contribution, method, called, ibc, short in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_conditionally_activated_auxili`

- Preferred role: `content`
- Cue keywords: `first, conditionally, activated, auxiliary, agent, forms, implicit, curriculum, helps, main`
- Narration: The first is a conditionally activated auxiliary agent that forms an implicit curriculum: it helps the main agent early on and then gradually disappears as the main agent becomes capable.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_first_conditionally_activated_auxili" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, conditionally, activated, auxiliary, agent, forms in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_bidirectional_goal_curriculum`

- Preferred role: `content`
- Cue keywords: `second, bidirectional, goal, curriculum, grounded, optimal, transport, automatically, proposes, intermediate`
- Narration: The second is a bidirectional goal curriculum, grounded in optimal transport, that automatically proposes intermediate goals for both the forward and the backward directions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_second_bidirectional_goal_curriculum" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, bidirectional, goal, curriculum, grounded, optimal in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_together_these_let_agent_bootstrap`

- Preferred role: `method`
- Cue keywords: `together, these, let, agent, bootstrap, its, own, signal, across, six`
- Narration: Together these let the agent bootstrap its own training signal, and across six sparse-reward environments IBC beats methods that rely on expert data while approaching the performance of an idealized episodic oracle.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_together_these_let_agent_bootstrap" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, these, let, agent, bootstrap, its in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_how_ibc_works_during_agent`

- Preferred role: `method`
- Cue keywords: `how, ibc, works, during, agent, constantly, alternates, between, two, roles`
- Narration: Here is how IBC works. During training the agent constantly alternates between two roles. The forward agent tries to accomplish the task. The auxiliary agent brings it back toward a set of target initial states so it can practice again.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_how_ibc_works_during_agent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, ibc, works, during, agent, constantly in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_key_trick_auxiliary_agent_activated`

- Preferred role: `content`
- Cue keywords: `key, trick, auxiliary, agent, activated, only, when, forward, agent, fails`
- Narration: The key trick is that the auxiliary agent is activated only when the forward agent fails, so as the forward agent gets better, the auxiliary agent naturally steps in less and less. That is the implicit curriculum. On top of this sits the explicit, bidirectional goal curriculum.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_key_trick_auxiliary_agent_activated" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, trick, auxiliary, agent, activated, only in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_rather_relying_demonstrations_ibc_sa`

- Preferred role: `method`
- Cue keywords: `rather, relying, demonstrations, ibc, samples, candidate, states, its, own, replay`
- Narration: Rather than relying on demonstrations, IBC samples candidate states from its own replay buffer and frames curriculum generation as an optimal transport problem, specifically a Wasserstein Barycenter augmented with a value bias term. It solves the resulting bipartite matching with a Minimum Cost Maximum Flow algorithm, producing K intermediate goals for the forward agent and K for the auxiliary agent.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_rather_relying_demonstrations_ibc_sa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rather, relying, demonstrations, ibc, samples, candidate in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_lipschitz_continuity_assumption_lets`

- Preferred role: `method`
- Cue keywords: `lipschitz-continuity, assumption, lets, method, relax, true, objective, tractable, lower, bound`
- Narration: A Lipschitz-continuity assumption lets the method relax the true objective into a tractable lower bound, and standard Soft Actor-Critic handles the policy updates. Remarkably, defining the target distribution needs only about ten sample states, and sometimes just one, rather than thousands of demonstration transitions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_lipschitz_continuity_assumption_lets" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lipschitz-continuity, assumption, lets, method, relax, true in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_test_ibc_authors_assembled_six`

- Preferred role: `method`
- Cue keywords: `test, ibc, authors, assembled, six, sparse-reward, environments, spanning, both, manipulation`
- Narration: To test IBC, the authors assembled six sparse-reward environments spanning both manipulation and locomotion. Two of them, Tabletop Manipulation and Sawyer Door, come from EARL, an established benchmark for autonomous reinforcement learning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_test_ibc_authors_assembled_six" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords test, ibc, authors, assembled, six, sparse-reward in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_other_four_fetch_pick_place`

- Preferred role: `title`
- Cue keywords: `other, four, fetch, pick, place, fetch, push, fetch, reach, point-u-maze`
- Narration: The other four are Fetch Pick and Place, Fetch Push, Fetch Reach, and Point-U-Maze, which are standard MuJoCo-based OpenAI Gym tasks that the authors modified for the reset-free, non-episodic setting.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s06_c2_other_four_fetch_pick_place" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords other, four, fetch, pick, place, fetch in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_evaluation_follows_earl_protocol_age`

- Preferred role: `result`
- Cue keywords: `evaluation, follows, earl, protocol, agent, spawned, once, interacts, continually, reset`
- Narration: Evaluation follows the EARL protocol: the agent is spawned once, interacts continually, and is reset only rarely, after hundreds of thousands of steps.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c3_evaluation_follows_earl_protocol_age" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, follows, earl, protocol, agent, spawned in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_performance_measured_deployed_policy`

- Preferred role: `result`
- Cue keywords: `performance, measured, deployed, policy, evaluation, metric, reported, ten-thousand-step, intervals, averaged`
- Narration: Performance is measured as the deployed policy evaluation metric, reported at ten-thousand-step intervals and averaged across five random seeds.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_performance_measured_deployed_policy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords performance, measured, deployed, policy, evaluation, metric in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_result_ibc_reaches_state_of`

- Preferred role: `method`
- Cue keywords: `headline, result, ibc, reaches, state-of-the-art, success, rates, across, all, six`
- Narration: The headline result is that IBC reaches state-of-the-art success rates across all six environments, and it does so without a single demonstration.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_headline_result_ibc_reaches_state_of" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, result, ibc, reaches, state-of-the-art, success in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_outperforms_vaprl_medal_two_strong`

- Preferred role: `method`
- Cue keywords: `outperforms, vaprl, medal, two, strong, baselines, actually, near-expert, demonstration, many`
- Narration: It outperforms VaPRL and MEDAL, two strong baselines that actually use near-expert demonstration data, and in many tasks its success rate is comparable to the oracle: a standard reinforcement learning agent trained in the easy, fully-resettable episodic setting.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_outperforms_vaprl_medal_two_strong" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords outperforms, vaprl, medal, two, strong, baselines in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_demonstration_based_baselines_especi`

- Preferred role: `method`
- Cue keywords: `demonstration-based, baselines, especially, falter, fetch, environments, where, task-relevant, interactions, sparse`
- Narration: The demonstration-based baselines especially falter in the Fetch environments, where the task-relevant interactions are sparse and the evaluation goals are spread across a whole region rather than a few discrete points.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_demonstration_based_baselines_especi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords demonstration-based, baselines, especially, falter, fetch, environments in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_when_vaprl_stripped_its_demonstratio`

- Preferred role: `method`
- Cue keywords: `when, vaprl, stripped, its, demonstrations, fair, comparison, its, performance, drops`
- Narration: And when VaPRL is stripped of its demonstrations for a fair comparison, its performance drops noticeably, underscoring just how much the prior methods depend on that extra data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_when_vaprl_stripped_its_demonstratio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, vaprl, stripped, its, demonstrations, fair in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablation_study_peels_method_apart`

- Preferred role: `method`
- Cue keywords: `ablation, study, peels, method, apart, show, both, pieces, earn, their`
- Narration: The ablation study peels the method apart to show that both pieces earn their keep. First, removing the bidirectional curriculum causes a consistent drop in performance, demonstrating the value of gradually guiding the agent from easy initial states and goals to harder ones.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_ablation_study_peels_method_apart" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablation, study, peels, method, apart, show in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_further_removing_auxiliary_agent_whi`

- Preferred role: `method`
- Cue keywords: `further, removing, auxiliary, agent, which, reduces, method, naive, reset-free, reinforcement`
- Narration: Then, further removing the auxiliary agent, which reduces the method to naive reset-free reinforcement learning, causes an additional and larger drop, particularly in the object-manipulation tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_further_removing_auxiliary_agent_whi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords further, removing, auxiliary, agent, which, reduces in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_gains_task_dependent_bidirectional_c`

- Preferred role: `result`
- Cue keywords: `gains, task-dependent, bidirectional, curriculum, matters, little, simple, tabletop, manipulation, environment`
- Narration: The gains are task-dependent: the bidirectional curriculum matters little in the simple Tabletop Manipulation environment, and the auxiliary agent is less helpful in Point-U-Maze, where the start is already far from the goal.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c3_gains_task_dependent_bidirectional_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gains, task-dependent, bidirectional, curriculum, matters, little in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_authors_also_confirm_implicit_curric`

- Preferred role: `method`
- Cue keywords: `authors, also, confirm, implicit, curriculum, behaves, intended, fraction, episodes, auxiliary`
- Narration: The authors also confirm the implicit curriculum behaves as intended: the fraction of episodes the auxiliary agent intervenes in falls toward zero once the forward agent is fully trained.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_authors_also_confirm_implicit_curric" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, also, confirm, implicit, curriculum, behaves in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact_ibc`

- Preferred role: `result`
- Cue keywords: `few, numbers, capture, impact, ibc, tested, six, sparse-reward, environments, two`
- Narration: A few numbers capture the impact. IBC was tested on six sparse-reward environments, two from the established EARL benchmark and four adapted MuJoCo tasks, each run over five random seeds.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact_ibc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact, ibc, tested in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_define_its_target_distribution_needs`

- Preferred role: `method`
- Cue keywords: `define, its, target, distribution, needs, only, about, ten, example, states`
- Narration: To define its target distribution, it needs only about ten example states, and sometimes just one, compared with the thousands of demonstration transitions that prior autonomous methods require.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_define_its_target_distribution_needs" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords define, its, target, distribution, needs, only in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_despite_zero_demonstrations_zero_man`

- Preferred role: `method`
- Cue keywords: `despite, zero, demonstrations, zero, manual, resets, reaches, success, rates, comparable`
- Narration: And despite using zero demonstrations and zero manual resets, it reaches success rates comparable to an oracle agent trained in the far easier episodic setting.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_despite_zero_demonstrations_zero_man" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords despite, zero, demonstrations, zero, manual, resets in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_short_none_usual_crutches_roughly`

- Preferred role: `content`
- Cue keywords: `short, none, usual, crutches, roughly, same, performance`
- Narration: In short: none of the usual crutches, and roughly the same performance.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_short_none_usual_crutches_roughly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords short, none, usual, crutches, roughly, same in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple_remember_ibc_shows`

- Preferred role: `method`
- Cue keywords: `takeaway, simple, remember, ibc, shows, agent, learn, robotic, manipulation, locomotion`
- Narration: The takeaway is simple to remember. IBC shows that an agent can learn robotic manipulation and locomotion tasks entirely on its own, with no environment resets and no demonstrations, by generating its own curriculum.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_takeaway_simple_remember_ibc_shows" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple, remember, ibc, shows, agent in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_does_two_cooperating_ideas_auxiliary`

- Preferred role: `content`
- Cue keywords: `does, two, cooperating, ideas, auxiliary, agent, anchors, learner, early, fades`
- Narration: It does this with two cooperating ideas: an auxiliary agent that anchors the learner early and then fades away, and a bidirectional goal curriculum built on optimal transport that keeps proposing achievable intermediate goals.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_does_two_cooperating_ideas_auxiliary" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords does, two, cooperating, ideas, auxiliary, agent in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_result_matches_methods_depend_expert`

- Preferred role: `method`
- Cue keywords: `result, matches, methods, depend, expert`
- Narration: The result matches methods that depend on expert data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_result_matches_methods_depend_expert" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, matches, methods, depend, expert in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_main_caveats_assumes_reversible_envi`

- Preferred role: `content`
- Cue keywords: `main, caveats, assumes, reversible, environments, still, needs, human, specify, sparse`
- Narration: The main caveats are that it assumes reversible environments and still needs a human to specify a sparse reward, and the authors point to a fully reward-free version, hinted at by their C-learning experiments, as the natural next step.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c4_main_caveats_assumes_reversible_envi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords main, caveats, assumes, reversible, environments, still in title/desc so the matcher can verify semantic overlap.
