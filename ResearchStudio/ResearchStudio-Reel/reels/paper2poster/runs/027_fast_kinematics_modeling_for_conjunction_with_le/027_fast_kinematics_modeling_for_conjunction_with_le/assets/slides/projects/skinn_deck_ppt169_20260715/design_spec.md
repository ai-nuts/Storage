---
kind: free-design
canvas: ppt169 (1280x720)
mode: flat
visual_style: deep-space-editorial
---

# Design Specification — SKiNN (NeurIPS 2022 ML4PS)

## I. Direction
Explain SKiNN, a neural-network emulator of the JAM stellar-kinematics physics code, used inside a joint gravitational-lensing + kinematics modeling framework to measure the Hubble constant. Audience: ML-for-science researchers and astrophysicists. Register: confident, precise, research-talk. 10 slides, one per narration section (title, problem, motivation, contribution, method, dataset, key-result, ablation, headline-numbers, takeaway).

## II. Canvas
16:9, 1280x720, flat free-design (one Master + Blank Layout on export).

## III. Color Scheme (deep-space editorial)
- background: #0B1220 → #10203A vertical gradient
- panel: #16233B ; card: #1B2C48 → #14223A ; hairline/border: #2A3B57
- primary accent (SKiNN): #FF7A3D ; light #FF9B66
- secondary accent (lensing): #4F9DFF ; light #7DBBFF
- success: #35D0A5
- text primary: #EAF1FB ; muted: #9DB0CC ; faint: #6B7E9C

Semantic color pairing follows Figure 1 of the paper: blue = traditional lens modeling, orange = SKiNN.

## IV. Typography
Font family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif (Arial-safe fallback for LibreOffice/Chrome rendering).
- Slide title: 44px bold
- Kicker: 17px, letter-spaced, uppercase
- Card title: 22-26px bold
- Body: 18-20px
- Big stat: 54-96px bold
Formula policy: text-only (Unicode math), no PNG formula assets.

## V. Page Structure (repeating frame)
Header: numbered kicker chip + slide title + short orange accent rule. Footer: SKiNN wordmark (left), venue + page number (right). Body: 2-4 semantic content groups (cards / figure + cards).

## VI. Visual cue anchors
Each slide carries 3-4 top-level content groups whose id is the video cue anchor id `cue_sNN_cM_...` (from visual_anchor_contract.json), plus a `data-cue-label` of narration keywords and a `<title>`. These bound the exact visual the narration discusses.

## VII. Figures
- fig1_framework.png — Figure 1 joint modeling framework (blue lens path / orange SKiNN path) → contribution + method slides.
- fig2_accuracy.png — Figure 2 SKiNN vs JAM vrms images + relative-error histograms within the 2-arcsec circle → key-result slide.

## VIII. Image Resource List
| File | Type | Acquire Via | Status |
|---|---|---|---|
| images/fig1_framework.png | Figure | user | Ready |
| images/fig2_accuracy.png | Figure | user | Ready |
| images/qr_project.png | QR | user | Ready |
| images/qr_code.png | QR | user | Ready |
| images/logo_eth.png / logo_mpa.png / logo_epfl.png | Logo | user | Ready |

## IX. Content Outline
Sourced 1:1 from assets/meta/paper_spec.md and the narration script; no invented numbers.
