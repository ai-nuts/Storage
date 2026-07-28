# Ablation Study

Core claim: Removing the cross-attention modules degrades performance substantially, confirming they are essential to bridging the two streams; each of the four attention modules contributes.

Supporting detail: On MD17 energy prediction, adding cross-attention yields 18.7% (Inv-Cross-Attn), 9.8% (Equ-Cross-Attn), and 20.8% (both) relative improvement; on MD17 force prediction the gains are 28.0%, 43.9%, and 60.8%; on N-body they are 7.8%, 13.0%, and 17.5%.

Narration: To understand where the gains come from, the authors ablate each building block. The most telling finding concerns the cross-attention modules that bridge the invariant and equivariant streams. Removing them hurts sharply. On the MD17 energy prediction task, adding the invariant cross-attention gives an eighteen point seven percent relative improvement, the equivariant cross-attention gives nine point eight percent, and using both together gives twenty point eight percent. On the harder MD17 force prediction task the effect is even larger, with a sixty point eight percent relative improvement when both cross-attention modules are used. On the N-body simulation the combined improvement is seventeen point five percent. The self-attention, feed-forward, and layer-normalization modules also each contribute, but the cross-attention bridge is clearly the heart of the design.
