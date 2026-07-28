# Headline Numbers

Core claim: - Behavior prediction Pearson r up to 0.97 (Neuroformer) vs 0.73 for Lasso regression on the same split. - Neuroformer behavior correlation 0.95 / 0.97 vs Lasso 0.62 / 0.73 across two conditions (Table 1). - Few-shot transfer: pretrained model fine-tuned on 1% of behavior data (r=0.51) beats non-pretrained on 10% (r=0.33). - Population-response prediction beats GLM with t-test p=0.0196; largest models ~100M parameters.

Supporting detail: 386 reliable neurons imaged across mouse visual areas V1 and AL; three "hub" neurons recovered by attention in the simulated ground-truth network.

Narration: For behavior prediction, Neuroformer reaches Pearson correlation up to 0.97, versus about 0.73 for Lasso. Few-shot, a model pretrained and fine-tuned on just 1% of behavior data hits 0.51, beating a non-pretrained model given 10%, which reaches only 0.33. Its largest models scale to roughly 100 million parameters.
