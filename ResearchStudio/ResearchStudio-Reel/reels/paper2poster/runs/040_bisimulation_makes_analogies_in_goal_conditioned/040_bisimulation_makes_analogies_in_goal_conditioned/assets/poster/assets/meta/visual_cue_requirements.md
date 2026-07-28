# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_what_robot_told_what_analogy`

- Preferred role: `content`
- Cue keywords: `what, robot, told, what, analogy, not, exact, goal, image`
- Narration: What if a robot were told what to do by analogy, not by an exact goal image?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_what_robot_told_what_analogy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, robot, told, what, analogy, not in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_icml_2022_work_berkeley_meta`

- Preferred role: `method`
- Cue keywords: `icml, 2022, work, berkeley, meta, introduces, goal-conditioned, bisimulation, abstraction, where`
- Narration: This ICML 2022 work from Berkeley and Meta introduces goal-conditioned bisimulation: an abstraction where behaviorally equivalent state-goal pairs share a representation, so goals compose by arithmetic.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_icml_2022_work_berkeley_meta" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords icml, 2022, work, berkeley, meta, introduces in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_goal_conditioned_reinforcement_learn`

- Preferred role: `content`
- Cue keywords: `goal-conditioned, reinforcement, learning, usually, hands, agent, exact, goal, target, image`
- Narration: Goal-conditioned reinforcement learning usually hands the agent the exact goal, as a target image.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_goal_conditioned_reinforcement_learn" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords goal-conditioned, reinforcement, learning, usually, hands, agent in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_real_world_you_rarely`

- Preferred role: `content`
- Cue keywords: `but, real, world, you, rarely, know, precise, goal, advance`
- Narration: But in the real world you rarely know the precise goal in advance.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_but_real_world_you_rarely" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, real, world, you, rarely, know in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_ask_robot_close_drawer_you`

- Preferred role: `content`
- Cue keywords: `ask, robot, close, drawer, you, not, know, how, closed, drawer`
- Narration: Ask a robot to close a drawer, and you may not know how the closed drawer looks.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_ask_robot_close_drawer_you" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ask, robot, close, drawer, you, not in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_want_specify_tasks_analogy`

- Preferred role: `title`
- Cue keywords: `want, specify, tasks, analogy`
- Narration: We want to specify tasks by analogy.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c4_want_specify_tasks_analogy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords want, specify, tasks, analogy in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_consider_dicing_carrot_versus_radish`

- Preferred role: `content`
- Cue keywords: `consider, dicing, carrot, versus, radish`
- Narration: Consider dicing a carrot versus a radish.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_consider_dicing_carrot_versus_radish" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords consider, dicing, carrot, versus, radish in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_objects_differ_but_skill_change`

- Preferred role: `content`
- Cue keywords: `objects, differ, but, skill, change, start, goal, same`
- Narration: The objects differ, but the skill and the change from start to goal are the same.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_objects_differ_but_skill_change" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords objects, differ, but, skill, change, start in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_good_representations_invariant_irrel`

- Preferred role: `content`
- Cue keywords: `good, representations, invariant, irrelevant, details, equivariant, what, varies`
- Narration: Good representations are invariant to irrelevant details and equivariant to what varies.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_good_representations_invariant_irrel" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords good, representations, invariant, irrelevant, details, equivariant in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_prior_bisimulation_handled_distracto`

- Preferred role: `method`
- Cue keywords: `prior, bisimulation, handled, distractors, one, task, lift, families, tasks`
- Narration: Prior bisimulation handled distractors for one task; we lift it to families of tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_prior_bisimulation_handled_distracto" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, bisimulation, handled, distractors, one, task in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, contributions`
- Narration: The paper makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_defines_goal_conditioned_bisimulatio`

- Preferred role: `content`
- Cue keywords: `defines, goal-conditioned, bisimulation, grouping, state-goal, pairs, behave, equivalently`
- Narration: It defines goal-conditioned bisimulation, grouping state-goal pairs that behave equivalently.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_defines_goal_conditioned_bisimulatio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords defines, goal-conditioned, bisimulation, grouping, state-goal, pairs in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_gives_metric_learning_objective_new`

- Preferred role: `content`
- Cue keywords: `gives, metric-learning, objective, new, goals, arise, latent, arithmetic`
- Narration: It gives a metric-learning objective so new goals arise from latent arithmetic.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_gives_metric_learning_objective_new" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gives, metric-learning, objective, new, goals, arise in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_proves_representation_sufficient_any`

- Preferred role: `content`
- Cue keywords: `proves, representation, sufficient, any, state-only, reward, task`
- Narration: And it proves the representation is sufficient for any state-only reward task.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_proves_representation_sufficient_any" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords proves, representation, sufficient, any, state-only, reward in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_gcb_learns_two_encoders_together`

- Preferred role: `method`
- Cue keywords: `gcb, learns, two, encoders, together`
- Narration: GCB learns two encoders together.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_gcb_learns_two_encoders_together" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gcb, learns, two, encoders, together in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_phi_encodes_state_goal_pair_its`

- Preferred role: `title`
- Cue keywords: `phi, encodes, state-goal, pair, its, 1, distance, matches, on-policy, bisimulation`
- Narration: Phi encodes a state-goal pair so its L1 distance matches an on-policy bisimulation metric, capturing how differently two tasks behave.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s05_c2_phi_encodes_state_goal_pair_its" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords phi, encodes, state-goal, pair, its, 1 in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_psi_encodes_state_goal_embedding`

- Preferred role: `content`
- Cue keywords: `psi, encodes, state, goal, embedding, minus, state, embedding, equals, phi`
- Narration: Psi encodes a state so the goal embedding minus the state embedding equals phi.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_psi_encodes_state_goal_embedding" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords psi, encodes, state, goal, embedding, minus in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_makes_goals_composable_add_analogous`

