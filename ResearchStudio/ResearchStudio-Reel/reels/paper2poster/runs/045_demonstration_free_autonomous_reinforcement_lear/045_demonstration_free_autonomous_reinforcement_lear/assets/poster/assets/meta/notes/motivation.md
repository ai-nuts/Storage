# Motivation

Core claim: A truly autonomous agent should learn from scratch without external interventions or prior data, yet naive RL fails in the non-episodic setting because pre-convergence rollouts leave the agent in arbitrary states, causing highly variable initial conditions and unstable learning.

Supporting detail: Prior reset-free methods either still require occasional manual resets, only work where task interactions occur by chance, or (like VaPRL and MEDAL) depend on demonstrations to build subgoal curricula or to define the backward objective.

Narration: Why is demonstration-free autonomous learning so hard? In the non-episodic setting, an untrained forward agent wanders off to arbitrary states, so every new attempt starts from a wildly different, often useless initial condition. That instability makes learning collapse. Prior work patched this in ways that reintroduce human effort. Some methods still ask for occasional manual resets. Others only succeed when the useful interactions happen to occur by chance. And the two most directly comparable methods, VaPRL and MEDAL, both lean on demonstration data, either to seed a subgoal curriculum or to define what the backward agent should return to. The motivation here is to build an agent that provides its own anchor and its own curriculum, using nothing but the experience it collects.
