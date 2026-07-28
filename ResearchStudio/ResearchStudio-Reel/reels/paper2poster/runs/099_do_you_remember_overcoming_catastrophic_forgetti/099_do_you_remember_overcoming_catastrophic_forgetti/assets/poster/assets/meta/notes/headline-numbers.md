# Headline Numbers

Core claim: RAWM forgetting ≈ one-tenth of fine-tuning; new-dataset EER ≈ half of fine-tuning; best η = 0.50.

Supporting detail: Few-sample (100 samples) two-dataset EER: RAWM 0.923 (S) / 0.312 (T1) vs Fine-tune 7.951 / 0.617 and DFWF 1.975 / 0.733. Speech emotion recognition accuracy: RAWM 41.995% (MSP-Podcast) / 54.229% (IEMOCAP), best among continual learning methods.

Narration: In numbers: forgetting drops to about one tenth of fine-tuning, and new-dataset error to about one half. In the few-sample regime with only one hundred new samples, RAWM scores an equal error rate of zero point nine two on the old set and zero point three one on the new, far ahead of fine-tuning's near eight. On speech emotion recognition it reaches about forty-two percent accuracy on MSP-Podcast and fifty-four percent on IEMOCAP, the best of all continual learning methods tested. The optimal regularization weight is one half.
