# Key Result

Core claim: The gap between adversarially trained classifiers and the optimal loss is large even at small ε, and far larger than in the binary case. For 3-class CIFAR-10, TRADES cannot beat about 0.6 loss at a budget where the optimal loss is near 0.

Supporting detail: In the 10-class setting the truncated-hypergraph lower bounds and the Caro-Wei upper bound match closely at practical ε, tightly localizing the true optimal loss and confirming the AT gap holds against both bounds.

Narration: The headline finding is a large, previously unquantified gap. Adversarially trained classifiers perform far worse than the theoretical optimum, and this gap is much wider than what prior work observed for binary classification. On 3-class CIFAR-10, TRADES adversarial training cannot achieve a loss much better than 0.6 at a perturbation strength where the optimal achievable loss is essentially zero. In the 10-class setting, the efficient lower and upper bounds sandwich the optimal loss tightly for the budgets used in practice, so the gap is not an artifact of loose bounds. This suggests current robust training struggles far more as the number of classes grows.
