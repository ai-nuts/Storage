# Ablation Study

Core claim: Comparing recurrent-weight parameterizations on MNIST, the three stable reparameterizations (softplus, exp, inverse) all outperform the direct/unstable parameterization g(M)=M in optimization speed and test accuracy, while final capacity is comparable.

Supporting detail: Reparameterization is also demonstrated with exp and softplus maps on linear RNNs for polynomial-decay targets (Figure 4), restoring a continuous limiting perturbation curve.

Narration: The key ablation varies only how the recurrent weight is parameterized, holding initialization fixed. On MNIST, the three stable reparameterizations, softplus, exponential, and inverse, all speed up optimization and reach higher test accuracy than the direct, unstable parameterization where the weight is used as-is. Importantly, since reparameterization does not change the model's inherent capacity, the final performance across stable variants is comparable, isolating the effect as an optimization and stability benefit rather than a capacity change. On the synthetic side, applying exponential and softplus reparameterizations to linear RNNs approximating polynomial-decay targets restores the expected continuous limiting error curve, confirming stability is recovered.
