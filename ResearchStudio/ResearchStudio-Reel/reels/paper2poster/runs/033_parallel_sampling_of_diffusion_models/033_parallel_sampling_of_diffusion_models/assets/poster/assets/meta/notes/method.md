# Method

Core claim: ParaDiGMS reframes denoising as solving an ODE by Picard iteration: it guesses the entire denoising trajectory, then iteratively refines every timestep in parallel until the fixed-point iteration converges, which empirically needs far fewer iterations than there are steps.

Supporting detail: To fit GPU memory it processes a sliding batch window of size p, updating each point from the cumulative drift over the window and sliding forward as soon as the leading timesteps converge; for SDEs the noise is sampled up front so the resulting ODE stays Lipschitz.

Narration: The method builds on Picard iterations, a classic technique for solving ordinary differential equations by fixed-point iteration. The insight is to write the value at each timestep as the initial value plus the integral of the drift along the path. Starting from a full guess of the trajectory, ParaDiGMS updates every timestep simultaneously using the cumulative drift, and repeats until the values stop changing. Because each iteration can be computed in parallel across timesteps, and the number of iterations to converge is much smaller than the number of steps, the whole trajectory resolves much faster. In practice it uses a sliding window of a fixed size to respect GPU memory, advancing the window as soon as the earliest timesteps converge.
