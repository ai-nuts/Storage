# Key Result

Core claim: The theory holds empirically: the finite-ensemble kernel converges to the closed-form TNTK as trees increase, training dynamics match the kernel-regression prediction, and deep trees show the predicted degeneracy (accuracy first rises then falls with depth). On the 90 datasets the TNTK beats the MLP-induced NTK on more than 30% of them and is much faster to compute.

Supporting detail: Harder decision functions (α > 0.5) consistently outperform the near-linear sigmoid case (α = 0.5), matching the theory that hardness makes the kernel nonlinear.

Narration: The experiments confirm every prediction. As the number of trees grows, the empirical kernel converges to the closed-form Tree NTK, and training dynamics match kernel regression. Making trees deeper first improves then hurts accuracy, exactly the predicted degeneracy. On the ninety datasets the multi-layer perceptron kernel wins on average, but the tree kernel is better on more than thirty percent of them, where the tree inductive bias fits. And because its cost never grows with depth, it is far faster to compute.
