# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_presented_icml_2024_tackles_one_shot`

- Preferred role: `method`
- Cue keywords: `presented, icml, 2024, tackles, one-shot, imitation, learning, when, world, changes`
- Narration: This paper, presented at ICML 2024, tackles one-shot imitation learning when the world changes after the demonstration is given.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_presented_icml_2024_tackles_one_shot" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords presented, icml, 2024, tackles, one-shot, imitation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_authors_introduce_deep_demonstration`

- Preferred role: `method`
- Cue keywords: `authors, introduce, deep, demonstration, tracing, ddt, method, lets, imitator, agent`
- Narration: The authors introduce Deep Demonstration Tracing, or DDT, a method that lets an imitator agent adaptively trace the right states in a single demonstration while recovering from unforeseen obstacles.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_authors_introduce_deep_demonstration" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, introduce, deep, demonstration, tracing, ddt in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_ddt_combines_purpose_built_demonstra`

- Preferred role: `method`
- Cue keywords: `ddt, combines, purpose-built, demonstration, transformer, meta-reinforcement-learning, scheme, outperforms, prior, one-shot`
- Narration: DDT combines a purpose-built demonstration transformer with a meta-reinforcement-learning training scheme, and it outperforms prior one-shot imitation methods across a new maze navigation benchmark and several robotics tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_ddt_combines_purpose_built_demonstra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ddt, combines, purpose-built, demonstration, transformer, meta-reinforcement-learning in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_one_shot_imitation_learning_asks_age`

- Preferred role: `method`
- Cue keywords: `one-shot, imitation, learning, asks, agent, carry, out, task, after, seeing`
- Narration: One-shot imitation learning asks an agent to carry out a task after seeing just a single demonstration. It works well when deployment looks like the demonstration, but the real world is dynamic.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_one_shot_imitation_learning_asks_age" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one-shot, imitation, learning, asks, agent, carry in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_after_demonstration_provided_unexpec`

- Preferred role: `method`
- Cue keywords: `after, demonstration, provided, unexpected, obstacle, appear, grasped, object, slip, pushing`
- Narration: After the demonstration is provided, an unexpected obstacle can appear, or a grasped object can slip, pushing the agent into situations the demonstration never covered.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_after_demonstration_provided_unexpec" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords after, demonstration, provided, unexpected, obstacle, appear in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_traditional_one_shot_imitation_metho`

- Preferred role: `method`
- Cue keywords: `traditional, one-shot, imitation, methods, excel, stationary, settings, yet, their, ability`
- Narration: Traditional one-shot imitation methods excel in stationary settings, yet their ability to handle these unforeseen changes is limited and rarely studied.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_traditional_one_shot_imitation_metho" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords traditional, one-shot, imitation, methods, excel, stationary in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_focuses_squarely_gap_making_one_shot`

- Preferred role: `content`
- Cue keywords: `focuses, squarely, gap, making, one-shot, imitation, robust, when, environment, changes`
- Narration: This paper focuses squarely on that gap: making one-shot imitation robust when the environment changes at runtime.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_focuses_squarely_gap_making_one_shot" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords focuses, squarely, gap, making, one-shot, imitation in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_consider_person_following_demonstrat`

- Preferred role: `method`
- Cue keywords: `consider, person, following, demonstrated, route, start, point, destination, partway, truck`
- Narration: Consider a person following a demonstrated route from a start point to a destination. Partway there, a truck is parked where the demonstration had none.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_consider_person_following_demonstrat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords consider, person, following, demonstrated, route, start in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_human_simply_detours_around_rejoins`

- Preferred role: `content`
- Cue keywords: `human, simply, detours, around, rejoins, original, path, convenient, point`
- Narration: A human simply detours around it and then rejoins the original path at a convenient point.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_human_simply_detours_around_rejoins" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords human, simply, detours, around, rejoins, original in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_easy_people_but_hard_current`

- Preferred role: `method`
- Cue keywords: `easy, people, but, hard, current, one-shot, imitation, techniques, which, mostly`
- Narration: This is easy for people but hard for current one-shot imitation techniques, which mostly clone demonstrated actions and have no principled way to behave in states the demonstration never showed.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_easy_people_but_hard_current" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords easy, people, but, hard, current, one-shot in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_authors_distill_human_behavior_three`

