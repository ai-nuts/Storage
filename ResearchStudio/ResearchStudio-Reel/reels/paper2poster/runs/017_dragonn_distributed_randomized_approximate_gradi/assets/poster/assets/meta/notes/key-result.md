# Key Result

Core claim: DRAGONN reduces compression time by up to 70% versus state-of-the-art GS, and reaches the same convergence with up to 3.52x speedup in total training throughput over DGC and up to 35.9x over full synchronization, while matching FULL's test accuracy.

Supporting detail: The speedup of DRAGONN over DGC grows with the number of GPUs, showing better scalability; gains are expected to widen on faster networks where communication-to-compression ratio shifts toward compression.

Narration: The headline result is that DRAGONN cuts compression time by up to seventy percent compared to the best existing sparsification methods. Reaching the same level of convergence, it delivers up to three-and-a-half times higher total training throughput than Deep Gradient Compression, and up to nearly thirty-six times over full gradient synchronization, all while matching the test accuracy of full synchronization. Importantly, its advantage over DGC grows as more GPUs are added, which signals strong scalability, and the authors expect the gains to widen further on faster networks.
