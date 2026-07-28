# Ablation Study

Core claim: Varying the middle point m (Table 2) yields a "U"-shaped FID, with the best FID of 15.42 at m = 1.1; points too close together miss long-term curvature, while points near 0 or 1 are hard for the model to score.

Supporting detail: Varying sampling steps (Table 3) shows ICFG is already strong at few steps (FID 15.80 at T = 10, improving to 15.28 at T = 50 for Call), and varying w and v maps the fidelity–diversity trade-off across condition spaces Call and Cnouns.

Narration: Two ablations illuminate the design choices. First, the middle point m, used to estimate the second-order term, produces a U-shaped FID curve: if the two points are too close, the estimate can't capture long-term change, and if they drift too near zero or one, the model struggles to score them, with the best value around m equals one point one. Second, varying the sampling steps shows the method already produces well-matched images at just ten steps, improving modestly up to fifty.
