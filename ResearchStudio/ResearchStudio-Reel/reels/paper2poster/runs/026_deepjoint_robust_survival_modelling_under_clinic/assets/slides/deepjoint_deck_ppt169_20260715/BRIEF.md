# DeepJoint deck — authoring brief (paper2video / ppt-master)

You are the ppt-master **main agent** for this deck. Author it end-to-end in ONE
continuous pass. This is an autonomous batch run: **never stop to ask questions,
never launch the Confirm UI / browser server, never wait on a gate.** Adopt the
locked decisions below and go straight to the exported PPTX.

## Project
- PROJECT_PATH: `/datadisk/project/ResearchStudio/benchmarks/paper2poster/runs/026_deepjoint_robust_survival_modelling_under_clinic/assets/slides/deepjoint_deck_ppt169_20260715`
- PPT_MASTER skill dir: `/datadisk/project/ResearchStudio/benchmarks/paper2poster/vendor/ppt-master/skills/ppt-master`  (call scripts as `python3 <skilldir>/scripts/<script>.py`; use `python3` = /datadisk/project/miniconda3/bin/python3)
- Canvas: **ppt169 = 1280×720**, viewBox `0 0 1280 720`.
- Route: **free design, flat mode** (`pptx_structure.mode: flat`). No templates, no Master/Layout/placeholder metadata.
- Deck length: **exactly 10 slides**, filenames `01_title.svg` … `10_takeaway.svg` in `svg_output/`, in the exact order below. Slide count MUST equal 10.

## Locked design system (write into design_spec.md §III/§IV and spec_lock.md)
Visual style: **swiss-minimal** (references/visual-styles/swiss-minimal.md). Mode: **briefing** (references/modes/briefing.md). Clean grid, generous whitespace, one strong accent, confident numerals, thin rules. NOT a uniform card-grid on every page — vary rhythm.

Palette:
- background `#F4F6F9`
- surface/card `#FFFFFF`, hairline border `#DCE2EA`
- ink / heading `#0E1B2B`
- body text `#3A4658`
- muted `#6B7787`
- primary accent (cobalt) `#1E63E9`
- secondary accent (teal) `#0FA3A3`
- warm highlight for contrast marks `#E4572E`

Typography (px, canvas 1280×720):
- Heading font css stack: `"Inter","Segoe UI",system-ui,"Helvetica Neue",Arial,sans-serif`; weight 700.
- Body same stack, weight 400/500.
- Sizes: slide H1 ~40; slide kicker/eyebrow ~15 uppercase letter-spaced; card title ~20; body ~18–20; big KPI numerals 56–84; caption ~13.
- Keep on-slide text SHORT (the narration carries detail). Prefer phrases, numbers, labels over paragraphs.

## Title-slide utility assets (slide 01 only)
Images are already in `images/`:
- `logo_cambridge.png`, `logo_manchester.png` — institute logos, small, aligned, right/lower title area.
- `qr_code.png` (label "Code"), `qr_paper.png` (label "Paper") — small labeled QR tiles, lower-right safe zone.
Keep title + hook dominant; logos/QR are a restrained utility cluster. Omit cleanly if a file is missing; never leave broken boxes or literal paths.

## Paper figures available in `images/` (embed where noted; do NOT read them as pixels — place by filename)
- `arch_fig1.png` (1391×677) — the real DeepJoint architecture: LSTM → embedding h → heads L (longitudinal), I (inter-observation time), M (missingness), S (survival). USE on slide 05 (Method) as the central visual.
- `cindex_fig4.png` (4198×927, very wide/low-legibility) — optional small supporting strip only; PREFER an authored bar chart on slide 07.
- `tests24h_fig3.png`, `robust_fig2.png` — optional supporting; prefer authored mini-schematics.

## Cue anchors (CRITICAL for the video highlight pass)
On each slide, wrap the visible content region that a narration chunk talks about in a **top-level `<g id="cue_...">`** using the exact `anchor_id` values in `CUE_ANCHORS.md` (same folder). Rules:
- Put the anchor on the REAL content element (card / KPI tile / figure panel / chart row / equation block / definition chip) — never on the page background, heading bar, eyebrow, logo, or QR.
- Add a child `<desc>` containing that chunk's keywords (from CUE_ANCHORS.md) so the semantic matcher can confirm overlap. You may also set `data-cue-label="<anchor_id>"`.
- Create one wrapping group per listed chunk. If a slide lists 4 chunks, make 4 distinct anchored regions (design the slide so there are 4 discussable elements). Anchors must be visible, non-overlapping, and reasonably sized (a card/tile, not a whole half-slide, not a single word).
- These `<g>` wrappers are ALSO the normal content groups — keep all visible children inside them.

