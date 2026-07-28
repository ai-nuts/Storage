# Design Specification — CITransNet paper video deck

## I. Direction
- Source: "A Context-Integrated Transformer-Based Neural Network for Auction Design" (ICML 2022), Duan et al., Peking University / Google.
- Purpose: 3-minute narrated explainer video; one slide per narration section (10 slides).
- Audience: ML / mechanism-design researchers and practitioners.
- Content divergence: faithful to the paper; numbers and named settings preserved exactly.

## II. Canvas
- 1280×720 (PPT 16:9), flat free-design (`pptx_structure.mode: flat`).

## III. Color Scheme
- Ink navy `#14264C` (primary text + structure), cobalt `#2563EB` (accent / method / links), amber `#D98A0B` (revenue / headline numbers), light panel `#F3F6FB`, hairline `#DCE2EC` on white `#FFFFFF`.

## IV. Font Plan
- Single Arial-led sans stack, Windows-safe. Baseline body 24 px; cover_title 72, title 44, subtitle 30, subheading 28, lead 26, hero_number 60, annotation 18, footnote 16.

## V. Visual style
- swiss-minimal: strict grid, generous whitespace, hairline rules, restrained accent color, no gradients-as-decoration, numbers as the visual focus.

## VIII. Image Resource List
- figure1.png (CITransNet architecture schematic) — method slide, `Acquire Via: user`, `no-crop`.
- figure2.png (out-of-setting generalization) — takeaway slide, `Acquire Via: user`, `no-crop`.
- logo_pku/google/deepmind.png, qr_code/paper.png — title slide utility cluster, `Acquire Via: user`, `no-crop`.

## IX. Content Outline
1. title — CITransNet title / authors / venue / logos / QR
2. problem — revenue-max + IC open problem; Myerson 1981; deep methods fixed/symmetric
3. motivation — real auctions richer (e-commerce); need context + varying sizes
4. contribution — contextual RegretNet + sample-complexity bound; CITransNet properties
5. method — architecture (3 inputs, embed, transformer interaction layers, output) + figure1
6. dataset-benchmark — 9 settings; A–C single-item (Myerson), D–I multi-item up to 5×10
7. key-result — recovers Myerson single-item; beats Item-wise Myerson all 6 multi-item
8. ablation-study — CIRegretNet/CIEquivariantNet earn less; removing context hurts
9. headline-numbers — 0.593/0.594, 6.872/6.509, 1.177/1.071, 6/6 wins, regret ≤0.003
10. takeaway — context as first-class input; scale-independent transfer + figure2
