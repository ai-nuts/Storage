# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_self_driving_policies_learned_behavi`

- Preferred role: `method`
- Cue keywords: `self-driving, policies, learned, behavioral, cloning, usually, trained, open-loop, matching, expert`
- Narration: "Self-driving policies learned by behavioral cloning are usually trained open-loop, matching expert actions one step at a time, yet they are deployed closed-loop where every action shapes future states.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_self_driving_policies_learned_behavi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords self-driving, policies, learned, behavioral, cloning, usually in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_mismatch_quietly_hurts_real_world_sa`

- Preferred role: `content`
- Cue keywords: `mismatch, quietly, hurts, real-world, safety`
- Narration: This mismatch quietly hurts real-world safety.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_mismatch_quietly_hurts_real_world_sa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mismatch, quietly, hurts, real-world, safety in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_introduces_c_w_e_r_m_closed_loop_wei`

- Preferred role: `method`
- Cue keywords: `introduces, c-w-e-r-m, closed-loop, weighted, empirical, risk, minimization, simple, two-stage, recipe`
- Narration: This paper introduces C-W-E-R-M, Closed-loop Weighted Empirical Risk Minimization: a simple two-stage recipe that first runs a policy in a simulator to find the scenes where it fails, then upsamples exactly those scenes when training the final policy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_introduces_c_w_e_r_m_closed_loop_wei" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, c-w-e-r-m, closed-loop, weighted, empirical, risk in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_challenging_urban_driving_dataset_cu`

- Preferred role: `method`
- Cue keywords: `challenging, urban, driving, dataset, cuts, collisions, substantially, improvements, around, thirty-five`
- Narration: On a challenging urban driving dataset it cuts collisions substantially, with improvements around thirty-five percent on some metrics, all without a differentiable simulator or costly closed-loop training."
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_challenging_urban_driving_dataset_cu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords challenging, urban, driving, dataset, cuts, collisions in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_imitation_learning_self_driving_cars`

- Preferred role: `method`
- Cue keywords: `imitation, learning, self-driving, cars, usually, done, through, behavioral, cloning, where`
- Narration: "Imitation learning for self-driving cars is usually done through behavioral cloning, where the network is trained to reproduce an expert's next action.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_imitation_learning_self_driving_cars" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords imitation, learning, self-driving, cars, usually, done in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_catch_done_open_loop_never_sees`

- Preferred role: `content`
- Cue keywords: `catch, done, open-loop, never, sees, consequences, its, own, actions, but`
- Narration: The catch is that this is done open-loop: the model never sees the consequences of its own actions. But when the policy actually drives, every action changes the future state it will see.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_catch_done_open_loop_never_sees" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords catch, done, open-loop, never, sees, consequences in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_small_prediction_errors_accumulate_p`

- Preferred role: `method`
- Cue keywords: `small, prediction, errors, accumulate, pushing, car, out-of-distribution, situations, never, trained`
- Narration: Small prediction errors accumulate, pushing the car into out-of-distribution situations the model was never trained on.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_small_prediction_errors_accumulate_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords small, prediction, errors, accumulate, pushing, car in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_metrics_truly_matter_like_collisions`

- Preferred role: `method`
- Cue keywords: `metrics, truly, matter, like, collisions, non-differentiable, they, effectively, invisible, standard`
- Narration: And the metrics that truly matter, like collisions, are non-differentiable, so they are effectively invisible to the standard training loss. The result is a policy that looks great open-loop but drives poorly in closed-loop evaluation."
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_metrics_truly_matter_like_collisions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords metrics, truly, matter, like, collisions, non-differentiable in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_been_attempts_close_gap_methods`

- Preferred role: `method`
- Cue keywords: `been, attempts, close, gap, methods, like, urban, driver, run, differentiable`
- Narration: "There have been attempts to close this gap. Methods like Urban Driver run a differentiable simulator directly inside the training loop using backpropagation through time.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_been_attempts_close_gap_methods" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords been, attempts, close, gap, methods, like in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_works_but_expensive_requires_differe`

- Preferred role: `method`
- Cue keywords: `works, but, expensive, requires, differentiable, simulator, does, not, scale, well`
- Narration: This works, but it is expensive: it requires a differentiable simulator, it does not scale well, and it carries the heavy memory cost of unrolling policies during training.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_works_but_expensive_requires_differe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords works, but, expensive, requires, differentiable, simulator in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_other_approaches_collect_on_policy_a`

