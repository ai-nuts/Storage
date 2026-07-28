# Contribution

Core claim: The paper derives sharp non-asymptotic high-probability upper AND lower bounds on the finite-rank KRR test error in the under-parameterized regime (sample size N greater than rank M), valid for any ridge λ. It (i) gives non-vacuous bounds in the ridgeless λ→0 limit, (ii) provides a lower bound that matches the upper bound as N grows, and (iii) validates the improvement empirically.

Supporting detail: A key technical move is analyzing the target in the L²ρ basis {ψk} rather than the RKHS basis, decoupling the spectrum from the sampling randomness to obtain sharper constants.

Narration: The contribution is threefold. First, the bounds improve as the ridge goes to zero. Second, a sharp lower bound matches the upper bound as samples grow, so both are tight. Third, experiments show a large gain over prior work. The key trick: work in the eigenfunction basis, separating spectrum from sampling noise.
