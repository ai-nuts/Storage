# Method

Core claim: Using stochastic approximation techniques, the authors treat mSGD and AdaGrad as noisy dynamical systems and show their iterates track a limiting ODE toward the stationary set. A stability lemma bounds the expected loss, and a relaxed noise condition controls gradient fluctuations without requiring a uniform bound over the whole space.

Supporting detail: For mSGD, a decreasing step size satisfying the Robbins-Monro conditions counteracts noise while the momentum coefficient stays static; for AdaGrad, the adaptive (random, gradient-dependent) step size is handled by carefully bounding the conditionally dependent terms that block naive conditional-expectation arguments.

Narration: The analysis uses stochastic approximation, treating each algorithm as a noisy gradient flow. A stability lemma bounds the expected loss. Instead of uniformly bounded noise, they bound it relative to the loss. mSGD uses decreasing Robbins-Monro steps with static momentum; AdaGrad's adaptive step needs new bounds.
