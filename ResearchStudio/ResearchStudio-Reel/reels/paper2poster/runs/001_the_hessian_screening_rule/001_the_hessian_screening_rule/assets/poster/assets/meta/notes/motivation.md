# Motivation

Core claim: Existing sequential rules such as the strong rule and working-set strategy base their next-step estimate on first-order information, which over-screens under high correlation and forces costly KKT rechecks and re-optimization.

Supporting detail: The authors observe that both the strong rule and the working-set strategy can be rewritten as estimates of the correlation (negative gradient) at the next path step, exposing a common weakness that second-order information can fix.

Narration: The authors start from a unifying observation: the popular strong rule and the working-set strategy can both be expressed as estimates of the gradient, or correlation, at the next step of the path. When they lean only on first-order information, these estimates are crude, especially under high correlation. That crudeness has two costs. Screening becomes conservative, keeping far more predictors than necessary, and the warm starts that seed each optimization are inaccurate, so the solver needs many more passes to converge. Both problems point to the same fix, richer curvature information from the Hessian.
