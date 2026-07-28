# Key Result

Core claim: A NeuPL population of size 8 exploits PSRO baselines representing the same 8 policies even when those baselines received twice as many gradient updates, and its rising performance tracks its effective population size growing from 5 to 8.

Supporting detail: Populations become less exploitable as they expand; effective population size plateaus at 12 across maximum sizes, and increasing the cap beyond 8 gives only marginal exploitability benefit.

Narration: "The headline result is that NeuPL is both more efficient and more robust than comparable PSRO baselines. With a maximum population of eight policies, a NeuPL population successfully exploits PSRO populations of the same eight policies — even when each PSRO iteration was given twice as many gradient steps. Crucially, the gain in relative population performance coincides with growth in the effective population size, from five up to eight distinct policies, showing that the improvement comes from genuinely discovering new strategies rather than overfitting. Both continued-training and from-scratch PSRO variants prove equally exploitable, suggesting they fail to build reusable representations."
