# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_graph_neural_networks_famously_easy`

- Preferred role: `method`
- Cue keywords: `graph, neural, networks, famously, easy, fool, small, structural, changes, field`
- Narration: Graph neural networks are famously easy to fool with small structural changes, and the field has long treated that fragility as pure adversarial vulnerability.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_graph_neural_networks_famously_easy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, neural, networks, famously, easy, fool in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_iclr_2023_technical_university_munic`

- Preferred role: `title`
- Cue keywords: `iclr, 2023, technical, university, munich, asks, sharper, question, those, small`
- Narration: This ICLR 2023 paper from the Technical University of Munich asks a sharper question: do those small perturbations actually preserve a node's true meaning?
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s01_c2_iclr_2023_technical_university_munic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords iclr, 2023, technical, university, munich, asks in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_semantics_aware_notion_adversarial_g`

- Preferred role: `content`
- Cue keywords: `semantics-aware, notion, adversarial, graph, authors, show, low-degree, nodes, many, small`
- Narration: Using a semantics-aware notion of an adversarial graph, the authors show that for low-degree nodes many "small" edge edits already change the ground-truth label, and that every graph neural network they test is over-robust, staying stubbornly unchanged even after the semantics have flipped.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_semantics_aware_notion_adversarial_g" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords semantics-aware, notion, adversarial, graph, authors, show in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_they_show_feeding_graph_label`

- Preferred role: `method`
- Cue keywords: `they, show, feeding, graph, label, structure, back, through, label, propagation`
- Narration: They then show that feeding the training graph's label structure back in through label propagation sharply cuts this over-robustness while improving accuracy and genuine adversarial robustness.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_they_show_feeding_graph_label" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, show, feeding, graph, label, structure in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_adversarial_example_supposed_small_c`

- Preferred role: `content`
- Cue keywords: `adversarial, example, supposed, small, change, does, not, alter, true, category`
- Narration: An adversarial example is supposed to be a small change that does not alter the true category of the input. For images a human can verify this by looking.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_adversarial_example_supposed_small_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords adversarial, example, supposed, small, change, does in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_graphs_such_visual_check_community`

- Preferred role: `content`
- Cue keywords: `graphs, such, visual, check, community, settled, counting, edited, edges, zero`
- Narration: For graphs there is no such visual check, so the community settled on counting edited edges with an ℓ-zero budget.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_graphs_such_visual_check_community" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graphs, such, visual, check, community, settled in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_but_real_graphs_dominated_low_degree`

- Preferred role: `content`
- Cue keywords: `but, real, graphs, dominated, low-degree, nodes, those, nodes, even, tiny`
- Narration: But real graphs are dominated by low-degree nodes, and for those nodes even a tiny edge budget can completely rewire the neighbourhood.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_but_real_graphs_dominated_low_degree" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, real, graphs, dominated, low-degree, nodes in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_raises_fundamental_previously_unansw`

- Preferred role: `title`
- Cue keywords: `raises, fundamental, previously, unanswered, question, these, standard, perturbations, really, keep`
- Narration: That raises a fundamental and previously unanswered question: do these standard perturbations really keep a node's semantic content unchanged, or are we attacking nodes whose true label has already flipped?
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c4_raises_fundamental_previously_unansw" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords raises, fundamental, previously, unanswered, question, these in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_belief_graph_neural_networks_easily`

- Preferred role: `content`
- Cue keywords: `belief, graph, neural, networks, easily, fooled, rests, assumption, perturbations, used`
- Narration: The belief that graph neural networks are easily fooled rests on the assumption that the perturbations used are semantics-preserving.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_belief_graph_neural_networks_easily" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords belief, graph, neural, networks, easily, fooled in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_only_few_works_beyond_simple`

