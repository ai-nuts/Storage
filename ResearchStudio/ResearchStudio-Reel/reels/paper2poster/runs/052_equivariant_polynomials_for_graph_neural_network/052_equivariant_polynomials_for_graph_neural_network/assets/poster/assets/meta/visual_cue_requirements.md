# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_graph_neural_networks_limited_what`

- Preferred role: `figure`
- Cue keywords: `graph, neural, networks, limited, what, they, compute, yardstick, weisfeiler-lehman, hierarchy`
- Narration: Graph neural networks are limited in what they can compute, and the yardstick, the Weisfeiler-Lehman hierarchy, is hard to interpret and too coarse to separate architectures.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c1_graph_neural_networks_limited_what" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, neural, networks, limited, what, they in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_icml_2023_measures_graph_network`

- Preferred role: `content`
- Cue keywords: `icml, 2023, measures, graph, network, instead, which, equivariant, polynomials, compute`
- Narration: This ICML 2023 paper measures a graph network instead by which equivariant polynomials it can compute.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_icml_2023_measures_graph_network" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords icml, 2023, measures, graph, network, instead in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_authors_give_complete_basis_these`

- Preferred role: `method`
- Cue keywords: `authors, give, complete, basis, these, polynomials, build, tools, read, off`
- Narration: The authors give a complete basis for these polynomials, build tools to read off any model's exact power, and design a stronger network that reaches state of the art on molecular benchmarks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_authors_give_complete_basis_these" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, give, complete, basis, these, polynomials in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_graph_networks_bounded_expressive_po`

- Preferred role: `content`
- Cue keywords: `graph, networks, bounded, expressive, power, only, some, functions, graph, represented`
- Narration: Graph networks have bounded expressive power: only some functions of a graph can be represented.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_graph_networks_bounded_expressive_po" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, networks, bounded, expressive, power, only in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_field_measures_weisfeiler_lehman_hie`

- Preferred role: `content`
- Cue keywords: `field, measures, weisfeiler-lehman, hierarchy, isomorphism, tests`
- Narration: The field measures this with the Weisfeiler-Lehman hierarchy of isomorphism tests.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_field_measures_weisfeiler_lehman_hie" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords field, measures, weisfeiler-lehman, hierarchy, isomorphism, tests in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_but_combinatorial_giving_recipe_make`

- Preferred role: `method`
- Cue keywords: `but, combinatorial, giving, recipe, make, network, stronger, its, rungs, far`
- Narration: But WL is combinatorial, giving no recipe to make a network stronger, and its rungs are so far apart that very different GNNs collapse to the same level.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_but_combinatorial_giving_recipe_make" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, combinatorial, giving, recipe, make, network in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_need_finer_more_actionable_ruler`

- Preferred role: `guidance`
- Cue keywords: `need, finer, more, actionable, ruler`
- Narration: We need a finer, more actionable ruler.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s02_c4_need_finer_more_actionable_ruler" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords need, finer, more, actionable, ruler in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_authors_argue_right_way_grade`

- Preferred role: `content`
- Cue keywords: `authors, argue, right, way, grade, graph, network, quantities, compute`
- Narration: The authors argue the right way to grade a graph network is by the quantities it can compute.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_authors_argue_right_way_grade" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, argue, right, way, grade, graph in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_equivariant_polynomials_polynomials`

- Preferred role: `method`
- Cue keywords: `equivariant, polynomials, polynomials, adjacency, matrix, respect, node, relabeling, natural, candidates`
- Narration: Equivariant polynomials, polynomials of the adjacency matrix that respect node relabeling, are natural candidates: subgraph counts and many structural features are exactly such polynomials.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_equivariant_polynomials_polynomials" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords equivariant, polynomials, polynomials, adjacency, matrix, respect in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_knowing_their_full_space_which`

- Preferred role: `guidance`
- Cue keywords: `knowing, their, full, space, which, network, evaluate, gives, both, fine-grained`
- Narration: Knowing their full space, and which a network can evaluate, gives both a fine-grained ruler and a to-do list of missing operations.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s03_c3_knowing_their_full_space_which" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords knowing, their, full, space, which, network in title/desc so the matcher can verify semantic overlap.

## Slide 04: method

Heading: Method

### Cue 1: `cue_s04_c1_core_object_basis_equivariant_graph`

- Preferred role: `content`
- Cue keywords: `core, object, basis, equivariant, graph, polynomials, basis, element, directed, multi-graph`
- Narration: The core object is a basis for equivariant graph polynomials. Each basis element is a directed multi-graph with a marked red edge, and its value is a tensor contraction, an einsum over adjacency entries that sums over internal nodes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_core_object_basis_equivariant_graph" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, object, basis, equivariant, graph, polynomials in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_averaging_monomials_over_all_node`

