# Problem

Core claim: CNNs exploit color for recognition but fail under train-test color distribution shifts; color invariance fixes robustness only by discarding all color, sacrificing discriminative power.

Supporting detail: Balanced training data covering every color variation is impossible due to the long tail of real-world appearance, so underrepresented colors are systematically misclassified.

Narration: Convolutional neural networks lean heavily on color to recognize objects, but real-world data rarely contains every color a class can take. When a model trained mostly on red cars sees a blue one, accuracy collapses. The classic remedy, color invariance, sidesteps the problem by removing color entirely, but that throws away a genuinely useful signal. The paper frames the real challenge as keeping color information while still generalizing across colors that were rare or absent during training.
