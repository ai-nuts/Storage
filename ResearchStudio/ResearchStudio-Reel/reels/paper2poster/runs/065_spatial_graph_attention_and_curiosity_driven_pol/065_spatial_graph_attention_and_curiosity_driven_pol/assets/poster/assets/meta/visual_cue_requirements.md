# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_introduces_dgapn_distilled_graph_att`

- Preferred role: `method`
- Cue keywords: `introduces, dgapn, distilled, graph, attention, policy, network, reinforcement, learning, framework`
- Narration: This paper introduces DGAPN, the Distilled Graph Attention Policy Network, a reinforcement learning framework for generating drug-like molecules that bind antiviral targets.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_introduces_dgapn_distilled_graph_att" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, dgapn, distilled, graph, attention, policy in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_combines_spatial_graph_attention_enc`

- Preferred role: `method`
- Cue keywords: `combines, spatial, graph, attention, encoding, chemistry, 3, structure, fragment-based, attentional`
- Narration: It combines spatial graph attention encoding chemistry and 3D structure, a fragment-based attentional policy, and a curiosity bonus from random network distillation, beating prior generators on binding affinity.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_combines_spatial_graph_attention_enc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords combines, spatial, graph, attention, encoding, chemistry in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_designing_molecules_optimize_propert`

- Preferred role: `content`
- Cue keywords: `designing, molecules, optimize, property, like, binding, tightly, viral, protein, central`
- Narration: Designing molecules that optimize a property, like binding tightly to a viral protein, is a central goal in drug discovery, yet hard to automate.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_designing_molecules_optimize_propert" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords designing, molecules, optimize, property, like, binding in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_chemical_space_discrete_astronomical`

- Preferred role: `method`
- Cue keywords: `chemical, space, discrete, astronomically, large, making, exploration, difficult, compressing, molecule`
- Narration: The chemical space is discrete and astronomically large, making exploration difficult, and compressing a molecule's atom-and-bond graph into a faithful, learnable representation is itself nontrivial.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_chemical_space_discrete_astronomical" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords chemical, space, discrete, astronomically, large, making in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_prior_methods_leave_value_table`

- Preferred role: `method`
- Cue keywords: `prior, methods, leave, value, table, twice`
- Narration: Prior methods leave value on the table twice.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_prior_methods_leave_value_table" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, methods, leave, value, table, twice in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_first_most_graph_networks_encode`

- Preferred role: `content`
- Cue keywords: `first, most, graph, networks, encode, only, atom, attributes, adjacency, ignoring`
- Narration: First, most graph networks encode only atom attributes and adjacency, ignoring bond features and 3D geometry, even though shape and complementarity to the receptor pocket make a good binder.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_first_most_graph_networks_encode" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, most, graph, networks, encode, only in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_second_building_molecules_atom_atom`

- Preferred role: `content`
- Cue keywords: `second, building, molecules, atom, atom, gives, long, unstable, trajectories, hard-to-synthesize`
- Narration: Second, building molecules atom by atom gives long, unstable trajectories and hard-to-synthesize products.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_second_building_molecules_atom_atom" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, building, molecules, atom, atom, gives in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_motivates_encoding_spatial_structure`

- Preferred role: `method`
- Cue keywords: `motivates, encoding, spatial, structure, while, acting, over, whole, fragments`
- Narration: This motivates encoding spatial structure while acting over whole fragments.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_motivates_encoding_spatial_structure" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords motivates, encoding, spatial, structure, while, acting in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_dgapn_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `dgapn, makes, three, contributions`
- Narration: DGAPN makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_dgapn_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dgapn, makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_spatial_graph_attention_gnn`

- Preferred role: `method`
- Cue keywords: `first, spatial, graph, attention, gnn, self-attends, over, node, edge, attributes`
- Narration: First, spatial Graph Attention, a GNN that self-attends over node and edge attributes and encodes 3D structure via an inverse distance matrix.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_spatial_graph_attention_gnn" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, spatial, graph, attention, gnn, self-attends in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_graph_attention_policy_networ`

