# Ablation Study

Core claim: Comparing variants: DeepJointFeature improves over DeepJoint and matches the feature-augmented baseline; DeepJointFineTune adds discriminative power but overfits under shift, while DeepJointFeature stays closest to the diagonal, best robustness with strong discrimination.

Supporting detail: Baselines span Last, Count, Ignore, Resample, Feature, and GRU-D, isolating the effect of each way of using (or ignoring) clinical presence.

Narration: The approach decomposes into three variants against six baselines. DeepJointFeature, which adds clinical-presence features to the joint model, improves over plain DeepJoint and matches a strong feature baseline. The fine-tuned variant reaches the highest population-level discrimination but overfits when the observation process shifts. Across the robustness experiment, DeepJointFeature best combines strong discrimination with proximity to the diagonal, transferring most reliably across settings.
