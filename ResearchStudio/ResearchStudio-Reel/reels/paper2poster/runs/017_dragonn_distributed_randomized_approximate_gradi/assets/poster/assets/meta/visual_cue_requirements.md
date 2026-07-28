# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_dragonn_randomized_hashing_algorithm`

- Preferred role: `method`
- Cue keywords: `dragonn, randomized, hashing, algorithm, gradient, sparsification, data-parallel, distributed, rice, university`
- Narration: DRAGONN is a randomized hashing algorithm for gradient sparsification in data-parallel distributed training, from Rice University and ThirdAI.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_dragonn_randomized_hashing_algorithm" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dragonn, randomized, hashing, algorithm, gradient, sparsification in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_distributed_synchronizing_gradients`

- Preferred role: `method`
- Cue keywords: `distributed, synchronizing, gradients, across, gpus, main, efficiency, bottleneck, gradient, sparsification`
- Narration: In distributed training, synchronizing gradients across GPUs is the main efficiency bottleneck, and gradient sparsification methods were meant to help, but their own compression overhead has become the new bottleneck.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_distributed_synchronizing_gradients" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords distributed, synchronizing, gradients, across, gpus, main in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_dragonn_replaces_exact_parallel_pref`

- Preferred role: `method`
- Cue keywords: `dragonn, replaces, exact, parallel-prefix-sum, operations, used, prior, methods, direct, hashing`
- Narration: DRAGONN replaces the exact parallel-prefix-sum operations used by prior methods with direct hashing, cutting compression time by up to seventy percent and delivering up to three-and-a-half times faster training throughput.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_dragonn_replaces_exact_parallel_pref" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dragonn, replaces, exact, parallel-prefix-sum, operations, used in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_data_parallel_distributed_standard_w`

- Preferred role: `method`
- Cue keywords: `data-parallel, distributed, standard, way, scale, deep, learning, across, many, gpus`
- Narration: Data-parallel distributed training is the standard way to scale deep learning across many GPUs, but synchronizing gradients between workers is the dominant cost.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_data_parallel_distributed_standard_w" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords data-parallel, distributed, standard, way, scale, deep in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_gradient_sparsification_promised_rel`

- Preferred role: `content`
- Cue keywords: `gradient, sparsification, promised, relief, transmitting, only, small, subset, gradients, yet`
- Narration: Gradient sparsification promised relief by transmitting only a small subset of gradients, yet in practice the time spent compressing the gradients grew so large that it cancelled out the communication savings.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_gradient_sparsification_promised_rel" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gradient, sparsification, promised, relief, transmitting, only in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_shows_once_tensor_exceeds_about`

- Preferred role: `method`
- Cue keywords: `shows, once, tensor, exceeds, about, sixteen, megabytes, compression, overhead, becomes`
- Narration: The paper shows that once a tensor exceeds about sixteen megabytes, this compression overhead becomes the single largest efficiency bottleneck, and for small tensors sparsification can even be slower than sending everything.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_shows_once_tensor_exceeds_about" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords shows, once, tensor, exceeds, about, sixteen in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_leading_sparsification_method_deep_g`

- Preferred role: `method`
- Cue keywords: `leading, sparsification, method, deep, gradient, compression, selects, gradients, above, estimated`
- Narration: The leading sparsification method, Deep Gradient Compression, selects gradients above an estimated threshold, which is an approximate operation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_leading_sparsification_method_deep_g" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords leading, sparsification, method, deep, gradient, compression in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_but_place_those_gradients_memory`

- Preferred role: `content`
- Cue keywords: `but, place, those, gradients, memory, without, conflicts, relies, parallel, prefix`
- Narration: But to place those gradients into memory without conflicts it relies on parallel prefix sum, an exact algorithm that builds a balanced binary tree, runs in logarithmic sequential steps, and touches memory about seven times more than the theoretical lower bound.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_but_place_those_gradients_memory" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, place, those, gradients, memory, without in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_authors_call_exact_approximate_misma`

- Preferred role: `content`
- Cue keywords: `authors, call, exact-approximate, mismatch, since, only, approximate, set, top, gradients`
- Narration: The authors call this an exact-approximate mismatch: since only an approximate set of top gradients is required, using an expensive exact algorithm to place them is wasted effort.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_authors_call_exact_approximate_misma" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, call, exact-approximate, mismatch, since, only in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, contributions`
- Narration: The paper makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_proposes_dragonn_hashing_based`

- Preferred role: `result`
- Cue keywords: `first, proposes, dragonn, hashing-based, sparsification, algorithm, slashes, compression, overhead, while`
- Narration: First, it proposes DRAGONN, a hashing-based sparsification algorithm that slashes compression overhead while keeping the same per-iteration convergence, backed by theoretical bounds on both compression error and generalization error.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c2_first_proposes_dragonn_hashing_based" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, proposes, dragonn, hashing-based, sparsification, algorithm in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_adds_two_system_level_optimiz`

