#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 059
(Bayesian Inverse Transition Learning for Offline Settings).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue
pass resolves every anchor from PPTX geometry."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
META = os.environ["VIDEO_META"]
OUT  = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)
AM = json.load(open(os.path.join(META, "_anchor_map.json")))
QR_PAPER = os.path.join(os.environ["VIDEO_OUT"], "assets/qr/paper.png")
LOGO_H = os.path.join(os.environ["VIDEO_OUT"], "assets/logos/harvard-university.png")
LOGO_I = os.path.join(os.environ["VIDEO_OUT"], "assets/logos/imperial-college-london.png")

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

def image(x,y,w,h,href):
    return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{esc(href)}" preserveAspectRatio="xMidYMid meet"/>'

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
            T(x-12,y+h*0.72,label,14,lblcolor,"600",anchor="end")+
            T(x+bw+10,y+h*0.72,valtxt,14,color,"800"))

def chip(x,y,w,text,col,h=34,size=14.5):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+5,text,size,TEXT,"600"))

def kpi(x,y,w,num,lbl,col,h=100,nsize=30):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.54,num,nsize,col,"800",anchor="middle")+
            T(x+w/2,y+h*0.82,lbl,12.5,SEC,"600",anchor="middle"))

# ---------- SLIDE 1: TITLE (3 chunks) ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICML 2023",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Harvard University   ·   Imperial College London",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,158,"Bayesian Inverse Transition Learning",42,WHITE,"800")
    b+=T(64,200,"Safe, gradient-free offline RL from a near-optimal expert",20,ACCENT,"700")
    b+=T(64,236,"Leo Benac   ·   Sonali Parbhoo   ·   Finale Doshi-Velez      —   Harvard, Imperial College London",15.5,SEC,"500")
    cy=280; cw=370; gap=21; cx=64
    data=[
        (RED,"The failure mode","Offline RL must estimate transition dynamics from fixed data — plain maximum likelihood gives high-variance policies that act unsafely where data is thin."),
        (ACCENT,"Inverse Transition Learning","A gradient-free, constraint-based method: use a near-optimal expert's demonstrations to CLIP a Bayesian posterior over the dynamics."),
        (GREEN,"Safe by construction","Every sampled model yields a safe, high-performing policy — 100% accuracy where the best action is known, with dramatically lower variance."),
    ]
    for i,(col,ti,tx) in enumerate(data):
        x=cx+i*(cw+gap)
        body=(rect(x,cy,cw,214,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+28,cy+44,7,fill=col)+
              T(x+46,cy+50,ti,16.5,TEXT,"800"))
        pp,_=para(x+22,cy+88,tx,14,SEC,42,22)
        body+=pp
        b+=anchor(ch[i]["aid"],ch[i]["kw"],body)
    b+=line(64,528,1216,528,STROKE,1)
    b+=T(64,568,"A distribution of dynamics guaranteed to induce safe, high-performing offline policies.",16,TEXT,"600")
    b+=T(64,606,"arXiv:2308.05075",14,ACCENT,"700")
    # logos + QR utility cluster (lower-right) — kept as small utility marks
    if os.path.exists(LOGO_H):
        b+=rect(852,580,100,40,fill=WHITE,rx=8,sw=0)+image(864,587,74,26,LOGO_H)
    if os.path.exists(LOGO_I):
        b+=rect(962,580,100,40,fill=WHITE,rx=8,sw=0)+image(974,587,74,26,LOGO_I)
    if os.path.exists(QR_PAPER):
        b+=rect(1148,566,64,80,fill=WHITE,rx=8,sw=0)+image(1156,572,48,48,QR_PAPER)+T(1180,636,"Paper",11,TER,"700",anchor="middle")
    return svg(b)

