# Headline Numbers

Core claim: - 0.73 DDT success rate under Unforeseen Obstacles (best baseline 0.57) - -15% DDT degradation from Train to Unforeseen Obstacle vs -20% / -33% / -52% for baselines - 0.61 DDT success on unseen Meta-World demos with disturbance (baselines ≤0.12) - ~2× performance gain when scaling up model parameters; log-linear scaling with data and parameters

Supporting detail: On mixed-up demonstrations DDT reaches 0.84 / 0.88 / 0.90 unseen-demo success across 2 / 4 / 8 environments; a single demonstration (|T_ω| = 1) suffices under the Ω-recoverable condition.

Narration: A few numbers capture the impact. Under unforeseen obstacles, DDT succeeds seventy-three percent of the time, compared to fifty-seven percent for the best baseline. Its performance degradation from training to unforeseen obstacles is just fifteen percent, at least five percent better retention than any competitor. On disturbed Meta-World tasks it reaches sixty-one percent on unseen demonstrations while baselines stay at or below twelve percent. And when scaled up, DDT improves roughly two-fold with more model parameters and shows a clean log-linear gain with both data volume and model size, hinting at its promise as a backbone for generalist agents.
