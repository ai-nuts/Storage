# Headline Numbers

Core claim: mSGD mean-square-gradient rate is $O(e^{-\sum_{i=1}^n s\varepsilon_i / (p(1-\alpha)^2)})$; with α = 0 this equals the SGD rate, and as α→1 the time-average rate reaches order $O(1/T)$.

Supporting detail: Results require only Robbins-Monro step sizes (∑εₙ = ∞, ∑εₙ² < ∞, e.g. εₙ = 1/n) and a relaxed noise bound E‖∇g(θ) − ∇g(θ,ξ)‖² ≤ M(1 + g(θ)), with no convexity or bounded-iterate assumptions.

Narration: The key numbers are convergence rates. Momentum SGD's expected squared gradient norm decays exponentially, with exponent scaling as summed step sizes over p times one-minus-alpha squared. Alpha zero recovers the SGD rate; near one it reaches order one over T.
