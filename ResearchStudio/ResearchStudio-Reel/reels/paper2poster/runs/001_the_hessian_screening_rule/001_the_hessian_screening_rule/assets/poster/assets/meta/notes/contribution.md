# Contribution

Core claim: The paper introduces the Hessian Screening Rule, which uses second-order (Hessian) information to produce a more accurate next-step gradient estimate for screening and, from the same Hessian, a much more accurate warm start; it also enables efficient Hessian updates and an approximate-homotopy path.

Supporting detail: The rule extends beyond the standard lasso to general smooth convex losses such as ℓ1-regularized logistic regression, and ships as an open C++/R implementation.

Narration: Their contribution is the Hessian Screening Rule. It exploits second-order information in two complementary ways. First, the Hessian gives a sharper estimate of the correlation at the next penalty value, which translates into far tighter screening. Second, the same Hessian and its inverse yield a warm start that is nearly the exact solution whenever the active set does not change, cutting the number of solver passes dramatically. The authors also show how to update the Hessian and its inverse efficiently as the active set changes, extend the method to general smooth convex losses like logistic regression, and release a full C++ and R implementation.
