# Ablation Study

Core claim: Comparing the relaxed LP against the exact integer BQCLP (feasible only for small ρ ≤ 12) shows Collective-LP2 loses only about 5% certified ratio from the relaxation, explaining its slight under-performance versus sample-wise at very small ρ.

Supporting detail: Runtime comparison (Figure 4) shows Collective-LP1 scales super-linearly to over 1000 s at large ρ, whereas Collective-LP2 stays near 1 minute; clean-accuracy vs certified-ratio trade-off (Figure 3) confirms LP2 dominates LP1 at equal clean accuracy.

Narration: How much does the linear relaxation cost us? To find out, the authors compare the relaxed program against the exact integer program, which is only tractable for very small budgets. The gap is small: the customized relaxation loses only about five percent in certified ratio, which also explains why the collective approach can trail sample-wise at very tiny budgets. On runtime, the standard relaxation blows up past a thousand seconds as the attack grows, while the customized version stays near a single minute, and at equal clean accuracy it dominates the standard version on the accuracy-versus-certification trade-off.