- Preferred role: `method`
- Cue keywords: `second, graph, attention, policy, network, attentional, policy, over, dynamic, fragment`
- Narration: Second, the Graph Attention Policy Network, an attentional policy over a dynamic fragment action space trained with PPO.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_graph_attention_policy_networ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, graph, attention, policy, network, attentional in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_random_network_distillation_cu`

- Preferred role: `result`
- Cue keywords: `third, random-network-distillation, curiosity, bonus, giving, innovation, rewards, high-affinity, synthesizable, molecules`
- Narration: Third, a random-network-distillation curiosity bonus giving innovation rewards for high-affinity, synthesizable molecules.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c4_third_random_network_distillation_cu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, random-network-distillation, curiosity, bonus, giving, innovation in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_dgapn_casts_molecule_generation_mark`

- Preferred role: `content`
- Cue keywords: `dgapn, casts, molecule, generation, markov, decision, process, step, crem, library`
- Narration: DGAPN casts molecule generation as a Markov decision process. At each step, the CReM library proposes valid molecules reachable by swapping one fragment, guaranteeing synthesizable candidates.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_dgapn_casts_molecule_generation_mark" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dgapn, casts, molecule, generation, markov, decision in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_spatial_graph_attention_embeds_candi`

- Preferred role: `method`
- Cue keywords: `spatial, graph, attention, embeds, candidate, combining, attention, over, atom, bond`
- Narration: Spatial Graph Attention embeds each candidate, combining attention over atom and bond attributes with a spatial convolution from a sparsified inverse distance matrix, so chemistry and geometry both inform the representation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_spatial_graph_attention_embeds_candi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords spatial, graph, attention, embeds, candidate, combining in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_attentional_policy_scores_candidates`

- Preferred role: `method`
- Cue keywords: `attentional, policy, scores, candidates, samples, next, molecule, trained, ppo`
- Narration: An attentional policy scores candidates and samples the next molecule, trained with PPO.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_attentional_policy_scores_candidates" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords attentional, policy, scores, candidates, samples, next in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_finally_random_network_distillation`

- Preferred role: `result`
- Cue keywords: `finally, random, network, distillation, supplies, innovation, reward, whose, error, rewards`
- Narration: Finally, random network distillation supplies an innovation reward whose error rewards exploring novel states.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c4_finally_random_network_distillation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finally, random, network, distillation, supplies, innovation in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_primary_benchmark_designs_novel_inhi`

- Preferred role: `result`
- Cue keywords: `primary, benchmark, designs, novel, inhibitors, binding, nsp15, site, sars-cov-2`
- Narration: The primary benchmark designs novel inhibitors binding the NSP15 site of SARS-CoV-2.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_primary_benchmark_designs_novel_inhi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords primary, benchmark, designs, novel, inhibitors, binding in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_binding_affinity_estimated_molecular`

- Preferred role: `method`
- Cue keywords: `binding, affinity, estimated, molecular, docking, gpu-accelerated, tool, protein, 3, structure`
- Narration: Binding affinity is estimated by molecular docking, using a GPU-accelerated tool on the protein's 3D structure, starting from a dataset of purchasable molecules with NSP15 docking scores.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_binding_affinity_estimated_molecular" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords binding, affinity, estimated, molecular, docking, gpu-accelerated in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_method_also_tested_standard_qed`

- Preferred role: `method`
- Cue keywords: `method, also, tested, standard, qed, penalized, logp, optimization, tasks`
- Narration: The method is also tested on standard QED and penalized LogP optimization tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_method_also_tested_standard_qed" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, also, tested, standard, qed, penalized in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_docking_against_nsp15_dgapn_clearly`

- Preferred role: `method`
- Cue keywords: `docking, against, nsp15, dgapn, clearly, beats, five, state-of-the-art, baselines, reaching`
- Narration: On docking against NSP15, DGAPN clearly beats five state-of-the-art baselines, reaching a best score near minus ten and a mean of minus six point seven seven, well ahead of MolDQN, with an astronomically small p-value under Welch's t-test.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_docking_against_nsp15_dgapn_clearly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords docking, against, nsp15, dgapn, clearly, beats in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_also_wins_constrained_optimization_e`

