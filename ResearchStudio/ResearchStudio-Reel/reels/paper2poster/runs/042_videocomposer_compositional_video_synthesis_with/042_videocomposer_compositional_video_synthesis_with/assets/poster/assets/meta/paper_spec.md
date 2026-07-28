---
title: "VideoComposer: Compositional Video Synthesis with Motion Controllability"
authors: Xiang Wang¹*, Hangjie Yuan¹*, Shiwei Zhang¹*, Dayou Chen¹*, Jiuniu Wang¹, Yingya Zhang¹, Yujun Shen², Deli Zhao¹, Jingren Zhou¹
institutes: ¹Alibaba Group; ²Ant Group
venue: NeurIPS 2023
paper_url: https://arxiv.org/abs/2306.02018
code_url: https://github.com/damo-vilab/videocomposer
title_audio_script: VideoComposer, from Alibaba and Ant Group, tackles controllable video generation. Building on the paradigm of compositional generation, it lets users compose a video from textual, spatial, and temporal conditions at the same time. Its key ideas are to use motion vectors from compressed video as an explicit signal for temporal dynamics, and a unified Spatio-Temporal Condition encoder that fuses diverse conditions while keeping frames consistent. The result is flexible, controllable video synthesis driven by text, sketches, reference video, or even simple hand-drawn strokes.
---

## Problem
**Necessary:** Controllable video synthesis is far harder than controllable image synthesis: temporal dynamics vary widely and generated frames must stay temporally consistent, so image-style controls do not transfer directly.
**Additional:** Prior progress in customizable image generation gives spatial control, but offers no principled way to steer how content moves and evolves over time.
**Audio script:** Recent diffusion models made customizable image generation remarkably controllable, but doing the same for video is much harder. Video adds a temporal axis: the motion patterns vary enormously from clip to clip, and every generated frame has to remain consistent with its neighbours. Simply reusing the spatial controls designed for images gives no reliable handle on temporal dynamics, so controllable video synthesis remained an open challenge.

## Motivation
**Necessary:** To give users explicit control over motion, the paper introduces motion vectors from compressed video as a temporal condition, providing direct guidance on temporal dynamics that other conditions lack.
**Additional:** Feeding many heterogeneous conditions naively breaks cross-frame consistency, motivating a single encoder that captures space-time relations across all sequential inputs.
**Audio script:** The authors argue that to control a video you must control its motion, not just its appearance. Their insight is that motion vectors, which are already computed inside compressed video formats to encode inter-frame variation, are a cheap and explicit description of temporal dynamics. By turning motion vectors into a control signal, users can prescribe how things move. But mixing motion vectors with sketches, depth maps, masks and images naively hurts frame-to-frame consistency, which motivates a unified encoder that understands space and time together.

## Contribution
**Necessary:** (1) VideoComposer, a compositional framework that generates video from arbitrary combinations of textual, spatial, and temporal conditions; (2) the use of compressed-video motion vectors as an explicit temporal control signal; (3) the Spatio-Temporal Condition encoder (STC-encoder), a unified interface that embeds diverse sequential conditions while improving inter-frame consistency.
**Additional:** VideoComposer supports text, single image, single sketch, motion vectors, depth sequences, mask sequences, sketch sequences, and style, and can even animate simple hand-crafted strokes.
**Audio script:** VideoComposer makes three contributions. First, it frames video generation as compositional: a user supplies any subset of textual, spatial, and temporal conditions and the model recomposes a video that obeys all of them. Second, it introduces motion vectors from compressed video as an explicit temporal control signal for guiding dynamics. Third, it proposes the Spatio-Temporal Condition encoder, a single lightweight module that turns every kind of sequential condition into a shared representation while boosting temporal consistency. Together these let one model handle text, images, sketches, depth, masks, reference videos, and hand-drawn motions.

## Method
**Necessary:** VideoComposer is built on a Video Latent Diffusion Model. Each video is decomposed into textual, spatial, and temporal conditions; sequential conditions pass through the STC-encoder (two 2D convolutions, average pooling, then a temporal Transformer), are fused by element-wise addition, and concatenated with the noisy latent along the channel dimension, while text and style are injected via cross-attention. A two-stage strategy first pre-trains text-to-video, then trains compositionally; DDIM with classifier-free guidance is used at inference.
**Additional:** Motion vectors are extracted in standard formats to encode inter-frame variation; single-image and single-sketch spatial conditions are repeated along time to align with the temporal conditions before fusion.
**Audio script:** Under the hood, VideoComposer is a latent diffusion model that denoises video in a compressed latent space for efficiency. A training video is decomposed into three families of conditions, textual, spatial, and temporal, that can be freely combined. The sequential conditions, such as motion vectors, depth maps, masks, and sketch sequences, are all passed through one shared module called the STC-encoder: two convolutions and a pooling layer capture local spatial structure, then a temporal Transformer models how things change across frames. The encoded conditions are added together and concatenated with the noisy latent as control signals, while text and style are injected through cross-attention. Training happens in two stages, first learning plain text-to-video, then learning to compose many conditions, and inference uses DDIM sampling with classifier-free guidance.
**Key equation:** `$\mathcal{L}_{VLDM} = \mathbb{E}_{\mathcal{E}(x),\,\epsilon\sim\mathcal{N}(0,1),\,c,\,t}\big[\lVert \epsilon - \epsilon_\theta(z_t, c, t)\rVert_2^2\big]$`

