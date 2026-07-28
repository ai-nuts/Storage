# Dataset / Benchmark

Core claim: Evaluated on language tasks with RoBERTa-base/large (MNLI, QQP, QNLI, SST-2) and GPT2/GPT2-medium/large text generation (E2E, DART), plus vision tasks (CIFAR10 with SimCLRv2, ImageNette with ResNet9, ImageNet with ResNet18).

Supporting detail: Uses standard privacy budgets epsilon=3 and epsilon=8, the exact hyperparameters of prior SOTA (Li et al.), and reports 95% confidence intervals over 5 runs on image tasks.

Narration: The method is tested broadly. On language, the authors finetune RoBERTa base and large on the GLUE tasks MNLI, QQP, QNLI, and SST-2, and finetune GPT2 in three sizes for table-to-text generation on the E2E and DART datasets. On vision, they evaluate CIFAR-10 with a pretrained SimCLRv2, ImageNette with a ResNet9, and ImageNet with ResNet18. They use standard privacy budgets of epsilon three and epsilon eight and reuse the exact hyperparameters of prior state-of-the-art work, changing only the clipping.
