---
title: Self-supervised detection of atmospheric phenomena from remotely sensed synthetic aperture radar imagery
authors: Yannik Glaser¹, Peter Sadowski¹, Justin E. Stopa²
institutes: ¹Information and Computer Sciences, University of Hawai‘i at Mānoa; ²Ocean Engineering Department, University of Hawai‘i at Mānoa
venue: NeurIPS 2022
paper_url: https://ml4physicalsciences.github.io/2022/files/NeurIPS_ML4PS_2022_158.pdf
code_url:
title_audio_script: Satellite radar sees the ocean day and night, through any cloud cover, capturing wind streaks, convective cells, and other atmospheric signatures on the sea surface. But teaching machines to read these images is hard, because expert labels are scarce. This work asks whether self-supervised learning on three million unlabeled Sentinel-1 radar images can overcome that labeling bottleneck, and honestly reports what it found.
---

## Problem
**Necessary:** Machine learning on Sentinel-1 SAR ocean imagery is bottlenecked by sparse expert labels, and prior classifiers used biased, single-label datasets that misrepresent the true image population.
**Additional:** Labeling SAR vignettes requires trained experts, so datasets beyond a few thousand images are infeasible, limiting supervised deep learning for atmospheric phenomena detection.
**Audio script:** The European Space Agency's Sentinel-1 radar satellites image the global ocean at unprecedented scale, capturing waves, turbulence, fronts, and biological slicks. Computer vision can process these images, but machine learning has been held back by a lack of labeled data, since only trained experts can annotate radar vignettes. Earlier work also relied on a biased dataset that picked only exemplary images and forced a single label per image, even though multiple phenomena usually coexist. The result was a training set that did not reflect the real distribution of ocean conditions.

## Motivation
**Necessary:** Self-supervised contrastive learning can exploit vast unlabeled imagery to build reusable embeddings, and has never been widely tested on remote-sensing SAR data despite its success on natural and medical images.
**Additional:** Sentinel-1 collects nearly 120,000 Wave-mode images every month, an enormous unlabeled resource that contrastive learning could turn into a strong SAR representation.
**Audio script:** Contrastive self-supervised learning has transformed computer vision by training networks on huge pools of unlabeled data to produce embeddings that transfer well to downstream tasks. It has worked for natural images and medical images, but has rarely been applied to remote sensing. That gap matters here, because Sentinel-1 alone collects roughly a hundred and twenty thousand Wave-mode ocean images every single month. This study tests the hypothesis that contrastive learning on that unlabeled stream can overcome the scarcity of expert labels for SAR analysis.

## Contribution
**Necessary:** The authors compile a new unbiased, multi-label, expert-annotated SAR dataset, apply the SwAV contrastive framework to three million unlabeled Sentinel-1 images, and benchmark self-supervised embeddings against ImageNet transfer learning and the prior CmWV model.
**Additional:** They evaluate the learned representation under three protocols (weighted kNN, linear evaluation, and full fine-tuning) to isolate the value of self-supervised pretraining.
**Audio script:** This paper makes three contributions. First, it builds a new hand-labeled dataset of about twenty-three hundred randomly sampled, multi-label radar observations that better represents the real ocean population. Second, it leverages three years of unlabeled Sentinel-1 imagery, roughly three million images, to train a SwAV contrastive embedding of SAR scenes. Third, it rigorously compares that self-supervised representation against standard transfer learning from ImageNet and against the previous state-of-the-art CmWV classifier, using three different downstream evaluation protocols.

## Method
**Necessary:** A ResNet-50 backbone is pretrained with SwAV, a clustering-based contrastive framework that predicts swapped cluster assignments between augmented views and works with modest batch sizes via a feature queue. The embedding is then evaluated by weighted kNN, linear probing, and end-to-end fine-tuning on the labeled stability-classification task.
**Additional:** SwAV was trained with batch size 1024 across eight NVIDIA V100 32GB GPUs, a queue of 16 batches, 1000 cluster centroids, for 65 epochs over about 10 days. Fine-tuning ran on a single V100 with batch size 128.
**Audio script:** The core method is SwAV, a contrastive framework that assigns image representations to clusters and trains the network to predict the cluster assignment of one augmented view from another. Unlike methods such as SimCLR, SwAV avoids prohibitively large batches by storing recent cluster assignments in a queue. The authors train a standard ResNet-50 backbone with SwAV using a batch size of one thousand twenty-four across eight V100 GPUs, a queue of sixteen batches, and one thousand cluster centroids, stopping after sixty-five epochs and about ten days of compute. To measure representation quality, they use three downstream protocols: a weighted k-nearest-neighbor classifier, a linear evaluation that freezes the backbone and trains a single softmax layer, and full end-to-end fine-tuning of all weights on the labeled data.

