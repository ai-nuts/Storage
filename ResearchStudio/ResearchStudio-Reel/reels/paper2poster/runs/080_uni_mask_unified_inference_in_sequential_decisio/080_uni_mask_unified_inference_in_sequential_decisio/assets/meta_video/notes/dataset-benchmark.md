# Dataset / Benchmark

Core claim: Two environments: a MiniGrid gridworld navigating to a goal behind a locked door, and the MuJoCo-physics Maze2D (D4RL) continuous-control maze.

Supporting detail: MiniGrid data is used for the qualitative and validation-loss task comparisons; Maze2D reports reward from 1000 rollouts across 5 seeds against feedforward, Decision Transformer, and Decision-GPT baselines at context lengths 5 and 10.

Narration: The framework is evaluated on two environments. The first is MiniGrid, a gridworld where an agent must reach a fixed goal behind a locked door; it is used to qualitatively demonstrate the many inference tasks a single model can perform and to compare task-specific validation losses. The second is Maze2D, a continuous-control maze from the MuJoCo-based D4RL benchmark, where the authors measure test-time reward over one thousand rollouts across five seeds, comparing Uni-MASK against a feedforward network, Decision Transformer, and their own improved Decision-GPT baseline at context lengths of five and ten.
