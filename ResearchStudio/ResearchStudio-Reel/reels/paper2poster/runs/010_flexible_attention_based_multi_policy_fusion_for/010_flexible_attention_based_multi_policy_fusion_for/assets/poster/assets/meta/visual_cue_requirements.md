# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_reinforcement_learning_agents_still`

- Preferred role: `method`
- Cue keywords: `reinforcement, learning, agents, still, learn, far, less, efficiently, humans, who`
- Narration: Reinforcement learning agents still learn far less efficiently than humans, who freely borrow strategies from many sources and rearrange them at will.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_reinforcement_learning_agents_still" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reinforcement, learning, agents, still, learn, far in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_work_presented_neurips_2023_introduc`

- Preferred role: `method`
- Cue keywords: `work, presented, neurips, 2023, introduces, knowledge-grounded, reinforcement, learning, paradigm, fuses`
- Narration: This work, presented at NeurIPS 2023, introduces Knowledge-Grounded Reinforcement Learning, a paradigm that fuses multiple external knowledge policies, and a new actor architecture called the Knowledge-Inclusive Attention Network, or KIAN.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_work_presented_neurips_2023_introduc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, presented, neurips, 2023, introduces, knowledge-grounded in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_kian_lets_agent_add_remove`

- Preferred role: `method`
- Cue keywords: `kian, lets, agent, add, remove, recombine, knowledge, policies, without, retraining`
- Narration: KIAN lets an agent add, remove, and recombine knowledge policies without retraining, and fixes an exploration pathology called entropy imbalance, delivering more sample-efficient and flexible learning across grid-world and robotics tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_kian_lets_agent_add_remove" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords kian, lets, agent, add, remove, recombine in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_reinforcement_learning_succeeded_acr`

- Preferred role: `title`
- Cue keywords: `reinforcement, learning, succeeded, across, physics, robotics, yet, agents, still, need`
- Narration: Reinforcement learning has succeeded across physics and robotics, yet agents still need enormous numbers of samples to solve tasks that humans master quickly.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c1_reinforcement_learning_succeeded_acr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reinforcement, learning, succeeded, across, physics, robotics in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_part_gap_humans_learn_observing`

- Preferred role: `method`
- Cue keywords: `part, gap, humans, learn, observing, others, freely, reuse, combine, swap`
- Narration: Part of the gap is that humans learn by observing others and freely reuse, combine, and swap the strategies they already know.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_part_gap_humans_learn_observing" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords part, gap, humans, learn, observing, others in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_earlier_reinforcement_learning_metho`

- Preferred role: `method`
- Cue keywords: `earlier, reinforcement, learning, methods, did, incorporate, external, knowledge, policies, improve`
- Narration: Earlier reinforcement learning methods did incorporate external knowledge policies to improve efficiency, but they made it hard to perform arbitrary combinations and replacements of those policies.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_earlier_reinforcement_learning_metho" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords earlier, reinforcement, learning, methods, did, incorporate in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_rigidity_exactly_property_set_out`

- Preferred role: `content`
- Cue keywords: `rigidity, exactly, property, set, out, fix`
- Narration: That rigidity is exactly the property this paper set out to fix.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_rigidity_exactly_property_set_out" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rigidity, exactly, property, set, out, fix in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_authors_summarize_five_properties_ef`

- Preferred role: `content`
- Cue keywords: `authors, summarize, five, properties, efficient, flexible, human, learning, being, knowledge-acquirable`
- Narration: The authors summarize five properties of efficient, flexible human learning: being knowledge-acquirable, sample-efficient, generalizable, compositional, and incremental.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_authors_summarize_five_properties_ef" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, summarize, five, properties, efficient, flexible in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_existing_knowledge_guided_reinforcem`

- Preferred role: `method`
- Cue keywords: `existing, knowledge-guided, reinforcement, learning, methods, satisfy, some, these, but, stumble`
- Narration: Existing knowledge-guided reinforcement learning methods satisfy some of these but stumble on flexibility.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_existing_knowledge_guided_reinforcem" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords existing, knowledge-guided, reinforcement, learning, methods, satisfy in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_when_their_fusion_mechanism_depends`

