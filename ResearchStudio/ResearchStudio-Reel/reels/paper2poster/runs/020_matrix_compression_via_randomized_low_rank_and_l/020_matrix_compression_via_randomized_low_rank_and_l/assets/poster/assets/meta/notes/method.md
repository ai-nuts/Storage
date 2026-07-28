# Method

Core claim: LPLR sketches the columns of A with a Gaussian matrix S to get an approximate range basis AS, quantizes it to Q(AS), then solves a least-squares projection W = argmin ‖Q(AS)W − A‖²_F and quantizes W to Q'(W), returning L = Q(AS) and R = Q'(W).

Supporting detail: Because S is a Gaussian JL embedding, uniform quantization enjoys an equalization property: the vector quantization error of x̂ = SᵀQ(Sx) stays O(1) rather than growing as O(d), which is why LPLR tolerates aggressive bit budgets, even 1-bit sign quantization.

Narration: LPLR runs in a few steps. It draws a Gaussian sketching matrix S and forms the sketch A times S, a randomized rangefinder for the column space of A, then quantizes it to get Q of A S. Next it least-squares-projects A's columns onto this quantized basis, solving for the projection W star, then quantizes W star too, returning factors L and R. The key insight: Gaussian sketches are Johnson-Lindenstrauss embeddings with an equalization property, so reconstruction error stays order one and doesn't grow with dimension, keeping LPLR accurate even at one bit.
