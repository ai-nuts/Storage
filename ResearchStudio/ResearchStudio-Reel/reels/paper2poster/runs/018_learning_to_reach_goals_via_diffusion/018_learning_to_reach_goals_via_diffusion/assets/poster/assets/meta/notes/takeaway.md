# Takeaway

Core claim: Reframing goal-conditioned reinforcement learning as reverse diffusion turns goal-reaching into simple, value-free behavior cloning that matches or beats state-of-the-art methods while being far more computationally efficient.

Supporting detail: Performing diffusion in the state space with a single denoising step per environment step makes diffusion for reinforcement learning both simple and scalable.

Narration: The big takeaway is that goal-conditioned reinforcement learning can be reframed as the reverse of a diffusion process, and that this reframing makes the problem remarkably simple. By constructing trajectories that walk away from goals and learning to reverse them, Merlin reduces goal-reaching to plain behavior cloning, with no value function to estimate and no instability to fight. It matches or beats state-of-the-art methods across ten tasks, yet runs an order of magnitude faster than other diffusion-based approaches. This suggests that diffusion in the state space is a simple, scalable, and practical new direction for sequential decision making.
