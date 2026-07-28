# Motivation

Core claim: The same patient population presents differently under different observation processes, so a model that overfits one clinical-presence regime fails when practice changes, a real risk as medicine evolves.

Supporting detail: The well-documented "weekend effect", different testing intensity and mortality for weekend versus weekday admissions, gives a natural, controllable observation-process shift to test robustness.

Narration: A key challenge is heterogeneity: the same patient population can appear very differently depending on the observation process, and that process shifts across countries, over time, and even between weekdays and weekends. The literature has studied covariate and label shift, but shift in the observation process itself is under-explored. DeepJoint asks how explicitly modelling clinical presence makes survival models more robust to it.
