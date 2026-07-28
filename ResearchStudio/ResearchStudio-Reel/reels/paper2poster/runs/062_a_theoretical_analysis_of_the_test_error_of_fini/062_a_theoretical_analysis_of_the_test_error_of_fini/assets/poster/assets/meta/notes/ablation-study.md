# Ablation Study

Core claim: The analysis is decomposed to show each term's role: the finite-rank error term γ̃>M² is the irreducible floor that never vanishes with more data; the residue terms proportional to ‖f̃‖² and the C₁, C₂ constants decay like √(log N / N) and are negligible for large N. Figure 3 shows that dropping these residue terms makes the simplified bounds fail to bracket the error only for small N.

Supporting detail: Varying the ridge (Figure 2, right) shows the new bound improves monotonically as 1/λ grows (ridgeless direction), whereas Bach's bound degrades, isolating the ridge-dependence as the main source of the improvement.

Narration: The paper ablates its bound. The finite-rank error is an irreducible floor, while residue terms shrink at a log-N-over-N rate and vanish for large samples. Dropped, the simplified bounds fail only in the small-sample regime, as predicted. A ridge sweep shows the new bound improves toward the ridgeless limit while the prior worsens.
