---
title: DRAGONN: Distributed Randomized Approximate Gradients of Neural Networks
authors: Zhuang Wang¹, Zhaozhuo Xu¹, Xinyu Crystal Wu¹, Anshumali Shrivastava¹², T. S. Eugene Ng¹
institutes: ¹Rice University; ²ThirdAI Corp
venue: ICML 2022
paper_url: https://proceedings.mlr.press/v162/wang22aj.html
code_url: https://github.com/zhuangwang93/dragonn
title_audio_script: DRAGONN is a randomized hashing algorithm for gradient sparsification in data-parallel distributed training, from Rice University and ThirdAI. In distributed training, synchronizing gradients across GPUs is the main efficiency bottleneck, and gradient sparsification methods were meant to help, but their own compression overhead has become the new bottleneck. DRAGONN replaces the exact parallel-prefix-sum operations used by prior methods with direct hashing, cutting compression time by up to seventy percent and delivering up to three-and-a-half times faster training throughput.
---

## Problem
**Necessary:** In data-parallel distributed training, gradient synchronization is the efficiency bottleneck. Gradient sparsification (GS) reduces traffic, but its compression overhead now outweighs the communication savings, becoming the new bottleneck.
**Additional:** For tensors above 2^24 bytes the compression overhead exceeds communication and other overheads; for small tensors GS can even be slower than full synchronization.
**Audio script:** Data-parallel distributed training is the standard way to scale deep learning across many GPUs, but synchronizing gradients between workers is the dominant cost. Gradient sparsification promised relief by transmitting only a small subset of gradients, yet in practice the time spent compressing the gradients grew so large that it cancelled out the communication savings. The paper shows that once a tensor exceeds about sixteen megabytes, this compression overhead becomes the single largest efficiency bottleneck, and for small tensors sparsification can even be slower than sending everything.

## Motivation
**Necessary:** State-of-the-art GS methods such as DGC extract approximate top-k gradients using exact parallel prefix sum, an inherently sequential O(log d) algorithm that scans the tensor multiple times, incurring roughly 7x more memory accesses than the lower bound.
**Additional:** The authors argue this is an exact-approximate mismatch: only approximate top-k gradients are needed, so paying for an exact selection algorithm is unnecessary overhead.
**Audio script:** The leading sparsification method, Deep Gradient Compression, selects gradients above an estimated threshold, which is an approximate operation. But to place those gradients into memory without conflicts it relies on parallel prefix sum, an exact algorithm that builds a balanced binary tree, runs in logarithmic sequential steps, and touches memory about seven times more than the theoretical lower bound. The authors call this an exact-approximate mismatch: since only an approximate set of top gradients is required, using an expensive exact algorithm to place them is wasted effort.

## Contribution
**Necessary:** (1) DRAGONN, a randomized hashing algorithm for GS that reduces compression overhead while preserving iteration-wise accuracy, with theoretical bounds on compression and generalization error. (2) System-level optimizations: efficiency-aware tensor selection and sparse decoding. (3) Extensive vision and recommendation evaluation showing large end-to-end speedups.
**Additional:** DRAGONN supports massively parallel gradient extraction because independent threads can hash and write indices simultaneously without ordering dependencies.
**Audio script:** The paper makes three contributions. First, it proposes DRAGONN, a hashing-based sparsification algorithm that slashes compression overhead while keeping the same per-iteration convergence, backed by theoretical bounds on both compression error and generalization error. Second, it adds two system-level optimizations: an efficiency-aware tensor selection that only compresses tensors where it actually pays off, and a sparse decoding scheme that keeps decode cost from growing with the number of GPUs. Third, it evaluates the method broadly across vision and recommendation models and demonstrates substantial end-to-end training speedups.

## Method
**Necessary:** DRAGONN pre-allocates a compressed memory buffer and, for every gradient above the threshold, hashes its index directly into a memory slot instead of computing nonzero positions with prefix sum. Collisions overwrite prior entries and empty slots (-1) map to zero. Because memory writes are atomic on GPUs, many threads hash and write in parallel with no ordering dependency, so the algorithm needs only d comparisons plus l hashing operations, near the d-comparison lower bound.
**Additional:** DRAGONN is deployed in practice with efficiency-aware tensor selection (compress a tensor only when compression time is less than the communication savings) and a sparse decoding mechanism that batches the K received compressed tensors into a single decode, making decoding cost nearly constant in the number of GPUs.
**Key equation:** `$\text{if } |G[i]| \ge t:\ j \leftarrow h(i),\ I[j] \leftarrow i$` ; `$T_{comp}(d) < T_{full}(d) - T_{spr}(d)$`
**Audio script:** DRAGONN works by pre-allocating a small memory buffer sized to the compression ratio. For each gradient whose absolute value clears the threshold, it hashes the gradient's index to a slot and writes it directly, rather than scanning to compute nonzero positions. If two indices collide, the later one simply overwrites the earlier, and any slot left empty maps to zero. Because writing memory is an atomic operation on GPUs, many threads can hash and write at the same time with no dependency between them, so the whole compression needs only d comparisons plus l hash operations, essentially the theoretical lower bound. To deploy it well, DRAGONN adds two tricks: it only compresses a tensor when the compression time is smaller than the communication it would save, and it batches all the compressed tensors received from other workers into one sparse decode, so decoding cost stays nearly constant no matter how many GPUs participate.

