# Headline Numbers

Core claim: - MSR-VTT text-to-video: FVD 580, CLIPSIM 0.2932 (zero-shot), vs first-stage pre-training FVD 803. - Motion-control error: 2.18 for full VideoComposer, vs 2.67 without STC-encoder and 4.03 with text only (lower is better). - Trained on WebVid10M (10.3M video-caption pairs) + LAION-400M.

Supporting detail: Supports 8+ condition types (text, single image, single sketch, motion vectors, depth sequence, mask sequence, sketch sequence, style) that can be composed arbitrarily.

Narration: A few numbers capture the impact. On MSR-VTT, VideoComposer scores a Fréchet Video Distance of five hundred eighty and a CLIP similarity of zero point two nine three two. Its motion-control error falls to two point one eight, versus four point zero three for a text-only baseline. And all is learned from two datasets, WebVid-10M and LAION-400M.
