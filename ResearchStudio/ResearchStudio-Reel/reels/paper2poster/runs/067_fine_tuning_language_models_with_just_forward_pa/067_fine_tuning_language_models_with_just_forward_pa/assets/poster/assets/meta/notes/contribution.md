# Contribution

Core claim: The paper proposes MeZO, an in-place zeroth-order SGD optimizer that fine-tunes language models with the exact memory footprint of inference, and shows it matches backpropagation across model types, scales, and tasks with up to 12x memory savings.

Supporting detail: It also provides theory explaining why MeZO converges fast despite huge parameter counts (the rate depends on the loss landscape's effective local rank, not the parameter count), and shows MeZO works with LoRA, prefix tuning, and non-differentiable objectives.

Narration: The paper makes four main contributions. First, it introduces MeZO, a memory-efficient zeroth-order optimizer that adapts classical zeroth-order SGD to operate in place, so fine-tuning costs no more memory than inference. Second, through comprehensive experiments across masked and autoregressive models, scales up to sixty-six billion parameters, and classification, multiple-choice, and generation tasks, it shows MeZO matches full backpropagation fine-tuning while using far less memory. Third, it demonstrates compatibility with parameter-efficient methods like LoRA and prefix tuning, and the ability to optimize non-differentiable objectives such as accuracy or F1. Fourth, it supplies theory explaining why MeZO converges quickly despite the enormous parameter count.
