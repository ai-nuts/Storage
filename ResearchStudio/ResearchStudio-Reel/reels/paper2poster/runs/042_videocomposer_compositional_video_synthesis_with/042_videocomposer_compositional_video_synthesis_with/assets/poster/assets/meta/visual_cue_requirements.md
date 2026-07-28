# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_videocomposer_alibaba_ant_group_make`

- Preferred role: `content`
- Cue keywords: `videocomposer, alibaba, ant, group, makes, video, generation, controllable, through, composition`
- Narration: VideoComposer, from Alibaba and Ant Group, makes video generation controllable through composition.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_videocomposer_alibaba_ant_group_make" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords videocomposer, alibaba, ant, group, makes, video in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_users_combine_textual_spatial_tempor`

- Preferred role: `content`
- Cue keywords: `users, combine, textual, spatial, temporal, conditions, once`
- Narration: Users combine textual, spatial, and temporal conditions at once.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_users_combine_textual_spatial_tempor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords users, combine, textual, spatial, temporal, conditions in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_its_key_ideas_motion_vectors`

- Preferred role: `method`
- Cue keywords: `its, key, ideas, motion, vectors, compressed, video, explicit, temporal, signal`
- Narration: Its key ideas: motion vectors from compressed video as an explicit temporal signal, and a unified Spatio-Temporal Condition encoder that fuses diverse controls while keeping frames consistent, from text and sketches to reference video or simple strokes.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_its_key_ideas_motion_vectors" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, key, ideas, motion, vectors, compressed in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_diffusion_models_made_image_generati`

- Preferred role: `content`
- Cue keywords: `diffusion, models, made, image, generation, highly, controllable, but, video, much`
- Narration: Diffusion models made image generation highly controllable, but video is much harder.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_diffusion_models_made_image_generati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords diffusion, models, made, image, generation, highly in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_video_adds_temporal_axis_motion`

- Preferred role: `content`
- Cue keywords: `video, adds, temporal, axis, motion, patterns, vary, enormously, across, clips`
- Narration: Video adds a temporal axis: motion patterns vary enormously across clips, and every frame must stay consistent with its neighbours.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_video_adds_temporal_axis_motion" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords video, adds, temporal, axis, motion, patterns in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_reusing_spatial_controls_designed_im`

- Preferred role: `content`
- Cue keywords: `reusing, spatial, controls, designed, images, gives, reliable, handle, temporal, dynamics`
- Narration: Reusing the spatial controls designed for images gives no reliable handle on temporal dynamics, so controllable video synthesis stayed an open challenge.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_reusing_spatial_controls_designed_im" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reusing, spatial, controls, designed, images, gives in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_control_video_you_must_control`

- Preferred role: `content`
- Cue keywords: `control, video, you, must, control, its, motion, not, only, its`
- Narration: To control a video, you must control its motion, not only its appearance.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_control_video_you_must_control" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords control, video, you, must, control, its in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_authors_insight_motion_vectors_compu`

- Preferred role: `content`
- Cue keywords: `authors, insight, motion, vectors, computed, inside, compressed, video, encode, inter-frame`
- Narration: The authors' insight: motion vectors, computed inside compressed video to encode inter-frame change, are a cheap, explicit description of temporal dynamics.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_authors_insight_motion_vectors_compu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, insight, motion, vectors, computed, inside in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_turning_them_control_signal_lets`

- Preferred role: `content`
- Cue keywords: `turning, them, control, signal, lets, users, prescribe, how, things, move`
- Narration: Turning them into a control signal lets users prescribe how things move.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_turning_them_control_signal_lets" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords turning, them, control, signal, lets, users in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_but_mixing_them_sketches_depth`

- Preferred role: `method`
- Cue keywords: `but, mixing, them, sketches, depth, images, naively, hurts, consistency, motivating`
- Narration: But mixing them with sketches, depth, and images naively hurts consistency, motivating a unified encoder for space and time.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_but_mixing_them_sketches_depth" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, mixing, them, sketches, depth, images in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_videocomposer_makes_three_contributi`

