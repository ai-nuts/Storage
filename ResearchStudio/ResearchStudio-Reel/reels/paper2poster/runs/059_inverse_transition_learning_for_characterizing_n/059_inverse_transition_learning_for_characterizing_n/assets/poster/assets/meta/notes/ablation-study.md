# Ablation Study

Core claim: Varying data volume shows more data does NOT rescue MLE: it keeps making "bad mistakes" (actions outside the ε-ball) because large regions of the state-action space stay unexplored under expert-only data (aleatoric uncertainty).

Supporting detail: Sweeping ε=0/3/4 confirms the method holds across degrees of expert optimality, recovering policies that can beat the expert while keeping near-zero variance.

Narration: A central finding of the analysis is that more data does not rescue maximum likelihood. Even in the high data regime it keeps making bad mistakes, choosing actions outside the epsilon ball, because expert only data leaves large parts of the state and action space unexplored no matter how many episodes we collect. Sweeping the optimality level from zero through four confirms that our method holds across degrees of expert optimality, recovering policies that can even beat the expert while keeping variance close to zero.
