# Key Result

Core claim: The logistic-risk minimizer w on the constructed Q provably has zero-one risk R₀₋₁(w) ≥ √OPT/(60π), matching Frei et al.'s Õ(√OPT) upper bound and proving it tight. Under radial-Lipschitzness, logistic regression instead achieves R₀₋₁(w*) = O((1+Cκ)OPT), i.e. Õ(OPT).

Supporting detail: The two-phase algorithm attains E[min_t R₀₋₁(w_t)] = O(OPT+ε) for bounded and O(OPT·ln(1/OPT)+ε) for sub-exponential distributions.

Narration: The headline finding is a matching pair of bounds. On the constructed well-behaved distribution, the global minimizer of the population logistic risk has zero-one error at least square-root OPT divided by sixty pi, which asymptotically matches the best known upper bound and therefore proves that square-root OPT is the true rate for logistic regression alone. That is the sense in which the paper closes the long-standing gap. Then, by adding radial Lipschitzness of the density, the same logistic minimizer jumps to near-optimal error of order OPT, up to a constant Cκ that is bounded whenever the density is Lipschitz. And without any such assumption, the two-phase algorithm achieves order OPT plus epsilon error for bounded distributions and order OPT times log one over OPT for sub-exponential ones, in expectation over the run.
