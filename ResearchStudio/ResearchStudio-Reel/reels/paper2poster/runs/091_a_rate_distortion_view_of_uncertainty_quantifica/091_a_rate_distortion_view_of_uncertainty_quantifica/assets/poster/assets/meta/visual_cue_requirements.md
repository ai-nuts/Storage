# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_presented_icml_2024_introduces_dista`

- Preferred role: `method`
- Cue keywords: `presented, icml, 2024, introduces, distance, aware, bottleneck, new, way, give`
- Narration: This paper, presented at ICML 2024, introduces the Distance Aware Bottleneck, a new way to give deep neural networks the sense of "knowing what they don't know." The authors reframe uncertainty quantification as a rate-distortion problem: the network learns a compact codebook that summarizes its training data, and the distance of a new input from that codebook becomes a principled uncertainty score, computed in a single forward pass.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_presented_icml_2024_introduces_dista" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords presented, icml, 2024, introduces, distance, aware in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_trustworthy_should_know_when_operati`

- Preferred role: `content`
- Cue keywords: `trustworthy, should, know, when, operating, far, what, seen`
- Narration: A trustworthy model should know when it is operating far from what it has seen.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_trustworthy_should_know_when_operati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trustworthy, should, know, when, operating, far in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_deep_neural_networks_however_often`

- Preferred role: `method`
- Cue keywords: `deep, neural, networks, however, often, make, confident, predictions, even, inputs`
- Narration: Deep neural networks, however, often make confident predictions even on inputs that are wildly different from their training data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_deep_neural_networks_however_often" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deep, neural, networks, however, often, make in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_classical_probabilistic_models_such`

- Preferred role: `method`
- Cue keywords: `classical, probabilistic, models, such, gaussian, processes, built-in, sense, distance, set`
- Narration: Classical probabilistic models such as Gaussian Processes have a built-in sense of distance from the training set, but standard deep networks do not, and reliable, efficient uncertainty estimation for real deployments remains an open problem.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_classical_probabilistic_models_such" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords classical, probabilistic, models, such, gaussian, processes in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_today_fast_single_forward_pass_uncer`

- Preferred role: `method`
- Cue keywords: `today, fast, single-forward-pass, uncertainty, methods, usually, depend, special, architectural, tricks`
- Narration: Today's fast, single-forward-pass uncertainty methods usually depend on special architectural tricks, like spectral normalization, to stop the network's features from collapsing.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_today_fast_single_forward_pass_uncer" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords today, fast, single-forward-pass, uncertainty, methods, usually in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_those_constraints_quietly_damage_cal`

- Preferred role: `method`
- Cue keywords: `those, constraints, quietly, damage, calibration, awkward, bolt, onto, large, pre-trained`
- Narration: Those constraints can quietly damage calibration and are awkward to bolt onto large pre-trained models.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_those_constraints_quietly_damage_cal" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords those, constraints, quietly, damage, calibration, awkward in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_alternative_deep_ensembles_bayesian`

- Preferred role: `content`
- Cue keywords: `alternative, deep, ensembles, bayesian, networks, naturally, distance-aware, but, require, many`
- Narration: The alternative, deep ensembles and Bayesian networks, are naturally distance-aware but require many forward passes, which is expensive at scale.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_alternative_deep_ensembles_bayesian" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords alternative, deep, ensembles, bayesian, networks, naturally in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_authors_ask_whether_single_determini`

- Preferred role: `content`
- Cue keywords: `authors, ask, whether, single, deterministic, distance-aware, without, these, drawbacks`
- Narration: The authors ask whether a single deterministic model can be distance-aware without these drawbacks.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_authors_ask_whether_single_determini" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, ask, whether, single, deterministic, distance-aware in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_their_key_idea_view_uncertainty`

- Preferred role: `content`
- Cue keywords: `their, key, idea, view, uncertainty, quantification, through, lens, rate-distortion, theory`
- Narration: Their key idea is to view uncertainty quantification through the lens of rate-distortion theory.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_their_key_idea_view_uncertainty" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords their, key, idea, view, uncertainty, quantification in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_they_compress_entire_set_small`

- Preferred role: `method`
- Cue keywords: `they, compress, entire, set, small, codebook, prototype, distributions, measure, how`
- Narration: They compress the entire training set into a small codebook of prototype distributions, and measure how far a new input is from that codebook.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_they_compress_entire_set_small" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, compress, entire, set, small, codebook in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_gives_distance_aware_bottleneck_dab`

