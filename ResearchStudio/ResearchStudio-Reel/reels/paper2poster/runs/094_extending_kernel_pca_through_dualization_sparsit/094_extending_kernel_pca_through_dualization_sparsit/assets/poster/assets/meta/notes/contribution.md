# Contribution

Core claim: The paper derives a general dual formulation of Kernel PCA as a difference of convex functions that (1) enables SVD-free gradient-based solvers, including for infinite-dimensional feature spaces, and (2) unifies robust and sparse variants through Moreau-envelope objectives in a single framework.

Supporting detail: It provides the dualization theory (nuclear-norm gradient, critical-point characterization), practical L-BFGS and DC algorithms, and closed-form proximal operators for Huber and ε-insensitive losses.

Narration: The core contribution is a general dual-based formulation of Kernel PCA built on the dualization of a difference of convex functions. This formulation does two things at once. First, it turns the problem into one over a finite-dimensional dual matrix, which can be solved with efficient gradient-based methods and avoids the expensive singular value decomposition, even when the feature space is infinite-dimensional. Second, it makes the objective modular: by choosing objectives expressible as Moreau envelopes, the same framework promotes robustness or sparsity without leaving the dual picture. The authors supply the supporting theory, concrete L-BFGS and difference-of-convex algorithms, and the proximal operators needed to make the robust and sparse cases practical.
