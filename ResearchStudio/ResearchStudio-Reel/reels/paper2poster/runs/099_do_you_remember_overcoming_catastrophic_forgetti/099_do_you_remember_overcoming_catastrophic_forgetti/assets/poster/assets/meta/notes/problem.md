# Problem

Core claim: Fake audio detectors reach strong accuracy on their training dataset but degrade sharply on audio from a different dataset; naively fine-tuning on new data causes catastrophic forgetting of the old.

Supporting detail: Prior cross-dataset fixes (ensemble learning, domain adaptation) need samples from the old dataset, which are often unavailable, for example when a released pre-trained model cannot be re-fine-tuned on the vendor's private data.

Narration: Fake audio detection has become critical as speech synthesis and voice conversion produce human-like speech. Detectors perform well on their own dataset, but their equal error rate rises dramatically on audio from another dataset. The obvious fix, fine-tuning on the new data, causes the network to forget what it learned before. Earlier remedies require replaying old samples, which is impractical when the original data is inaccessible.
