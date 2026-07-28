# Contribution

Core claim: The paper introduces ParaDiGMS, the first diffusion sampling method that trades compute for speed by denoising multiple steps in parallel, and it is complementary to existing fast samplers such as DDIM and DPMSolver.

Supporting detail: ParaDiGMS combines with prior methods to form ParaDDPM, ParaDDIM, and ParaDPMSolver, trading both compute and quality for speed, and works with classifier-free guidance.

Narration: The key contribution is ParaDiGMS, short for Parallel Diffusion Generative Model Sampling. It is the first general method that lets you spend extra parallel compute to sample a pretrained diffusion model faster, without any retraining. Crucially, it is orthogonal to existing techniques, so it can be layered on top of DDIM or DPMSolver to yield ParaDDIM and ParaDPMSolver, combining both axes of speedup. It is also compatible with classifier-free guidance.