- Preferred role: `content`
- Cue keywords: `other, approaches, collect, on-policy, add, extra, human, oracles, which, slow`
- Narration: Other approaches collect on-policy data or add extra human oracles, which are slow and costly.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_other_approaches_collect_on_policy_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords other, approaches, collect, on-policy, add, extra in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_authors_ask_simpler_question_get`

- Preferred role: `method`
- Cue keywords: `authors, ask, simpler, question, get, closed-loop, benefits, only, simulator, decide`
- Narration: The authors ask a simpler question: can we get closed-loop benefits by only using a simulator to decide which training scenes matter, without changing the loss function or requiring differentiability? That question motivates CW-ERM."
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_authors_ask_simpler_question_get" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, ask, simpler, question, get, closed-loop in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, contributions`
- Narration: "The paper makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_proposes_closed_loop_weighted`

- Preferred role: `method`
- Cue keywords: `first, proposes, closed-loop, weighted, empirical, risk, minimization, technique, leverages, closed-loop`
- Narration: First, it proposes Closed-loop Weighted Empirical Risk Minimization, a technique that leverages closed-loop metrics from policy rollouts to debias the policy network and shrink the distribution gap between open-loop training and closed-loop inference.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_proposes_closed_loop_weighted" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, proposes, closed-loop, weighted, empirical, risk in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_evaluates_method_experimental`

- Preferred role: `method`
- Cue keywords: `second, evaluates, method, experimentally, challenging, urban, driving, dataset, shows, significant`
- Narration: Second, it evaluates the method experimentally on a challenging urban driving dataset and shows significant closed-loop improvements, all without complex or computationally expensive closed-loop training.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_evaluates_method_experimental" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, evaluates, method, experimentally, challenging, urban in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_establishes_important_theoreti`

- Preferred role: `method`
- Cue keywords: `third, establishes, important, theoretical, connection, between, reweighting, scheme, classic, family`
- Narration: Third, it establishes an important theoretical connection between this reweighting scheme and the classic family of methods that correct covariate shift through density-ratio estimation."
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_third_establishes_important_theoreti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, establishes, important, theoretical, connection, between in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_three_stages_strikingly_simpl`

- Preferred role: `method`
- Cue keywords: `method, three, stages, strikingly, simple, stage, one, you, train, identification`
- Narration: "The method has three stages and is strikingly simple. In stage one, you train an identification policy the ordinary way, with standard ERM behavioral cloning. In stage two, you take that policy and roll it out in a closed-loop simulator over the training scenes, collecting metrics like the number of collisions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_three_stages_strikingly_simpl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, three, stages, strikingly, simple, stage in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_every_scene_where_cost_positive`

- Preferred role: `result`
- Cue keywords: `every, scene, where, cost, positive, meaning, policy, failed, goes, error`
- Narration: Every scene where a cost is positive, meaning the policy failed, goes into an error set. In stage three, you train the final policy again with weighted ERM, but now the error-set scenes are upsampled by a factor w.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c2_every_scene_where_cost_positive" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords every, scene, where, cost, positive, meaning in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_nearly_identical_original_behavioral`

- Preferred role: `content`
- Cue keywords: `nearly, identical, original, behavioral-cloning, objective, single, addition, weighting, term, driven`
- Narration: This is nearly identical to the original behavioral-cloning objective, with the single addition of a weighting term driven by closed-loop failures.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_nearly_identical_original_behavioral" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords nearly, identical, original, behavioral-cloning, objective, single in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_two_practical_tricks_matter_identifi`

- Preferred role: `result`
- Cue keywords: `two, practical, tricks, matter, identification, policy, stopped, early, error, set`
- Narration: Two practical tricks matter: the identification policy is stopped early so the error set is not depleted, and upsampling is used instead of reweighting because it is more stable. Crucially, because the simulator is only used to pick scenes, any non-differentiable metric works and no differentiable simulator is needed."
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c4_two_practical_tricks_matter_identifi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, practical, tricks, matter, identification, policy in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_method_evaluated_proprietary_real_wo`

- Preferred role: `method`
- Cue keywords: `method, evaluated, proprietary, real-world, dataset, collected, company, self-driving, vehicles, challenging`
- Narration: "The method is evaluated on a proprietary real-world dataset, collected from the company's self-driving vehicles on challenging urban missions in San Francisco and Palo Alto.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_method_evaluated_proprietary_real_wo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, evaluated, proprietary, real-world, dataset, collected in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_includes_recorded_trajectories_ego_v`

