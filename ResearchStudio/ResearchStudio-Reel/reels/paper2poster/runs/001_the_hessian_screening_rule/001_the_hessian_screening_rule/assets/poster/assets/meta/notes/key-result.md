# Key Result

Core claim: The Hessian screening rule is the fastest in every simulated setting, with the largest margin in the high-correlation low-dimensional case, and wins on nearly all real data sets, in all but one least-squares case taking under half the runner-up's time.

Supporting detail: On YearPredictionMSD it fits the path in 78.8 s versus 541 s for the working+ runner-up, and on e2006-tfidf in 14.3 s versus 143 s, roughly a 7× to 10× speedup.

Narration: The results are decisive. Across every simulated configuration, the Hessian rule takes the least time, and its advantage is largest exactly where competitors struggle, the high-correlation, low-dimensional setting. On real data it wins on nearly all twelve sets. For ℓ1-regularized least-squares it is fastest on all five, and in all but one case it finishes in under half the time of the next-best method, the working-set strategy. On YearPredictionMSD it fits the full path in seventy-nine seconds against five hundred forty-one for the runner-up, and on e2006-tfidf in fourteen seconds against one hundred forty-three, speedups of roughly seven to ten times.
