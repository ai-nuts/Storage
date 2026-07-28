# Contribution

Core claim: CROP is the first unified framework to certify RL robustness at both the per-state action level and the cumulative-reward level, with three concrete algorithms and an evaluation of nine robust RL methods across four environments.

Supporting detail: It contributes a local smoothing algorithm for action certification, a global smoothing algorithm for a reward lower bound, and a novel adaptive local-smoothing search (CROP-LoRe) for tighter reward certificates, plus a public leaderboard.

Narration: CROP makes three main contributions. First, it defines two certification criteria for reinforcement learning: robustness of the per-state action, and a lower bound on the cumulative reward. Second, it turns each criterion into an algorithm. CROP-LoAct uses local randomized smoothing to certify a radius around each state within which the chosen action cannot change. CROP-GRe uses global smoothing to bound the expected and percentile reward, and CROP-LoRe performs an adaptive tree search to produce a much tighter absolute lower bound on reward. Third, the authors apply these tools to nine existing robust RL algorithms across four environments, and release the results as an open leaderboard for the community.
