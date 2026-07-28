# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_studies_puzzling_instability_behavio`

- Preferred role: `method`
- Cue keywords: `studies, puzzling, instability, behavior, cloning`
- Narration: This paper studies a puzzling training instability in behavior cloning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_studies_puzzling_instability_behavio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords studies, puzzling, instability, behavior, cloning in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_when_you_train_policy_network`

- Preferred role: `figure`
- Cue keywords: `when, you, train, policy, network, minibatch, stochastic, gradient, descent, long-horizon`
- Narration: When you train a policy network with minibatch stochastic gradient descent, the long-horizon reward can swing wildly from one iterate to the next, even though the behavior cloning loss barely moves.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c2_when_you_train_policy_network" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, you, train, policy, network, minibatch in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_authors_trace_what_they_call`

- Preferred role: `method`
- Cue keywords: `authors, trace, what, they, call, gradient, variance, amplification, where, tiny`
- Narration: The authors trace this to what they call gradient variance amplification, where tiny stochastic gradient noise gets amplified into catastrophic error accumulation through the closed loop between the policy and its environment.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_authors_trace_what_they_call" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, trace, what, they, call, gradient in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_most_standard_fixes_not_help`

- Preferred role: `result`
- Cue keywords: `most, standard, fixes, not, help, but, taking, exponential, moving, average`
- Narration: Most standard fixes do not help, but taking an exponential moving average of the weights turns out to be remarkably effective, and the same story holds for autoregressive language models.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c4_most_standard_fixes_not_help" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords most, standard, fixes, not, help, but in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_imagine_robot_controller_imitation_y`

- Preferred role: `method`
- Cue keywords: `imagine, robot, controller, imitation, you, watch, loss, drops, smoothly, stays`
- Narration: Imagine training a robot controller by imitation. You watch the training loss, and it drops smoothly and stays low. Everything looks fine.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_imagine_robot_controller_imitation_y" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords imagine, robot, controller, imitation, you, watch in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_you_actually_deploy_policy`

- Preferred role: `method`
- Cue keywords: `but, you, actually, deploy, policy, measure, how, well, walks, score`
- Narration: But if you actually deploy the policy and measure how well it walks, the score jumps around violently from one training step to the next.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_but_you_actually_deploy_policy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, you, actually, deploy, policy, measure in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_about_gap_single_step_imitation_loss`

- Preferred role: `figure`
- Cue keywords: `about, gap, single-step, imitation, loss, calm, stable, yet, thing, you`
- Narration: This paper is about that gap. The single-step imitation loss is calm and stable, yet the thing you truly care about, the long-horizon reward, is oscillating wildly.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s02_c3_about_gap_single_step_imitation_loss" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords about, gap, single-step, imitation, loss, calm in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_because_expensive_roll_out_evaluate`

- Preferred role: `content`
- Cue keywords: `because, expensive, roll, out, evaluate, every, checkpoint, you, usually, never`
- Narration: And because it is expensive to roll out and evaluate at every checkpoint, you usually never see these swings, which means whichever checkpoint you happen to grab could be a bad one.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_because_expensive_roll_out_evaluate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, expensive, roll, out, evaluate, every in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_modern_deep_learning_full_feedback`

- Preferred role: `content`
- Cue keywords: `modern, deep, learning, full, feedback, loops, language, next, token, depends`
- Narration: Modern deep learning is full of feedback loops. A language model's next token depends on the tokens it already generated. A robot's next observation depends on the action it just took.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_modern_deep_learning_full_feedback" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords modern, deep, learning, full, feedback, loops in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_but_when_train_these_systems`

- Preferred role: `content`
- Cue keywords: `but, when, train, these, systems, almost, always, optimize, surrogate, objective`
- Narration: But when we train these systems, we almost always optimize a surrogate objective, like next-token prediction, that pretends the feedback loop is not there.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_but_when_train_these_systems" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, when, train, these, systems, almost in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_surrogate_tends_improve_smoothly_whi`

