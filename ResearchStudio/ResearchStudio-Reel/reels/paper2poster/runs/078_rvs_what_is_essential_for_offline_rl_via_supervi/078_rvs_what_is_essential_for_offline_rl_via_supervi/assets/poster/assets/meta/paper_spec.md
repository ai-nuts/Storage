---
title: "RvS: What is Essential for Offline RL via Supervised Learning?"
authors: Scott Emmons¹, Benjamin Eysenbach², Ilya Kostrikov¹, Sergey Levine¹
institutes: ¹UC Berkeley; ²Carnegie Mellon University
venue: ICLR 2022
paper_url: https://arxiv.org/abs/2112.10751
code_url: https://github.com/scottemmons/rvs
title_audio_script: What is actually essential for offline reinforcement learning done via supervised learning? This ICLR 2022 paper by Scott Emmons, Benjamin Eysenbach, Ilya Kostrikov, and Sergey Levine strips reinforcement learning via supervised learning, or RvS, down to its bare essentials. Their surprising finding: a plain two-layer feedforward network, trained simply to maximize likelihood, matches state-of-the-art results from far more complex methods built on temporal-difference learning or Transformer sequence models. The two things that really matter are choosing model capacity carefully and choosing what to condition on, goals or rewards.
---

## Problem
**Necessary:** Supervised learning can solve offline RL without temporal-difference learning, but it is unclear when this works and which algorithmic components are actually necessary for good performance.
**Additional:** Prior RvS methods disagree on whether advantage weighting or Transformer sequence models are needed, leaving practitioners without a clear recipe.
**Audio script:** Recent work showed that plain supervised learning, with no temporal-difference bootstrapping, can be remarkably effective for offline reinforcement learning. But the picture was muddy. Different papers reached contradictory conclusions about what makes these methods work: some emphasized advantage weighting, others reached for large Transformer sequence models. The core question this paper asks is simple but unanswered. When does supervised learning for offline RL actually work, and which algorithmic components are truly essential versus incidental complexity?

## Motivation
**Necessary:** Value-based offline RL is powerful in theory but hard to use, needing stabilization tricks and delicate tuning; converting RL into conditional imitation learning promises a simpler alternative.
**Additional:** If a minimal supervised recipe matches complex methods, it gives practitioners a dependable field guide and exposes where such methods still fail.
**Audio script:** Value-based methods dominate offline and off-policy RL, and they come with appealing theoretical guarantees. But in practice they are difficult to apply. They require complex tricks to stabilize learning and careful tuning of many hyperparameters. An attractive alternative is to convert the RL problem into a conditional, filtered, or weighted imitation learning problem, using the insight that suboptimal experience for one task may be optimal for another. If a minimal supervised recipe can match these complex methods, it would give practitioners a dependable field guide and also reveal exactly where such supervised methods still break down.

## Contribution
**Necessary:** The paper unifies existing goal- and reward-conditioned methods under a single RvS framework, then empirically isolates the essential design choices: model capacity, regularization, and the conditioning variable.
**Additional:** It shows a two-layer MLP maximizing likelihood is competitive with state-of-the-art TD and Transformer methods, and it exposes RvS weakness on random data as an open problem.
**Audio script:** The paper makes three contributions. First, it does not propose a new algorithm but instead places many existing goal-conditioned and reward-conditioned methods under one common framework, which the authors call RvS, reinforcement learning via supervised learning. Second, through extensive experiments it boils these methods down to their essential elements, showing that a two-layer feedforward network trained to maximize likelihood is competitive with much more complex state-of-the-art methods. Third, it identifies exactly which choices matter, model capacity, regularization, and what you condition on, and it honestly probes the limits, showing RvS is comparatively weak on random data.

## Method
**Necessary:** RvS trains an outcome-conditioned policy πθ(a | s, ω) with a two-layer feedforward MLP by maximizing the log-likelihood of observed actions, using hindsight relabeling so each action is a demonstration for the outcome it achieved.
**Additional:** Outcomes are either a future goal state (RvS-G) or an average future return (RvS-R), formed by concatenating the outcome onto the input state; no advantage weighting or Transformer is used.
**Audio script:** The method is deliberately simple. RvS assumes an agent in a Markov decision process and trains a policy conditioned on an outcome, which can be a future goal state or an average future return. Given an offline dataset of trajectories, it applies hindsight relabeling: every observed action becomes a demonstration for whatever outcome actually occurred in that trajectory. The policy is just a feedforward MLP with two fully connected layers, and the outcome is fed in by concatenating it onto the input state. Training maximizes the log-likelihood of the observed actions under the conditioned policy. There is no advantage weighting, no temporal-difference bootstrapping, and no Transformer, only a maximum-likelihood objective over relabeled experience.
**Key equation:** `$\max_{\theta} \sum_{\tau \in \mathcal{D}} \sum_{1 \le t \le |\tau|} \mathbb{E}_{\omega \sim f(\omega \mid \tau_{t:H})}\big[\log \pi_\theta(a_t \mid s_t, \omega)\big]$` with goal outcomes `$f(\omega \mid \tau_{t:H}) = \mathrm{Unif}(s_{t+1}, \dots, s_H)$` (RvS-G) and reward outcomes `$\omega = \tfrac{1}{H-t+1}\sum_{t'=t}^{H} r(s_{t'}, a_{t'})$` (RvS-R)