- Preferred role: `method`
- Cue keywords: `second, adds, two, system-level, optimizations, efficiency-aware, tensor, selection, only, compresses`
- Narration: Second, it adds two system-level optimizations: an efficiency-aware tensor selection that only compresses tensors where it actually pays off, and a sparse decoding scheme that keeps decode cost from growing with the number of GPUs.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_adds_two_system_level_optimiz" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, adds, two, system-level, optimizations, efficiency-aware in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_evaluates_method_broadly_acros`

- Preferred role: `method`
- Cue keywords: `third, evaluates, method, broadly, across, vision, recommendation, models, demonstrates, substantial`
- Narration: Third, it evaluates the method broadly across vision and recommendation models and demonstrates substantial end-to-end training speedups.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_third_evaluates_method_broadly_acros" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, evaluates, method, broadly, across, vision in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_dragonn_works_pre_allocating_small_m`

- Preferred role: `content`
- Cue keywords: `dragonn, works, pre-allocating, small, memory, buffer, sized, compression, ratio, gradient`
- Narration: DRAGONN works by pre-allocating a small memory buffer sized to the compression ratio. For each gradient whose absolute value clears the threshold, it hashes the gradient's index to a slot and writes it directly, rather than scanning to compute nonzero positions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_dragonn_works_pre_allocating_small_m" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dragonn, works, pre-allocating, small, memory, buffer in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_two_indices_collide_later_one`

- Preferred role: `content`
- Cue keywords: `two, indices, collide, later, one, simply, overwrites, earlier, any, slot`
- Narration: If two indices collide, the later one simply overwrites the earlier, and any slot left empty maps to zero.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_two_indices_collide_later_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, indices, collide, later, one, simply in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_because_writing_memory_atomic_operat`

- Preferred role: `content`
- Cue keywords: `because, writing, memory, atomic, operation, gpus, many, threads, hash, write`
- Narration: Because writing memory is an atomic operation on GPUs, many threads can hash and write at the same time with no dependency between them, so the whole compression needs only d comparisons plus l hash operations, essentially the theoretical lower bound.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_because_writing_memory_atomic_operat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, writing, memory, atomic, operation, gpus in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_deploy_well_dragonn_adds_two`

- Preferred role: `content`
- Cue keywords: `deploy, well, dragonn, adds, two, tricks, only, compresses, tensor, when`
- Narration: To deploy it well, DRAGONN adds two tricks: it only compresses a tensor when the compression time is smaller than the communication it would save, and it batches all the compressed tensors received from other workers into one sparse decode, so decoding cost stays nearly constant no matter how many GPUs participate.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_deploy_well_dragonn_adds_two" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deploy, well, dragonn, adds, two, tricks in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_span_four_models_coverin`

- Preferred role: `method`
- Cue keywords: `experiments, span, four, models, covering, both, vision, recommendation-style, workloads, resnet50`
- Narration: The experiments span four models covering both vision and recommendation-style workloads: ResNet50 trained on ImageNet, Vision Transformer and MLP-Mixer fine-tuned on Cifar10 from ImageNet-21k pretraining, and an extreme multi-label classification model on the Wiki10-31K dataset.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_experiments_span_four_models_coverin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, span, four, models, covering, both in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_testbed_sixteen_nvidia_v100_gpus`

- Preferred role: `method`
- Cue keywords: `testbed, sixteen, nvidia, v100, gpus, across, two, machines, connected, twenty-five`
- Narration: The testbed is sixteen Nvidia V100 GPUs across two machines connected by a twenty-five gigabit network, running PyTorch with Horovod and NCCL, and using memory-momentum error feedback to preserve accuracy across all sparsification methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_testbed_sixteen_nvidia_v100_gpus" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords testbed, sixteen, nvidia, v100, gpus, across in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_result_dragonn_cuts_compres`

- Preferred role: `method`
- Cue keywords: `headline, result, dragonn, cuts, compression, time, seventy, percent, compared, best`
- Narration: The headline result is that DRAGONN cuts compression time by up to seventy percent compared to the best existing sparsification methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_headline_result_dragonn_cuts_compres" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, result, dragonn, cuts, compression, time in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_reaching_same_level_convergence_deli`