## Dataset / Benchmark
**Necessary:** The unlabeled pretraining set holds 2,943,550 Sentinel-1 A/B Wave-mode images from 2017-2019 (each 20 km × 20 km at 5 m resolution). The labeled benchmark has 2,300 expert-consensus, multi-label vignettes over four classes, MC, WS, NV, and OT, split 60/20/20 for train, validation, and test.
**Additional:** Images are freely available from ESA's Sentinel Open Access Hub with no licensing restrictions; unlabeled images are zero-padded to 450×450 pixels with no further preprocessing.
**Audio script:** Two datasets drive the study. The pretraining pool is nearly three million unlabeled Wave-mode images from Sentinel-1 A and B over 2017 to 2019, each covering a twenty by twenty kilometer patch of ocean at five meter resolution, ninety percent used for training and ten percent held out for validation. The labeled benchmark contains twenty-three hundred vignettes annotated by experts into a consensus multi-label ground truth across four classes: mesoscale convection cells, wind streaks, negligible variability, and other. This set is stratified and split sixty, twenty, twenty into training, validation, and held-out test data.

## Key Result
**Necessary:** Fine-tuned models achieve a best micro-averaged AUROC of 0.93, and both the contrastive and ImageNet models dramatically outperform the previous CmWV classifier on the wind-streak and convection-cell classes.
**Additional:** On WS, fine-tuned SwAV reaches 0.831 and ImageNet 0.850 versus CmWV's 0.727; on MC, 0.872 and 0.873 versus 0.793; the three models tie on NV around 0.95.
**Audio script:** The headline result is that fine-tuned models reach a best micro-averaged area under the ROC curve of about zero point nine three. Both the contrastive and the ImageNet-pretrained models comfortably beat the earlier CmWV classifier on the two hardest atmospheric classes. For wind streaks, the new models score in the mid eighties compared with CmWV's zero point seven three, and for convection cells they reach about zero point eight seven versus zero point seven nine. On the negligible-variability class, all three models perform about equally well, near zero point nine five.

## Ablation Study
**Necessary:** Comparing evaluation protocols, contrastive weights beat ImageNet weights slightly under kNN (0.864 vs 0.859) and linear evaluation (0.841 vs 0.836), but this reverses under full fine-tuning, where ImageNet edges ahead (0.931 vs 0.929).
**Additional:** The advantage of self-supervised pretraining only appears when the backbone is frozen; once all weights are fine-tuned, the initialization barely matters.
**Audio script:** The most informative comparison is across the three evaluation protocols. When the backbone is frozen, the self-supervised contrastive weights hold a small edge, scoring zero point eight six four versus zero point eight five nine under nearest-neighbor classification and zero point eight four one versus zero point eight three six under linear evaluation. But once all weights are fine-tuned end to end, that gap not only disappears but slightly reverses, with the ImageNet initialization reaching zero point nine three one against the contrastive model's zero point nine two nine. In other words, the benefit of self-supervised pretraining vanishes once the whole network is allowed to adapt.

## Headline Numbers
**Necessary:**
- 0.93 best micro-averaged AUROC (fine-tuned model)
- ~3 million (2,943,550) unlabeled Sentinel-1 images for contrastive pretraining
- 2,300 expert-labeled, multi-label vignettes across 4 classes
- WS AUROC 0.831-0.850 vs CmWV 0.727; MC 0.872-0.873 vs 0.793
**Additional:** SwAV trained 65 epochs / ~10 days on 8× V100 GPUs; images 20×20 km at 5 m resolution.
**Audio script:** A few numbers capture the study. Self-supervised training used almost three million unlabeled radar images. The labeled benchmark held twenty-three hundred expert vignettes across four classes. The best fine-tuned model reached a micro-averaged AUROC of about zero point nine three. And on the toughest classes, wind streaks and convection cells, the new models jumped from CmWV's roughly zero point seven three and zero point seven nine into the mid eighties, a substantial detection improvement.

## Takeaway
**Necessary:** Self-supervised contrastive pretraining on massive unlabeled SAR imagery matches but does not beat plain ImageNet transfer learning here, though both yield a large jump over the prior state of the art for detecting ocean-surface atmospheric phenomena.
**Additional:** The authors caution these are preliminary results; longer training, better hyperparameters, and remote-sensing-specific pretext tasks may yet unlock self-supervised gains.
**Audio script:** The honest takeaway is that self-supervised contrastive learning, at least in this preliminary study, offers only marginal gains over simply transferring features from a model trained on natural images, while costing far more compute. Yet both approaches deliver a dramatic improvement over the previous state-of-the-art classifier for reading atmospheric phenomena from ocean radar. The authors argue the idea still holds promise, and that longer training, better tuning, and pretext tasks designed for remote sensing deserve exploration before drawing final conclusions.
