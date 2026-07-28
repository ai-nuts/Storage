# Problem

Core claim: Offline goal-conditioned reinforcement learning must train agents to reach arbitrary goals from fixed datasets under sparse binary rewards, but most methods depend on a learned value function that becomes unreliable in this setting.

Supporting detail: Out-of-distribution actions generated during training corrupt value estimates, and these errors compound over time and can cause the policy to diverge.

Narration: Goal-conditioned reinforcement learning aims to train a single agent that can reach any target state within an environment, using only a sparse reward of one when the goal is reached and zero otherwise. In the offline setting, the agent must learn purely from a pre-collected dataset, without any further interaction. The trouble is that most methods rely on estimating a value function, and in the offline goal-conditioned setting this estimate is fragile. Policies generate actions not present in the data, the value estimates for those actions are wrong, and these errors compound over time until the policy diverges. Sparse binary rewards only make the estimation problem harder.
