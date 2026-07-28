# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_molecular_modeling_quantum_mechanics`

- Preferred role: `content`
- Cue keywords: `molecular, modeling, quantum, mechanics, demands, models, respect, physical, laws, namely`
- Narration: Molecular modeling in quantum mechanics demands models that respect physical laws, namely invariance and equivariance to rotation and translation of atomic coordinates.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_molecular_modeling_quantum_mechanics" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords molecular, modeling, quantum, mechanics, demands, models in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_introduces_geomformer_general_flexib`

- Preferred role: `method`
- Cue keywords: `introduces, geomformer, general, flexible, transformer-based, architecture, learns, both, invariant, equivariant`
- Narration: This paper introduces GeoMFormer, a general and flexible Transformer-based architecture that learns both invariant and equivariant molecular representations at once.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_introduces_geomformer_general_flexib" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, geomformer, general, flexible, transformer-based, architecture in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_two_parallel_transformer_streams_one`

- Preferred role: `method`
- Cue keywords: `two, parallel, transformer, streams, one, type, representation, bridges, them, carefully`
- Narration: It uses two parallel Transformer streams, one for each type of representation, and bridges them with carefully designed cross-attention modules so information flows between the two.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_two_parallel_transformer_streams_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, parallel, transformer, streams, one, type in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_many_prior_geometric_models_turn`

- Preferred role: `result`
- Cue keywords: `many, prior, geometric, models, turn, out, special, cases, framework, geomformer`
- Narration: Many prior geometric models turn out to be special cases of this framework, and GeoMFormer sets new state-of-the-art results across a wide range of molecular tasks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c4_many_prior_geometric_models_turn" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords many, prior, geometric, models, turn, out in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_deep_learning_become_powerful_tool`

- Preferred role: `content`
- Cue keywords: `deep, learning, become, powerful, tool, molecular, science, predicting, properties, molecules`
- Narration: Deep learning has become a powerful tool for molecular science, predicting properties of molecules from their three-dimensional coordinates and simulating how atoms move.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_deep_learning_become_powerful_tool" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deep, learning, become, powerful, tool, molecular in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_these_tasks_impose_strict`

- Preferred role: `method`
- Cue keywords: `but, these, tasks, impose, strict, physical, constraints`
- Narration: But these tasks impose strict physical constraints.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_but_these_tasks_impose_strict" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, these, tasks, impose, strict, physical in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_prediction_must_transform_correctly`

- Preferred role: `content`
- Cue keywords: `prediction, must, transform, correctly, when, input, coordinate, system, rotated, translated`
- Narration: A model's prediction must transform correctly when the input coordinate system is rotated or translated, a requirement known as invariance for scalar quantities and equivariance for vector quantities.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_prediction_must_transform_correctly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prediction, must, transform, correctly, when, input in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_existing_methods_handle_these_constr`

- Preferred role: `method`
- Cue keywords: `existing, methods, handle, these, constraints, but, most, built, heuristic, costly`
- Narration: Existing methods handle these constraints, but most are built on heuristic and costly modules, and few offer a single general framework that learns both invariant and equivariant representations effectively at the same time.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_existing_methods_handle_these_constr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords existing, methods, handle, these, constraints, but in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_trouble_existing_geometric_models_th`

- Preferred role: `content`
- Cue keywords: `trouble, existing, geometric, models, they, largely, built, hand`
- Narration: The trouble with existing geometric models is that they are largely built by hand.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_trouble_existing_geometric_models_th" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trouble, existing, geometric, models, they, largely in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_designers_craft_specialized_equivari`

- Preferred role: `method`
- Cue keywords: `designers, craft, specialized, equivariant, modules, either, expensive, scale, constrained, they`
- Narration: Designers craft specialized equivariant modules that are either expensive to scale or so constrained that they sacrifice expressive power, and the resulting architectures grow complex just to guarantee the physical constraints.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_designers_craft_specialized_equivari" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords designers, craft, specialized, equivariant, modules, either in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_more_importantly_real_applications_i`

