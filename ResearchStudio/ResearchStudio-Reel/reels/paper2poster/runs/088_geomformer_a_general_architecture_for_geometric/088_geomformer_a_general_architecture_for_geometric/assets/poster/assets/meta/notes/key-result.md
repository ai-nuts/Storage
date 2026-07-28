# Key Result

Core claim: GeoMFormer sets state-of-the-art or highly competitive results across all benchmarks: it outperforms baselines on OC20 IS2RE and IS2RS, achieves the lowest MAE among quadratic-complexity models on PCQM4Mv2, and beats all baselines on Molecule3D and the N-body simulation.

Supporting detail: On N-body simulation the MSE drops 33.8% versus the previous best; on Molecule3D it cuts MAE by 16.3% (random) and 11.6% (scaffold); on PCQM4Mv2 it reduces MAE 6.7% relative to the previous best quadratic model, all with O(n²) complexity.

Narration: GeoMFormer delivers strong results everywhere it is tested. On the Open Catalyst energy prediction task it outperforms prior invariant models, and on the structure prediction task it excels at equivariant modeling. On the PCQM4Mv2 benchmark it reaches the lowest error among models with quadratic complexity, a six point seven percent relative reduction over the previous best, while staying efficient enough to scale to large systems. On Molecule3D it improves error by sixteen point three percent on the random split and eleven point six percent on the scaffold split. And on the N-body simulation it cuts mean squared error by a striking thirty-three point eight percent. A single architecture, built from standard Transformer parts, achieves state-of-the-art performance on both invariant and equivariant tasks.
