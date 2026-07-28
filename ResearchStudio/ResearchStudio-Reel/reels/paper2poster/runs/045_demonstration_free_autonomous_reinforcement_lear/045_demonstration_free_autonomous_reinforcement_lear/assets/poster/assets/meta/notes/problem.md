# Problem

Core claim: Reinforcement learning assumes cheap resets to a fixed initial state after each episode, but real-world autonomous agents cannot reset on demand, so learning must proceed from continual, non-episodic interaction.

Supporting detail: Existing autonomous RL (ARL) methods lean on prior data such as expert or sub-optimal demonstrations and fail when task-relevant interactions are sparse and unlikely to occur by chance.

Narration: Standard reinforcement learning quietly assumes something that rarely holds outside a simulator: that at the end of every episode, the environment magically resets to its starting state. For a physical robot, resetting means human intervention, scripted reset policies, or custom rigs, all of which are slow and costly. Autonomous reinforcement learning tries to remove that assumption by learning from one long uninterrupted stream of experience. But the existing autonomous methods cheat in a different way: they rely on prior data, like expert demonstrations or example states of interest, and they struggle badly in environments where the interactions that matter are sparse and almost never happen by chance. What has been missing is an agent that learns truly from scratch, with no resets and no demonstrations.
