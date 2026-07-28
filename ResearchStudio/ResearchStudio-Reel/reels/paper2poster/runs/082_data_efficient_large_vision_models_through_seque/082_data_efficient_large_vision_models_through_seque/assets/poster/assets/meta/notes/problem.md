# Problem

Core claim: Autoregressive large vision models (LVMs) generalize across tasks but rely on colossal models (3B+ parameters) and enormous visual corpora (~400B tokens, 1.64B images), making them costly and hard to deploy.

Supporting detail: Vision tasks follow a long-tailed distribution, so naively mixing benchmarks lets data-rich tasks (segmentation) swamp data-poor ones (keypoint detection), which the model then fails to learn.

Narration: In language modeling, autoregressive models like GPT thrive on a universal token interface. Recent work extends this idea to vision, treating images and annotations as visual sentences. But the leading large vision model needs over three billion parameters and roughly four hundred billion visual tokens drawn from more than a billion images. That scale is expensive and impractical for edge deployment. Worse, the visual world is long-tailed: some tasks like segmentation have abundant data while others like pose estimation are starved, and training on the raw mixture leaves the model unable to learn the rare tasks at all.
