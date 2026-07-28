# Key Result

Core claim: The augmented model maintains near-SOTA answer accuracy while generating explanations, reaching 77.49% VQA score on GQA-REX and 71.48% on VQA-E, essentially matching the explanation-free baseline.

Supporting detail: For explanation quality, CFRF+LSTM beats the baseline on VQA-E (BLEU-1 0.33 vs 0.268; ROUGE-L 0.325 vs 0.249), though absolute scores remain only satisfactory.

Narration: The central result is that adding explanation generation does not cost accuracy. On GQA-REX the model reaches a VQA score of seventy-seven point four nine percent, and on VQA-E seventy-one point four eight percent, both essentially matching the baseline that was trained without any explanation supervision. Varying the balance factor alpha changes the trade-off only marginally. For the explanations themselves, the CFRF-plus-LSTM model outperforms the prior baseline on VQA-E, with a BLEU-1 of zero point three three versus zero point two six eight and a ROUGE-L of zero point three two five versus zero point two four nine. The authors are candid that these absolute numbers are only satisfactory, which sets up their argument about evaluation.
