#!/usr/bin/env python3
"""Un-bake render artifacts that forced the Method column too wide, and bound the grid.
   - grid tracks -> minmax(0, ...) so a wide element can't expand a track past its share
   - p-eq font smaller so the long equation fits a fair-share column
   - restore both baked KaTeX equations to $$...$$ source (re-render at new size)
   - strip baked inline px widths from figures (let fit() re-scale to the new column)
"""
import re
import sys
from pathlib import Path

p = Path(sys.argv[1])
html = p.read_text(encoding="utf-8")

# 1. bound grid tracks
html = html.replace(
    "grid-template-columns: 1fr 1.25fr 1.25fr 1fr;",
    "grid-template-columns: minmax(0,1fr) minmax(0,1.25fr) minmax(0,1.25fr) minmax(0,1fr);",
)

# 2. shrink the equation font so it fits a fair-share column
html = html.replace("font-size: 1.08em; text-align: center; flex-shrink: 0;",
                    "font-size: 0.72em; text-align: center; flex-shrink: 0;")

# 3. restore baked katex spans to $$ source, pulled from the tex annotation
def unbake_katex(doc):
    out, i, n = [], 0, 0
    marker = '<span><span class="katex-display">'
    while True:
        s = doc.find(marker, i)
        if s == -1:
            out.append(doc[i:])
            break
        out.append(doc[i:s])
        # find the tex annotation for this equation
        a0 = doc.find('annotation encoding="application/x-tex">', s)
        a1 = doc.find('</annotation>', a0)
        tex = doc[a0 + len('annotation encoding="application/x-tex">'):a1]
        # find the end of the whole outer <span> ... need to balance <span>/</span>
        j, depth = s, 0
        while j < len(doc):
            o = doc.find('<span', j)
            c = doc.find('</span>', j)
            if c == -1:
                break
            if o != -1 and o < c:
                depth += 1
                j = o + 5
            else:
                depth -= 1
                j = c + len('</span>')
                if depth == 0:
                    break
        out.append(f"$${tex}$$")
        n += 1
        i = j
    return "".join(out), n

html, ncount = unbake_katex(html)

# 4. strip baked inline styles from the method/figure <figure> and its <img>
#    (remove style="...px..." so width:100% from CSS applies again)
html = re.sub(r'(<figure)\s+style="[^"]*"', r'\1', html)
html = re.sub(r'(<img\b[^>]*?)\s+style="[^"]*"', r'\1', html)

p.write_text(html, encoding="utf-8")
print(f"unbaked {ncount} equation(s); grid bounded; figure px widths stripped -> {p}")
