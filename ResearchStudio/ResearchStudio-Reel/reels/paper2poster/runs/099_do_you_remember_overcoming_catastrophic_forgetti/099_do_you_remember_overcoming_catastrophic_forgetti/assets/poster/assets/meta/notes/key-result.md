# Key Result

Core claim: On sequence training between two datasets, RAWM's forgetting is one-tenth that of naive fine-tuning and its EER on the new dataset is half that of fine-tuning, beating EWC, LwF, OWM, and DFWF on both old and new sets.

Supporting detail: For four-dataset sequence training at the best setting η = 0.50, RAWM reaches EER of 1.508 (S), 0.641 (T1), 3.850 (T2), 3.163 (T3), versus a baseline that degrades to 24.5 / 46.5 / 91.5 on T1/T2/T3.

Narration: The headline finding is that RAWM cuts catastrophic forgetting to roughly one tenth of naive fine-tuning, while also halving the error on the new dataset. Across two-dataset and four-dataset sequences, it achieves the lowest equal error rate on both old and new datasets compared with mainstream continual learning methods including EWC, LwF, OWM, and the fake-audio-specific DFWF. With the regularization coefficient set to one half, giving equal attention to old and new data, RAWM keeps error low across all four datasets even as a baseline collapses.
