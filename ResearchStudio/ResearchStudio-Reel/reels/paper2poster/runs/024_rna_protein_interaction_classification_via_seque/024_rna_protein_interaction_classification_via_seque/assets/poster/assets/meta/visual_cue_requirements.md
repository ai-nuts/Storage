# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_rna_protein_interactions_drive_gene`

- Preferred role: `content`
- Cue keywords: `rna-protein, interactions, drive, gene, regulation, yet, measuring, them, lab, slow`
- Narration: RNA-protein interactions drive gene regulation, yet measuring them in the lab is slow and costly, and existing predictors lean on small, protein-specific datasets.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_rna_protein_interactions_drive_gene" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rna-protein, interactions, drive, gene, regulation, yet in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_work_introduces_rnainteract_large_cu`

- Preferred role: `method`
- Cue keywords: `work, introduces, rnainteract, large, curated, dataset, non-coding, rna-protein, interactions, rpiembeddor`
- Narration: This work introduces RNAInterAct, a large curated dataset of non-coding RNA-protein interactions, and RPIembeddor, a transformer model that classifies whether any RNA and protein interact using only their sequences.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_work_introduces_rnainteract_large_cu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, introduces, rnainteract, large, curated, dataset in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_feeding_embeddings_two_foundation_mo`

- Preferred role: `method`
- Cue keywords: `feeding, embeddings, two, foundation, models, rna-fm, rna, esm-2, proteins, attention-based`
- Narration: By feeding embeddings from two foundation models, RNA-FM for RNA and ESM-2 for proteins, into an attention-based network, RPIembeddor outperforms prior state-of-the-art methods and generalizes to unseen RNA families and data distributions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_feeding_embeddings_two_foundation_mo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords feeding, embeddings, two, foundation, models, rna-fm in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_non_coding_rnas_regulate_cell_largel`

- Preferred role: `content`
- Cue keywords: `non-coding, rnas, regulate, cell, largely, through, their, interactions, proteins, but`
- Narration: Non-coding RNAs regulate the cell largely through their interactions with proteins, but mapping these interactions experimentally is slow and costly.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_non_coding_rnas_regulate_cell_largel" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords non-coding, rnas, regulate, cell, largely, through in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_most_computational_predictors_sidest`

- Preferred role: `method`
- Cue keywords: `most, computational, predictors, sidestep, general, problem, one, per, protein, which`
- Narration: Most computational predictors sidestep the general problem by training one model per protein, which requires a large interaction dataset for that specific protein.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_most_computational_predictors_sidest" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords most, computational, predictors, sidestep, general, problem in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_such_datasets_exist_only_few`

- Preferred role: `content`
- Cue keywords: `such, datasets, exist, only, few, hundred, roughly, two, thousand, human`
- Narration: Such datasets exist for only a few hundred of the roughly two thousand human RNA-binding proteins.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_such_datasets_exist_only_few" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords such, datasets, exist, only, few, hundred in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_what_missing_method_decides_any`

- Preferred role: `method`
- Cue keywords: `what, missing, method, decides, any, given, rna, protein, pair, whether`
- Narration: What is missing is a method that decides, for any given RNA and protein pair, whether they interact using nothing but their sequences.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_what_missing_method_decides_any" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, missing, method, decides, any, given in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_recent_progress_shows_two_useful`

- Preferred role: `content`
- Cue keywords: `recent, progress, shows, two, useful, ideas`
- Narration: Recent progress shows two useful ideas.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_recent_progress_shows_two_useful" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords recent, progress, shows, two, useful, ideas in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_first_learning_across_many_tasks`

- Preferred role: `title`
- Cue keywords: `first, learning, across, many, tasks, rather, one, protein, time, help`
- Narration: First, learning across many tasks, rather than one protein at a time, can help when labeled data is scarce.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s03_c2_first_learning_across_many_tasks" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, learning, across, many, tasks, rather in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_second_foundation_models_trained_hug`

- Preferred role: `method`
- Cue keywords: `second, foundation, models, trained, huge, unlabeled, biological, corpora, capture, structural`
- Narration: Second, foundation models trained on huge unlabeled biological corpora capture structural and functional signal that raw sequences do not expose directly.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_second_foundation_models_trained_hug" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, foundation, models, trained, huge, unlabeled in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_combining_these_ideas_single_could`

