# Design Specification — VectorMapNet paper video deck

## I. Project Context
- Source: VectorMapNet: End-to-end Vectorized HD Map Learning (ICML 2023).
- Purpose: 10-slide narrated paper walkthrough matching the paper2assets narration section order (title, problem, motivation, contribution, method, dataset-benchmark, key-result, ablation-study, headline-numbers, takeaway).
- content_divergence: faithful to the paper; every claim/number sourced from paper_spec.md.

## II. Audience & Message
- Audience: ML / autonomous-driving researchers and practitioners.
- Core message: HD mapping does not need a rasterize-then-vectorize detour; posing it as detection + autoregressive polyline generation yields clean vector maps end-to-end and a double-digit mAP lead.

## III. Color Scheme
- Near-white field (#FFFFFF); ink #111418; single cobalt accent #1857D6 reserved for VectorMapNet / focal points; HDMapNet baseline rendered in muted grey. No gradients on content, flat.

## IV. Typography
- Single sans-serif family (Arial / Segoe UI). Weight contrast for hierarchy. Body 24px baseline. Left-aligned, flush.

## V. Mode & Style
- mode: narrative (scenario -> conflict -> resolution across the arc). visual_style: swiss-minimal (vast whitespace, few large exact elements, one accent point).

## VI. Structure / Rhythm
- 10 pages; anchor covers at start/end, one breathing turn at motivation, dense info pages for method/results/ablation.

## VII. Charts
- Key-result and headline pages use hand-authored SVG bar/number visuals (VectorMapNet vs HDMapNet). No template charts.

## VIII. Image Resource List
- figure1 overview / figure2 architecture / figure3 keypoint reps / figure4 qualitative — Acquire Via: user, Status: Present.
- institute logos + code/paper QR — Acquire Via: user, Status: Present (title utility cluster).

## IX. Content Outline
- Per-slide narration is authored in assets/audio/script.json; each slide carries the contracted cue_ anchors from visual_anchor_contract.json on its key visual targets.

## X. Execution Lock
- See spec_lock.md (mode: flat, swiss-minimal, narrative).
