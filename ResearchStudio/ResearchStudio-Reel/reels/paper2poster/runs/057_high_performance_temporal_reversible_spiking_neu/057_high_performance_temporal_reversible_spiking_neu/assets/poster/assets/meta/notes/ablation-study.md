# Ablation Study

Core claim: Applying T-RevSNN to an MS-ResNet-34 baseline cuts training memory from 267.1 to 88.1 MB/img and epoch time from 11.2 to 7.4 min with only a 1.6% accuracy change (68.3%→66.7%); multi-level temporal fusion is worth 1.2% accuracy (68.6% vs 67.4%).

Supporting detail: Timestep T trades accuracy for cost (T=8 gives 69.8% at 49.8 MB/img); the scaled residual connection speeds convergence (25 vs 32 epochs to 60% accuracy); temporal and spatial reversibility are orthogonal and combine.

Narration: The ablations show that each design choice earns its place. Simply applying temporal reversibility to a standard MS-ResNet-34 slashes training memory from 267 down to 88 megabytes per image and cuts epoch time from 11.2 to 7.4 minutes, at the cost of only about one and a half accuracy points. The multi-level temporal fusion between stages is worth roughly 1.2 points of accuracy on its own. Varying the number of timesteps trades accuracy against cost, and the scaled residual connection helps the model converge noticeably faster, reaching 60 percent accuracy in 25 epochs instead of 32. The authors also confirm that temporal and spatial reversibility are orthogonal and can be stacked together.
