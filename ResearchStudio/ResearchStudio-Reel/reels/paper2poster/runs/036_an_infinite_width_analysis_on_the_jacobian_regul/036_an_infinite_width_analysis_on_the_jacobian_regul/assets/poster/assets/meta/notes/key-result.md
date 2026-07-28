# Key Result

Core claim: As MLP width grows, the finite Jacobian NNGP kernel converges to its deterministic limit Σ⁽ᴸ⁾ (Figure 1) and the (1/κ²)-scaled finite JNTK converges to the limiting JNTK Θ (Figure 2), confirming Theorems 3.1 and 4.3. During robust training the JNTK's deviation from Θ shrinks monotonically with width at every training step (Figure 3), supporting the constancy claim of Theorem 4.5.

Supporting detail: The max-norm error at width 8192 is still above the smallest Gram-matrix eigenvalue, but its steady decrease with width indicates full validation would need wider networks than compute allowed.

Narration: The theory holds up. As the network gets wider, the finite Jacobian NNGP kernel closes in on its predicted deterministic limit, and the scaled finite JNTK converges to the limiting JNTK, matching the two initialisation theorems. And during robust training, the gap between the finite JNTK and its limit shrinks monotonically with width at every training step we checked, which is exactly what the constancy theorem predicts. The largest networks tested don't fully nail the bound because of compute limits, but the trend is unmistakable: wider is closer, in precisely the way the theory says.
