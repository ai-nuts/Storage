## 01_title

DeepJoint is a robust survival model for clinical data. In medicine, when and which tests get ordered is itself informative — a phenomenon the authors call clinical presence. When these patterns shift, standard prediction models degrade. DeepJoint is a multi-task recurrent network that models three clinical-presence processes jointly with survival.

## 02_problem

Observational medical data arise from the interaction between patients and the healthcare system. A test's timing and its existence carry information about the patient. Most models ignore this, assuming sampling is non-informative — which yields sub-optimal, non-transportable models.

## 03_motivation

The same patient population appears differently under different observation processes, and that process shifts across countries, over time, and between weekdays and weekends. ML has studied covariate and label shift, but shift in the observation process itself is under-explored.

## 04_contribution

The paper contributes a deep joint model that treats clinical presence as multi-task learning. A shared recurrent embedding feeds four heads — longitudinal, inter-observation timing, missingness, and survival — trained together with dynamic weighting. The result encodes the observation process, giving a predictive edge and robustness.

## 05_method

An LSTM encodes each patient's irregular lab-test sequence into an embedding h. Three clinical-presence heads model next values (Gaussian), which tests appear (Bernoulli), and inter-observation timing. A DeepSurv head models survival under Cox proportional hazards. The four losses are combined by dynamic weighting, balanced by alpha, optimised end-to-end.

## 06_dataset_benchmark

Experiments use MIMIC-III, an intensive-care database of anonymised lab tests for over 38,000 patients. Restricting to those surviving the first 24 hours leaves 30,834 patients. Models predict in-hospital survival from the embedding at the last day-1 observation, scored by time-dependent C-index and Brier at 1 / 7 / 14 days.

## 07_key_result

On a random population split, the three proposed methods deliver competitive-to-best discrimination against same-input models. DeepJoint, seeing only lab values, already outperforms Ignore-LSTM and GRU-D. Modelling the observation process — even without feeding it in — yields a more predictive embedding. Fine-tuning reaches a 1-day C-index of 0.878.

## 08_ablation_study

The approach decomposes into three variants against six baselines. DeepJointFeature improves over plain DeepJoint and matches a strong feature baseline. The fine-tuned variant reaches the highest discrimination but overfits under shift. Across the robustness experiment, DeepJointFeature sits closest to the diagonal, transferring most reliably.

## 09_headline_numbers

The headline numbers: a concordance index of 0.878 at the one-day horizon, on a cohort of 30,834 MIMIC-III patients. DeepJoint jointly captures three dimensions of clinical presence — longitudinal, timing, and missingness — alongside survival, across horizons of one, seven, and fourteen days.

## 10_takeaway

The takeaway: the way clinical data are sampled is itself informative, and jointly modelling that observation process with survival produces predictions that are both more accurate and markedly more robust when clinical practice changes. Clinical presence is signal, not noise.
