# Ablation Study

Core claim: Isolating the warm start, Hessian warm starts sharply cut coordinate-descent passes versus standard warm starts, often needing only a single pass per step because the warm start is near-exact when the active set is stable (Figure 2).

Supporting detail: The screening component alone keeps the number of screened predictors close to the true active-set minimum (Figure 1), whereas Celer, Blitz, Strong, EDPP, Gap Safe, and Sasvi screen orders of magnitude more, especially as correlation rises.

Narration: Two component studies show where the gains come from. Looking at the warm start in isolation, on colon-cancer and YearPredictionMSD the Hessian warm start collapses the number of coordinate-descent passes, frequently to a single pass per step, because when the active set does not change the warm start is essentially the exact solution. Looking at screening in isolation, the Hessian rule keeps the number of retained predictors close to the true active-set floor, while alternatives like Celer, Blitz, the strong rule, EDPP, Gap Safe, and Sasvi retain orders of magnitude more predictors, and the gap widens as correlation increases.
