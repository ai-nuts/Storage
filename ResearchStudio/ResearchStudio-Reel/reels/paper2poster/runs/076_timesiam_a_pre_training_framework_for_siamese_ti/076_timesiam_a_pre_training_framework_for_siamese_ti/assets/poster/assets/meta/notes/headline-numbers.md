# Headline Numbers

Core claim: - 5.7% / 2.5% average MSE reduction on in-domain forecasting (PatchTST / iTransformer) vs random init. - 11.5% average classification-accuracy gain in-domain vs random init. - 13 benchmarks covering forecasting and classification, in- and cross-domain. - 8 state-of-the-art self-supervised baselines outperformed.

Supporting detail: TSLD-1G pre-training dataset contains 13.9M examples across multiple domains.

Narration: To put the impact in numbers: TimeSiam reduces average forecasting error by five point seven percent on PatchTST and two point five percent on iTransformer, and raises classification accuracy by eleven point five percent in the in-domain setting, all relative to training from scratch. It does this across thirteen benchmarks covering forecasting and classification in both in-domain and cross-domain settings, and it outperforms eight state-of-the-art self-supervised baselines. Backing the cross-domain story is TSLD-1G, a newly built pre-training dataset with nearly fourteen million examples spanning multiple domains.
