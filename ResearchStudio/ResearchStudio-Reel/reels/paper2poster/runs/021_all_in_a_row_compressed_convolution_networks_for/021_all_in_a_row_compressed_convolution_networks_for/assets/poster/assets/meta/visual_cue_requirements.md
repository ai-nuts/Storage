# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_all_row_compressed_convolution_netwo`

- Preferred role: `content`
- Cue keywords: `all, row, compressed, convolution, networks, graphs, icml, 2023, chinese, academy`
- Narration: This is All in a Row: Compressed Convolution Networks for Graphs, an ICML 2023 paper from the Chinese Academy of Sciences.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_all_row_compressed_convolution_netwo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords all, row, compressed, convolution, networks, graphs in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_run_standard_cnn_style_euclidean_con`

- Preferred role: `content`
- Cue keywords: `run, standard, cnn-style, euclidean, convolution, directly, graphs`
- Narration: Can we run standard, CNN-style Euclidean convolution directly on graphs?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_run_standard_cnn_style_euclidean_con" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords run, standard, cnn-style, euclidean, convolution, directly in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_yes_learn_differentiable_permutation`

- Preferred role: `content`
- Cue keywords: `yes, learn, differentiable, permutation, lines, nodes, row, kernel, across, them`
- Narration: Yes: learn a differentiable permutation that lines nodes in a row, then slide a kernel across them.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_yes_learn_differentiable_permutation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords yes, learn, differentiable, permutation, lines, nodes in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_cocn_sets_state_art`

- Preferred role: `content`
- Cue keywords: `cocn, sets, state, art`
- Narration: The model, CoCN, sets state of the art.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c4_cocn_sets_state_art" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cocn, sets, state, art in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_convolutional_graph_networks_two_wea`

- Preferred role: `content`
- Cue keywords: `convolutional, graph, networks, two, weaknesses, because, their, filters, come, graph`
- Narration: Convolutional graph networks have two weaknesses. Because their filters come from graph polynomials, they lack expressiveness on a small parameter budget.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_convolutional_graph_networks_two_wea" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords convolutional, graph, networks, two, weaknesses, because in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_they_cannot_learn_hierarchical_multi`

- Preferred role: `content`
- Cue keywords: `they, cannot, learn, hierarchical, multi-scale, features, alone, needing, bolt-on, tricks`
- Narration: And they cannot learn hierarchical, multi-scale features alone, needing bolt-on tricks like clustering or node dropping.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_they_cannot_learn_hierarchical_multi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, cannot, learn, hierarchical, multi-scale, features in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_image_cnns_neither_problem_local`

- Preferred role: `content`
- Cue keywords: `image, cnns, neither, problem, local, learning, shared, filters, naturally, capture`
- Narration: Image CNNs have neither problem: local learning and shared filters naturally capture multi-scale patterns.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_image_cnns_neither_problem_local" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords image, cnns, neither, problem, local, learning in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_but_their_euclidean_convolution_assu`

- Preferred role: `content`
- Cue keywords: `but, their, euclidean, convolution, assumes, regular, grid, does, not, fit`
- Narration: But their Euclidean convolution assumes a regular grid, and does not fit irregular graphs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_but_their_euclidean_convolution_assu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, their, euclidean, convolution, assumes, regular in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_why_not_borrow_euclidean_convolution`

- Preferred role: `content`
- Cue keywords: `why, not, borrow, euclidean, convolution, graphs`
- Narration: So why not borrow Euclidean convolution for graphs?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_why_not_borrow_euclidean_convolution" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords why, not, borrow, euclidean, convolution, graphs in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_convolution_sensitive_spatial_order`

- Preferred role: `content`
- Cue keywords: `convolution, sensitive, spatial, order, but, graph, networks, must, permutation, invariant`
- Narration: Convolution is sensitive to spatial order, but graph networks must be permutation invariant.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_convolution_sensitive_spatial_order" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords convolution, sensitive, spatial, order, but, graph in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_earlier_methods_picked_node_ordering`

- Preferred role: `method`
- Cue keywords: `earlier, methods, picked, node, ordering, independently, convolution, could, not, tuned`
- Narration: Earlier methods picked a node ordering independently of the convolution, so it could not be tuned for the task and often lost information.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_earlier_methods_picked_node_ordering" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords earlier, methods, picked, node, ordering, independently in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_what_missing_ordering_differentiable`

- Preferred role: `content`
- Cue keywords: `what, missing, ordering, differentiable, learned, end, end`
- Narration: What is missing is an ordering that is differentiable and learned end to end.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_what_missing_ordering_differentiable" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, missing, ordering, differentiable, learned, end in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_two_contributions`