## Dataset / Benchmark
**Necessary:** Evaluated on four models: ResNet50 on ImageNet-1K, ViT and MLP-Mixer fine-tuned on Cifar10 (pretrained on ImageNet-21k), and an extreme multi-label classification (XML) model on Wiki10-31K.
**Additional:** Testbed: 16 Nvidia Tesla V100-32GB GPUs (2 machines x 8 GPUs), 25Gbps network, CUDA 11.0, PyTorch 1.8.0, NCCL 2.7.8, Horovod 0.19.1, with memory-momentum error feedback.
**Audio script:** The experiments span four models covering both vision and recommendation-style workloads: ResNet50 trained on ImageNet, Vision Transformer and MLP-Mixer fine-tuned on Cifar10 from ImageNet-21k pretraining, and an extreme multi-label classification model on the Wiki10-31K dataset. The testbed is sixteen Nvidia V100 GPUs across two machines connected by a twenty-five gigabit network, running PyTorch with Horovod and NCCL, and using memory-momentum error feedback to preserve accuracy across all sparsification methods.

## Key Result
**Necessary:** DRAGONN reduces compression time by up to 70% versus state-of-the-art GS, and reaches the same convergence with up to 3.52x speedup in total training throughput over DGC and up to 35.9x over full synchronization, while matching FULL's test accuracy.
**Additional:** The speedup of DRAGONN over DGC grows with the number of GPUs, showing better scalability; gains are expected to widen on faster networks where communication-to-compression ratio shifts toward compression.
**Audio script:** The headline result is that DRAGONN cuts compression time by up to seventy percent compared to the best existing sparsification methods. Reaching the same level of convergence, it delivers up to three-and-a-half times higher total training throughput than Deep Gradient Compression, and up to nearly thirty-six times over full gradient synchronization, all while matching the test accuracy of full synchronization. Importantly, its advantage over DGC grows as more GPUs are added, which signals strong scalability, and the authors expect the gains to widen further on faster networks.

## Ablation Study
**Necessary:** A component ablation isolates the three parts. The hashing compressor alone gives the base speedup; adding efficiency-aware tensor selection raises it (e.g. to 1.92x on one model), and adding sparse decoding pushes it further (up to 4.33x). Sparse decoding's speedup exceeds K-fold because it removes the linear-in-GPU decode cost.
**Additional:** Micro-benchmarks (Figure 5) confirm DRAGONN has the lowest encoding time across tensor sizes and that sparse decoding stays nearly flat as GPUs increase, whereas dense decoding grows linearly.
**Audio script:** An ablation study separates the contributions of the three components. The hashing-based compressor by itself provides the base improvement; layering on efficiency-aware tensor selection increases the speedup, for example to about one-point-nine times on one model, and adding sparse decoding pushes it as high as four-point-three times. Notably, the benefit of sparse decoding can exceed the number of workers, because it eliminates the decode cost that otherwise grows linearly with the number of GPUs. Micro-benchmarks confirm DRAGONN has the lowest encoding time across all tensor sizes and that its decode time stays nearly flat as GPUs are added.

## Headline Numbers
**Necessary:**
- Up to 70% reduction in compression time vs SOTA GS
- Up to 3.52x total training speedup over DGC (35.9x over FULL) at equal convergence
- Table 2 speedups over DGC: ResNet50 1.42x, ViT 2.15x, MLP-Mixer 1.72x, XML 3.52x
- Decoding overhead reduced from linear in #GPUs to nearly constant
**Additional:** DGC's GPU compression incurs ~7x the memory accesses of the d-comparison lower bound; DRAGONN removes this via O(1)-dependency hashing.
**Audio script:** The key numbers are: up to a seventy percent reduction in compression time versus state-of-the-art sparsification; up to three-and-a-half times faster total training than DGC and up to thirty-six times faster than full synchronization at equal convergence; per-model speedups over DGC of about one-point-four on ResNet50, two-point-two on ViT, one-point-seven on MLP-Mixer, and three-point-five on extreme classification; and a decoding overhead reduced from growing linearly with the GPU count to nearly constant.

## Takeaway
**Necessary:** Because gradient sparsification only needs approximate top-k gradients, replacing exact parallel-prefix-sum selection with direct randomized hashing removes the compression bottleneck, making GS actually pay off in distributed training.
**Additional:** Hashing turns a sequential, dependency-heavy operation into an embarrassingly parallel one, and pairing it with tensor selection and sparse decoding delivers end-to-end scalable speedups without hurting accuracy.
**Audio script:** The lasting lesson is simple: since gradient sparsification only ever needs an approximate set of top gradients, it should not pay for an exact selection algorithm. By swapping exact parallel prefix sum for direct randomized hashing, DRAGONN turns a sequential, dependency-heavy compression step into an embarrassingly parallel one, removes the overhead that had been cancelling out sparsification's benefits, and, together with tensor selection and sparse decoding, makes gradient sparsification finally pay off at scale without sacrificing accuracy.
