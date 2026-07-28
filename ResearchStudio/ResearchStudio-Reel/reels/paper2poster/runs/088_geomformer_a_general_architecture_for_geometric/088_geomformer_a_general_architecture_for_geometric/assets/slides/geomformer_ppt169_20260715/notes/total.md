## 01_title

Molecular modeling in quantum mechanics demands models that respect physical laws, namely invariance and equivariance to rotation and translation of atomic coordinates. This paper introduces GeoMFormer, a general and flexible Transformer-based architecture that learns both invariant and equivariant molecular representations at once. It uses two parallel Transformer streams, one for each type of representation, and bridges them with carefully designed cross-attention modules so information flows between the two. Many prior geometric models turn out to be special cases of this framework, and GeoMFormer sets new state-of-the-art results across a wide range of molecular tasks.

## 02_problem

Deep learning has become a powerful tool for molecular science, predicting properties of molecules from their three-dimensional coordinates and simulating how atoms move. But these tasks impose strict physical constraints. A model's prediction must transform correctly when the input coordinate system is rotated or translated, a requirement known as invariance for scalar quantities and equivariance for vector quantities. Existing methods handle these constraints, but most are built on heuristic and costly modules, and few offer a single general framework that learns both invariant and equivariant representations effectively at the same time.

## 03_motivation

The trouble with existing geometric models is that they are largely built by hand. Designers craft specialized equivariant modules that are either expensive to scale or so constrained that they sacrifice expressive power, and the resulting architectures grow complex just to guarantee the physical constraints. More importantly, real applications increasingly demand a single model that performs both invariant and equivariant prediction with strong accuracy. There is a clear need for a general, flexible framework built on well-understood, standard components rather than one-off heuristic modules.

## 04_contribution

The paper makes three main contributions. First, it introduces GeoMFormer, a novel Transformer-based molecular model that maintains two separate streams, one for invariant and one for equivariant representations, using only standard Transformer building blocks. Second, it designs cross-attention modules that bridge these two streams, letting each draw on contextual information from the other to enhance geometric modeling. Third, it shows that this framework is general enough that many previously proposed architectures can be viewed as special instantiations of GeoMFormer, and it backs the design with strong empirical results across a diverse set of molecular tasks.

## 05_method

GeoMFormer keeps two representations for every atom: an invariant feature vector and an equivariant three-dimensional feature. These flow through two parallel Transformer streams. Within each stream, a self-attention module first mixes information across atoms. For the equivariant stream, standard attention is modified so the attention score is computed by summing dot products over the three-dimensional Query and Key vectors, which provably preserves equivariance. Then, the key innovation, a cross-attention module lets each stream query the other: the invariant stream attends to the equivariant stream and vice versa, fusing the two kinds of geometric information. A feed-forward network completes each block, and blocks are stacked. Because the design uses only standard Transformer components arranged this way, many earlier geometric networks fall out as special cases of the framework.

## 06_dataset-benchmark

The authors evaluate GeoMFormer across a broad suite of tasks that together stress both invariant and equivariant abilities. On the Open Catalyst 2020 dataset, spanning over four hundred sixty thousand adsorbate-catalyst complexes, they test both the Initial Structure to Relaxed Energy task, which is invariant, and the Initial Structure to Relaxed Structure task, which is equivariant. On the large quantum chemistry datasets PCQM4Mv2 and Molecule3D, with millions of molecules, they predict the HOMO-LUMO energy gap. They further use a synthetic five-particle N-body simulation to test equivariant position prediction, and the MD17 dataset for force-field modeling in the ablation studies. This breadth lets a single architecture be judged on both scalar and vector prediction.

## 07_key-result

GeoMFormer delivers strong results everywhere it is tested. On the Open Catalyst energy prediction task it outperforms prior invariant models, and on the structure prediction task it excels at equivariant modeling. On the PCQM4Mv2 benchmark it reaches the lowest error among models with quadratic complexity, a six point seven percent relative reduction over the previous best, while staying efficient enough to scale to large systems. On Molecule3D it improves error by sixteen point three percent on the random split and eleven point six percent on the scaffold split. And on the N-body simulation it cuts mean squared error by a striking thirty-three point eight percent. A single architecture, built from standard Transformer parts, achieves state-of-the-art performance on both invariant and equivariant tasks.

## 08_ablation-study

To understand where the gains come from, the authors ablate each building block. The most telling finding concerns the cross-attention modules that bridge the invariant and equivariant streams. Removing them hurts sharply. On the MD17 energy prediction task, adding the invariant cross-attention gives an eighteen point seven percent relative improvement, the equivariant cross-attention gives nine point eight percent, and using both together gives twenty point eight percent. On the harder MD17 force prediction task the effect is even larger, with a sixty point eight percent relative improvement when both cross-attention modules are used. On the N-body simulation the combined improvement is seventeen point five percent. The self-attention, feed-forward, and layer-normalization modules also each contribute, but the cross-attention bridge is clearly the heart of the design.

## 09_headline-numbers

A few numbers capture the impact. On PCQM4Mv2, GeoMFormer reaches a validation error of zero point zero seven three four, the best of any quadratic-complexity model, a six point seven percent relative reduction. On the N-body simulation it achieves a mean squared error of zero point zero zero four seven, a thirty-three point eight percent reduction over the previous best. On Molecule3D it records errors of zero point zero two five two on the random split and zero point one zero four five on the scaffold split, improvements of sixteen point three and eleven point six percent. And in the ablations, adding cross-attention yields up to a sixty point eight percent relative improvement on force prediction, underscoring how central that bridge is.

## 10_takeaway

The lasting message of this work is that you do not need bespoke, heuristic modules to model molecules under physical constraints. By running two standard Transformer streams in parallel, one for invariant and one for equivariant features, and connecting them with simple cross-attention, GeoMFormer learns both kinds of representation at once and outperforms specialized architectures on a wide range of tasks. Because many earlier models are special cases of this framework, GeoMFormer offers a clean, general, and scalable design principle for geometric molecular representation learning.
