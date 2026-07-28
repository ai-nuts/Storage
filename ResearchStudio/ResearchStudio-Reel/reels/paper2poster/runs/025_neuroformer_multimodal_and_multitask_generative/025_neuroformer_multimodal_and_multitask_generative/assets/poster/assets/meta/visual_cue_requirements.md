# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_neuroformer_multimodal_multitask_gen`

- Preferred role: `method`
- Cue keywords: `neuroformer, multimodal, multitask, generative, pretrained, transformer, brain, built, santa, barbara`
- Narration: Neuroformer is a multimodal, multitask generative pretrained transformer for brain data, built at UC Santa Barbara.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_neuroformer_multimodal_multitask_gen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords neuroformer, multimodal, multitask, generative, pretrained, transformer in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_reframes_cellular_resolution_spike_a`

- Preferred role: `figure`
- Cue keywords: `reframes, cellular-resolution, spike, analysis, autoregressive, spatiotemporal, generation, borrowing, recipe, behind`
- Narration: It reframes cellular-resolution spike analysis as autoregressive spatiotemporal generation, borrowing the recipe behind large language and vision models.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c2_reframes_cellular_resolution_spike_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reframes, cellular-resolution, spike, analysis, autoregressive, spatiotemporal in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_trained_self_supervised_recovers_cir`

- Preferred role: `method`
- Cue keywords: `trained, self-supervised, recovers, circuit, connectivity, decodes, mouse, behavior`
- Narration: Trained self-supervised, it recovers circuit connectivity and decodes mouse behavior.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_trained_self_supervised_recovers_cir" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trained, self-supervised, recovers, circuit, connectivity, decodes in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_modern_neuroscience_records_thousand`

- Preferred role: `content`
- Cue keywords: `modern, neuroscience, records, thousands, neurons, cellular, resolution, alongside, visual, stimuli`
- Narration: Modern neuroscience records thousands of neurons at cellular resolution, alongside visual stimuli and behavior.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_modern_neuroscience_records_thousand" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords modern, neuroscience, records, thousands, neurons, cellular in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_these_datasets_large_multimodal_mess`

- Preferred role: `figure`
- Cue keywords: `these, datasets, large, multimodal, messy, yet, field, traditional, statistical, tools`
- Narration: These datasets are large, multimodal, and messy, yet the field's traditional statistical tools were built for far smaller, single-modality recordings, leaving a widening data-analysis gap.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s02_c2_these_datasets_large_multimodal_mess" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, datasets, large, multimodal, messy, yet in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_large_pretrained_models_vision_langu`

- Preferred role: `method`
- Cue keywords: `large, pretrained, models, vision, language, point, way, forward, they, learn`
- Narration: Large pretrained models in vision and language point a way forward: they learn general representations self-supervised from raw data, then transfer with little labeling.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_large_pretrained_models_vision_langu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords large, pretrained, models, vision, language, point in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_authors_ask_whether_reframing_spike`

- Preferred role: `figure`
- Cue keywords: `authors, ask, whether, reframing, spike, analysis, generative, prediction, likewise, scale`
- Narration: The authors ask whether reframing spike analysis as generative prediction can likewise scale, fuse modalities, and transfer to behavior decoding.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s03_c2_authors_ask_whether_reframing_spike" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, ask, whether, reframing, spike, analysis in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_neuroformer_makes_four_contributions`

- Preferred role: `figure`
- Cue keywords: `neuroformer, makes, four, contributions, reframes, spike, analysis, self-supervised, autoregressive, generation`
- Narration: Neuroformer makes four contributions. It reframes spike analysis as self-supervised autoregressive generation, needing no labels.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c1_neuroformer_makes_four_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords neuroformer, makes, four, contributions, reframes, spike in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_its_cross_attention_scales_linearly`

- Preferred role: `method`
- Cue keywords: `its, cross-attention, scales, linearly, feature, size, fuses, many, modalities`
- Narration: Its cross-attention scales linearly with feature size and fuses many modalities.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_its_cross_attention_scales_linearly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, cross-attention, scales, linearly, feature, size in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_simulated_its_attention_maps_recover`

