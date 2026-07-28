# Shared SVG authoring contract — DARTFormer paper2video deck

You are authoring ONE slide of a 10-slide narrated video deck about the paper
"DARTFormer: Finding the Best Type of Attention" (Brown, Zhao, Shumailov, Mullins, 2022; arXiv:2210.00641).
Visual style: **swiss-minimal** — a strict modular grid, sharp geometry, generous whitespace,
one indigo accent, one restrained red used ONLY for the negative/cautionary finding.

## Canvas & file
- Canvas is 1280x720. Root MUST be exactly:
  `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1280" height="720" viewBox="0 0 1280 720" data-pptx-page-role="ROLE">`
  where ROLE is given in your slide brief (cover / content / ending).
- Write the file to the EXACT absolute path given in your brief. Nothing else.

## Color tokens (use these hex values verbatim)
- bg `#FFFFFF`; secondary_bg (card fill) `#F5F4F1`; primary/indigo `#2440D9`;
  accent/red `#D8402A` (negative finding only); green `#12805C` (positive finding);
  text `#14171F`; text_secondary `#6E7178`; border `#DBDBD6`.

## Type (font-family always `Arial, 'Helvetica Neue', sans-serif`)
- display_title 62, hero_number 120, title 44, subtitle 30, lead 28, body 24,
  annotation 18, kicker 16 (uppercase, letter-spacing ~2), footnote 15.
- Set `fill` explicitly on every text. Use `font-weight="700"` for titles/numbers.

## Layout grid
- Safe margins: keep all content within x ∈ [72, 1208], y ∈ [56, 664].
- Top of every non-cover slide: a kicker like `NN · SECTION NAME` in kicker size,
  text_secondary, uppercase; a short indigo rule (e.g. 44x4 rect) under it optional;
  then the slide title at title size in text color (or indigo for emphasis words).
- Prefer modular cards: rounded rects (`rx="14"`) filled secondary_bg with a 1px border
  (`stroke="#DBDBD6"`), holding a small heading + body lines. Align to a clean grid.
- Multi-line text: use multiple `<text>` elements OR `<tspan x=".." dy="..">`. Never rely
  on auto-wrap. Keep line length readable; do not overflow card edges.
- Vast whitespace is a feature. Do NOT crowd. 3–5 content blocks per slide max.

## FORBIDDEN (svg_quality_checker will reject these — never use)
- No `<style>`, no `class=`, no CSS selectors, no `@import`, no `<link>`, no external CSS.
- No `<mask>`, no `<foreignObject>`, no `<textPath>`, no `@font-face`.
- No `<script>`, no event attributes (onclick/onload/...), no SMIL (`<animate>`, `<set>`).
- Use inline presentation attributes only (fill, stroke, stroke-width, opacity, font-*, etc.).
- `data-pptx-page-role` goes ONLY on the root `<svg>`.
- For manual line breaks inside one text element use `<tspan>`, not `<foreignObject>`.

## Images (only if your brief lists them)
- Reference with `xlink:href="../images/<file>"` (paths are relative to this svg's folder).
- Preserve aspect ratio: use `preserveAspectRatio="xMidYMid meet"` and the width/height in your brief.
- Wrap each figure in its cue group (see below) so it becomes a highlight target.

## Visual cue anchors (CRITICAL — this is a hard contract)
Your brief lists 3–4 required cue anchors. For EACH one you MUST create a visible content
group shaped like:

```
<g id="cue_sXX_cY_slug">
  <title>short human label with keywords</title>
  <desc>keyword1 keyword2 keyword3 ... (include the listed cue keywords)</desc>
  <rect x=".." y=".." width=".." height=".." rx="14" fill="#F5F4F1" stroke="#DBDBD6" stroke-width="1"/>
  ...visible text/figure for this idea...
</g>
```
Rules for cue groups:
- The `id` MUST be exactly the anchor id from your brief (starts with `cue_`).
- The group MUST contain real, visible drawn content (a card rect + text, or a figure),
  sized so its bounding box is a meaningful region of the slide (not tiny, not the whole slide).
- The `<desc>` MUST include the cue keywords listed for that anchor so a text matcher can confirm it.
- The cue content is what the narrator is talking about at that moment — make it the actual
  card/figure/number for that idea, NOT a header, footer, page number, logo, or background.
- Do NOT put a cue id on the background, the kicker, or a decorative rule.
- Keep 2–4 cue groups per slide as listed; you may add non-cue decorative elements freely
  (kicker, title, rules) but those must NOT have `cue_` ids.

## Quality bar
- It must look like a real, polished conference-talk slide: aligned grid, consistent spacing,
  clear hierarchy, no overlapping text, no text spilling outside cards or the canvas.
- Numbers and claims must match the brief exactly (this is a faithful paper explainer).
- Output ONLY the SVG file at the given path. Reply with a one-line confirmation.
