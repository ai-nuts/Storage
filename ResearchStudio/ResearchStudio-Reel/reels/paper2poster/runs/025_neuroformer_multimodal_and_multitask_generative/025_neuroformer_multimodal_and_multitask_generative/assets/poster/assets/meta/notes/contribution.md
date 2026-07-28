# Contribution

Core claim: Neuroformer is a multimodal, multitask generative pretrained transformer for neural data that scales linearly with feature size, ingests an arbitrary number of modalities, recovers directed circuit connectivity, and transfers to behavior prediction with few-shot fine-tuning.

Supporting detail: All training is self-supervised and label-free; the paper validates the model on both a ground-truth simulated network and real two-photon imaging data from mouse visual cortex.

Narration: Neuroformer makes four contributions. It reframes spike analysis as self-supervised autoregressive generation, needing no labels. Its cross-attention scales linearly with feature size and fuses many modalities. On simulated data, its attention maps recover directed connectivity, including hub neurons correlation misses. Pretrained, it decodes behavior with few-shot fine-tuning.
