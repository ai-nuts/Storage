# Dataset / Benchmark

Core claim: The score network is trained on 11 hours of real LIGO-Hanford data around GW150914 (sampled at 4096 Hz, split into 4 s segments), with the segment containing the true signal discarded.

Supporting detail: Testing injects a simulated GW150914-like signal (chirp mass M = 29 M⊙, η = 0.2495, χ₁ = χ₂ = 0, dL = 400 Mpc) into held-out real LIGO noise after the training window; training is done in the Fourier domain after a Tukey window (αT = 0.1), with likelihood integration starting at 20 Hz.

Narration: The demonstration uses real data. They train the score network on eleven hours of real LIGO-Hanford data around GW150914, sampled at four thousand ninety-six hertz in four-second segments, discarding the segment holding the true signal. Training runs in the Fourier domain after a Tukey window. To test, they inject a simulated GW150914-like signal into held-out real noise never seen during training.
