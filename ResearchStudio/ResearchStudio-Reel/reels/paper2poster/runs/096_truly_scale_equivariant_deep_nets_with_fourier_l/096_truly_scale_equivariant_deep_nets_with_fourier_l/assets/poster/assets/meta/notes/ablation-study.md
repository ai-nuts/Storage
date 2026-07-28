# Ablation Study

Core claim: Removing the consistency loss lowers both accuracy and scale-consistency at every training-set size (e.g. at 5k samples scale-consistency drops from 0.9296 to 0.9150; at 2.5k from 0.8906 to 0.8633), validating the loss.

Supporting detail: Frequency-domain non-linearities were also tried but empirically degraded classification, motivating the spatial-domain scale-equivariant non-linearity σ_s used instead.

Narration: An ablation isolates the consistency loss. Across training-set sizes of five thousand, twenty-five hundred, and one thousand samples, adding the consistency loss consistently improves both accuracy and the scale-consistency rate. For example, at five thousand samples the scale-consistency rises from ninety-one and a half percent to nearly ninety-three percent. This confirms that the hinge consistency loss is doing real work, encouraging the model to make better predictions as resolution increases. The authors also note that applying the non-linearity directly in the frequency domain, though equivariant, hurt classification, which is why they designed the spatial-domain scale-equivariant non-linearity.
