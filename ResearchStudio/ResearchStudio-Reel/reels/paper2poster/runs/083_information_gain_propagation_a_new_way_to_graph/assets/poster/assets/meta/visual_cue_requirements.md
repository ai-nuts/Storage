# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_graph_neural_networks_need_many`

- Preferred role: `content`
- Cue keywords: `graph, neural, networks, need, many, labeled, nodes, labeling, expensive`
- Narration: Graph neural networks need many labeled nodes, and labeling is expensive.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_graph_neural_networks_need_many" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, neural, networks, need, many, labeled in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_iclr_2022_information_gain_propagati`

- Preferred role: `result`
- Cue keywords: `iclr, 2022, information, gain, propagation, rethinks, graph, active, learning`
- Narration: This ICLR 2022 paper, Information Gain Propagation, rethinks graph active learning.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c2_iclr_2022_information_gain_propagati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords iclr, 2022, information, gain, propagation, rethinks in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_instead_asking_oracle_node_exact`

- Preferred role: `title`
- Cue keywords: `instead, asking, oracle, node, exact, class, asks, cheaper, binary, question`
- Narration: Instead of asking an oracle for a node's exact class, it asks a cheaper binary question: does this node belong to a given class?
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s01_c3_instead_asking_oracle_node_exact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, asking, oracle, node, exact, class in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_soft_label_plus_criterion_picking`

- Preferred role: `result`
- Cue keywords: `soft, label, plus, criterion, picking, nodes, whose, information, gain, propagates`
- Narration: That soft label, plus a criterion picking nodes whose information gain propagates farthest, gives higher accuracy at lower cost.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c4_soft_label_plus_criterion_picking" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords soft, label, plus, criterion, picking, nodes in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_graph_neural_networks_rely_large`

- Preferred role: `content`
- Cue keywords: `graph, neural, networks, rely, large, amounts, labeled, which, costly, obtain`
- Narration: Graph neural networks rely on large amounts of labeled data, which is costly to obtain.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_graph_neural_networks_rely_large" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, neural, networks, rely, large, amounts in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_active_learning_cuts_cost_selecting`

- Preferred role: `method`
- Cue keywords: `active, learning, cuts, cost, selecting, most, valuable, nodes, label`
- Narration: Active learning cuts this cost by selecting the most valuable nodes to label.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_active_learning_cuts_cost_selecting" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords active, learning, cuts, cost, selecting, most in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_but_every_prior_method_assumes`

- Preferred role: `method`
- Cue keywords: `but, every, prior, method, assumes, oracle, always, name, node, exact`
- Narration: But every prior method assumes an oracle can always name a node's exact class.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_but_every_prior_method_assumes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, every, prior, method, assumes, oracle in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_when_categories_many_domain_unfamili`

- Preferred role: `title`
- Cue keywords: `when, categories, many, domain, unfamiliar, multi-class, question, too, demanding, budget`
- Narration: When categories are many or the domain is unfamiliar, that multi-class question is too demanding, and the budget is spent inefficiently.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c4_when_categories_many_domain_unfamili" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, categories, many, domain, unfamiliar, multi-class in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_confirming_guess_far_easier_naming`

- Preferred role: `content`
- Cue keywords: `confirming, guess, far, easier, naming, exact, class`
- Narration: Confirming a guess is far easier than naming the exact class.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_confirming_guess_far_easier_naming" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords confirming, guess, far, easier, naming, exact in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_expert_only_answers_binary_yes_or_no`

- Preferred role: `title`
- Cue keywords: `expert, only, answers, binary, yes-or-no, question, labeling, cost, per, node`
- Narration: If an expert only answers a binary yes-or-no question, the labeling cost per node drops sharply, especially with many classes.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s03_c2_expert_only_answers_binary_yes_or_no" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords expert, only, answers, binary, yes-or-no, question in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_meanwhile_existing_selection_criteri`

- Preferred role: `method`
- Cue keywords: `meanwhile, existing, selection, criteria, built, hard, labels, only, measure, single`
- Narration: Meanwhile, existing selection criteria were built for hard labels and only measure a single node's uncertainty.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_meanwhile_existing_selection_criteri" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords meanwhile, existing, selection, criteria, built, hard in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_they_ignore_graph_network_labeling`

