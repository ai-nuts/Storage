# Problem

Core claim: Fitting the lasso along a full regularization path is costly because the optimal penalty λ is unknown and must be tuned by cross-validation, requiring repeated refits over high-dimensional data.

Supporting detail: Screening rules cut cost by discarding predictors before fitting, but existing heuristic and safe rules screen conservatively and degrade sharply when predictors are highly correlated.

Narration: Sparse regression with the lasso is a workhorse for high-dimensional data, but fitting it is expensive. The best penalty strength is never known in advance, so practitioners fit an entire path of models across many penalty values and tune by cross-validation, refitting again and again. Screening rules help by discarding predictors before the solver even runs, shrinking each subproblem. The trouble is that the widely used rules become conservative and inefficient precisely when predictors are strongly correlated, which is exactly the regime where speed matters most.
