# Takeaway

Core claim: By learning a task-specific, differentiable permutation that lines up all graph nodes in a row, CoCN brings standard CNN-style diagonal convolution and hierarchical pooling to graphs and achieves state-of-the-art node and graph classification.

Supporting detail: The permutation is provably convergent and permutation invariant, and its O(n²) cost makes CNN-on-graphs practical at scale.

Narration: The takeaway is elegant. Learn a differentiable permutation that arranges a graph's nodes into a single row, and all the machinery of image convolution becomes available for graphs. CoCN does exactly this, provably convergent and invariant, reaching state-of-the-art results. Graphs, all in a row, can be convolved like images.