- Preferred role: `content`
- Cue keywords: `includes, recorded, trajectories, ego, vehicle, surrounding, agents, together, high-definition, maps`
- Narration: It includes recorded trajectories of the ego vehicle and surrounding agents together with high-definition maps.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_includes_recorded_trajectories_ego_v" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords includes, recorded, trajectories, ego, vehicle, surrounding in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_scenarios_diverse_difficult_stopping`

- Preferred role: `method`
- Cue keywords: `scenarios, diverse, difficult, stopping, behind, lead, vehicle, stopping, intersections, navigating`
- Narration: The scenarios are diverse and difficult: stopping behind a lead vehicle, stopping at intersections, and navigating dense traffic with cars, pedestrians, and cyclists. Most scenes run eleven to thirteen seconds, with the longest reaching thirty seconds.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_scenarios_diverse_difficult_stopping" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords scenarios, diverse, difficult, stopping, behind, lead in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_total_authors_train_one_hundred`

- Preferred role: `takeaway`
- Cue keywords: `total, authors, train, one, hundred, eighty, hours, driving, validate, test`
- Narration: In total, the authors train on one hundred and eighty hours of driving and validate and test on sixty hours each. They also open-source the closed-loop simulator and metrics used in the work."
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s06_c4_total_authors_train_one_hundred" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords total, authors, train, one, hundred, eighty in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_results_strong_compared_against_best`

- Preferred role: `method`
- Cue keywords: `results, strong, compared, against, best, baseline, behavioral, cloning, erm, perturbation`
- Narration: "The results are strong. Compared against the best baseline, behavioral cloning with ERM and perturbation, CW-ERM significantly reduces collisions across the board, with improvements reaching about thirty-five percent on some metrics.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_results_strong_compared_against_best" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, strong, compared, against, best, baseline in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_when_upsamples_front_collision_scene`

- Preferred role: `content`
- Cue keywords: `when, upsamples, front-collision, scenes, front, collisions, fall, fourteen, nine`
- Narration: When the model upsamples front-collision scenes, front collisions fall from fourteen to nine.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_when_upsamples_front_collision_scene" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, upsamples, front-collision, scenes, front, collisions in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_when_upsamples_side_collision_scenes`

- Preferred role: `content`
- Cue keywords: `when, upsamples, side-collision, scenes, side, collisions, fall, fifty-five, forty-seven, nice`
- Narration: When it upsamples side-collision scenes, side collisions fall from fifty-five to forty-seven. There is a nice side effect too: improving one metric often improves related ones.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_when_upsamples_side_collision_scenes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, upsamples, side-collision, scenes, side, collisions in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_upsampling_side_collisions_also_redu`

- Preferred role: `result`
- Cue keywords: `upsampling, side, collisions, also, reduces, rear, collisions, evidence, policy, becoming`
- Narration: Upsampling side collisions also reduces rear collisions, evidence that the policy is becoming less passive rather than just gaming a single number. Variance is also lower than the baseline in several cases, so the gains are stable."
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c4_upsampling_side_collisions_also_redu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords upsampling, side, collisions, also, reduces, rear in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablations_reveal_how_method_well`

- Preferred role: `method`
- Cue keywords: `ablations, reveal, how, method, well, targeting, single, metric, isolation, gives`
- Narration: "The ablations reveal how to use the method well. Targeting a single metric in isolation gives the largest improvement on that metric, while combining metrics achieves a balance, tracing out a Pareto front of trade-offs.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_ablations_reveal_how_method_well" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, reveal, how, method, well, targeting in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_combining_front_side_distance_to_ref`

- Preferred role: `content`
- Cue keywords: `combining, front, side, distance-to-reference, works, nicely, but, adding, rear, collisions`
- Narration: Combining front, side, and distance-to-reference works nicely, but adding rear collisions causes a clear regression. The authors trace this to false positives in the rear-collision metric, caused by log-replayed agents that do not react in the simulator. Two hyperparameters also matter.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_combining_front_side_distance_to_ref" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords combining, front, side, distance-to-reference, works, nicely in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_early_stopping_budget_identification`

