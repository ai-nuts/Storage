# Key Result

Core claim: Depth L = Θ(log k) is both necessary and sufficient for transformers to solve k-hop induction heads. Trained transformers match this threshold: incrementing depth by one approximately doubles the largest learnable k, with the empirical boundary landing exactly at ⌊log₂ k⌋ + 2.

Supporting detail: A six-layer transformer performs well on all k ≤ 16, five layers on k ≤ 8, four layers on k ≤ 4, and so on, an exponential growth of solvable k with depth that mirrors the constructive theory.

Narration: The headline result ties theory and experiment together. On the theory side, they prove logarithmic depth is not just sufficient but necessary: any transformer solving k-hop needs depth on the order of log k. On the experimental side, they train transformers of depths two through six and measure token-wise error as k grows. The picture is remarkably clean. Each extra layer roughly doubles the largest hop count the model can learn, so a six-layer network handles every k up to sixteen, a five-layer network up to eight, a four-layer network up to four. The empirical threshold sits right at floor of log base two of k plus two, precisely the depth their construction predicts. The learned models even turn out to be interpretable, with attention patterns that mirror the hand-designed proof.