- Preferred role: `method`
- Cue keywords: `gives, distance, aware, bottleneck, dab, single, deterministic, produces, uncertainty, one`
- Narration: This gives the Distance Aware Bottleneck, or DAB: a single deterministic model that produces uncertainty in one forward pass.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_gives_distance_aware_bottleneck_dab" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gives, distance, aware, bottleneck, dab, single in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_along_way_they_contribute_practical`

- Preferred role: `method`
- Cue keywords: `along, way, they, contribute, practical, alternating-minimization, algorithm, meta-probabilistic, distortion, operates`
- Narration: Along the way they contribute a practical alternating-minimization training algorithm, a meta-probabilistic distortion that operates over distributions of embeddings, and a post-hoc variant that adds distance awareness to large pre-trained feature extractors.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_along_way_they_contribute_practical" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords along, way, they, contribute, practical, alternating-minimization in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_dab_builds_information_bottleneck_fr`

- Preferred role: `method`
- Cue keywords: `dab, builds, information, bottleneck, framework, but, replaces, its, rate, term`
- Narration: DAB builds on the Information Bottleneck framework but replaces its rate term with an achievable rate borrowed from rate-distortion theory with finite cardinality.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_dab_builds_information_bottleneck_fr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dab, builds, information, bottleneck, framework, but in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_concretely_learns_codebook_centroid`

- Preferred role: `method`
- Cue keywords: `concretely, learns, codebook, centroid, distributions, quantize, encoders, all, points, uncertainty`
- Narration: Concretely, the model learns a codebook of centroid distributions that quantize the encoders of all training points. The uncertainty of a new example is simply its expected statistical distance, here the Kullback-Leibler divergence, from that codebook.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_concretely_learns_codebook_centroid" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords concretely, learns, codebook, centroid, distributions, quantize in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_alternates_between_gradient_updates`

- Preferred role: `method`
- Cue keywords: `alternates, between, gradient, updates, encoder, decoder, cheap, analytic, updates, soft`
- Narration: Training alternates between gradient updates of the encoder and decoder and cheap analytic updates of the soft assignments and centroids, echoing the classic Blahut-Arimoto algorithm.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_alternates_between_gradient_updates" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords alternates, between, gradient, updates, encoder, decoder in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_result_closely_analogous_gaussian_pr`

- Preferred role: `result`
- Cue keywords: `result, closely, analogous, gaussian, process, where, codebook, plays, role, inducing`
- Narration: The result is closely analogous to a Gaussian Process, where the codebook plays the role of inducing points and statistical distance replaces Euclidean distance.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c4_result_closely_analogous_gaussian_pr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, closely, analogous, gaussian, process, where in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_method_tested_across_several_setting`

- Preferred role: `method`
- Cue keywords: `method, tested, across, several, settings`
- Narration: The method is tested across several settings.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_method_tested_across_several_setting" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, tested, across, several, settings in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_cifar_10_in_distribution_svhn_serves`

- Preferred role: `method`
- Cue keywords: `cifar-10, in-distribution, svhn, serves, far, out-of-distribution, set, cifar-100, harder, near`
- Narration: On CIFAR-10 as the in-distribution data, SVHN serves as a far out-of-distribution set and CIFAR-100 as a harder near out-of-distribution set.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_cifar_10_in_distribution_svhn_serves" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-10, in-distribution, svhn, serves, far, out-of-distribution in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_authors_also_study_misclassification`

- Preferred role: `method`
- Cue keywords: `authors, also, study, misclassification, prediction, cifar-10, scale, imagenet-1k, imagenet-o, out-of-distribution`
- Narration: The authors also study misclassification prediction on CIFAR-10 and scale up to ImageNet-1K with ImageNet-O as the out-of-distribution set.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_authors_also_study_misclassification" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, also, study, misclassification, prediction, cifar-10 in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_notably_dab_works_very_narrow`

- Preferred role: `method`
- Cue keywords: `notably, dab, works, very, narrow, eight-dimensional, latent, bottleneck, just, ten`
- Narration: Notably, DAB works with a very narrow eight-dimensional latent bottleneck and just ten distributional codes, and is compared against strong baselines including deep ensembles, DDU, DUQ, DUE, SNGP, and the vanilla variational Information Bottleneck.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_notably_dab_works_very_narrow" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords notably, dab, works, very, narrow, eight-dimensional in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_result_dab_outperforms_ever`

- Preferred role: `method`
- Cue keywords: `headline, result, dab, outperforms, every, baseline, both, out-of-distribution, tasks`
- Narration: The headline result is that DAB outperforms every baseline on both out-of-distribution tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_headline_result_dab_outperforms_ever" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, result, dab, outperforms, every, baseline in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_trained_cifar_10_reaches_auroc_0_986`

