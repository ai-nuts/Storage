# Headline Numbers

Core claim: - NeuPL population size 8 exploits PSRO populations of 8 policies while PSRO used 2× the gradient updates. - Effective population size rises from 5 → 8 as relative population performance increases. - Effective population size plateaus at 12 across maximum population caps. - Transfer experiments repeated 5×; exploiters learned against Nash mixtures of n ∈ {2, 4, 7} policies.

Supporting detail: Evaluated on 3 domains (rock-paper-scissors, running-with-scissors, 2-vs-2 MuJoCo Football); a population cap greater than 8 yields only marginal exploitability benefit.

Narration: "To put numbers on it: a NeuPL population capped at eight policies beats PSRO populations of eight policies even when PSRO trained twice as long per iteration. As relative population performance climbs, the effective number of distinct policies grows from five to eight, and across different maximum caps the effective size saturates around twelve. The transfer study spans Nash mixtures over two, four, and seven policies, each repeated five times. Together these establish NeuPL as more sample-efficient and more robust than the standard iterative baselines."
