# Problem

Core claim: In offline RL for healthcare and education, the transition dynamics T must be estimated from fixed batch data, but standard MLE estimates yield high-variance policies that take unsafe actions wherever the data gives poor state-action coverage.

Supporting detail: The number of dynamics parameters grows with the state and action space, and offline settings forbid gathering new data to fill the gaps left by the users who produced the batch.

Narration: In fields like healthcare and education we cannot experiment freely, so offline reinforcement learning must learn the environment's transition dynamics purely from a fixed batch of collected experience. The trouble is that this data only covers the actions the original users actually took, leaving much of the state and action space unseen. Standard maximum likelihood estimates of the dynamics therefore produce policies that swing wildly from dataset to dataset and can recommend genuinely unsafe actions in the regions where data is thin.
