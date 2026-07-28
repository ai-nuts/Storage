# Ablation Study

Core claim: Feature sparsification is nearly free: pruning the SCM to k=48 non-zero elements (307K params) meets the storage budget while keeping ConvNet accuracy at 73.5%, versus 74.0% for the full 15M-parameter model. FReeNet depth R=2, three heads (H=3), and moderate token count/dimension are the best settings.

Supporting detail: A moderate k improves cross-architecture generalization; too-small k (12, 106K) collapses accuracy to 57.8%, and Figure 4 shows synthetic samples look almost identical before and after sparsification down to 0.3% density.

Narration: The ablations show sparsification is essentially free. Pruning each sparse coding matrix to just forty-eight non-zero elements, about three hundred thousand parameters, meets the storage budget while keeping ConvNet accuracy at seventy-three point five percent, barely below the seventy-four percent of the full fifteen-million-parameter model. Push k too low, down to twelve, and accuracy collapses, so a moderate value is best and even improves cross-architecture generalization. On the network side, two recurrent blocks and three heads work best. And qualitatively, synthetic images before and after sparsification to zero point three percent density look almost identical, confirming that the pruned features preserve the global semantics.
