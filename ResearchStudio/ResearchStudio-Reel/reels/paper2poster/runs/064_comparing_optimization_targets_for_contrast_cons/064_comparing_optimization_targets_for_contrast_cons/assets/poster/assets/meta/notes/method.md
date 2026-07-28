# Method

Core claim: The authors decompose CCS behavior into two quantities along a unit weight direction θ̂: σ_d² (mean-square separation of contrast-pair displacement vectors u_i = φ⁺_i − φ⁻_i) and σ_m² (mean-square value of contrast-pair midpoints v_i = φ⁺_i + φ⁻_i). They argue CCS's double-saturating sigmoid forces a trade-off — maximizing σ_d² while minimizing σ_m² — so CCS implicitly optimizes a balance of the two. The proposed Midpoint-Displacement (MD) loss makes this trade-off explicit through a single hyper-parameter λ. Two variants are studied: MD-CCS (λ chosen to mimic CCS) and MD-Acc (λ tuned for accuracy).

Supporting detail: Similarity to CCS is measured by cosine similarity between learned weight vectors; accuracy uses ground-truth labels. Probers are compared against MA, SMR, PCA, random, and supervised baselines over four models and five datasets.

Narration: CCS is described by two statistics along the probe direction: sigma-d-squared, how far a statement and its negation are pushed apart, and sigma-m-squared, how far their midpoint sits from origin. Its saturating sigmoid forces a trade-off between the two. Midpoint-Displacement makes this explicit with one knob, lambda, reproducing CCS or maximizing accuracy.
