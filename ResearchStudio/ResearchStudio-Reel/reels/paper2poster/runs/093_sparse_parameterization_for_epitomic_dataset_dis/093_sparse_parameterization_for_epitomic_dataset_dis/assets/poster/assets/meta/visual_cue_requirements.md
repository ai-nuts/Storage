# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_deep_learning_depends_huge_datasets`

- Preferred role: `result`
- Cue keywords: `deep, learning, depends, huge, datasets, costly, store, preprocess, train, dataset`
- Narration: Deep learning depends on huge datasets that are costly to store, preprocess, and train on. Dataset distillation compresses a dataset into a tiny synthetic one that still trains high-accuracy models. This paper introduces SPEED, Sparse Parameterization for Epitomic dataset Distillation.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c1_deep_learning_depends_huge_datasets" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deep, learning, depends, huge, datasets, costly in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_instead_tuning_matching_objective_li`

- Preferred role: `content`
- Cue keywords: `instead, tuning, matching, objective, like, most, prior, work, speed, rethinks`
- Narration: Instead of tuning the matching objective like most prior work, SPEED rethinks how the synthetic dataset itself is parameterized.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_instead_tuning_matching_objective_li" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, tuning, matching, objective, like, most in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_borrows_ideas_dictionary_learning_sp`

- Preferred role: `content`
- Cue keywords: `borrows, ideas, dictionary, learning, sparse, coding, shared, pool, spatial-agnostic, epitomic`
- Narration: It borrows ideas from dictionary learning and sparse coding: a shared pool of spatial-agnostic epitomic tokens acts as a dictionary, sparse coding matrices pick the significant tokens per image, and a feature-recurrent network reassembles them into high-resolution synthetic images.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_borrows_ideas_dictionary_learning_sp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords borrows, ideas, dictionary, learning, sparse, coding in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_result_state_of_the_art_distillation`

- Preferred role: `result`
- Cue keywords: `result, state-of-the-art, distillation, especially, high-resolution, imagenet, subsets, fraction, storage`
- Narration: The result is state-of-the-art distillation, especially on high-resolution ImageNet subsets, with a fraction of the storage.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c4_result_state_of_the_art_distillation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, state-of-the-art, distillation, especially, high-resolution, imagenet in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_goal_dataset_distillation_shrink_big`

- Preferred role: `content`
- Cue keywords: `goal, dataset, distillation, shrink, big, dataset, small, synthetic, set, still`
- Narration: The goal of dataset distillation is to shrink a big dataset into a small synthetic set that still trains models well.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_goal_dataset_distillation_shrink_big" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords goal, dataset, distillation, shrink, big, dataset in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_most_existing_work_pours_its`

- Preferred role: `figure`
- Cue keywords: `most, existing, work, pours, its, energy, matching, objective, loss, aligns`
- Narration: Most existing work pours its energy into the matching objective, the loss that aligns the synthetic and real datasets. But how the synthetic images are actually parameterized has been an afterthought.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s02_c2_most_existing_work_pours_its" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords most, existing, work, pours, its, energy in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_standard_approach_optimizes_syntheti`

- Preferred role: `method`
- Cue keywords: `standard, approach, optimizes, synthetic, image, independently, naive, scheme, never, exploits`
- Narration: The standard approach optimizes each synthetic image independently, a naive scheme that never exploits the fact that natural images share enormous amounts of visual structure, both within a single image and across different images.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_standard_approach_optimizes_syntheti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords standard, approach, optimizes, synthetic, image, independently in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_spatial_redundancy_silently_wastes_a`

- Preferred role: `content`
- Cue keywords: `spatial, redundancy, silently, wastes, already, tiny, storage, budget, problem, gets`
- Narration: This spatial redundancy silently wastes the already tiny storage budget, and the problem gets worse as image resolution grows.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_spatial_redundancy_silently_wastes_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords spatial, redundancy, silently, wastes, already, tiny in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_key_insight_images_highly_redundant`

- Preferred role: `method`
- Cue keywords: `key, insight, images, highly, redundant, patches, repeat, textures, recur, similar`
- Narration: The key insight is that images are highly redundant. Patches repeat, textures recur, and similar structures appear across many images.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_key_insight_images_highly_redundant" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, insight, images, highly, redundant, patches in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_classical_representation_learning_di`

- Preferred role: `content`
- Cue keywords: `classical, representation, learning, dictionary, learning, sparse, coding, built, exactly, capture`
- Narration: Classical representation learning, dictionary learning and sparse coding, was built exactly to capture this: represent many signals as sparse combinations of a shared dictionary.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_classical_representation_learning_di" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords classical, representation, learning, dictionary, learning, sparse in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_handful_recent_distillation_methods`

- Preferred role: `method`
- Cue keywords: `handful, recent, distillation, methods, started, exploiting, relationships, between, synthetic, images`
- Narration: A handful of recent distillation methods started exploiting relationships between synthetic images, but none tackled redundancy in a spatially-agnostic way, no matter where a feature appears.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_handful_recent_distillation_methods" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords handful, recent, distillation, methods, started, exploiting in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_speed_asks_what_spend_almost`

