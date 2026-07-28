# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_vision_transformers_overtaking_convo`

- Preferred role: `method`
- Cue keywords: `vision, transformers, overtaking, convolutional, networks, but, their, size, makes, privacy-preserving`
- Narration: Vision transformers are overtaking convolutional networks, but their size makes privacy-preserving distributed training hard.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_vision_transformers_overtaking_convo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords vision, transformers, overtaking, convolutional, networks, but in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_federated_learning_must_move_whole`

- Preferred role: `method`
- Cue keywords: `federated, learning, must, move, whole, models, split, learning, leaks, privacy`
- Narration: Federated learning must move whole models, and split learning leaks privacy because a transformer's smashed data still resembles the raw input.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_federated_learning_must_move_whole" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords federated, learning, must, move, whole, models in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_yonsei_deakin_oulu_neurips_2022`

- Preferred role: `result`
- Cue keywords: `yonsei, deakin, oulu, neurips, 2022, proposes, dp-cutmixsl, pairing, gaussian, differential-privacy`
- Narration: From Yonsei, Deakin, M.I.T., and Oulu, at NeurIPS 2022, this paper proposes DP-CutMixSL, pairing a Gaussian differential-privacy mechanism with a patch-level randomized CutMix that mixes masked patches across clients.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c3_yonsei_deakin_oulu_neurips_2022" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords yonsei, deakin, oulu, neurips, 2022, proposes in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_strengthens_privacy_while_improving`

- Preferred role: `method`
- Cue keywords: `strengthens, privacy, while, improving, accuracy`
- Narration: It strengthens privacy while improving accuracy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_strengthens_privacy_while_improving" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords strengthens, privacy, while, improving, accuracy in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_want_train_user_without_exposing`

- Preferred role: `method`
- Cue keywords: `want, train, user, without, exposing, federated, learning, keeps, local, but`
- Narration: We want to train on user data without exposing it. Federated learning keeps data local but exchanges whole models, costly for large transformers.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_want_train_user_without_exposing" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords want, train, user, without, exposing, federated in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_split_learning_instead_shares_only`

- Preferred role: `content`
- Cue keywords: `split, learning, instead, shares, only, cut-layer, activations, smashed`
- Narration: Split learning instead shares only cut-layer activations, the smashed data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_split_learning_instead_shares_only" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords split, learning, instead, shares, only, cut-layer in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_but_transformers_pooling_convolution`

- Preferred role: `method`
- Cue keywords: `but, transformers, pooling, convolution, their, smashed, barely, distorts, input, stays`
- Narration: But transformers have no pooling or convolution, so their smashed data barely distorts the input and stays visually similar to the raw image.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_but_transformers_pooling_convolution" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, transformers, pooling, convolution, their, smashed in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_similarity_leaks_privacy_preserving`

- Preferred role: `content`
- Cue keywords: `similarity, leaks, privacy, preserving, much, information, also, inflates, communication, cost`
- Narration: That similarity leaks privacy and, preserving so much information, also inflates communication cost.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_similarity_leaks_privacy_preserving" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords similarity, leaks, privacy, preserving, much, information in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_transformers_displace_cnns_old_priva`

- Preferred role: `method`
- Cue keywords: `transformers, displace, cnns, old, privacy, recipes, still, hold, authors, note`
- Narration: As transformers displace CNNs, do the old privacy recipes still hold? The authors note three things about ViT.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_transformers_displace_cnns_old_priva" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords transformers, displace, cnns, old, privacy, recipes in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_first_without_pooling_its_hidden`

- Preferred role: `content`
- Cue keywords: `first, without, pooling, its, hidden, representation, barely, distorted, regularizing, works`
- Narration: First, without pooling its hidden representation is barely distorted, so regularizing it works as well as regularizing the input, yet high mutual information leaks.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_first_without_pooling_its_hidden" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, without, pooling, its, hidden, representation in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_second_global_self_attention_makes_v`

- Preferred role: `method`
- Cue keywords: `second, global, self-attention, makes, vit, robust, large, noise, part, image`
- Narration: Second, global self-attention makes ViT robust to large noise on part of the image, ideal for Cutout and CutMix.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_second_global_self_attention_makes_v" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, global, self-attention, makes, vit, robust in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_third_every_operation_patch_level_to`

