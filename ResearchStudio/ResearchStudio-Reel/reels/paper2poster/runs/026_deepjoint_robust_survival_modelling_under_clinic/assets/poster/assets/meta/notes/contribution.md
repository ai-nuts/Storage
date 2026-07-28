# Contribution

Core claim: A single multi-task recurrent architecture that jointly models three clinical-presence dimensions, longitudinal values, inter-observation timing, and missingness, alongside the survival outcome, trained end-to-end with a dynamically weighted likelihood.

Supporting detail: Empirical evidence that this joint modelling both improves discrimination and regularises the embedding to be robust under observation-process shift.

Narration: The paper contributes a deep joint model that treats clinical presence as multi-task learning. A shared recurrent embedding feeds four heads: longitudinal, inter-observation timing, missingness, and survival, all trained together by maximising a combined likelihood with dynamic weighting. The result is a representation that encodes the observation process, giving both a predictive edge and robustness when that process changes.