- Preferred role: `method`
- Cue keywords: `when, their, fusion, mechanism, depends, number, ordering, external, policies, rearranging`
- Narration: When their fusion mechanism depends on the number or ordering of external policies, rearranging the knowledge set or swapping one policy for another means rebuilding or retraining large parts of the model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_when_their_fusion_mechanism_depends" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, their, fusion, mechanism, depends, number in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_motivation_design_actor_whose_struct`

- Preferred role: `method`
- Cue keywords: `motivation, design, actor, whose, structure, lets, knowledge, policies, freely, rearranged`
- Narration: The motivation here is to design an actor whose structure lets knowledge policies be freely rearranged, added, or replaced, so a single trained agent can carry its skills into new tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_motivation_design_actor_whose_struct" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords motivation, design, actor, whose, structure, lets in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_main_contributions_first`

- Preferred role: `content`
- Cue keywords: `makes, three, main, contributions, first, defines, knowledge-grounded, reinforcement, learning, paradigm`
- Narration: The paper makes three main contributions. First, it defines Knowledge-Grounded Reinforcement Learning, a paradigm that fuses an inner, self-learned policy with multiple external knowledge policies.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_main_contributions_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, main, contributions, first, defines in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_introduces_knowledge_inclusiv`

- Preferred role: `method`
- Cue keywords: `second, introduces, knowledge-inclusive, attention, network, kian, whose, embedding-based, attention, lets`
- Narration: Second, it introduces the Knowledge-Inclusive Attention Network, KIAN, whose embedding-based attention lets knowledge policies be freely rearranged, added, or replaced without touching the rest of the network.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_second_introduces_knowledge_inclusiv" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, introduces, knowledge-inclusive, attention, network, kian in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_uncovers_problem_called_entrop`

- Preferred role: `method`
- Cue keywords: `third, uncovers, problem, called, entropy, imbalance, arises, when, maximizing, entropy`
- Narration: Third, it uncovers a problem called entropy imbalance that arises when maximizing entropy for exploration, proves when it happens, and proposes modified policy distributions that fix it.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_third_uncovers_problem_called_entrop" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, uncovers, problem, called, entropy, imbalance in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_together_these_give_agent_efficient`

- Preferred role: `content`
- Cue keywords: `together, these, give, agent, efficient, generalizable, truly, modular, its, knowledge`
- Narration: Together these give an agent that is efficient, generalizable, and truly modular in its use of knowledge.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_together_these_give_agent_efficient" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, these, give, agent, efficient, generalizable in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_kian_knowledge_inclusive_attention_n`

- Preferred role: `method`
- Cue keywords: `kian, knowledge-inclusive, attention, network, built, three, components, inner, actor, normal`
- Narration: KIAN, the Knowledge-Inclusive Attention Network, is built from three components. The inner actor is a normal learnable policy that lets the agent develop its own strategy, so even if every external policy is useless for a task the agent can still find a solution.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_kian_knowledge_inclusive_attention_n" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords kian, knowledge-inclusive, attention, network, built, three in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_knowledge_policy_including_inner_one`

- Preferred role: `content`
- Cue keywords: `knowledge, policy, including, inner, one, given, learnable, embedding, vector, called`
- Narration: Each knowledge policy, including the inner one, is given a learnable embedding vector called its key, which represents the whole policy independent of any state or action.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_knowledge_policy_including_inner_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords knowledge, policy, including, inner, one, given in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_state_dependent_query_produces_vecto`

- Preferred role: `method`
- Cue keywords: `state-dependent, query, produces, vector, compared, every, key, dot, product, softmax`
- Narration: A state-dependent query then produces a vector that is compared to every key by a dot product, and a softmax turns those scores into attention weights. The agent fuses all policies as a weighted sum and samples the final action.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_state_dependent_query_produces_vecto" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords state-dependent, query, produces, vector, compared, every in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_because_key_independent_policies_uno`

- Preferred role: `method`
- Cue keywords: `because, key, independent, policies, unordered, rearranged, any, one, replaced, just`
- Narration: Because each key is independent, the policies are unordered, can be rearranged, and any one can be replaced just by replacing its key, without retraining the rest of KIAN.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_because_key_independent_policies_uno" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, key, independent, policies, unordered, rearranged in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_span_two_families_enviro`