- Preferred role: `guidance`
- Cue keywords: `combining, these, ideas, single, could, learn, general, rules, rna-protein, binding`
- Narration: Combining these ideas, a single model could learn general rules of RNA-protein binding and apply them to interaction types it has never seen, which is exactly what a broad, sequence-only predictor needs.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s03_c4_combining_these_ideas_single_could" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords combining, these, ideas, single, could, learn in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_work_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `work, makes, three, contributions`
- Narration: The work makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_work_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_builds_rnainteract_extensive_dataset`

- Preferred role: `content`
- Cue keywords: `builds, rnainteract, extensive, dataset, non-coding, rna-protein, interactions, derived, rnainter, database`
- Narration: It builds RNAInterAct, an extensive dataset of non-coding RNA-protein interactions derived from the RNAInter database and enriched with carefully generated negatives.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_builds_rnainteract_extensive_dataset" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords builds, rnainteract, extensive, dataset, non-coding, rna-protein in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_introduces_rpiembeddor_transformer_c`

- Preferred role: `method`
- Cue keywords: `introduces, rpiembeddor, transformer, classifies, interactions, sequence, embeddings, beats, existing, tools`
- Narration: It introduces RPIembeddor, a transformer that classifies interactions from sequence embeddings and beats existing tools while generalizing to new data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_introduces_rpiembeddor_transformer_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, rpiembeddor, transformer, classifies, interactions, sequence in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_through_ablation_study_shows_two`

- Preferred role: `content`
- Cue keywords: `through, ablation, study, shows, two, foundation-model, embeddings, not, optional, add-ons`
- Narration: And through an ablation study it shows that the two foundation-model embeddings are not optional add-ons but the core of the model's ability to classify correctly.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_through_ablation_study_shows_two" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords through, ablation, study, shows, two, foundation-model in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_rpiembeddor_turns_sequences_knowledg`

- Preferred role: `method`
- Cue keywords: `rpiembeddor, turns, sequences, knowledge, leaning, two, pre-trained, foundation, models`
- Narration: RPIembeddor turns sequences into knowledge by leaning on two pre-trained foundation models.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_rpiembeddor_turns_sequences_knowledg" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rpiembeddor, turns, sequences, knowledge, leaning, two in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_rna_sequences_embedded_rna_fm_traine`

- Preferred role: `method`
- Cue keywords: `rna, sequences, embedded, rna-fm, trained, twenty-three, million, non-coding, rnas, protein`
- Narration: RNA sequences are embedded with RNA-FM, trained on twenty-three million non-coding RNAs, and protein sequences with ESM-2, which predicts folding without multiple sequence alignments. Both produce embeddings of size N by six hundred forty.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_rna_sequences_embedded_rna_fm_traine" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rna, sequences, embedded, rna-fm, trained, twenty-three in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_two_parallel_feed_forward_layers_nor`

- Preferred role: `method`
- Cue keywords: `two, parallel, feed-forward, layers, normalize, their, sizes, encoder, layers, process`
- Narration: Two parallel feed-forward layers normalize their sizes, and encoder layers process the RNA and protein embeddings symmetrically so attention can focus on the parts of each sequence most relevant to interaction.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_two_parallel_feed_forward_layers_nor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, parallel, feed-forward, layers, normalize, their in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_latent_representations_concatenated`

- Preferred role: `content`
- Cue keywords: `latent, representations, concatenated, passed, through, further, feed-forward, layers, ending, linear`
- Narration: The latent representations are concatenated and passed through further feed-forward layers, ending in a linear layer with a sigmoid that outputs the probability of interaction. The whole model has just one-point-four million parameters.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_latent_representations_concatenated" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords latent, representations, concatenated, passed, through, further in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_dataset_backbone_study_starting_rnai`

