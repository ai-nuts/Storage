# Design Specification — CABINET Paper Video Deck

## I. Project Overview
- Source: CABINET (ICLR 2024), Content Relevance-Based Noise Reduction for Table Question Answering.
- Purpose: 10-slide narrated video deck aligned 1:1 with paper2assets narration sections.
- Audience: ML researchers / practitioners in table QA and LLM reasoning.
- content_divergence: balanced — faithful to the paper;每页 facts sourced from paper_spec.md.

## II. Narrative
- mode: briefing. One section per slide in canonical order: title, problem, motivation, contribution, method, dataset-benchmark, key-result, ablation-study, headline-numbers, takeaway.

## III. Color Scheme
- Background white; deep navy primary for structure; amber accent for "relevance/highlight"; teal secondary; semantic red (wrong / hard-decomposition) and green (correct).

## IV. Font Plan
- Per-role font stacks:
  - font_family: Arial, "Helvetica Neue", sans-serif
  - title_family: Arial, "Helvetica Neue", sans-serif
  - code_family: Consolas, "Courier New", monospace
- Sizes (px): cover_title 60, title 36, subtitle 24, lead 22, body 20, annotation 16, footnote 14, hero_number 52.
- Formula policy: text-only — formulas typeset as inline SVG text/tspan with Unicode symbols (η, λ, μ, σ). No PNG formula assets.

## V. Icon Usage
- Minimal; simple authored glyphs (check/cross, arrows) drawn as SVG paths. No icon library dependency.

## VI. Layout System
- Canvas 1280x720. Left 10px navy rail. Header: kicker + title at x=60. Footer rule at y=678 with paper credit and slide number. Content band y 132–662.

## VII. Visual Cue Contract
- Each slide carries 2–4 visible groups with id="cue_sNN_cM_..." matching assets/meta/visual_anchor_contract.json, each with <title>/<desc> holding narration keywords, bounding the specific discussed element.

## VIII. Image Resource List
- images/fig2_architecture.png | no-crop — Type: Diagram, Acquire Via: user, Status: Provided (method slide backbone).
- images/logo_adobe.png, images/logo_iitkgp.png, images/logo_iitr.png | no-crop — title-slide institute logos, Acquire Via: user.
- images/qr_code.png, images/qr_paper.png | no-crop — title/takeaway QR tiles, Acquire Via: user.

## IX. Content Outline
- P01 title / P02 problem / P03 motivation / P04 contribution / P05 method / P06 dataset-benchmark / P07 key-result / P08 ablation-study / P09 headline-numbers / P10 takeaway.
