---
title: "CROP: Certifying Robust Policies for Reinforcement Learning through Functional Smoothing"
authors: Fan Wu¹, Linyi Li¹, Zijian Huang¹, Yevgeniy Vorobeychik², Ding Zhao³, Bo Li¹
institutes: ¹University of Illinois at Urbana-Champaign; ²Washington University in St. Louis; ³Carnegie Mellon University
venue: ICLR 2022
paper_url: https://arxiv.org/abs/2106.09292
code_url:
title_audio_script: Reinforcement learning now drives safety-critical systems like autonomous vehicles, but adversarial perturbations to a policy's input states can quietly steer it toward disaster. Many defenses improve robustness empirically, yet almost none can certify it with guarantees. This paper introduces CROP, the first unified framework to certify robust policies for reinforcement learning through functional smoothing. CROP certifies robustness at two levels: the stability of the action taken at each state, and a provable lower bound on the cumulative reward across a whole trajectory. Using it, the authors benchmark nine existing robust RL algorithms across four environments and show that their certificates are often tight.
---

## Problem
**Necessary:** Reinforcement learning agents deployed in safety-critical settings are vulnerable to adversarial perturbations of their input states, yet no method could certify their robustness with theoretical guarantees.
**Additional:** Prior defenses (adversarial training, smoothness regularization) only offer empirical robustness, which stronger adaptive attacks repeatedly break.
**Audio script:** Reinforcement learning has moved into domains where failure is costly, such as autonomous driving and trading. But researchers have shown that an adversary who slightly perturbs the state observations fed to an RL agent can reliably change its decisions. A wave of empirical defenses followed, only to be defeated by newer adaptive attacks. What has been missing is certification: a way to prove, rather than just observe, that a trained policy stays reliable under every perturbation within a bounded budget. This paper tackles exactly that gap for reinforcement learning.

## Motivation
**Necessary:** Empirical robustness offers no guarantees, so a policy that resists known attacks may still fail against a stronger, unseen adversary; safety-critical RL needs provable certificates.
**Additional:** Randomized smoothing gives certified robustness in classification, but Q-learning breaks its assumptions: the output range is unbounded and outputs are not probabilities.
**Audio script:** The core motivation is trust. If you cannot prove a policy is robust, then passing today's attacks tells you little about tomorrow's. Randomized smoothing has become a leading tool for certifying image classifiers, but reinforcement learning does not fit its mold. In classification the confidence output lives in a known zero-to-one range and behaves like a probability; in Q-learning the value function has an unknown range and its outputs are not probabilities at all. On top of that, a single action decision is not the whole story: what ultimately matters is the reward accumulated along an entire trajectory of decisions. CROP is designed to overcome both obstacles.

## Contribution
**Necessary:** CROP is the first unified framework to certify RL robustness at both the per-state action level and the cumulative-reward level, with three concrete algorithms and an evaluation of nine robust RL methods across four environments.
**Additional:** It contributes a local smoothing algorithm for action certification, a global smoothing algorithm for a reward lower bound, and a novel adaptive local-smoothing search (CROP-LoRe) for tighter reward certificates, plus a public leaderboard.
**Audio script:** CROP makes three main contributions. First, it defines two certification criteria for reinforcement learning: robustness of the per-state action, and a lower bound on the cumulative reward. Second, it turns each criterion into an algorithm. CROP-LoAct uses local randomized smoothing to certify a radius around each state within which the chosen action cannot change. CROP-GRe uses global smoothing to bound the expected and percentile reward, and CROP-LoRe performs an adaptive tree search to produce a much tighter absolute lower bound on reward. Third, the authors apply these tools to nine existing robust RL algorithms across four environments, and release the results as an open leaderboard for the community.

## Method
**Necessary:** For each state, CROP draws Gaussian noise to smooth the trained Q-function; the smoothed value function is Lipschitz continuous, which yields a certified radius on the action from the margin between the top two smoothed action-values. For reward, global smoothing bounds the expected and percentile reward, and an adaptive local-smoothing tree search certifies an absolute lower bound.
**Additional:** Monte Carlo sampling estimates the smoothed values; the Q-output range [Vmin, Vmax] is pre-estimated on a state subset, and Hoeffding's inequality bounds the top-two smoothed values to certify a positive radius.
**Audio script:** The engine of CROP is functional smoothing. At each state, and for each action, the method adds Gaussian noise to the state and averages the trained Q-network's output, producing a smoothed value function. A key lemma shows this smoothed function is Lipschitz continuous, with a constant that shrinks as the smoothing variance grows. From that continuity, Theorem 1 gives a certified radius: as long as the perturbation is smaller than this radius, the smoothed policy's action does not change. The radius depends on the gap between the best and runner-up smoothed action-values, revealing a trade-off, since more smoothing stabilizes the values but also narrows their margin. For cumulative reward, global smoothing treats the whole trajectory as a function to bound the expected and percentile reward, while the adaptive local search of CROP-LoRe grows a trajectory tree to certify a tight absolute lower bound.
**Key equation:** `$\tilde{Q}^\pi(s_t,a) := \mathbb{E}_{\Delta_t \sim \mathcal{N}(0,\sigma^2 I_N)}\, Q^\pi(s_t+\Delta_t, a)$`, `$r_t = \frac{\sigma}{2}\left(\Phi^{-1}\!\left(\frac{\tilde{Q}^\pi(s_t,a_1)-V_{min}}{V_{max}-V_{min}}\right) - \Phi^{-1}\!\left(\frac{\tilde{Q}^\pi(s_t,a_2)-V_{min}}{V_{max}-V_{min}}\right)\right)$`, `$J(\pi) := \sum_{t=0}^{\infty} \gamma^t R(s_t, \pi(s_t))$`

