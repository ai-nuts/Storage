---
title: Parallel Sampling of Diffusion Models
authors: Andy Shih¹, Suneel Belkhale¹, Stefano Ermon¹, Dorsa Sadigh¹, Nima Anari¹
institutes: ¹Stanford University
venue: NeurIPS 2023
paper_url: https://arxiv.org/abs/2305.16317
code_url: https://github.com/AndyShih12/paradigms
title_audio_script: Diffusion models produce stunning samples, but they are slow, often needing a thousand sequential denoising steps to generate a single sample. This paper from Stanford asks a different question than most prior work. Instead of cutting the number of steps and paying with sample quality, can we keep every step but run them in parallel, trading extra compute for lower latency? The answer is a method called ParaDiGMS, which uses Picard iterations to guess the whole denoising trajectory and refine it in parallel until it converges. It delivers two-to-four times faster sampling with no measurable drop in quality.
---

## Problem
**Necessary:** Diffusion models generate high-quality samples but sample slowly, often requiring up to 1000 sequential denoising steps to produce a single sample.
**Additional:** Prior accelerators like DDIM and DPMSolver reduce the number of denoising steps, but fewer steps degrades sample quality, trading quality for speed.
**Audio script:** The central limitation of diffusion models is sampling speed. A standard denoising diffusion probabilistic model can take a thousand sequential passes through the neural network to create one sample, which is far too slow for interactive use. The popular fix is to simply use fewer denoising steps, as DDIM and DPMSolver do, but reducing steps comes at the cost of sample quality. The field has largely accepted this quality-for-speed tradeoff.

## Motivation
**Necessary:** Rather than trading quality for speed by reducing steps, the authors ask whether additional parallel compute can perform the same number of denoising steps in less wall-clock time.
**Additional:** Sampling latency, not throughput, is the bottleneck; naive parallelism only raises throughput because denoising proceeds sequentially, so cutting single-sample latency looks hard.
**Audio script:** The authors pursue an orthogonal direction. Instead of trading quality for speed, they ask whether we can trade compute for speed. The goal is to lower the latency of generating a single sample, not just the throughput of generating many. At first this seems impossible, because denoising is inherently sequential: each step depends on the previous one. Naive parallelization can generate multiple samples at once, but making a single sample appear faster in wall-clock time is a much harder problem.

## Contribution
**Necessary:** The paper introduces ParaDiGMS, the first diffusion sampling method that trades compute for speed by denoising multiple steps in parallel, and it is complementary to existing fast samplers such as DDIM and DPMSolver.
**Additional:** ParaDiGMS combines with prior methods to form ParaDDPM, ParaDDIM, and ParaDPMSolver, trading both compute and quality for speed, and works with classifier-free guidance.
**Audio script:** The key contribution is ParaDiGMS, short for Parallel Diffusion Generative Model Sampling. It is the first general method that lets you spend extra parallel compute to sample a pretrained diffusion model faster, without any retraining. Crucially, it is orthogonal to existing techniques, so it can be layered on top of DDIM or DPMSolver to yield ParaDDIM and ParaDPMSolver, combining both axes of speedup. It is also compatible with classifier-free guidance.

## Method
**Necessary:** ParaDiGMS reframes denoising as solving an ODE by Picard iteration: it guesses the entire denoising trajectory, then iteratively refines every timestep in parallel until the fixed-point iteration converges, which empirically needs far fewer iterations than there are steps.
**Additional:** To fit GPU memory it processes a sliding batch window of size p, updating each point from the cumulative drift over the window and sliding forward as soon as the leading timesteps converge; for SDEs the noise is sampled up front so the resulting ODE stays Lipschitz.
**Key equation:** `$x_t^{k+1} = x_0^k + \int_0^t s(x_u^k, u)\, du \;\approx\; x_0^k + \tfrac{1}{T}\sum_{i=0}^{t-1} s(x_i^k, i/T)$`
**Audio script:** The method builds on Picard iterations, a classic technique for solving ordinary differential equations by fixed-point iteration. The insight is to write the value at each timestep as the initial value plus the integral of the drift along the path. Starting from a full guess of the trajectory, ParaDiGMS updates every timestep simultaneously using the cumulative drift, and repeats until the values stop changing. Because each iteration can be computed in parallel across timesteps, and the number of iterations to converge is much smaller than the number of steps, the whole trajectory resolves much faster. In practice it uses a sliding window of a fixed size to respect GPU memory, advancing the window as soon as the earliest timesteps converge.

