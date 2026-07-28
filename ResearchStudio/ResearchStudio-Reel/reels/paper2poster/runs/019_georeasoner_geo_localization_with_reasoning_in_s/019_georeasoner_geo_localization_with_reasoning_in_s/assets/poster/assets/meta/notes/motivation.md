# Motivation

Core claim: Large vision-language models excel at joint visual and textual reasoning, and reasoning is known to boost model capability, so an LVLM augmented with human inference knowledge is a natural fit for interpretable geo-localization.

Supporting detail: Online geo-localization games like GeoGuessr and Tuxun contain rich, human-curated textual clues that encode exactly the domain knowledge a model needs but no prior street-view dataset provides in image-text pair form.

Narration: Why now, and why this approach? Large vision-language models have shown they can fuse images and text and follow step-by-step reasoning, and prior research shows that adding a reasoning process makes language models stronger. Meanwhile, a huge untapped resource exists: communities behind geo-localization games have spent years assembling textual clues that pinpoint countries and cities from subtle visual details. GeoReasoner's insight is to harvest that human inference knowledge and pair it with high-quality street views, so the model learns not just to guess a location but to justify it.
