# Motivation

Core claim: Settings with abundant unlabeled data and costly expert labels are a natural fit for active learning, yet no prior work combines active learning with tabular language models.

Supporting detail: Large transformers require batch-based acquisition (not one-by-one selection) and train for multiple epochs per round, so naive uncertainty sampling picks highly correlated, redundant cells that add little value.

Narration: Active learning is built for this setting: plentiful unlabeled data and expensive labels, squeezing the most performance from every annotation. But big transformer models can't learn one example at a time; they train in batches over several epochs, so the acquisition function must choose a whole batch at once. Pure uncertainty sampling grabs very similar, correlated cells, often from the same table, wasting budget. Yet no one had studied active learning with tabular language models, the gap this work fills.
