# Headline Numbers

Core claim: - Lower bound: R₀₋₁(w) ≥ √OPT / (60π) for the logistic minimizer (valid when OPT ≤ 1/100). - Upper bound with radial-Lipschitzness: R₀₋₁(w) = Õ(OPT). - Two-phase algorithm error: O(OPT + ε) (bounded); O(OPT·ln(1/OPT) + ε) (sub-exponential). - Sample complexity: Õ(d/ε²), improving the Õ(d/ε⁴) of prior nonconvex approaches.

Supporting detail: Prior O(OPT+ε) algorithms solve O(log(1/OPT)) minimization problems; this method needs only 2 convex steps (logistic regression + one perceptron phase).

Narration: A few numbers capture the impact. The lower bound gives a zero-one error of at least square-root OPT over sixty pi for the logistic minimizer, valid whenever OPT is at most one one-hundredth. Under radial Lipschitzness, logistic regression reaches near-optimal order-OPT error. The two-phase algorithm achieves order OPT plus epsilon error for bounded distributions and order OPT times log one over OPT for sub-exponential ones. It does so with a sample complexity of order d over epsilon squared, a quadratic improvement over the d over epsilon to the fourth required by prior nonconvex methods. And structurally, whereas earlier algorithms that hit order OPT error had to solve a logarithmic number of minimization problems while guessing OPT by binary search, this method needs only two convex steps.
