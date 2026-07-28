# Headline Numbers

Core claim: - Up to 70% reduction in compression time vs SOTA GS - Up to 3.52x total training speedup over DGC (35.9x over FULL) at equal convergence - Table 2 speedups over DGC: ResNet50 1.42x, ViT 2.15x, MLP-Mixer 1.72x, XML 3.52x - Decoding overhead reduced from linear in #GPUs to nearly constant

Supporting detail: DGC's GPU compression incurs ~7x the memory accesses of the d-comparison lower bound; DRAGONN removes this via O(1)-dependency hashing.

Narration: The key numbers are: up to a seventy percent reduction in compression time versus state-of-the-art sparsification; up to three-and-a-half times faster total training than DGC and up to thirty-six times faster than full synchronization at equal convergence; per-model speedups over DGC of about one-point-four on ResNet50, two-point-two on ViT, one-point-seven on MLP-Mixer, and three-point-five on extreme classification; and a decoding overhead reduced from growing linearly with the GPU count to nearly constant.
