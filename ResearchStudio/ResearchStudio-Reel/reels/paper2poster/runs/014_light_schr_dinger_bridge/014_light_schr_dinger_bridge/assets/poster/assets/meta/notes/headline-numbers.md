# Headline Numbers

Core claim: - Convergence in under 1 minute on 4 CPU cores (no GPU) for 512-dim latent image translation. - MSCI DIM=1000: energy distance 1.27 in 146 s on 4 CPUs vs 1.32 in 71 min on a V100 GPU (Minimax solver). - EOT/SB benchmark: cBW²₂-UVP as low as 0.03–0.62% for LightSB vs 1.04–18.05% for the best baseline. - Universal approximator of SBs (first such result) with generalization error vanishing at the parametric rate.

Supporting detail: Training each MSCI setup takes 65–146 s on CPU across DIM=50/100/1000, versus 8–71 min for GPU baselines.

Narration: A few numbers capture the impact. LightSB converges in under one minute on four CPU cores for the five-hundred-twelve-dimensional image translation task, with no GPU at all. On the hardest single-cell setting, one thousand dimensions, it reaches an energy distance of one point two seven in one hundred forty-six seconds on CPU, matching a minimax GPU solver that needs seventy-one minutes on a V100. On the entropic transport benchmark, its conditional error drops to as little as three hundredths of a percent, against best-baseline errors ranging from about one to eighteen percent. And all of this comes with a theoretical guarantee: LightSB is a universal approximator of Schrödinger Bridges, with generalization error that vanishes at the standard parametric rate.
