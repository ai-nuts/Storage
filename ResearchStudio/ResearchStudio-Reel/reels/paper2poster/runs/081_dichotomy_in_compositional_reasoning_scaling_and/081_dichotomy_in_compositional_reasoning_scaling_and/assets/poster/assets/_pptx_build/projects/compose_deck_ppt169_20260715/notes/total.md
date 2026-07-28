# 01_title

Can large language models combine skills they already know? This COLM 2024 paper tests whether models solve an unseen composite task by fusing two simple tasks seen separately. Across Llama and GPT, a sharp dichotomy emerges.

---

# 02_problem

Suppose a model learned two simple tasks in-context, capitalizing certain words and swapping others. Given an input needing both, can it combine the skills? For humans this is trivial, yet even GPT-4 and Claude 3 often fail.

---

# 03_motivation

Models are increasingly asked to chain skills for real reasoning, yet we lack a clear account of when chaining works. Prior studies are narrow with little theory, and the failure reproduces easily on frontier models.

---

# 04_contribution

Three contributions: a test suite of linguistic and logical composite tasks with simple-task examples only; evaluation across Llama and GPT scales revealing a clear dichotomy; and a linear self-attention theory explaining when composition emerges.

---

# 05_method

Two halves. Empirically, each composite task is tested in four settings with ten in-context examples: each simple task alone, a composite test with simple-task demos, and an all-composite gold standard. Theoretically, a linear self-attention model shows composition succeeds under confined support.

---

# 06_dataset_benchmark

The suite pairs simple building blocks. Linguistic tasks include capitalization, swapping, and translations like phrase recombination and passive-to-active. Logical tasks combine arithmetic with word operations. Tasks split into separable composites, acting on different input parts, and compose-by-step composites requiring chained reasoning.

---

# 07_key_result

A sharp split. On separable composite tasks, models compose well and improve with scale, approaching the gold standard. On compose-by-step tasks they collapse: Llama solves each simple task near ninety percent, but the composite drops below twenty percent, and scaling doesn't help.

---

# 08_ablation

The scale sweep is the key ablation. On separable tasks accuracy rises with scale; on compose-by-step tasks it stays flat or degrades. Swapping simple-task demos for composite ones recovers performance, isolating composition, not capability, as the bottleneck.

---

# 09_headline_numbers

The numbers tell it. Simple capitalization and swap reach about ninety percent for Llama. The compose-by-step version falls to twenty percent or lower, with no gain from scaling. Milder separable cases climb to forty-four and sixty-six percent.

---

# 10_takeaway

The takeaway: models combine two skills only when they act on separate parts of the input. When a task needs genuinely chained, multi-step reasoning, they fail, and more parameters won't help. Task structure predicts whether scaling helps.

