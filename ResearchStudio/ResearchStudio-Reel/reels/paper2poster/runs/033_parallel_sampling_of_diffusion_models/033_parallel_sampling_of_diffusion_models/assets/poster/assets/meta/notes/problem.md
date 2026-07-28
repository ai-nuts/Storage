# Problem

Core claim: Diffusion models generate high-quality samples but sample slowly, often requiring up to 1000 sequential denoising steps to produce a single sample.

Supporting detail: Prior accelerators like DDIM and DPMSolver reduce the number of denoising steps, but fewer steps degrades sample quality, trading quality for speed.

Narration: The central limitation of diffusion models is sampling speed. A standard denoising diffusion probabilistic model can take a thousand sequential passes through the neural network to create one sample, which is far too slow for interactive use. The popular fix is to simply use fewer denoising steps, as DDIM and DPMSolver do, but reducing steps comes at the cost of sample quality. The field has largely accepted this quality-for-speed tradeoff.