- Preferred role: `method`
- Cue keywords: `more, importantly, real, applications, increasingly, demand, single, performs, both, invariant`
- Narration: More importantly, real applications increasingly demand a single model that performs both invariant and equivariant prediction with strong accuracy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_more_importantly_real_applications_i" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords more, importantly, real, applications, increasingly, demand in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_clear_need_general_flexible_framewor`

- Preferred role: `guidance`
- Cue keywords: `clear, need, general, flexible, framework, built, well-understood, standard, components, rather`
- Narration: There is a clear need for a general, flexible framework built on well-understood, standard components rather than one-off heuristic modules.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s03_c4_clear_need_general_flexible_framewor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords clear, need, general, flexible, framework, built in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_main_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, main, contributions`
- Narration: The paper makes three main contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_main_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, main, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_introduces_geomformer_novel_tr`

- Preferred role: `method`
- Cue keywords: `first, introduces, geomformer, novel, transformer-based, molecular, maintains, two, separate, streams`
- Narration: First, it introduces GeoMFormer, a novel Transformer-based molecular model that maintains two separate streams, one for invariant and one for equivariant representations, using only standard Transformer building blocks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_introduces_geomformer_novel_tr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, introduces, geomformer, novel, transformer-based, molecular in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_designs_cross_attention_modul`

- Preferred role: `method`
- Cue keywords: `second, designs, cross-attention, modules, bridge, these, two, streams, letting, draw`
- Narration: Second, it designs cross-attention modules that bridge these two streams, letting each draw on contextual information from the other to enhance geometric modeling.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_designs_cross_attention_modul" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, designs, cross-attention, modules, bridge, these in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_shows_framework_general_enough`

- Preferred role: `method`
- Cue keywords: `third, shows, framework, general, enough, many, previously, proposed, architectures, viewed`
- Narration: Third, it shows that this framework is general enough that many previously proposed architectures can be viewed as special instantiations of GeoMFormer, and it backs the design with strong empirical results across a diverse set of molecular tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_third_shows_framework_general_enough" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, shows, framework, general, enough, many in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_geomformer_keeps_two_representations`

- Preferred role: `method`
- Cue keywords: `geomformer, keeps, two, representations, every, atom, invariant, feature, vector, equivariant`
- Narration: GeoMFormer keeps two representations for every atom: an invariant feature vector and an equivariant three-dimensional feature. These flow through two parallel Transformer streams. Within each stream, a self-attention module first mixes information across atoms.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_geomformer_keeps_two_representations" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords geomformer, keeps, two, representations, every, atom in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_equivariant_stream_standard_attentio`

- Preferred role: `method`
- Cue keywords: `equivariant, stream, standard, attention, modified, attention, score, computed, summing, dot`
- Narration: For the equivariant stream, standard attention is modified so the attention score is computed by summing dot products over the three-dimensional Query and Key vectors, which provably preserves equivariance.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_equivariant_stream_standard_attentio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords equivariant, stream, standard, attention, modified, attention in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_key_innovation_cross_attention_modul`

- Preferred role: `method`
- Cue keywords: `key, innovation, cross-attention, module, lets, stream, query, other, invariant, stream`
- Narration: Then, the key innovation, a cross-attention module lets each stream query the other: the invariant stream attends to the equivariant stream and vice versa, fusing the two kinds of geometric information.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_key_innovation_cross_attention_modul" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, innovation, cross-attention, module, lets, stream in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_feed_forward_network_completes_block`

- Preferred role: `method`
- Cue keywords: `feed-forward, network, completes, block, blocks, stacked, because, design, only, standard`
- Narration: A feed-forward network completes each block, and blocks are stacked. Because the design uses only standard Transformer components arranged this way, many earlier geometric networks fall out as special cases of the framework.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_feed_forward_network_completes_block" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords feed-forward, network, completes, block, blocks, stacked in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_authors_evaluate_geomformer_across_b`

- Preferred role: `method`
- Cue keywords: `authors, evaluate, geomformer, across, broad, suite, tasks, together, stress, both`
- Narration: The authors evaluate GeoMFormer across a broad suite of tasks that together stress both invariant and equivariant abilities.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_authors_evaluate_geomformer_across_b" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, evaluate, geomformer, across, broad, suite in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_open_catalyst_2020_dataset_spanning`

