# Dataset / Benchmark

Core claim: Continuous control uses MuJoCo locomotion tasks (Walker2d-v4 as the primary testbed, plus Hopper, HalfCheetah, Ant, Humanoid) with behavior cloning from SAC experts over horizon H = 1000. Language experiments use 270M-parameter Transformers trained on the TinyStories dataset.

Supporting detail: Rollout reward is averaged over 20 initial conditions with per-episode rewards shown disaggregated; the BC setting uses N = H = 1000 so overfitting is not the confound.

Narration: The experiments span two very different domains. For continuous control, the authors use classic MuJoCo locomotion tasks, with Walker2d as the primary testbed and Hopper, HalfCheetah, Ant, and Humanoid for breadth. They clone from strong expert policies over a long horizon of a thousand steps, and they deliberately set the dataset size so that overfitting is not the issue. For language, they train two hundred and seventy million parameter Transformers on TinyStories, a small synthetic dataset of simple children's stories that keeps the setup tractable while still exhibiting the phenomenon. Reward is averaged over twenty initial conditions so the oscillations are not just measurement noise.
