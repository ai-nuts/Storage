# Problem

Core claim: Convolutional GNNs built on graph polynomials are weakly expressive under limited parameters and cannot perform hierarchical representation learning without extra node clustering or node-drop pooling.

Supporting detail: Euclidean CNNs escape both limits via local feature learning and global parameter sharing, but their convolution cannot be applied to irregular, non-grid graph structures.

Narration: Convolutional graph networks have two weaknesses. Because their filters come from graph polynomials, they lack expressiveness on a small parameter budget. And they cannot learn hierarchical, multi-scale features alone, needing bolt-on tricks like clustering or node dropping. Image CNNs have neither problem: local learning and shared filters naturally capture multi-scale patterns. But their Euclidean convolution assumes a regular grid, and does not fit irregular graphs.
