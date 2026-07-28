# Motivation

Core claim: Denoising diffusion models offer a value-free way to model a target distribution by learning to reverse a noising process, suggesting goal-reaching can be cast as reversing trajectories that walk away from goal states.

Supporting detail: Prior attempts to stabilize offline learning add policy constraints or conservative value updates, which compromise performance and hurt generalization.

Narration: Diffusion models have become a powerful class of generative models. They work by defining a forward process that gradually destroys data into Gaussian noise, then learning a reverse process that denoises noise back into realistic samples, without ever estimating a value function. The authors ask a simple question: what if we treat goal states as the data distribution we want to model? In a diffusion model, noise walks away from the data manifold; in goal-conditioned reinforcement learning, we can construct trajectories that walk away from potential goals. Learning to reverse those deviations is directly analogous to learning the score function, and it sidesteps the value-estimation problems that plague offline methods.
