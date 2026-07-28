# Dataset / Benchmark

Core claim: Training uses two public datasets: WebVid10M (10.3M video-caption pairs scraped from the web) and LAION-400M (a CLIP-filtered image-caption dataset). Text-to-video quality is evaluated on the MSR-VTT benchmark.

Supporting detail: Motion controllability is measured on 1000 randomly selected caption-video pairs using a dedicated motion-control error metric, with FVD and CLIPSIM for generation quality.

Narration: VideoComposer is trained on two public datasets: WebVid-10M, about ten million video-caption pairs from the web, and LAION-400M, CLIP-filtered image-caption pairs for visual quality. For evaluation, the authors report text-to-video on MSR-VTT using Fréchet Video Distance and CLIP similarity, and measure motion controllability on a thousand caption-video pairs with a dedicated motion-control error.
