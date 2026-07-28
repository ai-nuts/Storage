# Ablation Study

Core claim: On Fashion MNIST the Cauchy-integral estimate removes finite-nudge bias: at large nudge |β|=0.5, classic one-sided EP degrades to 38.4% error while the N=6 estimate reaches 14.3%, matching the true derivative (14.7%).

Supporting detail: Using N=2 instead of the exact derivative costs an extra 2.9 points on CIFAR-10, isolating the residual finite-nudge contribution; an antisymmetric output-to-first-layer architecture shows the same benefits, confirming the loss is more general than weight alignment.

Narration: The ablations cleanly separate the two biases. On Fashion MNIST, when the nudge is made large, classic one-sided EP falls apart, its error ballooning to thirty-eight point four percent. The holomorphic Cauchy-integral estimate with six points instead stays at fourteen point three percent, essentially matching the true derivative at fourteen point seven percent, proof that finite-nudge bias is fully removed. Separately, dropping from the exact derivative to a coarse two-point estimate costs about three points on CIFAR-10, quantifying the residual nudge bias. And an architecture whose output feeds straight back to the first layer, with no reciprocal connections, benefits just as much, confirming the loss targets functional symmetry rather than weight symmetry.