- Preferred role: `method`
- Cue keywords: `authors, distill, human, behavior, three-stage, decision, process, identify, which, demonstrated`
- Narration: The authors distill this human behavior into a three-stage decision process — identify which demonstrated states are relevant, analyze how the expert behaved there, and trace back onto the demonstration — and use it as the blueprint for their method.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_authors_distill_human_behavior_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, distill, human, behavior, three-stage, decision in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_main_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, main, contributions`
- Narration: The paper makes three main contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_main_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, main, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_advances_one_shot_imitation_se`

- Preferred role: `method`
- Cue keywords: `first, advances, one-shot, imitation, setting, deliberately, introducing, large, difference, between`
- Narration: First, it advances the one-shot imitation setting by deliberately introducing a large difference between when the demonstration is collected and when the policy is deployed, and it supports this with a new demonstration-navigation benchmark.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_advances_one_shot_imitation_se" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, advances, one-shot, imitation, setting, deliberately in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_proposes_demonstration_transf`

- Preferred role: `method`
- Cue keywords: `second, proposes, demonstration, transformer, architecture, encourages, policy, trace, demonstration, following`
- Narration: Second, it proposes a demonstration transformer architecture that encourages the policy to trace the demonstration, following the three-stage identify, analyze, and trace process.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_proposes_demonstration_transf" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, proposes, demonstration, transformer, architecture, encourages in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_addresses_one_shot_imitation_c`

- Preferred role: `figure`
- Cue keywords: `third, addresses, one-shot, imitation, context-based, meta-reinforcement-learning, problem, theoretically, analyzes, conditions`
- Narration: Third, it addresses one-shot imitation as a context-based meta-reinforcement-learning problem, and it theoretically analyzes the conditions under which an imitator can succeed from just a single trajectory.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c4_third_addresses_one_shot_imitation_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, addresses, one-shot, imitation, context-based, meta-reinforcement-learning in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_ddt_two_core_pieces_first`

- Preferred role: `method`
- Cue keywords: `ddt, two, core, pieces, first, demonstration, transformer, which, turns, human`
- Narration: DDT has two core pieces. The first is the demonstration transformer, which turns the human three-stage process into a network. The agent's current state becomes a query; the demonstration's states and actions become keys and values.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_ddt_two_core_pieces_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ddt, two, core, pieces, first, demonstration in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_attention_weighting_module_identifie`

- Preferred role: `method`
- Cue keywords: `attention-weighting, module, identifies, which, demonstrated, states, follow, point-wise, multiplication, analyzes`
- Narration: An attention-weighting module identifies which demonstrated states to follow, a point-wise multiplication analyzes how the expert behaved in those states, and the result is combined with the current state to produce the action — the tracing step.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_attention_weighting_module_identifie" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords attention-weighting, module, identifies, which, demonstrated, states in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_second_piece_rather_behavior_cloning`

- Preferred role: `method`
- Cue keywords: `second, piece, rather, behavior, cloning, ddt, frames, one-shot, imitation, context-based`
- Narration: The second piece is training. Rather than behavior cloning, DDT frames one-shot imitation as context-based meta-reinforcement learning, so the agent can explore and learn to act in states the demonstration never visited.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_second_piece_rather_behavior_cloning" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, piece, rather, behavior, cloning, ddt in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_carefully_designed_stationary_osil_r`

- Preferred role: `method`
- Cue keywords: `carefully, designed, stationary, osil, reward, rewards, following, demonstration, while, large-weighted`
- Narration: It uses a carefully designed stationary OSIL reward that rewards following the demonstration while a large-weighted task reward keeps the focus on actually completing the task, and it optimizes everything with Soft Actor-Critic.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_carefully_designed_stationary_osil_r" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords carefully, designed, stationary, osil, reward, rewards in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_test_one_shot_imitation_under_unfore`

