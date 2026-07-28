# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_vision_transformers_powerful_but_dat`

- Preferred role: `method`
- Cue keywords: `vision, transformers, powerful, but, data-hungry, they, only, beat, convolutional, networks`
- Narration: Vision transformers are powerful but data-hungry: they only beat convolutional networks when huge labeled datasets are available. This paper introduces PatchRot, a self-supervised technique crafted specifically for vision transformers. The key idea is simple.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_vision_transformers_powerful_but_dat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords vision, transformers, powerful, but, data-hungry, they in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_rotate_whole_image_its_individual`

- Preferred role: `method`
- Cue keywords: `rotate, whole, image, its, individual, patches, multiples, ninety, degrees, train`
- Narration: Rotate the whole image or its individual patches by multiples of ninety degrees, and train the transformer to predict every rotation angle.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_rotate_whole_image_its_individual" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rotate, whole, image, its, individual, patches in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_class_token_predicts_image_rotation`

- Preferred role: `method`
- Cue keywords: `class, token, predicts, image, rotation, capturing, global, structure, while, new`
- Narration: The class token predicts the image rotation, capturing global structure, while new per-patch heads predict each patch's rotation, capturing local detail.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_class_token_predicts_image_rotation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords class, token, predicts, image, rotation, capturing in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_after_pretraining_patchrot_features`

- Preferred role: `method`
- Cue keywords: `after, pretraining, patchrot, features, consistently, beat, both, supervised, scratch, rotnet`
- Narration: After this pretraining, PatchRot features consistently beat both supervised training from scratch and the RotNet baseline across CIFAR-10, CIFAR-100, FashionMNIST, and Tiny-ImageNet.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_after_pretraining_patchrot_features" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords after, pretraining, patchrot, features, consistently, beat in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_vision_transformers_overtaken_convol`

- Preferred role: `method`
- Cue keywords: `vision, transformers, overtaken, convolutional, networks, many, vision, tasks, but, only`
- Narration: Vision transformers have overtaken convolutional networks on many vision tasks, but only when trained on very large labeled datasets.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_vision_transformers_overtaken_convol" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords vision, transformers, overtaken, convolutional, networks, many in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_limited_labels_their_performance_fal`

- Preferred role: `content`
- Cue keywords: `limited, labels, their, performance, falls, behind, convnets, because, they, lack`
- Narration: With limited labels their performance falls behind ConvNets, because they lack built-in inductive biases like locality and translation equivariance.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_limited_labels_their_performance_fal" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords limited, labels, their, performance, falls, behind in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_labeling_scale_vits_need_expensive`

- Preferred role: `content`
- Cue keywords: `labeling, scale, vits, need, expensive, slow`
- Narration: Labeling data at the scale ViTs need is expensive and slow.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_labeling_scale_vits_need_expensive" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords labeling, scale, vits, need, expensive, slow in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_self_supervised_learning_help_learni`

- Preferred role: `method`
- Cue keywords: `self-supervised, learning, help, learning, useful, features, without, labels, but, popular`
- Narration: Self-supervised learning can help by learning useful features without labels, but the popular self-supervised pretext tasks were all designed for convolutional networks and ignore the patch-token structure that makes transformers special.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_self_supervised_learning_help_learni" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords self-supervised, learning, help, learning, useful, features in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_vision_transformer_splits_image_patc`

- Preferred role: `method`
- Cue keywords: `vision, transformer, splits, image, patches, applies, self-attention, unlike, convolutional, network`
- Narration: A vision transformer splits an image into patches and applies self-attention, so unlike a convolutional network it can produce a separate output for every patch, not just one output for the whole image.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_vision_transformer_splits_image_patc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords vision, transformer, splits, image, patches, applies in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_prior_work_called_rotnet_showed`

- Preferred role: `content`
- Cue keywords: `prior, work, called, rotnet, showed, simply, predicting, rotation, angle, image`
- Narration: Prior work called RotNet showed that simply predicting the rotation angle of an image teaches a convolutional network surprisingly rich features.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_prior_work_called_rotnet_showed" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, work, called, rotnet, showed, simply in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_natural_question_push_rotation_predi`

