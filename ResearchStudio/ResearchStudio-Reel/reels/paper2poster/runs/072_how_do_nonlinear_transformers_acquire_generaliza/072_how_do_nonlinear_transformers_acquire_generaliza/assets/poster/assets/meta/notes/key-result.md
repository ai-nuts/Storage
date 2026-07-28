# Key Result

Core claim: With T = Θ(η⁻¹M₁α^(−2/3)β^(−2/3)√(log M₁)) iterations and N = BT samples, the trained one-layer Transformer provably reaches O(ε) in-domain generalization error, and also O(ε) out-of-domain error when the shifted relevant patterns are linear combinations (coefficient sum ≥ 1) of the training patterns.

Supporting detail: Experimentally, out-of-domain classification error drops below 0.01 once S₁ ≥ 1 (verifying the linear-combination condition), and required iterations and context length scale as predicted with α.

Narration: The main theorem shows that a number of iterations, and a matching number of samples, that grow only polynomially in the problem parameters is enough to drive the in-domain generalization error down to order epsilon. Crucially, the same trained model also generalizes out of domain to shifted tasks, as long as the new relevant patterns are linear combinations of the training patterns with coefficients summing to at least one. The experiments confirm this sharply: the out-of-domain classification error falls below one percent exactly when the combination strength S-one reaches one, and stays near zero above it, while the required context length and iterations track the predicted dependence on alpha.
