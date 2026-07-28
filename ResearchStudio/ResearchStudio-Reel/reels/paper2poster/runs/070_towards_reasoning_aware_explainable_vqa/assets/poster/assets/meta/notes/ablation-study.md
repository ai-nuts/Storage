# Ablation Study

Core claim: Sweeping the loss balance factor alpha and swapping the explanation generator shows accuracy is robust: on GQA-REX, LSTM scores range 75.08%–77.49% across alpha, and the Transformer decoder (alpha=0.5) reaches 77.06%, all close to the 77.49% baseline.

Supporting detail: On VQA-E, LSTM scores stay within 71.32%–71.55% across alpha and the Transformer reaches 71.46%, confirming the explanation module barely perturbs answering regardless of architecture or loss weighting.

Narration: The authors ablate two design choices: the balance factor alpha that weights answer loss against explanation loss, and the choice of explanation generator. On GQA-REX, the LSTM variant ranges from about seventy-five to seventy-seven and a half percent across different alpha values, and the Transformer decoder at alpha equal to one half reaches seventy-seven point zero six percent. On VQA-E, every configuration lands within a fraction of a percent of the seventy-one and a half percent baseline. The takeaway from these sweeps is that answer accuracy is remarkably stable no matter how the explanation loss is weighted or which decoder architecture generates the explanation, so the explanation module can be added essentially for free.
