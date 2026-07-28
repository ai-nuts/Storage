# Key Result

Core claim: ParaDiGMS delivers a consistent 2-4x sampling speedup across all tasks and samplers with no measurable loss in task reward, FID, or CLIP score, reaching 0.2s per sample on 100-step DiffusionPolicy and 14.6s on 1000-step StableDiffusion-v2.

Supporting detail: On robotics, ParaDDPM gives 3.7x (Square), 3.9x (PushT), and 3.4x (FrankaKitchen); on StableDiffusion-v2, ParaDDPM cuts 50.0s to 14.6s (3.4x) while ParaDDIM/ParaDPMSolver reach 4.0x, all at unchanged CLIP score.

Narration: The headline finding is remarkably consistent: a two-to-four times speedup across every task and every sampler, with no measurable degradation in quality. On robotic control, ParaDDPM speeds up sampling by roughly 3.4 to 3.9 times while holding task reward constant. On StableDiffusion version 2, it brings the time to generate an image down from fifty seconds to under fifteen, a 3.4x gain, and stacking it on faster samplers reaches four times. The number of parallel iterations needed for convergence is up to twenty times smaller than the number of sequential steps, which is why the approach works.
