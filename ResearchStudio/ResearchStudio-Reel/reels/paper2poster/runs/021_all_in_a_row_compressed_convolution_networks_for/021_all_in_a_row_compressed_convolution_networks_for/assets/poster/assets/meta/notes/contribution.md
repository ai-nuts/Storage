# Contribution

Core claim: The paper introduces a differentiable graph-regularization method that applies learnable permutations to constrain all nodes into a row with permutation invariance, and builds Compressed Convolution Network (CoCN), which applies CNN-style diagonal convolution and pooling for end-to-end hierarchical graph representation learning.

Supporting detail: CoCN is validated across node and graph classification benchmarks, beating competitive convolutional GNNs and graph-pooling models while cutting permutation-modeling cost from O(n!) to O(n²).

Narration: The paper makes two contributions. First, a differentiable regularization for graphs: a learnable permutation that lines nodes into a single row while preserving permutation invariance, so Euclidean convolution finally applies. Second, the model built on it, the Compressed Convolution Network, or CoCN. It learns both node and structure features and trains end to end, beating competitive GNNs and pooling models.
