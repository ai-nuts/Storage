# Key Result

Core claim: On in-domain forecasting TimeSiam lowers average MSE by 5.7% (PatchTST) and 2.5% (iTransformer) over random initialization, and on in-domain classification it raises average accuracy by 11.5%, consistently outperforming eight strong self-supervised baselines in both in- and cross-domain settings.

Supporting detail: In cross-domain transfer from TSLD-1G, TimeSiam sometimes exceeds even the in-domain result (e.g., TSLD-1G → ETTh1/ETTm1), underscoring the value of large, diverse pre-training data.

Narration: The results are consistent and strong. On in-domain forecasting, TimeSiam cuts average mean squared error by five point seven percent with a PatchTST backbone and two point five percent with iTransformer, and remember these backbones already forecast very well from scratch. On in-domain classification, it lifts average accuracy by eleven point five percent over random initialization. Across all these settings TimeSiam beats eight strong self-supervised baselines. Perhaps the most striking finding is in cross-domain transfer: pre-training on the large, diverse TSLD-1G dataset and fine-tuning elsewhere sometimes beats even in-domain pre-training, which confirms that scale and diversity of pre-training data really pay off.
