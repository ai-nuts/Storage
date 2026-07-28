# Problem

Core claim: In split learning with a vision transformer, the cut-layer "smashed data" stays highly similar to the raw input because ViT lacks pooling and convolution, leaking privacy and inflating communication cost.

Supporting detail: Federated learning is the usual privacy-preserving alternative but must communicate ViT's large model, imposing excessive energy and communication burdens on edge devices.

Narration: We want to train on user data without exposing it. Federated learning keeps data local but exchanges whole models, costly for large transformers. Split learning instead shares only cut-layer activations, the smashed data. But transformers have no pooling or convolution, so their smashed data barely distorts the input and stays visually similar to the raw image. That similarity leaks privacy and, preserving so much information, also inflates communication cost.
