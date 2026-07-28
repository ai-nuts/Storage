---
title: The Hessian Screening Rule
authors: Johan Larsson¹, Jonas Wallin¹
institutes: ¹Department of Statistics, Lund University
venue: NeurIPS 2022
paper_url: https://arxiv.org/abs/2104.13026
code_url: https://github.com/jolars/HessianScreening
title_audio_script: This work, presented at NeurIPS 2022 by Johan Larsson and Jonas Wallin of Lund University, introduces the Hessian Screening Rule, a new way to speed up fitting the lasso regularization path. Screening rules discard predictors before a model is fit, shrinking the problem. The authors show that using second-order Hessian information yields both far tighter screening and much more accurate warm starts, especially when predictors are highly correlated, where existing rules struggle most. The result is a method that is the fastest across nearly every simulated and real benchmark they tested.
---

## Problem
**Necessary:** Fitting the lasso along a full regularization path is costly because the optimal penalty λ is unknown and must be tuned by cross-validation, requiring repeated refits over high-dimensional data.
**Additional:** Screening rules cut cost by discarding predictors before fitting, but existing heuristic and safe rules screen conservatively and degrade sharply when predictors are highly correlated.
**Audio script:** Sparse regression with the lasso is a workhorse for high-dimensional data, but fitting it is expensive. The best penalty strength is never known in advance, so practitioners fit an entire path of models across many penalty values and tune by cross-validation, refitting again and again. Screening rules help by discarding predictors before the solver even runs, shrinking each subproblem. The trouble is that the widely used rules become conservative and inefficient precisely when predictors are strongly correlated, which is exactly the regime where speed matters most.

## Motivation
**Necessary:** Existing sequential rules such as the strong rule and working-set strategy base their next-step estimate on first-order information, which over-screens under high correlation and forces costly KKT rechecks and re-optimization.
**Additional:** The authors observe that both the strong rule and the working-set strategy can be rewritten as estimates of the correlation (negative gradient) at the next path step, exposing a common weakness that second-order information can fix.
**Audio script:** The authors start from a unifying observation: the popular strong rule and the working-set strategy can both be expressed as estimates of the gradient, or correlation, at the next step of the path. When they lean only on first-order information, these estimates are crude, especially under high correlation. That crudeness has two costs. Screening becomes conservative, keeping far more predictors than necessary, and the warm starts that seed each optimization are inaccurate, so the solver needs many more passes to converge. Both problems point to the same fix, richer curvature information from the Hessian.

## Contribution
**Necessary:** The paper introduces the Hessian Screening Rule, which uses second-order (Hessian) information to produce a more accurate next-step gradient estimate for screening and, from the same Hessian, a much more accurate warm start; it also enables efficient Hessian updates and an approximate-homotopy path.
**Additional:** The rule extends beyond the standard lasso to general smooth convex losses such as ℓ1-regularized logistic regression, and ships as an open C++/R implementation.
**Audio script:** Their contribution is the Hessian Screening Rule. It exploits second-order information in two complementary ways. First, the Hessian gives a sharper estimate of the correlation at the next penalty value, which translates into far tighter screening. Second, the same Hessian and its inverse yield a warm start that is nearly the exact solution whenever the active set does not change, cutting the number of solver passes dramatically. The authors also show how to update the Hessian and its inverse efficiently as the active set changes, extend the method to general smooth convex losses like logistic regression, and release a full C++ and R implementation.

## Method
**Necessary:** For an interval where the active set is fixed, the lasso solution is linear in λ, so the Hessian yields a second-order estimate of the next-step correlation ĉ_H(λ_{k+1}); computation is restricted to the strong-rule set for efficiency, with a small unit-bound margin added. The same Hessian inverse gives a coefficient warm start that is exact when the active set stays constant.
**Additional:** Efficient low-rank updates maintain the Hessian and its inverse across active-set changes, and approximate homotopy adaptively places the λ grid; a preconditioner keeps the warm start stable.
**Key equation:** `$\hat{c}_H(\lambda_{k+1}) = c(\lambda_k) + (\lambda_{k+1}-\lambda_k)\, X^{\mathsf{T}} X_{A_k}\,(X_{A_k}^{\mathsf{T}} X_{A_k})^{-1}\,\mathrm{sign}\,\hat{\beta}(\lambda_k)_{A_k}$` and the Hessian warm start `$\hat{\beta}(\lambda_{k+1})_{A_k} := \hat{\beta}(\lambda_k)_{A_k} + (\lambda_k-\lambda_{k+1})\,H_{A_k}^{-1}\,\mathrm{sign}\,\hat{\beta}(\lambda_k)_{A_k}$`
**Audio script:** The method rests on a simple fact: on any interval where the active set of nonzero coefficients is unchanged, the lasso solution is a linear function of the penalty λ. That linearity lets the authors write down a second-order estimate of the correlation at the next penalty value using the Hessian of the active predictors. To keep it cheap, they restrict the expensive inner products to the strong-rule set and add a small fraction of the unit bound as a safety margin. The very same Hessian inverse provides the warm start, which is exact when the active set does not change, so the solver often converges in a single pass. Efficient low-rank updates keep the Hessian and its inverse current as predictors enter and leave, and an approximate-homotopy scheme adaptively chooses the penalty grid.

