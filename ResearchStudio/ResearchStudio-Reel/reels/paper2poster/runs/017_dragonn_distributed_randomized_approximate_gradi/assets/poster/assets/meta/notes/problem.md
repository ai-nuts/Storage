# Problem

Core claim: In data-parallel distributed training, gradient synchronization is the efficiency bottleneck. Gradient sparsification (GS) reduces traffic, but its compression overhead now outweighs the communication savings, becoming the new bottleneck.

Supporting detail: For tensors above 2^24 bytes the compression overhead exceeds communication and other overheads; for small tensors GS can even be slower than full synchronization.

Narration: Data-parallel distributed training is the standard way to scale deep learning across many GPUs, but synchronizing gradients between workers is the dominant cost. Gradient sparsification promised relief by transmitting only a small subset of gradients, yet in practice the time spent compressing the gradients grew so large that it cancelled out the communication savings. The paper shows that once a tensor exceeds about sixteen megabytes, this compression overhead becomes the single largest efficiency bottleneck, and for small tensors sparsification can even be slower than sending everything.
