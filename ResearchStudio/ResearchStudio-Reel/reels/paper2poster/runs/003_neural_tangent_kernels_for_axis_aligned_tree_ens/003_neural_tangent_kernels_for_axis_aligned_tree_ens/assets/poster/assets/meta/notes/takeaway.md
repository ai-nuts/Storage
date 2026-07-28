# Takeaway

Core claim: The Tree Neural Tangent Kernel gives the first kernel-theoretic account of infinite soft-tree ensembles, explaining their global convergence, why oblivious trees lose nothing, why deep trees degenerate, and why harder splits help.

Supporting detail: It also offers a depth-free, fast-to-compute kernel that is competitive with, and on many datasets superior to, the MLP-induced NTK.

Narration: The lasting takeaway is that the neural tangent kernel framework, once used only for neural networks, applies to tree models. The resulting Tree NTK explains many soft-tree behaviors from one theory: training converges globally, oblivious sharing costs nothing in the limit, deep trees degenerate into a nearly constant kernel, and harder splits yield a more useful nonlinear kernel. It also delivers a fast kernel whose cost is independent of depth.
