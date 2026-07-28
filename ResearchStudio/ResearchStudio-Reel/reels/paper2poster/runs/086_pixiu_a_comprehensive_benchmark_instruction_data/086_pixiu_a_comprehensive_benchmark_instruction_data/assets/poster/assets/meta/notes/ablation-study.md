# Ablation Study

Core claim: Scaling from FinMA-7B to FinMA-30B gives no consistent gain on most NLP or prediction tasks, showing data quality and diversity matter more than parameter count; FinMA-7B-full (trained on NLP + prediction) achieves the best result on the ACL18 stock dataset.

Supporting detail: On complex quantitative QA (ConvFinQA), larger LLaMA-based FinMA does help, tracking LLaMA's better math performance at scale, but still trails GPT-4.

Narration: Comparing model variants is revealing. FinMA-30B shows no significantly better performance than FinMA-7B on most NLP tasks or on stock movement prediction, indicating that the quality and diversity of the instruction data matter more than sheer parameter count. Scale does help on complex quantitative question answering like ConvFinQA, mirroring LLaMA's improved math ability at larger sizes, though it still trails GPT-4. Notably, FinMA-7B-full, fine-tuned on both NLP and prediction tasks, achieves the best performance among all models on the ACL18 stock prediction dataset, highlighting the promise of task-specific instruction tuning for financial prediction.