- Preferred role: `method`
- Cue keywords: `natural, question, push, rotation, prediction, down, patch, level, transformer, learns`
- Narration: The natural question is: can we push rotation prediction down to the patch level, so the transformer learns local features for each patch as well as global structure for the whole image?
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_natural_question_push_rotation_predi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords natural, question, push, rotation, prediction, down in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_patch_level_signal_exactly_what_toke`

- Preferred role: `content`
- Cue keywords: `patch-level, signal, exactly, what, token-based, built, exploit`
- Narration: That patch-level signal is exactly what a token-based model is built to exploit.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_patch_level_signal_exactly_what_toke" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords patch-level, signal, exactly, what, token-based, built in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_main_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, main, contributions`
- Narration: The paper makes three main contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_main_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, main, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_introduces_patchrot_self_super`

- Preferred role: `method`
- Cue keywords: `first, introduces, patchrot, self-supervised, technique, crafted, vision, transformers, predicts, rotation`
- Narration: First, it introduces PatchRot, a self-supervised technique crafted for vision transformers that predicts rotation angles at two levels: the class token predicts the whole-image rotation for global context, and new per-patch heads predict each patch's rotation for local detail.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_introduces_patchrot_self_super" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, introduces, patchrot, self-supervised, technique, crafted in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_introduces_buffer_gap_between`

- Preferred role: `method`
- Cue keywords: `second, introduces, buffer, gap, between, patches, during, network, cannot, cheat`
- Narration: Second, it introduces a buffer gap between patches during training so the network cannot cheat by matching continuous edges, forcing it to learn genuine content.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_introduces_buffer_gap_between" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, introduces, buffer, gap, between, patches in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_demonstrates_through_extensive`

- Preferred role: `method`
- Cue keywords: `third, demonstrates, through, extensive, experiments, patchrot, beats, both, supervised, scratch`
- Narration: Third, it demonstrates through extensive experiments that PatchRot beats both supervised training from scratch and the RotNet baseline across multiple datasets, and that its features transfer well and help in semi-supervised settings.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_third_demonstrates_through_extensive" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, demonstrates, through, extensive, experiments, patchrot in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_patchrot_works_follows_take_input`

- Preferred role: `result`
- Cue keywords: `patchrot, works, follows, take, input, image, either, rotate, whole, image`
- Narration: PatchRot works as follows. Take an input image and either rotate the whole image, or rotate each of its patches independently, by a random multiple of ninety degrees: zero, ninety, one-eighty, or two-seventy.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c1_patchrot_works_follows_take_input" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords patchrot, works, follows, take, input, image in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_vision_transformer_trained_predict_t`

- Preferred role: `method`
- Cue keywords: `vision, transformer, trained, predict, these, rotation, angles, simple, four-way, classification`
- Narration: The vision transformer is then trained to predict these rotation angles as a simple four-way classification. The transformer's class token, which normally predicts the object category, is repurposed to predict the whole-image rotation, capturing global structure.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_vision_transformer_trained_predict_t" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords vision, transformer, trained, predict, these, rotation in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_new_multilayer_perceptron_heads_atta`

- Preferred role: `result`
- Cue keywords: `new, multilayer-perceptron, heads, attached, patch, token, predict, individual, patch, rotation`
- Narration: New multilayer-perceptron heads are attached to each patch token to predict that individual patch's rotation, capturing local detail. To prevent the network from cheating, patches are carved from a slightly larger grid and randomly cropped, so a random buffer gap sits between them and edge continuity can't give away the answer.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c3_new_multilayer_perceptron_heads_atta" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords new, multilayer-perceptron, heads, attached, patch, token in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_happens_reduced_resolution_extra_pat`

- Preferred role: `method`
- Cue keywords: `happens, reduced, resolution, extra, patch, heads, removed, network, fine-tuned, full`
- Narration: Training happens at a reduced resolution; then the extra patch heads are removed and the network is fine-tuned at full resolution on the real classification task, with positional embeddings interpolated to the larger patch count.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_happens_reduced_resolution_extra_pat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords happens, reduced, resolution, extra, patch, heads in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_authors_test_patchrot_four_standard`

- Preferred role: `result`
- Cue keywords: `authors, test, patchrot, four, standard, image, classification, datasets, cifar-10, cifar-100`
- Narration: The authors test PatchRot on four standard image classification datasets: CIFAR-10, CIFAR-100, FashionMNIST at thirty-two by thirty-two resolution, and Tiny-ImageNet at sixty-four by sixty-four.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_authors_test_patchrot_four_standard" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, test, patchrot, four, standard, image in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_they_also_study_svhn_mnist`

