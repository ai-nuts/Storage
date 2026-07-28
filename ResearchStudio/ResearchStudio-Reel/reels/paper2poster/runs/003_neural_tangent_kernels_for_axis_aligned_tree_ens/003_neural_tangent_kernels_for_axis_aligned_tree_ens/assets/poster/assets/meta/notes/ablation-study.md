# Ablation Study

Core claim: Sweeping the split-hardness α (Table 1) shows the win rate against the MLP-induced NTK rises from 13.6% at α = 0.5 to a peak of 34.9% at α = 32, versus 11.8% for the RBF kernel; sweeping depth reveals the rise-then-fall accuracy pattern predicted by degeneracy.

Supporting detail: The oblivious-tree equivalence is verified: sharing splitting rules within a depth (NODE-style) yields the same kernel as non-oblivious trees, so this common architectural constraint costs nothing in the infinite limit.

Narration: Two ablations are central. Sweeping the split-hardness parameter alpha shows harder splits give better dataset-wise win rates against the MLP kernel, climbing from about fourteen percent when splits are soft to nearly thirty-five percent at the hardest, all above the radial basis function baseline. Sweeping tree depth reproduces the degeneracy story. The authors also verify empirically that oblivious trees, as used by NODE, induce the same kernel as ordinary soft trees.