## Slides (order fixed; id must appear as file prefix)

### 01 title
- H1 wordmark: **DeepJoint**. Sub: *Robust Survival Modelling Under Clinical Presence Shift*.
- Authors: Vincent Jeanselme¹, Glen Martin², Niels Peek², Matthew Sperrin², Brian Tom¹, Jessica Barrett¹. Affil: ¹University of Cambridge (MRC Biostatistics Unit) · ²University of Manchester. Venue: **NeurIPS 2022**. arXiv 2205.13481.
- Hook line: "How clinical data are observed is itself informative — model it, and survival predictions get both more accurate and more transportable."
- A small right-side schematic chip: embedding → {L, I, M} + S (four heads) — supports anchor c4.
- Anchors: c1 = title/wordmark block; c2 = a "clinical presence" definition chip; c3 = a small "practice shift → models degrade" chip; c4 = the four-heads schematic chip. Utility cluster (logos+QR) is NOT an anchor.

### 02 problem — "The observation process is informative"
- c1 card: *Data = patient × health-system interaction* (small icon of patient↔clinician).
- c2 card: *A test's timing and its existence carry information about the patient.*
- c3 card: *Most models assume sampling is non-informative.*
- c4 full-width banner (accent): *Ignoring clinical presence → sub-optimal, non-transportable models. Modelling it explicitly is the fix.*

### 03 motivation — "Clinical presence shifts — and models break"
- c1 card: *Heterogeneity — the same population looks different under a different observation process; shifts across countries, time, and weekday ↔ weekend.* (a small weekday/weekend contrast motif)
- c2 card: *ML has studied covariate & label shift; the shift in the observation process itself is under-explored.*
- c3 accent card / question: *DeepJoint's question — does explicitly modelling clinical presence make survival models robust to this shift?*

### 04 contribution — "A joint model of clinical presence + survival"
- c1 card: *Treat clinical presence as multi-task learning.*
- c2 card: *One shared recurrent embedding → four heads: longitudinal · inter-observation timing · missingness · survival; combined likelihood, dynamic weighting, end-to-end.* (row of 4 labeled chips L·I·M·S)
- c3 accent card: *Result — a representation that encodes the observation process: a predictive edge AND robustness when practice changes.*

### 05 method — "Architecture: one embedding, four heads"  (embed arch_fig1.png as the hero visual)
- c1 region: the LSTM→embedding part of the figure (or a caption chip beside it): *LSTM encodes each patient's irregular lab-test sequence into embedding h.*
- c2 region: the L/I/M heads legend: *Three clinical-presence heads — L: next values (Gaussian) · M: which tests appear (Bernoulli) · I: inter-observation intensity.*
- c3 region: the S head chip: *DeepSurv head — survival under Cox proportional hazards.*
- c4 equation block (render as crisp text/Unicode, not an image): `ℓ(e) = (1−α)·ℓ_S + α·Σ_{task∈{L,I,M}} w_task(e)·ℓ_task(e)` with caption *dynamic weighting, balanced by α, optimised end-to-end.*

### 06 dataset-benchmark — "MIMIC-III ICU laboratory tests"
- c1 card: *MIMIC-III — Beth Israel Deaconess, 2001–2012, >38,000 patients, anonymised labs.*
- c2 KPI tile: *30,834 patients* (survived first 24 h) + *17 lab tests*.
- c3 card: *Predict in-hospital survival from the embedding at the last observation in day 1; time-dependent C-index & Brier at 1 / 7 / 14 days; 90/10 patient split.*

### 07 key-result — "Modelling clinical presence lifts short-horizon discrimination"
- Author a clean **horizontal bar chart** of 1-day C-index (label each bar with its value, higher = better):
  Ignore-LSTM **0.853** · GRU-D **0.855** · DeepJoint (labs only) **0.862** · DeepJointFineTune **0.878** (highlight the last in accent). Axis start ~0.84 to make gaps legible; label the axis meaning.
