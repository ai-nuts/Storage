# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_view_somewhere_published_iclr_2023`

- Preferred role: `content`
- Cue keywords: `view, somewhere, published, iclr, 2023, researchers, sony, university, tokyo, rethinks`
- Narration: This paper, A View From Somewhere, published at ICLR 2023 by researchers at Sony AI and the University of Tokyo, rethinks how we represent human faces in datasets.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_view_somewhere_published_iclr_2023" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords view, somewhere, published, iclr, 2023, researchers in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_instead_relying_problematic_demograp`

- Preferred role: `content`
- Cue keywords: `instead, relying, problematic, demographic, labels, like, race, gender, authors, collect`
- Narration: Instead of relying on problematic demographic labels like race or gender, the authors collect over six hundred thousand human judgments of face similarity and learn a continuous embedding space aligned with human perception.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_instead_relying_problematic_demograp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, relying, problematic, demographic, labels, like in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_result_face_representation_interpret`

- Preferred role: `result`
- Cue keywords: `result, face, representation, interpretable, avoids, invasive, categorical, labels, captures, smooth`
- Narration: The result is a face representation that is interpretable, that avoids invasive categorical labels, and that captures the smooth, continuous nature of human phenotypic diversity, opening a new path for measuring dataset diversity more responsibly.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c3_result_face_representation_interpret" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, face, representation, interpretable, avoids, invasive in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_evaluating_diversity_face_datasets_a`

- Preferred role: `guidance`
- Cue keywords: `evaluating, diversity, face, datasets, almost, always, relies, categorical, demographic, labels`
- Narration: Evaluating the diversity of face datasets almost always relies on categorical demographic labels such as race, gender, or age.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s02_c1_evaluating_diversity_face_datasets_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluating, diversity, face, datasets, almost, always in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_these_labels_frequently_unavaila`

- Preferred role: `method`
- Cue keywords: `but, these, labels, frequently, unavailable, legally, restricted, collect, prone, bias`
- Narration: But these labels are frequently unavailable, legally restricted to collect, and prone to bias when they are inferred by annotators rather than self-reported.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_but_these_labels_frequently_unavaila" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, these, labels, frequently, unavailable, legally in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_worse_categorical_labels_flatten_con`

- Preferred role: `method`
- Cue keywords: `worse, categorical, labels, flatten, continuous, nature, human, appearance, skin, tone`
- Narration: Worse, categorical labels flatten the continuous nature of human appearance: skin tone becomes simply light or dark, and two faces sharing the same label can still look strikingly different.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_worse_categorical_labels_flatten_con" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords worse, categorical, labels, flatten, continuous, nature in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_rigid_taxonomies_also_erase_multi_et`

- Preferred role: `content`
- Cue keywords: `rigid, taxonomies, also, erase, multi-ethnic, people, shift, meaning, across, cultures`
- Narration: Rigid taxonomies also erase multi-ethnic people, shift meaning across cultures, and can cause real psychological harm when someone is mislabeled.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_rigid_taxonomies_also_erase_multi_et" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rigid, taxonomies, also, erase, multi-ethnic, people in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_authors_argue_face_similarity_fundam`

- Preferred role: `content`
- Cue keywords: `authors, argue, face, similarity, fundamentally, continuous, depends, who, doing, judging`
- Narration: The authors argue that face similarity is fundamentally continuous and depends on who is doing the judging.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_authors_argue_face_similarity_fundam" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, argue, face, similarity, fundamentally, continuous in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_could_learn_representation_directly`

- Preferred role: `guidance`
- Cue keywords: `could, learn, representation, directly, aligned, human, perception, could, sidestep, problematic`
- Narration: If we could learn a representation directly aligned with human perception, we could sidestep problematic semantic labels entirely while still measuring diversity.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s03_c2_could_learn_representation_directly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords could, learn, representation, directly, aligned, human in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_existing_psychological_embedding_met`

- Preferred role: `method`
- Cue keywords: `existing, psychological-embedding, methods, fall, short, they, either, cannot, embed, new`
- Narration: Existing psychological-embedding methods fall short: they either cannot embed new faces beyond the fixed training set, or they pool every judgment together, throwing away the meaningful differences within and between individual annotators.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_existing_psychological_embedding_met" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords existing, psychological-embedding, methods, fall, short, they in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_their_answer_view_somewhere_avfs`

- Preferred role: `title`
- Cue keywords: `their, answer, view, somewhere, avfs`
- Narration: Their answer is A View From Somewhere, or AVFS.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s04_c1_their_answer_view_somewhere_avfs" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords their, answer, view, somewhere, avfs in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_they_collect_dataset_six_hundred`

