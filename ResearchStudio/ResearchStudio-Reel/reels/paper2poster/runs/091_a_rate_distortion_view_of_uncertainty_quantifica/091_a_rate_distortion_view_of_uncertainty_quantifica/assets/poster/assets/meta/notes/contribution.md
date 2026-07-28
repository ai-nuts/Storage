# Contribution

Core claim: The paper formulates uncertainty quantification as computing a rate-distortion function that compresses the training set into a codebook of prototype distributions, yielding the Distance Aware Bottleneck (DAB), a single-model, deterministic, single-forward-pass uncertainty estimator.

Supporting detail: It contributes a practical alternating-minimization learning algorithm, a "meta-probabilistic" distortion defined over distributions of embeddings, and a post-hoc variant that adds distance awareness to large pre-trained feature extractors.

Narration: Their key idea is to view uncertainty quantification through the lens of rate-distortion theory. They compress the entire training set into a small codebook of prototype distributions, and measure how far a new input is from that codebook. This gives the Distance Aware Bottleneck, or DAB: a single deterministic model that produces uncertainty in one forward pass. Along the way they contribute a practical alternating-minimization training algorithm, a meta-probabilistic distortion that operates over distributions of embeddings, and a post-hoc variant that adds distance awareness to large pre-trained feature extractors.
