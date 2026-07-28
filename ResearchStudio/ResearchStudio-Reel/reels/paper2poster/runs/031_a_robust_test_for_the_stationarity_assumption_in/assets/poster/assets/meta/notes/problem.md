# Problem

Core claim: Most RL algorithms assume a stationary MDP with time-invariant transition and reward functions, but real offline systems drift over time, so policies learned under stationarity become suboptimal or harmful.

Supporting detail: Detecting whether and where the dynamics change is essential before trusting any learned policy, yet valid inference is hard in high-dimensional, complex environments.

Narration: Reinforcement learning agents are trained to find the optimal policy, but nearly every algorithm leans on one fragile assumption: that the environment never changes. This is the stationarity assumption, requiring the state transition and reward functions to stay fixed over time. In the real world, that rarely holds. Robotics, healthcare, and digital marketing all drift over long horizons, and a policy learned as if the world were frozen quietly becomes suboptimal, sometimes even harmful. The problem this paper tackles is how to reliably tell whether an offline decision-making system is actually stationary before you trust the policy it produced.
