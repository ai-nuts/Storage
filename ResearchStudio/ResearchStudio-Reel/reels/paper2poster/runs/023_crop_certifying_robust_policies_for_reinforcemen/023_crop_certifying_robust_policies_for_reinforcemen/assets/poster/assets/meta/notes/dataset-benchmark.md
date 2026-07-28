# Dataset / Benchmark

Core claim: CROP is evaluated on four environments: two high-dimensional Atari games (Pong and Freeway), the low-dimensional CartPole control task, and an autonomous-driving Highway environment.

Supporting detail: Nine RL methods are certified: StdTrain, GaussAug, AdvTrain, SA-MDP (PGD), SA-MDP (CVX), RadialRL, CARRL, NoisyNet, and GradDQN.

Narration: To test the framework broadly, the authors run it on four environments spanning very different regimes. Pong and Freeway are high-dimensional Atari games; CartPole is a classic low-dimensional control task; and Highway simulates autonomous driving. On these, they certify nine existing reinforcement learning methods, ranging from standard training and Gaussian augmentation to adversarial training, the SA-MDP variants, RadialRL, CARRL, NoisyNet, and gradient-based DQN. This makes CROP not just a single certificate but a benchmark that places many robust RL methods on a common, provable footing.
