# Headline Numbers

Core claim: - First unified robustness certification framework for RL, covering both action and cumulative-reward levels - 9 empirically robust RL methods certified - 4 environments: Pong, Freeway, CartPole, Highway - 3 certification algorithms: CROP-LoAct, CROP-GRe, CROP-LoRe

Supporting detail: - Smoothing variance σ certified up to 1.0 on Freeway - 3 reward bounds computed: expectation JE, percentile Jp (p = 50%), absolute lower bound J

Narration: A few numbers capture the scope. CROP is the first unified certification framework for reinforcement learning, working at both the action level and the cumulative-reward level. It certifies nine existing robust RL methods across four environments: Pong, Freeway, CartPole, and Highway. It does so with three algorithms: CROP-LoAct for actions, and CROP-GRe and CROP-LoRe for reward. The smoothing variance is pushed as high as one point zero on Freeway, and reward robustness is reported through three bounds, an expectation bound, a fifty-percent percentile bound, and an absolute lower bound.
