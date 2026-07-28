# Dataset / Benchmark

Core claim: The model is validated on (1) a simulated spiking neural network with known ground-truth connectivity and (2) real large field-of-view two-photon calcium imaging from mouse visual areas V1 and AL (386 reliable neurons) responding to gratings and naturalistic videos, plus a Visnav virtual-navigation dataset with simultaneous speed/behavior.

Supporting detail: V1+AL and Visnav Neuroformer models use ~40M and ~100M parameters respectively; 8 layers, 8 heads, embedding dimension 256, 80/20 train/test split, AdamW at learning rate 2e-4.

Narration: Validation spans two levels. First, a simulated spiking network with three hub neurons gives a ground-truth connectivity matrix. Second, two-photon calcium imaging of mouse visual cortex records 386 neurons across V1 and AL viewing gratings and natural videos, plus a virtual-navigation dataset pairing activity with running speed.
