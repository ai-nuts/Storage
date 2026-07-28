# Motivation

Core claim: Frequentist Graphical Lasso gives the l1 solution path over λ but not a posterior; Bayesian formulations give a posterior but rely on expensive Gibbs samplers that must be re-run for every λ and do not generalize to other priors.

Supporting detail: Variational inference could unify both, but mean-field approximations assume independence, which is precisely the dependence structure a GGM aims to model, so they cannot be applied naively.

Narration: Two camps exist. The frequentist Graphical Lasso traces the whole solution path as lambda varies, but returns only point estimates. The Bayesian Graphical Lasso gives a full posterior and a marginal likelihood, but relies on Gibbs samplers that mix poorly and must restart for every lambda. Variational inference could bridge them, yet the usual mean-field trick assumes independence, exactly what a graphical model seeks. We need a family that respects dependence and flexes across lambda and the norm.
