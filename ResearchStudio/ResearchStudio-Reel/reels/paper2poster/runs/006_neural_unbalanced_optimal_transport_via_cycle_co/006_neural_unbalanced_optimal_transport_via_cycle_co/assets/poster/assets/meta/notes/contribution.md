# Contribution

Core claim: NubOT, a neural unbalanced OT formulation that (i) weaves the semi-coupling theory of unbalanced OT with a scalable neural OT map estimator, (ii) parameterizes it via convex dual potentials (ICNNs) plus learned reweighting functions, and (iii) trains it through a novel cycle-consistent alternating scheme that generalizes out-of-sample.

Supporting detail: The formulation recovers interpretable semi-couplings and predicts per-cell mass changes for previously unseen samples.

Narration: The paper makes three main contributions. First, it introduces a novel formulation of the unbalanced optimal transport problem that connects the rigorous theory of semi-couplings, which allow mass to vary, with a practical and scalable optimal-transport mapping estimator. Second, it derives a computationally feasible implementation based on dual potentials parameterized by input convex neural networks, together with learned reweighting functions that predict mass changes. Third, it proposes a new cycle-consistent training procedure that alternates between updating these maps and rescaling functions, and crucially generalizes to new, out-of-sample cells. Together these give the first neural method that estimates semi-couplings for unbalanced OT at single-cell scale.
