# Key Result

Core claim: A single Conditional Matrix Flow reconstructs the frequentist l1 solution path with MSE = 0.052 and, in the low-sample regime (n<d), sub-l1 pseudo-norms give higher F1 edge-recovery than the Bayesian Graphical Lasso, with CMF at q=0.25 outperforming all competing frequentist l0-surrogate penalties (atan, selo, log, sica) across every sample size, most strongly at n=15.

Supporting detail: Model selection via the CMF marginal likelihood picks λ=3.52, matching the Graphical Lasso cross-validation choice of λ=3.36. On real data the inferred network shows strong edges between cancer group stage (GS) and each TNM variable (T, N, M), and lower q yields visibly sparser graphs.

Narration: One model does the work of many. Trained once, the flow reconstructs the frequentist solution path with a mean squared error of just zero point zero five two. When samples are scarce, the sub-l-one pseudo-norms clearly beat the Bayesian Graphical Lasso, and the gain grows as q approaches zero. Against frequentist competitors it wins at every sample size, most at fifteen samples. Its model selection picks a lambda of three point five two, matching the cross-validated Graphical Lasso value of three point three six.