- Preferred role: `method`
- Cue keywords: `also, wins, constrained, optimization, every, similarity, threshold, multi-objective, mode, trades`
- Narration: It also wins constrained optimization at every similarity threshold, and in multi-objective mode trades slight affinity for markedly better drug-likeness and synthesizability.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_also_wins_constrained_optimization_e" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords also, wins, constrained, optimization, every, similarity in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_authors_ablate_component`

- Preferred role: `content`
- Cue keywords: `authors, ablate, component`
- Narration: The authors ablate each component.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_authors_ablate_component" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, ablate, component in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_supervised_setting_nsp15_loss_curves`

- Preferred role: `method`
- Cue keywords: `supervised, setting, nsp15, loss, curves, over, forty, runs, show, spatial`
- Narration: In a supervised setting on NSP15, loss curves over forty runs show spatial convolution strongly improves molecular representation learning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_supervised_setting_nsp15_loss_curves" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords supervised, setting, nsp15, loss, curves, over in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_comparing_full_dgapn_against_gapn`

- Preferred role: `method`
- Cue keywords: `comparing, full, dgapn, against, gapn, without, innovation, reward, curiosity, bonus`
- Narration: Comparing full DGAPN against GAPN without the innovation reward, the curiosity bonus lifts the best docking score, though it slightly worsens synthetic accessibility.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_comparing_full_dgapn_against_gapn" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords comparing, full, dgapn, against, gapn, without in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_remarkably_dgapn_even_beats_greedy`

- Preferred role: `content`
- Cue keywords: `remarkably, dgapn, even, beats, greedy, crem, oracle, sees, intermediate, docking`
- Narration: Remarkably, DGAPN even beats a greedy CReM oracle that sees intermediate docking rewards.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_remarkably_dgapn_even_beats_greedy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords remarkably, dgapn, even, beats, greedy, crem in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_nsp15_docking_dgapn_reaches_best`

- Preferred role: `method`
- Cue keywords: `nsp15, docking, dgapn, reaches, best, score, near, minus, ten, mean`
- Narration: On NSP15 docking, DGAPN reaches a best score near minus ten and a mean of minus six point seven seven, versus roughly minus eight and minus five for the strongest baseline.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_nsp15_docking_dgapn_reaches_best" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords nsp15, docking, dgapn, reaches, best, score in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_gap_over_second_best_statistically_o`

- Preferred role: `content`
- Cue keywords: `gap, over, second-best, statistically, overwhelming, around, ten, minus, two, hundred`
- Narration: The gap over the second-best model is statistically overwhelming, p around ten to the minus two hundred ninth.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_gap_over_second_best_statistically_o" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gap, over, second-best, statistically, overwhelming, around in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_multi_objective_mode_yields_qed_zero`

- Preferred role: `content`
- Cue keywords: `multi-objective, mode, yields, qed, zero, point, seven, two, synthetic, accessibility`
- Narration: In multi-objective mode it yields QED zero point seven two and synthetic accessibility two point two.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_multi_objective_mode_yields_qed_zero" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords multi-objective, mode, yields, qed, zero, point in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_combining_spatial_structure`

- Preferred role: `method`
- Cue keywords: `takeaway, combining, spatial, structure, curiosity, pays, off, molecular, design`
- Narration: The takeaway: combining spatial structure with curiosity pays off for molecular design.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_takeaway_combining_spatial_structure" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, combining, spatial, structure, curiosity, pays in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_encoding_3_geometry_through_spatial`

- Preferred role: `method`
- Cue keywords: `encoding, 3, geometry, through, spatial, graph, attention, acting, over, whole`
- Narration: By encoding 3D geometry through spatial graph attention, acting over whole fragments for synthesizability, and rewarding novelty with random network distillation, DGAPN designs tighter-binding, more synthesizable drug candidates than prior methods, with a user-defined objective that dials between affinity and drug-likeness.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_encoding_3_geometry_through_spatial" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords encoding, 3, geometry, through, spatial, graph in title/desc so the matcher can verify semantic overlap.
