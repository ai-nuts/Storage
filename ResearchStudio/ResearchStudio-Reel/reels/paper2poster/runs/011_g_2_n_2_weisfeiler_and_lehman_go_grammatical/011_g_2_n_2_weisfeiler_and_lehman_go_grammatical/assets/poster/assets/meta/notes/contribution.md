# Contribution

Core claim: (i) A generic framework that produces a GNN from any fragment of an algebraic language via context-free grammars; (ii) an instantiation on ML(L3) yielding G2N2, a provably 3-WL GNN; (iii) experimental validation of the grammar reduction / rule set; (iv) extensive experiments showing G2N2 outperforms existing 3-WL GNNs across regression, classification, and spectral tasks.

Supporting detail: The grammar-reduction step both preserves 3-WL expressiveness and exposes which operations matter, enabling informed pruning of the model.

Narration: The paper makes four contributions. First, a generic framework that turns any fragment of an algebraic language into a graph neural network through context-free grammars. Second, it runs that framework on the ML-of-L-three fragment and out comes G2N2, a network that is provably 3-W-L. Third, it validates the rule set experimentally, showing that the grammar reduction keeps expressiveness while trimming redundancy. And fourth, across a broad battery of downstream tasks, G2N2 beats the existing 3-W-L networks, often while running faster.