## Dataset / Benchmark
**Necessary:** Training uses two public datasets: WebVid10M (10.3M video-caption pairs scraped from the web) and LAION-400M (a CLIP-filtered image-caption dataset). Text-to-video quality is evaluated on the MSR-VTT benchmark.
**Additional:** Motion controllability is measured on 1000 randomly selected caption-video pairs using a dedicated motion-control error metric, with FVD and CLIPSIM for generation quality.
**Audio script:** VideoComposer is trained on two widely used public datasets. WebVid ten million provides about ten point three million video-caption pairs scraped from the web, and LAION four hundred million supplies CLIP-filtered image-caption pairs for visual quality. For evaluation, the authors report text-to-video generation on the MSR-VTT benchmark using Fréchet Video Distance and CLIP similarity, and they measure motion controllability on a thousand caption-video pairs with a dedicated motion-control error.

## Key Result
**Necessary:** On MSR-VTT, VideoComposer reaches an FVD of 580 and a CLIPSIM of 0.2932 in the zero-shot setting, competitive with state-of-the-art text-to-video methods and better than its own first-stage text-to-video pre-training (FVD 803), showing compositional training does not sacrifice text-to-video quality.
**Additional:** Qualitatively, VideoComposer produces videos that faithfully follow supplied sketches, depth sequences, motion vectors, masks, and reference styles, and can animate two simple strokes into coherent motion and shape.
**Audio script:** On the MSR-VTT benchmark, VideoComposer achieves a Fréchet Video Distance of five hundred eighty and a CLIP similarity of zero point two nine three two, all zero-shot. That is competitive with leading text-to-video systems, and notably it improves over the model's own first-stage text-to-video pre-training, which scored eight hundred three. In other words, adding compositional, multi-condition control does not cost anything in raw text-to-video quality. Qualitatively, the generated videos closely follow the sketches, depth maps, motion vectors, masks, and styles that users provide.

## Ablation Study
**Necessary:** On motion controllability, adding motion vectors as a condition lowers the motion-control error from 4.03 (text only) to 2.67, and the STC-encoder lowers it further to 2.18, confirming that both the motion-vector signal and the STC-encoder contribute to temporal control.
**Additional:** The qualitative ablation shows that removing the STC-encoder degrades adherence to the specified temporal structure and inter-frame consistency.
**Audio script:** The ablations isolate where the control comes from. Using only text gives a motion-control error of four point zero three. Adding motion vectors as an explicit temporal condition drops that error to two point six seven, and turning on the Spatio-Temporal Condition encoder brings it down further to two point one eight. So both ingredients matter: motion vectors supply the temporal signal, and the STC-encoder makes the model actually use it, sharpening motion control and inter-frame consistency.

## Headline Numbers
**Necessary:**
- MSR-VTT text-to-video: **FVD 580**, **CLIPSIM 0.2932** (zero-shot), vs first-stage pre-training FVD 803.
- Motion-control error: **2.18** for full VideoComposer, vs 2.67 without STC-encoder and 4.03 with text only (lower is better).
- Trained on **WebVid10M (10.3M video-caption pairs)** + **LAION-400M**.
**Additional:** Supports 8+ condition types (text, single image, single sketch, motion vectors, depth sequence, mask sequence, sketch sequence, style) that can be composed arbitrarily.
**Audio script:** A few numbers capture the impact. On MSR-VTT, VideoComposer scores a Fréchet Video Distance of five hundred eighty and a CLIP similarity of zero point two nine three two. Its motion-control error falls to two point one eight, compared with four point zero three for a text-only baseline. And all of this is learned from two public datasets, WebVid ten million with over ten million video-caption pairs, and LAION four hundred million.

## Takeaway
**Necessary:** By treating a video as a composition of textual, spatial, and temporal conditions, and by pairing compressed-video motion vectors with a unified STC-encoder, VideoComposer delivers flexible, controllable video synthesis with strong inter-frame consistency and no loss in text-to-video quality.
**Additional:** The same model can be driven by text, sketches, depth, masks, reference video, or even two hand-drawn strokes, making motion an explicit, user-editable dimension of video generation.
**Audio script:** The lasting takeaway is that video generation becomes far more controllable when you treat a video as a composition of conditions and give motion its own explicit signal. VideoComposer combines compressed-video motion vectors with a single Spatio-Temporal Condition encoder, so users can steer content and motion together, using anything from text and sketches to depth maps, masks, reference videos, or two simple strokes, all while keeping frames consistent and text-to-video quality intact.
