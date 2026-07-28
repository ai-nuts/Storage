# Motivation

Core claim: If a single protocol could ingest arbitrarily structured tables and be pretrained at scale, the resulting model would transfer knowledge across tasks, handle missing values, generalize zero-shot, and absorb newly added columns.

Supporting detail: Self-supervised objectives similar to masked language modeling have proven that unlabeled data teaches useful representations; the open question is how to apply that recipe to structure-varied tables.

Narration: The promise of pretraining is that a model learns general knowledge once from huge unlabeled data, then transfers it to many tasks. The authors ask whether this recipe can work for tables. Three ingredients are needed: a way to represent any table regardless of schema, a training framework flexible enough for many objectives, and a data source large enough to pretrain at scale. Together, one tabular model could handle classification, regression, missing-value imputation, zero-shot prediction, and tables that grow new columns, without redesigning per task.
