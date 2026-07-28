# Contribution

Core claim: The authors compile a new unbiased, multi-label, expert-annotated SAR dataset, apply the SwAV contrastive framework to three million unlabeled Sentinel-1 images, and benchmark self-supervised embeddings against ImageNet transfer learning and the prior CmWV model.

Supporting detail: They evaluate the learned representation under three protocols (weighted kNN, linear evaluation, and full fine-tuning) to isolate the value of self-supervised pretraining.

Narration: This paper makes three contributions. First, it builds a new hand-labeled dataset of about twenty-three hundred randomly sampled, multi-label radar observations that better represents the real ocean population. Second, it leverages three years of unlabeled Sentinel-1 imagery, roughly three million images, to train a SwAV contrastive embedding of SAR scenes. Third, it rigorously compares that self-supervised representation against standard transfer learning from ImageNet and against the previous state-of-the-art CmWV classifier, using three different downstream evaluation protocols.