- Preferred role: `title`
- Cue keywords: `experiments, span, two, families, environments, minigrid, provides, discrete-action, grid-world, tasks`
- Narration: The experiments span two families of environments. MiniGrid provides discrete-action grid-world tasks of increasing difficulty, from empty rooms to door-key puzzles, dynamic obstacles, lava crossings, multi-room mazes, and key corridors.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s06_c1_experiments_span_two_families_enviro" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, span, two, families, environments, minigrid in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_openai_robotics_provides_continuous`

- Preferred role: `title`
- Cue keywords: `openai-robotics, provides, continuous-control, manipulation, tasks, such, push, pick-and-place, reach`
- Narration: OpenAI-Robotics provides continuous-control manipulation tasks such as Push, Slide, Pick-and-Place, and Reach.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s06_c2_openai_robotics_provides_continuous" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords openai-robotics, provides, continuous-control, manipulation, tasks, such in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_crucially_every_method_starts_same`

- Preferred role: `method`
- Cue keywords: `crucially, every, method, starts, same, initial, knowledge, set, built, simple`
- Narration: Crucially, every method starts from the same initial knowledge set built from simple if-else programs that are deliberately sub-optimal and cannot complete any task on their own.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_crucially_every_method_starts_same" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, every, method, starts, same, initial in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_experiment_repeated_ten_random_seeds`

- Preferred role: `result`
- Cue keywords: `experiment, repeated, ten, random, seeds, reported, learning, curves, show, ninety-five`
- Narration: Each experiment is repeated with ten random seeds, and the reported learning curves show ninety-five percent confidence intervals.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_experiment_repeated_ten_random_seeds" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiment, repeated, ten, random, seeds, reported in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_across_both_benchmark_suites_kian`

- Preferred role: `method`
- Cue keywords: `across, both, benchmark, suites, kian, only, method, succeed, every, environment`
- Narration: Across both benchmark suites, KIAN was the only method to succeed in every environment when starting from sub-optimal external knowledge, and its sample-efficiency advantage grew as tasks became more complex.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_across_both_benchmark_suites_kian" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, both, benchmark, suites, kian, only in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_zero_shot_generalization_where_polic`

- Preferred role: `method`
- Cue keywords: `zero-shot, generalization, where, policy, trained, one, task, tested, different, one`
- Narration: In zero-shot generalization, where a policy trained on one task is tested on a different one, KIAN outperformed all baselines in most transfers and did so with noticeably smaller variance.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_zero_shot_generalization_where_polic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords zero-shot, generalization, where, policy, trained, one in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_hardest_simple_to_complex_grid_task`

- Preferred role: `method`
- Cue keywords: `hardest, simple-to-complex, grid, task, kian, reached, reward, about, 0.93, while`
- Narration: On the hardest simple-to-complex grid task, KIAN reached a reward of about 0.93 while the strongest baseline stalled near 0.53.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_hardest_simple_to_complex_grid_task" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords hardest, simple-to-complex, grid, task, kian, reached in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_continuous_control_competing_methods`

- Preferred role: `method`
- Cue keywords: `continuous, control, competing, methods, ignore, exploration, issue, collapse, whereas, kian`
- Narration: In continuous control, competing methods that ignore the exploration issue collapse, whereas KIAN keeps learning efficiently.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_continuous_control_competing_methods" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords continuous, control, competing, methods, ignore, exploration in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_key_ablation_isolates_fix_entropy`

- Preferred role: `content`
- Cue keywords: `key, ablation, isolates, fix, entropy, imbalance`
- Narration: A key ablation isolates the paper's fix for entropy imbalance.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_key_ablation_isolates_fix_entropy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, ablation, isolates, fix, entropy, imbalance in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_when_kian_runs_original_policy`

