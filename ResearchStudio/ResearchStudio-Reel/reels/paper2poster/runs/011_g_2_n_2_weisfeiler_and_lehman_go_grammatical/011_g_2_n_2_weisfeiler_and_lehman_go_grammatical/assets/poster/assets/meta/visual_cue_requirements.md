# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_g2n2_presented_iclr_2024_asks`

- Preferred role: `method`
- Cue keywords: `g2n2, presented, iclr, 2024, asks, deceptively, simple, question, design, graph`
- Narration: This paper, G2N2, presented at ICLR 2024, asks a deceptively simple question: can we design a graph neural network whose expressive power is guaranteed by construction, rather than proved after the fact?
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_g2n2_presented_iclr_2024_asks" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords g2n2, presented, iclr, 2024, asks, deceptively in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_authors_give_recipe`

- Preferred role: `content`
- Cue keywords: `authors, give, recipe`
- Narration: The authors give a recipe.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_authors_give_recipe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, give, recipe in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_they_take_fragment_algebraic_matrix`

- Preferred role: `guidance`
- Cue keywords: `they, take, fragment, algebraic, matrix, language, known, match, third-order, weisfeiler-lehman`
- Narration: They take a fragment of an algebraic matrix language known to match the third-order Weisfeiler-Lehman test, write it as a context-free grammar, prune the grammar down to its essential rules, and then translate those rules directly into the layers of a neural network.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s01_c3_they_take_fragment_algebraic_matrix" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, take, fragment, algebraic, matrix, language in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_result_provably_three_w_l_graph_neur`

- Preferred role: `result`
- Cue keywords: `result, provably, three-w-l, graph, neural, network, both, principled, practice, faster`
- Narration: The result is a provably three-W-L graph neural network that is both principled and, in practice, faster and more accurate than its competitors.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c4_result_provably_three_w_l_graph_neur" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, provably, three-w-l, graph, neural, network in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_how_expressive_graph_neural_network`

- Preferred role: `title`
- Cue keywords: `how, expressive, graph, neural, network, years, field, answered, weisfeiler-lehman, hierarchy`
- Narration: How expressive is a graph neural network? For years the field has answered that with the Weisfeiler-Lehman hierarchy, and the gold standard has been to design a model and then prove it matches, say, the third-order test.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c1_how_expressive_graph_neural_network" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, expressive, graph, neural, network, years in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_proof_comes_after_design`

- Preferred role: `content`
- Cue keywords: `but, proof, comes, after, design, almost, afterthought`
- Narration: But that proof comes after the design, almost as an afterthought.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_but_proof_comes_after_design" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, proof, comes, after, design, almost in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_what_been_missing_systematic_way`

- Preferred role: `content`
- Cue keywords: `what, been, missing, systematic, way, other, direction, start, language, already`
- Narration: What has been missing is a systematic way to go the other direction: to start from a language we already know is exactly as powerful as 3-W-L, and mechanically build a network that inherits that power.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_what_been_missing_systematic_way" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, been, missing, systematic, way, other in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_without_such_recipe_every_expressive`

- Preferred role: `figure`
- Cue keywords: `without, such, recipe, every, expressive, architecture, fresh, hand-crafted, proof`
- Narration: Without such a recipe, every expressive architecture is a fresh, hand-crafted proof.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s02_c4_without_such_recipe_every_expressive" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords without, such, recipe, every, expressive, architecture in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_seed_idea_comes_groundbreaking_obser`

- Preferred role: `content`
- Cue keywords: `seed, idea, comes, groundbreaking, observation, 1, w-l, 3, w-l, tests`
- Narration: The seed of the idea comes from a groundbreaking observation: the 1-W-L and 3-W-L tests can each be rewritten as a fragment of a matrix language called MATLANG.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_seed_idea_comes_groundbreaking_obser" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords seed, idea, comes, groundbreaking, observation, 1 in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_two_graphs_look_same_3`

