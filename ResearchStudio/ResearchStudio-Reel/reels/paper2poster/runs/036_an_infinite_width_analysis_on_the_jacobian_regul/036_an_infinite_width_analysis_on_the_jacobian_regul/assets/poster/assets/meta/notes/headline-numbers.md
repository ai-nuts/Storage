# Headline Numbers

Core claim: Widths swept from 64 to 8192 (2⁶–2¹³); each experiment repeated 10× with 95% bootstrap confidence intervals; covariance estimates use one million Monte-Carlo samples.

Supporting detail: Robust-training hyperparameters λ = 0.01, κ = 0.1, learning rate 1; full-rank JNTK (Assumption 4.4) first holds at depth 11 (GeLU) and depth 6 (erf); required width estimate F = O(N²(log N)¹²ᴸ).

Narration: A few numbers anchor the study. Widths span 64 to 8192, powers of two from six to thirteen. Every experiment is repeated ten times and reported with ninety-five percent bootstrap confidence intervals, and the covariance estimates rest on a full million Monte-Carlo samples. Robust training uses a Jacobian coefficient of 0.01, a scaling kappa of 0.1, and a learning rate of one. The full-rank condition first kicks in at depth eleven for GeLU and depth six for erf, and the theory's width requirement scales like N-squared times log-N to the twelve-L.
