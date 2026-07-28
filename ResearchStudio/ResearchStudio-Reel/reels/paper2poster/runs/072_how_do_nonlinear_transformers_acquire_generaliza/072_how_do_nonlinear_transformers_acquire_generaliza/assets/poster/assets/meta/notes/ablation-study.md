# Ablation Study

Core claim: Varying the relevant-pattern fraction shows required context length scales as α⁻¹ (training) and α′⁻¹ (testing), and iterations and samples scale as α^(−2/3): a larger fraction gives faster convergence and shorter needed context.

Supporting detail: Comparing ICL against logistic regression, Gaussian/linear-kernel SVM, and 1-/3-nearest-neighbor: at α′ = 0.8 ICL's advantage is modest, but at the harder α′ = 0.6 ICL is the most sample-efficient, showing it filters irrelevant data and resists label noise better than classical methods.

Narration: Ablations vary the fraction of context examples that share the query's relevant pattern. As predicted, the needed context length grows like one over alpha and the needed iterations and samples grow like alpha to the minus two-thirds, so richer contexts converge faster and need shorter prompts. A second comparison pits in-context learning against logistic regression, kernel and linear SVMs, and nearest-neighbor classifiers. When the relevant fraction is high the gap is small, but in the harder low-fraction regime in-context learning is the most sample-efficient method, indicating it removes irrelevant data and tolerates label noise better than the classical baselines.
