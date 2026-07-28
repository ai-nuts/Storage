# Motivation

Core claim: Kernel PCA is naturally a variance-maximization problem under orthonormality constraints, which places it in the well-studied family of difference-of-convex (DC) problems, but prior DC treatments handled only linear PCA or a single component.

Supporting detail: Infimal convolution is known to design robust and sparse losses cleanly in duality settings, suggesting one dual framework could unify these extensions for the nonlinear, multi-component kernel case.

Narration: The authors observe that Kernel PCA can be written as variance maximization under orthonormality constraints, which puts it squarely in the family of difference-of-convex problems that optimization researchers understand well. Earlier work had studied PCA as a difference-of-convex program, but only for linear PCA, and often only for the first component where the orthogonality constraints vanish. Meanwhile, a separate line of research had shown that infimal convolution is an elegant way to build robust or sparse losses, and that these constructions behave especially nicely in dual formulations. Bringing these two observations together is the opening the paper exploits.
