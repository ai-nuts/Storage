# Key Result

Core claim: Lack of linear mode connectivity provably and empirically signals mechanistic dissimilarity: ResNet-18 minimizers trained with versus without cues cannot be linearly connected even after permutation, yet quadratic paths connect them easily.

Supporting detail: Naive fine-tuning keeps models linearly connected to pretraining and preserves cue reliance, whereas CBFT breaks this connectivity and removes it.

Narration: The central empirical finding validates the theory. When ResNet-18 models are trained with and without spurious cues, they are mechanistically dissimilar, and the paper shows they cannot be connected by a linear path, even after accounting for permutation symmetries. However, a quadratic path connects them with ease. This confirms that linear disconnection is a reliable signal of differing mechanisms. It also explains why naive fine-tuning fails: fine-tuned models stay linearly connected to their pretraining solution and therefore keep relying on the same spurious cues.
