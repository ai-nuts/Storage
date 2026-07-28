# Key Result

Core claim: Balancing the three-task mixture by augmentation gives the best overall performance, and knowledge distillation consistently improves the compact student on every task in both single-task and multi-task settings; the distilled LLaMA-300M outperforms its from-scratch counterpart on Pascal-5i foreground segmentation.

Supporting detail: Increasing SA-1B data from 1% to 10% (0.34B to 3.43B tokens) cuts validation loss by 0.19 and perplexity by 22.4; augmentation reproduces this trend without any new data.

Narration: The results consistently favor the proposed recipe. On the mixed three-task benchmark, balancing the data through augmentation beats both the raw unbalanced mixture and naive re-sampling, which actually collapses on the scarce tasks. Knowledge distillation then improves the compact student on segmentation, pose estimation, and deraining, in both single-task and multi-task training. On the Pascal five-i foreground segmentation benchmark, the distilled and fine-tuned three-hundred-million model clearly surpasses the same model trained from scratch. And scaling data on segmentation from one to ten percent lowers validation loss by nearly two tenths and perplexity by over twenty-two points, an effect augmentation reproduces with no new data at all.
