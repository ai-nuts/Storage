# Motivation

Core claim: Statistical moments of observables, such as their energy-scale dependence, are often predictable from theory even when the full probability density is not, so a method that targets moments directly is valuable.

Supporting detail: Existing unbinned unfolding methods unfold whole spectra generically, which can compromise precision for any specific aspect like a small set of moments.

Narration: Summarizing a distribution with a few moments makes it tractable to visualize and, crucially, to predict from first principles. For example, the full densities of hadronic jets cannot be computed in perturbative QCD, but the energy dependence of their moments can be. Unbinned unfolding methods already exist and avoid binning artifacts, but they are built to unfold entire spectra, so they may trade away precision on the handful of moments a physicist actually wants. This motivates a dedicated method that unfolds the moments themselves.