- Preferred role: `method`
- Cue keywords: `open, catalyst, 2020, dataset, spanning, over, four, hundred, sixty, thousand`
- Narration: On the Open Catalyst 2020 dataset, spanning over four hundred sixty thousand adsorbate-catalyst complexes, they test both the Initial Structure to Relaxed Energy task, which is invariant, and the Initial Structure to Relaxed Structure task, which is equivariant.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_open_catalyst_2020_dataset_spanning" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords open, catalyst, 2020, dataset, spanning, over in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_large_quantum_chemistry_datasets_pcq`

- Preferred role: `method`
- Cue keywords: `large, quantum, chemistry, datasets, pcqm4mv2, molecule3d, millions, molecules, they, predict`
- Narration: On the large quantum chemistry datasets PCQM4Mv2 and Molecule3D, with millions of molecules, they predict the HOMO-LUMO energy gap.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_large_quantum_chemistry_datasets_pcq" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords large, quantum, chemistry, datasets, pcqm4mv2, molecule3d in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_they_further_synthetic_five_particle`

- Preferred role: `figure`
- Cue keywords: `they, further, synthetic, five-particle, n-body, simulation, test, equivariant, position, prediction`
- Narration: They further use a synthetic five-particle N-body simulation to test equivariant position prediction, and the MD17 dataset for force-field modeling in the ablation studies. This breadth lets a single architecture be judged on both scalar and vector prediction.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s06_c4_they_further_synthetic_five_particle" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, further, synthetic, five-particle, n-body, simulation in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_geomformer_delivers_strong_results_e`

- Preferred role: `method`
- Cue keywords: `geomformer, delivers, strong, results, everywhere, tested, open, catalyst, energy, prediction`
- Narration: GeoMFormer delivers strong results everywhere it is tested. On the Open Catalyst energy prediction task it outperforms prior invariant models, and on the structure prediction task it excels at equivariant modeling.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_geomformer_delivers_strong_results_e" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords geomformer, delivers, strong, results, everywhere, tested in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_pcqm4mv2_benchmark_reaches_lowest_er`

- Preferred role: `result`
- Cue keywords: `pcqm4mv2, benchmark, reaches, lowest, error, among, models, quadratic, complexity, six`
- Narration: On the PCQM4Mv2 benchmark it reaches the lowest error among models with quadratic complexity, a six point seven percent relative reduction over the previous best, while staying efficient enough to scale to large systems.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_pcqm4mv2_benchmark_reaches_lowest_er" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pcqm4mv2, benchmark, reaches, lowest, error, among in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_molecule3d_improves_error_sixteen_po`

- Preferred role: `method`
- Cue keywords: `molecule3d, improves, error, sixteen, point, three, percent, random, split, eleven`
- Narration: On Molecule3D it improves error by sixteen point three percent on the random split and eleven point six percent on the scaffold split. And on the N-body simulation it cuts mean squared error by a striking thirty-three point eight percent.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_molecule3d_improves_error_sixteen_po" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords molecule3d, improves, error, sixteen, point, three in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_single_architecture_built_standard_t`

- Preferred role: `method`
- Cue keywords: `single, architecture, built, standard, transformer, parts, achieves, state-of-the-art, performance, both`
- Narration: A single architecture, built from standard Transformer parts, achieves state-of-the-art performance on both invariant and equivariant tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_single_architecture_built_standard_t" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords single, architecture, built, standard, transformer, parts in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_understand_where_gains_come_authors`

- Preferred role: `method`
- Cue keywords: `understand, where, gains, come, authors, ablate, building, block, most, telling`
- Narration: To understand where the gains come from, the authors ablate each building block. The most telling finding concerns the cross-attention modules that bridge the invariant and equivariant streams. Removing them hurts sharply.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_understand_where_gains_come_authors" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords understand, where, gains, come, authors, ablate in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_md17_energy_prediction_task_adding`

