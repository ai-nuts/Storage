# Contribution

Core claim: The paper proposes CW-ERM, a simple training principle that uses closed-loop simulation of an identification policy to find failure scenes and then upsamples them when training the final policy, debiasing it toward closed-loop performance.

Supporting detail: It evaluates CW-ERM on a challenging real-world urban driving dataset showing significant collision reductions, and draws a formal connection to covariate-shift correction via density-ratio estimation.

Narration: "The paper makes three contributions. First, it proposes Closed-loop Weighted Empirical Risk Minimization, a technique that leverages closed-loop metrics from policy rollouts to debias the policy network and shrink the distribution gap between open-loop training and closed-loop inference. Second, it evaluates the method experimentally on a challenging urban driving dataset and shows significant closed-loop improvements, all without complex or computationally expensive closed-loop training. Third, it establishes an important theoretical connection between this reweighting scheme and the classic family of methods that correct covariate shift through density-ratio estimation."