# ---------- SLIDE 2: PROBLEM (3 chunks) ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","You cannot experiment — you only have a fixed batch")
    # c1 left tall card
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,404,6,fill=ACCENT,rx=6,sw=0)+
        T(92,206,"No new interactions allowed",18,TEXT,"800")+
        para(92,242,"In healthcare and education we cannot experiment on people. Offline RL must learn the transition dynamics T purely from a fixed batch of logged experience.",15,SEC,40,24)[0]+
        # batch glyph
        rect(120,360,292,150,fill=PANEL2,stroke=STROKE,rx=10)+
        T(266,392,"fixed batch  D",14,TEAL,"800",anchor="middle",ff=MONO)+
        line(140,410,392,410,STROKE,1,dash="3 4")+
        circle(160,440,7,fill=ACCENT)+circle(210,440,7,fill=ACCENT)+circle(260,440,7,fill=STROKE)+
        circle(310,440,7,fill=ACCENT)+circle(360,440,7,fill=STROKE)+
        circle(160,478,7,fill=STROKE)+circle(210,478,7,fill=ACCENT)+circle(260,478,7,fill=STROKE)+
        circle(310,478,7,fill=STROKE)+circle(360,478,7,fill=ACCENT)+
        T(266,506,"logged (s, a) pairs — no queries",12,TER,"600",anchor="middle"))
    # c2 right top: coverage gap
    fx=500; fw=716
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,176,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,176,fill=GOLD,rx=6,sw=0)+
        T(fx+28,198,"The data only covers what users did",17,GOLD,"800")+
        para(fx+28,232,"Logged trajectories reveal only the actions the original users actually took. Vast parts of the state-action space are simply never seen.",15,SEC,66,24)[0]+
        rect(fx+28,286,fw-56,32,fill=PANEL2,stroke=STROKE,rx=6)+
        T(fx+44,307,"covered state-action pairs  <<  full state-action space",13.5,GOLD,"700",ff=MONO))
    # c3 right bottom: MLE unsafe (danger)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,350,fw,200,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(fx,350,6,200,fill=RED,rx=6,sw=0)+
        T(fx+28,390,"Maximum likelihood breaks down",17,RED,"800")+
        para(fx+28,424,"An MLE fit of the dynamics yields policies that swing wildly from one dataset to the next, and recommend genuinely unsafe actions exactly where data is thin.",15,TEXT,66,24)[0]+
        T(fx+28,512,"high variance  +  unsafe actions  where coverage is poor",15,RED,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 3: MOTIVATION (4 chunks) ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","The expert who logged the data already knows a lot")
    # c1 full-width headline
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,84,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,84,fill=TEAL,rx=6,sw=0)+
        T(92,194,"Key insight",15,TEAL,"800",ls="1.5")+
        T(92,224,"The people who generate offline data — clinicians, teachers — are usually acting near-optimally.",17,TEXT,"600"))
    # c2 left card: choices encode good/bad
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,262,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,262,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,300,"Their choices are a hidden signal",17,ACCENT,"800")+
        para(92,332,"Each expert decision quietly encodes which actions are good and which are bad — yet a plain MLE fit of the dynamics throws that information away.",14.5,SEC,54,22)[0]+
        T(92,400,"expert action  =  implicit label on quality",13,TEAL,"700",ff=MONO))
    # c3 right card: prior gradient IRL fragile
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(648,262,568,150,fill=PANEL,stroke=STROKE)+
        rect(648,262,6,150,fill=GOLD,rx=6,sw=0)+
        T(676,300,"Prior gradient-based inverse RL",17,GOLD,"800")+
        para(676,332,"Earlier methods estimate an expert's belief of the dynamics, but never tie it back to the true environment — and inherit the fragility of gradient optimization.",14.5,SEC,54,22)[0]+
        T(676,400,"estimated T  =/=  true T   ·   gradients are brittle",13,GOLD,"700",ff=MONO))
    # c4 full-width goal
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,432,1152,118,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,432,6,118,fill=TEAL,rx=6,sw=0)+
        T(92,470,"Our goal",15,TEAL,"800",ls="1.5")+
        T(92,502,"Exploit the expert signal directly, and without any gradients.",19,TEXT,"800")+
        T(92,532,"turn near-optimal demonstrations into hard constraints on the dynamics",14,SEC,"600"))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION (3 chunks) ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","Inverse Transition Learning: constraints meet a posterior")
    cards=[
        (ch[0],ACCENT,"1","Gradient-free & constraint-based","We introduce Inverse Transition Learning (ITL) — a gradient-free, constraint-based approach to estimating offline dynamics."),
        (ch[1],GREEN,"2","Clip the Bayesian posterior","Convert a near-optimal expert policy into constraints on the dynamics, then clip a Bayesian posterior so every sampled model yields a safe, high-performing policy."),
        (ch[2],GOLD,"3","Analysis of when MLE fails","We analyze exactly when and why MLE breaks under uneven coverage, and show constraints plus uncertainty rank actions even where the expert is unsure."),
    ]
    cw=368; gap=24; x0=64; cy=176
    for i,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,374,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+52,cy+70,27,fill="none",stroke=col,sw=2.5)+
              T(x+52,cy+80,num,30,col,"800",anchor="middle"))
        yy=cy+140
        for j,ln in enumerate(wrap(ti,22)):
            body+=T(x+28,yy+j*28,ln,18.5,TEXT,"800")
        yy+=28*len(wrap(ti,22))+14
        body+=para(x+28,yy,tx,15,SEC,40,25)[0]
        b+=anchor(c["aid"],c["kw"],body)
    return svg(b)

