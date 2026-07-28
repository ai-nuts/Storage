---
title: Do You Remember? Overcoming Catastrophic Forgetting for Fake Audio Detection
authors: Xiaohui Zhang¹², Jiangyan Yi¹, Jianhua Tao³, Chenglong Wang¹⁴, Chuyuan Zhang¹
institutes: ¹Institute of Automation, Chinese Academy of Sciences; ²Beijing Jiaotong University; ³Tsinghua University; ⁴University of Science and Technology of China
venue: ICML 2023
paper_url: https://arxiv.org/abs/2308.03300
code_url: https://github.com/Cecile-hi/Regularized-Adaptive-Weight-Modification
title_audio_script: Fake audio detectors work well on the data they were trained on, but their accuracy collapses when they meet audio from a new dataset. Fine-tuning on the new data then makes them forget the old, a problem called catastrophic forgetting. This ICML 2023 paper introduces Regularized Adaptive Weight Modification, or RAWM, a continual learning method that adapts how it modifies network weights based on the ratio of genuine to fake utterances, and adds a regularization term so the model remembers the feature distribution of earlier datasets. Without replaying any past samples, RAWM cuts forgetting to roughly one tenth of naive fine-tuning and even generalizes beyond audio to speech emotion recognition and image recognition.
---

## Problem
**Necessary:** Fake audio detectors reach strong accuracy on their training dataset but degrade sharply on audio from a different dataset; naively fine-tuning on new data causes catastrophic forgetting of the old.
**Additional:** Prior cross-dataset fixes (ensemble learning, domain adaptation) need samples from the old dataset, which are often unavailable, for example when a released pre-trained model cannot be re-fine-tuned on the vendor's private data.
**Audio script:** Fake audio detection has become critical as speech synthesis and voice conversion produce human-like speech. Detectors perform well on their own dataset, but their equal error rate rises dramatically on audio from another dataset. The obvious fix, fine-tuning on the new data, causes the network to forget what it learned before. Earlier remedies require replaying old samples, which is impractical when the original data is inaccessible.

## Motivation
**Necessary:** Orthogonal Weight Modification (OWM) overcomes forgetting without replay but ignores that genuine audio often shares a similar feature distribution across datasets, wasting an exploitable regularity.
**Additional:** Conversely, a few datasets contain genuine audio recorded under very different acoustic conditions, so treating all classes identically skews the feature distribution and hurts retention.
**Audio script:** Existing weight-modification methods like OWM treat every input the same when constraining updates. But in fake audio detection, genuine speech tends to look similar from one dataset to the next, while the fake speech varies. That regularity is an opportunity: the direction of a weight update should adapt to how much of a batch is genuine versus fake. At the same time, some datasets collect genuine audio under acoustic conditions so different that a naive rule backfires, motivating an extra safeguard.

## Contribution
**Necessary:** The paper proposes RAWM, a replay-free continual learning method with two parts: adaptive weight modification that steers the update direction by the genuine-versus-fake ratio, and a regularization term that forces the model to remember the old inference distribution.
**Additional:** The method generalizes beyond fake audio detection to speech emotion recognition and image recognition (CLEAR benchmark), and is validated across four fake audio datasets averaged over seven runs.
**Audio script:** The authors contribute Regularized Adaptive Weight Modification. It has two essential steps. First, adaptive weight modification introduces an extra projector that adjusts the update direction according to the ratio of classes with similar feature distribution, such as genuine utterances, to the others. Second, a regularization term, inspired by learning without forgetting, keeps the new inference distribution close to the old one. The method needs no previous samples, and the authors show it transfers to speech emotion recognition and image recognition.

## Method
**Necessary:** RAWM builds on OWM's projector P (orthogonal to the subspace of previous inputs) and adds a second projector Q scaled by the genuine-to-fake ratio β; the final modification direction R combines normalized P and Q so updates adapt per batch while a distillation-style regularization preserves the old distribution.
**Additional:** Weights update as W ← W + R·G for new tasks, where G is the scaled back-prop gradient; the regularization replicates the pre-trained model into a frozen teacher and a fine-tuned student, matching softened softmax outputs via a modified cross-entropy loss weighted by coefficient η.
**Audio script:** RAWM starts from the orthogonal projector P of OWM, which points the update away from the subspace spanned by previous inputs. On top of it, the method builds a second projector Q that is orthogonal to P and scaled by the ratio beta of genuine to fake utterances in the batch. The two projectors are normalized and combined into a modified direction R, so when a batch is mostly genuine the update leans toward preserving old knowledge, and otherwise it leans toward learning the new data. For datasets recorded under very different conditions, a regularization term treats the frozen pre-trained model as a teacher and forces the fine-tuned student to match its softened outputs, remembering the old inference distribution. Crucially, none of this replays past samples.
**Key equation:** `$Q = \beta\,[\,I - P(P^{\top}P)^{-1}P\,]$`, `$R = P_{\text{norm}} + m\,Q_{\text{norm}}$`, `$\beta = \dfrac{N_g + 1}{N_f + 1}$`, `$L_{\text{reg}}(\hat{y}_o, \hat{y}_n) = -\,\hat{y}_o \cdot \log \hat{y}_n$`

