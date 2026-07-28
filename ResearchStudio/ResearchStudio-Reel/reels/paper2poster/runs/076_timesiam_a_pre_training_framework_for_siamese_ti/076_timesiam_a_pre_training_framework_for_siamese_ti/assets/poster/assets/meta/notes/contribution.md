# Contribution

Core claim: The paper proposes TimeSiam, a simple but effective Siamese pre-training framework that captures correlations among temporally distanced subseries; introduces learnable lineage embeddings to represent different past-to-current distances; and demonstrates consistent state-of-the-art fine-tuning across forecasting and classification in both in- and cross-domain settings.

Supporting detail: TimeSiam is backbone-agnostic (validated on iTransformer, PatchTST, and TCN) and supports both fixed-input and extended-input fine-tuning via multiple lineage embeddings.

Narration: This paper makes three main contributions. First, it proposes TimeSiam, a simple but effective pre-training framework that uses Siamese networks to capture correlations among temporally distanced subseries. Second, it introduces learnable lineage embeddings, a lightweight mechanism that lets one model represent many different past-to-current time distances. Third, through extensive experiments it shows TimeSiam achieves consistent state-of-the-art results when fine-tuned on both forecasting and classification, and across both in-domain and cross-domain settings. Crucially, the framework is backbone-agnostic, dropping cleanly onto modern encoders like iTransformer, PatchTST, and TCN.
