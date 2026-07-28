# GeoMFormer — Design Specification & Content Outline

## I. Direction
- Core message: A single, general Transformer architecture (two parallel streams bridged by cross-attention) learns both invariant and equivariant molecular representations and beats specialized geometric models.
- Audience: ML / geometric deep-learning researchers and practitioners.
- Delivery purpose: conference-style paper explainer video (10 slides, ~7 min narration).
- Content divergence: faithful to the paper; numbers verbatim from paper_spec.

## II. Visual System
- Swiss-minimal briefing deck. Generous whitespace, thin rules, one consistent header zone, page numbers.
- Semantic dual-color system matching Figure 1: **invariant = crimson `#C81E5A`**, **equivariant = blue `#1C6DD0`**. Neutral navy ink `#14213D` for structure.

## III. Color — see spec_lock.md
## IV. Typography — Inter family; body 22px, title 40px; sizes in spec_lock.md
## V. Icons — none (geometry/diagram-driven)
## VI. Formula policy — text-only (Unicode) for the equivariant attention score

## VIII. Image Resource List
| id | file | Acquire Via | Status | Type |
|---|---|---|---|---|
| figure1_architecture | images/figure1_architecture.png | user | Ready | Figure |
| logo_pku | images/logo_pku.png | user | Ready | Logo |
| logo_msr | images/logo_msr.png | user | Ready | Logo |
| qr_code | images/qr_code.png | user | Ready | QR |
| qr_paper | images/qr_paper.png | user | Ready | QR |

## IX. Content Outline (slide order matches narration section ids)
1. **title** — GeoMFormer title, authors, venue, two-stream + SOTA badges, logos/QR.
2. **problem** — DL for molecules; physical constraints; invariance/equivariance definition; the gap.
3. **motivation** — hand-built heuristic modules; scale/expressiveness tradeoff; demand for one model; need for a general framework.
4. **contribution** — three contributions: two-stream model; cross-attention bridge; generality + strong results.
5. **method** — two parallel streams (Inv/Equ), self-attn + cross-attn + FFN per block; equivariant attention score formula; cross-attention as the bridge.
6. **dataset-benchmark** — OC20; PCQM4Mv2 + Molecule3D; N-body + MD17; invariant vs equivariant coverage.
7. **key-result** — OC20 both tasks; PCQM4Mv2 6.7%; Molecule3D 16.3/11.6 + N-body 33.8%; single-architecture SOTA.
8. **ablation-study** — cross-attention is the heart; MD17 energy, MD17 force (up to 60.8%), N-body.
9. **headline-numbers** — KPI grid: PCQM4Mv2 0.0734; N-body 0.0047; Molecule3D 0.0252/0.1045; ablation 60.8%.
10. **takeaway** — no bespoke modules; two streams + cross-attn; prior models as special cases; general principle.
