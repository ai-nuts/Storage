# Motivation

Core claim: Vision lacks the massive uniform corpora that NLP enjoys, so the one-epoch, data-abundant training recipes of large language models cannot transfer directly to data-limited vision tasks.

Supporting detail: Prior LVM work chases ever-larger models and datasets; the compression techniques (augmentation, distillation) routine elsewhere in vision remain unexplored for autoregressive LVMs.

Narration: Language models are typically trained for a single epoch over vast corpora to avoid overfitting. Computer vision rarely has that luxury: many tasks have only tiny datasets, so the language training schedule does not carry over. At the same time, the community keeps scaling model and dataset size, while classical remedies for scarce and imbalanced data, namely data augmentation and knowledge distillation, have barely been tried in the autoregressive vision setting. This paper closes that gap.
