# Problem

Core claim: Classical Kernel PCA solves an n×n singular value decomposition of the Gram matrix, an O(n³) operation that is prohibitively slow and blocks large-scale use.

Supporting detail: Adding desirable properties like robustness to outliers or sparsity has long required ad-hoc, per-property reformulations and heuristics, with no unifying framework.

Narration: Kernel PCA is one of the most widely used tools in unsupervised learning, but it has a stubborn scaling problem. The standard recipe computes the singular value decomposition of the n-by-n Gram matrix, which costs order n-cubed and becomes painfully slow even for moderately sized datasets. On top of that, every time researchers wanted a robust or a sparse variant of Kernel PCA, they reached for a different ad-hoc formulation or weighting heuristic, producing a scattered collection of unrelated optimization problems rather than one coherent method.