- Preferred role: `method`
- Cue keywords: `only, few, works, beyond, simple, edge, counts, adding, proxies, like`
- Narration: Only a few works go beyond simple edge counts, adding proxies like the degree distribution or homophily metrics. None of them directly measure whether the ground-truth label is preserved.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_only_few_works_beyond_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords only, few, works, beyond, simple, edge in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_matters_because_small_perturbation_a`

- Preferred role: `content`
- Cue keywords: `matters, because, small, perturbation, actually, changed, node, true, class, keeps`
- Narration: This matters because if a "small" perturbation has actually changed a node's true class, then a model that keeps its prediction fixed is not being robustly correct, it is being wrong in a new and hidden way.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_matters_because_small_perturbation_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords matters, because, small, perturbation, actually, changed in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_authors_argue_need_principled_label`

- Preferred role: `content`
- Cue keywords: `authors, argue, need, principled, label-aware, notion, what, semantics-preserving, graph, perturbation`
- Narration: The authors argue we need a principled, label-aware notion of what a semantics-preserving graph perturbation really is.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_authors_argue_need_principled_label" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, argue, need, principled, label-aware, notion in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_four_contributions`

- Preferred role: `content`
- Cue keywords: `makes, four, contributions`
- Narration: The paper makes four contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_four_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, four, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_defines_semantics_aware_notion`

- Preferred role: `result`
- Cue keywords: `first, defines, semantics-aware, notion, adversarial, robustness, node-level, predictions, brand, new`
- Narration: First, it defines a semantics-aware notion of adversarial robustness for node-level predictions, and with it a brand new concept for the graph domain called over-robustness, which is robustness against admissible perturbations whose ground-truth label has already changed.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c2_first_defines_semantics_aware_notion" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, defines, semantics-aware, notion, adversarial, robustness in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_contextual_stochastic_block_m`

- Preferred role: `figure`
- Cue keywords: `second, contextual, stochastic, block, models, shows, common, perturbation, sets, contain`
- Narration: Second, using Contextual Stochastic Block Models it shows that common perturbation sets contain a large fraction of graphs with changed semantics and that every examined GNN is significantly over-robust, with matching patterns on real-world graphs.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c3_second_contextual_stochastic_block_m" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, contextual, stochastic, block, models, shows in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_shows_folding_known_label`

- Preferred role: `method`
- Cue keywords: `third, shows, folding, known, label, structure, inference, through, label, propagation`
- Narration: Third, it shows that folding the known label structure into inference through label propagation significantly reduces over-robustness with no cost to accuracy or adversarial robustness. Fourth, it proves that classifying an inductively sampled node carries no robustness-accuracy tradeoff.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_third_shows_folding_known_label" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, shows, folding, known, label, structure in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_key_idea_introduce_trusted_reference`

- Preferred role: `figure`
- Cue keywords: `key, idea, introduce, trusted, reference, classifier, knows, true, semantics, contextual`
- Narration: The key idea is to introduce a trusted reference classifier that knows the true semantics. On Contextual Stochastic Block Models the authors can derive the Bayes optimal classifier, which chooses the most likely class given the data, and use it as the ground-truth reference g.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c1_key_idea_introduce_trusted_reference" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, idea, introduce, trusted, reference, classifier in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_over_robust_example_perturbed_graph`

- Preferred role: `content`
- Cue keywords: `over-robust, example, perturbed, graph, where, reference, agree, clean, input, perturbation`
- Narration: An over-robust example is then a perturbed graph where the model and the reference agree on the clean input, the perturbation flips the reference (so the semantics genuinely changed), but the model stubbornly keeps its old prediction.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_over_robust_example_perturbed_graph" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords over-robust, example, perturbed, graph, where, reference in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_they_measure_over_robustness_one_min`

- Preferred role: `content`
- Cue keywords: `they, measure, over-robustness, one, minus, ratio, semantics-aware, robustness, conventional, robustness`
- Narration: They measure over-robustness as one minus the ratio of semantics-aware robustness to conventional robustness, so a value of zero-point-two means twenty percent of the measured robustness lies beyond semantic change.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_they_measure_over_robustness_one_min" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, measure, over-robustness, one, minus, ratio in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_finally_they_combine_graph_neural`

- Preferred role: `method`
- Cue keywords: `finally, they, combine, graph, neural, networks, label, propagation, feeding, graph`
- Narration: Finally, they combine graph neural networks with label propagation, feeding the training graph's known labels into the inference process to reduce this unwanted over-robustness.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_finally_they_combine_graph_neural" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finally, they, combine, graph, neural, networks in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_controlled_experiments_run_contextua`