- Preferred role: `result`
- Cue keywords: `test, one-shot, imitation, under, unforeseen, change, authors, created, benchmark, called`
- Narration: To test one-shot imitation under unforeseen change, the authors created a benchmark called Valet Parking Assist in Maze, or VPAM, inspired by real-world valet parking.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_test_one_shot_imitation_under_unfore" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords test, one-shot, imitation, under, unforeseen, change in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_point_agent_must_reach_target`

- Preferred role: `content`
- Cue keywords: `point, agent, must, reach, target, maze, never, seen, globally, relying`
- Narration: In it, a point agent must reach a target in a maze it has never seen globally, relying only on short local views computed from eight rays.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_point_agent_must_reach_target" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords point, agent, must, reach, target, maze in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_crucially_rectangular_obstacles_rand`

- Preferred role: `method`
- Cue keywords: `crucially, rectangular, obstacles, randomly, placed, path, often, did, not, exist`
- Narration: Crucially, rectangular obstacles are randomly placed on the path and often did not exist in the demonstration, so the agent cannot blindly replay demonstrated actions. Eight task variants change whether it is a single map or many, whether obstacles are present, and whether coordinates are given.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_crucially_rectangular_obstacles_rand" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, rectangular, obstacles, randomly, placed, path in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_beyond_vpam_ddt_also_applied`

- Preferred role: `result`
- Cue keywords: `beyond, vpam, ddt, also, applied, robotics, benchmarks, including, meta-world, added`
- Narration: Beyond VPAM, DDT is also applied to robotics benchmarks including Meta-World with added disturbances, Gymnasium's Reacher and Pusher, and a MuJoCo manipulation task involving grasping, stacking, and cluttered environments.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_beyond_vpam_ddt_also_applied" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords beyond, vpam, ddt, also, applied, robotics in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_across_vpam_benchmark_ddt_consistent`

- Preferred role: `result`
- Cue keywords: `across, vpam, benchmark, ddt, consistently, leads`
- Narration: Across the VPAM benchmark, DDT consistently leads.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_across_vpam_benchmark_ddt_consistent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, vpam, benchmark, ddt, consistently, leads in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_set_reaches_success_rate_0_86`

- Preferred role: `method`
- Cue keywords: `set, reaches, success, rate, 0.86, non-obstacle, test, settings, 0.84, even`
- Narration: On the training set it reaches a success rate of 0.86, on non-obstacle test settings 0.84, and even under unforeseen obstacles 0.73 — well above every baseline, with the closest competitor DCRL at 0.57 under obstacles and behavior-cloning Trans4OSIL as low as 0.16.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_set_reaches_success_rate_0_86" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords set, reaches, success, rate, 0.86, non-obstacle in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_just_important_stability_moving_cond`

- Preferred role: `method`
- Cue keywords: `just, important, stability, moving, condition, unforeseen, obstacles, ddt, performance, drops`
- Narration: Just as important is stability: moving from the training condition to unforeseen obstacles, DDT's performance drops only fifteen percent, while the baselines drop twenty, thirty-three, and fifty-two percent respectively.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_just_important_stability_moving_cond" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords just, important, stability, moving, condition, unforeseen in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_meta_world_robotics_tasks_added_dist`

- Preferred role: `method`
- Cue keywords: `meta-world, robotics, tasks, added, disturbance, ddt, still, succeeds, sixty-one, percent`
- Narration: On the Meta-World robotics tasks with added disturbance, DDT still succeeds sixty-one percent of the time on unseen demonstrations, whereas the strongest baseline manages only about twelve percent. The meta-RL mechanism is what gives DDT this robustness to change.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_meta_world_robotics_tasks_added_dist" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords meta-world, robotics, tasks, added, disturbance, ddt in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_confirm_component_matters_authors_ab`

- Preferred role: `content`
- Cue keywords: `confirm, component, matters, authors, ablate, two, pieces`
- Narration: To confirm each component matters, the authors ablate two pieces.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_confirm_component_matters_authors_ab" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords confirm, component, matters, authors, ablate, two in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_first_they_swap_demonstration_transf`