- c1 region: chart title/frame: *Three proposed methods are competitive-to-best vs same-input models.*
- c2 region: the DeepJoint (0.862) bar cluster: *DeepJoint sees only lab values yet beats Ignore-LSTM and GRU-D (which takes missingness as input).*
- c3 side card: *Modelling the observation process — even without feeding it in — yields a better embedding.*
- c4: the DeepJointFineTune 0.878 bar (accent) + a KPI callout *0.878 best 1-day C-index.*

### 08 ablation-study — "Variants × baselines: discrimination and robustness"
- c1 card: *3 variants (DeepJoint · DeepJointFeature · DeepJointFineTune) vs 6 baselines (Last · Count · Ignore · Resample · Feature · GRU-D).*
- c2 card: *DeepJointFeature > plain DeepJoint, and matches the strong Feature baseline.*
- c3 card: *DeepJointFineTune — highest internal discrimination, but overfits under observation-process shift.*
- c4 region: a small **robustness "closeness-to-diagonal" schematic** (transferred vs oracle C-index, y=x line; mark DeepJointFeature on the diagonal): *DeepJointFeature sits closest to the diagonal → transfers most reliably.*

### 09 headline-numbers — big-number tiles
- c1 tiles: **0.878** (1-day C-index) and **30,834** (MIMIC-III patients).
- c2 tiles: **3** (clinical-presence dimensions: longitudinal · timing · missingness, + survival) and **1 / 7 / 14** (day horizons).
- Swiss-minimal oversized numerals, thin labels.

### 10 takeaway — "Clinical presence is signal, not noise"
- c1 statement card: *The way clinical data are sampled is itself informative; jointly modelling the observation process with survival gives predictions that are both more accurate and markedly more robust when practice changes.*
- c2 accent card: *Model it → transportable medical predictions.*
- Footer: arXiv 2205.13481 · code github.com/Jeanselme/ClinicalPresence; small Paper/Code QR tiles ok.

## Execution steps (run in order; do NOT bundle)
1. Read: `references/executor-base.md`, `references/shared-standards.md`, `references/native-shape-authoring.md`, `references/visual-styles/swiss-minimal.md`, `references/modes/briefing.md`, and `templates/design_spec_reference.md` + `templates/spec_lock_reference.md` for structure.
2. Write `design_spec.md` (full I–X structure) and `spec_lock.md` (flat mode, the locked palette/fonts above, 10 pages). List the embedded images in §VIII (`Acquire Via: user`, `Status: Generated`).
3. Author the 10 SVGs sequentially into `svg_output/`, spec_lock re-read discipline, cue anchors embedded. After page 1, run `svg_quality_checker.py <proj>/svg_output/01_title.svg` and fix all errors before continuing.
4. After all 10: `python3 <skilldir>/scripts/svg_quality_checker.py <PROJECT_PATH>` → fix every **error** (warnings ok). Must reach 0 errors.
5. Write speaker notes `notes/total.md` (a `## 01_title` … section per slide is fine; brief).
6. `python3 <skilldir>/scripts/total_md_split.py <PROJECT_PATH>`
7. `python3 <skilldir>/scripts/finalize_svg.py <PROJECT_PATH>`
8. `python3 <skilldir>/scripts/svg_to_pptx.py <PROJECT_PATH>`  → note the exact `exports/*.pptx` path printed.

## SVG constraints (from shared-standards — must hold or export/quality fails)
- Every SVG: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" ...>`; all content within 1280×720; no text overflow past canvas or out of its card; no overlapping text.
- No unsupported filters/features the quality checker bans; keep gradients/shapes simple. Embed images with `<image href="images/xxx.png" ...>` and correct `preserveAspectRatio`.
- Top-level logical groups are `<g id="...">`; the cue groups satisfy this.
- Font sizes/colours come ONLY from the locked system above.

## Return when done
Report: the exact exported `exports/<name>.pptx` path, the final `svg_quality_checker.py` error count (must be 0), the slide count (must be 10), and any figure you could not place. If anything blocks, fix it yourself (this is autonomous) — only report a blocker if it needs a missing OS dependency.
