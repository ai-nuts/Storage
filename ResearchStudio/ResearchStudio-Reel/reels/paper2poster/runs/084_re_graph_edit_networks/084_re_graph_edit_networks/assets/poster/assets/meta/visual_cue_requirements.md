# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_reproducibility_study_graph_edit_net`

- Preferred role: `content`
- Cue keywords: `reproducibility, study, graph, edit, networks, graph, neural, network, output, layer`
- Narration: This is a reproducibility study of Graph Edit Networks, a graph neural network output layer that predicts how a graph changes over time as a sequence of interpretable edits.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_reproducibility_study_graph_edit_net" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reproducibility, study, graph, edit, networks, graph in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_reproduction_re_implements_re_tests`

- Preferred role: `content`
- Cue keywords: `reproduction, re-implements, re-tests, four, experimental, claims`
- Narration: The reproduction re-implements the model and re-tests the paper's four experimental claims.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_reproduction_re_implements_re_tests" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reproduction, re-implements, re-tests, four, experimental, claims in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_graph_time_series_prediction_asks_fo`

- Preferred role: `title`
- Cue keywords: `graph, time-series, prediction, asks, forecast, next, graph, sequence, not, just`
- Narration: Graph time-series prediction asks a model to forecast the next graph in a sequence, not just a label.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c1_graph_time_series_prediction_asks_fo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, time-series, prediction, asks, forecast, next in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_standard_graph_networks_emit_node`

- Preferred role: `method`
- Cue keywords: `standard, graph, networks, emit, node, edge, probabilities, which, naturally, express`
- Narration: Standard graph networks emit node or edge probabilities, which can't naturally express the structural operations that transform one graph into the next.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_standard_graph_networks_emit_node" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords standard, graph, networks, emit, node, edge in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_graph_edit_networks_close_gap`

- Preferred role: `content`
- Cue keywords: `graph, edit, networks, close, gap, predicting, explicit, human-readable, edit, script`
- Narration: Graph Edit Networks close this gap by predicting an explicit, human-readable edit script.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_graph_edit_networks_close_gap" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, edit, networks, close, gap, predicting in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_original_work_claims_beats_every`

- Preferred role: `result`
- Cue keywords: `original, work, claims, beats, every, baseline, reaches, perfect, accuracy, trees`
- Narration: The original work claims it beats every baseline, reaches perfect accuracy on trees, and scales to large graphs, but those claims rest on briefly-described benchmarks, where independent reproduction adds value.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c2_original_work_claims_beats_every" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords original, work, claims, beats, every, baseline in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_reproduction_contributes_four_things`

- Preferred role: `method`
- Cue keywords: `reproduction, contributes, four, things, re-runs, baseline, check, claim, documents, synthetic`
- Narration: The reproduction contributes four things: it re-runs the model and baseline to check each claim; it documents the synthetic data generators the paper omitted; it adds a cleaner setup separating training and test series; and it shows some benchmarks let the model win by memorising seen transitions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_reproduction_contributes_four_things" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reproduction, contributes, four, things, re-runs, baseline in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_graph_edit_network_attaches_standard`

- Preferred role: `content`
- Cue keywords: `graph, edit, network, attaches, standard, gnn, backbone, predicts, script, edits`
- Narration: A graph edit network attaches to a standard GNN backbone and predicts a script of edits: insert, delete or replace a node, or insert or delete an edge.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_graph_edit_network_attaches_standard" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, edit, network, attaches, standard, gnn in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_applying_them_sequence_maps_current`

- Preferred role: `content`
- Cue keywords: `applying, them, sequence, maps, current, graph, next`
- Narration: Applying them in sequence maps the current graph to the next.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_applying_them_sequence_maps_current" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords applying, them, sequence, maps, current, graph in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_reference_mappings_graph_edit_distan`

- Preferred role: `method`
- Cue keywords: `reference, mappings, graph-edit-distance, approximators, two, loss, variants, hinge, cross-entropy, edge-filtering`
- Narration: Training uses reference mappings from graph-edit-distance approximators, with two loss variants, hinge and cross-entropy, and edge-filtering for citation graphs.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_reference_mappings_graph_edit_distan" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reference, mappings, graph-edit-distance, approximators, two, loss in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_benchmarks_span_three_families_dynam`

- Preferred role: `result`
- Cue keywords: `benchmarks, span, three, families, dynamical, graph, systems, like, edit, cycles`
- Narration: Benchmarks span three families: dynamical graph systems like Edit Cycles, Degree Rules and Game of Life; tree systems for Boolean-formula simplification and Peano addition; and, for scaling, an arXiv citation network of about twenty-seven thousand papers yielding fifteen hundred sub-graphs up to nearly three thousand nodes.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_benchmarks_span_three_families_dynam" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords benchmarks, span, three, families, dynamical, graph in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_three_four_original_claims_hold`

- Preferred role: `method`
- Cue keywords: `three, four, original, claims, hold, beats, variational-autoencoder, baseline, every, dynamical`
- Narration: Three of the four original claims hold: the model beats the variational-autoencoder baseline on every dynamical task, reaches near-perfect accuracy on trees, and its forward pass grows sub-quadratically.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_three_four_original_claims_hold" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords three, four, original, claims, hold, beats in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_fourth_fails_backward_passes_claimed`

- Preferred role: `content`
- Cue keywords: `fourth, fails, backward, passes, claimed, scale, linearly, but, fitted, exponent`
- Narration: The fourth fails: backward passes were claimed to scale linearly, but the fitted exponent is clearly above one.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_fourth_fails_backward_passes_claimed" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fourth, fails, backward, passes, claimed, scale in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_two_robustness_checks_swapping_ad_ho`

- Preferred role: `method`
- Cue keywords: `two, robustness, checks, swapping, ad-hoc, initialisation, erd, nyi, configuration-model, generators`
- Narration: Two robustness checks: swapping the ad-hoc initialisation for Erdős–Rényi and configuration-model generators barely changes any metric, and adding a proper held-out test set lowers scores slightly.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_two_robustness_checks_swapping_ad_ho" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, robustness, checks, swapping, ad-hoc, initialisation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_but_deeper_diagnostic_finds_tree`

- Preferred role: `title`
- Cue keywords: `but, deeper, diagnostic, finds, tree, generators, mostly, produce, unsimplifiable, trees`
- Narration: But a deeper diagnostic finds the tree generators mostly produce unsimplifiable trees, only thirteen percent of Boolean and twenty-six percent of Peano samples are usable, undercutting those tasks.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s08_c2_but_deeper_diagnostic_finds_tree" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, deeper, diagnostic, finds, tree, generators in title/desc so the matcher can verify semantic overlap.

## Slide 09: takeaway

Heading: Takeaway

### Cue 1: `cue_s09_c1_verdict_nuanced_graph_edit_networks`

- Preferred role: `content`
- Cue keywords: `verdict, nuanced, graph, edit, networks, reproducible, elegant, interpretable, most, claims`
- Narration: The verdict is nuanced: Graph Edit Networks are reproducible, elegant and interpretable, and most claims hold.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_verdict_nuanced_graph_edit_networks" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords verdict, nuanced, graph, edit, networks, reproducible in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_but_one_scaling_claim_wrong`

- Preferred role: `result`
- Cue keywords: `but, one, scaling, claim, wrong, backward, passes, super-linear, several, benchmarks`
- Narration: But one scaling claim is wrong, backward passes are super-linear, and several benchmarks reward memorising seen transitions rather than genuine generalisation.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_but_one_scaling_claim_wrong" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, one, scaling, claim, wrong, backward in title/desc so the matcher can verify semantic overlap.