- Preferred role: `figure`
- Cue keywords: `controlled, experiments, run, contextual, stochastic, block, models, which, let, authors`
- Narration: The controlled experiments run on Contextual Stochastic Block Models, which let the authors compute the Bayes optimal reference exactly.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s06_c1_controlled_experiments_run_contextua" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords controlled, experiments, run, contextual, stochastic, block in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_graph_one_thousand_nodes_parametrize`

- Preferred role: `content`
- Cue keywords: `graph, one, thousand, nodes, parametrized, mimic, cora, matching, its, expected`
- Narration: Each graph has one thousand nodes and is parametrized to mimic CORA, matching its expected number of same-class and different-class edges.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_graph_one_thousand_nodes_parametrize" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, one, thousand, nodes, parametrized, mimic in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_parameter_controls_how_discriminativ`

- Preferred role: `method`
- Cue keywords: `parameter, controls, how, discriminative, node, features, swept, zero-point-one, where, features`
- Narration: A parameter K controls how discriminative the node features are, swept from zero-point-one, where features carry almost no signal and structure matters most, up to five, where structure becomes unnecessary.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_parameter_controls_how_discriminativ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords parameter, controls, how, discriminative, node, features in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_they_inductively_sample_thousand_tes`

- Preferred role: `method`
- Cue keywords: `they, inductively, sample, thousand, test, nodes, per, graph, average, over`
- Narration: They inductively sample a thousand test nodes per graph and average over ten graphs. Results are corroborated on the real-world Cora-ML graph and on a Barabási-Albert model with community structure.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_they_inductively_sample_thousand_tes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, inductively, sample, thousand, test, nodes in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_findings_striking_majority_nodes_sta`

- Preferred role: `method`
- Cue keywords: `findings, striking, majority, nodes, standard, perturbation, sets, full, graphs, whose`
- Narration: The findings are striking. For a majority of nodes, the standard perturbation sets are full of graphs whose true label has already changed.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_findings_striking_majority_nodes_sta" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords findings, striking, majority, nodes, standard, perturbation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_example_equal_one_per_node_degree_pl`

- Preferred role: `content`
- Cue keywords: `example, equal, one, per-node, degree-plus-two, budget, ninety-nine-point-four, percent, target, nodes`
- Narration: For example, at K equal to one and a per-node degree-plus-two budget, ninety-nine-point-four percent of target nodes have a perturbed graph with changed semantics.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_example_equal_one_per_node_degree_pl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords example, equal, one, per-node, degree-plus-two, budget in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_every_graph_neural_network_tested`

- Preferred role: `content`
- Cue keywords: `every, graph, neural, network, tested, shows, over-robustness`
- Narration: And every graph neural network tested shows over-robustness.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_every_graph_neural_network_tested" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords every, graph, neural, network, tested, shows in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_perfectly_robust_reference_like_mlp`

- Preferred role: `content`
- Cue keywords: `perfectly, robust, reference, like, mlp, exhibits, forty-three, percent, over-robustness, equal`
- Narration: A perfectly robust reference like an MLP exhibits forty-three percent over-robustness at K equal to zero-point-one under the weak ℓ₂ attack, meaning forty-three percent of its measured adversarial robustness is actually undesirable robustness beyond semantic change, and all the GNNs cluster close to that upper bound.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_perfectly_robust_reference_like_mlp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords perfectly, robust, reference, like, mlp, exhibits in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_most_informative_ablation_concerns_l`

- Preferred role: `content`
- Cue keywords: `most, informative, ablation, concerns, label, propagation, applying, top, graph, neural`
- Narration: The most informative ablation concerns label propagation. Applying it on top of a graph neural network sharply lowers over-robustness.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_most_informative_ablation_concerns_l" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords most, informative, ablation, concerns, label, propagation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_instance_gcn_combined_label_propagat`

