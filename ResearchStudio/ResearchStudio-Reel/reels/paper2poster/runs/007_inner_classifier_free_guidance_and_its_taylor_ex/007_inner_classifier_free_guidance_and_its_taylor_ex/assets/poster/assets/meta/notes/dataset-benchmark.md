# Dataset / Benchmark

Core claim: Experiments evaluate text-to-image generation on the MS-COCO validation set, reporting FID for fidelity and CLIP Score for text–image alignment.

Supporting detail: Guidance is tested on pretrained Stable Diffusion, with an additional class-conditional study on U-ViT and few-shot fine-tuning on Stable Diffusion v1.5.

Narration: The main evaluation is text-to-image on the MS-COCO validation set. Two metrics carry the story: FID, which measures image fidelity, where lower is better, and CLIP Score, which measures how well the image matches the prompt, where higher is better. The authors run these on pretrained Stable Diffusion, and add a class-conditional experiment on U-ViT plus a few-shot fine-tuning study on Stable Diffusion one point five.