- Preferred role: `method`
- Cue keywords: `makes, goals, composable, add, analogous, pair, your, state, take, nearest`
- Narration: That makes goals composable: add an analogous pair to your state, then take the nearest neighbor in psi space. Training is offline on Implicit Q-Learning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_makes_goals_composable_add_analogous" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, goals, composable, add, analogous, pair in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_gcb_tested_pybullet_manipulation_sui`

- Preferred role: `result`
- Cue keywords: `gcb, tested, pybullet, manipulation, suite, random, workspaces, built, eighty-four, object`
- Narration: GCB is tested in a PyBullet manipulation suite of random workspaces built from eighty-four object geometries.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_gcb_tested_pybullet_manipulation_sui" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gcb, tested, pybullet, manipulation, suite, random in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_tasks_span_drawer_button_and_drawer`

- Preferred role: `method`
- Cue keywords: `tasks, span, drawer, button-and-drawer, analogy, also, run, added, video, distractors`
- Narration: Tasks span Drawer, Button-and-Drawer, and Analogy, each also run with added video distractors to probe robustness.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_tasks_span_drawer_button_and_drawer" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tasks, span, drawer, button-and-drawer, analogy, also in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_results_average_over_five_seeds`

- Preferred role: `result`
- Cue keywords: `results, average, over, five, seeds`
- Narration: Results average over five seeds.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c3_results_average_over_five_seeds" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, average, over, five, seeds in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_across_six_settings_gcb_top`

- Preferred role: `method`
- Cue keywords: `across, six, settings, gcb, top, five, wins, every, distractor, task`
- Narration: Across six settings, GCB is top on five, and wins on every distractor task.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_across_six_settings_gcb_top" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, six, settings, gcb, top, five in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_reaches_about_forty_five_percent_dra`

- Preferred role: `method`
- Cue keywords: `reaches, about, forty-five, percent, drawer, distractors, thirty-two, button-and-drawer`
- Narration: It reaches about forty-five percent on Drawer with distractors and thirty-two on Button-and-Drawer.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_reaches_about_forty_five_percent_dra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reaches, about, forty-five, percent, drawer, distractors in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_analogy_tasks_where_goal_inferred`

- Preferred role: `title`
- Cue keywords: `analogy, tasks, where, goal, inferred, example, roughly, doubles, next-best, baseline`
- Narration: On analogy tasks, where the goal is inferred from an example, it roughly doubles the next-best baseline.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s07_c3_analogy_tasks_where_goal_inferred" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords analogy, tasks, where, goal, inferred, example in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablations_confirm_design`

- Preferred role: `content`
- Cue keywords: `ablations, confirm, design`
- Narration: Ablations confirm the design.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_ablations_confirm_design" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, confirm, design in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_adding_grounding_term_phi_goal`

- Preferred role: `content`
- Cue keywords: `adding, grounding, term, phi, goal, itself, normalizing, constant, psi, objective`
- Narration: Adding a grounding term, phi of a goal with itself, as a normalizing constant in psi's objective helps.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_adding_grounding_term_phi_goal" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords adding, grounding, term, phi, goal, itself in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_1_metric_loss_phi_beats`

- Preferred role: `figure`
- Cue keywords: `1, metric, loss, phi, beats, 2`
- Narration: An L1 metric loss for phi beats L2.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c3_1_metric_loss_phi_beats" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords 1, metric, loss, phi, beats, 2 in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_varying_latent_dimensionality_barely`

- Preferred role: `content`
- Cue keywords: `varying, latent, dimensionality, barely, changes, control`
- Narration: And varying the latent dimensionality barely changes control.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_varying_latent_dimensionality_barely" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords varying, latent, dimensionality, barely, changes, control in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_some_headline_numbers`

- Preferred role: `content`
- Cue keywords: `some, headline, numbers`
- Narration: Some headline numbers.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_some_headline_numbers" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords some, headline, numbers in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_drawer_video_distractors_gcb_reaches`

- Preferred role: `method`
- Cue keywords: `drawer, video, distractors, gcb, reaches, zero, point, four, four, eight`
- Narration: On Drawer with video distractors, GCB reaches zero point four four eight, best of any method.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_drawer_video_distractors_gcb_reaches" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords drawer, video, distractors, gcb, reaches, zero in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_button_and_drawer_distractors_zero_p`

- Preferred role: `method`
- Cue keywords: `button-and-drawer, distractors, zero, point, three, two, two`
- Narration: On Button-and-Drawer with distractors, zero point three two two.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_button_and_drawer_distractors_zero_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords button-and-drawer, distractors, zero, point, three, two in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_analogy_zero_point_four_zero`

- Preferred role: `content`
- Cue keywords: `analogy, zero, point, four, zero, three, versus, zero, point, one`
- Narration: On analogy, zero point four zero three versus zero point one seven six for the next best.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_analogy_zero_point_four_zero" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords analogy, zero, point, four, zero, three in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_treating_bisimulation_equiv`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, treating, bisimulation, equivalence, over, tasks, not, just, states, aligns`
- Narration: The takeaway: treating bisimulation as an equivalence over tasks, not just states, aligns analogous tasks in one space.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_treating_bisimulation_equiv" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, treating, bisimulation, equivalence, over, tasks in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_because_goals_become_composable_arit`

- Preferred role: `content`
- Cue keywords: `because, goals, become, composable, arithmetic, you, point, robot, example, infer`
- Narration: Because goals become composable by arithmetic, you can point a robot at an example and have it infer its own goal, provably sufficient for any state-only reward task.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_because_goals_become_composable_arit" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, goals, become, composable, arithmetic, you in title/desc so the matcher can verify semantic overlap.
