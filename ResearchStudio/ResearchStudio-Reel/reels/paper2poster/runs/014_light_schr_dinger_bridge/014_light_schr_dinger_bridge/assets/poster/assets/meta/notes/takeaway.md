# Takeaway

Core claim: LightSB is a simple, simulation-free, non-minimax Schrödinger Bridge solver, essentially a Gaussian-mixture model for the transport potential, that runs in minutes on a CPU, matches or beats heavy GPU solvers, and is provably a universal approximator, making it a natural default baseline for EOT/SB.

Supporting detail: Its main limitation is that it targets moderate-dimensional distributions and is applied in latent rather than raw image space.

Narration: The lasting message is that a Schrödinger Bridge solver does not have to be heavy. By parameterizing the transport potential as a Gaussian mixture and optimizing a single, straightforward objective, LightSB solves entropic optimal transport and Schrödinger Bridges in minutes on a CPU, without adversarial training or process simulation. It matches or outperforms much heavier GPU-based solvers, comes with a universal-approximation guarantee, and is easy to use. In short, LightSB is positioned to be the simple, reliable baseline that the Schrödinger Bridge field has been missing.
