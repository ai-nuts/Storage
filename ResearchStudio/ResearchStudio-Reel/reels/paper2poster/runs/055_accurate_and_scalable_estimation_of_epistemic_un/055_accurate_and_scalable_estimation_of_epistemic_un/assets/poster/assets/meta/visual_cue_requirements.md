# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_graph_neural_networks_increasingly_d`

- Preferred role: `method`
- Cue keywords: `graph, neural, networks, increasingly, deployed, safety-critical, settings, but, their, confidence`
- Narration: Graph neural networks are increasingly deployed in safety-critical settings, but their confidence estimates often become unreliable when the test data shifts away from training.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_graph_neural_networks_increasingly_d" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, neural, networks, increasingly, deployed, safety-critical in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_university_michigan_lawrence_livermo`

- Preferred role: `method`
- Cue keywords: `university, michigan, lawrence, livermore, national, laboratory, introduces, g-delta-uq, single-model, method`
- Narration: This paper, from the University of Michigan and Lawrence Livermore National Laboratory, introduces G-Delta-UQ, a single-model method for estimating epistemic uncertainty in graph neural networks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_university_michigan_lawrence_livermo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords university, michigan, lawrence, livermore, national, laboratory in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_adapting_stochastic_centering_partia`

- Preferred role: `method`
- Cue keywords: `adapting, stochastic, centering, partial, stochasticity, structured, graph, g-delta-uq, produces, better-calibrated`
- Narration: By adapting stochastic centering and partial stochasticity to structured graph data, G-Delta-UQ produces better-calibrated confidence indicators across size, concept, and covariate distribution shifts, and improves downstream tasks like out-of-distribution detection and generalization gap prediction.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_adapting_stochastic_centering_partia" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords adapting, stochastic, centering, partial, stochasticity, structured in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_graph_neural_networks_being_deployed`

- Preferred role: `method`
- Cue keywords: `graph, neural, networks, being, deployed, high-stakes, applications, where, test-time, rarely`
- Narration: Graph neural networks are being deployed in high-stakes applications where the test-time data rarely matches training conditions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_graph_neural_networks_being_deployed" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, neural, networks, being, deployed, high-stakes in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_these_shifted_settings_downstream_sa`

- Preferred role: `method`
- Cue keywords: `these, shifted, settings, downstream, safety, metrics, such, calibration, error, out-of-distribution`
- Narration: In these shifted settings, downstream safety metrics such as calibration error, out-of-distribution rejection, and generalization gap prediction all rely on the model's confidence indicators.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_these_shifted_settings_downstream_sa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, shifted, settings, downstream, safety, metrics in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_while_computer_vision_community_long`

- Preferred role: `method`
- Cue keywords: `while, computer, vision, community, long, known, confidence, quality, deteriorates, under`
- Narration: While the computer vision community has long known that confidence quality deteriorates under distribution shift, this behavior has remained under-explored for graph neural networks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_while_computer_vision_community_long" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords while, computer, vision, community, long, known in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_asks_whether_gnn_confidence_indicato`

- Preferred role: `method`
- Cue keywords: `asks, whether, gnn, confidence, indicators, made, reliable, under, realistic, structural`
- Narration: This paper asks whether GNN confidence indicators can be made reliable under realistic structural, size, concept, and covariate shifts.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_asks_whether_gnn_confidence_indicato" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords asks, whether, gnn, confidence, indicators, made in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_common_expectation_adopting_more_adv`

- Preferred role: `figure`
- Cue keywords: `common, expectation, adopting, more, advanced, expressive, architectures, will, inherently, improve`
- Narration: There is a common expectation that adopting more advanced or expressive architectures will inherently improve calibration.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s03_c1_common_expectation_adopting_more_adv" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords common, expectation, adopting, more, advanced, expressive in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_through_controlled_case_study_struct`

- Preferred role: `method`
- Cue keywords: `through, controlled, case, study, structural, distortion, benchmark, authors, demonstrate, expectation`
- Narration: Through a controlled case study on a structural distortion benchmark, the authors demonstrate this expectation is false: graph transformers and positional encodings do not meaningfully improve calibration over vanilla message-passing networks, and increasing model size can even make calibration worse.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_through_controlled_case_study_struct" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords through, controlled, case, study, structural, distortion in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_finding_motivates_different_path`

