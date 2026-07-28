# Motivation

Core claim: Logistic regression is a default algorithm in practice, but its worst-case behavior is alarming: Ben-David et al. (2012) show its minimizer can suffer zero-one risk as bad as 1−OPT on adversarial distributions.

Supporting detail: Restricting to "well-behaved" (e.g. isotropic log-concave) distributions makes the problem tractable, but the exact rate logistic regression achieves there was open, blocking any principled recommendation to use it.

Narration: Logistic regression is arguably the most widely deployed classification algorithm, so understanding its statistical guarantees is not merely academic. The worry is that logistic regression can behave terribly in the worst case; earlier work showed its risk minimizer can be wrong on nearly a one-minus-OPT fraction of examples on an adversarially built distribution. To rule out such pathologies, the community focuses on well-behaved distributions, such as isotropic log-concave ones, where much stronger guarantees are possible. But even under these assumptions the precise error rate of logistic regression was unknown, sitting somewhere between order OPT and order square-root OPT. Pinning down this rate tells us whether logistic regression is a near-optimal agnostic learner or whether it fundamentally leaves accuracy on the table, and if so, what minimal fix recovers optimality.
