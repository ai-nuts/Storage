# Title

Foundation models have transformed language and vision, yet tabular data, the workhorse of data science, was left behind. Every table has a different schema, so a model trained on one rarely transfers to another. This paper introduces UniTabE, a universal pretraining protocol that handles any table uniformly. It encodes each cell with a small module called TabUnit, refines the table with a Transformer, and adapts through text prompts. Pretrained on thirteen billion Kaggle samples, it beats XGBoost.
