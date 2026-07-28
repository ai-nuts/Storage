# Contribution

Core claim: The paper introduces Inverse Transition Learning (ITL): a gradient-free, constraint-based approach that turns a near-optimal expert policy into constraints on T, then clips a Bayesian posterior over T so every sampled dynamics yields a safe, high-performing policy.

Supporting detail: It also delivers a comprehensive analysis of when and why MLE of T fails under uneven coverage, and shows how coupling constraints with uncertainty produces an informative ranking of actions in uncertain states.

Narration: This work introduces Inverse Transition Learning, a gradient free and constraint based approach. It converts a near optimal expert policy into a set of constraints on the transition dynamics, and then clips a Bayesian posterior over the dynamics so that every sampled model yields a safe and high performing policy. Beyond the method itself, the paper carefully analyzes when and why maximum likelihood estimation of the dynamics breaks down under uneven data coverage, and it shows how combining the constraints with uncertainty produces an informative ranking of actions in the states where the expert is unsure.
