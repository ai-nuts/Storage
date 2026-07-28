# Motivation

Core claim: The Neural Tangent Kernel has explained training and generalization for many neural architectures in the infinite-width limit, but had never been derived for tree models, leaving soft-tree behavior theoretically opaque.

Supporting detail: Every architecture induces its own distinct NTK; deriving the tree-specific kernel is the missing piece needed to analyze infinite soft-tree ensembles.

Narration: The Neural Tangent Kernel has become a powerful tool for understanding neural networks with infinitely many hidden nodes. It has been derived for multi-layer perceptrons, convolutional networks, and more, each yielding its own distinct kernel. But no one had derived an NTK for tree ensembles. Because soft trees inherit characteristics of neural networks, the authors saw the NTK framework as the natural lens, seeking a closed-form kernel for infinitely many soft trees.