- Preferred role: `method`
- Cue keywords: `simulated, its, attention, maps, recover, directed, connectivity, including, hub, neurons`
- Narration: On simulated data, its attention maps recover directed connectivity, including hub neurons correlation misses.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_simulated_its_attention_maps_recover" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords simulated, its, attention, maps, recover, directed in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_pretrained_decodes_behavior_few_shot`

- Preferred role: `method`
- Cue keywords: `pretrained, decodes, behavior, few-shot, fine-tuning`
- Narration: Pretrained, it decodes behavior with few-shot fine-tuning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_pretrained_decodes_behavior_few_shot" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pretrained, decodes, behavior, few-shot, fine-tuning in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_neuroformer_treats_spike_token_split`

- Preferred role: `content`
- Cue keywords: `neuroformer, treats, spike, token, splitting, activity, current, past, states`
- Narration: Neuroformer treats each spike as a token, splitting activity into Current and Past States.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_neuroformer_treats_spike_token_split" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords neuroformer, treats, spike, token, splitting, activity in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_video_becomes_patches_via_3`

- Preferred role: `method`
- Cue keywords: `video, becomes, patches, via, 3, d-convolutional, encoder, behavior, forms, separate`
- Narration: Video becomes patches via a 3D-convolutional encoder; behavior forms a separate stream. A contrastive module aligns neural, visual, and behavioral features.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_video_becomes_patches_via_3" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords video, becomes, patches, via, 3, d-convolutional in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_cross_attention_fuses_current_state`

- Preferred role: `method`
- Cue keywords: `cross-attention, fuses, current, state, larger, feature, arrays, cutting, attention, cost`
- Narration: Cross-attention fuses the Current State with larger feature arrays, cutting attention cost from quadratic to linear.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_cross_attention_fuses_current_state" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cross-attention, fuses, current, state, larger, feature in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_causally_masked_decoder_predicts_whi`

- Preferred role: `method`
- Cue keywords: `causally, masked, decoder, predicts, which, neuron, fires, its, time, bin`
- Narration: A causally masked decoder predicts which neuron fires and its time bin.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_causally_masked_decoder_predicts_whi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords causally, masked, decoder, predicts, which, neuron in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_validation_spans_two_levels`

- Preferred role: `content`
- Cue keywords: `validation, spans, two, levels`
- Narration: Validation spans two levels.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_validation_spans_two_levels" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords validation, spans, two, levels in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_first_simulated_spiking_network_thre`

- Preferred role: `content`
- Cue keywords: `first, simulated, spiking, network, three, hub, neurons, gives, ground-truth, connectivity`
- Narration: First, a simulated spiking network with three hub neurons gives a ground-truth connectivity matrix.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_first_simulated_spiking_network_thre" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, simulated, spiking, network, three, hub in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_second_two_photon_calcium_imaging_mo`

- Preferred role: `content`
- Cue keywords: `second, two-photon, calcium, imaging, mouse, visual, cortex, records, 386, neurons`
- Narration: Second, two-photon calcium imaging of mouse visual cortex records 386 neurons across V1 and AL viewing gratings and natural videos, plus a virtual-navigation dataset pairing activity with running speed.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_second_two_photon_calcium_imaging_mo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, two-photon, calcium, imaging, mouse, visual in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_simulated_network_neuroformer_attent`

- Preferred role: `method`
- Cue keywords: `simulated, network, neuroformer, attention, reveals, directed, connectivity, identifies, hub, neurons`
- Narration: On the simulated network, Neuroformer's attention reveals directed connectivity and identifies the hub neurons, which plain correlation misses for lack of directionality.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_simulated_network_neuroformer_attent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords simulated, network, neuroformer, attention, reveals, directed in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_real_cortex_reproduces_responses_gra`