- Preferred role: `content`
- Cue keywords: `they, ignore, graph, network, labeling, one, node, propagates, supervision, across`
- Narration: They ignore that in a graph network, labeling one node propagates supervision across its k-hop neighborhood.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_they_ignore_graph_network_labeling" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, ignore, graph, network, labeling, one in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, contributions`
- Narration: The paper makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_new_active_learning_paradigm_g`

- Preferred role: `method`
- Cue keywords: `first, new, active-learning, paradigm, graph, networks, relaxed, queries, soft, labels`
- Narration: First, a new active-learning paradigm for graph networks that uses relaxed queries and soft labels instead of exact-class annotation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_new_active_learning_paradigm_g" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, new, active-learning, paradigm, graph, networks in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_node_selection_criterion_maxi`

- Preferred role: `method`
- Cue keywords: `second, node-selection, criterion, maximizes, how, information, gain, propagates, through, graph`
- Narration: Second, a node-selection criterion that maximizes how information gain propagates through the graph.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_node_selection_criterion_maxi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, node-selection, criterion, maximizes, how, information in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_experiments_showing_beats_stat`

- Preferred role: `content`
- Cue keywords: `third, experiments, showing, beats, state-of-the-art, baselines, generalizes, across, many, graph`
- Narration: Third, experiments showing it beats state-of-the-art baselines and generalizes across many graph neural network backbones.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_third_experiments_showing_beats_stat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, experiments, showing, beats, state-of-the-art, baselines in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_igp_runs_loop_graph_network`

- Preferred role: `method`
- Cue keywords: `igp, runs, loop, graph, network, first, trained, labeled, nodes, their`
- Narration: IGP runs in a loop. A graph network is first trained on the labeled nodes with their soft labels.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_igp_runs_loop_graph_network" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords igp, runs, loop, graph, network, first in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_candidate_oracle_asked_only_whether`

- Preferred role: `title`
- Cue keywords: `candidate, oracle, asked, only, whether, predicted, label, correct, answer, becomes`
- Narration: For each candidate, the oracle is asked only whether the predicted label is correct, and that answer becomes a normalized soft label.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s05_c2_candidate_oracle_asked_only_whether" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords candidate, oracle, asked, only, whether, predicted in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_choose_nodes_igp_measures_how`

- Preferred role: `method`
- Cue keywords: `choose, nodes, igp, measures, how, strongly, node, influences, its, neighbors`
- Narration: To choose nodes, IGP measures how strongly each node influences its neighbors through propagation, the influence magnitude, and combines it with the information gain, the entropy reduction, of every influenced node.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_choose_nodes_igp_measures_how" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords choose, nodes, igp, measures, how, strongly in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_selects_budget_limited_subset_maximi`

- Preferred role: `method`
- Cue keywords: `selects, budget-limited, subset, maximizes, total, propagated, information, gain, updates, repeats`
- Narration: It then selects the budget-limited subset that maximizes total propagated information gain, updates the model, and repeats.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_selects_budget_limited_subset_maximi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords selects, budget-limited, subset, maximizes, total, propagated in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_igp_evaluated_five_graph_benchmarks`

- Preferred role: `result`
- Cue keywords: `igp, evaluated, five, graph, benchmarks, citation, networks, cora, citeseer, pubmed`
- Narration: IGP is evaluated on five graph benchmarks: the citation networks Cora, Citeseer, and PubMed, the large social network Reddit, and the Open Graph Benchmark dataset ogbn-arxiv.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_igp_evaluated_five_graph_benchmarks" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords igp, evaluated, five, graph, benchmarks, citation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_crucially_budget_defined_true_annota`

- Preferred role: `content`
- Cue keywords: `crucially, budget, defined, true, annotation, cost, not, count, labels, since`
- Narration: Crucially, the budget is defined as true annotation cost, not a count of labels, since an exact query is far pricier than a binary one.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_crucially_budget_defined_true_annota" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, budget, defined, true, annotation, cost in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_budgets_vary_two_twenty_labels`

