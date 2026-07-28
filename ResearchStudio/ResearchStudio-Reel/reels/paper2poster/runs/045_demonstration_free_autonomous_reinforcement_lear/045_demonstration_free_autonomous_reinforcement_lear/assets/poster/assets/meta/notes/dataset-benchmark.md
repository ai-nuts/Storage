# Dataset / Benchmark

Core claim: IBC is evaluated on six sparse-reward environments: Tabletop Manipulation and Sawyer Door from the established EARL autonomous-RL benchmark, plus four MuJoCo-based OpenAI Gym environments modified for the ARL setting, Fetch Pick&Place, Fetch Push, Fetch Reach, and Point-U-Maze.

Supporting detail: These cover a mixture of robotic manipulation and locomotion tasks; evaluation follows the EARL protocol, reporting the deployed-policy evaluation return in 10k-step intervals with occasional resets only after hundreds of thousands of steps, averaged over 5 seeds.

Narration: To test IBC, the authors assembled six sparse-reward environments spanning both manipulation and locomotion. Two of them, Tabletop Manipulation and Sawyer Door, come from EARL, an established benchmark for autonomous reinforcement learning. The other four are Fetch Pick and Place, Fetch Push, Fetch Reach, and Point-U-Maze, which are standard MuJoCo-based OpenAI Gym tasks that the authors modified for the reset-free, non-episodic setting. Evaluation follows the EARL protocol: the agent is spawned once, interacts continually, and is reset only rarely, after hundreds of thousands of steps. Performance is measured as the deployed policy evaluation metric, reported at ten-thousand-step intervals and averaged across five random seeds.
