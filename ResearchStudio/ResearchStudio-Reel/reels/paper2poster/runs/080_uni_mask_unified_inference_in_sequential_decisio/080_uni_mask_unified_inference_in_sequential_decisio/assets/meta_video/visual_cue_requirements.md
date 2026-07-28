# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_randomly_masking_predicting_tokens_p`

- Preferred role: `method`
- Cue keywords: `randomly, masking, predicting, tokens, powered, pretraining, language, modeling`
- Narration: Randomly masking and predicting tokens has powered pretraining in language modeling.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_randomly_masking_predicting_tokens_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords randomly, masking, predicting, tokens, powered, pretraining in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_uni_mask_shows_same_idea_applies`

- Preferred role: `content`
- Cue keywords: `uni-mask, shows, same, idea, applies, naturally, sequential, decision, making`
- Narration: This paper, Uni-MASK, shows the same idea applies naturally to sequential decision making.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_uni_mask_shows_same_idea_applies" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords uni-mask, shows, same, idea, applies, naturally in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_many_well_studied_tasks_behavior_clo`

- Preferred role: `title`
- Cue keywords: `many, well-studied, tasks, behavior, cloning, offline, reinforcement, learning, inverse, dynamics`
- Narration: Many well-studied tasks, behavior cloning, offline reinforcement learning, inverse dynamics, and waypoint conditioning, all correspond to different maskings over a sequence of states, actions, and returns.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s01_c3_many_well_studied_tasks_behavior_clo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords many, well-studied, tasks, behavior, cloning, offline in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_uni_mask_unifies_them_one_framework`

- Preferred role: `method`
- Cue keywords: `uni-mask, unifies, them, one, framework, single, trained, way, often, matches`
- Narration: Uni-MASK unifies them into one framework, and a single model trained this way often matches or beats specialized single-task models, and consistently outperforms them after fine-tuning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_uni_mask_unifies_them_one_framework" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords uni-mask, unifies, them, one, framework, single in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_sequential_decision_making_tasks_lik`

- Preferred role: `method`
- Cue keywords: `sequential, decision, making, tasks, like, behavior, cloning, offline, reinforcement, learning`
- Narration: In sequential decision making, tasks like behavior cloning, offline reinforcement learning, inverse dynamics, and goal or waypoint conditioning are typically each handled by a separate, specially trained model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_sequential_decision_making_tasks_lik" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sequential, decision, making, tasks, like, behavior in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_yet_all_these_tasks_operate`

- Preferred role: `figure`
- Cue keywords: `yet, all, these, tasks, operate, over, very, same, object, trajectory`
- Narration: Yet all of these tasks operate over the very same object: a trajectory of states, actions, and returns.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s02_c2_yet_all_these_tasks_operate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords yet, all, these, tasks, operate, over in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_distinct_per_task_ignores_shared`

- Preferred role: `method`
- Cue keywords: `distinct, per, task, ignores, shared, structure, misses, chance, build, richer`
- Narration: Training a distinct model per task ignores this shared structure and misses the chance to build richer, reusable representations across tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_distinct_per_task_ignores_shared" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords distinct, per, task, ignores, shared, structure in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_masked_language_modeling_technique_b`

- Preferred role: `result`
- Cue keywords: `masked, language, modeling, technique, behind, bert, trains, models, predict, randomly`
- Narration: Masked language modeling, the technique behind BERT, trains models to predict randomly masked tokens in a sequence, producing rich bidirectional representations that transfer to many tasks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c1_masked_language_modeling_technique_b" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords masked, language, modeling, technique, behind, bert in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_authors_observe_idea_maps_directly`

- Preferred role: `content`
- Cue keywords: `authors, observe, idea, maps, directly, onto, decision, making`
- Narration: The authors observe that this idea maps directly onto decision making.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_authors_observe_idea_maps_directly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, observe, idea, maps, directly, onto in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_you_treat_states_actions_tokens`

- Preferred role: `content`
- Cue keywords: `you, treat, states, actions, tokens, mask, last, action, predicting, exactly`
- Narration: If you treat states and actions as tokens and mask the last action, predicting it is exactly a behavior cloning inference.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_you_treat_states_actions_tokens" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords you, treat, states, actions, tokens, mask in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_different_tasks_simply_different_mas`

- Preferred role: `figure`
- Cue keywords: `different, tasks, simply, different, masking, patterns, over, same, trajectory, single`
- Narration: Different tasks are simply different masking patterns over the same trajectory, so a single masked-prediction objective can, in principle, express them all.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s03_c4_different_tasks_simply_different_mas" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords different, tasks, simply, different, masking, patterns in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_main_contribution_uni_mask_framework`

- Preferred role: `figure`
- Cue keywords: `main, contribution, uni-mask, framework, unified, way, specify, models, sequential, decision`
- Narration: The main contribution is the Uni-MASK framework, a unified way to specify models for sequential decision making by casting each inference task as a masking scheme over a trajectory of states, actions, and reward-to-go tokens.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c1_main_contribution_uni_mask_framework" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords main, contribution, uni-mask, framework, unified, way in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_because_tasks_just_maskings_single`

