# Problem

Core claim: Pretraining has revolutionized NLP and vision, but tabular prediction in data science lacks a universal foundation model because every task carries a different table schema, blocking cross-task knowledge transfer.

Supporting detail: Prior methods either textualize tables, discarding numerical semantics, or require identical column structure between training and inference, so they cannot generalize across heterogeneous or evolving tables.

Narration: Tabular data underpins applications like stock prediction, real-estate forecasting, and credit scoring. Yet unlike text and images, it has no widely adopted foundation model. The reason: tables come in endless schemas, different column names, data types, and counts, so a model trained on one cannot be reused on another. Existing methods either flatten tables into text, losing numerical meaning, or assume train and test share a fixed structure. Both block knowledge transfer across tasks.
