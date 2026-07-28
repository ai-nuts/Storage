# Problem

Core claim: Sequential decision problems are usually solved one task at a time, with a separate model trained for behavior cloning, offline RL, dynamics prediction, or goal conditioning, despite their shared structure.

Supporting detail: This siloing wastes the fact that all these inferences operate over the same trajectory of states, actions, and returns and could share representations.

Narration: In sequential decision making, tasks like behavior cloning, offline reinforcement learning, inverse dynamics, and goal or waypoint conditioning are typically each handled by a separate, specially trained model. Yet all of these tasks operate over the very same object: a trajectory of states, actions, and returns. Training a distinct model per task ignores this shared structure and misses the chance to build richer, reusable representations across tasks.
