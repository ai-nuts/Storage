# Problem

Core claim: Momentum SGD (mSGD) and AdaGrad are empirically superior to SGD, yet their theoretical convergence for smooth, possibly non-convex loss functions remains poorly established.

Supporting detail: Most prior results only guarantee subsequence convergence or convergence of time averages, which is weaker than the almost-sure asymptotic convergence practitioners rely on.

Narration: Momentum SGD and AdaGrad consistently beat plain SGD, yet their theory is incomplete. For possibly non-convex losses, existing analyses prove only weak guarantees, like subsequence or time-average convergence, not the almost-sure convergence practitioners rely on.