## Dataset / Benchmark
**Necessary:** Four fake audio datasets are used in sequence, trained on ASVspoof2019LA (S) then fine-tuned on ASVspoof2015 (T1), VCC2020 (T2), and In-the-Wild (T3); performance is measured by Equal Error Rate (EER, %).
**Additional:** Generalization is tested on speech emotion recognition (MSP-Podcast → IEMOCAP, 4 emotions, accuracy) and image recognition (CLEAR-10 benchmark, 10 experiences, accuracy). Features come from a pre-trained Wav2vec 2.0 model for audio.
**Audio script:** Experiments run on four fake audio datasets in a continual-learning sequence: ASVspoof 2019 LA as the source, then ASVspoof 2015, the Voice Conversion Challenge 2020 set, and the In-the-Wild dataset. Each is a distinct acoustic and linguistic condition, with In-the-Wild being real-world deepfakes of public figures. Detection quality is reported as Equal Error Rate. To show breadth, the method is also evaluated on speech emotion recognition and on the CLEAR-10 image recognition benchmark.

## Key Result
**Necessary:** On sequence training between two datasets, RAWM's forgetting is one-tenth that of naive fine-tuning and its EER on the new dataset is half that of fine-tuning, beating EWC, LwF, OWM, and DFWF on both old and new sets.
**Additional:** For four-dataset sequence training at the best setting η = 0.50, RAWM reaches EER of 1.508 (S), 0.641 (T1), 3.850 (T2), 3.163 (T3), versus a baseline that degrades to 24.5 / 46.5 / 91.5 on T1/T2/T3.
**Audio script:** The headline finding is that RAWM cuts catastrophic forgetting to roughly one tenth of naive fine-tuning, while also halving the error on the new dataset. Across two-dataset and four-dataset sequences, it achieves the lowest equal error rate on both old and new datasets compared with mainstream continual learning methods including EWC, LwF, OWM, and the fake-audio-specific DFWF. With the regularization coefficient set to one half, giving equal attention to old and new data, RAWM keeps error low across all four datasets even as a baseline collapses.

## Ablation Study
**Necessary:** Removing regularization (–REG) or removing adaptive weight modification (–AWM) shows each part helps: adaptive modification dominates when feature distributions are similar or languages differ, while regularization dominates when acoustic conditions differ sharply.
**Additional:** In four-dataset sequence training, dropping adaptive modification (–REG to –AWM) degrades EER more than dropping regularization (RAWM to –REG), indicating adaptive weight modification is the larger contributor overall.
**Audio script:** An ablation separates the two components. When old and new datasets share a similar feature distribution, adaptive weight modification does most of the work, and removing it sharply raises error. When the datasets are recorded under very different conditions, the regularization term becomes the key to overcoming forgetting. Across the full four-dataset sequence, removing adaptive weight modification hurts more than removing regularization, so it is the primary driver, with regularization a valuable complement.

## Headline Numbers
**Necessary:** RAWM forgetting ≈ one-tenth of fine-tuning; new-dataset EER ≈ half of fine-tuning; best η = 0.50.
**Additional:** Few-sample (100 samples) two-dataset EER: RAWM 0.923 (S) / 0.312 (T1) vs Fine-tune 7.951 / 0.617 and DFWF 1.975 / 0.733. Speech emotion recognition accuracy: RAWM 41.995% (MSP-Podcast) / 54.229% (IEMOCAP), best among continual learning methods.
**Audio script:** In numbers: forgetting drops to about one tenth of fine-tuning, and new-dataset error to about one half. In the few-sample regime with only one hundred new samples, RAWM scores an equal error rate of zero point nine two on the old set and zero point three one on the new, far ahead of fine-tuning's near eight. On speech emotion recognition it reaches about forty-two percent accuracy on MSP-Podcast and fifty-four percent on IEMOCAP, the best of all continual learning methods tested. The optimal regularization weight is one half.

## Takeaway
**Necessary:** By adapting the weight-update direction to the genuine-versus-fake ratio and regularizing against the old distribution, RAWM overcomes catastrophic forgetting in fake audio detection without replaying any past data, and the idea transfers to other classification tasks.
**Additional:** The recipe is practical for released pre-trained detectors that cannot access their original training data.
**Audio script:** The takeaway is simple: you can teach a fake audio detector new datasets without it forgetting the old, and without keeping any of the old data around. RAWM does this by making the weight update adapt to how genuine-heavy each batch is and by regularizing the model to remember its previous behavior. Because the underlying regularity, some classes staying similar across datasets, appears in many problems, the same recipe extends to speech emotion recognition and image recognition.