- Preferred role: `method`
- Cue keywords: `they, also, study, svhn, mnist, probe, rotation-invariant, objects, like, digits`
- Narration: They also study SVHN and MNIST to probe rotation-invariant objects like digits. The backbone is a compact vision transformer with six encoder blocks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_they_also_study_svhn_mnist" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, also, study, svhn, mnist, probe in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_patch_sizes_four_pixels_small`

- Preferred role: `result`
- Cue keywords: `patch, sizes, four, pixels, small, datasets, eight, tiny-imagenet, buffer, gap`
- Narration: Patch sizes are four pixels for the small datasets and eight for Tiny-ImageNet, with a buffer gap set to a quarter of the patch size.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c3_patch_sizes_four_pixels_small" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords patch, sizes, four, pixels, small, datasets in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_beyond_plain_classification_they_eva`

- Preferred role: `result`
- Cue keywords: `beyond, plain, classification, they, evaluate, transfer, learning, between, cifar-10, cifar-100`
- Narration: Beyond plain classification, they evaluate transfer learning between CIFAR-10 and CIFAR-100, and a semi-supervised setting on CIFAR-10 where only a handful of labels, from two hundred fifty up to ten thousand, are available.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_beyond_plain_classification_they_eva" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords beyond, plain, classification, they, evaluate, transfer in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_result_patchrot_pretraining`

- Preferred role: `method`
- Cue keywords: `headline, result, patchrot, pretraining, consistently, outperforms, both, supervised, scratch, rotnet`
- Narration: The headline result is that PatchRot pretraining consistently outperforms both supervised training from scratch and the RotNet rotation baseline, on every dataset tested.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_headline_result_patchrot_pretraining" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, result, patchrot, pretraining, consistently, outperforms in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_cifar_10_full_fine_tuning_patchrot_r`

- Preferred role: `method`
- Cue keywords: `cifar-10, full, fine-tuning, patchrot, reaches, ninety-two, point, six, percent, top-one`
- Narration: On CIFAR-10 with full fine-tuning, PatchRot reaches ninety-two point six percent top-one accuracy, compared to eighty-three point nine percent for supervised training from scratch.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_cifar_10_full_fine_tuning_patchrot_r" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-10, full, fine-tuning, patchrot, reaches, ninety-two in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_cifar_100_gap_even_larger_seventy`

- Preferred role: `result`
- Cue keywords: `cifar-100, gap, even, larger, seventy, point, six, percent, top-one, versus`
- Narration: On CIFAR-100 the gap is even larger: seventy point six percent top-one versus fifty point two percent supervised, and ninety point two percent top-five. On FashionMNIST it improves ninety-four point one versus eighty-nine point eight.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_cifar_100_gap_even_larger_seventy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-100, gap, even, larger, seventy, point in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_remarkably_even_linear_probing_where`

- Preferred role: `method`
- Cue keywords: `remarkably, even, linear, probing, where, entire, network, frozen, only, final`
- Narration: Remarkably, even linear probing, where the entire network is frozen and only the final layer is trained, gets close to supervised performance, and fine-tuning just a single encoder block already beats training from scratch.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_remarkably_even_linear_probing_where" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords remarkably, even, linear, probing, where, entire in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablation_study_cifar_10_confirms_eve`

- Preferred role: `method`
- Cue keywords: `ablation, study, cifar-10, confirms, every, component, patchrot, matters, patch, rotations`
- Narration: The ablation study on CIFAR-10 confirms that every component of PatchRot matters. Training on patch rotations alone, without whole-image rotation, drops accuracy to ninety-one point eight percent because the model loses global context.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_ablation_study_cifar_10_confirms_eve" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablation, study, cifar-10, confirms, every, component in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_only_image_rotation_essentially_rotn`