- Preferred role: `content`
- Cue keywords: `dataset, backbone, study, starting, rnainter, over, forty-seven, million, rna, interactions`
- Narration: The dataset is the backbone of the study. Starting from RNAInter, with over forty-seven million RNA interactions, the authors recover sequences by cross-referencing NCBI, UniProt and Ensembl, and assign RNA families from Rfam and protein clans from Pfam.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_dataset_backbone_study_starting_rnai" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dataset, backbone, study, starting, rnainter, over in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_those_annotations_let_them_generate`

- Preferred role: `result`
- Cue keywords: `those, annotations, let, them, generate, negatives, biologically, meaningful, rather, random`
- Narration: Those annotations let them generate negatives that are biologically meaningful rather than random.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_those_annotations_let_them_generate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords those, annotations, let, them, generate, negatives in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_final_rnainteract_set_holds_about`

- Preferred role: `method`
- Cue keywords: `final, rnainteract, set, holds, about, one, hundred, twenty-two, thousand, interactions`
- Narration: The final RNAInterAct set holds about one hundred twenty-two thousand interactions at a one-to-two positive-to-negative ratio. Crucially, it is split by RNA family, so no family appears in both training and testing.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_final_rnainteract_set_holds_about" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords final, rnainteract, set, holds, about, one in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_homology_aware_split_plus_evaluation`

- Preferred role: `result`
- Cue keywords: `homology-aware, split, plus, evaluation, external, rpi2825, dataset, tests, true, generalization`
- Narration: This homology-aware split, plus evaluation on the external RPI2825 dataset, tests true generalization instead of memorization.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_homology_aware_split_plus_evaluation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords homology-aware, split, plus, evaluation, external, rpi2825 in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_hardest_test_tsfam_where_rna`

- Preferred role: `method`
- Cue keywords: `hardest, test, tsfam, where, rna, family, overlaps, rpiembeddor, reaches, 1`
- Narration: On the hardest test, TSfam, where no RNA family overlaps with training, RPIembeddor reaches an F1 score of about zero-point-five-nine and an accuracy of about zero-point-six-seven.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_hardest_test_tsfam_where_rna" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords hardest, test, tsfam, where, rna, family in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_its_roc_area_under_curve`

- Preferred role: `figure`
- Cue keywords: `its, roc, area, under, curve, zero-point-seven-zero, while, competing, tools, xrpi`
- Narration: Its ROC area under the curve is zero-point-seven-zero, while the competing tools XRPI and IPMiner sit at zero-point-four-eight and zero-point-five-zero, essentially chance.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s07_c2_its_roc_area_under_curve" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, roc, area, under, curve, zero-point-seven-zero in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_concrete_terms_rpiembeddor_correctly`

- Preferred role: `content`
- Cue keywords: `concrete, terms, rpiembeddor, correctly, labels, nearly, three, thousand, positive, interactions`
- Narration: In concrete terms, RPIembeddor correctly labels nearly three thousand of the positive interactions and over five thousand of the negatives, whereas XRPI simply predicts almost everything as interacting.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_concrete_terms_rpiembeddor_correctly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords concrete, terms, rpiembeddor, correctly, labels, nearly in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_clearly_learns_real_signal_generaliz`

- Preferred role: `content`
- Cue keywords: `clearly, learns, real, signal, generalizes, unseen, rna, families`
- Narration: The model clearly learns real signal that generalizes to unseen RNA families.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_clearly_learns_real_signal_generaliz" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords clearly, learns, real, signal, generalizes, unseen in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_test_whether_two_embeddings_really`

- Preferred role: `result`
- Cue keywords: `test, whether, two, embeddings, really, matter, authors, retrain, after, swapping`
- Narration: To test whether the two embeddings really matter, the authors retrain the model after swapping out the RNA embedding, the protein embedding, or both, for random vectors or one-hot encodings.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c1_test_whether_two_embeddings_really" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords test, whether, two, embeddings, really, matter in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_every_one_these_variants_stops`

- Preferred role: `method`
- Cue keywords: `every, one, these, variants, stops, working, predicting, only, negative, class`
- Narration: In every one of these variants the model stops working, predicting only the negative class, so its F1 score falls to zero and its accuracy merely reflects the fraction of negatives in the data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_every_one_these_variants_stops" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords every, one, these, variants, stops, working in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_only_when_both_rna_fm_esm_2`

