# Ablation Study

Core claim: Adding higher-degree hyperedges barely changes the lower bound at small ε: L(2), L(3), and L*(4) nearly coincide until loss exceeds ~0.4, despite millions of higher-degree hyperedges being present.

Supporting detail: For CIFAR-10 at ε=3 there are about 3 million degree-3 and 10 million degree-4 hyperedges, yet they leave the computed bound unchanged; aggregating binary bounds (L*_CO(2)) is cheapest but much looser; larger architectures help only slightly at low ε and not at all at high ε.

Narration: A key ablation examines how much the higher-order hyperedges actually matter. Surprisingly, at small perturbation budgets the lower bound computed with only edges is nearly identical to bounds that add degree-three and degree-four hyperedges, even though the graph contains millions of these higher-order structures. For CIFAR-10 at budget three, there are roughly three million degree-three and ten million degree-four hyperedges, yet they have no impact on the computed bound. This means edge-only bounds are both cheap and accurate in the practical regime. The aggregated binary bound is the fastest to compute but much looser, and scaling up model architecture yields only minor gains at low budgets.