- Preferred role: `result`
- Cue keywords: `third, every, operation, patch-level, together, these, point, patch-level, randomized, cutmix`
- Narration: Third, every operation is patch-level. Together these point to a patch-level randomized CutMix of the hidden representation.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c4_third_every_operation_patch_level_to" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, every, operation, patch-level, together, these in title/desc so the matcher can verify semantic overlap.

## Slide 04: method

Heading: Method

### Cue 1: `cue_s04_c1_dp_cutmixsl_step_step_mixer_draws`

- Preferred role: `method`
- Cue keywords: `dp-cutmixsl, step, step, mixer, draws, mixing, ratios, lambda, dirichlet, distribution`
- Narration: Here is DP-CutMixSL step by step. A mixer draws mixing ratios lambda from a Dirichlet distribution and builds a pseudorandom binary mask per client, with on-patches proportional to that client's lambda.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_dp_cutmixsl_step_step_mixer_draws" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dp-cutmixsl, step, step, mixer, draws, mixing in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_client_runs_its_input_through`

- Preferred role: `title`
- Cue keywords: `client, runs, its, input, through, lower, get, smashed, masks, cutout`
- Narration: Each client runs its input through the lower model to get smashed data, masks it into Cutout smashed data, then adds white Gaussian noise for DP-Cutout smashed data, and uploads it.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s04_c2_client_runs_its_input_through" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords client, runs, its, input, through, lower in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_because_masks_mutually_exclusive_col`

- Preferred role: `title`
- Cue keywords: `because, masks, mutually, exclusive, collectively, exhaustive, patch, level, server, simply`
- Narration: Because the masks are mutually exclusive and collectively exhaustive at the patch level, the server simply adds the clients' noisy patches into DP-CutMix smashed data with no blank patches, mixing labels by the same lambda weights.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s04_c3_because_masks_mutually_exclusive_col" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, masks, mutually, exclusive, collectively, exhaustive in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_forward_backward_propagation_proceed`

- Preferred role: `content`
- Cue keywords: `forward, backward, propagation, proceed, vanilla, split, learning, crucially, only, noisy`
- Narration: Forward and backward propagation then proceed as in vanilla split learning. Crucially, only a noisy fraction of each client's data is ever exposed.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_forward_backward_propagation_proceed" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords forward, backward, propagation, proceed, vanilla, split in title/desc so the matcher can verify semantic overlap.

## Slide 05: key-result

Heading: Key Result

### Cue 1: `cue_s05_c1_without_noise_cutmixsl_gives_best`

- Preferred role: `result`
- Cue keywords: `without, noise, cutmixsl, gives, best, top-1, accuracy, every, configuration, but`
- Narration: Without noise, CutMixSL gives the best top-1 accuracy in every configuration but one.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c1_without_noise_cutmixsl_gives_best" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords without, noise, cutmixsl, gives, best, top-1 in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_cifar_10_vit_tiny_reaches_seventy_th`

- Preferred role: `result`
- Cue keywords: `cifar-10, vit-tiny, reaches, seventy-three, point, seven, seven, percent, versus, fifty-seven`
- Narration: On CIFAR-10 with ViT-Tiny it reaches seventy-three point seven seven percent, versus fifty-seven for plain split learning and sixty-eight for SplitFed.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c2_cifar_10_vit_tiny_reaches_seventy_th" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-10, vit-tiny, reaches, seventy-three, point, seven in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_pit_tiny_hits_seventy_one_point_two`

- Preferred role: `figure`
- Cue keywords: `pit-tiny, hits, seventy-one, point, two, six, fashion-mnist, tops, eighty-nine, percent`
- Narration: With PiT-Tiny it hits seventy-one point two six. On Fashion-MNIST it tops eighty-nine percent across all three architectures.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c3_pit_tiny_hits_seventy_one_point_two" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pit-tiny, hits, seventy-one, point, two, six in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_exception_vgg_16_where_mixup_edges`