## Dataset / Benchmark
**Necessary:** CROP is evaluated on four environments: two high-dimensional Atari games (Pong and Freeway), the low-dimensional CartPole control task, and an autonomous-driving Highway environment.
**Additional:** Nine RL methods are certified: StdTrain, GaussAug, AdvTrain, SA-MDP (PGD), SA-MDP (CVX), RadialRL, CARRL, NoisyNet, and GradDQN.
**Audio script:** To test the framework broadly, the authors run it on four environments spanning very different regimes. Pong and Freeway are high-dimensional Atari games; CartPole is a classic low-dimensional control task; and Highway simulates autonomous driving. On these, they certify nine existing reinforcement learning methods, ranging from standard training and Gaussian augmentation to adversarial training, the SA-MDP variants, RadialRL, CARRL, NoisyNet, and gradient-based DQN. This makes CROP not just a single certificate but a benchmark that places many robust RL methods on a common, provable footing.

## Key Result
**Necessary:** CROP certifies and ranks the nine methods: RadialRL is consistently the most certifiably robust on Freeway, while SA-MDP (CVX) is most robust on Pong, and the certified rankings largely match empirical robustness observations.
**Additional:** All methods exhibit periodic patterns in the per-state certified radius on Pong, tied to "confident states" such as when the ball approaches the paddle.
**Audio script:** The certifications reveal clear and consistent winners. On Freeway, RadialRL achieves the highest certified radius across every smoothing level, because it explicitly optimizes against worst-case perturbations. On Pong, SA-MDP with the convex relaxation is the most certifiably robust. Encouragingly, these certified rankings largely agree with what people had observed empirically, which builds confidence in the certificates. The analysis also surfaces new structure: on Pong every method shows a periodic pattern in its certified radius over time, with robustness peaking at confident states such as when the ball flies toward the paddle, an insight that could guide future robust training.

## Ablation Study
**Necessary:** Varying the smoothing parameter σ shows a trade-off: on Freeway larger σ (up to 1.0) steadily raises certified robustness for SA-MDP and RadialRL, while on Pong a moderate σ around 0.01 to 0.03 is best for almost all methods.
**Additional:** Among the reward bounds, the percentile bound Jp is much tighter than the loose expectation bound JE, and the absolute lower bound J shows a zero gap to empirical PGD results over a wide range of attack magnitudes.
**Audio script:** A central ablation studies the smoothing variance sigma. On Freeway, robustness for the strong methods keeps improving as sigma grows all the way to one point zero, since Freeway tolerates large noise. On Pong the story differs: too much smoothing hurts, and a moderate sigma between about zero point zero one and zero point zero three works best for nearly all methods. The authors also compare their three reward bounds. The percentile bound is far tighter than the loose expectation bound, and the absolute lower bound from CROP-LoRe often matches the empirical reward under PGD attack exactly, a zero gap that demonstrates the certificates are tight rather than merely valid.

## Headline Numbers
**Necessary:**
- First unified robustness certification framework for RL, covering both action and cumulative-reward levels
- 9 empirically robust RL methods certified
- 4 environments: Pong, Freeway, CartPole, Highway
- 3 certification algorithms: CROP-LoAct, CROP-GRe, CROP-LoRe
**Additional:**
- Smoothing variance σ certified up to 1.0 on Freeway
- 3 reward bounds computed: expectation JE, percentile Jp (p = 50%), absolute lower bound J
**Audio script:** A few numbers capture the scope. CROP is the first unified certification framework for reinforcement learning, working at both the action level and the cumulative-reward level. It certifies nine existing robust RL methods across four environments: Pong, Freeway, CartPole, and Highway. It does so with three algorithms: CROP-LoAct for actions, and CROP-GRe and CROP-LoRe for reward. The smoothing variance is pushed as high as one point zero on Freeway, and reward robustness is reported through three bounds, an expectation bound, a fifty-percent percentile bound, and an absolute lower bound.

## Takeaway
**Necessary:** CROP shows that functional smoothing can give reinforcement learning policies provable robustness certificates, at both the per-state action and cumulative-reward levels, and those certificates are often tight.
**Additional:** It establishes a common, provable benchmark for robust RL and an open leaderboard for future methods and environments.
**Audio script:** The lasting message of CROP is that robustness in reinforcement learning need not be a matter of hope. By smoothing the value function, you can prove that an agent's action stays fixed within a certified radius, and you can prove a lower bound on the reward it will collect under any bounded attack. Applied to nine methods across four environments, these certificates are not only correct but often tight, matching what attacks achieve. CROP turns robust RL into something you can measure and compare on a common, provable leaderboard, and invites the community to certify more methods and more environments in future work.
