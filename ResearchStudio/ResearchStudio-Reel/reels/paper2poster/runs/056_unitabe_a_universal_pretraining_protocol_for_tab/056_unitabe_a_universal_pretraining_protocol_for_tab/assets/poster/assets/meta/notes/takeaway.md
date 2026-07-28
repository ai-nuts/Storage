# Takeaway

Core claim: A schema-agnostic cell encoder plus free-form prompts, pretrained on 13 billion tabular samples, yields the first broadly transferable tabular foundation model that beats XGBoost and adapts to missing values, zero-shot tasks, and growing schemas.

Supporting detail: UniTabE shows that the pretrain-then-transfer paradigm from NLP is viable for structured tabular data when feature processing respects cell-level structure rather than textualizing it.

Narration: The pretraining paradigm that reshaped language and vision can extend to tabular data. The key is to respect table structure rather than flatten it into text: represent each cell by its column name, value, and data type, refine with a Transformer, and adapt through free-form prompts. Pretrained on billions, UniTabE becomes a general tabular model that transfers across tasks, beats the XGBoost baseline, and handles missing values and tables that gain columns.
