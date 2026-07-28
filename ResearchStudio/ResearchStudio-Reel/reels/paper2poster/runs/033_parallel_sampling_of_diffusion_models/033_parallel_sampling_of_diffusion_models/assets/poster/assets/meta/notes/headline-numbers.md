# Headline Numbers

Core claim: 2-4x sampling speedup; StableDiffusion-v2 50.0s to 14.6s (3.4x); LSUN Church FID 12.8 to 12.9 at 3.9x; parallel iterations up to 20x fewer than sequential steps.

Supporting detail: 100-step DiffusionPolicy reaches 0.2s per sample; ParaDDIM and ParaDPMSolver reach 4.0x on StableDiffusion-v2 at unchanged CLIP score of 31.7-31.9.

Narration: To put concrete numbers on it: sampling speedups of two to four times across the board. StableDiffusion version 2 drops from fifty seconds to fourteen-point-six seconds per image. On LSUN Church, FID barely moves, from twelve-point-eight to twelve-point-nine, while running almost four times faster. And the deep reason it scales is that the number of parallel iterations to converge is up to twenty times smaller than the thousand sequential steps.
