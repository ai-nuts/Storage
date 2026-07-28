# Ablation Study

Core claim: The 2D Gaussian→Swiss-roll study varies ϵ (2·10⁻³, 10⁻², 10⁻¹): small ϵ gives nearly straight, near-deterministic trajectories, while larger ϵ increases trajectory volatility and disperses the conditional distributions π_θ(x₁|x₀), confirming the noise level behaves as expected.

Supporting detail: Across benchmark settings, LightSB's advantage is largest where the data matches its sum-exp Gaussian-mixture inductive bias, and its accuracy holds across dimensions D=2–128 and ϵ=0.1–10.

Narration: To understand the role of the noise parameter epsilon, the authors map a two-dimensional Gaussian to a Swiss roll while sweeping epsilon across three values. When epsilon is small, the learned process is nearly deterministic and its trajectories are almost straight lines. As epsilon grows, the trajectories become more volatile and the conditional distributions at the endpoint spread out. This matches the theory: epsilon controls the stochasticity of the bridge. The benchmark results also reveal that LightSB gains the most when the target distributions align with its Gaussian-mixture inductive bias, while remaining accurate across the tested dimensions and noise levels.