# ---------- SLIDE 5: METHOD (4 chunks) ----------
def s_method():
    ch=chunks("method"); b=header("Method","From expert constraints to a clipped posterior")
    gx=[64,648]; gy=[158,362]; cw=568; chh=192
    # c1 Bellman constraints
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(gx[0],gy[0],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[0],gy[0],6,chh,fill=ACCENT,rx=6,sw=0)+
        T(gx[0]+28,gy[0]+38,"1 · Constraints from the Bellman equations",15.5,ACCENT,"800")+
        para(gx[0]+28,gy[0]+68,"Given rewards R, an epsilon-optimal expert policy, and batch data, the closed-form Bellman equations demand expert-taken actions out-value never-taken ones.",14,SEC,60,21)[0]+
        rect(gx[0]+28,gy[0]+140,cw-56,38,fill=PANEL2,stroke=STROKE,rx=8)+
        T(gx[0]+cw/2,gy[0]+165,"V = (I - gamma T)^-1 R    ->    Q(expert) > Q(other)",14.5,TEXT,"800",anchor="middle",ff=MONO))
    # c2 epsilon-ball structure
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(gx[1],gy[0],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[1],gy[0],6,chh,fill=TEAL,rx=6,sw=0)+
        T(gx[1]+28,gy[0]+38,"2 · Recover the expert's epsilon-ball",15.5,TEAL,"800")+
        para(gx[1]+28,gy[0]+68,"Any dynamics satisfying the constraints recovers the expert's epsilon-ball structure: the set of actions the expert would consider acceptable in each state.",14,SEC,60,21)[0]+
        circle(gx[1]+90,gy[0]+155,26,fill="none",stroke=TEAL,sw=2)+
        circle(gx[1]+90,gy[0]+155,6,fill=GREEN)+
        T(gx[1]+130,gy[0]+150,"good actions inside the ball",13.5,SEC,"600")+
        T(gx[1]+130,gy[0]+170,"bad actions strictly outside",13.5,TER,"600"))
    # c3 clipped posterior via rejection sampling
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(gx[0],gy[1],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[0],gy[1],6,chh,fill=GREEN,rx=6,sw=0)+
        T(gx[0]+28,gy[1]+38,"3 · Clip a Bayesian posterior",15.5,GREEN,"800")+
        para(gx[0]+28,gy[1]+68,"Place a Dirichlet-Multinomial posterior over the dynamics, then reject every sample that violates a constraint. The survivors form the clipped posterior.",14,SEC,60,21)[0]+
        rect(gx[0]+28,gy[1]+140,cw-56,38,fill=PANEL2,stroke=STROKE,rx=8)+
        T(gx[0]+cw/2,gy[1]+165,"P(T | D)   --reject-->   P(T | D, expert)",15,GREEN,"800",anchor="middle",ff=MONO))
    # c4 two experts + slack
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(gx[1],gy[1],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[1],gy[1],6,chh,fill=GOLD,rx=6,sw=0)+
        T(gx[1]+28,gy[1]+38,"4 · Two experts, plus a slack term",15.5,GOLD,"800")+
        para(gx[1]+28,gy[1]+68,"Separate constraint sets handle a fully optimal expert and a partially uncertain one. A tunable slack delta enforces the structure even under action non-linearity.",14,SEC,60,21)[0]+
        chip(gx[1]+28,gy[1]+138,(cw-56)/2-8,"optimal expert",TEAL,h=40,size=13.5)+
        chip(gx[1]+28+(cw-56)/2+8,gy[1]+138,(cw-56)/2-8,"uncertain + slack",GOLD,h=40,size=13.5))
    return svg(b)

