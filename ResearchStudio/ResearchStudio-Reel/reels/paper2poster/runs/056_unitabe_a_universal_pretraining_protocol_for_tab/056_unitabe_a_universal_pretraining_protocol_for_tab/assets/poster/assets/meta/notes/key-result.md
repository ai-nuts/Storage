# Key Result

Core claim: On the 7 public tabular benchmarks UniTabE finetune reaches an average AUC of 0.83, surpassing strong baselines such as Tapas (0.81), FT-Transformer (0.80), and XGBoost (0.79); across the 12 held-out Kaggle tasks it outperforms XGBoost and TransTab-LSTM on both classification (AUC) and regression (R²).

Supporting detail: UniTabE also shows strong zero-shot classification (e.g. 0.94 AUC on IO, 0.89 on CA without target-data finetuning) and the smallest degradation under incremental columns.

Narration: The experiments show pretraining pays off. On seven standard public benchmarks, UniTabE reaches an average area-under-curve of about zero point eight three, beating Tapas, FT-Transformer, and the industry favorite XGBoost. On the twelve held-out Kaggle tasks, spanning classification and regression, it again outperforms XGBoost and a strong TransTab variant. It also performs well in zero-shot mode, making accurate predictions on some datasets with no task-specific finetuning, evidence of genuine transferable reasoning about tables.
