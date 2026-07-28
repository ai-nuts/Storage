# Problem

Core claim: Goal-conditioned RL usually assumes the agent is handed the exact goal configuration, which is often unrealistic since the precise goal state is unknown before the task is attempted.

Supporting detail: A more scalable interface would let a user provide an example of an analogous task and have the agent infer the corresponding goal for its own current state.

Narration: Goal-conditioned reinforcement learning usually hands the agent the exact goal, as a target image. But in the real world you rarely know the precise goal in advance. Ask a robot to close a drawer, and you may not know how the closed drawer looks. We want to specify tasks by analogy.