- Preferred role: `content`
- Cue keywords: `two, graphs, look, same, 3, w-l, only, every, sentence, you`
- Narration: Two graphs look the same to 3-W-L if and only if every sentence you can write in the fragment ML-of-L-three gives them the same value. That is a beautiful bridge between combinatorics and algebra. But a bridge is not a road.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_two_graphs_look_same_3" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, graphs, look, same, 3, w-l in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_turning_one_these_fragments_actual`

- Preferred role: `result`
- Cue keywords: `turning, one, these, fragments, actual, trainable, network, had, been, done`
- Narration: Turning one of these fragments into an actual, trainable network had been done only case by case, and the resulting models could not claim the full 3-W-L guarantee.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c3_turning_one_these_fragments_actual" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords turning, one, these, fragments, actual, trainable in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_motivation_pave_road_once_all`

- Preferred role: `content`
- Cue keywords: `motivation, pave, road, once, all`
- Narration: The motivation here is to pave that road once and for all.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_motivation_pave_road_once_all" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords motivation, pave, road, once, all in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_four_contributions_first_gener`

- Preferred role: `guidance`
- Cue keywords: `makes, four, contributions, first, generic, framework, turns, any, fragment, algebraic`
- Narration: The paper makes four contributions. First, a generic framework that turns any fragment of an algebraic language into a graph neural network through context-free grammars.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s04_c1_makes_four_contributions_first_gener" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, four, contributions, first, generic, framework in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_runs_framework_ml_of_l_three`

- Preferred role: `guidance`
- Cue keywords: `second, runs, framework, ml-of-l-three, fragment, out, comes, g2n2, network, provably`
- Narration: Second, it runs that framework on the ML-of-L-three fragment and out comes G2N2, a network that is provably 3-W-L.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s04_c2_second_runs_framework_ml_of_l_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, runs, framework, ml-of-l-three, fragment, out in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_validates_rule_set_experimenta`

- Preferred role: `takeaway`
- Cue keywords: `third, validates, rule, set, experimentally, showing, grammar, reduction, keeps, expressiveness`
- Narration: Third, it validates the rule set experimentally, showing that the grammar reduction keeps expressiveness while trimming redundancy.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s04_c3_third_validates_rule_set_experimenta" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, validates, rule, set, experimentally, showing in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_fourth_across_broad_battery_downstre`

- Preferred role: `method`
- Cue keywords: `fourth, across, broad, battery, downstream, tasks, g2n2, beats, existing, 3`
- Narration: And fourth, across a broad battery of downstream tasks, G2N2 beats the existing 3-W-L networks, often while running faster.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_fourth_across_broad_battery_downstre" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fourth, across, broad, battery, downstream, tasks in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_recipe_three_moves_start_operation`

- Preferred role: `content`
- Cue keywords: `recipe, three, moves, start, operation, set, l-three, matrix, product, transpose`
- Narration: Here is the recipe in three moves. Start from the operation set L-three: matrix product, transpose, the all-ones vector, diagonal, and element-wise product. Write down an exhaustive grammar whose sentences are exactly the fragment ML-of-L-three.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_recipe_three_moves_start_operation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords recipe, three, moves, start, operation, set in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_reduce_grammar_stripping_away_redund`

- Preferred role: `method`
- Cue keywords: `reduce, grammar, stripping, away, redundant, rules, variables, until, only, essential`
- Narration: Then reduce that grammar, stripping away redundant rules and variables until only the essential productions remain, while proving each step keeps the 3-W-L guarantee. Now the magic: the surviving variables tell you what the network's inputs should be, and each surviving rule becomes a piece of a layer.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_reduce_grammar_stripping_away_redund" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reduce, grammar, stripping, away, redundant, rules in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_concretely_layer_carries_edge_memory`

- Preferred role: `figure`
- Cue keywords: `concretely, layer, carries, edge, memory, node, memory, learnable, linear, blocks`
- Narration: Concretely, a layer carries an edge memory C and a node memory H; learnable linear blocks combine slices of these tensors, the reduced rules like M-times-M and M-Hadamard-M are computed, and two small MLPs stitch everything back together.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c3_concretely_layer_carries_edge_memory" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords concretely, layer, carries, edge, memory, node in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_stack_these_layers_add_permutation_e`

