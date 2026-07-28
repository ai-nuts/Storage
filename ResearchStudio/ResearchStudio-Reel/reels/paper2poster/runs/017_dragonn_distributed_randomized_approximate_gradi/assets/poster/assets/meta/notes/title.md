# Title

DRAGONN is a randomized hashing algorithm for gradient sparsification in data-parallel distributed training, from Rice University and ThirdAI. In distributed training, synchronizing gradients across GPUs is the main efficiency bottleneck, and gradient sparsification methods were meant to help, but their own compression overhead has become the new bottleneck. DRAGONN replaces the exact parallel-prefix-sum operations used by prior methods with direct hashing, cutting compression time by up to seventy percent and delivering up to three-and-a-half times faster training throughput.
