# Ablation Study

Core claim: The Metropolis-Hastings rejection step is important for stabilizing training, while the number of ALD iterations T has little effect once T ≥ 2. The encoder's last-layer dimensionality must satisfy d ≥ n (batch size) for samples to converge to the true posterior.

Supporting detail: With d < n some datapoints' samples collapse to a small region, empirically confirming the rank condition of Theorem 1.

Narration: Two ablations. Encoder capacity confirms the theory: when the final linear layer is at least the batch size, samples match the true posterior; smaller, and some collapse. On images, the Metropolis-Hastings step stabilizes training, while iteration count barely matters beyond two, so experiments use just two.