- Preferred role: `content`
- Cue keywords: `real, cortex, reproduces, responses, gratings, natural, videos, population, predictions, significantly`
- Narration: On real cortex, it reproduces responses to gratings and natural videos, with population predictions significantly beating a GLM, p around 0.02.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_real_cortex_reproduces_responses_gra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords real, cortex, reproduces, responses, gratings, natural in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_fine_tuned_decode_running_reaches_pe`

- Preferred role: `result`
- Cue keywords: `fine-tuned, decode, running, reaches, pearson, correlations, 0.97`
- Narration: Fine-tuned to decode running, it reaches Pearson correlations up to 0.97.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_fine_tuned_decode_running_reaches_pe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fine-tuned, decode, running, reaches, pearson, correlations in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablation_removes_components_one_time`

- Preferred role: `method`
- Cue keywords: `ablation, removes, components, one, time, current, state, past, state, video`
- Narration: An ablation removes components one at a time: the Current State, Past State, video stream, behavior stream, and contrastive objective each add measurable predictive power.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_ablation_removes_components_one_time" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablation, removes, components, one, time, current in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_two_findings_stand_out`

- Preferred role: `content`
- Cue keywords: `two, findings, stand, out`
- Narration: Two findings stand out.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_two_findings_stand_out" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, findings, stand, out in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_jointly_neural_responses_behavior_be`

- Preferred role: `method`
- Cue keywords: `jointly, neural, responses, behavior, beats, either, alone, contrastive, objective, helps`
- Narration: Jointly training on neural responses and behavior beats either alone, and the contrastive objective helps most when data is scarce.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_jointly_neural_responses_behavior_be" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords jointly, neural, responses, behavior, beats, either in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_behavior_prediction_neuroformer_reac`

- Preferred role: `result`
- Cue keywords: `behavior, prediction, neuroformer, reaches, pearson, correlation, 0.97, versus, about, 0.73`
- Narration: For behavior prediction, Neuroformer reaches Pearson correlation up to 0.97, versus about 0.73 for Lasso.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_behavior_prediction_neuroformer_reac" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords behavior, prediction, neuroformer, reaches, pearson, correlation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_few_shot_pretrained_fine_tuned_just`

- Preferred role: `method`
- Cue keywords: `few-shot, pretrained, fine-tuned, just, 1, behavior, hits, 0.51, beating, non-pretrained`
- Narration: Few-shot, a model pretrained and fine-tuned on just 1% of behavior data hits 0.51, beating a non-pretrained model given 10%, which reaches only 0.33.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_few_shot_pretrained_fine_tuned_just" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few-shot, pretrained, fine-tuned, just, 1, behavior in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_its_largest_models_scale_roughly`

- Preferred role: `content`
- Cue keywords: `its, largest, models, scale, roughly, 100, million, parameters`
- Narration: Its largest models scale to roughly 100 million parameters.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_its_largest_models_scale_roughly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, largest, models, scale, roughly, 100 in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_pretraining_paradigm_reshap`

- Preferred role: `method`
- Cue keywords: `takeaway, pretraining, paradigm, reshaped, vision, language, also, work, brain`
- Narration: The takeaway: the pretraining paradigm that reshaped vision and language can also work for the brain.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_takeaway_pretraining_paradigm_reshap" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, pretraining, paradigm, reshaped, vision, language in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_treating_spikes_autoregressive_multi`

- Preferred role: `method`
- Cue keywords: `treating, spikes, autoregressive, multimodal, generation, one, self-supervised, transformer, recovers, circuit`
- Narration: Treating spikes as autoregressive multimodal generation, one self-supervised transformer recovers a circuit's directed connectivity and decodes behavior from few examples, pointing toward scalable neuroscience foundation models.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_treating_spikes_autoregressive_multi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords treating, spikes, autoregressive, multimodal, generation, one in title/desc so the matcher can verify semantic overlap.
