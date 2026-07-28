# Motivation

Core claim: Value-based offline RL is powerful in theory but hard to use, needing stabilization tricks and delicate tuning; converting RL into conditional imitation learning promises a simpler alternative.

Supporting detail: If a minimal supervised recipe matches complex methods, it gives practitioners a dependable field guide and exposes where such methods still fail.

Narration: Value-based methods dominate offline and off-policy RL, and they come with appealing theoretical guarantees. But in practice they are difficult to apply. They require complex tricks to stabilize learning and careful tuning of many interacting hyperparameters. An attractive alternative is to convert the reinforcement learning problem into a conditional, filtered, or weighted imitation learning problem, using the insight that experience that is suboptimal for one task may be optimal for another. If a minimal supervised recipe can match these complex value-based methods, it would give practitioners a dependable field guide, and it would also reveal exactly where such supervised methods still break down.
