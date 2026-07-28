# Takeaway

Core claim: You can fine-tune huge language models with just forward passes: MeZO matches backpropagation quality at inference-level memory, unlocking training of models an order of magnitude larger on the same hardware.

Supporting detail: Contrary to classical zeroth-order pessimism, fine-tuning a well pre-trained model converges in a rate governed by the local effective dimensionality of the loss, not the raw parameter count.

Narration: The lasting takeaway is that fine-tuning no longer strictly requires backpropagation. With MeZO, you can adapt very large language models using only forward passes, at the memory cost of inference, and still match the quality of gradient-based fine-tuning on many tasks. This overturns the classical worry that zeroth-order methods must scale badly with model size: when you start from a strong pre-trained model, convergence is governed by the effective local structure of the loss landscape rather than the sheer number of parameters, which is why MeZO works at billion-parameter scale.
