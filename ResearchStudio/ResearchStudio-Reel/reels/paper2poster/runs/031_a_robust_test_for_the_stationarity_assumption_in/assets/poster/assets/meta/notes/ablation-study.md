# Ablation Study

Core claim: Varying model misspecification level λ ∈ {0.1,0.3,0.5,0.7,0.9} over 500 replications shows size stays at the nominal level whenever at least one of the two nuisance models is correct — a direct demonstration of the double robustness property.

Supporting detail: Sweeping κ (the tested interval length) locates the single change point; correct type-I control persists across all κ ≤ 25 (null true) and power rises for κ > 25 (alternative true).

Narration: The most informative ablation varies the model misspecification level from mild to severe, across five hundred replications. It shows the empirical size staying pinned at the nominal level whenever at least one of the two nuisance models remains correctly specified, a clean demonstration of the double robustness property. A second sweep varies kappa, the length of the tested interval, to actually locate the single change point: the test correctly holds its size while the null is true and its power climbs once the interval crosses the true change point at twenty-five.
