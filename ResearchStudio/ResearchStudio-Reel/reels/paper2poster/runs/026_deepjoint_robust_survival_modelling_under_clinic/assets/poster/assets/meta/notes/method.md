# Method

Core claim: An LSTM encodes each patient's irregular test sequence into an embedding h. Three MLP heads model the longitudinal (Gaussian), missingness (Bernoulli), and inter-observation timing (cumulative-intensity) processes; a DeepSurv Cox head models survival. All losses are averaged with a dynamic weighting-average scheme and back-propagated jointly.

Supporting detail: Variants: DeepJoint (embedding only), DeepJointFeature (adds clinical-presence features), and DeepJointFineTune (full fine-tune of the survival head after joint pre-training). Loss weights are normalised across tasks by a temperature-controlled Softmax.

Narration: A Long Short Term Memory network extracts an embedding from each patient's irregular sequence of laboratory tests. This embedding drives three clinical-presence heads: a longitudinal head predicting next test values under a Gaussian likelihood, a missingness head predicting which tests appear under a Bernoulli likelihood, and a timing head modelling the inter-observation intensity. A DeepSurv head models survival under Cox proportional hazards. The four losses are combined by dynamic weighting, balanced by a hyperparameter alpha, and optimised end to end.