# ---------- SLIDE 6: DATASET (4 chunks) ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","A controlled synthetic tabular MDP")
    # c1 MDP structure (left)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,232,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,232,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Synthetic tabular MDP",17,ACCENT,"800")+
        para(92,228,"A fully controlled Markov decision process where the true dynamics are known for evaluation.",14,SEC,54,21)[0]+
        kpi(92,282,152,"15 +1","states (+terminal)",ACCENT,h=92)+
        kpi(260,282,152,"6","actions",TEAL,h=92)+
        kpi(428,282,168,"0.95","discount factor",GOLD,h=92))
    # c2 mixed dynamics (right)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(656,158,560,232,fill=PANEL,stroke=STROKE)+
        rect(656,158,6,232,fill=TEAL,rx=6,sw=0)+
        T(684,196,"Deliberately mixed dynamics",17,TEAL,"800")+
        para(684,228,"Transition distributions are sometimes uniform and sometimes highly skewed toward a few states, to create rich, varied behavior.",14,SEC,54,21)[0]+
        # mini distribution glyphs, baseline y=338
        "".join(rect(704+i*17,338-18,13,18,fill=ACCENT,rx=1,sw=0) for i in range(5))+
        T(746,360,"uniform",12.5,SEC,"600",anchor="middle")+
        "".join(rect(944+i*17,338-h_,13,h_,fill=GOLD,rx=1,sw=0) for i,h_ in enumerate([5,10,38,12,6]))+
        T(986,360,"skewed",12.5,SEC,"600",anchor="middle")+
        line(848,300,848,346,STROKE,1,dash="3 4")+
        T(1176,338,"known true T",12.5,TER,"600",anchor="end"))
    # c3 regimes x optimality (full width grid)
    body=(rect(64,406,1152,144,fill=PANEL,stroke=STROKE)+
          rect(64,406,6,144,fill=GOLD,rx=6,sw=0)+
          T(92,442,"Two coverage regimes  x  three expert-optimality levels",16,TEXT,"800"))
    body+=chip(92,462,344,"Low data:  K = 15 episodes",ACCENT,h=36,size=13.5)
    body+=chip(456,462,344,"High data:  K = 300 episodes",ACCENT,h=36,size=13.5)
    body+=chip(820,462,396,"epsilon = 0 / 3 / 4  ->  0 / 3 / 6 uncertain states",GOLD,h=36,size=13.5)
    body+=T(92,528,"coverage and expert-optimality are varied independently to stress-test every method",13,TER,"600")
    b+=anchor(ch[2]["aid"],ch[2]["kw"],body)
    # c4 averaging note (bottom strip)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,566,1152,58,fill=PANEL2,stroke=STROKE)+
        rect(64,566,6,58,fill=GREEN,rx=6,sw=0)+
        T(92,601,"Every reported number is averaged over 1,000 independently generated datasets.",16,TEXT,"700"))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT (4 chunks) ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","The clipped posterior dominates every baseline")
    # c1 top banner
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,52,fill=PANEL,stroke=STROKE)+
        rect(64,150,6,52,fill=GREEN,rx=6,sw=0)+
        T(92,183,"On the Q*metric, P(T | D, expert) beats both maximum likelihood and the un-clipped posterior P(T | D).",16,TEXT,"700"))
    # c2 accuracy card (left) with bars
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,214,560,336,fill=PANEL,stroke=STROKE)+
        rect(64,214,6,336,fill=GREEN,rx=6,sw=0)+
        T(92,252,"100% accuracy on decided states",16.5,GREEN,"800")+
        para(92,284,"Where the expert knows a single best action, our method picks it every time, in every data and optimality setting.",14,SEC,56,21)[0]+
        T(92,356,"Accuracy on deterministic-policy states",13.5,SEC,"700")+
        bar(300,372,236,100,100,GREEN,"Ours","100%",h=26)+
        bar(300,412,236,92,100,ACCENT,"MLE best","92%",h=26)+
        bar(300,452,236,67,100,RED,"MLE worst","67%",h=26)+
        T(92,512,"MLE ranges 67-92% and is never guaranteed; ours is a constant 100%.",13,TER,"600"))
    # c3 no bad mistakes card (right) with Q*metric bars
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,214,560,336,fill=PANEL,stroke=STROKE)+
        rect(656,214,6,336,fill=ACCENT,rx=6,sw=0)+
        T(684,252,"Never a truly bad mistake",16.5,ACCENT,"800")+
        para(684,284,"Our policies never pick an action outside the expert's epsilon-ball. Lower Q*metric is better (0 = optimal).",14,SEC,56,21)[0]+
        T(684,356,"Q*metric at epsilon = 0, high data (lower is better)",13.5,SEC,"700")+
        bar(876,372,300,2,150,GREEN,"Ours","0",h=26)+
        bar(876,412,300,60,150,ACCENT,"MLE","59.75",h=26)+
        bar(876,452,300,142,150,GOLD,"P(T|D)","142",h=26)+
        T(684,512,"the plain posterior is even worse than MLE here.",13,TER,"600"))
    # c4 bottom strip: uncertain states
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,564,1152,116,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,564,6,116,fill=TEAL,rx=6,sw=0)+
        T(92,600,"A surprise on the uncertain states",16,TEAL,"800")+
        para(92,632,"Even though the constraints say nothing explicit about which action to pick when the expert is unsure, our method is still more accurate there than the baselines — the constraints implicitly transfer the expert's uncertainty structure.",15,TEXT,118,24)[0])
    return svg(b)

