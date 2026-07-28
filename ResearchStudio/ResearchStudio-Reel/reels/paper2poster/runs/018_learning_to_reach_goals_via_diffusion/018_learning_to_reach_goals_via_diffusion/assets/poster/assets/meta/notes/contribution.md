# Contribution

Core claim: The paper introduces Merlin, a goal-conditioned reinforcement learning method that frames goal-reaching as reverse diffusion in the state space and learns the reverse policy purely by goal-conditioned behavior cloning, with no separate value function.

Supporting detail: Merlin is the first method to perform diffusion directly in the state space, requiring only one denoising iteration per environment step, and comes in three variants: a base version, a parametric forward model (Merlin-P), and a non-parametric forward model with trajectory stitching (Merlin-NP).

Narration: The paper makes three main contributions. First, it presents Merlin, a fresh perspective that casts goal-conditioned reinforcement learning as a reverse diffusion process operating directly over the state space of the environment. Second, it proves that this reverse process can be learned by simple goal-conditioned behavior cloning with hindsight relabeling, eliminating the need for a value function entirely. Third, it develops three ways to construct the forward, goal-departing trajectories: a fixed heuristic version, a parametric learned forward model called Merlin-P, and a non-parametric version called Merlin-NP that stitches together nearby states in a learned latent space.