- Preferred role: `method`
- Cue keywords: `surrogate, tends, improve, smoothly, which, lulls, thinking, well, behaved`
- Narration: That surrogate tends to improve smoothly, which lulls us into thinking training is well behaved.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_surrogate_tends_improve_smoothly_whi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords surrogate, tends, improve, smoothly, which, lulls in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_authors_argue_dangerous_illusion_rea`

- Preferred role: `content`
- Cue keywords: `authors, argue, dangerous, illusion, real, culprit, behind, instability, not, but`
- Narration: The authors argue this is a dangerous illusion, and that the real culprit behind the instability is not the data or the model, but the noise in the optimizer itself.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_authors_argue_dangerous_illusion_rea" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, argue, dangerous, illusion, real, culprit in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_main_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, main, contributions`
- Narration: The paper makes three main contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_main_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, main, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_through_extensive_study_two`

- Preferred role: `content`
- Cue keywords: `first, through, extensive, study, two, hundred, seventy-eight, distinct, interventions, diagnoses`
- Narration: First, through an extensive study of two hundred and seventy-eight distinct interventions, it diagnoses these reward oscillations and names the mechanism gradient variance amplification, or G V A, the propagation of minibatch stochastic gradient noise through the closed-loop dynamics.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_first_through_extensive_study_two" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, through, extensive, study, two, hundred in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_shows_problem_algorithmic_rat`

- Preferred role: `result`
- Cue keywords: `second, shows, problem, algorithmic, rather, statistical, exponential, moving, average, weights`
- Narration: Second, it shows the problem is algorithmic rather than statistical, and that an exponential moving average of the weights fixes it, even though most standard mitigations fail.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c3_second_shows_problem_algorithmic_rat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, shows, problem, algorithmic, rather, statistical in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_demonstrates_exact_same_phenom`

- Preferred role: `method`
- Cue keywords: `third, demonstrates, exact, same, phenomenon, same, cure, autoregressive, language, models`
- Narration: Third, it demonstrates the exact same phenomenon and the same cure in autoregressive language models, and complements everything with a convex theory vignette. The upshot is a call to treat iterate averaging as an essential design choice, a stabilizer that belongs alongside your optimizer and your scheduler.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_third_demonstrates_exact_same_phenom" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, demonstrates, exact, same, phenomenon, same in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_approach_first_carefully_separate_tw`

- Preferred role: `content`
- Cue keywords: `approach, first, carefully, separate, two, possible, causes, oscillations, statistical, problem`
- Narration: The approach is first to carefully separate the two possible causes of the oscillations. Is it a statistical problem, meaning not enough data, or a computational one, meaning something about the optimization itself?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_approach_first_carefully_separate_tw" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords approach, first, carefully, separate, two, possible in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_ablating_away_statistical_difficulty`

- Preferred role: `content`
- Cue keywords: `ablating, away, statistical, difficulty, still, seeing, oscillations, authors, pin, blame`
- Narration: By ablating away the statistical difficulty and still seeing the oscillations, the authors pin the blame on gradient variance amplification. Then they test the natural fixes. Aggressively decaying the learning rate helps, and dramatically increasing the batch size helps, but both cost a lot of compute. The star of the paper is much cheaper.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_ablating_away_statistical_difficulty" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablating, away, statistical, difficulty, still, seeing in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_you_simply_keep_running_exponential`

- Preferred role: `result`
- Cue keywords: `you, simply, keep, running, exponential, moving, average, your, weights, updating`
- Narration: You simply keep a running exponential moving average of your weights, updating it every step, defined by theta-tilde at time t plus one equals one minus gamma times the old average plus gamma times the new iterate.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c3_you_simply_keep_running_exponential" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords you, simply, keep, running, exponential, moving in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_supporting_theorem_shows_simple_dete`

- Preferred role: `figure`
- Cue keywords: `supporting, theorem, shows, simple, deterministic, environment, tiny, perturbation, barely, changes`
- Narration: A supporting theorem shows that in a simple deterministic environment, a tiny perturbation that barely changes the imitation loss can blow up the rollout reward gap exponentially in the horizon.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c4_supporting_theorem_shows_simple_dete" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords supporting, theorem, shows, simple, deterministic, environment in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_span_two_very_different`

