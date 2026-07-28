# Ablation Study

Core claim: AUTO-S consistently outperforms AUTO-V once magnitude information is preserved, and the method is insensitive to the stability constant gamma: any gamma > 0 yields the same asymptotic convergence rate, justifying the fixed default gamma=0.01.

Supporting detail: Heatmaps over (R, learning rate) show the AUTO-S column matching the best hand-tuned R across SST2, QNLI, and MNLI, confirming R can be safely eliminated rather than tuned.

Narration: Two ablations anchor the design. First, comparing AUTO-V and AUTO-S shows that once the small stability constant restores gradient magnitude, AUTO-S consistently wins, confirming that the lazy region really does hurt AUTO-V. Second, sweeping the stability constant gamma shows the method is essentially insensitive to it: any positive gamma gives the same asymptotic convergence rate, which is why a single default of zero point zero one works everywhere. Heatmaps over threshold and learning rate further show the AUTO-S result landing right at the best hand-tuned threshold.
