# Method

Core claim: For additive-noise inverse problems, a score-based diffusion model learns the noise score ∇ₓ log Q(x) via denoising score matching; combined with the Jacobian of a differentiable waveform model M(θ), it yields the likelihood score, which is sampled with a Metropolis-adjusted Langevin algorithm (MALA).

Supporting detail: The forward model uses the differentiable IMRPhenomD waveform from the ripple package, enabling automatic differentiation for the required Jacobian; the score network is trained in the Fourier domain on Tukey-windowed 4 s segments.

Narration: Here is how SLIC works. The setting is an inverse problem with additive noise: an observation equals a deterministic signal model plus noise. Learn the score of the noise distribution and you can build the score of the likelihood. So they train a score-based diffusion model on real LIGO noise using denoising score matching, then chain it with the Jacobian of a differentiable IMRPhenomD waveform from the ripple package. Sampling uses a Metropolis-adjusted Langevin algorithm, MALA.
