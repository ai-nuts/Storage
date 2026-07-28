# Problem

Core claim: Time series pre-training borrows masked modeling and contrastive learning from vision and language, but randomly masking a series or computing series-wise similarity distorts or neglects the temporal correlations that are intrinsic and crucial to time series.

Supporting detail: Random masking can make reconstruction too hard to guide useful learning, while contrastive methods lean heavily on carefully chosen augmentations that are especially hard to design for time series.

Narration: Self-supervised pre-training has transformed vision and language, and researchers naturally reached for the same tools when working with time series. But the fit is awkward. When you randomly mask points across a time series, you can shatter the smooth temporal structure that the signal depends on, sometimes making reconstruction so hard the model learns little. Contrastive learning has the opposite problem: comparing whole series for similarity tends to ignore the fine-grained correlations inside them, and it hinges on augmentations that are notoriously difficult to design for temporal data. The gap this paper addresses is clear: existing recipes fail to emphasize the temporal correlations that make time series what they are.