- Preferred role: `content`
- Cue keywords: `averaging, monomials, over, all, node, permutations, reynolds, operator, makes, them`
- Narration: Averaging monomials over all node permutations, the Reynolds operator, makes them equivariant.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_averaging_monomials_over_all_node" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords averaging, monomials, over, all, node, permutations in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_analyze_network_authors_treat_bank`

- Preferred role: `content`
- Cue keywords: `analyze, network, authors, treat, bank, primitive, contractions, give, linear-time, algorithm`
- Narration: To analyze a network, the authors treat it as a bank of primitive contractions and give a linear-time algorithm deciding which polynomials it can assemble.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_analyze_network_authors_treat_bank" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords analyze, network, authors, treat, bank, primitive in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_node_based_banks_equal_one_wl_edge_b`

- Preferred role: `method`
- Cue keywords: `node-based, banks, equal, one-wl, edge-based, banks, equal, two-fwl, three-wl, building`
- Narration: Node-based banks equal one-WL, edge-based banks equal two-FWL, that is three-WL. Building on this, PPGN plus plus feeds in precomputed polynomial features, lifting it strictly above three-WL.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_node_based_banks_equal_one_wl_edge_b" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords node-based, banks, equal, one-wl, edge-based, banks in title/desc so the matcher can verify semantic overlap.

## Slide 05: key-result

Heading: Key Result

### Cue 1: `cue_s05_c1_result_state_art_across_board`

- Preferred role: `result`
- Cue keywords: `result, state, art, across, board`
- Narration: The result is state of the art across the board.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c1_result_state_art_across_board" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, state, art, across, board in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_zinc_12k_ppgn_plus_plus_degree_six`

- Preferred role: `result`
- Cue keywords: `zinc-12k, ppgn, plus, plus, degree-six, polynomial, features, reaches, 0.071, test`
- Narration: On ZINC-12K, PPGN plus plus with degree-six polynomial features reaches 0.071 test error, beating CIN at 0.079 and GIN at 0.163.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c2_zinc_12k_ppgn_plus_plus_degree_six" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords zinc-12k, ppgn, plus, plus, degree-six, polynomial in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_zinc_full_hits_0_020_alchemy_0_109`

- Preferred role: `content`
- Cue keywords: `zinc-full, hits, 0.020, alchemy, 0.109, both, best, class`
- Narration: On ZINC-full it hits 0.020 and on Alchemy 0.109, both best in class.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_zinc_full_hits_0_020_alchemy_0_109" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords zinc-full, hits, 0.020, alchemy, 0.109, both in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_features_model_agnostic_adding_them`

- Preferred role: `result`
- Cue keywords: `features, model-agnostic, adding, them, plain, gatedgcn, cuts, its, zinc, error`
- Narration: And the features are model-agnostic: adding them to a plain GatedGCN cuts its ZINC error from 0.265 to 0.106, all under a modest parameter budget.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c4_features_model_agnostic_adding_them" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords features, model-agnostic, adding, them, plain, gatedgcn in title/desc so the matcher can verify semantic overlap.

## Slide 06: takeaway

Heading: Takeaway

### Cue 1: `cue_s06_c1_lasting_message_express_network_powe`

- Preferred role: `content`
- Cue keywords: `lasting, message, express, network, power, which, equivariant, graph, polynomials, compute`
- Narration: The lasting message: express a network's power as which equivariant graph polynomials it can compute.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_lasting_message_express_network_powe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, express, network, power, which in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_small_multi_graph_evaluated_tensor_c`

- Preferred role: `guidance`
- Cue keywords: `small, multi-graph, evaluated, tensor, contraction, finer, ruler, weisfeiler-lehman, direct, list`
- Narration: Each is a small multi-graph evaluated by a tensor contraction, a finer ruler than Weisfeiler-Lehman and a direct list of missing operations.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s06_c2_small_multi_graph_evaluated_tensor_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords small, multi-graph, evaluated, tensor, contraction, finer in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_acting_list_precomputed_polynomial_f`

- Preferred role: `content`
- Cue keywords: `acting, list, precomputed, polynomial, features, push, ordinary, graph, networks, past`
- Narration: Acting on that list, precomputed polynomial features push ordinary graph networks past three-WL to best-in-class molecular property prediction.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_acting_list_precomputed_polynomial_f" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords acting, list, precomputed, polynomial, features, push in title/desc so the matcher can verify semantic overlap.