## Dataset / Benchmark
**Necessary:** Evaluated on three D4RL suites (AntMaze v2, Gym Locomotion v2, Franka Kitchen v0) plus the GCSL goal-conditioned suite (FourRooms, Door, Pusher, Lander, Claw), spanning navigation, locomotion, and manipulation.
**Additional:** D4RL datasets range from random to medium-expert quality; GCSL tasks are adapted for offline RL using random-policy data, and scores are normalized to the [0, 100] range.
**Audio script:** The evaluation is broad. On the D4RL benchmark, the authors use three suites: AntMaze, which requires an eight-degree-of-freedom quadruped to navigate a maze; Gym Locomotion, with HalfCheetah, Hopper, and Walker across random, medium, medium-replay, and medium-expert datasets; and Franka Kitchen, a nine-degree-of-freedom manipulation task built from human demonstrations. They also use the GCSL suite of goal-conditioned tasks, including two-dimensional navigation, Sawyer arm control, Lunar Lander, and a robotic claw, which they adapt for offline RL by collecting data with a random policy. All scores are normalized into a zero-to-one-hundred range for comparison.

## Key Result
**Necessary:** A simple two-layer MLP is state-of-the-art on AntMaze (RvS-G 53.5 average vs 50.6 for the best baseline), Kitchen (RvS-G 54.0), and GCSL (RvS-G 62.0 vs 58.0 for online GCSL), and on Gym RvS-R matches Decision Transformer using only an MLP.
**Additional:** RvS-G surprisingly matches dynamic-programming methods on subtrajectory-stitching tasks (mixed Kitchen, all AntMaze), where value-based methods were thought essential.
**Audio script:** The headline result is striking. Using nothing but a two-layer feedforward network trained with maximum likelihood, RvS reaches state-of-the-art performance in several suites. On AntMaze, goal-conditioned RvS scores fifty-three point five on average, edging out the best value-based baseline at fifty point six. On Kitchen it reaches fifty-four. On the GCSL suite it scores sixty-two, beating the online GCSL method at fifty-eight, despite using only offline data. And on Gym Locomotion, reward-conditioned RvS matches Decision Transformer while using a simple MLP instead of a large Transformer. Even on stitching tasks, long thought to demand dynamic programming, RvS-G keeps pace.

## Ablation Study
**Necessary:** Two design choices are decisive. Larger network width improves performance (up to 1024 hidden units), and dropout regularization helps or hurts depending on the dataset (boosts kitchen-complete, hurts hopper-medium-expert and antmaze-medium-play).
**Additional:** A categorical distribution over discretized actions matches or beats a unimodal Gaussian across the GCSL suite, again favoring higher policy capacity; validation loss only loosely predicts final performance.
**Audio script:** The ablations pin down what actually matters. First, capacity: the best architectures are larger than those used in standard online RL or imitation learning, and widening the network up to a thousand hidden units generally helps. Second, regularization: dropout is not universally good. It boosts performance on the small, human-demonstration kitchen-complete dataset, but hurts on hopper-medium-expert and antmaze-medium-play. Third, the output distribution: a categorical distribution over discretized actions matches or beats a unimodal Gaussian across the GCSL tasks, which fits the broader theme that more policy capacity helps. Finally, validation loss correlates only loosely with final performance, so it is not a reliable tuning signal.

## Headline Numbers
**Necessary:**
- RvS-G AntMaze average: **53.5** (best baseline CQL-p: 50.6) — state-of-the-art
- RvS-G Kitchen average: **54.0** (BC: 51.5, CQL-p: 48.2) — state-of-the-art
- RvS-G GCSL average: **62.0** vs online GCSL: 58.0 — from offline random data
**Additional:**
- RvS-R Gym average: **54.7**, matching Decision Transformer (57.0) with only an MLP
- Best hidden-layer width tuned up to **1024** units with two fully connected layers

## Takeaway
**Necessary:** A plain two-layer MLP trained to maximize likelihood is a state-of-the-art offline RL method, provided you carefully tune capacity and regularization and choose the right conditioning variable (goals vs rewards).
**Additional:** RvS remains comparatively weak on random data, where TD learning still wins, marking a clear open problem.
**Audio script:** The takeaway is a practitioner's field guide. You do not need advantage weighting or a Transformer to do offline RL by supervised learning. A plain two-layer feedforward network, trained simply to maximize likelihood, is competitive with the state of the art, as long as you get two things right: carefully tune the model's capacity and regularization, and choose the right thing to condition on, goals or rewards. The recipe is to grow the network width until performance saturates, then add a little dropout. The honest caveat is that on purely random data, temporal-difference methods still win, which the authors flag as an open problem for future work.