- Preferred role: `content`
- Cue keywords: `finding, motivates, different, path`
- Narration: This finding motivates a different path.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_finding_motivates_different_path" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finding, motivates, different, path in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_rather_chasing_expressivity_advocate`

- Preferred role: `content`
- Cue keywords: `rather, chasing, expressivity, advocates, epistemic, uncertainty, quantification, directly, modulate, confidence`
- Narration: Rather than chasing expressivity, the paper advocates for epistemic uncertainty quantification to directly modulate confidence indicators.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_rather_chasing_expressivity_advocate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rather, chasing, expressivity, advocates, epistemic, uncertainty in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, contributions`
- Narration: The paper makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_rigorous_case_study_establishi`

- Preferred role: `method`
- Cue keywords: `first, rigorous, case, study, establishing, improving, graph, neural, network, expressivity`
- Narration: First, a rigorous case study establishing that improving graph neural network expressivity does not mitigate poor calibration under distribution shift.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_rigorous_case_study_establishi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, rigorous, case, study, establishing, improving in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_g_delta_uq_novel_single_model`

- Preferred role: `method`
- Cue keywords: `second, g-delta-uq, novel, single-model, uncertainty, method, extends, stochastic, centering, framework`
- Narration: Second, G-Delta-UQ, a novel single-model uncertainty method that extends the stochastic centering framework to structured graph data and, crucially, supports partial stochasticity so that only part of the network is made stochastic.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_g_delta_uq_novel_single_model" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, g-delta-uq, novel, single-model, uncertainty, method in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_extensive_empirical_evaluation`

- Preferred role: `method`
- Cue keywords: `third, extensive, empirical, evaluation, spanning, covariate, concept, graph, size, shifts`
- Narration: Third, an extensive empirical evaluation spanning covariate, concept, and graph size shifts, across the safety-critical tasks of calibration, generalization gap prediction, and out-of-distribution detection.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_third_extensive_empirical_evaluation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, extensive, empirical, evaluation, spanning, covariate in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_g_delta_uq_builds_principle_stochast`

- Preferred role: `result`
- Cue keywords: `g-delta-uq, builds, principle, stochastic, anchoring, input, sample, transformed, relative, representation`
- Narration: G-Delta-UQ builds on the principle of stochastic anchoring. Each input sample is transformed into a relative representation by subtracting a randomly chosen anchor and concatenating it channel-wise, producing an anchored input.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c1_g_delta_uq_builds_principle_stochast" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords g-delta-uq, builds, principle, stochastic, anchoring, input in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_varying_anchor_across_iterations_emu`

- Preferred role: `method`
- Cue keywords: `varying, anchor, across, iterations, emulates, sampling, distribution, hypotheses, variance, predictions`
- Narration: By varying the anchor across iterations, the model emulates sampling from a distribution of hypotheses, and the variance of predictions over multiple anchors captures epistemic uncertainty.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_varying_anchor_across_iterations_emu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords varying, anchor, across, iterations, emulates, sampling in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_because_directly_anchoring_graph_adj`

- Preferred role: `content`
- Cue keywords: `because, directly, anchoring, graph, adjacency, would, introduce, artificial, edges, authors`
- Narration: Because directly anchoring on graph adjacency would introduce artificial edges, the authors anchor in node-feature or hidden-representation space. They introduce three variants, applying anchoring at the node features, at an intermediate message-passing layer, or after the readout.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_because_directly_anchoring_graph_adj" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, directly, anchoring, graph, adjacency, would in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_particularly_practical_variant_freez`

- Preferred role: `method`
- Cue keywords: `particularly, practical, variant, freezes, pretrained, backbone, only, trains, anchored, classifier`
- Narration: A particularly practical variant freezes a pretrained backbone and only trains an anchored classifier head, delivering inexpensive, partial stochasticity. At inference, predictions are averaged over K anchors to produce both a calibrated prediction and an uncertainty estimate.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_particularly_practical_variant_freez" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords particularly, practical, variant, freezes, pretrained, backbone in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_evaluation_deliberately_broad_struct`

