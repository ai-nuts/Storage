# Method

Core claim: Neuroformer tokenizes each neuron's spikes into Current and Past State windows, optionally encodes video and behavior, aligns the modalities with a multimodal contrastive objective, fuses them via cascading cross-attention, and decodes spikes autoregressively with a causally masked transformer that predicts both which neuron fires and its sub-interval time bin.

Supporting detail: Cross-attention between the small Current State array and the larger feature arrays reduces attention cost from O(Tf²) to O(Tc·Tf), scaling linearly when Tc≪Tf; inference uses nucleus sampling, and downstream tasks attach a mean-pooled head fine-tuned with cross-entropy or MSE.

Narration: Neuroformer treats each spike as a token, splitting activity into Current and Past States. Video becomes patches via a 3D-convolutional encoder; behavior forms a separate stream. A contrastive module aligns neural, visual, and behavioral features. Cross-attention fuses the Current State with larger feature arrays, cutting attention cost from quadratic to linear. A causally masked decoder predicts which neuron fires and its time bin.
