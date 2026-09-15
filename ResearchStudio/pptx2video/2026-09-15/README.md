# pptx2video launch demo

Media for [ai-nuts/pptx2video](https://github.com/ai-nuts/pptx2video), hosted here so the tool repository and installation stay small.

- [60-second workflow GIF](workflow-demo.gif): 1280 × 720, 20 fps, looping.
- [Workflow MP4 with narration](workflow-demo.mp4): 1920 × 1080, 30 fps.
- [Poster frame](workflow-poster.png).
- Actual CLI renders: [original deck](original.mp4) · [edited deck](edited.mp4).
- [File sizes and SHA-256 checksums](manifest.json).

The workflow shows an editable PPTX passed to the pptx2video skill, followed by source edits and a second render. The editor and skill invocation are illustrated; video playback comes from actual CLI renders. The editable source is the PPTX, which can be changed and rendered again.

Both source renders passed strict QA with zero errors or warnings and word-aligned subtitles. Small editable PowerPoints, reports, and reproduction scripts live in the [source repository](https://github.com/ai-nuts/pptx2video/tree/main/examples/workflow-demo).

Keep this dated media directory stable; publish future demo revisions in a new directory.
