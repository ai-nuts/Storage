# Takeaway

Core claim: CROP shows that functional smoothing can give reinforcement learning policies provable robustness certificates, at both the per-state action and cumulative-reward levels, and those certificates are often tight.

Supporting detail: It establishes a common, provable benchmark for robust RL and an open leaderboard for future methods and environments.

Narration: The lasting message of CROP is that robustness in reinforcement learning need not be a matter of hope. By smoothing the value function, you can prove that an agent's action stays fixed within a certified radius, and you can prove a lower bound on the reward it will collect under any bounded attack. Applied to nine methods across four environments, these certificates are not only correct but often tight, matching what attacks achieve. CROP turns robust RL into something you can measure and compare on a common, provable leaderboard, and invites the community to certify more methods and more environments in future work.
