# Ablation Study

Core claim: Enforcing an input topological ordering (Section 2.3 variant) reduces the search space and solve time relative to the unrestricted formulation. The per-node interval budget is fixed at Cv = 2 (C = 2) throughout the experiments.

Supporting detail: Table 1 contrasts formulation complexity: Checkmate-MILP uses O(n² + nm) Boolean variables, whereas Moccasin-CP uses O(Cn) integer variables with domain size O(n) and O(Cm) constraints.

Narration: The paper studies a few key knobs. The most important is the optional topological-ordering restriction: enforcing an input ordering enlarges the variable domain slightly but shrinks the overall search space, reducing solve time compared to the fully unrestricted formulation. The per-node interval budget, called C, is fixed at two throughout the experiments, which the authors note in every plot legend. The complexity table makes the contrast concrete: Checkmate's Boolean variable count grows quadratically in the number of nodes plus a node-edge term, while Moccasin's integer variable count grows only linearly in the number of nodes, with a constant factor C.