- Preferred role: `content`
- Cue keywords: `budgets, vary, two, twenty, labels, per, class`
- Narration: Budgets vary from two to twenty labels per class.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_budgets_vary_two_twenty_labels" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords budgets, vary, two, twenty, labels, per in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_across_every_dataset_budget_igp`

- Preferred role: `result`
- Cue keywords: `across, every, dataset, budget, igp, delivers, highest, test, accuracy`
- Narration: Across every dataset and budget, IGP delivers the highest test accuracy.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_across_every_dataset_budget_igp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, every, dataset, budget, igp, delivers in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_under_twenty_labels_per_class`

- Preferred role: `method`
- Cue keywords: `under, twenty, labels, per, class, gcn, reaches, 86.4, percent, cora`
- Narration: Under twenty labels per class with a GCN, it reaches 86.4 percent on Cora, 75.8 on Citeseer, and 83.6 on PubMed, beating the strongest prior method, GRAIN, by 1.6 to 2.2 percent on citation networks, with smaller but consistent gains on Reddit and ogbn-arxiv.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_under_twenty_labels_per_class" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords under, twenty, labels, per, class, gcn in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_budget_grows_igp_climbs_fastest`

- Preferred role: `content`
- Cue keywords: `budget, grows, igp, climbs, fastest, lead, holds, across, backbones`
- Narration: As budget grows, IGP climbs fastest, and the lead holds across backbones.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_budget_grows_igp_climbs_fastest" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords budget, grows, igp, climbs, fastest, lead in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablation_disables_one_component_time`

- Preferred role: `content`
- Cue keywords: `ablation, disables, one, component, time`
- Narration: An ablation disables one component at a time.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_ablation_disables_one_component_time" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablation, disables, one, component, time in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_removing_informative_selection_propa`

- Preferred role: `method`
- Cue keywords: `removing, informative, selection, propagation-aware, node, choice, causes, largest, drop, 3.2`
- Narration: Removing informative selection, the propagation-aware node choice, causes the largest drop, up to 3.2 percent on PubMed, making it the most important ingredient.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_removing_informative_selection_propa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords removing, informative, selection, propagation-aware, node, choice in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_removing_informative_soft_labels_cos`

- Preferred role: `method`
- Cue keywords: `removing, informative, soft, labels, costs, 2.9, percent, dropping, influence-magnitude, information`
- Narration: Removing informative training with soft labels costs up to 2.9 percent, dropping the influence-magnitude information quantity up to 2.1, and removing the normalized label up to 2.4.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_removing_informative_soft_labels_cos" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords removing, informative, soft, labels, costs, 2.9 in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_every_piece_contributes`

- Preferred role: `content`
- Cue keywords: `every, piece, contributes`
- Narration: Every piece contributes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_every_piece_contributes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords every, piece, contributes in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_headline_numbers_86_4_percent_accura`

- Preferred role: `result`
- Cue keywords: `headline, numbers, 86.4, percent, accuracy, cora, 2.2, percent, gain, over`
- Narration: The headline numbers: 86.4 percent accuracy on Cora, a 2.2 percent gain over the best baseline, state-of-the-art results across five datasets and four GNN backbones, all achieved by replacing the expensive exact-class question with one cheap binary query per node.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_headline_numbers_86_4_percent_accura" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, numbers, 86.4, percent, accuracy, cora in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple`
- Narration: The takeaway is simple.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_ask_cheap_binary_yes_or_no_question`

- Preferred role: `method`
- Cue keywords: `ask, cheap, binary, yes-or-no, question, select, nodes, whose, information, gain`
- Narration: Ask a cheap binary yes-or-no question, and select nodes whose information gain propagates farthest across the graph.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_ask_cheap_binary_yes_or_no_question" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ask, cheap, binary, yes-or-no, question, select in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_igp_makes_graph_active_learning`

- Preferred role: `content`
- Cue keywords: `igp, makes, graph, active, learning, both, more, accurate, far, cheaper`
- Narration: IGP makes graph active learning both more accurate and far cheaper to label, and works with any graph neural network.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_igp_makes_graph_active_learning" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords igp, makes, graph, active, learning, both in title/desc so the matcher can verify semantic overlap.
