# Motivation

Core claim: Users who generate offline trajectories (e.g. clinicians) are usually near-optimal, so their demonstrations carry information about which actions are good that a plain MLE of T completely ignores.

Supporting detail: Prior gradient-based inverse RL methods estimate an expert's belief of the dynamics but never relate the estimated T to the true T, and they inherit the instabilities of gradient optimization in tabular MDPs.

Narration: The key insight is that the people who generate this offline data, such as clinicians, are usually acting near optimally. Their choices quietly encode which actions are good and which are bad, yet a plain maximum likelihood fit of the dynamics throws that information away. Earlier gradient based inverse reinforcement learning methods try to recover an expert's belief about the dynamics, but they never connect their estimate back to the true environment and they suffer from the fragility of gradient optimization. We want to exploit the expert signal directly and without gradients.