- Preferred role: `method`
- Cue keywords: `because, tasks, just, maskings, single, trained, perform, behavior, cloning, reward`
- Narration: Because tasks are just maskings, a single model can be trained to perform behavior cloning, reward conditioning, dynamics modeling, and goal or waypoint conditioning together.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_because_tasks_just_maskings_single" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, tasks, just, maskings, single, trained in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_authors_show_single_often_matches`

- Preferred role: `result`
- Cue keywords: `authors, show, single, often, matches, exceeds, specialized, single-task, models, consistently`
- Narration: The authors show this single model often matches or exceeds specialized single-task models, and consistently outperforms them after fine-tuning.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c3_authors_show_single_often_matches" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, show, single, often, matches, exceeds in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_along_way_they_also_introduce`

- Preferred role: `content`
- Cue keywords: `along, way, they, also, introduce, decision-gpt, improved, gpt-based, baseline`
- Narration: Along the way they also introduce Decision-GPT, an improved GPT-based baseline.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_along_way_they_also_introduce" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords along, way, they, also, introduce, decision-gpt in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_uni_mask_represents_trajectory_seque`

- Preferred role: `figure`
- Cue keywords: `uni-mask, represents, trajectory, sequence, per-timestep, tokens, state, action, optionally, property`
- Narration: Uni-MASK represents a trajectory as a sequence of per-timestep tokens: a state, an action, and optionally a property token such as return-to-go, the sum of future rewards.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c1_uni_mask_represents_trajectory_seque" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords uni-mask, represents, trajectory, sequence, per-timestep, tokens in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_masking_scheme_specifies_two_things`

- Preferred role: `method`
- Cue keywords: `masking, scheme, specifies, two, things, which, input, tokens, visible, which`
- Narration: A masking scheme specifies two things: which input tokens are visible to the model, and which output tokens the model must predict and be scored on. Different schemes recover different tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_masking_scheme_specifies_two_things" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords masking, scheme, specifies, two, things, which in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_behavior_cloning_conditions_past_sta`

- Preferred role: `method`
- Cue keywords: `behavior, cloning, conditions, past, states, actions, predicts, next, action, goal`
- Narration: Behavior cloning conditions on past states and actions and predicts the next action; goal conditioning additionally reveals a future state; reward conditioning reveals return-to-go. The model itself is a bidirectional BERT-style transformer encoder that stacks each timestep's state, action, and property into one vector and predicts the masked tokens.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_behavior_cloning_conditions_past_sta" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords behavior, cloning, conditions, past, states, actions in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_authors_compare_four_regimes_single`

- Preferred role: `method`
- Cue keywords: `authors, compare, four, regimes, single-task, multi-task, random, scheme, per, snippet`
- Narration: The authors compare four training regimes: single-task, multi-task with a random scheme per snippet, fully random masking, and random-mask pretraining followed by task-specific fine-tuning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_authors_compare_four_regimes_single" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, compare, four, regimes, single-task, multi-task in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_framework_evaluated_two_environments`

- Preferred role: `guidance`
- Cue keywords: `framework, evaluated, two, environments`
- Narration: The framework is evaluated on two environments.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s06_c1_framework_evaluated_two_environments" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords framework, evaluated, two, environments in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_first_minigrid_gridworld_where_agent`

- Preferred role: `method`
- Cue keywords: `first, minigrid, gridworld, where, agent, must, reach, fixed, goal, behind`
- Narration: The first is MiniGrid, a gridworld where an agent must reach a fixed goal behind a locked door; it is used to qualitatively demonstrate the many inference tasks a single model can perform and to compare task-specific validation losses.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_first_minigrid_gridworld_where_agent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, minigrid, gridworld, where, agent, must in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_second_maze2d_continuous_control_maz`

- Preferred role: `method`
- Cue keywords: `second, maze2d, continuous-control, maze, mujoco-based, d4rl, benchmark, where, authors, measure`
- Narration: The second is Maze2D, a continuous-control maze from the MuJoCo-based D4RL benchmark, where the authors measure test-time reward over one thousand rollouts across five seeds, comparing Uni-MASK against a feedforward network, Decision Transformer, and their own improved Decision-GPT baseline at context lengths of five and ten.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_second_maze2d_continuous_control_maz" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, maze2d, continuous-control, maze, mujoco-based, d4rl in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_minigrid_environment_single_trained`

- Preferred role: `method`
- Cue keywords: `minigrid, environment, single, trained, random, masking, outperforms, single-task, models, all`
- Narration: In the MiniGrid environment, a single model trained with random masking outperforms single-task models on all tasks, and adding task-specific fine-tuning on top of random-mask pretraining gives the best performance of all, beating single-task models on every task except behavior cloning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_minigrid_environment_single_trained" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords minigrid, environment, single, trained, random, masking in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_means_even_you_only_care`