- Preferred role: `title`
- Cue keywords: `experiments, span, two, very, different, domains, continuous, control, authors, classic`
- Narration: The experiments span two very different domains. For continuous control, the authors use classic MuJoCo locomotion tasks, with Walker2d as the primary testbed and Hopper, HalfCheetah, Ant, and Humanoid for breadth.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s06_c1_experiments_span_two_very_different" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, span, two, very, different, domains in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_they_clone_strong_expert_policies`

- Preferred role: `method`
- Cue keywords: `they, clone, strong, expert, policies, over, long, horizon, thousand, steps`
- Narration: They clone from strong expert policies over a long horizon of a thousand steps, and they deliberately set the dataset size so that overfitting is not the issue.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_they_clone_strong_expert_policies" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, clone, strong, expert, policies, over in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_language_they_train_two_hundred`

- Preferred role: `method`
- Cue keywords: `language, they, train, two, hundred, seventy, million, parameter, transformers, tinystories`
- Narration: For language, they train two hundred and seventy million parameter Transformers on TinyStories, a small synthetic dataset of simple children's stories that keeps the setup tractable while still exhibiting the phenomenon.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_language_they_train_two_hundred" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords language, they, train, two, hundred, seventy in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_reward_averaged_over_twenty_initial`

- Preferred role: `result`
- Cue keywords: `reward, averaged, over, twenty, initial, conditions, oscillations, not, just, measurement`
- Narration: Reward is averaged over twenty initial conditions so the oscillations are not just measurement noise.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_reward_averaged_over_twenty_initial" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reward, averaged, over, twenty, initial, conditions in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_finding_striking_plotting_r`

- Preferred role: `method`
- Cue keywords: `headline, finding, striking, plotting, rollout, reward, against, step, reveals, dramatic`
- Narration: The headline finding is striking. Plotting rollout reward against training step reveals dramatic swings between consecutive iterates, and zooming in shows a jagged, almost fractal reward landscape, all while the behavior cloning loss sits flat and smooth.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_headline_finding_striking_plotting_r" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, finding, striking, plotting, rollout, reward in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_jaggedness_completely_invisible_one`

- Preferred role: `content`
- Cue keywords: `jaggedness, completely, invisible, one-step, objective`
- Narration: That jaggedness is completely invisible in the one-step objective.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_jaggedness_completely_invisible_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords jaggedness, completely, invisible, one-step, objective in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_now_apply_exponential_moving_average`

- Preferred role: `result`
- Cue keywords: `now, apply, exponential, moving, average, those, oscillations, dramatically, damped, across`
- Narration: Now apply the exponential moving average, and those oscillations are dramatically damped, across architectures, dataset sizes, and multiple tasks, with no change to the learning rate schedule or batch size.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_now_apply_exponential_moving_average" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords now, apply, exponential, moving, average, those in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_same_butterfly_effect_shows_language`

- Preferred role: `method`
- Cue keywords: `same, butterfly, effect, shows, language, generation, where, two, nearly, identical`
- Narration: And the same butterfly effect shows up in language generation, where two nearly identical training checkpoints produce stories that diverge into totally different plots. Here too the moving average tames the instability and even yields the lowest-perplexity model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_same_butterfly_effect_shows_language" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords same, butterfly, effect, shows, language, generation in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablations_what_make_diagnosis_convin`

- Preferred role: `method`
- Cue keywords: `ablations, what, make, diagnosis, convincing, oscillations, refuse, away, you, vary`
- Narration: The ablations are what make the diagnosis convincing. The oscillations refuse to go away as you vary dataset size, swap a multilayer perceptron for a Transformer, scale the model, or add regularizers.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_ablations_what_make_diagnosis_convin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, what, make, diagnosis, convincing, oscillations in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_only_genuine_variance_reduction_cons`

- Preferred role: `content`
- Cue keywords: `only, genuine, variance, reduction, consistently, calms, them, which, exactly, what`
- Narration: Only genuine variance reduction consistently calms them, which is exactly what you would predict if gradient noise is the cause.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_only_genuine_variance_reduction_cons" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords only, genuine, variance, reduction, consistently, calms in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_fix_side_moving_average_works`

