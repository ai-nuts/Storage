# 01_title

This work sharply analyzes the test error of finite-rank kernel ridge regression, the model behind tuning a frozen network's last layer. It derives matching upper and lower bounds that stay tight for any regularization.

---

# 02_problem

Kernel ridge regression helps explain generalization, and tuning a network's last layer behaves like it with a finite-rank kernel. But classical bounds are far too loose here: they keep the ridge above zero, give only upper bounds, and go vacuous as regularization vanishes.

---

# 03_motivation

Freezing a pre-trained backbone and retraining only the final layer is everywhere, and it defines a finite-rank kernel. Yet the theory lags: many results need the input dimension to grow, others fix how the ridge decays, and almost none give a lower bound, without which tightness cannot be claimed.

---

# 04_contribution

The contribution is threefold. First, the bounds improve as the ridge goes to zero. Second, a sharp lower bound matches the upper bound as samples grow, so both are tight. Third, experiments show a large gain over prior work. The key trick: work in the eigenfunction basis, separating spectrum from sampling noise.

---

# 05_method

The method starts from the kernel-ridge estimator and splits the test error into a bias term and a variance term, each bounded with high probability. The key ingredients: careful algebra on the ridge terms, a sub-Gaussian covariance concentration inequality, and a Neumann-series expansion. That lets the bounds hold for any ridge value.

---

# 06_dataset-benchmark

Being a theory paper, the experiments use controlled synthetic settings. The authors test two finite-rank kernels: a truncated neural tangent kernel and a constructed low-rank kernel. For each they sweep sample sizes from ten to two hundred and many ridge values, averaging ten trials with median and quartile bars.

---

# 07_key-result

The new upper and lower bounds bracket the error across sample sizes on both kernels, and squeeze together as samples grow. Against Bach's bound the gain is stark: the new bound hugs the true error while Bach's floats far above. In the ridgeless limit, bias reduces to the finite-rank error and variance to the noise.

---

# 08_ablation-study

The paper ablates its bound. The finite-rank error is an irreducible floor, while residue terms shrink at a log-N-over-N rate and vanish for large samples. Dropped, the simplified bounds fail only in the small-sample regime, as predicted. A ridge sweep shows the new bound improves toward the ridgeless limit while the prior worsens.

---

# 09_headline-numbers

The bounds hold with probability at least one minus two over N. The upper bound decays at a log-N-over-N rate, faster than the square-root Rademacher rate. Variance scales as noise times twice the rank over N. And these are the first finite-rank bounds with a high-probability lower bound.

---

# 10_takeaway

The takeaway: finite-rank kernel ridge regression, behind last-layer fine-tuning, has sharp bounds, matching upper and lower, tight for any regularization including none. The key idea, working in the eigenfunction basis to separate spectrum from sampling noise, is a template others can borrow.