- Preferred role: `method`
- Cue keywords: `exception, vgg-16, where, mixup, edges, ahead, because, cnns, focus, locally`
- Narration: The exception is VGG-16, where Mixup edges ahead, because CNNs focus locally, so replacing whole patches costs them more information than it costs transformers.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_exception_vgg_16_where_mixup_edges" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords exception, vgg-16, where, mixup, edges, ahead in title/desc so the matcher can verify semantic overlap.

## Slide 06: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s06_c1_ablations_probe_privacy_accuracy_tra`

- Preferred role: `result`
- Cue keywords: `ablations, probe, privacy-accuracy, trade-off, sweeping, noise, variance, dp-cutmixsl, best, accuracy`
- Narration: Ablations probe the privacy-accuracy trade-off. Sweeping noise variance, DP-CutMixSL has the best accuracy at nearly every level and always beats DP-MixSL.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_ablations_probe_privacy_accuracy_tra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, probe, privacy-accuracy, trade-off, sweeping, noise in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_its_rdp_epsilon_tighter_dp_sl`

- Preferred role: `content`
- Cue keywords: `its, rdp, epsilon, tighter, dp-sl, but, looser, dp-mixsl, exactly, trade-off`
- Narration: Its RDP epsilon is tighter than DP-SL but looser than DP-MixSL, exactly the trade-off theory predicts, since Mixup melts information across the whole representation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_its_rdp_epsilon_tighter_dp_sl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, rdp, epsilon, tighter, dp-sl, but in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_larger_mixing_groups_lower_both`

- Preferred role: `method`
- Cue keywords: `larger, mixing, groups, lower, both, accuracy, epsilon, hiding-in-the-crowd, effect, reconstruction`
- Narration: Larger mixing groups lower both accuracy and epsilon, a hiding-in-the-crowd effect. A reconstruction attack shows robustness rising from raw data to Mixup, patch CutMix, then Cutout.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_larger_mixing_groups_lower_both" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords larger, mixing, groups, lower, both, accuracy in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_finally_accuracy_grows_clients_scale`

- Preferred role: `result`
- Cue keywords: `finally, accuracy, grows, clients, scale, two, ten, splitfed-style, averaging, helps`
- Narration: Finally, accuracy grows as clients scale from two to ten, and SplitFed-style averaging helps further.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_finally_accuracy_grows_clients_scale" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finally, accuracy, grows, clients, scale, two in title/desc so the matcher can verify semantic overlap.

## Slide 07: takeaway

Heading: Takeaway

### Cue 1: `cue_s07_c1_takeaway_vision_transformers_you_nee`

- Preferred role: `method`
- Cue keywords: `takeaway, vision, transformers, you, need, not, trade, accuracy, privacy, split`
- Narration: The takeaway: for vision transformers, you need not trade accuracy for privacy in split learning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_takeaway_vision_transformers_you_nee" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, vision, transformers, you, need, not in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_adding_gaussian_noise_mixing_randoml`

- Preferred role: `result`
- Cue keywords: `adding, gaussian, noise, mixing, randomly, masked, patches, across, clients, amplifies`
- Narration: Adding Gaussian noise and mixing randomly masked patches across clients amplifies the differential-privacy guarantee over plain split learning and raises accuracy, with the gain provably bounded by a Mixup baseline.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_adding_gaussian_noise_mixing_randoml" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords adding, gaussian, noise, mixing, randomly, masked in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_works_because_transformers_global_se`

- Preferred role: `method`
- Cue keywords: `works, because, transformers, global, self-attention, patch, level, swapping, patches, costs`
- Narration: It works because transformers use global self-attention at the patch level, so swapping patches costs little, though it would hurt a CNN.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_works_because_transformers_global_se" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords works, because, transformers, global, self-attention, patch in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_patch_level_cutmix_privacy_regulariz`

- Preferred role: `method`
- Cue keywords: `patch-level, cutmix, privacy, regularizer, built, transformer, era`
- Narration: Patch-level CutMix is a privacy regularizer built for the transformer era.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_patch_level_cutmix_privacy_regulariz" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords patch-level, cutmix, privacy, regularizer, built, transformer in title/desc so the matcher can verify semantic overlap.