- Preferred role: `result`
- Cue keywords: `early-stopping, budget, identification, policy, ten, epochs, works, best, single-metric, error`
- Narration: The early-stopping budget K of the identification policy: ten epochs works best for single-metric error sets and twenty for multi-metric.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c3_early_stopping_budget_identification" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords early-stopping, budget, identification, policy, ten, epochs in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_upsampling_factor_performance_improv`

- Preferred role: `method`
- Cue keywords: `upsampling, factor, performance, improves, about, factor, fifty, after, which, side`
- Narration: And the upsampling factor: performance improves up to about a factor of fifty, after which side collisions start to rise again, echoing a similar saturation observed in the Just Train Twice method."
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_upsampling_factor_performance_improv" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords upsampling, factor, performance, improves, about, factor in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_put_concrete_numbers_front_collision`

- Preferred role: `method`
- Cue keywords: `put, concrete, numbers, front, collisions, drop, fourteen, nine, against, strongest`
- Narration: "To put concrete numbers on it: front collisions drop from fourteen to nine against the strongest baseline, roughly a thirty-six percent reduction.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_put_concrete_numbers_front_collision" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords put, concrete, numbers, front, collisions, drop in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_distance_to_reference_trajectory_fai`

- Preferred role: `figure`
- Cue keywords: `distance-to-reference-trajectory, failures, fall, thirty-five, twenty-eight, about, twenty, percent, reduction, side`
- Narration: Distance-to-reference-trajectory failures fall from thirty-five to twenty-eight, about a twenty percent reduction. Side collisions go from fifty-five to forty-seven.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s09_c2_distance_to_reference_trajectory_fai" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords distance-to-reference-trajectory, failures, fall, thirty-five, twenty-eight, about in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_overall_reports_improvements_around`

- Preferred role: `result`
- Cue keywords: `overall, reports, improvements, around, thirty-five, percent, some, metrics, best, upsampling`
- Narration: Overall the paper reports improvements of around thirty-five percent on some metrics. The best upsampling factor is around fifty.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_overall_reports_improvements_around" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords overall, reports, improvements, around, thirty-five, percent in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_models_trained_one_hundred_eighty`

- Preferred role: `method`
- Cue keywords: `models, trained, one, hundred, eighty, hours, driving, validated, tested, sixty`
- Narration: The models were trained on one hundred and eighty hours of driving data, validated and tested on sixty hours each, with the final policy trained for forty epochs."
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_models_trained_one_hundred_eighty" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords models, trained, one, hundred, eighty, hours in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_refreshingly_practical_you`

- Preferred role: `method`
- Cue keywords: `takeaway, refreshingly, practical, you, not, need, differentiable, simulator, human, loop`
- Narration: "The takeaway is refreshingly practical. You do not need a differentiable simulator, a human in the loop, or expensive closed-loop training to get closed-loop benefits.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_takeaway_refreshingly_practical_you" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, refreshingly, practical, you, not, need in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_you_just_need_run_your`

- Preferred role: `content`
- Cue keywords: `you, just, need, run, your, policy, once, simulator, note, where`
- Narration: You just need to run your policy once in a simulator, note where it fails, upsample those scenes, and retrain.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_you_just_need_run_your" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords you, just, need, run, your, policy in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_simple_recipe_delivers_significant_r`

- Preferred role: `content`
- Cue keywords: `simple, recipe, delivers, significant, reductions, collisions, other, non-differentiable, metrics, works`
- Narration: That simple recipe delivers significant reductions in collisions and other non-differentiable metrics, works with any closed-loop metric, and adds no inference latency.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_simple_recipe_delivers_significant_r" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords simple, recipe, delivers, significant, reductions, collisions in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_comes_clean_theoretical_story_weight`

- Preferred role: `content`
- Cue keywords: `comes, clean, theoretical, story, weighting, scenes, failure, closely, connected, correcting`
- Narration: And it comes with a clean theoretical story: weighting scenes by failure is closely connected to correcting covariate shift through density-ratio estimation, a promising direction for making imitation-learned planners both simpler and safer."
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c4_comes_clean_theoretical_story_weight" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords comes, clean, theoretical, story, weighting, scenes in title/desc so the matcher can verify semantic overlap.