- Preferred role: `content`
- Cue keywords: `videocomposer, makes, three, contributions`
- Narration: VideoComposer makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_videocomposer_makes_three_contributi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords videocomposer, makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_frames_video_generation_compos`

- Preferred role: `content`
- Cue keywords: `first, frames, video, generation, compositional, user, supplies, any, subset, textual`
- Narration: First, it frames video generation as compositional: a user supplies any subset of textual, spatial, and temporal conditions, and the model recomposes a video obeying all of them.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_first_frames_video_generation_compos" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, frames, video, generation, compositional, user in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_introduces_motion_vectors_com`

- Preferred role: `content`
- Cue keywords: `second, introduces, motion, vectors, compressed, video, explicit, temporal, control, signal`
- Narration: Second, it introduces motion vectors from compressed video as an explicit temporal control signal.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_second_introduces_motion_vectors_com" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, introduces, motion, vectors, compressed, video in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_proposes_spatio_temporal_condi`

- Preferred role: `method`
- Cue keywords: `third, proposes, spatio-temporal, condition, encoder, lightweight, module, turns, every, sequential`
- Narration: Third, it proposes the Spatio-Temporal Condition encoder, a lightweight module that turns every sequential condition into a shared representation while boosting temporal consistency.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_third_proposes_spatio_temporal_condi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, proposes, spatio-temporal, condition, encoder, lightweight in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_videocomposer_latent_diffusion_denoi`

- Preferred role: `method`
- Cue keywords: `videocomposer, latent, diffusion, denoises, video, compressed, latent, space, video, decomposed`
- Narration: VideoComposer is a latent diffusion model that denoises video in a compressed latent space. Each training video is decomposed into three families of conditions, textual, spatial, and temporal, combined freely.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_videocomposer_latent_diffusion_denoi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords videocomposer, latent, diffusion, denoises, video, compressed in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_sequential_conditions_like_motion_ve`

- Preferred role: `method`
- Cue keywords: `sequential, conditions, like, motion, vectors, depth, maps, masks, sketches, all`
- Narration: Sequential conditions like motion vectors, depth maps, masks, and sketches all pass through one shared STC-encoder: two convolutions and pooling capture local spatial structure, then a temporal Transformer models change across frames.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_sequential_conditions_like_motion_ve" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sequential, conditions, like, motion, vectors, depth in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_encoded_conditions_summed_concatenat`

- Preferred role: `method`
- Cue keywords: `encoded, conditions, summed, concatenated, noisy, latent, while, text, style, enter`
- Narration: Encoded conditions are summed and concatenated with the noisy latent, while text and style enter through cross-attention.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_encoded_conditions_summed_concatenat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords encoded, conditions, summed, concatenated, noisy, latent in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_runs_two_stages_inference_ddim`

- Preferred role: `method`
- Cue keywords: `runs, two, stages, inference, ddim, sampling, classifier-free, guidance`
- Narration: Training runs in two stages, and inference uses DDIM sampling with classifier-free guidance.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_runs_two_stages_inference_ddim" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords runs, two, stages, inference, ddim, sampling in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_videocomposer_trained_two_public_dat`

- Preferred role: `method`
- Cue keywords: `videocomposer, trained, two, public, datasets, webvid-10m, about, ten, million, video-caption`
- Narration: VideoComposer is trained on two public datasets: WebVid-10M, about ten million video-caption pairs from the web, and LAION-400M, CLIP-filtered image-caption pairs for visual quality.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_videocomposer_trained_two_public_dat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords videocomposer, trained, two, public, datasets, webvid-10m in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_evaluation_authors_report_text_to_vi`

- Preferred role: `result`
- Cue keywords: `evaluation, authors, report, text-to-video, msr-vtt, chet, video, distance, clip, similarity`
- Narration: For evaluation, the authors report text-to-video on MSR-VTT using Fréchet Video Distance and CLIP similarity, and measure motion controllability on a thousand caption-video pairs with a dedicated motion-control error.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_evaluation_authors_report_text_to_vi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, authors, report, text-to-video, msr-vtt, chet in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_msr_vtt_videocomposer_achieves_chet`

- Preferred role: `content`
- Cue keywords: `msr-vtt, videocomposer, achieves, chet, video, distance, five, hundred, eighty, clip`
- Narration: On MSR-VTT, VideoComposer achieves a Fréchet Video Distance of five hundred eighty and a CLIP similarity of zero point two nine three two, zero-shot.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_msr_vtt_videocomposer_achieves_chet" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords msr-vtt, videocomposer, achieves, chet, video, distance in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_competitive_leading_text_to_video_sy`

