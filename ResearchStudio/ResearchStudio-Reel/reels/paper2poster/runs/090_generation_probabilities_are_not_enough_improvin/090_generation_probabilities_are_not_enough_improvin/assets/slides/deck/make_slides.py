#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 090
("Generation Probabilities are Not Enough: Improving Error Highlighting for AI
Code Suggestions", NeurIPS 2022 HCAI, Stanford + Microsoft Research).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue
pass resolves every anchor from PPTX geometry. Zero <image>, zero gradients, ASCII
mono only.
Theme motif: a code editor with highlighted tokens - generation-probability
highlights (GOLD, the challenged baseline) vs edit-model highlights (GREEN, wins),
RED bug tokens, and a spell-checker wavy underline. Bars for time / survival /
preference. Color semantics: ACCENT=shared Codex model, GOLD=generation
probability, GREEN=edit model / wins, RED=bug/worst, TEAL=study/participants."""
import json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
META = os.environ["VIDEO_META"]
OUT  = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)
AM = json.load(open(os.path.join(META, "_anchor_map.json")))

W, H = 1280, 720
BG="#0B1B2B"; PANEL="#12293D"; PANEL2="#16324A"; STROKE="#26455F"
ACCENT="#4C9BE8"; TEAL="#34D3C0"; GOLD="#F2C14E"; RED="#F2685C"; GREEN="#48C78E"
TEXT="#EAF2FB"; SEC="#9DB3C8"; TER="#6E869C"; WHITE="#FFFFFF"
SANS="Arial, 'Helvetica Neue', Helvetica, sans-serif"
MONO="'DejaVu Sans Mono', Consolas, monospace"

def esc(s):
    return (str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
            .replace('"',"&quot;"))

def T(x,y,s,size,fill=TEXT,weight="400",anchor="start",ff=SANS,ls=None,opacity=None):
    a=f' letter-spacing="{ls}"' if ls is not None else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    return (f'<text x="{x}" y="{y}" font-family="{ff}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}"{a}{o}>{esc(s)}</text>')

def rect(x,y,w,h,fill=PANEL,stroke=None,rx=14,sw=1.5,opacity=None):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st}{o}/>'

def line(x1,y1,x2,y2,stroke=STROKE,sw=1.5,dash=None,cap="round"):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>'

def circle(cx,cy,r,fill=ACCENT,stroke=None,sw=1.5,opacity=None):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{st}{o}/>'

def poly(pts,fill="none",stroke=ACCENT,sw=2.5,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    p=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    return f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{d}/>'

def polygon(pts,fill=PANEL2,stroke=None,sw=1.0):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    p=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    return f'<polygon points="{p}" fill="{fill}"{st}/>'

def arrow(x1,y1,x2,y2,stroke=SEC,sw=2.2):
    ang=math.atan2(y2-y1,x2-x1); a=10
    xa=x2-a*math.cos(ang-0.45); ya=y2-a*math.sin(ang-0.45)
    xb=x2-a*math.cos(ang+0.45); yb=y2-a*math.sin(ang+0.45)
    return (line(x1,y1,x2,y2,stroke,sw)+
            f'<polyline points="{xa:.1f},{ya:.1f} {x2},{y2} {xb:.1f},{yb:.1f}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')

def wrap(text,maxc):
    words=text.split(); lines=[]; cur=""
    for w in words:
        if len(cur)+len(w)+1<=maxc: cur=(cur+" "+w).strip()
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines

def para(x,y,text,size,fill,maxc,lh,weight="400"):
    ls=wrap(text,maxc); out=[T(x,y+i*lh,l,size,fill,weight) for i,l in enumerate(ls)]
    return "".join(out), y+len(ls)*lh

def anchor(aid,kw,body):
    return f'<g id="{aid}"><title>{esc(" ".join(kw))}</title>{body}</g>'

def eyebrow(label):
    return (rect(64,52,5,26,fill=ACCENT,rx=2,sw=0)+
            T(82,72,label.upper(),15,SEC,"700",ls="2.5"))

def header(label,title,tsize=30):
    return eyebrow(label)+T(64,110,title,tsize,TEXT,"800")

def chunks(slide_id):
    return AM[slide_id]["chunks"]

def svg(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'width="{W}" height="{H}" font-family="{SANS}">'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>'
            f'{body}</svg>')

def bar(x,y,w,val,vmax,color,label,valtxt,lblcolor=SEC,h=26):
    bw=max(2,int(w*val/vmax))
    return (rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=6,sw=1)+
            rect(x,y,bw,h,fill=color,rx=6,sw=0)+
            T(x-12,y+h*0.70+2,label,14,lblcolor,"600",anchor="end")+
            T(x+bw+10,y+h*0.70+2,valtxt,14,color,"800"))

def stat(x,y,w,h,num,lbl,col):
    ns=min(32,h*0.34)
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.52,num,ns,col,"800",anchor="middle")+
            T(x+w/2,y+h*0.80,lbl,12.5,SEC,"600",anchor="middle"))

def chip(x,y,text,col,w=512,h=34):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+6,text,14.5,TEXT,"600"))

def eqbox(x,y,w,expr,size=17,h=44):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            T(x+w/2,y+h/2+6,expr,size,TEXT,"800",anchor="middle",ff=MONO))

# ---- theme glyphs -------------------------------------------------------
HLCOL={'gp':GOLD,'edit':GREEN,'bug':RED}

def code_pane(x,y,w,h,rows,unit=7):
    """Stylized code editor: line-number gutter + token bars per row.
    rows: list of rows; each row is a list of (units, hl) where hl in
    {None,'gp','edit','bug'} sets a highlight color behind/over the token bar."""
    out=rect(x,y,w,h,fill="#0C1E2E",stroke=STROKE,rx=8)
    gut=26
    out+=line(x+gut,y+7,x+gut,y+h-7,STROKE,1)
    n=max(1,len(rows)); lnh=(h-16)/n
    for i,row in enumerate(rows):
        yy=y+12+lnh*i+lnh/2-4
        out+=T(x+gut/2,yy+4,str(i+1),9,TER,"700",anchor="middle",ff=MONO)
        cx=x+gut+9
        for units,hl in row:
            tw=units*unit
            if cx+tw>x+w-8: break
            if hl:
                col=HLCOL[hl]
                out+=rect(cx-2,yy-4,tw+4,12,fill=col,rx=3,sw=0,opacity=0.30)
                out+=rect(cx,yy-1,tw,6,fill=col,rx=2,sw=0)
            else:
                out+=rect(cx,yy-1,tw,6,fill="#3E5A74",rx=2,sw=0)
            cx+=tw+6
    return out

def wavy(x,y,w,color=GOLD,sw=1.7,step=4,amp=2):
    pts=[]; n=int(w/step)
    for i in range(n+1):
        pts.append((x+i*step, y+(amp if i%2 else 0)))
    return poly(pts,stroke=color,sw=sw)

def shared_codex(x,y,w,h):
    """One Codex model feeding three display conditions (none / gen-prob / edit).
    Content is sized to fit exactly inside the (x,y,w,h) box - no overflow."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=10)
    cbw=118; cbh=58; cbx=x+18; cby=y+h/2-cbh/2
    out+=rect(cbx,cby,cbw,cbh,fill=PANEL2,stroke=ACCENT,rx=8,sw=1.8)
    out+=T(cbx+cbw/2,cby+cbh/2-1,"Codex",16,ACCENT,"800",anchor="middle")
    out+=T(cbx+cbw/2,cby+cbh/2+16,"one shared model",10,SEC,"600",anchor="middle")
    px=cbx+cbw+52
    conds=[("No highlight",None,SEC),
           ("Generation-probability",'gp',GOLD),
           ("Edit model",'edit',GREEN)]
    n=len(conds); gap=8; pad=7
    ph=(h-2*pad-(n-1)*gap)/n
    labelw=210; panew=(x+w)-px-labelw-14
    for i,(lb,hl,col) in enumerate(conds):
        py=y+pad+i*(ph+gap)
        out+=arrow(cbx+cbw+2,cby+cbh/2,px-6,py+ph/2,SEC,1.6)
        out+=code_pane(px,py,panew,ph,[[(3,None),(4,hl),(2,None),(3,None)]],unit=6)
        out+=circle(px+panew+14,py+ph/2,5,fill=col)
        out+=T(px+panew+26,py+ph/2+5,lb,12,col,"800")
    return out

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"NeurIPS 2022 · HCAI Workshop",14,ACCENT,"800",ls="1.5")
    b+=T(1216,72,"Stanford University · Microsoft Research",13.5,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"Generation Probabilities are Not Enough",40,WHITE,"800")
    b+=T(64,192,"Improving Error Highlighting for AI Code Suggestions",22,ACCENT,"800")
    # code-highlight motif near the title: edit-model highlight beats gen-prob
    b+=code_pane(966,104,250,92,[
        [(3,None),(4,'edit'),(2,None)],
        [(2,None),(3,'gp'),(4,None),(2,None)],
        [(4,None),(2,None),(3,'edit')],
    ])
    b+=T(966,208,"which tokens to highlight?",11.5,TER,"700")
    b+=T(64,228,"Helena Vasconcelos · Gagan Bansal · Adam Fourney · Q. Vera Liao · Jennifer Wortman Vaughan",14.5,SEC,"500")
    cw=276; gap=16; x0=64; cy=290; chh=246
    data=[
        (ch[0],ACCENT,x0,"Assistants make mistakes",
         "Tools like Copilot suggest code completions, but they err, and programmers have to catch those mistakes before they become bugs."),
        (ch[1],GOLD,x0+cw+gap,"Highlight low-confidence tokens?",
         "The popular idea is to highlight the tokens the model was least confident about. But are generation probabilities the right thing to highlight?"),
        (ch[2],TEAL,x0+2*(cw+gap),"30 programmers, preregistered",
         "A preregistered study compares highlighting low-probability tokens against a new edit model that predicts which tokens a person will change."),
        (ch[3],GREEN,x0+3*(cw+gap),"The edit model wins",
         "The edit model is faster, edits are more precise, and users prefer it - showing generation probabilities alone are not enough."),
    ]
    for c,col,x,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              para(x+24,cy+50,ti,17,TEXT,25,23,"800")[0])
        body+=para(x+24,cy+128,tx,12.8,SEC,35,18)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,566,1216,566,STROKE,1)
    b+=T(64,600,"arXiv:2302.07248",14,ACCENT,"700")
    b+=T(260,600,"osf.io/tymah",13.5,SEC,"600")
    b+=T(1216,600,"What you highlight matters more than whether you highlight.",14,SEC,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Catching AI's mistakes, one token at a time")
    # c1 left tall: imperfect assistants plant bugs
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=RED,rx=6,sw=0)+
        T(92,202,"A wrong suggestion plants a bug",17.5,RED,"800")+
        para(92,238,"AI code assistants are now everywhere, but they are imperfect. A wrong suggestion can quietly plant a bug or a security hole.",14.5,SEC,42,23)[0]+
        code_pane(92,346,348,120,[
            [(3,None),(4,None),(2,None)],
            [(2,None),(5,'bug'),(3,None),(2,None)],
            [(4,None),(2,None),(3,None)],
            [(3,None),(3,None),(4,None),(2,None)],
        ])+
        T(92,494,"one bad token, quietly wrong",12.8,RED,"700",ff=MONO))
    fx=500; fw=716
    # c2 must notice them - over-trust
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,120,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,120,fill=GOLD,rx=6,sw=0)+
        T(fx+28,196,"First you have to notice",16.5,GOLD,"800")+
        para(fx+28,226,"To catch mistakes, a programmer must first notice them - and that is hard, because people tend to over-trust automation.",14,SEC,74,21)[0])
    # c3 hundreds of tiny decisions - one per token
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,294,fw,164,fill=PANEL,stroke=STROKE)+
        rect(fx,294,6,164,fill=ACCENT,rx=6,sw=0)+
        T(fx+28,332,"Not one decision, but hundreds",16.5,ACCENT,"800")+
        para(fx+28,362,"A single code suggestion is not one decision but hundreds of tiny ones - one per token.",14,SEC,72,21)[0]+
        code_pane(fx+28,402,fw-56,44,[
            [(2,None),(3,None),(2,None),(3,None),(2,None),(4,None),(2,None),(3,None),(2,None),(3,None),(2,None)],
        ]))
    # c4 prior uncertainty research: single-shot
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,474,fw,76,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(fx,474,6,76,fill=GOLD,rx=6,sw=0)+
        T(fx+28,506,"Old uncertainty research does not carry over",15.5,GOLD,"800")+
        para(fx+28,532,"Built for single-shot decisions like a diagnosis, not this token-by-token world.",14,SEC,95,20)[0])
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Highlight uncertain tokens - but which signal?")
    # c1 left top: spell-checker analogy
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,192,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,192,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Highlight like a spell-checker",16.5,ACCENT,"800")+
        para(92,226,"One natural idea: highlight uncertain tokens, much as a spell-checker underlines suspect words, drawing the eye to spots that most need review.",14,SEC,58,21)[0]+
        code_pane(92,300,300,34,[[(3,None),(5,'gp'),(2,None),(3,None)]],unit=8)+
        wavy(126,338,116,GOLD))
    # c2 left bottom: generation probability signal
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,366,560,184,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,366,6,184,fill=GOLD,rx=6,sw=0)+
        T(92,404,"The obvious signal: generation probability",15.5,GOLD,"800")+
        para(92,434,"Use the model's own generation probability - highlight the tokens the model was least sure about.",14,TEXT,56,21)[0]+
        eqbox(92,500,504,"low generation probability  ->  highlight token",13,h=34))
    # c3 right top: ships in OpenAI Playground
    rx=648; rw=568
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,158,rw,150,fill=PANEL,stroke=STROKE)+
        rect(rx,158,6,150,fill=TEAL,rx=6,sw=0)+
        T(rx+28,196,"Already a shipping strategy",16.5,TEAL,"800")+
        para(rx+28,226,"This is an existing strategy - it even ships in OpenAI's Playground, colouring tokens by confidence.",14,SEC,58,21)[0]+
        chip(rx+28,282,"OpenAI Playground  ·  colour tokens by confidence",TEAL,w=rw-56,h=30))
    # c4 right bottom: the untested gap
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,324,rw,226,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(rx,324,6,226,fill=GREEN,rx=6,sw=0)+
        T(rx+28,362,"But is low probability the right target?",16,GREEN,"800")+
        para(rx+28,392,"Nobody had tested whether low probability actually lines up with where humans need to make edits. That gap is exactly what this paper probes.",14,TEXT,56,21)[0]+
        eqbox(rx+28,482,rw-56,"low probability  =?=  where humans edit",13.5,h=42))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION (3 chunks) ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","From model uncertainty to human intervention")
    cw=372; gap=18; x0=64; cy=176; chh=374
    cards=[
        (ch[0],TEAL,"S","A preregistered 3-way study",
         "A preregistered, mixed-methods study with 30 programmers compares three displays of the same AI completions.",
         ["No highlights", "Generation-probability", "Edit model"]),
        (ch[1],GREEN,"E","The edit model: the key idea",
         "Instead of asking how confident the model was, the edit model predicts which tokens a human is actually likely to change.",
         None),
        (ch[2],ACCENT,"R","Reframing the whole problem",
         "This shifts the goal from surfacing model uncertainty to surfacing human intervention - a recipe that could scale from edit telemetry products already collect.",
         None),
    ]
    for i,(c,col,tag,ti,tx,chips) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+52,cy+70,28,fill="none",stroke=col,sw=2.5)+
              T(x+52,cy+79,tag,26,col,"800",anchor="middle"))
        yy=cy+140
        for j,ln in enumerate(wrap(ti,26)):
            body+=T(x+28,yy+j*26,ln,18,TEXT,"800");
        yy+=26*len(wrap(ti,26))+14
        body+=para(x+28,yy,tx,14,SEC,40,22)[0]
        if chips:
            colmap=[SEC,GOLD,GREEN]
            for k,cc in enumerate(chips):
                body+=chip(x+28,cy+270+k*36,cc,colmap[k],w=cw-56,h=30)
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,596,"Same completions, three displays - and a new signal: predicted human edits, not model confidence.",15.5,GREEN,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Same model, only the highlighted tokens differ")
    # c1 wide top: one Codex feeding three conditions
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,190,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,190,fill=ACCENT,rx=6,sw=0)+
        T(92,194,"One Codex model, three displays",16.5,ACCENT,"800")+
        para(92,222,"All three tools use the very same Codex model, so any difference in behavior comes purely from how the completion is displayed.",13.5,SEC,110,19)[0]+
        shared_codex(92,250,1096,96))
    # c2 left bottom: gen-prob tool 71%
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,366,378,184,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,366,6,184,fill=GOLD,rx=6,sw=0)+
        T(92,402,"Generation-probability tool",15.5,GOLD,"800")+
        para(92,430,"Highlights the tokens the model was least confident in.",13.5,TEXT,44,19)[0]+
        stat(92,470,140,64,"71%","confidence thr.",GOLD)+
        code_pane(248,470,180,64,[[(2,None),(4,'gp'),(2,None)],[(3,None),(2,'gp'),(3,None)]],unit=7))
    # c3 mid bottom: edit-model tool 66%
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(458,366,378,184,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(458,366,6,184,fill=GREEN,rx=6,sw=0)+
        T(486,402,"Edit-model tool",15.5,GREEN,"800")+
        para(486,430,"Highlights tokens most likely to be edited; trained on 9 coders.",13.5,TEXT,44,19)[0]+
        stat(486,470,140,64,"66%","edit thr.",GREEN)+
        code_pane(642,470,180,64,[[(3,None),(3,'edit'),(2,None)],[(2,None),(4,'edit'),(2,None)]],unit=7))
    # c4 right bottom: equal highlight count controls
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(852,366,364,184,fill=PANEL,stroke=STROKE)+
        rect(852,366,6,184,fill=TEAL,rx=6,sw=0)+
        T(880,402,"Same count of highlights",15.5,TEAL,"800")+
        para(880,430,"Thresholds are chosen so every condition shows the same total number of highlights.",13.5,SEC,42,19)[0]+
        T(880,508,"which tokens, not how many",12.8,TEAL,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Study Design","30 Python programmers, LeetCode tasks")
    # c1 breadth strip: participants
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,96,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,96,fill=TEAL,rx=6,sw=0)+
        T(92,194,"Experienced Python programmers at a large US tech company",16.5,TEXT,"800")+
        para(92,224,"Each participant was paid fifty dollars for roughly an hour of their time.",14,SEC,80,20)[0]+
        stat(980,168,110,76,"30","participants",TEAL)+
        stat(1100,168,110,76,"$50","~1 hour",ACCENT))
    # c2 tasks
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,270,560,152,fill=PANEL,stroke=STROKE)+
        rect(64,270,6,152,fill=ACCENT,rx=6,sw=0)+
        T(92,306,"Three LeetCode easy problems",16.5,ACCENT,"800")+
        para(92,336,"A ten-minute cap per task; participants could run their code and a set of provided unit tests to debug.",13.5,TEXT,58,20)[0]+
        chip(92,380,"3 easy tasks",ACCENT,w=158,h=32)+
        chip(266,380,"10-min cap",SEC,w=150,h=32)+
        chip(432,380,"run unit tests",TEAL,w=158,h=32))
    # c3 randomization
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,270,560,152,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,270,6,152,fill=GREEN,rx=6,sw=0)+
        T(684,306,"Randomized for a fair comparison",16.5,GREEN,"800")+
        para(684,336,"Both task order and which tool went with which task were randomized across participants.",13.5,TEXT,58,20)[0]+
        chip(684,388,"task order  +  tool-task pairing  randomized",GREEN,w=504,h=28))
    # c4 edit model training set
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,438,1152,112,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,438,6,112,fill=GOLD,rx=6,sw=0)+
        T(92,474,"The edit model was trained earlier, separately",16,GOLD,"800")+
        para(92,504,"It learned from a separate group of nine coders who had previously edited Codex output until their tasks passed the tests.",14,SEC,86,22)[0]+
        stat(980,452,230,84,"9 coders","separate group",GOLD))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Edit highlights are fastest; gen-prob is worst")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,110,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,158,6,110,fill=GREEN,rx=6,sw=0)+
        T(92,196,"The headline result is about speed",16.5,GREEN,"800")+
        para(92,226,"With edit-model highlights, people finished their tasks fastest of the three conditions.",14,SEC,74,20)[0]+
        stat(720,170,236,84,"8.59 min","edit model (fastest)",GREEN)+
        stat(970,170,246,84,"9.61 min","gen-prob (slowest)",GOLD))
    # c2 time bars (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,284,560,264,fill=PANEL,stroke=STROKE)+
        rect(64,284,6,264,fill=ACCENT,rx=6,sw=0)+
        T(92,320,"Mean task time by condition",16,ACCENT,"800")+
        para(92,348,"Edit-model fastest, generation-probability slowest, no-highlight in between.",13.5,SEC,60,20)[0]+
        bar(300,404,240,8.59,10.0,GREEN,"edit model","8.59",h=26)+
        bar(300,448,240,9.10,10.0,SEC,"no highlight","in between",h=26)+
        bar(300,492,240,9.61,10.0,GOLD,"gen-prob","9.61",h=26))
    # c3 significance (right top)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,284,560,120,fill=PANEL,stroke=STROKE)+
        rect(656,284,6,120,fill=TEAL,rx=6,sw=0)+
        T(684,320,"The gap is highly significant",16,TEAL,"800")+
        para(684,350,"Between the two highlighting strategies, the speed difference is highly significant.",13.5,SEC,64,20)[0]+
        T(684,392,"p = 0.003",15,TEAL,"800",ff=MONO))
    # c4 the striking part (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,420,560,128,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,420,6,128,fill=GOLD,rx=6,sw=0)+
        T(684,454,"Gen-prob was the worst of the three",15.5,GOLD,"800")+
        para(684,482,"Generation-probability highlighting was slower even than showing no highlights at all - highlighting the wrong tokens can hurt, not help.",13.5,TEXT,62,19)[0]+
        T(684,540,"wrong tokens highlighted  ->  slower",12.8,GOLD,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Why It Works","Do the highlights predict what people edit?")
    # c1 setup (left top)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,160,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,160,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Measure: token survival",16.5,ACCENT,"800")+
        para(92,226,"The authors tracked which tokens survived - were left unchanged by the participant.",14,SEC,62,21)[0]+
        chip(92,286,"survived  =  token left unchanged",ACCENT,w=468,h=28))
    # c2 edit model bars (left bottom)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,332,560,218,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,332,6,218,fill=GREEN,rx=6,sw=0)+
        T(92,370,"Edit model: highlights track edits",16,GREEN,"800")+
        para(92,400,"Tokens it left un-highlighted survived far more often than the tokens it did highlight.",14,TEXT,56,21)[0]+
        bar(360,472,200,0.87,1.0,GREEN,"un-highlighted","87%",h=24)+
        bar(360,510,200,0.35,1.0,GOLD,"highlighted","35%",h=24))
    # c3 gen-prob comparison (right top)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,160,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,158,6,160,fill=GOLD,rx=6,sw=0)+
        T(684,196,"Gen-prob: highlights barely move it",16,GOLD,"800")+
        para(684,226,"Under generation-probability highlighting, highlighted tokens still survived most of the time.",14,TEXT,58,21)[0]+
        bar(884,290,296,0.74,1.0,GOLD,"gen-prob highlighted","74%",h=22))
    # c4 conclusion + progression (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,332,560,218,fill=PANEL,stroke=STROKE)+
        rect(656,332,6,218,fill=TEAL,rx=6,sw=0)+
        T(684,370,"Edit highlights predict real edits",16.5,TEAL,"800")+
        para(684,398,"The edit model's highlights closely predict what people actually change; gen-prob highlights barely move the needle. All differences are extremely significant.",13.5,SEC,62,19)[0]+
        T(684,490,"survival if highlighted",12.5,TER,"700")+
        bar(884,504,300,0.35,1.0,GREEN,"edit","35%",h=20)+
        bar(884,530,300,0.74,1.0,GOLD,"gen-prob","74%",h=20))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS (3 chunks) ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The impact in one place")
    # c1 the time strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,166,1152,150,fill=PANEL,stroke=STROKE)+
        rect(64,166,6,150,fill=GREEN,rx=6,sw=0)+
        T(92,202,"Task time fell with edit-model highlights",16.5,GREEN,"800")+
        stat(92,220,300,80,"9.61 min","generation probability",GOLD)+
        T(410,268,"->",26,GREEN,"800")+
        stat(452,220,300,80,"8.59 min","edit model",GREEN)+
        rect(772,220,444,80,fill=PANEL2,stroke=STROKE,rx=12)+
        T(772+222,252,"a significant speed-up",14,SEC,"600",anchor="middle")+
        T(772+222,278,"p = 0.003",15,TEAL,"800",anchor="middle",ff=MONO))
    # c2 survival
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,332,560,218,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,332,6,218,fill=TEAL,rx=6,sw=0)+
        T(92,368,"Highlighted-token survival fell sharply",16,TEAL,"800")+
        para(92,398,"Tighter alignment with real edits: highlighted tokens survived far less often under the edit model.",13.5,TEXT,56,20)[0]+
        stat(92,462,236,64,"74%","gen-prob survived",GOLD)+
        T(340,502,"->",24,TEAL,"800")+
        stat(380,462,236,64,"35%","edit survived",TEAL)+
        T(92,542,"p < 0.0001",13.5,TEAL,"800",ff=MONO))
    # c3 preference
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,332,560,218,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,332,6,218,fill=GOLD,rx=6,sw=0)+
        T(684,368,"Users preferred the edit highlights",16,GOLD,"800")+
        para(684,398,"On a seven-point preference scale, users rated the edit highlights well above generation probability.",13.5,TEXT,58,20)[0]+
        bar(824,452,300,3.94,7.0,GREEN,"edit model","3.94",h=26)+
        bar(824,494,300,2.88,7.0,GOLD,"gen-prob","2.88",h=26)+
        T(684,542,"7-point scale  ·  p = 0.001",13.5,GOLD,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","What you highlight matters more than whether")
    cards=[
        (ch[0],ACCENT,64,"A simple but pointed lesson",
         "The lesson from the study is simple, but pointed - and it challenges an intuitive default."),
        (ch[1],GREEN,646,"Highlight where people edit",
         "What you highlight matters more than whether you highlight. Highlight where people are likely to edit, not where the model happened to be unsure."),
        (ch[2],GOLD,64,"Generation probabilities are not enough",
         "The model's own confidence, on its own, does not point programmers to the tokens that actually need their attention."),
        (ch[3],TEAL,646,"A signal products already collect",
         "Tools like Copilot already log the edits people make to AI suggestions - that signal could train an open-world edit model and carry these speed, precision, and preference gains into everyday coding."),
    ]
    cw=570; ys=[176,176,340,340]; hs=[148,148,210,210]
    for (c,col,x,ti,tx),y,hh in zip(cards,ys,hs):
        body=(rect(x,y,cw,hh,fill=PANEL,stroke=STROKE)+
              rect(x,y,6,hh,fill=col,rx=6,sw=0)+
              circle(x+40,y+40,10,fill=col)+
              T(x+64,y+46,ti,17.5,TEXT,"800"))
        body+=para(x+28,y+82,tx,14,SEC,60,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,576,1216,576,STROKE,1)
    b+=circle(84,600,7,fill=GREEN)
    b+=T(104,606,"Highlight human intervention, not model uncertainty",13.5,SEC,"600")
    b+=T(1216,606,"Generation Probabilities are Not Enough · NeurIPS 2022",14,SEC,"600",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
