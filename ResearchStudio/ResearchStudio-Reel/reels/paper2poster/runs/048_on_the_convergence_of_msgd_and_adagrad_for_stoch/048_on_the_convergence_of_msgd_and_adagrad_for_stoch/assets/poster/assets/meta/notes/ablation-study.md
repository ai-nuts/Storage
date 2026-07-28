# Ablation Study

Core claim: As a theory paper there are no experimental ablations; instead the analysis isolates the effect of the momentum coefficient α by deriving the convergence rate as a function of α.

Supporting detail: Setting α = 0 recovers the SGD rate exactly, and increasing α toward one reduces the rate coefficient, showing momentum's acceleration analytically rather than empirically.

Narration: In place of experiments, the paper studies how the convergence rate depends on the momentum coefficient. At zero it recovers SGD's rate exactly; toward one it shrinks the coefficient and pushes the time-average rate to order one over T.
