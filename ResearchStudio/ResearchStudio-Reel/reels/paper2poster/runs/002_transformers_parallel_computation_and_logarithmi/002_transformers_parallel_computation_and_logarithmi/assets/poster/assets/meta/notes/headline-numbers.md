# Headline Numbers

Core claim: - Depth to solve k-hop induction heads: L = ⌊log₂ k⌋ + 2 (matched by theory and experiment) - +1 layer ≈ 2× the largest learnable k (exponential benefit of depth); 6 layers solve all k ≤ 16 - R-round MPC protocol → transformer of depth R + 1; depth-L transformer → O(L)-round MPC - Competing architectures need depth L ≥ k: multi-layer RNNs / Mamba (Cor. 5.2) and sub-quadratic attention like Performer (Cor. 5.3)

Supporting detail: Trained models span 500K–5M parameters; MPC simulation uses embedding dimension m = O(n^{4δ} log n) and H = O(log log n) heads.

Narration: A few numbers capture the paper. Solving k-hop needs depth equal to floor of log base two of k plus two, and that formula holds both in the proof and in the trained networks. Adding a single layer roughly doubles the reach in k, so six layers cover everything up to sixteen hops. The simulation constants are clean too: an R-round parallel protocol becomes a transformer of depth R plus one, and any depth-L transformer collapses into order-L parallel rounds. The contrast with other architectures is stark: multi-layer recurrent networks, and by extension state-space models like Mamba, need depth at least k, and so do efficient sub-quadratic attention variants like Performer. Where the transformer is logarithmic in k, the alternatives are linear.