- Preferred role: `method`
- Cue keywords: `they, collect, dataset, six, hundred, thirty-eight, thousand, triplet, similarity, judgments`
- Narration: They collect a dataset of six hundred thirty-eight thousand triplet similarity judgments over nearly five thousand faces, and crucially, each judgment records the identity and self-reported demographics of the annotator who made it.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_they_collect_dataset_six_hundred" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, collect, dataset, six, hundred, thirty-eight in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_top_they_build_conditional_learning`

- Preferred role: `title`
- Cue keywords: `top, they, build, conditional, learning, framework, produces, continuous, low-dimensional, human-interpretable`
- Narration: On top of this data they build a conditional learning framework that produces a continuous, low-dimensional, and human-interpretable embedding space, along with per-annotator masks that reveal how different people weigh different visual dimensions.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s04_c3_top_they_build_conditional_learning" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords top, they, build, conditional, learning, framework in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_core_conditional_convolutional_netwo`

- Preferred role: `method`
- Cue keywords: `core, conditional, convolutional, network, resnet, eighteen, maps, face, one-hundred-twenty-eight-dimensional, embedding`
- Narration: At the core is a conditional convolutional network, a ResNet eighteen, that maps each face to a one-hundred-twenty-eight-dimensional embedding. Training uses odd-one-out judgments: given a triplet of faces, an annotator picks the least similar one.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_core_conditional_convolutional_netwo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, conditional, convolutional, network, resnet, eighteen in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_annotator_assigned_learnable_gating`

- Preferred role: `content`
- Cue keywords: `annotator, assigned, learnable, gating, mask, passed, through, sigmoid, scales, importance`
- Narration: Each annotator is assigned a learnable gating mask, passed through a sigmoid, that scales the importance of every embedding dimension for that person.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_annotator_assigned_learnable_gating" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords annotator, assigned, learnable, gating, mask, passed in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_similarity_between_two_faces_dot`

- Preferred role: `content`
- Cue keywords: `similarity, between, two, faces, dot, product, their, masked, rectified, embeddings`
- Narration: Similarity between two faces is the dot product of their masked, rectified embeddings, and the model predicts the odd-one-out probability directly from these three pairwise similarities.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_similarity_between_two_faces_dot" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords similarity, between, two, faces, dot, product in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_sparsity_non_negativity_penalty_keep`

- Preferred role: `content`
- Cue keywords: `sparsity, non-negativity, penalty, keeps, dimensions, few, interpretable, leaving, only, about`
- Narration: A sparsity and non-negativity penalty keeps the dimensions few and interpretable, leaving only about twenty-two active dimensions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_sparsity_non_negativity_penalty_keep" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sparsity, non-negativity, penalty, keeps, dimensions, few in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_avfs_dataset_comprises_six_hundred`

- Preferred role: `content`
- Cue keywords: `avfs, dataset, comprises, six, hundred, thirty-eight, thousand, quality-controlled, triplet, judgments`
- Narration: The AVFS dataset comprises six hundred thirty-eight thousand quality-controlled triplet judgments over four thousand nine hundred twenty-one near-frontal face images.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_avfs_dataset_comprises_six_hundred" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords avfs, dataset, comprises, six, hundred, thirty-eight in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_every_single_judgment_carries_annota`

- Preferred role: `content`
- Cue keywords: `every, single, judgment, carries, annotator, identifier, self-identified, demographic, attributes`
- Narration: Every single judgment carries the annotator's identifier and self-identified demographic attributes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_every_single_judgment_carries_annota" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords every, single, judgment, carries, annotator, identifier in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_authors_evaluate_held_out_judgments`

- Preferred role: `method`
- Cue keywords: `authors, evaluate, held-out, judgments, over, same, stimuli, eighty, thousand, judgments`
- Narration: The authors evaluate on held-out judgments over the same stimuli, on eighty thousand judgments over entirely novel faces, and against attribute-recognition baselines trained on CelebA and FairFace semantic labels.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_authors_evaluate_held_out_judgments" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, evaluate, held-out, judgments, over, same in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_across_both_same_stimuli_novel_stimu`