- Preferred role: `content`
- Cue keywords: `only, when, both, rna-fm, esm-2, embeddings, present, does, classify, correctly`
- Narration: Only when both the RNA-FM and ESM-2 embeddings are present does the model classify correctly.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_only_when_both_rna_fm_esm_2" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords only, when, both, rna-fm, esm-2, embeddings in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_confirms_foundation_model_embeddings`

- Preferred role: `method`
- Cue keywords: `confirms, foundation-model, embeddings, carry, structural, functional, information, task, depends`
- Narration: This confirms that the foundation-model embeddings carry the structural and functional information the task depends on.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_confirms_foundation_model_embeddings" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords confirms, foundation-model, embeddings, carry, structural, functional in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact_rpiembedd`

- Preferred role: `method`
- Cue keywords: `few, numbers, capture, impact, rpiembeddor, scores, roc, area, under, curve`
- Narration: A few numbers capture the impact. RPIembeddor scores a ROC area under the curve of zero-point-seven-zero on the homology-separated test set, where the best competitor manages only zero-point-five-zero.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact_rpiembedd" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact, rpiembeddor, scores in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_its_1_zero_point_five_nine_accuracy`

- Preferred role: `method`
- Cue keywords: `its, 1, zero-point-five-nine, accuracy, zero-point-six-seven, lead, all, methods`
- Narration: Its F1 of zero-point-five-nine and accuracy of zero-point-six-seven lead all methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_its_1_zero_point_five_nine_accuracy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, 1, zero-point-five-nine, accuracy, zero-point-six-seven, lead in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_rnainteract_dataset_contributes_over`

- Preferred role: `content`
- Cue keywords: `rnainteract, dataset, contributes, over, one, hundred, twenty-two, thousand, interactions, spanning`
- Narration: The RNAInterAct dataset contributes over one hundred twenty-two thousand interactions spanning nine hundred seventy-six RNA families.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_rnainteract_dataset_contributes_over" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rnainteract, dataset, contributes, over, one, hundred in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_all_runs_compact_one_point_four_mill`

- Preferred role: `content`
- Cue keywords: `all, runs, compact, one-point-four-million-parameter, powered, rna-fm, esm-2, foundation, models`
- Narration: And all of this runs in a compact one-point-four-million-parameter model powered by the RNA-FM and ESM-2 foundation models.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_all_runs_compact_one_point_four_mill" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords all, runs, compact, one-point-four-million-parameter, powered, rna-fm in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_message_general_rna_protein`

- Preferred role: `content`
- Cue keywords: `lasting, message, general, rna-protein, interaction, prediction, sequence, alone, achievable, when`
- Narration: The lasting message is that general RNA-protein interaction prediction from sequence alone is achievable when you stand on the shoulders of foundation models.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c1_lasting_message_general_rna_protein" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, general, rna-protein, interaction, prediction in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_compact_attention_network_fed_rna_fm`

- Preferred role: `method`
- Cue keywords: `compact, attention, network, fed, rna-fm, esm-2, embeddings, outperforms, specialized, tools`
- Narration: A compact attention network fed with RNA-FM and ESM-2 embeddings outperforms specialized tools and, unlike them, generalizes to RNA families it has never seen.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_compact_attention_network_fed_rna_fm" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords compact, attention, network, fed, rna-fm, esm-2 in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_companion_rnainteract_dataset_split`

- Preferred role: `result`
- Cue keywords: `companion, rnainteract, dataset, split, remove, homology, bias, gives, community, fair`
- Narration: The companion RNAInterAct dataset, split to remove homology bias, gives the community a fair benchmark.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c3_companion_rnainteract_dataset_split" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords companion, rnainteract, dataset, split, remove, homology in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_both_embeddings_essential_authors_po`

- Preferred role: `method`
- Cue keywords: `both, embeddings, essential, authors, point, toward, adding, rna-structure, models, longer`
- Narration: Both embeddings are essential, and the authors point toward adding RNA-structure models and longer sequences next.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c4_both_embeddings_essential_authors_po" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords both, embeddings, essential, authors, point, toward in title/desc so the matcher can verify semantic overlap.
