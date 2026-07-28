# Problem

Core claim: Equilibrium propagation (EP) needs weight symmetry and infinitesimal nudges for unbiased gradients, both hard to realize in physical or neuromorphic hardware, so how weight asymmetry causes bias was unknown.

Supporting detail: In practice asymmetry's contribution to bias is masked by the finite nudge, so the two effects had never been analytically separated.

Narration: Equilibrium propagation, or EP, is an appealing way to train neural networks directly on physical substrates like brains or analog chips, because it computes gradients using only the network's own relaxation dynamics. But it comes with two strict requirements: the weights must be perfectly symmetric, and the nudge that pushes the network toward its target must be infinitesimally small. Both are very hard to satisfy in real physical hardware. And crucially, whether weight asymmetry actually harms learning had never been pinned down, because in practice its effect gets tangled up with the error introduced by using a finite nudge.
