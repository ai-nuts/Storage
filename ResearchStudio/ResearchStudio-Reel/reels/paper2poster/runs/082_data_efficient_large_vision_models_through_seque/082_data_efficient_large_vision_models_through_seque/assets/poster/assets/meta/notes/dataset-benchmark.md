# Dataset / Benchmark

Core claim: Training and evaluation span three vision tasks, image segmentation (subsets of SA-1B), human pose estimation (COCO-Pose), and image deraining (Rain13K), plus foreground segmentation on Pascal-5i and image classification on ImageNet.

Supporting detail: Held-out SA-1B subsets, MPII, and Test2800 serve as validation sets; metrics include validation loss, pixel accuracy, perplexity, and mIoU. The VQGAN encoder is trained on Laion.

Narration: Experiments cover three core tasks. Image segmentation uses subsets of SA-1B ranging from one to ten percent; human pose estimation uses the full COCO-Pose dataset; image deraining uses Rain13K. Validation relies on held-out SA-1B splits together with MPII and Test2800. The distilled models are also benchmarked on Pascal five-i foreground segmentation using mean intersection-over-union, and the practical eighty-million model is evaluated on ImageNet classification. Throughout, the VQGAN tokenizer is trained on the Laion dataset and used off the shelf.
