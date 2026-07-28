# Ablation Study

Core claim: Ablating CBFT's two auxiliary losses shows both are essential: the barrier loss $\mathcal{L}_B$ induces a mechanistically dissimilar model, while the invariance loss $\mathcal{L}_I$ selects the desired cue-invariant mechanism.

Supporting detail: Learning rate and cue-correlation strength affect whether large-learning-rate or perfectly correlated cues change linear connectivity after permutation.

Narration: The authors ablate the two auxiliary terms in the CBFT objective. Removing the barrier loss prevents the model from moving to a mechanistically dissimilar solution, while removing the invariance loss means the model no longer reliably selects the specific cue-invariant mechanism the user wants. In other words, the barrier loss handles the where, pushing away from the cue-relying minimizer, and the invariance loss handles the which, locking onto the desired invariance. Both are needed for CBFT to work.