- Preferred role: `method`
- Cue keywords: `competitive, leading, text-to-video, systems, improves, over, first-stage, pre-training, which, scored`
- Narration: That is competitive with leading text-to-video systems, and it improves over the model's first-stage pre-training, which scored eight hundred three.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_competitive_leading_text_to_video_sy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords competitive, leading, text-to-video, systems, improves, over in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_adding_compositional_multi_condition`

- Preferred role: `content`
- Cue keywords: `adding, compositional, multi-condition, control, costs, nothing, quality, while, videos, follow`
- Narration: So adding compositional, multi-condition control costs nothing in quality, while videos follow the sketches, depth, motion, and styles users provide.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_adding_compositional_multi_condition" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords adding, compositional, multi-condition, control, costs, nothing in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablations_isolate_where_control_orig`

- Preferred role: `content`
- Cue keywords: `ablations, isolate, where, control, originates`
- Narration: The ablations isolate where control originates.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_ablations_isolate_where_control_orig" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, isolate, where, control, originates in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_only_text_gives_motion_control_error`

- Preferred role: `result`
- Cue keywords: `only, text, gives, motion-control, error, four, point, zero, three`
- Narration: Using only text gives a motion-control error of four point zero three.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_only_text_gives_motion_control_error" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords only, text, gives, motion-control, error, four in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_adding_motion_vectors_temporal_condi`

- Preferred role: `method`
- Cue keywords: `adding, motion, vectors, temporal, condition, drops, two, point, six, seven`
- Narration: Adding motion vectors as a temporal condition drops it to two point six seven, and enabling the Spatio-Temporal Condition encoder lowers it to two point one eight.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_adding_motion_vectors_temporal_condi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords adding, motion, vectors, temporal, condition, drops in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_both_matter_motion_vectors_supply`

- Preferred role: `method`
- Cue keywords: `both, matter, motion, vectors, supply, signal, stc-encoder, makes`
- Narration: Both matter: motion vectors supply the signal, and the STC-encoder makes the model use it.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_both_matter_motion_vectors_supply" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords both, matter, motion, vectors, supply, signal in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, impact`
- Narration: A few numbers capture the impact.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_msr_vtt_videocomposer_scores_chet_vi`

- Preferred role: `method`
- Cue keywords: `msr-vtt, videocomposer, scores, chet, video, distance, five, hundred, eighty, clip`
- Narration: On MSR-VTT, VideoComposer scores a Fréchet Video Distance of five hundred eighty and a CLIP similarity of zero point two nine three two.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_msr_vtt_videocomposer_scores_chet_vi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords msr-vtt, videocomposer, scores, chet, video, distance in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_its_motion_control_error_falls_two`

- Preferred role: `result`
- Cue keywords: `its, motion-control, error, falls, two, point, one, eight, versus, four`
- Narration: Its motion-control error falls to two point one eight, versus four point zero three for a text-only baseline.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_its_motion_control_error_falls_two" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, motion-control, error, falls, two, point in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_all_learned_two_datasets_webvid_10m`

- Preferred role: `content`
- Cue keywords: `all, learned, two, datasets, webvid-10m, laion-400m`
- Narration: And all is learned from two datasets, WebVid-10M and LAION-400M.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_all_learned_two_datasets_webvid_10m" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords all, learned, two, datasets, webvid-10m, laion-400m in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_video_generation_becomes_mo`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, video, generation, becomes, more, controllable, when, you, treat, video`
- Narration: The takeaway: video generation becomes more controllable when you treat a video as a composition of conditions and give motion an explicit signal.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_video_generation_becomes_mo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, video, generation, becomes, more, controllable in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_videocomposer_combines_compressed_vi`

- Preferred role: `method`
- Cue keywords: `videocomposer, combines, compressed-video, motion, vectors, spatio-temporal, condition, encoder, users, steer`
- Narration: VideoComposer combines compressed-video motion vectors with a Spatio-Temporal Condition encoder, so users steer content and motion together, from text, sketches, and depth to masks, reference videos, or two strokes, while keeping frames consistent.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_videocomposer_combines_compressed_vi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords videocomposer, combines, compressed-video, motion, vectors, spatio-temporal in title/desc so the matcher can verify semantic overlap.