- Preferred role: `method`
- Cue keywords: `when, kian, runs, original, policy, fusion, agent, maximizing, entropy, exploration`
- Narration: When KIAN runs with the original policy fusion, an agent maximizing entropy for exploration collapses onto a single policy and struggles, especially on demanding tasks like dynamic obstacles, multi-room mazes, and the robotic manipulation tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_when_kian_runs_original_policy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, kian, runs, original, policy, fusion in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_switching_modified_policy_distributi`

- Preferred role: `method`
- Cue keywords: `switching, modified, policy, distributions, restores, efficient, exploration, recovers, strong, performance`
- Narration: Switching on the modified policy distributions restores efficient exploration and recovers strong performance.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_switching_modified_policy_distributi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords switching, modified, policy, distributions, restores, efficient in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_separate_compositional_incremental_e`

- Preferred role: `method`
- Cue keywords: `separate, compositional, incremental, experiments, confirm, modular, design, pays, off, kian`
- Narration: Separate compositional and incremental experiments confirm the modular design pays off: KIAN reuses its learned keys and inner policy to acquire new tasks sequentially with fewer samples than training each task from scratch.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_separate_compositional_incremental_e" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords separate, compositional, incremental, experiments, confirm, modular in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_gains_zero_shot`

- Preferred role: `method`
- Cue keywords: `few, numbers, capture, gains, zero-shot, simple-to-complex, transfer, empty-random, grid, kian`
- Narration: A few numbers capture the gains. In zero-shot simple-to-complex transfer on the Empty-Random grid, KIAN scored about 0.93 at the sixteen-by-sixteen size while the best competing method reached only 0.53.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_gains_zero_shot" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, gains, zero-shot, simple-to-complex in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_pick_and_place_task_tested_ten_times`

- Preferred role: `method`
- Cue keywords: `pick-and-place, task, tested, ten-times-larger, goal, range, kian, reached, 0.72, against`
- Narration: On the Pick-and-Place task tested at a ten-times-larger goal range, KIAN reached 0.72 against 0.30 for the strongest baseline.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_pick_and_place_task_tested_ten_times" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pick-and-place, task, tested, ten-times-larger, goal, range in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_complex_to_simple_transfer_doorkey_e`

- Preferred role: `content`
- Cue keywords: `complex-to-simple, transfer, doorkey, eight-by-eight, reach, kian, achieved, perfect, 1.0, versus`
- Narration: In complex-to-simple transfer from DoorKey eight-by-eight to Reach, KIAN achieved a perfect 1.0 versus 0.80 for the reinforcement-learning baselines.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_complex_to_simple_transfer_doorkey_e" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords complex-to-simple, transfer, doorkey, eight-by-eight, reach, kian in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_all_measured_across_two_benchmark`

- Preferred role: `method`
- Cue keywords: `all, measured, across, two, benchmark, suites, five, baselines, ten, random`
- Narration: All of this is measured across two benchmark suites, five baselines, and ten random seeds with ninety-five percent confidence intervals, and KIAN is the only method that succeeds everywhere.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_all_measured_across_two_benchmark" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords all, measured, across, two, benchmark, suites in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_message_treating_knowledge_p`

- Preferred role: `method`
- Cue keywords: `lasting, message, treating, knowledge, policy, independent, attention-addressable, key, turns, external`
- Narration: The lasting message is that treating each knowledge policy as an independent, attention-addressable key turns external knowledge into truly modular building blocks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_lasting_message_treating_knowledge_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, treating, knowledge, policy, independent in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_agent_add_drop_reorder_its`

- Preferred role: `method`
- Cue keywords: `agent, add, drop, reorder, its, policies, any, time, without, retraining`
- Narration: An agent can add, drop, or reorder its policies at any time without retraining the network, and the paper's fix for entropy imbalance keeps exploration efficient when many policies are fused.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_agent_add_drop_reorder_its" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords agent, add, drop, reorder, its, policies in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_result_reinforcement_learning_actor`

- Preferred role: `result`
- Cue keywords: `result, reinforcement, learning, actor, learns, faster, generalizes, better, stays, flexible`
- Narration: The result is a reinforcement learning actor that learns faster, generalizes better, and stays flexible, moving agents a step closer to the efficiency and adaptability of human learning.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c3_result_reinforcement_learning_actor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, reinforcement, learning, actor, learns, faster in title/desc so the matcher can verify semantic overlap.