- Preferred role: `method`
- Cue keywords: `means, even, you, only, care, about, one, inference, task, first`
- Narration: This means that even if you only care about one inference task, first training on many tasks generally helps.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_means_even_you_only_care" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords means, even, you, only, care, about in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_harder_maze2d_environment_fine_tunin`

- Preferred role: `method`
- Cue keywords: `harder, maze2d, environment, fine-tuning, becomes, critical, fine-tuned, uni-mask, models, reach`
- Narration: In the harder Maze2D environment, fine-tuning becomes critical: the fine-tuned Uni-MASK models reach rewards around two point seven, outperforming every baseline at context length five, including a Decision Transformer that scores only around one point one to one point five.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_harder_maze2d_environment_fine_tunin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords harder, maze2d, environment, fine-tuning, becomes, critical in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_training_regime_comparison_isolates`

- Preferred role: `method`
- Cue keywords: `training-regime, comparison, isolates, effect, ingredient, shows, fine-tuning, decisive, one, good`
- Narration: The training-regime comparison isolates the effect of each ingredient and shows fine-tuning is the decisive one for good performance in the more complex Maze2D environment.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_training_regime_comparison_isolates" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords training-regime, comparison, isolates, effect, ingredient, shows in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_second_controlled_comparison_pits_si`

- Preferred role: `result`
- Cue keywords: `second, controlled, comparison, pits, single-task, uni-mask, against, decision-gpt, baseline, where`
- Narration: A second, controlled comparison pits single-task Uni-MASK against the Decision-GPT baseline, where the only real difference is a BERT-style versus a GPT-style backbone.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_second_controlled_comparison_pits_si" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, controlled, comparison, pits, single-task, uni-mask in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_picture_nuanced_bert_works_well`

- Preferred role: `figure`
- Cue keywords: `picture, nuanced, bert, works, well, short, context, length, five, but`
- Narration: Here the picture is nuanced: BERT works well at a short context length of five, but at length ten the BERT-style Uni-MASK models degrade and are outbeaten by the GPT-based Decision-GPT, revealing a known difficulty of BERT-like architectures with longer-sequence generation.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c3_picture_nuanced_bert_works_well" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords picture, nuanced, bert, works, well, short in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, impact`
- Narration: A few numbers capture the impact.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_maze2d_context_length_five_fine_tune`

- Preferred role: `method`
- Cue keywords: `maze2d, context, length, five, fine-tuned, uni-mask, models, reach, reward, around`
- Narration: In Maze2D at context length five, the fine-tuned Uni-MASK models reach reward around two point seven three on both behavior cloning and reward conditioning, compared to just one point one three and one point four nine for the Decision Transformer, and around one point five to one point seven for a feedforward network.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_maze2d_context_length_five_fine_tune" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords maze2d, context, length, five, fine-tuned, uni-mask in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_these_results_averaged_over_five`

- Preferred role: `result`
- Cue keywords: `these, results, averaged, over, five, seeds, one, thousand, rollouts`
- Narration: These results are averaged over five seeds and one thousand rollouts.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_these_results_averaged_over_five" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, results, averaged, over, five, seeds in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_critically_single_uni_mask_handles_b`

- Preferred role: `content`
- Cue keywords: `critically, single, uni-mask, handles, behavior, cloning, reward, conditioning, dynamics, modeling`
- Narration: And critically, a single Uni-MASK model handles behavior cloning, reward conditioning, dynamics modeling, and goal and waypoint conditioning all at once.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_critically_single_uni_mask_handles_b" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords critically, single, uni-mask, handles, behavior, cloning in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_takeaway_simple_powerful_man`

- Preferred role: `figure`
- Cue keywords: `lasting, takeaway, simple, powerful, many, seemingly, distinct, sequential-decision, tasks, just`
- Narration: The lasting takeaway is simple and powerful: many seemingly distinct sequential-decision tasks are just different maskings of the same trajectory, so a single masked-prediction model can replace a zoo of specialized ones.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s10_c1_lasting_takeaway_simple_powerful_man" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, takeaway, simple, powerful, many, seemingly in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_many_masking_schemes_fine_tuning_gen`

- Preferred role: `method`
- Cue keywords: `many, masking, schemes, fine-tuning, generally, does, better, any, single, task`
- Narration: And training on many masking schemes, then fine-tuning, generally does better than training on any single task alone, even when you only care about that one task.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_many_masking_schemes_fine_tuning_gen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords many, masking, schemes, fine-tuning, generally, does in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_main_caveat_architectural_bert_style`

- Preferred role: `method`
- Cue keywords: `main, caveat, architectural, bert-style, models, shine, short, contexts, but, struggle`
- Narration: The main caveat is architectural, BERT-style models shine at short contexts but struggle to generate over longer sequences, suggesting that combining GPT-style backbones with random masking is a promising next step.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_main_caveat_architectural_bert_style" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords main, caveat, architectural, bert-style, models, shine in title/desc so the matcher can verify semantic overlap.
