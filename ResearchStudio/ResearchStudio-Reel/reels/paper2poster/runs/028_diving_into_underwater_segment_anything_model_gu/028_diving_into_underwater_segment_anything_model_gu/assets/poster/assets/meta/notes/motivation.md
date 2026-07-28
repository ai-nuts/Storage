# Motivation

Core claim: Foundation models like SAM show strong segmentation potential, but without underwater-specific adaptation and salient data they underperform on the domain, so both a dataset and an adapted architecture are needed.

Supporting detail: Prior salient instance datasets are small and class-agnostic, limiting both training and the study of multi-class underwater saliency.

Narration: With large models advancing, SAM has spread across computer vision, but using it underwater falls short. Its features do not adapt to murky, low-contrast water, and it needs manual foreground prompts that defeat automatic salient segmentation. The authors argue that unlocking SAM here requires two things at once: a large-scale dataset capturing underwater saliency, and an architecture that teaches SAM to see underwater and prompt itself. This paper delivers both.
