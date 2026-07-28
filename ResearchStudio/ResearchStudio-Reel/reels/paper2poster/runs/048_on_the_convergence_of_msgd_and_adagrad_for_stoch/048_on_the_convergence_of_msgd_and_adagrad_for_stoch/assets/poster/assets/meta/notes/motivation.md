# Motivation

Core claim: A rigorous convergence theory for static-momentum mSGD and standard AdaGrad, without convexity, bounded-iterate, or uniformly bounded-gradient-noise assumptions, is still missing.

Supporting detail: Prior work handles only time-varying momentum or modified AdaGrad variants; the widely used static momentum coefficient and the norm-form AdaGrad in practice fall outside those conditions.

Narration: Why now? Prior momentum proofs need a coefficient shrinking to zero, but practitioners fix it near zero point nine. Prior AdaGrad results cover a modified form, not the standard one. It drops convexity, bounded-iterate, and bounded-noise assumptions.
