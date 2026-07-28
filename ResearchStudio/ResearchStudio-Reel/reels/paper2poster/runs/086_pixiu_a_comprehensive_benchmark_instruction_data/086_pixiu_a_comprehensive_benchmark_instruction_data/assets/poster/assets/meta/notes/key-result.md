# Key Result

Core claim: FinMA significantly outperforms BloombergGPT, ChatGPT, and GPT-4 on most FLARE NLP tasks; on the FPB sentiment dataset FinMA-30B beats GPT-4 by 10% F1 and BloombergGPT by 37% F1, and achieves SOTA on 3 NLP tasks plus 1 prediction dataset.

Supporting detail: FinMA underperforms on question answering (FinQA/ConvFinQA) due to LLaMA's weak quantitative reasoning, and all LLMs remain limited on stock movement prediction.

Narration: On the FLARE benchmark, the fine-tuned FinMA models significantly outperform other large language models on most financial NLP tasks, including sentiment analysis, headline classification, and named entity recognition. For example, on the Financial Phrase Bank sentiment dataset, FinMA-30B outperforms GPT-4 by ten percent F1 and BloombergGPT by thirty-seven percent F1. This demonstrates the value of tailoring LLMs to the financial domain through instruction tuning. However, FinMA underperforms on question answering tasks that demand quantitative reasoning, a limitation inherited from LLaMA's weak mathematical ability. And across all models, stock movement prediction remains challenging, leaving clear room for future improvement.