- Preferred role: `result`
- Cue keywords: `fix, side, moving, average, works, best, when, you, update, every`
- Narration: On the fix side, the moving average works best when you update it every single step, use an initial burn-in period, and anneal the averaging rate with a polynomial decay.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c3_fix_side_moving_average_works" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fix, side, moving, average, works, best in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_skip_burn_in_update_average_only`

- Preferred role: `result`
- Cue keywords: `skip, burn-in, update, average, only, occasionally, its, stabilizing, power, degrades`
- Narration: Skip the burn-in, or update the average only occasionally, and its stabilizing power degrades. Learning rate decay and giant batches also work, but they cost far more compute for the same benefit.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_skip_burn_in_update_average_only" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords skip, burn-in, update, average, only, occasionally in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_anchor_study_empirical`

- Preferred role: `content`
- Cue keywords: `few, numbers, anchor, study, empirical, investigation, covers, two, hundred, seventy-eight`
- Narration: A few numbers anchor the study. The empirical investigation covers two hundred and seventy-eight distinct interventions in continuous control.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_anchor_study_empirical" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, anchor, study, empirical, investigation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_rollouts_run_over_horizon_one`

- Preferred role: `result`
- Cue keywords: `rollouts, run, over, horizon, one, thousand, steps, theory, shows, error`
- Narration: The rollouts run over a horizon of one thousand steps, and the theory shows the error amplification constant grows exponentially in that horizon.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_rollouts_run_over_horizon_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rollouts, run, over, horizon, one, thousand in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_language_side_models_two_hundred`

- Preferred role: `method`
- Cue keywords: `language, side, models, two, hundred, seventy, million, parameter, transformers, trained`
- Narration: On the language side, the models are two hundred and seventy million parameter Transformers trained on TinyStories.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_language_side_models_two_hundred" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords language, side, models, two, hundred, seventy in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_key_contrast_theory_perturbation_cha`

- Preferred role: `figure`
- Cue keywords: `key, contrast, theory, perturbation, changes, behavior, cloning, loss, only, order`
- Narration: The key contrast in the theory is that a perturbation changes the behavior cloning loss by only order H delta squared, but can change the rollout reward by order H times e to the H delta minus one, an exponential gap.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s09_c4_key_contrast_theory_perturbation_cha" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, contrast, theory, perturbation, changes, behavior in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple_actionable`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple, actionable`
- Narration: The takeaway is simple and actionable.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple_actionable" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple, actionable in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_stochastic_gradient_noise_completely`

- Preferred role: `method`
- Cue keywords: `stochastic, gradient, noise, completely, harmless, one-step, loss, you, watch, but`
- Narration: Stochastic gradient noise is completely harmless for the one-step training loss you watch, but once your model sits inside a feedback loop, that same noise gets amplified into chaotic, catastrophic failures over long horizons.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_stochastic_gradient_noise_completely" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stochastic, gradient, noise, completely, harmless, one-step in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_they_call_gradient_variance_amplific`

- Preferred role: `result`
- Cue keywords: `they, call, gradient, variance, amplification, good, news, fix, almost, free`
- Narration: They call this gradient variance amplification. The good news is that the fix is almost free. Keep an exponential moving average of your weights, and you get a cheap, broadly effective stabilizer.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c3_they_call_gradient_variance_amplific" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, call, gradient, variance, amplification, good in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_whether_you_robot_controller_languag`

- Preferred role: `method`
- Cue keywords: `whether, you, robot, controller, language, iterate, averaging, deserves, standard, part`
- Narration: Whether you are training a robot controller or a language model, iterate averaging deserves to be a standard part of the pipeline, right next to your optimizer and your learning rate schedule.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c4_whether_you_robot_controller_languag" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords whether, you, robot, controller, language, iterate in title/desc so the matcher can verify semantic overlap.