- Preferred role: `method`
- Cue keywords: `reaching, same, level, convergence, delivers, three-and-a-half, times, higher, total, throughput`
- Narration: Reaching the same level of convergence, it delivers up to three-and-a-half times higher total training throughput than Deep Gradient Compression, and up to nearly thirty-six times over full gradient synchronization, all while matching the test accuracy of full synchronization.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_reaching_same_level_convergence_deli" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reaching, same, level, convergence, delivers, three-and-a-half in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_importantly_its_advantage_over_dgc`

- Preferred role: `method`
- Cue keywords: `importantly, its, advantage, over, dgc, grows, more, gpus, added, which`
- Narration: Importantly, its advantage over DGC grows as more GPUs are added, which signals strong scalability, and the authors expect the gains to widen further on faster networks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_importantly_its_advantage_over_dgc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords importantly, its, advantage, over, dgc, grows in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablation_study_separates_contributio`

- Preferred role: `content`
- Cue keywords: `ablation, study, separates, contributions, three, components`
- Narration: An ablation study separates the contributions of the three components.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_ablation_study_separates_contributio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablation, study, separates, contributions, three, components in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_hashing_based_compressor_itself_prov`

- Preferred role: `method`
- Cue keywords: `hashing-based, compressor, itself, provides, base, improvement, layering, efficiency-aware, tensor, selection`
- Narration: The hashing-based compressor by itself provides the base improvement; layering on efficiency-aware tensor selection increases the speedup, for example to about one-point-nine times on one model, and adding sparse decoding pushes it as high as four-point-three times.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_hashing_based_compressor_itself_prov" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords hashing-based, compressor, itself, provides, base, improvement in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_notably_benefit_sparse_decoding_exce`

- Preferred role: `content`
- Cue keywords: `notably, benefit, sparse, decoding, exceed, number, workers, because, eliminates, decode`
- Narration: Notably, the benefit of sparse decoding can exceed the number of workers, because it eliminates the decode cost that otherwise grows linearly with the number of GPUs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_notably_benefit_sparse_decoding_exce" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords notably, benefit, sparse, decoding, exceed, number in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_micro_benchmarks_confirm_dragonn_low`

- Preferred role: `result`
- Cue keywords: `micro-benchmarks, confirm, dragonn, lowest, encoding, time, across, all, tensor, sizes`
- Narration: Micro-benchmarks confirm DRAGONN has the lowest encoding time across all tensor sizes and that its decode time stays nearly flat as GPUs are added.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_micro_benchmarks_confirm_dragonn_low" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords micro-benchmarks, confirm, dragonn, lowest, encoding, time in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_key_numbers_seventy_percent_reductio`

- Preferred role: `method`
- Cue keywords: `key, numbers, seventy, percent, reduction, compression, time, versus, state-of-the-art, sparsification`
- Narration: The key numbers are: up to a seventy percent reduction in compression time versus state-of-the-art sparsification; up to three-and-a-half times faster total training than DGC and up to thirty-six times faster than full synchronization at equal convergence; per-model speedups over DGC of about one-point-four on ResNet50, two-point-two on ViT, one-point-seven on MLP-Mixer, and three-point-five on extreme classification; and a decoding overhead reduced from growing linearly with the GPU count to nearly constant.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_key_numbers_seventy_percent_reductio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, numbers, seventy, percent, reduction, compression in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_lesson_simple_since_gradient`

- Preferred role: `method`
- Cue keywords: `lasting, lesson, simple, since, gradient, sparsification, only, ever, needs, approximate`
- Narration: The lasting lesson is simple: since gradient sparsification only ever needs an approximate set of top gradients, it should not pay for an exact selection algorithm.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_lasting_lesson_simple_since_gradient" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, lesson, simple, since, gradient, sparsification in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_swapping_exact_parallel_prefix_sum`

- Preferred role: `method`
- Cue keywords: `swapping, exact, parallel, prefix, sum, direct, randomized, hashing, dragonn, turns`
- Narration: By swapping exact parallel prefix sum for direct randomized hashing, DRAGONN turns a sequential, dependency-heavy compression step into an embarrassingly parallel one, removes the overhead that had been cancelling out sparsification's benefits, and, together with tensor selection and sparse decoding, makes gradient sparsification finally pay off at scale without sacrificing accuracy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_swapping_exact_parallel_prefix_sum" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords swapping, exact, parallel, prefix, sum, direct in title/desc so the matcher can verify semantic overlap.