- Preferred role: `method`
- Cue keywords: `speed, asks, what, spend, almost, none, storage, budget, shared, dictionary`
- Narration: SPEED asks: what if we spend almost none of the storage budget on a shared dictionary and per-image sparse codes, and let a small network reconstruct rich images from them? That reframing is where the gains come from.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_speed_asks_what_spend_almost" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords speed, asks, what, spend, almost, none in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_speed_makes_three_main_contributions`

- Preferred role: `method`
- Cue keywords: `speed, makes, three, main, contributions, first, introduces, spatial-agnostic, epitomic, tokens`
- Narration: SPEED makes three main contributions. First, it introduces spatial-agnostic epitomic tokens, a shared dictionary of tokens reused by every synthetic image patch, together with sparse coding matrices that select only the most significant tokens per image.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_speed_makes_three_main_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords speed, makes, three, main, contributions, first in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_proposes_feature_recurrent_ne`

- Preferred role: `method`
- Cue keywords: `second, proposes, feature-recurrent, network, compact, transformer-style, network, recurrently, assembles, those`
- Narration: Second, it proposes a feature-recurrent network, a compact transformer-style network that recurrently assembles those tokens into hierarchical, high-resolution synthetic images while reusing the same shared tokens and codes.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_second_proposes_feature_recurrent_ne" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, proposes, feature-recurrent, network, compact, transformer-style in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_shows_parameterization_drop_in`

- Preferred role: `method`
- Cue keywords: `third, shows, parameterization, drop-in, module, plugs, gradient, distribution, trajectory, matching`
- Narration: Third, it shows this parameterization is a drop-in module: it plugs into gradient, distribution, and trajectory matching objectives alike and improves all of them.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_third_shows_parameterization_drop_in" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, shows, parameterization, drop-in, module, plugs in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_framework_sets_new_state_of_the_art`

- Preferred role: `method`
- Cue keywords: `framework, sets, new, state-of-the-art, results, especially, strong, high-resolution`
- Narration: The framework sets new state-of-the-art results and is especially strong on high-resolution data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_framework_sets_new_state_of_the_art" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords framework, sets, new, state-of-the-art, results, especially in title/desc so the matcher can verify semantic overlap.

## Slide 05: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s05_c1_speed_tested_broadly_standard_side`

- Preferred role: `result`
- Cue keywords: `speed, tested, broadly, standard, side, cifar-10, cifar-100, thirty-two, thirty-two, resolution`
- Narration: SPEED is tested broadly. On the standard side, it uses CIFAR-10 and CIFAR-100 at thirty-two by thirty-two resolution and TinyImageNet at sixty-four by sixty-four.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c1_speed_tested_broadly_standard_side" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords speed, tested, broadly, standard, side, cifar-10 in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_stress_high_resolution_performance_s`

- Preferred role: `method`
- Cue keywords: `stress, high-resolution, performance, six, imagenet, subsets, one-twenty-eight, one-twenty-eight, ten, classes`
- Narration: To stress high-resolution performance, it uses six ImageNet subsets at one-twenty-eight by one-twenty-eight, each with ten classes: ImageNette, ImageWoof, ImageFruit, ImageMeow, ImageSquawk, and ImageYellow.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_stress_high_resolution_performance_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stress, high-resolution, performance, six, imagenet, subsets in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_robustness_measured_cifar_100_c_four`

- Preferred role: `result`
- Cue keywords: `robustness, measured, cifar-100-c, fourteen, corruption, types, five, severity, levels, everything`
- Narration: Robustness is measured on CIFAR-100-C with fourteen corruption types at five severity levels. Everything is compared under equal storage budgets, counted in parameters per class, at one, ten, and fifty images per class.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c3_robustness_measured_cifar_100_c_four" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords robustness, measured, cifar-100-c, fourteen, corruption, types in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_default_backbone_convnet_default_mat`

- Preferred role: `figure`
- Cue keywords: `default, backbone, convnet, default, matching, objective, trajectory, matching, generalization, checked`
- Narration: The default backbone is a ConvNet, the default matching objective is trajectory matching, and generalization is checked on MLP, ResNet18, and ViT.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c4_default_backbone_convnet_default_mat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords default, backbone, convnet, default, matching, objective in title/desc so the matcher can verify semantic overlap.

## Slide 06: key-result

Heading: Key Result

### Cue 1: `cue_s06_c1_headline_clean_sweep_across_all`

- Preferred role: `result`
- Cue keywords: `headline, clean, sweep, across, all, three, standard, benchmarks, all, six`
- Narration: The headline is a clean sweep. Across all three standard benchmarks and all six high-resolution ImageNet subsets, SPEED sets new state-of-the-art.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_headline_clean_sweep_across_all" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, clean, sweep, across, all, three in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_tightest_one_image_per_class_budget`

