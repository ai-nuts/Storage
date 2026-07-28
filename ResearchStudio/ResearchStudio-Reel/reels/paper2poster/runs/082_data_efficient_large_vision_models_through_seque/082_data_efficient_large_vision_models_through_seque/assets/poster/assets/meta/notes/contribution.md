# Contribution

Core claim: The paper introduces DeLVM, a data-efficient autoregressive vision model, and shows that (1) data augmentation rebalances long-tailed multi-task data as effectively as adding new data, and (2) knowledge distillation transfers a large teacher's ability into a compact student LVM for both single- and multi-task settings.

Supporting detail: It further demonstrates a practical 80M-parameter model that, with augmentation plus distillation, even reaches 83% top-1 accuracy on ImageNet classification, hinting that generation and understanding can be learned jointly.

Narration: The authors make three main contributions. First, they show that simple data augmentation, random crop and flip, rebalances long-tailed multi-task data and improves an autoregressive vision model just as effectively as collecting more real samples. Second, they bring knowledge distillation to autoregressive large vision models for the first time, using a LLaMA one-billion teacher to lift a compact three-hundred-million student across single-task and multi-task benchmarks. Third, they build a practical eighty-million-parameter model that, combining both techniques, surprisingly reaches eighty-three percent top-one accuracy on ImageNet, suggesting generation and understanding can be learned together.
