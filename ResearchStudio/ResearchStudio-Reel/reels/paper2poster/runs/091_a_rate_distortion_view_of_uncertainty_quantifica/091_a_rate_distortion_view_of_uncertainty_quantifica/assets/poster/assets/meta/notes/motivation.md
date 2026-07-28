# Motivation

Core claim: Existing single-pass Deterministic Uncertainty Methods rely on architectural constraints (e.g. spectral normalization) to avoid feature collapse, which can hurt calibration and complicate integration into large pre-trained models.

Supporting detail: Ensembles and Bayesian methods are distance-aware but need many forward passes, making them expensive to deploy at scale.

Narration: Today's fast, single-forward-pass uncertainty methods usually depend on special architectural tricks, like spectral normalization, to stop the network's features from collapsing. Those constraints can quietly damage calibration and are awkward to bolt onto large pre-trained models. The alternative, deep ensembles and Bayesian networks, are naturally distance-aware but require many forward passes, which is expensive at scale. The authors ask whether a single deterministic model can be distance-aware without these drawbacks.