# ---------- SLIDE 8: ABLATION (3 chunks) ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","More data does not rescue maximum likelihood")
    # c1 top banner
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,58,fill=RED,rx=6,sw=0)+
        T(92,193,"A central finding: simply collecting more episodes does NOT fix MLE's unsafe behavior.",16.5,TEXT,"600"))
    # c2 bad-mistakes persist (left) with bars
    body=(rect(64,238,680,312,fill=PANEL,stroke=STROKE)+
          rect(64,238,6,312,fill=RED,rx=6,sw=0)+
          T(92,276,"Bad mistakes persist even with abundant data",16,TEXT,"800")+
          para(92,306,"Expert-only data leaves large parts of the state-action space unexplored no matter how many episodes we collect — an irreducible, aleatoric gap.",14,SEC,64,21)[0])
    body+=T(92,378,"Rate of bad mistakes (actions outside the epsilon-ball)",13.5,SEC,"700")
    body+=bar(300,398,360,44,60,RED,"MLE · low data","high",h=30)
    body+=bar(300,444,360,38,60,GOLD,"MLE · high data","still high",h=30)
    body+=bar(300,490,360,2,60,GREEN,"Ours · any data","none",h=30)
    body+=T(92,536,"only the constraints — not more data — eliminate the unsafe actions",13,TER,"600")
    b+=anchor(ch[1]["aid"],ch[1]["kw"],body)
    # c3 optimality sweep (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(764,238,452,312,fill=PANEL,stroke=STROKE)+
        rect(764,238,6,312,fill=GREEN,rx=6,sw=0)+
        T(792,276,"Robust across expert optimality",16,GREEN,"800")+
        para(792,308,"Sweeping epsilon from 0 through 4 confirms the method holds across every degree of expert optimality.",14,SEC,44,21)[0]+
        chip(792,368,396,"Holds for epsilon = 0, 1, 2, 3, 4",ACCENT,h=36,size=13.5)+
        chip(792,412,396,"Can even beat the demonstrating expert",GREEN,h=36,size=13.5)+
        rect(792,462,396,60,fill=PANEL2,stroke=GREEN,rx=10,sw=1.5)+
        T(812,490,"policy variance",13.5,SEC,"600")+T(1168,490,"~ 0",22,GREEN,"800",anchor="end")+
        T(812,510,"kept close to zero throughout the sweep",12,TER,"600"))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS (4 chunks) ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The impact, in the numbers")
    # c1 top banner (short chunk)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,56,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,56,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"The numbers tell a clear story — lower Q*metric is better, and zero is optimal.",16.5,TEXT,"600"))
    # three tiles below
    tiles=[
        (ch[1],GREEN,"0 ± 0","Q*metric at epsilon = 0","Exactly optimal with zero variance, in both low and high data — vs MLE 59.75 and the plain posterior 142."),
        (ch[2],ACCENT,"8.79","hardest setting, eps = 4","Beats MLE's 20.11 and roughly matches the near-optimal expert's 9.4 in the high-data regime."),
        (ch[3],GOLD,"52 -> 0","policy std. deviation","Deterministic-state accuracy is a constant 100%; policy variance collapses from about 52 down to essentially zero."),
    ]
    cw=370; gap=21; x0=64; y=238; hh=300
    for i,(c,col,num,lbl,tx) in enumerate(tiles):
        x=x0+i*(cw+gap)
        body=(rect(x,y,cw,hh,fill=PANEL,stroke=STROKE)+
              rect(x,y,6,hh,fill=col,rx=6,sw=0)+
              T(x+30,y+96,num,42,col,"800")+
              T(x+30,y+134,lbl,16.5,TEXT,"800"))
        body+=para(x+30,y+172,tx,14.5,SEC,42,23)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,572,1216,572,STROKE,1)
    b+=T(64,606,"Averaged over 1,000 datasets per setting.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY (2 chunks) ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Clip the posterior — get safe, expert-beating policies")
    cards=[
        (ch[0],GREEN,"Provably safe, gradient-free, low-variance","By clipping a Bayesian posterior over the transition dynamics with constraints derived from a near-optimal expert, you obtain gradient-free offline policies that are provably safe, can outperform the expert who generated the data, and carry dramatically lower variance than maximum likelihood."),
        (ch[1],TEAL,"Uncertainty becomes an action ranking","The same recipe of constraints plus uncertainty also yields a ranking of actions in the uncertain states, making the learned policies more informative for high-stakes planning such as clinical decision making."),
    ]
    y=176
    for c,col,ti,tx in cards:
        lines=wrap(tx,96)
        hh=88+len(lines)*25
        body=(rect(64,y,1152,hh,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,hh,fill=col,rx=6,sw=0)+
              circle(112,y+52,10,fill=col)+
              T(150,y+58,ti,20,TEXT,"800"))
        body+=para(150,y+92,tx,15.5,SEC,96,25)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=hh+22
    b+=line(64,y+8,1216,y+8,STROKE,1)
    b+=T(64,y+44,"Bayesian Inverse Transition Learning for Offline Settings",16,TEXT,"700")
    b+=T(64,y+70,"ICML 2023  ·  arXiv:2308.05075  ·  Benac, Parbhoo, Doshi-Velez",13.5,SEC,"600")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline_numbers",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