- Preferred role: `result`
- Cue keywords: `tightest, one-image-per-class, budget, reaches, forty, percent, cifar-100, six, point, gain`
- Narration: At the tightest one-image-per-class budget, it reaches forty percent on CIFAR-100, a six point gain, and twenty-six point nine percent on TinyImageNet, a ten point nine gain over the previous best.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_tightest_one_image_per_class_budget" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tightest, one-image-per-class, budget, reaches, forty, percent in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_imagenet_subsets_averages_eleven_poi`

- Preferred role: `method`
- Cue keywords: `imagenet, subsets, averages, eleven, point, two, percent, improvement, same, budget`
- Narration: On the ImageNet subsets it averages an eleven point two percent improvement at the same budget. Strikingly, its one-image-per-class results match what prior methods needed ten images per class to achieve, using only about ten percent of their storage.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_imagenet_subsets_averages_eleven_poi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords imagenet, subsets, averages, eleven, point, two in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_also_stays_best_every_step`

- Preferred role: `method`
- Cue keywords: `also, stays, best, every, step, continual, learning, under, corruption, resnet18`
- Narration: It also stays best at every step of continual learning, and under corruption on ResNet18 it nearly doubles the accuracy of prior methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_also_stays_best_every_step" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords also, stays, best, every, step, continual in title/desc so the matcher can verify semantic overlap.

## Slide 07: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s07_c1_ablations_show_sparsification_essent`

- Preferred role: `content`
- Cue keywords: `ablations, show, sparsification, essentially, free`
- Narration: The ablations show sparsification is essentially free.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_ablations_show_sparsification_essent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, show, sparsification, essentially, free in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_pruning_sparse_coding_matrix_just`

- Preferred role: `result`
- Cue keywords: `pruning, sparse, coding, matrix, just, forty-eight, non-zero, elements, about, three`
- Narration: Pruning each sparse coding matrix to just forty-eight non-zero elements, about three hundred thousand parameters, meets the storage budget while keeping ConvNet accuracy at seventy-three point five percent, barely below the seventy-four percent of the full fifteen-million-parameter model.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_pruning_sparse_coding_matrix_just" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pruning, sparse, coding, matrix, just, forty-eight in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_push_too_low_down_twelve`

- Preferred role: `result`
- Cue keywords: `push, too, low, down, twelve, accuracy, collapses, moderate, value, best`
- Narration: Push k too low, down to twelve, and accuracy collapses, so a moderate value is best and even improves cross-architecture generalization. On the network side, two recurrent blocks and three heads work best.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_push_too_low_down_twelve" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords push, too, low, down, twelve, accuracy in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_qualitatively_synthetic_images_befor`

- Preferred role: `content`
- Cue keywords: `qualitatively, synthetic, images, before, after, sparsification, zero, point, three, percent`
- Narration: And qualitatively, synthetic images before and after sparsification to zero point three percent density look almost identical, confirming that the pruned features preserve the global semantics.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_qualitatively_synthetic_images_befor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords qualitatively, synthetic, images, before, after, sparsification in title/desc so the matcher can verify semantic overlap.

## Slide 08: takeaway

Heading: Takeaway

### Cue 1: `cue_s08_c1_lasting_message_speed_parameterizati`

- Preferred role: `method`
- Cue keywords: `lasting, message, speed, parameterization, deserves, much, attention, matching, objective`
- Narration: The lasting message of SPEED is that parameterization deserves as much attention as the matching objective.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_lasting_message_speed_parameterizati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, speed, parameterization, deserves, much in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_treating_synthetic_dataset_shared_di`

- Preferred role: `method`
- Cue keywords: `treating, synthetic, dataset, shared, dictionary, spatial-agnostic, epitomic, tokens, sparse, per-image`
- Narration: By treating a synthetic dataset as a shared dictionary of spatial-agnostic epitomic tokens, sparse per-image coding matrices, and a small recurrent network that reassembles them, SPEED removes the spatial redundancy that naive methods leave on the table.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_treating_synthetic_dataset_shared_di" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords treating, synthetic, dataset, shared, dictionary, spatial-agnostic in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_payoff_state_of_the_art_distillation`

- Preferred role: `method`
- Cue keywords: `payoff, state-of-the-art, distillation, fraction, storage, biggest, high-resolution, images, plus, better`
- Narration: The payoff is state-of-the-art distillation at a fraction of the storage, biggest on high-resolution images, plus better generalization to unseen architectures and stronger robustness to corruption.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_payoff_state_of_the_art_distillation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords payoff, state-of-the-art, distillation, fraction, storage, biggest in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_short_sparse_shared_representation_p`

- Preferred role: `content`
- Cue keywords: `short, sparse, shared, representation, powerful, general, lever, making, tiny, synthetic`
- Narration: In short, sparse, shared representation is a powerful and general lever for making tiny synthetic datasets do far more.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_short_sparse_shared_representation_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords short, sparse, shared, representation, powerful, general in title/desc so the matcher can verify semantic overlap.