- Preferred role: `method`
- Cue keywords: `trained, cifar-10, reaches, auroc, 0.986, auprc, 0.994, against, svhn, auroc`
- Narration: Trained on CIFAR-10, it reaches an AUROC of 0.986 and AUPRC of 0.994 against SVHN, and an AUROC of 0.922 and AUPRC of 0.915 against the harder CIFAR-100, beating even a five-model deep ensemble.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_trained_cifar_10_reaches_auroc_0_986" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trained, cifar-10, reaches, auroc, 0.986, auprc in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_crucially_does_single_forward_pass`

- Preferred role: `result`
- Cue keywords: `crucially, does, single, forward, pass, about, thirty-six, half, million, parameters`
- Narration: Crucially, it does this in a single forward pass with about thirty-six and a half million parameters, versus the ensemble's roughly one hundred and eighty-two million, while keeping accuracy on par at about ninety-six percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_crucially_does_single_forward_pass" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, does, single, forward, pass, about in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_task_predicting_its_own_mistakes`

- Preferred role: `result`
- Cue keywords: `task, predicting, its, own, mistakes, cifar-10, dab, reaches, calibration, auroc`
- Narration: On the task of predicting its own mistakes on CIFAR-10, DAB reaches a calibration AUROC of 0.930.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c1_task_predicting_its_own_mistakes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords task, predicting, its, own, mistakes, cifar-10 in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_nearly_closes_gap_deep_ensemble`

- Preferred role: `method`
- Cue keywords: `nearly, closes, gap, deep, ensemble, 0.951, while, dramatically, outperforming, other`
- Narration: That nearly closes the gap to a deep ensemble at 0.951, while dramatically outperforming other single-pass deterministic methods such as DDU at 0.632, DUE at 0.856, DUQ at 0.889, and SNGP at 0.897.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_nearly_closes_gap_deep_ensemble" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords nearly, closes, gap, deep, ensemble, 0.951 in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_visualization_learned_codebook_furth`

- Preferred role: `method`
- Cue keywords: `visualization, learned, codebook, further, shows, ten, centroids, progressively, attracting, test`
- Narration: A visualization of the learned codebook further shows each of the ten centroids progressively attracting test points of a single class as training proceeds, confirming that the codes capture meaningful structure in the data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_visualization_learned_codebook_furth" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords visualization, learned, codebook, further, shows, ten in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_summarize_numbers_cifar_10_dab_achie`

- Preferred role: `result`
- Cue keywords: `summarize, numbers, cifar-10, dab, achieves, best-in-class, ood, auroc, 0.986, against`
- Narration: To summarize the numbers: on CIFAR-10, DAB achieves a best-in-class OOD AUROC of 0.986 against SVHN and 0.922 against CIFAR-100, and a misclassification calibration AUROC of 0.930.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_summarize_numbers_cifar_10_dab_achie" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords summarize, numbers, cifar-10, dab, achieves, best-in-class in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_imagenet_scale_dab_built_fine_tuned`

- Preferred role: `method`
- Cue keywords: `imagenet, scale, dab, built, fine-tuned, resnet-50, beats, five-model, ensemble, misclassification`
- Narration: At ImageNet scale, DAB built on a fine-tuned ResNet-50 beats a five-model ensemble on misclassification, 0.868 versus 0.861, and on out-of-distribution detection against ImageNet-O, 0.743 versus 0.642, all while using far fewer trainable parameters, roughly thirty-six million versus one hundred and eighteen million.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_imagenet_scale_dab_built_fine_tuned" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords imagenet, scale, dab, built, fine-tuned, resnet-50 in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_recasting_uncertainty_probl`

- Preferred role: `method`
- Cue keywords: `takeaway, recasting, uncertainty, problem, compressing, learned, codebook, gives, single, deterministic`
- Narration: The takeaway is that recasting uncertainty as the problem of compressing training data into a learned codebook gives a single deterministic network a genuine sense of distance from what it has seen, letting it match or beat expensive ensembles at a fraction of the cost.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_takeaway_recasting_uncertainty_probl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, recasting, uncertainty, problem, compressing, learned in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_because_notion_distance_statistical`

- Preferred role: `method`
- Cue keywords: `because, notion, distance, statistical, rather, geometric, dab, offers, unified, gaussian-process-like`
- Narration: Because the notion of distance is statistical rather than geometric, DAB offers a unified, Gaussian-Process-like view of uncertainty that works for both classification and regression, and can even be attached after the fact to large pre-trained models.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_because_notion_distance_statistical" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, notion, distance, statistical, rather, geometric in title/desc so the matcher can verify semantic overlap.
