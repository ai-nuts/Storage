# Contribution

Core claim: IGP is the first graph active-learning framework built on relaxed binary queries and soft labels, paired with a new node-selection criterion that explicitly maximizes information-gain propagation across the graph.

Supporting detail: It works on any GNN backbone (SGC, APPNP, GCN, MVGRL) and consistently beats state-of-the-art AL baselines under equal labeling cost.

Narration: The paper makes three contributions. First, a new active-learning paradigm for graph networks that uses relaxed queries and soft labels instead of exact-class annotation. Second, a node-selection criterion that maximizes how information gain propagates through the graph. Third, experiments showing it beats state-of-the-art baselines and generalizes across many graph neural network backbones.
