# Dataset / Benchmark

Core claim: Four numerical studies — a discrete-state toy example, high-dimensional synthetic data (state dim dS ∈ {1,10,20,30}), a 4×4 grid world, and a batch-online semi-synthetic study — plus a real-world Intern Health Study (IHS) micro-randomized mobile-health trial spanning 21 weeks.

Supporting detail: Synthetic settings fix N=100, T=50, α=0.05, true change point t_cpt=25; baselines are ODCP (Padakandla et al., 2020) and CUSUM-RL (Li et al., 2022, integral and normalized variants).

Narration: The method is stress-tested across four numerical studies and one real dataset. A discrete-state toy example illustrates the double robustness property directly. High-dimensional synthetic data pushes the state dimension from one up to thirty and pits the test against two existing baselines, ODCP and CUSUM-RL. A four-by-four grid world shows how detecting the change point improves policy learning, and a batch-online semi-synthetic study mimics the structure of the real trial. Finally, the authors apply the test to the Intern Health Study, a twenty-one-week mobile-health micro-randomized trial of medical interns in the United States.
