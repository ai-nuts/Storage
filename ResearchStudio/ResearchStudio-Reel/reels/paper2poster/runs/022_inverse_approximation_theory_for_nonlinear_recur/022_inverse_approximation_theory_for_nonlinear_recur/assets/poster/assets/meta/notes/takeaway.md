# Takeaway

Core claim: Nonlinear RNNs can only stably learn targets whose memory decays exponentially, so their trouble with long-term dependencies is a fundamental architectural limit, but a principled stable reparameterization provably and empirically relaxes it.

Supporting detail: The memory function and stable-approximation framework are general tools that also extend toward GRU and LSTM.

Narration: The one-line takeaway is this: no matter how you train them, plain nonlinear RNNs can only stably approximate sequence relationships whose memory fades exponentially, so their well-known struggle with long-term dependencies is baked into the architecture, not merely the optimizer. But the same analysis points to the cure. By reparameterizing the recurrent weights with a stable map like exponential or softplus, the network can keep eigenvalues near the edge of stability without losing it, provably relaxing the curse of memory and, on real tasks like MNIST, training faster and generalizing better.
