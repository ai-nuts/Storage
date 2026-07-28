# Problem

Core claim: How good is plain logistic regression for agnostically learning homogeneous halfspaces, where an adversary corrupts an OPT fraction of labels and we must compete with the best linear classifier of zero-one risk OPT?

Supporting detail: Prior work left a wide gap between an Ω̃(OPT) lower bound for all convex surrogates and an Õ(√OPT) upper bound achieved by logistic regression on well-behaved distributions.

Narration: The paper studies the agnostic learning of homogeneous halfspaces, one of the most fundamental problems in machine learning. We are given samples from an unknown distribution over feature-label pairs, and we want a linear classifier whose zero-one error is close to OPT, the best error achievable by any homogeneous halfspace. Equivalently, an adversary is allowed to flip an OPT fraction of the labels of an otherwise perfectly linearly separable dataset. Logistic regression is the natural, ubiquitous heuristic here, yet its theoretical guarantees for this problem were poorly understood. Prior results left a frustrating gap: a lower bound saying no convex surrogate loss can beat order OPT error, against an upper bound showing logistic regression reaches only order square-root of OPT. The central question is which of these bounds reflects the truth for logistic regression.
