# Ablation Study

Core claim: Removing regularization (–REG) or removing adaptive weight modification (–AWM) shows each part helps: adaptive modification dominates when feature distributions are similar or languages differ, while regularization dominates when acoustic conditions differ sharply.

Supporting detail: In four-dataset sequence training, dropping adaptive modification (–REG to –AWM) degrades EER more than dropping regularization (RAWM to –REG), indicating adaptive weight modification is the larger contributor overall.

Narration: An ablation separates the two components. When old and new datasets share a similar feature distribution, adaptive weight modification does most of the work, and removing it sharply raises error. When the datasets are recorded under very different conditions, the regularization term becomes the key to overcoming forgetting. Across the full four-dataset sequence, removing adaptive weight modification hurts more than removing regularization, so it is the primary driver, with regularization a valuable complement.
