# Ablation Study

Core claim: Removing the Underwater Adaptive ViT encoder drops multi-class performance by 1.6 mAP (43.1 to 41.5), and replacing the Salient Feature Prompt Generator with a Multi-scale Feature Enhancer drops it by 0.9 mAP (43.1 to 42.2), confirming both modules contribute.

Supporting detail: Further ablations show freezing the image encoder costs about 1.4 mAP, and simplifying the multi-scale convolution reduces performance, validating the specific adapter design choices.

Narration: Ablations isolate each component. Starting from the full model at 43.1 mAP on the multi-class task, reverting the Underwater Adaptive ViT block to the original drops performance by 1.6 mAP, confirming that adapters help the frozen backbone handle complex marine scenes. Replacing the Salient Feature Prompt Generator with a generic Multi-scale Feature Enhancer costs 0.9 mAP, showing it does more than fuse features, it focuses attention on salient regions. Further ablations on encoder freezing and the convolution design confirm each choice matters.
