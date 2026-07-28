# Ablation Study

Core claim: Varying the pseudo-norm q ∈ {1, 0.75, 0.5, 0.25} shows the posterior median is progressively less shrunk toward zero as q decreases: at λ=0.3 the 95% credible interval excludes zero for q∈{0.25,0.5,0.75} but includes it for the BGL / q=1, directly demonstrating that sub-l1 norms reduce over-shrinkage.

Supporting detail: Sweeping temperature T interpolates the same model between the Bayesian solution (T=1, matches BGL) and the frequentist MAP path (T=0.01); on real data q∈{1.0,0.9,0.8,0.7,0.6} traces increasing sparsity of the recovered graph.

Narration: The key study varies the pseudo-norm exponent q. As q shrinks from one toward a quarter, the posterior median for a precision entry is pulled less toward zero, reducing over-shrinkage as promised. At a lambda of zero point three the ninety-five percent credible interval excludes zero for q below one, while the Bayesian Lasso at q equals one still includes zero and would drop the edge. A second knob, the temperature, slides the model from the Bayesian regime to the frequentist path.
