# Contribution

Core claim: The paper (1) presents a new paradigm that pairs an LVLM with human inference knowledge from geo-localization games for geo-localization with reasoning, (2) introduces the concept of locatability and a CLIP-based network to quantify it, and (3) proposes GeoReasoner, an LVLM that outperforms existing geo-localization models while providing explanations.

Supporting detail: Together these yield a curated dataset of over 70K highly locatable geo-tagged street views plus 3K reasoned text-image pairs, and a two-stage fine-tuning recipe (reasoning tuning then location tuning) built on Qwen-VL with stacked LoRA adapters.

Narration: The work makes three contributions. It introduces a new paradigm that leverages a large vision-language model together with external human reasoning knowledge learned from online games, enabling geo-localization that comes with an explanation. It defines the concept of locatability, a metric for how findable an image's location is, and builds a CLIP-based network to compute it, which drives the curation of a clean, high-quality training set. And it delivers GeoReasoner itself, a model that beats existing geo-localization systems while offering detailed reasoning for every prediction.