- Preferred role: `method`
- Cue keywords: `evaluation, deliberately, broad, structural, shift, authors, build, rotated, super-pixel, mnist`
- Narration: The evaluation is deliberately broad. For structural shift, the authors build a Rotated Super-pixel MNIST benchmark where increasing rotation induces controlled distortion.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_evaluation_deliberately_broad_struct" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, deliberately, broad, structural, shift, authors in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_size_shift_they_standard_graph`

- Preferred role: `result`
- Cue keywords: `size, shift, they, standard, graph, classification, datasets, including, nci1, nci109`
- Narration: For size shift, they use standard graph classification datasets including D and D, NCI1, NCI109, and PROTEINS with GCN, GIN, and PNA backbones.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_size_shift_they_standard_graph" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords size, shift, they, standard, graph, classification in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_concept_covariate_shifts_they_good`

- Preferred role: `result`
- Cue keywords: `concept, covariate, shifts, they, good, benchmark, suite, covering, colored, mnist`
- Narration: For concept and covariate shifts, they use the GOOD benchmark suite covering colored MNIST, motif, and SST2 datasets.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c3_concept_covariate_shifts_they_good" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords concept, covariate, shifts, they, good, benchmark in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_across_all_these_they_compare`

- Preferred role: `method`
- Cue keywords: `across, all, these, they, compare, against, strong, uncertainty, baselines, including`
- Narration: Across all of these they compare against strong uncertainty baselines including deep ensembles, temperature scaling, and Monte Carlo dropout, measuring calibration error, out-of-distribution detection AUROC, and generalization gap mean absolute error.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_across_all_these_they_compare" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, all, these, they, compare, against in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_across_board_g_delta_uq_improves_rel`

- Preferred role: `method`
- Cue keywords: `across, board, g-delta-uq, improves, reliability, confidence, indicators, structural, distortion, benchmark`
- Narration: Across the board, G-Delta-UQ improves the reliability of confidence indicators. On the structural distortion benchmark it achieves substantial reductions in expected calibration error even at severe rotations, while keeping accuracy close to the vanilla model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_across_board_g_delta_uq_improves_rel" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, board, g-delta-uq, improves, reliability, confidence in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_under_size_shift_last_layer_anchorin`

- Preferred role: `result`
- Cue keywords: `under, size, shift, last-layer, anchoring, lowers, calibration, error, while, maintaining`
- Narration: Under size shift, last-layer anchoring lowers calibration error while maintaining or improving accuracy, with the largest gains on the most severe shift.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_under_size_shift_last_layer_anchorin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords under, size, shift, last-layer, anchoring, lowers in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_under_concept_covariate_shifts_deliv`

- Preferred role: `method`
- Cue keywords: `under, concept, covariate, shifts, delivers, competitive, in-distribution, out-of-distribution, accuracy, alongside`
- Narration: Under concept and covariate shifts it delivers competitive in-distribution and out-of-distribution accuracy alongside better calibration than other single-model methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_under_concept_covariate_shifts_deliv" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords under, concept, covariate, shifts, delivers, competitive in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_when_its_confidence_estimates_feed`

- Preferred role: `method`
- Cue keywords: `when, its, confidence, estimates, feed, downstream, tasks, among, best, single-model`
- Narration: And when its confidence estimates feed downstream tasks, it is among the best single-model estimators for generalization gap prediction and is highly competitive for out-of-distribution detection, with the pretrained variant frequently the strongest under covariate shift.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_when_its_confidence_estimates_feed" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, its, confidence, estimates, feed, downstream in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_carefully_ablates_where_stochastic_a`