- Preferred role: `content`
- Cue keywords: `stack, these, layers, add, permutation-equivariant, readouts, you, g2n2`
- Narration: Stack these layers, add permutation-equivariant readouts, and you have G2N2.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_stack_these_layers_add_permutation_e" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stack, these, layers, add, permutation-equivariant, readouts in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_evaluation_spans_three_very_differen`

- Preferred role: `result`
- Cue keywords: `evaluation, spans, three, very, different, arenas, regression, qm9, dataset, one`
- Narration: The evaluation spans three very different arenas. For regression, the QM9 dataset of one hundred thirty thousand small molecules, with twelve quantum-chemical targets, including R-squared, the hardest one to predict.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_evaluation_spans_three_very_differen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, spans, three, very, different, arenas in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_classification_classic_tud_benchmark`

- Preferred role: `result`
- Cue keywords: `classification, classic, tud, benchmark, six, datasets, ranging, molecules, like, mutag`
- Narration: For classification, the classic TUD benchmark, six datasets ranging from molecules like MUTAG and PTC to social graphs like IMDB.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_classification_classic_tud_benchmark" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords classification, classic, tud, benchmark, six, datasets in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_spectral_stress_test_node_regression`

- Preferred role: `method`
- Cue keywords: `spectral, stress, test, node-regression, task, nine-hundred-node, graphs, asks, whether, act`
- Narration: And for a spectral stress test, a node-regression task on nine-hundred-node graphs that asks whether the model can act as a band-pass filter.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_spectral_stress_test_node_regression" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords spectral, stress, test, node-regression, task, nine-hundred-node in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_together_they_probe_accuracy_general`

- Preferred role: `result`
- Cue keywords: `together, they, probe, accuracy, generality, subtle, spectral, ability, trips, other`
- Narration: Together they probe accuracy, generality, and a subtle spectral ability that trips up other 3-W-L models.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_together_they_probe_accuracy_general" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, they, probe, accuracy, generality, subtle in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_result_g2n2_does_not`

- Preferred role: `method`
- Cue keywords: `headline, result, g2n2, does, not, just, match, theory, dominates, practice`
- Narration: The headline result is that G2N2 does not just match the theory, it dominates in practice. On QM9, learning targets one at a time, it posts the best error on every single target while training faster than PPGN.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_headline_result_g2n2_does_not" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, result, g2n2, does, not, just in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_notoriously_hard_r_squared_target_it`

- Preferred role: `result`
- Cue keywords: `notoriously, hard, r-squared, target, its, error, drops, zero-point-three-four-two, where, ppgn`
- Narration: On the notoriously hard R-squared target, its error drops to zero-point-three-four-two, where PPGN sits at three-point-seven-eight, more than a ten-fold improvement, and when all twelve targets are learned at once the gap widens further.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_notoriously_hard_r_squared_target_it" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords notoriously, hard, r-squared, target, its, error in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_graph_classification_beats_second_be`

- Preferred role: `result`
- Cue keywords: `graph, classification, beats, second-best, network, five, six, tud, datasets`
- Narration: On graph classification it beats the second-best network on five of the six TUD datasets.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_graph_classification_beats_second_be" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, classification, beats, second-best, network, five in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_spectral_test_cleanly_learns_band_pa`

- Preferred role: `content`
- Cue keywords: `spectral, test, cleanly, learns, band-pass, filters, where, ppgn, starved, memory`
- Narration: And on the spectral test it cleanly learns band-pass filters where PPGN, starved of the memory it would need, essentially fails.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_spectral_test_cleanly_learns_band_pa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords spectral, test, cleanly, learns, band-pass, filters in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_most_instructive_experiment_grammar`

- Preferred role: `method`
- Cue keywords: `most, instructive, experiment, grammar-reduction, ablation, authors, compare, full, grammar, intermediate`
- Narration: The most instructive experiment is the grammar-reduction ablation. The authors compare the full grammar, an intermediate one, and the reduced grammar r-G-of-L-three on the QM9 R-squared target.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_most_instructive_experiment_grammar" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords most, instructive, experiment, grammar-reduction, ablation, authors in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_their_errors_essentially_same_which`

