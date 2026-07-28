# Dataset / Benchmark

Core claim: Evaluation spans robotics policies (Robosuite Square, PushT, FrankaKitchen) and image generation (StableDiffusion-v2 on COCO2017 captions, and pixel-space LSUN Church/Bedroom).

Supporting detail: Robotics tasks use DiffusionPolicy models measured by task reward over 200 episodes; image models are measured by CLIP score on ViT-g-14 and FID on 5000 samples.

Narration: The experiments cover two very different domains to show generality. On the robotics side, the authors test diffusion policies on Robosuite Square, PushT, and FrankaKitchen, measuring task reward averaged over hundreds of evaluation episodes. On the image side, they evaluate StableDiffusion version 2 generating 768-by-768 images from COCO captions, judged by CLIP score, and pixel-space LSUN Church and Bedroom models, judged by FID score. Together these span latent-space and pixel-space diffusion at very different scales.
