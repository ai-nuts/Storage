# Ablation Study

Core claim: A component ablation isolates the three parts. The hashing compressor alone gives the base speedup; adding efficiency-aware tensor selection raises it (e.g. to 1.92x on one model), and adding sparse decoding pushes it further (up to 4.33x). Sparse decoding's speedup exceeds K-fold because it removes the linear-in-GPU decode cost.

Supporting detail: Micro-benchmarks (Figure 5) confirm DRAGONN has the lowest encoding time across tensor sizes and that sparse decoding stays nearly flat as GPUs increase, whereas dense decoding grows linearly.

Narration: An ablation study separates the contributions of the three components. The hashing-based compressor by itself provides the base improvement; layering on efficiency-aware tensor selection increases the speedup, for example to about one-point-nine times on one model, and adding sparse decoding pushes it as high as four-point-three times. Notably, the benefit of sparse decoding can exceed the number of workers, because it eliminates the decode cost that otherwise grows linearly with the number of GPUs. Micro-benchmarks confirm DRAGONN has the lowest encoding time across all tensor sizes and that its decode time stays nearly flat as GPUs are added.
