#!/usr/bin/env python3
"""Comprehensive 3col restructure -> feasible 2-figure layout.
  col0 (no fig): problem, motivation, dataset-benchmark, headline-numbers, takeaway(grow)
  col1: method(grow) + Fig1
  col2: key-result(grow) + Fig4
Also: drop teaser figure, drop scan-to-read, trim Method to 3 steps.
"""
import re, sys
from pathlib import Path

p = Path(sys.argv[1]); s = p.read_text(encoding="utf-8")

def extract(html, sec):
    m = re.search(rf'<div class="section(?: grow)?" data-section="{re.escape(sec)}">', html)
    assert m, sec
    start = m.start(); j = start; depth = 0
    while j < len(html):
        o = html.find("<div", j); c = html.find("</div>", j)
        if o != -1 and o < c:
            depth += 1; j = o + 4
        else:
            depth -= 1; j = c + 6
            if depth == 0:
                return html[start:j], html[:start] + html[j:]
    raise RuntimeError(sec)

secs = {}
for name in ["problem","motivation","method","dataset-benchmark","key-result","headline-numbers","takeaway"]:
    secs[name], s = extract(s, name)

# strip grow everywhere; re-add per target
for k in secs:
    secs[k] = secs[k].replace('class="section grow"', 'class="section"')

# motivation: drop teaser figure
secs["motivation"] = re.sub(r'\s*<!-- OPTIONAL teaser figure.*?</figure>', '', secs["motivation"], flags=re.DOTALL)
secs["motivation"] = re.sub(r'\s*<figure><img src="assets/figures/figure2\.png".*?</figure>', '', secs["motivation"], flags=re.DOTALL)

# key-result: fold the evaluation benchmark list into the conclusion (dataset section dropped)
secs["key-result"] = secs["key-result"].replace(
    "UniMax wins at every model size on TyDi QA and WMT21, with the majority of WMT21 language pairs improving.",
    "Across TyDi QA, WMT21, XNLI, XQuAD, MLQA & PAWS-X, UniMax wins at every model size — and most WMT21 language pairs improve.")

# method: trim 4 steps -> 3 concise steps
new_steps = ('        <div class="p-steps">\n'
             '          <div class="step"><strong>Sort</strong> languages ascending by corpus size; '
             'set budget <strong>B = C</strong>.</div>\n'
             '          <div class="step"><strong>Split</strong> the remaining budget uniformly across '
             'the languages not yet allocated.</div>\n'
             '          <div class="step"><strong>Cap</strong> any language above <strong>N epochs</strong> '
             'at N·D<sub>l</sub>, redistribute the surplus. <strong>N=1</strong> ⇒ no repeats.</div>\n'
             '        </div>')
secs["method"] = re.sub(r'<div class="p-steps">.*?</div>\s*</div>', new_steps, secs["method"], count=1, flags=re.DOTALL)

def grow(b): return b.replace('class="section"', 'class="section grow"', 1)

# NOTE: dataset-benchmark deliberately dropped (its 29T/107/9.0B numbers lead the Headline hero).
col0 = "\n".join([secs["problem"], secs["motivation"], secs["headline-numbers"], grow(secs["takeaway"])])
col1 = grow(secs["method"])
col2 = grow(secs["key-result"])

new_cols = ('  <div class="columns">\n\n'
            '    <div class="col">\n' + col0 + '\n    </div>\n\n'
            '    <div class="col">\n' + col1 + '\n    </div>\n\n'
            '    <div class="col">\n' + col2 + '\n    </div>\n\n'
            '  </div>')

i = s.find('<div class="columns">')
j, depth = i, 0
while j < len(s):
    o = s.find("<div", j); c = s.find("</div>", j)
    if o != -1 and o < c:
        depth += 1; j = o + 4
    else:
        depth -= 1; j = c + 6
        if depth == 0: break
s = s[:i] + new_cols + s[j:]

# drop scan-to-read section div
si = s.find('<div class="section" data-section="scan-to-read">')
if si != -1:
    j, depth = si, 0
    while j < len(s):
        o = s.find("<div", j); c = s.find("</div>", j)
        if o != -1 and o < c: depth += 1; j = o + 4
        else:
            depth -= 1; j = c + 6
            if depth == 0: break
    s = s[:si] + s[j:]

# drop dataset-benchmark from the audio PLAYLIST (section removed)
s = s.replace('"method", "dataset-benchmark", "key-result"', '"method", "key-result"')

p.write_text(s, encoding="utf-8")
print("restructured; len", len(s))