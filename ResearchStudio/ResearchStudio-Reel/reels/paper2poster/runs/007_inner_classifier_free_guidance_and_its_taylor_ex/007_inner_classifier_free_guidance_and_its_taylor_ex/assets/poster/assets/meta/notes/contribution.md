# Contribution

Core claim: The paper proposes Inner Classifier-Free Guidance (ICFG), showing that CFG is exactly the first-order case of a Taylor expansion of ICFG around guidance strength β = 1, and derives a second-order implementation that adds new information without changing the training policy.

Supporting detail: It contributes a training policy based on a correlation metric between condition and data, two second-order sampling algorithms (a strict and a practical non-strict version), and a convergence analysis of the Taylor expansion.

Narration: The central contribution is a reframing: standard CFG is not the whole story, it is just the first-order term of a more general expansion the authors call inner classifier-free guidance. By writing the guided score as a Taylor series in the guidance strength around one, they recover CFG as the first-order case and then add a second-order term. This term is computed from the existing pretrained model, so no retraining is needed. They also provide a training policy, two sampling algorithms, and a convergence analysis.