- Preferred role: `method`
- Cue keywords: `first, they, swap, demonstration, transformer, standard, transformer, significantly, reduces, final`
- Narration: First, they swap the demonstration transformer for a standard transformer; this significantly reduces the final asymptotic performance, underscoring that the tailored architecture, not just attention in general, is what drives DDT's imitation ability.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_first_they_swap_demonstration_transf" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, they, swap, demonstration, transformer, standard in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_second_they_remove_osil_reward`

- Preferred role: `method`
- Cue keywords: `second, they, remove, osil, reward, train, only, sparse, ending, reward`
- Narration: Second, they remove the OSIL reward and train with only the sparse ending reward; this sharply slows learning, because the OSIL reward supplies a dense, informative signal that lets the agent closely follow the demonstration early in training.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_second_they_remove_osil_reward" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, they, remove, osil, reward, train in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_together_ablations_show_demonstratio`

- Preferred role: `method`
- Cue keywords: `together, ablations, show, demonstration, transformer, osil, reward, play, distinct, necessary`
- Narration: Together the ablations show the demonstration transformer and the OSIL reward each play a distinct and necessary role.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_together_ablations_show_demonstratio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, ablations, show, demonstration, transformer, osil in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact_under`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, impact, under, unforeseen, obstacles, ddt, succeeds, seventy-three`
- Narration: A few numbers capture the impact. Under unforeseen obstacles, DDT succeeds seventy-three percent of the time, compared to fifty-seven percent for the best baseline.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact_under" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact, under, unforeseen in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_its_performance_degradation_unforese`

- Preferred role: `method`
- Cue keywords: `its, performance, degradation, unforeseen, obstacles, just, fifteen, percent, least, five`
- Narration: Its performance degradation from training to unforeseen obstacles is just fifteen percent, at least five percent better retention than any competitor.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_its_performance_degradation_unforese" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, performance, degradation, unforeseen, obstacles, just in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_disturbed_meta_world_tasks_reaches_s`

- Preferred role: `method`
- Cue keywords: `disturbed, meta-world, tasks, reaches, sixty-one, percent, unseen, demonstrations, while, baselines`
- Narration: On disturbed Meta-World tasks it reaches sixty-one percent on unseen demonstrations while baselines stay at or below twelve percent.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_disturbed_meta_world_tasks_reaches_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords disturbed, meta-world, tasks, reaches, sixty-one, percent in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_when_scaled_ddt_improves_roughly`

- Preferred role: `result`
- Cue keywords: `when, scaled, ddt, improves, roughly, two-fold, more, parameters, shows, clean`
- Narration: And when scaled up, DDT improves roughly two-fold with more model parameters and shows a clean log-linear gain with both data volume and model size, hinting at its promise as a backbone for generalist agents.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c4_when_scaled_ddt_improves_roughly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, scaled, ddt, improves, roughly, two-fold in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple`
- Narration: The takeaway is simple.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_instead_blindly_replaying_demonstrat`

- Preferred role: `method`
- Cue keywords: `instead, blindly, replaying, demonstration, agent, should, learn, trace, figuring, out`
- Narration: Instead of blindly replaying a demonstration, an agent should learn to trace it — figuring out which demonstrated states are relevant right now, understanding what the expert did there, and steering back onto the path after a detour.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_instead_blindly_replaying_demonstrat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, blindly, replaying, demonstration, agent, should in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_deep_demonstration_tracing_operation`

- Preferred role: `method`
- Cue keywords: `deep, demonstration, tracing, operationalizes, demonstration, transformer, trained, meta-reinforcement, learning, result`
- Narration: Deep Demonstration Tracing operationalizes this with a demonstration transformer trained by meta-reinforcement learning, and the result is one-shot imitation that stays robust when the environment changes unexpectedly, a regime where earlier methods fail.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_deep_demonstration_tracing_operation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deep, demonstration, tracing, operationalizes, demonstration, transformer in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_its_clean_scaling_behavior_even`

- Preferred role: `figure`
- Cue keywords: `its, clean, scaling, behavior, even, suggests, could, become, building, block`
- Narration: Its clean scaling behavior even suggests it could become a building block for larger, more general decision-making agents.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s10_c4_its_clean_scaling_behavior_even" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, clean, scaling, behavior, even, suggests in title/desc so the matcher can verify semantic overlap.