## Dataset / Benchmark
**Necessary:** Evaluation spans robotics policies (Robosuite Square, PushT, FrankaKitchen) and image generation (StableDiffusion-v2 on COCO2017 captions, and pixel-space LSUN Church/Bedroom).
**Additional:** Robotics tasks use DiffusionPolicy models measured by task reward over 200 episodes; image models are measured by CLIP score on ViT-g-14 and FID on 5000 samples.
**Audio script:** The experiments cover two very different domains to show generality. On the robotics side, the authors test diffusion policies on Robosuite Square, PushT, and FrankaKitchen, measuring task reward averaged over hundreds of evaluation episodes. On the image side, they evaluate StableDiffusion version 2 generating 768-by-768 images from COCO captions, judged by CLIP score, and pixel-space LSUN Church and Bedroom models, judged by FID score. Together these span latent-space and pixel-space diffusion at very different scales.

## Key Result
**Necessary:** ParaDiGMS delivers a consistent 2-4x sampling speedup across all tasks and samplers with no measurable loss in task reward, FID, or CLIP score, reaching 0.2s per sample on 100-step DiffusionPolicy and 14.6s on 1000-step StableDiffusion-v2.
**Additional:** On robotics, ParaDDPM gives 3.7x (Square), 3.9x (PushT), and 3.4x (FrankaKitchen); on StableDiffusion-v2, ParaDDPM cuts 50.0s to 14.6s (3.4x) while ParaDDIM/ParaDPMSolver reach 4.0x, all at unchanged CLIP score.
**Audio script:** The headline finding is remarkably consistent: a two-to-four times speedup across every task and every sampler, with no measurable degradation in quality. On robotic control, ParaDDPM speeds up sampling by roughly 3.4 to 3.9 times while holding task reward constant. On StableDiffusion version 2, it brings the time to generate an image down from fifty seconds to under fifteen, a 3.4x gain, and stacking it on faster samplers reaches four times. The number of parallel iterations needed for convergence is up to twenty times smaller than the number of sequential steps, which is why the approach works.

## Ablation Study
**Necessary:** Lowering the convergence tolerance trades speed for fidelity; a relaxed tolerance still preserves quality while a tolerance that is too high starts to degrade samples, confirming the tolerance as the key speed-quality knob.
**Additional:** On LSUN Church, ParaDDPM matches DDPM FID (12.8 vs 12.9) at 3.9x speedup, while 500-step DDIM alone gives a noticeably worse FID, showing the speedup does not come from simply cutting steps.
**Audio script:** The main ablation studies the effect of the error tolerance in the fixed-point iteration. A lower tolerance means more iterations and slower sampling but higher fidelity, while a looser tolerance is faster. The paper shows there is a comfortable regime where a fairly relaxed tolerance still preserves sample quality. Importantly, on LSUN Church, ParaDDPM matches full DDPM's FID score at nearly four times the speed, whereas simply reducing DDIM to 500 steps produces visibly worse images, demonstrating that the gains genuinely come from parallelism rather than fewer steps.

## Headline Numbers
**Necessary:** 2-4x sampling speedup; StableDiffusion-v2 50.0s to 14.6s (3.4x); LSUN Church FID 12.8 to 12.9 at 3.9x; parallel iterations up to 20x fewer than sequential steps.
**Additional:** 100-step DiffusionPolicy reaches 0.2s per sample; ParaDDIM and ParaDPMSolver reach 4.0x on StableDiffusion-v2 at unchanged CLIP score of 31.7-31.9.
**Audio script:** To put concrete numbers on it: sampling speedups of two to four times across the board. StableDiffusion version 2 drops from fifty seconds to fourteen-point-six seconds per image. On LSUN Church, FID barely moves, from twelve-point-eight to twelve-point-nine, while running almost four times faster. And the deep reason it scales is that the number of parallel iterations to converge is up to twenty times smaller than the thousand sequential steps.

## Takeaway
**Necessary:** By reformulating denoising as parallel Picard iteration, ParaDiGMS trades extra parallel compute for 2-4x lower diffusion sampling latency with no quality loss, and layers on top of existing fast samplers.
**Additional:** As GPUs get better at large parallel batches, the wall-clock cost of sampling will be bounded only by the small number of parallel iterations, promising even larger future speedups.
**Audio script:** The lasting takeaway is a new axis for accelerating diffusion models. Rather than sacrificing quality by taking fewer steps, ParaDiGMS spends parallel compute to run all the steps faster, cutting sampling latency by two to four times with no loss in quality, and it composes with the fast samplers people already use. Looking forward, as parallel hardware keeps improving, sampling time will be limited only by the small number of Picard iterations, pointing toward even faster real-time generation.
