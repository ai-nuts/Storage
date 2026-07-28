# Design Spec — DeLVM Research Talk Deck

## I. Project
- Title: Data-efficient Large Vision Models through Sequential Autoregression (DeLVM)
- Venue: ICML 2024 · arXiv 2402.04841 · github.com/ggjy/DeLVM
- Audience: ML researchers. Format: PPT 16:9, 1280×720, 8 slides.
- Purpose: paper-explainer video deck. One slide per narration section, fixed order and count (downstream video compositor pairs slide N to audio N).

## II. Visual Direction
- Clean modern academic-tech. Light background (#FFFFFF), generous whitespace, strong typographic hierarchy.
- One primary (deep navy #14264A) + one accent (cobalt #2563EB), teal #0EA5A4 as restrained secondary accent for "efficiency / student" motifs. Neutral gray text ramp.
- Serif (Georgia) for titles/emphasis, sans (Arial) for body. Consistent header treatment (accent tab + serif title + kicker) across all content pages. No shadows except at most 2 floating elements per page.

## III. Typography
- cover_title 54 / chapter_title 44 / title 34 / subtitle 24 / body 20 / annotation 14 / footnote 11 / hero_number 40. All structural roles fixed deck-wide from spec_lock.

## IV. Color Roles
- primary navy: titles, key figures. accent cobalt: kickers, accent tabs, emphasis, augmentation motif. teal: distillation / student / efficiency motif. success green: winning results. warning: collapse / forgetting failure states.

## V. Page Roster (mandatory slide↔section map)
1. P01 title (anchor) — cover: title, authors, ICML 2024, hook "do we really need 3B params + 400B tokens?", two-idea thesis (augmentation + distillation). Logo cluster (Sydney, BIT, Huawei Noah's Ark) + QR (Paper, Code).
2. P02 problem (dense) — AR LVM needs >3B params, ~400B tokens, >1B images; expensive, edge-impractical; long-tail (segmentation abundant vs pose starved) → rare tasks unlearned.
3. P03 motivation (dense) — LMs 1 epoch over vast corpora; CV tiny datasets so schedule fails; field keeps scaling while classical remedies untried in AR vision; this paper closes the gap.
4. P04 contribution (dense) — three contributions (simple aug rebalances long-tail; first KD for AR LVMs, LLaMA-1B→300M; practical 80M reaching 83% ImageNet). figure1 framework banner.
5. P05 dataset-benchmark (dense) — tasks seg SA-1B 1–10%, pose COCO-Pose, derain Rain13K; validation SA-1B/MPII/Test2800; Pascal-5i mIoU; ImageNet; VQGAN tokenizer on Laion off the shelf.
6. P06 key-result (dense) — balancing via augmentation beats mixture & resampling (collapses); KD improves student on 3 tasks single+multi; Pascal-5i distilled+finetuned 300M beats scratch; scaling seg 1→10% lowers loss ~0.19 / perplexity 22.4, aug reproduces with no new data. figure2 loss curves + figure3 balancing visualizations.
7. P07 ablation-study (dense) — prompt background color controls generated bg (black-bg → reliable grayscale-threshold post-proc); no-shuffle → catastrophic forgetting (earlier-task perplexity into thousands); even 80M, KD still improves val perplexity on all 3 tasks. figure5 + figure6.
8. P08 takeaway (anchor) — you don't need 3B params + hundreds of billions of tokens; two classical techniques let compact limited-data models perform strongly; 80M hits 83% ImageNet → efficient deployable generalist vision unifying generation + understanding.

## VI. Headline Numbers
- 3B params / ~400B tokens / 1.64B images baseline vs compact 300M / 80M student.
- 83.04% ImageNet top-1 (LLaMA-80M, aug + KD).
- SA-1B 1%→10% (0.34B→3.43B tokens): val loss −0.19, perplexity −22.4.
- Pascal-5i mIoU distilled+finetuned 300M: 18.58 / 21.32 / 19.90 / 21.08 (splits 0–3).

## VII. Visualizations
- P02: imbalance mini-bars (long-tail) + big-number KPI cards. P06: comparison columns (balancing schemes) + real figure2 loss curves. Real paper figures placed as image panels on P04 (figure1), P06 (figure2, figure3), P07 (figure5, figure6).

## VIII. Images
- Real paper figures figure1–figure6 (no-crop, meet). Institute logos + QR (Paper/Code) on cover only. image_usage = provided; no generation, no search.

## IX. Per-page content — see narration.json sections in order; each page renders its section's meaning. Formula policy: text-only Unicode. Cue anchors: each page carries 3–4 top-level <g id="cue_sNN_cM_..."> groups with <title>/<desc> echoing cue keywords, wrapping the real content region the narration discusses (never header/logo/QR/background).
