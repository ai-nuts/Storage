# Design Specification — Neuroformer (paper2video deck)

## I. Direction
- Canvas: PPT 16:9 (1280×720), 10 slides matching the paper2assets narration order (title, problem, motivation, contribution, method, dataset-benchmark, key-result, ablation-study, headline-numbers, takeaway).
- Audience: technical ML / computational-neuroscience audience watching a 3-minute narrated summary.
- Core message: a self-supervised, multimodal generative transformer brings the pretraining paradigm to systems neuroscience — recovering circuit connectivity and decoding behavior.
- Mode: briefing. Visual style: swiss-minimal (generous whitespace, strong type hierarchy, thin rules, restrained cobalt/teal/warm accents).

## II. Layout system
- Left rule + top accent bar as persistent chrome. 72px side margins.
- Persistent header (eyebrow kicker + slide title + accent underline) on content slides; persistent footer ("Neuroformer · ICLR 2024" left, "NN / 10" right).
- Content built from cards / rows / figure panels; each narration chunk maps to a visible `cue_*` anchor group carrying its keywords in `<title>`/`<desc>` for the video highlight contract.

## III. Color — see spec_lock.md
Cobalt #2F5BEA primary, teal #12A594 secondary, warm #E8663D for numbers/emphasis, ink #12161D, body #444B55 on white / #F3F5F9 panels.

## IV. Typography
Inter family (installed on the render host; frames are rendered from svg_final via Chrome, so Inter is faithful; PPTX export maps to the theme font and PowerPoint substitutes a system sans — geometry is fixed by explicit SVG coordinates, so substitution does not reflow the layout). Cover title 88, section title 40, subtitle 27, body 24, lead 20, annotation 17, footnote 13, hero number 56.

## V. Figures
Paper figures reused: figure1 (architecture), figure2 (ground-truth simulation), figure3 (real-data setup), figure5 (velocity prediction), figure6 (ablation). All `no-crop` (data figures).

## VI. Title assets
UC Santa Barbara logo + Code/Paper QR tiles as a restrained utility cluster on slide 1.

## VII. Visual-cue anchors
Each slide carries the exact `cue_sXX_cY_*` anchor ids from assets/meta/visual_anchor_contract.json on real content regions (cards / figure panels / number tiles), never on headers, footers, logos, or QR chrome.
