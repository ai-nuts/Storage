# Ablation Study

Core claim: No ablation experiments are performed; the paper instead discusses design variants — different choices of the function f for the weight- or energy-dependent learning rate, and different activation functions — as directions to explore for modeling normal versus pathological behavioral modes.

Supporting detail: It notes that linear versus nonlinear forms of f, and sigmoid, Heaviside, or trigonometric activations, would be expected to yield qualitatively different network dynamics worth systematic study.

Narration: There are no ablation experiments in this work, since no model is trained. The paper does, however, sketch the variations that a future empirical study should compare. These include different forms of the function that links the learning rate to weights or to energy changes, ranging from simple linear approximations to more complex nonlinear ones, and different activation functions such as sigmoid, Heaviside threshold, and trigonometric functions. The author suggests these variations could reproduce different normal and pathological behavioral modes in biological systems, and are worth exploring systematically once the mechanisms are implemented.