- Preferred role: `result`
- Cue keywords: `their, errors, essentially, same, which, confirms, reduction, throws, away, redundancy`
- Narration: Their errors are essentially the same, which confirms that reduction throws away redundancy without touching expressive power.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_their_errors_essentially_same_which" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords their, errors, essentially, same, which, confirms in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_but_when_you_push_past`

- Preferred role: `guidance`
- Cue keywords: `but, when, you, push, past, reduced, grammar, start, deleting, essential`
- Narration: But when you push past the reduced grammar and start deleting essential rules, performance degrades in a measurable way.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s08_c3_but_when_you_push_past" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, when, you, push, past, reduced in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_degradation_actually_useful_informat`

- Preferred role: `method`
- Cue keywords: `degradation, actually, useful, information, tells, you, how, much, operation, contributes`
- Narration: That degradation is actually useful information: it tells you how much each operation contributes, so you can prune the model deliberately when a task does not demand the full 3-W-L strength.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_degradation_actually_useful_informat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords degradation, actually, useful, information, tells, you in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, impact`
- Narration: A few numbers capture the impact.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_qm9_r_squared_target_error_falls`

- Preferred role: `result`
- Cue keywords: `qm9, r-squared, target, error, falls, three-point-seven-eight, zero-point-three-four-two, roughly, eleven-fold, reduction`
- Narration: On QM9's R-squared target, error falls from three-point-seven-eight to zero-point-three-four-two, roughly an eleven-fold reduction, and the model does it in ninety-eight seconds per epoch versus PPGN's one hundred twenty-nine.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_qm9_r_squared_target_error_falls" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords qm9, r-squared, target, error, falls, three-point-seven-eight in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_spectral_band_pass_task_its_r_square`

- Preferred role: `method`
- Cue keywords: `spectral, band-pass, task, its, r-squared, score, zero-point-eight-two, towers, over, ppgn`
- Narration: On the spectral band-pass task, its R-squared score of zero-point-eight-two towers over PPGN's zero-point-one-zero.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_spectral_band_pass_task_its_r_square" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords spectral, band-pass, task, its, r-squared, score in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_tud_classification_suite_lands_bette`

- Preferred role: `result`
- Cue keywords: `tud, classification, suite, lands, better, second, place, five, six, datasets`
- Narration: And on the TUD classification suite it lands better than second place on five of six datasets, including ninety-two-and-a-half percent on MUTAG.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c4_tud_classification_suite_lands_bette" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tud, classification, suite, lands, better, second in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_message_change_workflow`

- Preferred role: `content`
- Cue keywords: `lasting, message, change, workflow`
- Narration: The lasting message is a change of workflow.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c1_lasting_message_change_workflow" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, change, workflow in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_instead_designing_graph_network_hopi`

- Preferred role: `method`
- Cue keywords: `instead, designing, graph, network, hoping, prove, expressive, you, start, language`
- Narration: Instead of designing a graph network and then hoping to prove it is expressive, you can start from a language whose expressive power you already know, reduce it to a clean grammar, and read the network straight off the rules, expressiveness guaranteed by construction.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_instead_designing_graph_network_hopi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, designing, graph, network, hoping, prove in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_g2n2_concrete_payoff_idea_provably`

- Preferred role: `content`
- Cue keywords: `g2n2, concrete, payoff, idea, provably, 3, w-l, faster, more, accurate`
- Narration: G2N2 is the concrete payoff of that idea: a provably 3-W-L model that is faster and more accurate than its predecessors.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_g2n2_concrete_payoff_idea_provably" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords g2n2, concrete, payoff, idea, provably, 3 in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_because_framework_generic_same_gramm`

- Preferred role: `guidance`
- Cue keywords: `because, framework, generic, same, grammatical, route, could, turn, other, algebraic`
- Narration: And because the framework is generic, the same grammatical route could turn other algebraic fragments into other networks, each carrying its expressive power by design.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s10_c4_because_framework_generic_same_gramm" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, framework, generic, same, grammatical, route in title/desc so the matcher can verify semantic overlap.
