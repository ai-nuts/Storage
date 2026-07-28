# Dataset / Benchmark

Core claim: Experiments span 13 benchmarks: eleven established datasets (ETT four subsets, Weather, Electricity, Traffic, Exchange for forecasting; AD, TDBrain, PTB for classification) plus two newly constructed large-scale multi-domain datasets, TSLD-500M and TSLD-1G, for cross-domain pre-training.

Supporting detail: TSLD-1G contains 13.9M examples merged from non-overlapping domains, enabling large-scale cross-domain transfer studies.

Narration: The evaluation is deliberately broad, spanning thirteen benchmarks and two mainstream tasks. For forecasting there are the four ETT subsets, plus Weather, Electricity, Traffic, and Exchange. For classification there are two EEG datasets, AD and TDBrain, and an ECG dataset, PTB. On top of these eleven established benchmarks, the authors construct two new large-scale, multi-domain datasets called TSLD-500M and TSLD-1G. The larger one packs nearly fourteen million examples drawn from diverse, non-overlapping domains, which lets the paper stress-test cross-domain transfer where pre-training and fine-tuning data come from entirely different sources.