## Dataset / Benchmark
**Necessary:** Evaluation uses simulated Gaussian designs in a low-dimensional setting (n=10000, p=100, s=5, SNR=1) and a high-dimensional setting (n=400, p=40000, s=20, SNR=2), each at correlations ρ ∈ {0, 0.4, 0.8}, plus twelve real data sets.
**Additional:** Real data include bcTCGA, e2006-log1p, e2006-tfidf, scheetz, YearPredictionMSD (least-squares) and arcene, colon-cancer, duke-breast-cancer, ijcnn1, madelon, news20, rcv1 (logistic), spanning p up to ~4.3 million.
**Audio script:** The experiments cover both simulated and real data. On simulated Gaussian designs, they sweep a low-dimensional regime with ten thousand observations and a hundred predictors and a high-dimensional regime with four hundred observations and forty thousand predictors, each at three correlation levels, zero, point four, and point eight, averaged over twenty repetitions. They then test twelve real data sets for both ℓ1-regularized least-squares and logistic regression, ranging from small gene-expression matrices up to problems with millions of features such as news20 and rcv1. Baselines are the working-set strategy, Celer, and Blitz.

## Key Result
**Necessary:** The Hessian screening rule is the fastest in every simulated setting, with the largest margin in the high-correlation low-dimensional case, and wins on nearly all real data sets, in all but one least-squares case taking under half the runner-up's time.
**Additional:** On YearPredictionMSD it fits the path in 78.8 s versus 541 s for the working+ runner-up, and on e2006-tfidf in 14.3 s versus 143 s, roughly a 7× to 10× speedup.
**Audio script:** The results are decisive. Across every simulated configuration, the Hessian rule takes the least time, and its advantage is largest exactly where competitors struggle, the high-correlation, low-dimensional setting. On real data it wins on nearly all twelve sets. For ℓ1-regularized least-squares it is fastest on all five, and in all but one case it finishes in under half the time of the next-best method, the working-set strategy. On YearPredictionMSD it fits the full path in seventy-nine seconds against five hundred forty-one for the runner-up, and on e2006-tfidf in fourteen seconds against one hundred forty-three, speedups of roughly seven to ten times.

## Ablation Study
**Necessary:** Isolating the warm start, Hessian warm starts sharply cut coordinate-descent passes versus standard warm starts, often needing only a single pass per step because the warm start is near-exact when the active set is stable (Figure 2).
**Additional:** The screening component alone keeps the number of screened predictors close to the true active-set minimum (Figure 1), whereas Celer, Blitz, Strong, EDPP, Gap Safe, and Sasvi screen orders of magnitude more, especially as correlation rises.
**Audio script:** Two component studies show where the gains come from. Looking at the warm start in isolation, on colon-cancer and YearPredictionMSD the Hessian warm start collapses the number of coordinate-descent passes, frequently to a single pass per step, because when the active set does not change the warm start is essentially the exact solution. Looking at screening in isolation, the Hessian rule keeps the number of retained predictors close to the true active-set floor, while alternatives like Celer, Blitz, the strong rule, EDPP, Gap Safe, and Sasvi retain orders of magnitude more predictors, and the gap widens as correlation increases.

## Headline Numbers
**Necessary:**
- YearPredictionMSD (least-squares): 78.8 s vs 541 s for working+ (≈6.9× faster)
- e2006-tfidf (least-squares): 14.3 s vs 143 s (≈10× faster)
- Fastest in all 3 correlation levels × both dimensional regimes on simulated data
**Additional:**
- bcTCGA: 3.00 s vs 7.67 s (working+); madelon (logistic): 48.2 s vs 232 s
- Screens ~200 predictors near the active-set floor where rivals keep 10³–10⁴ (p = 20000, ρ up to 0.8)

## Takeaway
**Necessary:** Second-order Hessian information delivers both tighter screening and near-exact warm starts, making the Hessian Screening Rule the fastest way to fit lasso and ℓ1-logistic regularization paths, especially under high correlation.
**Additional:** The same Hessian machinery serves double duty (screening and warm starts) and generalizes cleanly to smooth convex losses beyond least-squares.
**Audio script:** The takeaway is that a single idea, reusing second-order Hessian information, pays off twice over. It tightens screening so the solver sees far fewer predictors, and it supplies warm starts so accurate that many path steps converge in one pass. Together these make the Hessian Screening Rule the fastest method for fitting lasso and ℓ1-regularized logistic regression paths across the benchmarks tested, with the biggest edge in the high-correlation regime that has historically been the hardest for screening rules.