- Preferred role: `method`
- Cue keywords: `md17, energy, prediction, task, adding, invariant, cross-attention, gives, eighteen, point`
- Narration: On the MD17 energy prediction task, adding the invariant cross-attention gives an eighteen point seven percent relative improvement, the equivariant cross-attention gives nine point eight percent, and using both together gives twenty point eight percent.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_md17_energy_prediction_task_adding" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords md17, energy, prediction, task, adding, invariant in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_harder_md17_force_prediction_task`

- Preferred role: `method`
- Cue keywords: `harder, md17, force, prediction, task, effect, even, larger, sixty, point`
- Narration: On the harder MD17 force prediction task the effect is even larger, with a sixty point eight percent relative improvement when both cross-attention modules are used.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_harder_md17_force_prediction_task" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords harder, md17, force, prediction, task, effect in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_n_body_simulation_combined_improveme`

- Preferred role: `method`
- Cue keywords: `n-body, simulation, combined, improvement, seventeen, point, five, percent, self-attention, feed-forward`
- Narration: On the N-body simulation the combined improvement is seventeen point five percent. The self-attention, feed-forward, and layer-normalization modules also each contribute, but the cross-attention bridge is clearly the heart of the design.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_n_body_simulation_combined_improveme" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords n-body, simulation, combined, improvement, seventeen, point in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact_pcqm4mv2`

- Preferred role: `result`
- Cue keywords: `few, numbers, capture, impact, pcqm4mv2, geomformer, reaches, validation, error, zero`
- Narration: A few numbers capture the impact. On PCQM4Mv2, GeoMFormer reaches a validation error of zero point zero seven three four, the best of any quadratic-complexity model, a six point seven percent relative reduction.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact_pcqm4mv2" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact, pcqm4mv2, geomformer in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_n_body_simulation_achieves_mean_squa`

- Preferred role: `result`
- Cue keywords: `n-body, simulation, achieves, mean, squared, error, zero, point, zero, zero`
- Narration: On the N-body simulation it achieves a mean squared error of zero point zero zero four seven, a thirty-three point eight percent reduction over the previous best.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_n_body_simulation_achieves_mean_squa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords n-body, simulation, achieves, mean, squared, error in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_molecule3d_records_errors_zero_point`

- Preferred role: `result`
- Cue keywords: `molecule3d, records, errors, zero, point, zero, two, five, two, random`
- Narration: On Molecule3D it records errors of zero point zero two five two on the random split and zero point one zero four five on the scaffold split, improvements of sixteen point three and eleven point six percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_molecule3d_records_errors_zero_point" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords molecule3d, records, errors, zero, point, zero in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_ablations_adding_cross_attention_yie`

- Preferred role: `method`
- Cue keywords: `ablations, adding, cross-attention, yields, sixty, point, eight, percent, relative, improvement`
- Narration: And in the ablations, adding cross-attention yields up to a sixty point eight percent relative improvement on force prediction, underscoring how central that bridge is.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_ablations_adding_cross_attention_yie" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, adding, cross-attention, yields, sixty, point in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_message_work_you_not`

- Preferred role: `method`
- Cue keywords: `lasting, message, work, you, not, need, bespoke, heuristic, modules, molecules`
- Narration: The lasting message of this work is that you do not need bespoke, heuristic modules to model molecules under physical constraints.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_lasting_message_work_you_not" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, work, you, not, need in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_running_two_standard_transformer_str`

- Preferred role: `method`
- Cue keywords: `running, two, standard, transformer, streams, parallel, one, invariant, one, equivariant`
- Narration: By running two standard Transformer streams in parallel, one for invariant and one for equivariant features, and connecting them with simple cross-attention, GeoMFormer learns both kinds of representation at once and outperforms specialized architectures on a wide range of tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_running_two_standard_transformer_str" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords running, two, standard, transformer, streams, parallel in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_because_many_earlier_models_special`

- Preferred role: `guidance`
- Cue keywords: `because, many, earlier, models, special, cases, framework, geomformer, offers, clean`
- Narration: Because many earlier models are special cases of this framework, GeoMFormer offers a clean, general, and scalable design principle for geometric molecular representation learning.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s10_c3_because_many_earlier_models_special" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, many, earlier, models, special, cases in title/desc so the matcher can verify semantic overlap.