- Preferred role: `content`
- Cue keywords: `carefully, ablates, where, stochastic, anchoring, should, applied`
- Narration: The paper carefully ablates where stochastic anchoring should be applied.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_carefully_ablates_where_stochastic_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords carefully, ablates, where, stochastic, anchoring, should in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_dataset_which_most_severe_size`

- Preferred role: `result`
- Cue keywords: `dataset, which, most, severe, size, shift, applying, anchoring, after, readout`
- Narration: On the D and D dataset, which has the most severe size shift, applying anchoring after the readout layer dramatically improves both accuracy and calibration as network depth grows, while earlier-layer anchoring converges less well.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_dataset_which_most_severe_size" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dataset, which, most, severe, size, shift in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_leads_practical_recommendation_ancho`

- Preferred role: `content`
- Cue keywords: `leads, practical, recommendation, anchor, last, layer, size-shift, settings`
- Narration: This leads to a practical recommendation to anchor at the last layer for size-shift settings.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_leads_practical_recommendation_ancho" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords leads, practical, recommendation, anchor, last, layer in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_authors_also_validate_partial_stocha`

- Preferred role: `method`
- Cue keywords: `authors, also, validate, partial, stochasticity, form, pretrained, variant, only, trains`
- Narration: The authors also validate that partial stochasticity, in the form of the pretrained variant that only trains an anchored classifier head, is both effective and scalable, and a neural tangent kernel analysis confirms that intermediate constant shifts truly alter the model's function rather than acting as a trivial reparameterization.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_authors_also_validate_partial_stocha" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, also, validate, partial, stochasticity, form in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_numbers_g_delta_uq_single_model_meth`

- Preferred role: `method`
- Cue keywords: `numbers, g-delta-uq, single-model, method, offering, three, anchoring, variants, plus, pretrained`
- Narration: In numbers, G-Delta-UQ is a single-model method offering three anchoring variants plus a pretrained partial-stochasticity option.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_numbers_g_delta_uq_single_model_meth" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords numbers, g-delta-uq, single-model, method, offering, three in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_evaluated_across_three_distinct_type`

- Preferred role: `method`
- Cue keywords: `evaluated, across, three, distinct, types, distribution, shift, three, safety-critical, downstream`
- Narration: It is evaluated across three distinct types of distribution shift and three safety-critical downstream tasks, and compared against four established uncertainty baselines including deep ensembles.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_evaluated_across_three_distinct_type" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluated, across, three, distinct, types, distribution in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_despite_requiring_only_single_consis`

- Preferred role: `method`
- Cue keywords: `despite, requiring, only, single, consistently, matches, outperforms, these, baselines, calibration`
- Narration: Despite requiring only a single model, it consistently matches or outperforms these baselines on calibration, out-of-distribution detection, and generalization gap prediction.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_despite_requiring_only_single_consis" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords despite, requiring, only, single, consistently, matches in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_core_message_simple`

- Preferred role: `content`
- Cue keywords: `core, message, simple`
- Narration: The core message is simple.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c1_core_message_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, message, simple in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_not_expect_larger_more_expressive`

- Preferred role: `method`
- Cue keywords: `not, expect, larger, more, expressive, graph, neural, networks, automatically, give`
- Narration: Do not expect larger or more expressive graph neural networks to automatically give trustworthy confidence estimates under distribution shift.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_not_expect_larger_more_expressive" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords not, expect, larger, more, expressive, graph in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_instead_adapt_principle_stochastic_a`

- Preferred role: `content`
- Cue keywords: `instead, adapt, principle, stochastic, anchoring, graphs`
- Narration: Instead, adapt the principle of stochastic anchoring to graphs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_instead_adapt_principle_stochastic_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, adapt, principle, stochastic, anchoring, graphs in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_g_delta_uq_flexible_scalable_single`

- Preferred role: `method`
- Cue keywords: `g-delta-uq, flexible, scalable, single-model, framework, produces, reliable, well-calibrated, uncertainty, across`
- Narration: G-Delta-UQ is a flexible, scalable, single-model framework that produces reliable, well-calibrated uncertainty across structural, size, concept, and covariate shifts, and its pretrained variant makes it inexpensive to add to models you already have.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c4_g_delta_uq_flexible_scalable_single" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords g-delta-uq, flexible, scalable, single-model, framework, produces in title/desc so the matcher can verify semantic overlap.
