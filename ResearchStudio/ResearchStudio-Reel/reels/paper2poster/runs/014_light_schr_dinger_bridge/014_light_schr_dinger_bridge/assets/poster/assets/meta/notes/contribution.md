# Contribution

Core claim: The paper proposes LightSB, a fast, simulation-free, non-minimax SB solver that combines Gaussian-mixture (sum-exp quadratic) parameterization of the Schrödinger potential with an energy-based view, giving a single straightforward objective with closed-form plan and drift.

Supporting detail: It also proves LightSB is a universal approximator of Schrödinger Bridges (the first such result) and analyzes its generalization error, showing it vanishes at the standard parametric rate.

Narration: The paper makes three contributions. First, it introduces LightSB, a lightweight solver that combines two recent ideas: parameterizing the Schrödinger potential with sum-exp quadratic, that is Gaussian mixture, functions, and viewing the log-potential as an energy function. Together these yield a single, non-minimax, simulation-free optimization objective with closed-form expressions for the plan and the drift. Second, the authors prove that this Gaussian-mixture solver is a universal approximator of Schrödinger Bridges, which they note is the first ever such result. Third, they analyze the generalization error and show it converges at the standard parametric rate as sample size grows.
