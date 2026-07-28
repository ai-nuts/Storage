# Headline Numbers

Core claim: - 10,632 underwater images with pixel-level annotations across 7 categories (USIS10K) - 59.7 mAP class-agnostic salient instance segmentation (state of the art) - 43.1 mAP multi-class salient instance segmentation (state of the art) - +1.6 mAP from the Underwater Adaptive ViT encoder; +0.9 mAP from the SFPG

Supporting detail: Trained 24 epochs on 6 NVIDIA 3090 GPUs with a ViT-H backbone; class-agnostic scores 81.6 AP50 and 67.7 AP75.

Narration: The headline numbers tell the story. USIS10K brings 10,632 annotated underwater images across seven categories. On class-agnostic segmentation, USIS-SAM reaches 59.7 mAP, with 81.6 AP at fifty percent and 67.7 at seventy-five. On multi-class it reaches 43.1 mAP. Ablations attribute 1.6 mAP to the Underwater Adaptive ViT encoder and 0.9 to the Salient Feature Prompt Generator. Training used 24 epochs on six NVIDIA 3090 GPUs with a ViT-H backbone.
