# Dataset / Benchmark

Core claim: Evaluated on three D4RL suites (AntMaze v2, Gym Locomotion v2, Franka Kitchen v0) plus the GCSL goal-conditioned suite (FourRooms, Door, Pusher, Lander, Claw), spanning navigation, locomotion, and manipulation.

Supporting detail: D4RL datasets range from random to medium-expert quality; GCSL tasks are adapted for offline RL using random-policy data, and scores are normalized to the [0, 100] range.

Narration: The evaluation is deliberately broad. On the D4RL benchmark, the authors use three suites: AntMaze, which requires an eight-degree-of-freedom quadruped to navigate a maze; Gym Locomotion, with HalfCheetah, Hopper, and Walker across random, medium, medium-replay, and medium-expert datasets; and Franka Kitchen, a nine-degree-of-freedom manipulation task built from human demonstrations. They also use the GCSL suite of goal-conditioned tasks, including two-dimensional navigation, Sawyer arm control, Lunar Lander, and a robotic claw, which they adapt for offline RL by collecting data with a random policy. All scores are normalized into a zero-to-one-hundred range so methods can be compared directly.
