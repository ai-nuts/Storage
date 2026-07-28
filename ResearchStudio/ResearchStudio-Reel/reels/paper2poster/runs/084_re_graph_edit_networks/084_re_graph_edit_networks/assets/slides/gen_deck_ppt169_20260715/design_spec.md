# Design Specification & Content Outline

## I. Direction
- Source: "[Re] Graph Edit Networks" (Stropnik & Oražem, ReScience C 2022), a reproducibility study.
- Core message: Graph Edit Networks are reproducible and interpretable; most original claims hold, but one scaling claim is corrected and several benchmarks are shown to reward memorisation.
- Audience: ML researchers / reproducibility-minded practitioners.
- Mode: flat free-design, 16:9, 9 pages, one page per narration section.
- Tone: precise, restrained academic; verdict-driven (green = confirmed, red = refuted).

## II. Canvas
- 1280×720, viewBox 0 0 1280 720.

## III. Color
- Deep navy primary (#16324F), warm orange accent (#E8743B), cool blue secondary (#3E7CB1).
- Semantic: success green (#2E7D32) for claims that hold, warning red (#C62828) for the refuted claim.

## IV. Typography
- Arial / Helvetica sans stack; body 18px, section title 32px, hero number 64px.

## V. Icons / VIII. Images
- No raster images and no icon-library `<use>` refs. Simple glyphs (checks, arrows, nodes/edges) drawn as native SVG shapes.

## IX. Content Outline (one slide per script section)
1. title — paper title, reproduction framing, 4-claim audit.
2. problem — graph time-series prediction; standard GNNs emit probabilities, not structural ops.
3. motivation — GEN closes the gap with an edit script; three appealing original claims on under-documented benchmarks.
4. contribution — four contributions of the reproduction.
5. method — GNN backbone + edit vocabulary; apply-in-sequence Gt→Gt+1; GED-approximated training, two losses, edge filtering.
6. dataset-benchmark — three benchmark families (dynamical, tree, arXiv citation scaling).
7. key-result — 3 of 4 claims hold; the linear backward-scaling claim fails (exponent > 1).
8. ablation-study — two robustness checks; tree generators mostly unsimplifiable (13% / 26% usable).
9. takeaway — nuanced verdict: reproducible & interpretable, but scaling corrected and benchmarks reward memorisation.

Each slide carries `cue_sNN_cM_*` anchor groups (id + <title>/<desc> keywords) matching assets/meta/visual_anchor_contract.json.