- Preferred role: `method`
- Cue keywords: `across, both, same-stimuli, novel-stimuli, evaluations, avfs, models, predict, human, similarity`
- Narration: Across both the same-stimuli and the novel-stimuli evaluations, the AVFS models predict human similarity judgments more accurately than baselines trained on semantic labels, and they better capture the uncertainty in human judgments as measured by Spearman correlation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_across_both_same_stimuli_novel_stimu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, both, same-stimuli, novel-stimuli, evaluations, avfs in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_importantly_annotator_specific_masks`

- Preferred role: `title`
- Cue keywords: `importantly, annotator-specific, masks, generalize, even, triplets, made, entirely, novel, previously`
- Narration: Importantly, the annotator-specific masks generalize even to triplets made entirely of novel, previously unseen faces, which shows the embedding space is far more closely aligned with the human mental representation of faces than spaces learned from rigid categorical labels.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s07_c2_importantly_annotator_specific_masks" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords importantly, annotator-specific, masks, generalize, even, triplets in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_test_whether_annotators_really_matte`

- Preferred role: `result`
- Cue keywords: `test, whether, annotators, really, matter, authors, randomly, shuffle, which, annotator`
- Narration: To test whether annotators really matter, the authors randomly shuffle which annotator mask is attached to each of the eighty thousand judgments and recompute accuracy a hundred times over.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c1_test_whether_annotators_really_matte" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords test, whether, annotators, really, matter, authors in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_accuracy_drops_about_sixty_two_perce`

- Preferred role: `result`
- Cue keywords: `accuracy, drops, about, sixty-two, percent, down, roughly, fifty-three, percent, proving`
- Narration: Accuracy drops from about sixty-two percent down to roughly fifty-three percent, proving that annotators are genuinely not interchangeable.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_accuracy_drops_about_sixty_two_perce" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords accuracy, drops, about, sixty-two, percent, down in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_dimension_elimination_analysis_furth`

- Preferred role: `method`
- Cue keywords: `dimension-elimination, analysis, further, shows, only, six, thirteen, dimensions, needed, recover`
- Narration: A dimension-elimination analysis further shows that only six to thirteen dimensions are needed to recover most of the predictive accuracy, while fifteen to twenty-two dimensions are required to explain the full similarity structure, clear evidence that similarity is context-dependent.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_dimension_elimination_analysis_furth" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dimension-elimination, analysis, further, shows, only, six in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_headline_numbers_tell_whole_story`

- Preferred role: `content`
- Cue keywords: `headline, numbers, tell, whole, story`
- Narration: The headline numbers tell the whole story.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_headline_numbers_tell_whole_story" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, numbers, tell, whole, story in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_six_hundred_thirty_eight_thousand_hu`

- Preferred role: `content`
- Cue keywords: `six, hundred, thirty-eight, thousand, human, judgments, gathered, over, four, thousand`
- Narration: Six hundred thirty-eight thousand human judgments gathered over four thousand nine hundred twenty-one distinct faces.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_six_hundred_thirty_eight_thousand_hu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords six, hundred, thirty-eight, thousand, human, judgments in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_twenty_two_interpretable_embedding_d`

- Preferred role: `result`
- Cue keywords: `twenty-two, interpretable, embedding, dimensions, retained, nearly, sixty-two, percent, validation, accuracy`
- Narration: Twenty-two interpretable embedding dimensions retained at nearly sixty-two percent validation accuracy.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_twenty_two_interpretable_embedding_d" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords twenty-two, interpretable, embedding, dimensions, retained, nearly in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_when_annotator_identities_scrambled`

- Preferred role: `method`
- Cue keywords: `when, annotator, identities, scrambled, accuracy, falls, sixty-one, point, seven, down`
- Narration: And when annotator identities are scrambled, accuracy falls from sixty-one point seven down to fifty-two point eight percent, all achieved without ever training on a single semantic label.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_when_annotator_identities_scrambled" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, annotator, identities, scrambled, accuracy, falls in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_key_takeaway_learning_face_represent`

- Preferred role: `figure`
- Cue keywords: `key, takeaway, learning, face, representations, human, similarity, judgments, instead, demographic`
- Narration: The key takeaway is that learning face representations from human similarity judgments, instead of demographic labels, produces a continuous, interpretable, and perception-aligned embedding space that supports diversity analysis without invasive categorical labeling.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s10_c1_key_takeaway_learning_face_represent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, takeaway, learning, face, representations, human in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_because_framework_only_requires_keep`

- Preferred role: `guidance`
- Cue keywords: `because, framework, only, requires, keeping, track, which, annotator, made, which`
- Narration: And because the framework only requires keeping track of which annotator made which judgment, the same conditional approach can extend naturally to almost any machine-learning task built on subjective human decisions.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s10_c2_because_framework_only_requires_keep" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, framework, only, requires, keeping, track in title/desc so the matcher can verify semantic overlap.
