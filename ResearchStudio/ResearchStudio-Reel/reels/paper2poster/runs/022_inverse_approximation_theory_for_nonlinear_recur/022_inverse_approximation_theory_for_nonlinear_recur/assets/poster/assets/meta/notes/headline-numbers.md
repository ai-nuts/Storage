# Headline Numbers

Core claim: On MNIST (10 epochs, 3 repeats), softplus stable reparameterization reaches 71.36% test accuracy vs. 68.47% for the direct unstable baseline, a gain of about 2.9 points; exp 70.55% and inverse 70.77% also beat direct.

Supporting detail: Exponential-memory targets are approximated in ~10 epochs vs. ~1000 epochs for polynomial-memory targets; teacher models use hidden dimension m=256.

Narration: A few numbers capture the impact. On MNIST, trained for ten epochs and averaged over three runs, the softplus stable reparameterization reaches seventy one point three six percent test accuracy, compared with sixty eight point four seven percent for the direct, unstable baseline, an improvement of nearly three percentage points. The exponential and inverse stable maps also land above seventy percent, all beating the unstable version. On the synthetic side, exponential-memory targets are fit in roughly ten epochs, while polynomial-memory targets need on the order of a thousand epochs and still fail the stability test. The teacher-filtering experiment uses hidden dimension two hundred fifty six.
