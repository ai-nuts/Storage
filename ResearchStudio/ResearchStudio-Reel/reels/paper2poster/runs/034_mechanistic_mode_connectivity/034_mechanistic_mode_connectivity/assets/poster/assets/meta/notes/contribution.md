# Contribution

Core claim: The paper (1) defines mechanistic similarity via shared invariances to interventions on the data-generating process; (2) proves that lack of linear connectivity implies mechanistic dissimilarity; and (3) introduces Connectivity-Based Fine-Tuning (CBFT) to deliberately alter a model's mechanisms.

Supporting detail: It also contributes synthetic cue-augmented benchmarks (CIFAR-10, CIFAR-100, Dominoes) with counterfactual test sets for measuring mechanism reliance.

Narration: The paper makes three main contributions. First, it defines mechanistic similarity: two models are mechanistically similar if they are invariant to the same set of unit interventions on the data-generating process. Second, it characterizes connectivity, proving that if two models lack linear connectivity up to architectural symmetries, they must be mechanistically dissimilar. Third, motivated by this result, it proposes Connectivity-Based Fine-Tuning, a method that exploits loss barriers to steer a model toward the mechanisms we actually want.
