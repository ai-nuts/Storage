# Motivation

Core claim: When you down-scale a discrete signal, the Nyquist theorem requires an anti-aliasing filter; ignoring it lets high frequencies alias into low ones, breaking equivariance.

Supporting detail: Prior continuous-domain formulations have no notion of anti-aliasing, which is precisely the gap that produces their residual error.

Narration: The key insight is that down-scaling a discrete signal is fundamentally a signal-processing operation. The Nyquist sampling theorem tells us that before subsampling, we must apply an anti-aliasing filter, otherwise high-frequency content folds down into lower frequencies, the classic aliasing artifact seen in the wagon-wheel effect. Prior scale-equivariant networks, because they were formulated in the continuous domain, simply had no place for this filter. The authors argue that to be truly scale-equivariant, you must formulate the down-scaling directly in the discrete domain, with anti-aliasing built in from the start.