- Preferred role: `method`
- Cue keywords: `instance, gcn, combined, label, propagation, equal, zero-point-five, drops, its, over-robustness`
- Narration: For instance, a GCN combined with label propagation at K equal to zero-point-five drops its over-robustness to about twenty-one percent, and label propagation on its own achieves the lowest over-robustness of any method.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_instance_gcn_combined_label_propagat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instance, gcn, combined, label, propagation, equal in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_crucially_comes_free_adding_label`

- Preferred role: `method`
- Cue keywords: `crucially, comes, free, adding, label, propagation, does, not, hurt, test`
- Narration: Crucially, this comes for free: adding label propagation does not hurt test accuracy and often improves genuine adversarial robustness while structure still matters.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_crucially_comes_free_adding_label" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, comes, free, adding, label, propagation in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_effect_robust_stronger_attacks_too`

- Preferred role: `method`
- Cue keywords: `effect, robust, stronger, attacks, too, though, some, over-robustness, always, remains`
- Narration: The effect is robust to stronger attacks too, though some over-robustness always remains, such as eleven-point-four percent for a GCN under Nettack and nineteen-point-two percent for an MLP.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_effect_robust_stronger_attacks_too" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords effect, robust, stronger, attacks, too, though in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_summarize_impact`

- Preferred role: `content`
- Cue keywords: `few, numbers, summarize, impact`
- Narration: A few numbers summarize the impact.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_summarize_impact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, summarize, impact in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_ninety_nine_point_four_percent_targe`

- Preferred role: `content`
- Cue keywords: `ninety-nine-point-four, percent, target, nodes, perturbations, change, their, true, label, under`
- Narration: Up to ninety-nine-point-four percent of target nodes have perturbations that change their true label under a common threat model.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_ninety_nine_point_four_percent_targe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ninety-nine-point-four, percent, target, nodes, perturbations, change in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_perfectly_robust_classifier_shows_fo`

- Preferred role: `method`
- Cue keywords: `perfectly, robust, classifier, shows, forty-three, percent, over-robustness, low, signal, strength`
- Narration: A perfectly robust classifier shows forty-three percent over-robustness at low signal strength.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_perfectly_robust_classifier_shows_fo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords perfectly, robust, classifier, shows, forty-three, percent in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_label_propagation_cuts_gcn_over_robu`

- Preferred role: `method`
- Cue keywords: `label, propagation, cuts, gcn, over-robustness, roughly, twenty-one, percent, even, under`
- Narration: Label propagation cuts a GCN's over-robustness to roughly twenty-one percent, and even under the strong Nettack attack over-robustness never fully disappears, sitting around eleven to nineteen percent depending on the model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_label_propagation_cuts_gcn_over_robu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords label, propagation, cuts, gcn, over-robustness, roughly in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_one_line_takeaway_graph_neural_netwo`

- Preferred role: `result`
- Cue keywords: `one-line, takeaway, graph, neural, networks, not, simply, fragile, they, over-robust`
- Narration: The one-line takeaway is that graph neural networks are not simply fragile, they are over-robust: a large part of their measured robustness is stubborn robustness that persists after the node's true meaning has already changed, which conventional evaluations wrongly credit as good behaviour.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c1_one_line_takeaway_graph_neural_netwo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one-line, takeaway, graph, neural, networks, not in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_bringing_graph_label_structure_infer`

- Preferred role: `method`
- Cue keywords: `bringing, graph, label, structure, inference, through, label, propagation, reduces, over-robustness`
- Narration: Bringing the training graph's label structure into inference through label propagation reduces this over-robustness while improving accuracy and real adversarial robustness.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_bringing_graph_label_structure_infer" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords bringing, graph, label, structure, inference, through in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_semantics_aware_definition_classifyi`

- Preferred role: `result`
- Cue keywords: `semantics-aware, definition, classifying, newly, added, node, carries, robustness-accuracy, tradeoff, all`
- Narration: And with a semantics-aware definition, classifying a newly added node carries no robustness-accuracy tradeoff at all, changing how robustness in graph machine learning ought to be measured.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c3_semantics_aware_definition_classifyi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords semantics-aware, definition, classifying, newly, added, node in title/desc so the matcher can verify semantic overlap.
