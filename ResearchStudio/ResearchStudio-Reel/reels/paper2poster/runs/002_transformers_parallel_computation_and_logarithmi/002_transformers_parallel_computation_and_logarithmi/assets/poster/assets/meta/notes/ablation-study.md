# Ablation Study

Core claim: Varying depth is the central ablation: depths {2, 3, 4, 5, 6} sweep the log-threshold, confirming the ⌊log₂ k⌋ + 2 boundary. Widening embedding dimension and heads (from m=128,H=4 to m=256,H=8) leaves the logarithmic depth dependence intact.

Supporting detail: Finite-sample training (1000–3000 examples) shows deeper models generalize better, evidence of a favorable inductive bias; interpretability probes reveal attention heads computing the intermediate findⱼ pointers used in the proof.

Narration: The experiments include several ablations that stress the core claim. Sweeping depth from two to six is the main one, and it cleanly traces out the logarithmic threshold. When they widen the models, going from embedding dimension one hundred twenty-eight and four heads up to two hundred fifty-six and eight heads, the depth-versus-k boundary barely moves, showing the dependence is really about depth, not sheer size. In the finite-sample regime, where overfitting is a risk, deeper models generalize better, hinting at an inductive bias suited to compositional tasks. And when they crack open the trained networks, the attention matrices line up with the intermediate pointer computations from the proof, so the learned solution mechanistically resembles the theoretical construction.
