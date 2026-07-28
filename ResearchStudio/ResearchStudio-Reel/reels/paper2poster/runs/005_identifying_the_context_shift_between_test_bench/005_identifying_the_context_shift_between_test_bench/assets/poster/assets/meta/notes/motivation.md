# Motivation

Core claim: Distribution shift is only a symptom of changes in how data are generated, not part of the generating process itself. The jargon is overlapping and confusing, and the literature around it is exploding.

Supporting detail: Papers combining "machine learning" with covariate shift, concept drift, distribution shift, and dataset shift rose sharply from 2012 to 2021 (Figure 1), yet the terms remain conflated.

Narration: Prior work treats robustness as a difference between two distributions while disregarding the reasons behind that difference. But the difference is merely a symptom; the disease is in how data are created, collected, and curated. As Figure 1 shows, interest in distribution shift terminology has grown enormously over the last decade, with covariate shift papers alone climbing toward nine thousand per year by 2021. Despite this volume, the vocabulary stays tangled and rarely points practitioners toward the upstream, semantically meaningful factors they can actually intervene on.
