# IdeaSpark — usage guide

Four LLM environments are supported:

1. [Claude Code](#1-claude-code) — official harness, native skills support (lowest friction).
2. [Claude Desktop / claude.ai](#2-claude-desktop--claudeai) — skills library upload.
3. [OpenAI / GPT](#3-openai--gpt) — assistants-style with `SKILL.md` as system instructions + Python tools as functions.
4. [Gemini, open-weights, custom harnesses](#4-gemini-open-weights-custom-harnesses) — manual phase-by-phase invocation OR Python-library mode.

The skill is **model-agnostic**. The reasoning phases (1, 2.1, 2.2, 3.2, 3.3, 4.1, 4.1.5) read prompts from `references/system-prompts/` and produce JSON outputs — point them at any reasoning LLM. Phase 0 additionally runs a lightweight **fast-classify** LLM pass for per-paper pattern tagging + intent recognition (`CLASSIFY_FAST` profile; prompt embedded in `pattern_summary.py` / `intent.py`, not in `system-prompts/`; the host LLM does it in Claude Code). Everything else — the 0 / 3.1 retrieval connectors, 4.2 PDF render, and validators — is pure Python and runs the same regardless of which LLM you use.

---

## 1. Claude Code

Claude Code natively supports skills. **This is the lowest-friction option.**

### Install

This project ships as a subdirectory of the **ResearchStudio** repo — install from that repo's root, where the top-level `install.sh` links all three skills into `~/.claude/skills/` and installs their Python deps (see the root README). After it finishes, restart Claude Code; `idea-spark` appears under `/skills` (Phase 0 literature search is built in).

### Configure environment

```bash
# Phase 0 connector scripts read these from environment
export OPENALEX_MAILTO=<your-email>             # optional but recommended (polite-pool: 10 req/s vs 1 anonymous)
export OPENALEX_API_KEY=<your-openalex-key>     # optional, premium tier (https://openalex.org/about)
export OPENREVIEW_USER=<your-openreview-email>  # required for OpenReview connector
export OPENREVIEW_PASS=<your-openreview-pass>
```

For dev workflow, copy the project's `.env.template` to `.env` and source it. `.env.template` is committed (so others see the env-var schema) but `.env` is gitignored:

```bash
cp .env.template .env
$EDITOR .env                  # fill in real values
set -a; source .env; set +a   # load into current shell
```

Never commit `.env`, embed keys in `SKILL.md` / any tracked file, or share keys in issues / public chats. `.env.template` is the canonical list of env vars the skill reads — keep it in sync with the code.

Python deps — cross-platform notes:

- **PEP 668** (recent macOS/Homebrew & Ubuntu 23.04+) rejects a bare `pip install` with `externally-managed-environment`. Use a venv (`python3 -m venv .venv && source .venv/bin/activate`) or `python3 -m pip install --user --break-system-packages feedparser openreview-py beautifulsoup4 pymupdf` (drop the flag on older pip that rejects it).
- **Use the SAME interpreter for install and run.** Installing for a `pip`/`pip3` that maps to a *different* `python3` (a common macOS gotcha) makes `arxiv`/`openreview` silently skip at runtime even though `check_connectors` looked green — the run now prints a **CONNECTORS DEGRADED** banner + writes a `.connectors_degraded` marker. Verify with `python3 -m scripts.run check_connectors` from the shell you launch phases in.
- **`CLAUDE_PROJECT_DIR`** must be set when invoking orchestrator phases manually (Claude Code injects it, but a plain/background/cron shell often leaves it empty, which collapses `${CLAUDE_PROJECT_DIR}/phase0` to `/phase0`). `export CLAUDE_PROJECT_DIR="$PWD" && mkdir -p "$CLAUDE_PROJECT_DIR"`. The orchestrator now hard-fails early with an actionable message on an empty/unexpanded value.
- **PDF (optional):** the render auto-compiles a PDF when `xelatex` *or* `tectonic` is on PATH (cross-platform TeX paths + an available CJK font are auto-detected); otherwise the `.md`/`.tex` are still written and only the PDF is skipped, with an install hint. macOS: `brew install --cask mactex-no-gui` or `brew install tectonic`. Ubuntu: `sudo apt-get install texlive-xetex` or `cargo install tectonic`.

### Use

Ask in natural language, or use the `/idea-spark` slash command:

```
> /idea-spark I want a novel ML research idea about physical realism in text-to-video models.
```

Claude Code triggers `idea-spark`. The skill drives the 5-phase workflow:

1. Phase 0 — orchestrator probes 4 connectors (arxiv / openalex / semanticscholar / openreview) with role-based time windows; ~30-40 papers retrieved + tagged into `lit_table.md`. If a connector is missing its package/cred it is skipped and a **CONNECTORS DEGRADED** banner is printed (partial coverage is never mistaken for a full run).
2. Phase 1 — single LLM call writes a literature-grounded bottleneck statement citing ≥ 2 retrieved papers; routes to `proceed` or `do_not_generate`.
3. Phase 2.1 + 2.2 — two LLM calls: select 1-3 of 15 ideation patterns by structural fit (then one sub-pattern each); generate one candidate with full schema + `signature_terms[]`.
4. Phase 3.1 — orchestrator runs collision retrieval with `signature_terms[]` over a 6-month window (no LLM call).
5. Phase 3.2 — single LLM call performs 4 corpus-anchored audit checks (gap-closure reject lessons / recipe-application / anti-pattern mitigation / paper-pointed threat) with a two-layer verdict.
6. Phase 3.3 (only when verdict=revise) — single LLM call applies revision targets to the candidate; kill-switch fields preserved byte-identical.
7. Phase 4.1 — single LLM call expands the candidate into idea-card content (motivation, method flow, feasibility validation, etc.).
8. Phase 4.2 — orchestrator templates into Markdown + LaTeX (no LLM call), and auto-compiles a PDF when a LaTeX engine (`xelatex`/`tectonic`) is on PATH.
9. Validators — `kill_switch_integrity` + `subpattern_citation_consistency` + `expansion_completeness` (+ `implementability_*` when the Phase 4.1.5 audit ran) run as final mechanical checks.

Three outcomes per run: the rendered idea cards `idea.std.{en,zh}.{md,tex}` + `idea.detail.en.md` (+ `.pdf` when an engine is available) (success) / `do_not_generate.md` (Phase 1 OOD) / `phase_3_failed.md` (audit abandons). The skill never asks mid-flow.

LLM call budget: **6** (advance) or **7** (revise), counting the default-on Phase 4.1.5 implementability audit (**5** / **6** if it is skipped). End-to-end ~15-30 minutes with a frontier reasoning model (extended thinking on).

### Tweaks

- Read the candidate before Phase 4: outputs land in `outputs/<run>/phase{0,1,2,3,4}_*/`. The Phase 2.2 candidate JSON is at `outputs/<run>/phase2_generate/phase2_generate_output.json`.
- Re-run with corrections: if Phase 3.2 verdict was `revise` and you want to tweak revision_targets, edit `outputs/<run>/phase3_critique/phase3_critique_output.json`'s `revision_targets[]` and re-invoke Phase 3.3.

---

## 2. Claude Desktop / claude.ai

Skills can be uploaded as a folder via Settings → Skills.

### Install

```bash
# From the repo root:
(cd skills && zip -r idea_spark.zip idea_spark)
```

Upload the ZIP in Settings → Skills.

### Configure

API keys cannot be set as env vars in claude.ai. Two options:

1. **Private fork with embedded keys** — replace `os.environ.get('OPENALEX_API_KEY', '')` etc. in `skills/idea_spark/scripts/search_*.py` with literal strings (only do this on a private fork, never commit). Re-zip and re-upload.
2. **Run the orchestrator phases (0, 3.1) locally** — use claude.ai for LLM-driven phases (1, 2.1, 2.2, 3.2, 3.3, 4.1) by pasting prompts manually, run orchestrator scripts on your machine where env vars are set. This is more work but keeps secrets out of the upload.

For a typical dev workflow, Claude Code (option 1 above) is simpler than Claude Desktop.

### Use

Same natural-language prompt as Claude Code. The skill writes outputs into the conversation; PDF + Markdown are returned as attachments.

---

## 3. OpenAI / GPT

OpenAI Assistants don't have native skills support, but the skill works as a system-instructions + tools setup.

### Install

1. Create a new Assistant.
2. Upload `skills/idea_spark/SKILL.md` and all of `references/` as files (Phase 0 search rubrics `intent-recognition.md` / `pattern-summary-rubric.md` are included there).
3. In the Assistant's instructions:

```
Follow the 5-phase workflow in SKILL.md. Read references/system-prompts/ files
on-demand based on phase: bottleneck_identify.txt for Phase 1, ideate_select.txt
for Phase 2.1, ideate_generate.txt for Phase 2.2, critique.txt for Phase 3.2,
revise.txt for Phase 3.3 (only when verdict=revise), expand.txt for Phase 4.1.

For Phase 0 (literature retrieval) and Phase 3.1 (collision retrieval), call
the registered Python orchestrator functions (run_phase0, run_phase3_collision)
which subprocess into idea_spark/scripts/. For Phase 4.2 (PDF render),
call run_phase4_render.

After each phase, write the JSON output to outputs/<run>/<phase>/ and read
downstream from there.
```

5. Register the orchestrator scripts as functions (see OpenAI's [function-calling docs](https://platform.openai.com/docs/assistants/tools/function-calling)). Each `scripts/run.py` subcommand becomes one function:
   - `run_phase0(query: str, out_dir: str) -> dict`
   - `run_phase3_collision(idea_json: str, out_dir: str) -> dict`
   - `run_phase4_render(expansion_json: str, out_dir: str) -> dict`
   - `run_validate(phase2: str, phase3: str, phase4: str) -> dict`

### Configure environment

The Phase 0 connectors run server-side (wherever your function-calling backend executes Python):

```bash
export OPENALEX_API_KEY=...
export OPENREVIEW_USER=...
export OPENREVIEW_PASS=...
```

### Use

```
User: I want a novel ML research idea about physical realism in text-to-video models.
```

The assistant follows the 5-phase workflow, calling the registered functions for orchestrator-driven phases and producing JSON between each phase. PDF + Markdown are returned via the function-calling response.

### GPT-specific notes

- **Context window**: Phase 2.2 reads 1-3 full ideation pattern cards (~5-10k tokens each) + 3-4 sub-pattern cards (~3-5k each). Total prompt context can hit 30-50k tokens. Use a model with ≥ 128k context (gpt-4-turbo, gpt-4o, or larger).
- **JSON output**: every phase's output is JSON-validated. Use the model's JSON-mode (`response_format={"type": "json_object"}`).
- **Sub-pattern reads are composition-scoped**: Phase 3.2 reads exactly 1 sub-pattern card (the candidate's `sub_pattern_id`) + 1 pattern card per secondary in the composition. Don't preload the full `references/ideation-sub-patterns/` directory (31 cards); the prompt names which file to load.

---

## 4. Gemini, open-weights, custom harnesses

For any LLM you can call from Python, you have two options:

### Option A: Manual phase-by-phase (simplest for one-off use)

For each LLM-driven phase, copy the prompt from `references/system-prompts/<phase>.txt` into your LLM call along with the listed inputs, save the JSON output to the conventional location, then run orchestrator phases between LLM phases:

```bash
# Phase 0 (orchestrator)
python -m scripts.run phase0 --query "..." --out outputs/myrun/phase0/

# Phase 1 (manual: paste bottleneck_identify.txt + Phase 0 output into your LLM, save result)
# > save to outputs/myrun/phase1/phase1_output.json

# Phase 2.1 (manual: paste ideate_select.txt + Phase 1 output, save result)
# > save to outputs/myrun/phase2_select/phase2_select_output.json

# Phase 2.2 (manual: paste ideate_generate.txt + Phase 2.1 output + 1-3 pattern cards + 3-4 sub-pattern cards, save)
# > save to outputs/myrun/phase2_generate/phase2_generate_output.json

# Phase 3.1 (orchestrator)
python -m scripts.run phase3_collision \
  --idea-json outputs/myrun/phase2_generate/phase2_generate_output.json \
  --out outputs/myrun/phase3_collision/

# Phase 3.2 (manual: paste critique.txt + candidate + composition cards + collision_hits.json, save)
# > save to outputs/myrun/phase3_critique/phase3_critique_output.json

# Phase 3.3 (manual, only if verdict=revise; paste revise.txt + candidate + revision_targets, save)
# > save to outputs/myrun/phase3_revise/phase3_revise_output.json

# Phase 4.1 (manual: paste expand.txt + final candidate + Phase 1/3 outputs, save)
# > save to outputs/myrun/phase4/phase4_expansion.json

# Phase 4.2 + validators (orchestrator)
python -m scripts.run phase4_render --expansion outputs/myrun/phase4/phase4_expansion.json --out outputs/myrun/phase4/
python -m scripts.run validate \
  --phase2 outputs/myrun/phase2_generate/phase2_generate_output.json \
  --phase3 outputs/myrun/phase3_revise/phase3_revise_output.json \
  --phase4 outputs/myrun/phase4/phase4_expansion.json
```

### Option B: Backend-CLI integration (for repeated use)

Set environment variables that the orchestrator will use to dispatch each capability profile to your backend:

```bash
# Reasoning (large) — used in Phase 1, 2.1, 2.2, 3.2, 3.3, 4.1
export NOVELTY_LLM_REASONING_LARGE_CMD='python my_wrappers/gemini.py --model gemini-2.5-pro'

# Classify (fast) — used optionally by Phase 0 for pattern tagging
export NOVELTY_LLM_CLASSIFY_FAST_CMD='python my_wrappers/gemini.py --model gemini-2.5-flash'
```

Each command must:

- Accept the prompt on stdin (`<<SYSTEM>>\n<system>\n<<USER>>\n<user>`).
- Return JSON on stdout (parseable by `json.loads`).
- Exit 0 on success; non-zero with stderr explanation on failure.

A minimal Gemini wrapper:

```python
# my_wrappers/gemini.py
import json, os, sys
import google.generativeai as genai

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model_name = sys.argv[2] if sys.argv[1] == '--model' else 'gemini-2.5-flash'
text = sys.stdin.read()
system, user = text.split('<<USER>>', 1)
system = system.replace('<<SYSTEM>>', '').strip()
model = genai.GenerativeModel(model_name, system_instruction=system)
resp = model.generate_content(user, generation_config={'response_mime_type': 'application/json'})
print(resp.text)
```

For the LLM-driven phases (1, 2.1, 2.2, 3.2, 3.3, 4.1), full automation requires a thin orchestrator wrapper that loads the prompt, gathers inputs, calls the configured LLM, and saves output. The current `scripts/run.py` orchestrator only handles Phase 0 / 3.1 / 4.2 / validate; the LLM phases are designed for host-LLM execution where the host (Claude Code, Claude Desktop) reads the prompt + inputs and produces output natively.

For full automation with Gemini / open-weights, you'd write a Python loop:

```python
for phase in ['phase1', 'phase2_select', 'phase2_generate', 'phase3_critique', 'phase3_revise', 'phase4']:
    prompt_path = f'references/system-prompts/{phase_to_prompt[phase]}.txt'
    inputs = gather_inputs(phase)
    output = call_llm(prompt_path, inputs)
    save_to(f'outputs/{run}/{phase}/{phase}_output.json', output)
```

### Caveats

- **Context**: Phase 2.2 + 3.2 + 4.1 each need ≥ 100k context; 200k recommended for Phase 2.2 (full pattern + sub-pattern cards).
- **JSON adherence**: not all open-weights models reliably return JSON. Wrap with a parser-and-retry loop. Use `response_format` mode where available (Gemini 2.5+, Claude, GPT-4 turbo+).
- **Connectors standalone**: the Phase 0 / 3.1 retrieval scripts (`scripts/search_*.py`) run identically regardless of LLM backend — they are pure Python.

---

## Common questions

### Does the skill work offline?

Phase 0 and Phase 3.1 require network access (arxiv / openalex / semanticscholar / openreview). The other phases are LLM-driven and only require access to your chosen LLM backend. If you point all profiles at a local LLM (e.g., Llama 3 via vllm), the only network calls are to the Phase 0 / 3.1 literature APIs.

If no connector is available and `--allow-webfallback` is not passed, the orchestrator halts with `error: no_connector_available` rather than degrading to WebSearch — preventing silent quality loss.

### How long does a full run take?

In Claude Code with a frontier reasoning model (extended thinking on): **typically ~30 minutes** end-to-end (~20-40 min depending on model, thinking budget, and whether a revise pass runs). Retrieval and templating are fast; wall-clock is dominated by the ~6-7 reasoning LLM calls. Breakdown:

- Phase 0 retrieval: ~30-60s (4 parallel connector calls)
- Phase 1: ~1-2 min (1 LLM call)
- Phase 2.1 + 2.2: ~5-8 min (2 LLM calls; Phase 2.2 reads full pattern + sub-pattern cards — the longest generation)
- Phase 3.1 retrieval: ~30s
- Phase 3.2 audit: ~4-6 min (heaviest reasoning call; reads 1 sub-pattern card + N-1 pattern cards per the composition)
- Phase 3.3 (only if verdict=revise): ~2-3 min
- Phase 4.1 (+ 4.1.5 implementability audit): ~5-8 min (structured idea-card content + implementability pass)
- Phase 4.2 + validators: ~5s (orchestrator)

### Can I just use the Phase 0 literature search alone?

Yes. The orchestrator subcommands work independently:

```bash
python -m scripts.run phase0 --query "diffusion sampling acceleration" --out /tmp/lit/
cat /tmp/lit/lit_table.md  # ~30-40 papers tagged with ideation pattern + bottleneck + open issue
```

### What if I want to bypass the audit?

You shouldn't. The audit is the load-bearing quality gate; bypassing it returns to vanilla LLM critique without corpus grounding. If a specific audit verdict (e.g., `revise`) seems unjustified, edit `revision_targets[]` to empty + re-run Phase 4.1 directly with the Phase 2.2 candidate as input — but understand you're skipping the corpus checks the skill is built around.

### Does the skill prefer specific ideation patterns?

No — Phase 2.1 selects compositions by **structural fit** (does the bottleneck's shape match this pattern's operational signature?), not by historical Oral rate or pattern saturation in the area. The only place historical acceptance enters is the **anti-pattern guard**: 3 reject-favored 2-way compositions (audit + auxiliary signal at 30% Oral; audit + invariance at 39%; audit + surgical fix at 44%) trigger a required-mitigation check at Phase 2.2 + 3.2.

The Phase 4 idea card includes an **ideation pattern landscape** section showing the area's current pattern distribution — for transparency, not as a generation signal.

---

## File / output structure summary

```
<repo-root>/
├── README.md                           ← project README
├── docs/USAGE.md                       ← this file
├── skills/
│   └── idea_spark/                  ← the skill (5-phase workflow; Phase 0 search built in)
│       ├── SKILL.md
│       ├── README.md
│       ├── references/
│       │   ├── ideation-patterns/    ← 15 pattern cards
│       │   ├── ideation-sub-patterns/ ← 31 sub-pattern cards
│       │   ├── system-prompts/         ← LLM-call prompts
│       │   ├── intent-recognition.md   ← Phase 0 / 3.1 query + signature rubric
│       │   ├── pattern-summary-rubric.md ← Phase 0 per-paper tagging rubric
│       │   └── ...
│       └── scripts/
│           ├── run.py                  ← orchestrator (phase0, phase3_collision, phase4_render, validate)
│           ├── search_arxiv.py         ← Phase 0 / 3.1 connectors
│           ├── search_openalex.py
│           ├── search_semanticscholar.py
│           ├── search_openreview.py
│           ├── dedup_merge.py
│           ├── pattern_summary.py
│           ├── intent.py
│           ├── _time_guard.py
│           ├── render_pdf.py           ← Phase 4.2 templating + PDF/MD/TeX render
│           └── validators/             ← kill_switch_integrity + expansion_completeness + …
└── outputs/<run>/                      ← skill outputs
    ├── phase0/
    │   ├── lit_results.json
    │   └── lit_table.md
    ├── phase1/phase1_output.json
    ├── phase2_select/phase2_select_output.json
    ├── phase2_generate/phase2_generate_output.json
    ├── phase3_collision/collision_hits.json
    ├── phase3_critique/phase3_critique_output.json
    ├── phase3_revise/phase3_revise_output.json    (only when verdict=revise)
    └── phase4/
        ├── phase4_expansion.json
        ├── phase4_implementability.json          (when Phase 4.1.5 ran)
        ├── idea.detail.en.md                         (detailed-register card)
        ├── idea.std.en.md / idea.std.zh.md        (plain-register cards)
        ├── idea.std.en.tex / idea.std.zh.tex      (LaTeX side artifacts)
        └── idea.std.en.pdf / idea.std.zh.pdf      (only when xelatex/tectonic on PATH)
```
