# Method

Core claim: MuSc has three parts. LNAMD aggregates patch tokens from a frozen ViT at multiple degrees r to represent anomalies of different sizes. MSM lets every unlabeled test image assign anomaly scores to every other image's patches (mutual scoring), averaging only the minimum-interval scores to sharpen the normal/abnormal separation. RsCIN then refines the image-level classification score using a constrained neighborhood graph over class tokens with a multi-window mask.

Supporting detail: Backbone is a frozen ViT-L/14-336 (OpenAI CLIP), 24 layers in 4 stages; patch tokens from each stage feed LNAMD, and the last-layer class token feeds RsCIN. Inputs are scaled to 518×518; MSM keeps the minimum 30% interval; RsCIN uses multi-window {2,3} on MVTec AD and {8,9} on VisA.

Narration: The backbone is a frozen vision transformer. Patch tokens from several stages are aggregated at multiple neighborhood degrees to represent defect sizes. In mutual scoring, each patch is scored by its nearest match in every other image, and only the smallest score interval is averaged, sharpening the gap. The image score is refined with a constrained neighborhood graph on class tokens.
