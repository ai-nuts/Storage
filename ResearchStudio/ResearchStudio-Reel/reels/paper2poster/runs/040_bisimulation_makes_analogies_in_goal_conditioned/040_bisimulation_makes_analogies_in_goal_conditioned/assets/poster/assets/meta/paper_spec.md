---
title: Bisimulation Makes Analogies in Goal-Conditioned Reinforcement Learning
authors: Philippe Hansen-Estruch¹, Amy Zhang¹², Ashvin Nair¹, Patrick Yin¹, Sergey Levine¹
institutes: ¹University of California, Berkeley; ²Meta AI Research
venue: ICML 2022
paper_url: https://arxiv.org/abs/2204.13060
code_url:
title_audio_script: What if a robot could be told what to do not by an exact goal image, but by an analogy? This ICML 2022 paper from Berkeley and Meta AI proposes goal-conditioned bisimulation, a new state abstraction that captures functional equivariance between tasks. It lets an agent watch an analogous task, like closing a red drawer, and infer the equivalent goal for its own situation, like closing a blue one. The key idea is that behaviorally equivalent state-goal pairs should map to the same representation, so goals can be composed with simple arithmetic in latent space.
---

## Problem
**Necessary:** Goal-conditioned RL usually assumes the agent is handed the exact goal configuration, which is often unrealistic since the precise goal state is unknown before the task is attempted.
**Additional:** A more scalable interface would let a user provide an example of an analogous task and have the agent infer the corresponding goal for its own current state.
**Audio script:** In traditional goal-conditioned reinforcement learning, an agent is given the exact goal it should reach, typically as a target image or state. But in the real world, you rarely know the precise configuration of the goal ahead of time. Imagine asking a robot to close a drawer without knowing exactly what that drawer looks like when closed. A far more scalable framework would let us specify the task through an analogy: show the agent a similar task being solved, and let it work out what its own goal should be.

## Motivation
**Necessary:** Humans solve families of tasks, like dicing any vegetable, because their goal representation is invariant to irrelevant factors and equivariant to the factors that differ between analogous tasks.
**Additional:** Prior bisimulation and representation-learning methods focus on robustness to distractors for a single task, not on transferring skills across analogous goals.
**Audio script:** Consider a person asked to dice a carrot versus a radish. The objects differ, but the skill and the functional change from the starting state to the goal are essentially the same. Human task representations are invariant to irrelevant details and equivariant to the details that vary between similar tasks. Prior work on bisimulation metrics learned representations robust to visual distractors, but only for a single task. The motivation here is to lift that idea to whole families of tasks, so that skills learned in one setting transfer to new, unseen goals by analogy.

## Contribution
**Necessary:** The paper introduces goal-conditioned bisimulation (GCB), a state abstraction that captures functional equivariance across tasks, learned via a metric objective that enables goal specification through latent-space arithmetic over analogies.
**Additional:** It proves the learned representation is sufficient not only for goal-conditioned tasks but for any downstream task described by a state-only reward function, and validates GCB on simulated manipulation tasks.
**Audio script:** This work makes three main contributions. First, it defines goal-conditioned bisimulation, a new form of state abstraction that groups state-goal pairs which behave equivalently, capturing what the authors call functional equivariance. Second, it gives a practical metric-learning objective to learn this abstraction from pixels, so that new goals can be produced by simple arithmetic in the latent space. Third, it proves theoretically that the learned representation is sufficient for goal-conditioned control and, more broadly, for any task specified by a state-only reward function.

## Method
**Necessary:** GCB learns two encoders: a paired state-goal encoder φ trained so that ℓ₁ distance matches an on-policy goal-conditioned bisimulation metric, and a state encoder ψ trained so that the difference ψ(g) − ψ(s) equals φ(s, g), which makes goals composable by arithmetic. At test time an analogous pair (sₐ, gₐ) is added to the current state via ψ(s) + φ(sₐ, gₐ), and the nearest neighbor in ψ space yields the inferred goal.
**Additional:** Both encoders are six-layer CNNs mapping to 256-dim latent spaces; the policy π(ψ(s), φ(s, g)) is trained on top of Implicit Q-Learning (IQL) in an offline RL setting, with φ, ψ, and the policy learned concurrently.
**Key equation:** `$L_\phi = \Big(\lVert \phi(s_i,g_i)-\phi(s_j,g_j)\rVert_1 - \lVert r_i-r_j\rVert_2 - \gamma\lVert \bar\phi(s_i',g_i)-\bar\phi(s_j',g_j)\rVert_2\Big)^2$` ; `$\psi(g_i)-\psi(s_i)=\phi(s_i,g_i)$` ; `$L_\psi = \big\lVert(\bar\phi(s_i,g_i)-\bar\phi(g_i,g_i))-(\psi(g_i)-\psi(s_i))\big\rVert^2$`
**Audio script:** GCB learns two encoders trained together. The first, phi, encodes a state-goal pair so that the L1 distance between two pairs matches an on-policy goal-conditioned bisimulation metric, measuring how differently the two tasks behave. The second, psi, encodes a single state so that the vector difference between the goal's embedding and the state's embedding equals phi of that state-goal pair. This equality is what makes goals composable: you can add the representation of an analogous task to your current state and read off the corresponding goal. At evaluation, given an analogous pair, GCB computes psi of the current state plus phi of the analogous pair, then finds the nearest neighbor in psi space to recover a concrete goal. The whole system is trained offline on top of Implicit Q-Learning.

