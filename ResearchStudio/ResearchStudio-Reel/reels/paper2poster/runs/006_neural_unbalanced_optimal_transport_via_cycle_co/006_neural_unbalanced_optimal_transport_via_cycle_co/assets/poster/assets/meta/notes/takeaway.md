# Takeaway

Core claim: By recasting unbalanced OT through learnable semi-couplings and training with a cycle-consistent scheme, NubOT jointly predicts where single cells move and how their mass grows or dies, beating prior neural OT methods on drug-response forecasting while staying biologically interpretable.

Supporting detail: Explicitly modeling proliferation and death at single-cell resolution is a step toward faithfully forecasting heterogeneous perturbation responses.

Narration: The takeaway is that unbalanced optimal transport can be made both practical and biologically faithful. By reformulating it through learnable semi-couplings, and training the maps and reweighting functions with a cycle-consistent alternating scheme, NubOT simultaneously predicts the movement and the creation or destruction of mass at the level of individual cells. It outperforms previous neural optimal transport methods on the challenging task of forecasting how cancer cell lines respond to drugs, and it does so while producing predictions that align with known proliferation and death markers. Explicitly modeling cell birth and death, rather than assuming mass is conserved, is what makes this possible.
