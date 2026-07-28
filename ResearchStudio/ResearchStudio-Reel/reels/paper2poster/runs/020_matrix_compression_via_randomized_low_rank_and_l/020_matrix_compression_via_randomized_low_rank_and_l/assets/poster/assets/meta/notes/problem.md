# Problem

Core claim: Modern matrices can contain billions of entries, making storage and computation costly, even though such matrices are often approximately low rank.

Supporting detail: Low-rank approximation alone or low-precision quantization alone each leaves compression on the table; the two structures are rarely exploited jointly with error guarantees.

Narration: Matrices are everywhere in science and machine learning, but modern ones hold billions of elements that strain memory and compute. Luckily, many are approximately low rank. Prior work exploited either low-rank structure or low-precision quantization alone; combining both in one factorization, with provable error control, stayed open.
