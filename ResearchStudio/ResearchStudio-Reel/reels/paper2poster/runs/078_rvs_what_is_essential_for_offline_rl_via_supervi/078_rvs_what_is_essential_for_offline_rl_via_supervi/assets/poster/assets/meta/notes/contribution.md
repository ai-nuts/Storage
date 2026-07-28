# Contribution

Core claim: The paper unifies existing goal- and reward-conditioned methods under a single RvS framework, then empirically isolates the essential design choices: model capacity, regularization, and the conditioning variable.

Supporting detail: It shows a two-layer MLP maximizing likelihood is competitive with state-of-the-art TD and Transformer methods, and it exposes RvS weakness on random data as an open problem.

Narration: The paper makes three contributions. First, it does not propose a brand-new algorithm; instead it places many existing goal-conditioned and reward-conditioned methods under one common framework, which the authors call RvS, reinforcement learning via supervised learning. Second, through extensive experiments it boils these methods down to their essential elements, showing that a two-layer feedforward network trained to maximize likelihood is competitive with far more complex state-of-the-art methods. Third, it identifies exactly which design choices matter, namely model capacity, regularization, and what you condition on, and it honestly probes the limits, showing that RvS is comparatively weak on purely random data.
