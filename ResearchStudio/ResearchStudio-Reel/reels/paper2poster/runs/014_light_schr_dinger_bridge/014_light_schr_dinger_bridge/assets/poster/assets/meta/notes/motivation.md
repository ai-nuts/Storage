# Motivation

Core claim: A user who just wants EOT/SB between moderate-dimensional distributions is forced into heavy neural solvers with min-max objectives, process simulation during training, and hours of GPU time plus fragile hyperparameter tuning.

Supporting detail: In most real applications only the endpoints of the trajectories matter, so a solver that returns the conditional plan directly and cheaply would already cover the dominant use case.

Narration: Consider a researcher who simply wants to compute an entropic optimal transport or Schrödinger Bridge between two moderate-dimensional datasets. Today, that means adopting a solver with iterative proportional fitting steps, or min-max optimization, or simulation of the full stochastic process at every training step. These solvers demand careful neural network design, run for hours on GPUs, and are sensitive to many hyperparameters. Yet in many real settings, the user only cares about where the trajectories end, that is, the conditional plan. This mismatch, heavy machinery for a modest goal, is exactly the gap LightSB is built to close.