- Preferred role: `content`
- Cue keywords: `makes, two, contributions`
- Narration: The paper makes two contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_two_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, two, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_differentiable_regularization`

- Preferred role: `content`
- Cue keywords: `first, differentiable, regularization, graphs, learnable, permutation, lines, nodes, single, row`
- Narration: First, a differentiable regularization for graphs: a learnable permutation that lines nodes into a single row while preserving permutation invariance, so Euclidean convolution finally applies.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_first_differentiable_regularization" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, differentiable, regularization, graphs, learnable, permutation in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_built_compressed_convolution`

- Preferred role: `content`
- Cue keywords: `second, built, compressed, convolution, network, cocn`
- Narration: Second, the model built on it, the Compressed Convolution Network, or CoCN.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_second_built_compressed_convolution" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, built, compressed, convolution, network, cocn in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_learns_both_node_structure_features`

- Preferred role: `method`
- Cue keywords: `learns, both, node, structure, features, trains, end, end, beating, competitive`
- Narration: It learns both node and structure features and trains end to end, beating competitive GNNs and pooling models.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_learns_both_node_structure_features" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords learns, both, node, structure, features, trains in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_how_cocn_works_first_permutation`

- Preferred role: `content`
- Cue keywords: `how, cocn, works, first, permutation, generation, regresses, absolute, position, node`
- Narration: Here is how CoCN works. First, permutation generation regresses an absolute position for each node with an MLP on Laplacian-smoothed features, so similar nodes land nearby.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_how_cocn_works_first_permutation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, cocn, works, first, permutation, generation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_these_form_relaxed_permutation_matri`

- Preferred role: `content`
- Cue keywords: `these, form, relaxed, permutation, matrix, controlled, factor, tau, provably, converges`
- Narration: These form a relaxed permutation matrix, controlled by a factor tau that provably converges to a true permutation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_these_form_relaxed_permutation_matri" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, form, relaxed, permutation, matrix, controlled in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_nodes_row_cocn_slides_kernel`

- Preferred role: `method`
- Cue keywords: `nodes, row, cocn, slides, kernel, along, diagonal, permuted, edge, node`
- Narration: With nodes in a row, CoCN slides a kernel along the diagonal of the permuted edge and node matrices, extracting node features and their structure together.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_nodes_row_cocn_slides_kernel" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords nodes, row, cocn, slides, kernel, along in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_compressed_pooling_builds_hierarchy`

- Preferred role: `content`
- Cue keywords: `compressed, pooling, builds, hierarchy, transposed, convolution, up-samples, predictions, crucially, cuts`
- Narration: Compressed pooling builds a hierarchy, and transposed convolution up-samples for predictions. Crucially, this cuts permutation modeling from n factorial to n squared, letting it scale to large graphs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_compressed_pooling_builds_hierarchy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords compressed, pooling, builds, hierarchy, transposed, convolution in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_evaluation_broad`

- Preferred role: `result`
- Cue keywords: `evaluation, broad`
- Narration: The evaluation is broad.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_evaluation_broad" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, broad in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_graph_classification_six_datasets_mu`

- Preferred role: `result`
- Cue keywords: `graph, classification, six, datasets, mutag, proteins, nci1, collab, imdb-binary, imdb-multi`
- Narration: For graph classification, six datasets: MUTAG, PROTEINS, NCI1, COLLAB, IMDB-Binary, and IMDB-Multi, under ten-fold cross-validation.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_graph_classification_six_datasets_mu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, classification, six, datasets, mutag, proteins in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_node_classification_six_heterophilic`

- Preferred role: `result`
- Cue keywords: `node, classification, six, heterophilic, benchmarks, chameleon, squirrel, cornell, texas, wisconsin`
- Narration: For node classification, six heterophilic benchmarks: Chameleon, Squirrel, Cornell, Texas, Wisconsin, and Actor.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c3_node_classification_six_heterophilic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords node, classification, six, heterophilic, benchmarks, chameleon in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_rule_out_leakage_they_test`

- Preferred role: `guidance`
- Cue keywords: `rule, out, leakage, they, test, filtered, chameleon, squirrel, scale, mini-batch`
- Narration: To rule out leakage they test filtered Chameleon and Squirrel, and for scale, mini-batch experiments on three graphs with hundreds of thousands of nodes.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s06_c4_rule_out_leakage_they_test" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rule, out, leakage, they, test, filtered in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_results_strong_across_board`

- Preferred role: `method`
- Cue keywords: `results, strong, across, board`
- Narration: Results are strong across the board.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_results_strong_across_board" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, strong, across, board in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_node_classification_cocn_gets_best`

- Preferred role: `result`
- Cue keywords: `node, classification, cocn, gets, best, average, rank, one, point, eight`
- Narration: On node classification, CoCN gets the best average rank, one point eight three, topping Chameleon at seventy-nine percent, Squirrel at seventy-three, and Cornell at eighty-six.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_node_classification_cocn_gets_best" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords node, classification, cocn, gets, best, average in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_graph_classification_wins_five_six`

