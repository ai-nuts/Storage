# Contribution

Core claim: The paper introduces automatic clipping (AUTO-V and AUTO-S) that removes the clipping threshold from any DP optimizer, gives a non-convex convergence theorem matching standard SGD, and demonstrates state-of-the-art results on vision and language tasks with a one-line code change.

Supporting detail: It shows any constant R is equivalent to R=1, sets a default stability constant gamma=0.01, and integrates into existing libraries (Opacus, ObJAX) by replacing Abadi's clipping.

Narration: The authors make four contributions. First, they propose automatic clipping, which mathematically expunges the clipping threshold from general DP optimizers including DP-SGD, DP-Adam, and DP-LAMB. Second, they prove that automatic DP-SGD converges in the non-convex setting at the same asymptotic rate as standard SGD. Third, they show any positive constant threshold is equivalent to setting it to one, so a single default suffices. And fourth, they demonstrate superior results across vision and language benchmarks, achievable by changing a single line of code in popular libraries.