## Dataset / Benchmark
**Necessary:** GCB is evaluated in a PyBullet simulated manipulation suite of randomly generated workspaces with 84 object geometries, spanning Drawer, Button-and-Drawer (BD), and Analogy tasks, each also tested with added Video Distractors (VD).
**Additional:** The offline setting uses a demonstration policy that reaches the goal in roughly 80% of episodes; success is measured against the true goal over 5 seeds.
**Audio script:** The method is tested in a PyBullet simulation of robotic manipulation, using randomly generated workspaces built from a set of eighty-four object geometries. Tasks include operating a drawer, a combined button-and-drawer environment, and dedicated analogy tasks where the goal must be inferred from an example. Each task is also evaluated with video distractors added to the scene to test robustness. The environments were deliberately designed to showcase several distinct types of generalization, and all results are averaged over five random seeds.

## Key Result
**Necessary:** GCB achieves the best final success rate on 5 of 6 task settings, and is the strongest method on every distractor-augmented task, e.g. 0.448 on Drawer+VD, 0.322 on BD+VD, and 0.403 / 0.303 on Analogy / Analogy+VD.
**Additional:** On the analogy tasks GCB is the only representation that supports goal inference from an analogous pair, roughly doubling the next-best baseline (CPV) on Analogy (0.403 vs 0.176).
**Audio script:** Across six task settings, goal-conditioned bisimulation is the top performer on five of them, and it wins on every task that adds video distractors, showing its representation truly isolates task-relevant structure. On the drawer task with distractors it reaches about forty-five percent success, and on the harder button-and-drawer task with distractors about thirty-two percent, well ahead of the baselines. Most strikingly, on the analogy tasks, where the goal must be inferred from an example rather than given, GCB reaches roughly forty percent success and about double the next-best method, which is the compositional plan-vector baseline.

## Ablation Study
**Necessary:** Ablations show that adding the grounding point φ(gᵢ, gᵢ) as a normalizing constant in ψ's objective improves performance, and that the ℓ₁ metric loss for φ outperforms ℓ₂.
**Additional:** Varying the latent dimensionality of φ and ψ does not significantly affect downstream control performance on the Drawer task.
**Audio script:** The authors ablate several design decisions. Adding a grounding term, phi of goal with itself, as a normalizing constant in psi's objective helps performance, confirming the empirical choice in equation seven. Using an L1 metric loss to fit phi works better than L2. And varying the dimensionality of the learned latent spaces has little effect on downstream control, indicating the method is not sensitive to that hyperparameter.

## Headline Numbers
**Necessary:**
- Drawer+VD success: **0.448 ± 0.033** (GCB), best of all methods
- BD+VD success: **0.322 ± 0.021** (GCB), best of all methods
- Analogy success: **0.403 ± 0.041** (GCB) vs **0.176** (CPV, next best)
- Best method on **5 of 6** task settings, over **5 seeds**
**Additional:** Analogy+VD: 0.303 ± 0.027 (GCB, best); encoders are six-layer CNNs mapping to 256-dim latent spaces.
**Audio script:** Some headline numbers: on the drawer task with video distractors, GCB reaches a success rate of about forty-five percent, the best of any method. On button-and-drawer with distractors it reaches about thirty-two percent, again the best. On the core analogy task it hits about forty percent, more than double the next-best baseline's seventeen percent. Overall it is the strongest method on five of the six task settings, averaged over five seeds.

## Takeaway
**Necessary:** By making behaviorally equivalent state-goal pairs map to the same representation, goal-conditioned bisimulation lets an agent specify goals through analogy and latent-space arithmetic, generalizing skills to new, unseen goals.
**Additional:** The abstraction is provably sufficient for goal-conditioned control and for any state-only reward task, pointing toward more flexible task interfaces for RL.
**Audio script:** The core takeaway is that treating bisimulation as an equivalence over tasks, not just states, gives an agent a representation where analogous tasks line up. Because goals become composable by simple arithmetic in this space, you can point a robot at an example task and have it infer the right goal for its own situation. This makes goal-conditioned reinforcement learning far more flexible, and the authors prove the representation is sufficient not just for reaching goals but for any task defined by a state-only reward.