- Preferred role: `result`
- Cue keywords: `graph, classification, wins, five, six, datasets, including, collab, imdb-multi`
- Narration: On graph classification, it wins five of six datasets, including COLLAB and IMDB-Multi.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_graph_classification_wins_five_six" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, classification, wins, five, six, datasets in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_filtered_chameleon_squirrel_duplicat`

- Preferred role: `content`
- Cue keywords: `filtered, chameleon, squirrel, duplicates, removed, ranks, first, eighteen, models, its`
- Narration: And on filtered Chameleon and Squirrel, with duplicates removed, it ranks first of eighteen models, so its edge is not data leakage.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_filtered_chameleon_squirrel_duplicat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords filtered, chameleon, squirrel, duplicates, removed, ranks in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_several_ablations_show_why_cocn`

- Preferred role: `content`
- Cue keywords: `several, ablations, show, why, cocn, works`
- Narration: Several ablations show why CoCN works.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_several_ablations_show_why_cocn" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords several, ablations, show, why, cocn, works in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_first_permutation_heads_matter_more`

- Preferred role: `result`
- Cue keywords: `first, permutation, heads, matter, more, permutations, accuracy, rises, consistently, mutag`
- Narration: First, permutation heads matter: with more permutations, accuracy rises consistently on MUTAG, Chameleon, Cornell, and Wisconsin, since each exposes different node arrangements.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_first_permutation_heads_matter_more" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, permutation, heads, matter, more, permutations in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_second_larger_diagonal_kernels_give`

- Preferred role: `content`
- Cue keywords: `second, larger, diagonal, kernels, give, bigger, receptive, field, better, performance`
- Narration: Second, larger diagonal kernels give a bigger receptive field and better performance, without over-smoothing.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_second_larger_diagonal_kernels_give" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, larger, diagonal, kernels, give, bigger in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_third_information_loss_study_finds_r`

- Preferred role: `figure`
- Cue keywords: `third, information-loss, study, finds, relaxed, permutations, preserve, almost, all, information`
- Narration: Third, an information-loss study finds the relaxed permutations preserve almost all information, so the regularization is lossless.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c4_third_information_loss_study_finds_r" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, information-loss, study, finds, relaxed, permutations in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_cocn_reaches_average_rank_one`

- Preferred role: `method`
- Cue keywords: `cocn, reaches, average, rank, one, point, eight, three, across, six`
- Narration: CoCN reaches an average rank of one point eight three across six node datasets, the best of any method.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_cocn_reaches_average_rank_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cocn, reaches, average, rank, one, point in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_squirrel_scores_nearly_seventy_three`

- Preferred role: `method`
- Cue keywords: `squirrel, scores, nearly, seventy-three, percent, over, eleven, points, above, strongest`
- Narration: On Squirrel it scores nearly seventy-three percent, over eleven points above the strongest prior model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_squirrel_scores_nearly_seventy_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords squirrel, scores, nearly, seventy-three, percent, over in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_collab_hits_eighty_six_percent`

- Preferred role: `content`
- Cue keywords: `collab, hits, eighty-six, percent`
- Narration: On COLLAB it hits eighty-six percent.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_collab_hits_eighty_six_percent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords collab, hits, eighty-six, percent in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_cuts_permutation_modeling_intractabl`

- Preferred role: `content`
- Cue keywords: `cuts, permutation, modeling, intractable, factorial, squared`
- Narration: And it cuts permutation modeling from intractable n factorial to n squared.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_cuts_permutation_modeling_intractabl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cuts, permutation, modeling, intractable, factorial, squared in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_elegant`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, elegant`
- Narration: The takeaway is elegant.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_elegant" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, elegant in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_learn_differentiable_permutation_arr`

- Preferred role: `content`
- Cue keywords: `learn, differentiable, permutation, arranges, graph, nodes, single, row, all, machinery`
- Narration: Learn a differentiable permutation that arranges a graph's nodes into a single row, and all the machinery of image convolution becomes available for graphs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_learn_differentiable_permutation_arr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords learn, differentiable, permutation, arranges, graph, nodes in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_cocn_does_exactly_provably_convergen`

- Preferred role: `result`
- Cue keywords: `cocn, does, exactly, provably, convergent, invariant, reaching, state-of-the-art, results`
- Narration: CoCN does exactly this, provably convergent and invariant, reaching state-of-the-art results.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c3_cocn_does_exactly_provably_convergen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cocn, does, exactly, provably, convergent, invariant in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_graphs_all_row_convolved_like`

- Preferred role: `content`
- Cue keywords: `graphs, all, row, convolved, like, images`
- Narration: Graphs, all in a row, can be convolved like images.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c4_graphs_all_row_convolved_like" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graphs, all, row, convolved, like, images in title/desc so the matcher can verify semantic overlap.
