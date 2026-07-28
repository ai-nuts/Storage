# Key Result

Core claim: For a majority of nodes, common threat models include many perturbed graphs that violate unchanged semantics, and every assessed GNN (GCN, SGC, APPNP, GAT, GATv2, GraphSAGE) shows over-robustness, robustness beyond the point of semantic change.

Supporting detail: For K = 1.0 with the B_deg+2 threat model, 99.4% of target nodes admit a perturbed graph with changed semantic content; an MLP shows 43% over-robustness at K = 0.1 under ℓ₂-weak, and all GNNs sit close to this upper bound.

Narration: The findings are striking. For a majority of nodes, the standard perturbation sets are full of graphs whose true label has already changed. For example, at K equal to one and a per-node degree-plus-two budget, ninety-nine-point-four percent of target nodes have a perturbed graph with changed semantics. And every graph neural network tested shows over-robustness. A perfectly robust reference like an MLP exhibits forty-three percent over-robustness at K equal to zero-point-one under the weak ℓ₂ attack, meaning forty-three percent of its measured adversarial robustness is actually undesirable robustness beyond semantic change, and all the GNNs cluster close to that upper bound.
