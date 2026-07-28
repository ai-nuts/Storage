# Key Result

Core claim: MeZO substantially outperforms zero-shot, in-context learning, and linear probing, and matches Adam fine-tuning within roughly 1% on 7 of 11 OPT-13B tasks while using only 1/12 of the memory. On RoBERTa-large it approaches fine-tuning within about 5% at k=512.

Supporting detail: MeZO also cuts wall-clock cost: it needs only about half as many GPU-hours as Adam fine-tuning for a 30B model in the authors' implementation.

Narration: The headline result is that MeZO closes most of the gap to backpropagation fine-tuning at a fraction of the memory. On OPT-thirteen-billion, MeZO comes within about one percent of full Adam fine-tuning on seven of eleven tasks, while consuming only one-twelfth of the memory, and it clearly beats zero-shot prediction, in-context learning, and linear probing. On RoBERTa-large in the many-shot setting, it lands within roughly five percent of fine-tuning. Beyond memory, MeZO is also faster in practice, requiring about half the GPU-hours of Adam fine-tuning for a thirty-billion-parameter model.
