# Ablation Study

Core claim: On motion controllability, adding motion vectors as a condition lowers the motion-control error from 4.03 (text only) to 2.67, and the STC-encoder lowers it further to 2.18, confirming that both the motion-vector signal and the STC-encoder contribute to temporal control.

Supporting detail: The qualitative ablation shows that removing the STC-encoder degrades adherence to the specified temporal structure and inter-frame consistency.

Narration: The ablations isolate where control originates. Using only text gives a motion-control error of four point zero three. Adding motion vectors as a temporal condition drops it to two point six seven, and enabling the Spatio-Temporal Condition encoder lowers it to two point one eight. Both matter: motion vectors supply the signal, and the STC-encoder makes the model use it.