- Preferred role: `method`
- Cue keywords: `only, image, rotation, essentially, rotnet, approach, adapted, transformer, drops, ninety-one`
- Narration: Using only image rotation, essentially the RotNet approach adapted to a transformer, drops it to ninety-one point zero.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_only_image_rotation_essentially_rotn" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords only, image, rotation, essentially, rotnet, approach in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_rotating_image_its_patches_together`

- Preferred role: `method`
- Cue keywords: `rotating, image, its, patches, together, single, pass, rather, separate, passes`
- Narration: Rotating the image and its patches together in a single pass, rather than in separate passes, hurts performance, as does training at the original resolution instead of the reduced resolution, and reusing the existing head instead of adding dedicated patch heads.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_rotating_image_its_patches_together" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rotating, image, its, patches, together, single in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_these_lands_below_full_method`

- Preferred role: `method`
- Cue keywords: `these, lands, below, full, method, ninety-two, point, six, percent, showing`
- Narration: Each of these lands below the full method's ninety-two point six percent, showing every design decision contributes.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_these_lands_below_full_method" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, lands, below, full, method, ninety-two in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_numbers_tell_clear_story_cifar_10`

- Preferred role: `method`
- Cue keywords: `numbers, tell, clear, story, cifar-10, patchrot, reaches, ninety-two, point, six`
- Narration: The numbers tell a clear story. On CIFAR-10, PatchRot reaches ninety-two point six percent top-one accuracy, an improvement of eight point seven points over supervised training from scratch.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_numbers_tell_clear_story_cifar_10" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords numbers, tell, clear, story, cifar-10, patchrot in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_cifar_100_improvement_over_twenty_po`

- Preferred role: `result`
- Cue keywords: `cifar-100, improvement, over, twenty, points, fifty, point, two, seventy, point`
- Narration: On CIFAR-100 the improvement is over twenty points, from fifty point two to seventy point six percent top-one, and ninety point two percent top-five.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_cifar_100_improvement_over_twenty_po" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-100, improvement, over, twenty, points, fifty in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_fashionmnist_improves_ninety_four_po`

- Preferred role: `result`
- Cue keywords: `fashionmnist, improves, ninety-four, point, one, percent, tiny-imagenet, top-five, rises, seventy-three`
- Narration: FashionMNIST improves to ninety-four point one percent and Tiny-ImageNet's top-five rises to seventy-three point four percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_fashionmnist_improves_ninety_four_po" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fashionmnist, improves, ninety-four, point, one, percent in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_semi_supervised_setting_only_four_th`

- Preferred role: `method`
- Cue keywords: `semi-supervised, setting, only, four, thousand, labeled, cifar-10, images, patchrot, reaches`
- Narration: In the semi-supervised setting with only four thousand labeled CIFAR-10 images, PatchRot reaches eighty-one percent accuracy, versus roughly fifty-four percent for supervised training on the same labels, showing how valuable the self-supervised features are when labels are scarce.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_semi_supervised_setting_only_four_th" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords semi-supervised, setting, only, four, thousand, labeled in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_very_simple_idea_predicting`

- Preferred role: `method`
- Cue keywords: `takeaway, very, simple, idea, predicting, rotation, both, whole, image, individual`
- Narration: The takeaway is that a very simple idea, predicting the rotation of both the whole image and each individual patch, turns out to be a self-supervised task perfectly suited to vision transformers.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_takeaway_very_simple_idea_predicting" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, very, simple, idea, predicting, rotation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_because_class_token_learns_global`

- Preferred role: `method`
- Cue keywords: `because, class, token, learns, global, structure, patch, heads, learn, local`
- Narration: Because the class token learns global structure and the patch heads learn local detail, PatchRot teaches the transformer rich features without any labels, and those features reliably beat supervised training from scratch and the RotNet baseline across four datasets, in transfer learning, and especially when labeled data is scarce.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_because_class_token_learns_global" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, class, token, learns, global, structure in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_lightweight_practical_recipe_pretrai`

- Preferred role: `method`
- Cue keywords: `lightweight, practical, recipe, pretraining, vision, transformers, limited`
- Narration: It is a lightweight, practical recipe for pretraining vision transformers on limited data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_lightweight_practical_recipe_pretrai" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lightweight, practical, recipe, pretraining, vision, transformers in title/desc so the matcher can verify semantic overlap.
