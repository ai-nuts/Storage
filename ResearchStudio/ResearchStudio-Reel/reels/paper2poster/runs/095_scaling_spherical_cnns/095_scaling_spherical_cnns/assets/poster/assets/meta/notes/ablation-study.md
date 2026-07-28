# Ablation Study

Core claim: Table 1 isolates each contribution on a QM9 model: phase collapse cuts RMSE by 8.0%, spectral batch norm by a further 1.4%, and the efficient residual block by another 2.4%, while the JAX/DFT/symmetry choices deliver large steps-per-second gains.

Supporting detail: Table 6 confirms the phase collapse activation, spectral pooling, and the new spherical molecule representation each outperform prior alternatives, reaching 15.25 meV MAE on QM9 enthalpy.

Narration: A careful ablation isolates the effect of each change. Starting from the JAX implementation, the phase collapse activation cuts error by eight percent, spectral batch normalization trims a further one and a half percent, and the efficient residual block another two and a half percent, all while improving speed. A separate comparison confirms that the phase collapse activation, spectral pooling, and the new spherical molecule representation each beat the prior alternatives from earlier work, together driving the QM9 enthalpy error down to about fifteen point two five milli electron volts.
