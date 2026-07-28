# DeepJoint — Design Spec

> Human-readable design narrative. Machine-readable execution contract lives in `spec_lock.md`; on divergence spec_lock wins.

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | deepjoint_deck_ppt169_20260715 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 10 |
| **Design Style** | swiss-minimal |
| **Target Audience** | ML / clinical-ML research audience (NeurIPS) |
| **Use Case** | Conference paper walkthrough deck (narrated video source) |
| **Delivery Purpose** | text / read-close — body baseline 20px |
| **Content Strategy** | Faithful to the paper; distilled to short on-slide phrases, narration carries detail |
| **Created Date** | 2026-07-15 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | left/right 64px, top 56px, bottom 48px |
| **Content Area** | 1152×616 inside margins |

---

## III. Visual Theme

### Theme Style

- **Mode**: briefing (neutral, complete, topic-titled)
- **Visual style**: swiss-minimal (modular grid, aggressive whitespace, one accent, thin rules, flat — no shadows/gradients)
- **Theme**: Light
- **Tone**: precise, academic, confident

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#F4F6F9` | Page background |
| **Secondary bg / Surface** | `#FFFFFF` | Cards, tiles, panels |
| **Primary (cobalt)** | `#1E63E9` | Accent bars, key marks, highlight bar |
| **Accent (teal)** | `#0FA3A3` | Secondary emphasis, chips |
| **Warm highlight** | `#E4572E` | Single contrast mark (best result, key shift) |
| **Body text** | `#3A4658` | Body copy |
| **Secondary text (muted)** | `#6B7787` | Captions, labels |
| **Ink / heading** | `#0E1B2B` | Titles, KPI numerals |
| **Border/divider** | `#DCE2EA` | Hairline card borders, rules |

No gradients, no shadows (swiss-minimal is strictly flat). The accent appears at a single point per page.

---

## IV. Typography System

### Font Plan

**Typography direction**: single neo-grotesque family, weight contrast (700 headings / 400–500 body). PPT-safe: lead stack with Segoe UI (pre-installed) so native export resolves cleanly; Inter kept as a browser-preview nicety only.

**Per-role font stacks**:

- Title: `"Segoe UI", "Inter", "Helvetica Neue", Arial, sans-serif`
- Body: `"Segoe UI", "Inter", "Helvetica Neue", Arial, sans-serif`

> Note: the source brief named an Inter-led stack. Inter is not a guaranteed pre-installed export face, so the exported Latin face is Segoe UI (a neo-grotesque of the same character); Inter is retained only for on-screen preview. No font-install requirement is introduced.

### Font Size Hierarchy (unitless px, body anchor)

- Body content = **20**
- Page title (H1) = 40 (2.0x)
- Lead / sub = 26 (1.3x)
- Card / subheading title = 24 (1.2x)
- Eyebrow / annotation = 15 (0.75x, uppercase letter-spaced)
- Footnote / page number = 13 (0.65x)
- KPI numeral = 64 (3.2x, feature)
- Hero numeral = 84 (4.2x, feature)

All sizes sit inside the 0.5–5.0x ramp envelope.

---

## V. Layout Principles

- **Header** (every slide): eyebrow kicker (cobalt, uppercase) + H1 topic title + thin cobalt rule. Left-flush to the 64px margin.
- **Content**: modular grid — asymmetric splits, card rows, KPI tiles, one authored bar chart, one embedded architecture figure. Rhythm varies (not a uniform card grid every page).
- **Footer**: slide number `NN / 10` + running tag `DeepJoint · NeurIPS 2022`.
- Card radius rx=4, 1px `#DCE2EA` border, flat white; a 4px cobalt accent rule marks the focal card per page.

---

## VI. Icon Usage Specification

No icon library used — swiss-minimal relies on type, rule, and geometry. Small motifs are authored as native SVG primitives (dots, chips, rules).

---

## VII. Visualization Reference List

| Page | Template | Path | Summary-quote | Usage |
| ---- | -------- | ---- | ------------- | ----- |
| P07 | (authored) horizontal_bar | no-template-match | designed from scratch | 1-day C-index across four same-input models |

Slide 08 uses a small authored closeness-to-diagonal schematic (no chart template). No `templates/charts/` templates adapted.

---

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | text_policy | page_role |
| -------- | --------- | ----- | ------- | ---- | -------------- | ----------- | ------ | ----------- | --------- |
| arch_fig1.png | 1391×677 | 2.06 | DeepJoint architecture (LSTM→embedding→L/I/M/S heads) — hero on P05 | Diagram | #44 background figure + native caption chips | user | Generated | embedded | local |
| logo_cambridge.png | 1537×312 | 4.93 | Institute logo, title utility cluster | Logo | #49 utility cluster | user | Generated | embedded | local |
| logo_manchester.png | 543×169 | 3.21 | Institute logo, title utility cluster | Logo | #49 utility cluster | user | Generated | embedded | local |
| qr_code.png | 444×444 | 1.0 | Code QR tile (P01, P10) | QR | #49 utility cluster | user | Generated | none | local |
| qr_paper.png | 396×396 | 1.0 | Paper QR tile (P01, P10) | QR | #49 utility cluster | user | Generated | none | local |

---

## IX. Content Outline

1. **01 title** — DeepJoint wordmark, subtitle, authors/affil/venue, hook line, four-heads schematic chip, logo+QR utility cluster.
2. **02 problem** — the observation process is informative (4 blocks + accent banner).
3. **03 motivation** — clinical presence shifts and models break (heterogeneity, shift literature gap, DeepJoint question).
4. **04 contribution** — a joint model of clinical presence + survival (multi-task, four heads L·I·M·S, robustness result).
5. **05 method** — architecture figure hero + L/I/M/S caption chips + dynamic-weighting equation.
6. **06 dataset-benchmark** — MIMIC-III, 30,834 patients / 17 labs KPI, evaluation protocol.
7. **07 key-result** — authored horizontal bar chart of 1-day C-index (0.853/0.855/0.862/0.878), 0.878 highlighted.
8. **08 ablation** — 3 variants × 6 baselines, DeepJointFeature vs Feature, fine-tune overfits, closeness-to-diagonal schematic.
9. **09 headline-numbers** — oversized numerals 0.878 / 30,834 / 3 / 1·7·14.
10. **10 takeaway** — clinical presence is signal not noise; model it → transportable predictions; footer arXiv + code + QR.

---

## X. Speaker Notes Requirements

One note file per page in `notes/`, matching SVG names. Even, factual, plain briefing register.
