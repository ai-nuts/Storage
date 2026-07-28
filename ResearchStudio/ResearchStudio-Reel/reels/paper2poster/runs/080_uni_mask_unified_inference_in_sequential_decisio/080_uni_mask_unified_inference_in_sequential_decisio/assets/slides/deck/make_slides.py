#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 080 (Uni[MASK] / NeurIPS 2022).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue
pass resolves every anchor from PPTX geometry."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
META = os.environ["VIDEO_META"]
OUT  = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)
AM = json.load(open(os.path.join(META, "_anchor_map.json")))

W, H = 1280, 720
BG="#0B1220"; PANEL="#141F33"; PANEL2="#1A2942"; STROKE="#2B3D5A"
ACCENT="#5B9BF0"; TEAL="#35D0C4"; GOLD="#F3C24B"; RED="#F0655C"; GREEN="#45C88A"; VIOLET="#A487F0"
TEXT="#EAF1FB"; SEC="#A0B4CE"; TER="#6B819C"; WHITE="#FFFFFF"
SANS="Arial, 'Helvetica Neue', Helvetica, sans-serif"
MONO="'DejaVu Sans Mono', 'Courier New', monospace"

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

def arrow(x1,y1,x2,y2,color=ACCENT,sw=2.5):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" '
            f'marker-end="url(#arw)"/>')

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

def eyebrow(label,col=ACCENT):
    return (rect(64,52,5,26,fill=col,rx=2,sw=0)+
            T(82,72,label.upper(),15,SEC,"700",ls="2.5"))

def header(label,title,tsize=30,col=ACCENT):
    return eyebrow(label,col)+T(64,110,title,tsize,TEXT,"800")

def chunks(slide_id):
    return AM[slide_id]["chunks"]

DEFS=(f'<defs><marker id="arw" markerWidth="9" markerHeight="9" refX="7" refY="4.5" '
      f'orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="{ACCENT}"/></marker></defs>')

def svg(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'width="{W}" height="{H}" font-family="{SANS}">{DEFS}'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>'
            f'{body}</svg>')

def hbar(x,y,w,val,vmax,color,label,valtxt,h=24,lblcolor=SEC):
    bw=max(3,w*val/vmax)
    return (rect(x,y,w,h,fill="#0E1B2E",stroke=STROKE,rx=6,sw=1)+
            rect(x,y,bw,h,fill=color,rx=6,sw=0)+
            T(x-14,y+h*0.70,label,13.5,lblcolor,"600",anchor="end")+
            T(x+bw+10,y+h*0.70,valtxt,13.5,color,"800"))

def kpi(x,y,w,num,lbl,col,nsize=32,h=112,sub=None):
    b=(rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
       rect(x,y,w,5,fill=col,rx=5,sw=0)+
       T(x+w/2,y+h*0.50,num,nsize,col,"800",anchor="middle"))
    if sub:
        b+=T(x+w/2,y+h*0.50+22,sub,12.5,SEC,"600",anchor="middle")
        b+=T(x+w/2,y+h*0.86,lbl,12.5,SEC,"600",anchor="middle")
    else:
        b+=T(x+w/2,y+h*0.80,lbl,12.5,SEC,"600",anchor="middle")
    return b

def chip(x,y,w,text,col,h=32,sz=14):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+17,y+h/2,5,fill=col)+
            T(x+32,y+h/2+5,text,sz,TEXT,"600"))

def tok(x,y,label,col,masked=False,w=42,h=34):
    """One trajectory token cell."""
    if masked:
        return (rect(x,y,w,h,fill="#241A34",stroke=VIOLET,rx=6,sw=1.6)+
                T(x+w/2,y+h*0.68,"?",18,VIOLET,"800",anchor="middle",ff=MONO))
    return (rect(x,y,w,h,fill=PANEL2,stroke=col,rx=6,sw=1.4)+
            T(x+w/2,y+h*0.66,label,13,col,"700",anchor="middle",ff=MONO))

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"NeurIPS 2022",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"UC Berkeley  ·  Microsoft Research  ·  CMU",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,156,"Uni[MASK]: Unified Inference in",39,WHITE,"800")
    b+=T(64,202,"Sequential Decision Problems",39,ACCENT,"800")
    b+=rect(64,228,232,30,fill="#241A34",stroke=VIOLET,rx=15,sw=1.5)+T(180,248,"one masked model, many tasks",14.5,VIOLET,"800",anchor="middle")
    b+=T(64,288,"Carroll · Paradise · Lin · Georgescu · Sun · Bignell · Milani · Hofmann · Hausknecht · Dragan · Devlin",13.5,TER,"500")
    cy=312; cw=274; gap=18; cx=64
    data=[
        (ch[0],ACCENT,"The idea","Predicting randomly masked tokens is what powers pretraining in language modeling."),
        (ch[1],VIOLET,"The transfer","Uni[MASK] shows the very same recipe applies to sequential decision making."),
        (ch[2],TEAL,"The tasks","Behavior cloning, offline RL, inverse dynamics, and waypoint conditioning are all studied here."),
        (ch[3],GREEN,"The payoff","One framework unifies them; a single model matches or beats specialized ones."),
    ]
    for i,(c,col,ti,tx) in enumerate(data):
        x=cx+i*(cw+gap)
        body=(rect(x,cy,cw,214,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+28,cy+48,7,fill=col)+
              T(x+46,cy+54,ti,17,TEXT,"800"))
        body+=para(x+22,cy+92,tx,14,SEC,30,23)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,566,1216,566,STROKE,1)
    b+=T(64,602,"arXiv:2211.10869",14,ACCENT,"700")
    b+=T(300,602,"github.com/micahcarroll/uniMASK",14,SEC,"600")
    b+=T(1216,602,"Tasks are just maskings of one trajectory",14,TEAL,"700",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","One trajectory, many siloed models")
    # c1 : each task its own model
    body=(rect(64,150,1152,150,fill=PANEL,stroke=STROKE)+
          rect(64,150,6,150,fill=RED,rx=6,sw=0)+
          T(92,186,"Every inference task gets its own specially trained model",16.5,RED,"800"))
    tasks=["Behavior\ncloning","Offline\nRL","Inverse\ndynamics","Goal / waypoint\nconditioning"]
    bx=104
    for i,tt in enumerate(tasks):
        x=bx+i*272
        body+=rect(x,214,236,70,fill=PANEL2,stroke=STROKE,rx=10)
        l1,l2=tt.split("\n")
        body+=T(x+118,242,l1,14.5,TEXT,"700",anchor="middle")
        body+=T(x+118,262,l2,14.5,SEC,"600",anchor="middle")
        body+=T(x+118,300-2,"separate model",11.5,TER,"600",anchor="middle")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],body)
    # c2 : same object
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,318,720,132,fill=PANEL,stroke=TEAL,rx=14,sw=1.5)+
        rect(64,318,6,132,fill=TEAL,rx=6,sw=0)+
        T(92,354,"Yet all operate on the very same object",16.5,TEAL,"800")+
        T(92,398,"trajectory  =  ( s0 , a0 , p0 )  ( s1 , a1 , p1 )  …  ( sT , aT , pT )",16,TEXT,"700",ff=MONO)+
        T(92,428,"states, actions, and returns — shared across every task",14,SEC,"600"))
    # c3 : waste
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(800,318,416,132,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(800,318,6,132,fill=RED,rx=6,sw=0)+
        T(828,354,"The cost of siloing",16.5,RED,"800")+
        para(828,388,"A distinct model per task ignores this shared structure and misses reusable, richer representations.",14.5,SEC,40,23)[0])
    b+=line(64,486,1216,486,STROKE,1)
    b+=T(64,520,"The waste: shared trajectory structure is thrown away by per-task training.",14.5,SEC,"600")
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Masked prediction, borrowed from BERT",col=VIOLET)
    # c1 MLM
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,560,150,fill=PANEL,stroke=VIOLET,rx=14,sw=1.5)+
        rect(64,150,6,150,fill=VIOLET,rx=6,sw=0)+
        T(92,186,"Masked language modeling (BERT)",16.5,VIOLET,"800")+
        tok(92,204,"the",SEC)+tok(140,204,"cat",SEC)+tok(188,204,"",VIOLET,masked=True)+tok(236,204,"on",SEC)+tok(284,204,"",VIOLET,masked=True)+
        para(92,272,"Predict randomly masked tokens; the model learns bidirectional representations that transfer widely.",14,SEC,42,22)[0])
    # c2 maps directly
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(648,150,568,150,fill=PANEL,stroke=STROKE,rx=14)+
        rect(648,150,6,150,fill=ACCENT,rx=6,sw=0)+
        T(676,186,"The same idea maps onto decisions",16.5,ACCENT,"800")+
        tok(676,204,"s0",TEAL)+tok(724,204,"a0",GOLD)+tok(772,204,"s1",TEAL)+tok(820,204,"",VIOLET,masked=True)+
        T(880,226,"mask the last action",13.5,SEC,"600")+
        para(676,272,"Treat states and actions as tokens; the authors observe decision tasks are just maskings.",14,SEC,44,22)[0])
    # c3 BC = masking
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(64,318,720,138,fill=PANEL2,stroke=STROKE,rx=14)+
        rect(64,318,6,138,fill=GOLD,rx=6,sw=0)+
        T(92,354,"Mask the last action  =  a behavior-cloning inference",16.5,GOLD,"800")+
        T(92,398,"predict  a_t   given   s_0:t , a_0:t-1",17,TEXT,"800",ff=MONO)+
        para(92,428,"So one masked-prediction objective can, in principle, express the entire family of tasks.",14,SEC,64,22)[0])
    # c4 different tasks = different maskings
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(800,318,416,138,fill=PANEL,stroke=TEAL,rx=14,sw=1.5)+
        rect(800,318,6,138,fill=TEAL,rx=6,sw=0)+
        T(828,354,"One objective, many tasks",16.5,TEAL,"800")+
        para(828,388,"Different tasks are simply different masking patterns over the same trajectory of tokens.",14.5,SEC,40,23)[0])
    b+=line(64,492,1216,492,STROKE,1)
    b+=T(64,526,"Insight: decision-making inferences are different maskings of one trajectory.",14.5,VIOLET,"700")
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","Uni[MASK]: inference tasks as maskings")
    cards=[
        (ch[0],ACCENT,"A unifying framework","Cast each inference task as a masking scheme over a trajectory of state, action, and reward-to-go tokens."),
        (ch[1],TEAL,"One model, many tasks","Because tasks are just maskings, a single model trains on behavior cloning, reward conditioning, dynamics, and goal / waypoint conditioning together."),
        (ch[2],GREEN,"Matches and beats specialists","The single model often matches or exceeds specialized single-task models, and consistently wins after fine-tuning."),
        (ch[3],GOLD,"Decision-GPT baseline","Along the way, the authors introduce Decision-GPT, an improved GPT-based baseline for comparison."),
    ]
    y=152; hgt=100
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,hgt,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,hgt,fill=col,rx=6,sw=0)+
              circle(112,y+hgt/2,10,fill=col)+
              T(150,y+40,ti,18,TEXT,"800"))
        body+=para(150,y+68,tx,14.5,SEC,98,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=hgt+13
    b+=T(64,y+22,"A single masked model replaces a zoo of task-specific ones.",14.5,ACCENT,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Tokenize the trajectory, then mask")
    # c1 : tokenization row
    body=(rect(64,148,1152,132,fill=PANEL,stroke=STROKE)+
          rect(64,148,6,132,fill=ACCENT,rx=6,sw=0)+
          T(92,182,"A trajectory becomes per-timestep tokens: state, action, property (return-to-go)",16,ACCENT,"800"))
    x0=100; ty=204
    cols=[("s0",TEAL),("a0",GOLD),("p0",VIOLET),("s1",TEAL),("a1",GOLD),("p1",VIOLET),
          ("s2",TEAL),("a2",GOLD),("p2",VIOLET),("sT",TEAL),("aT",GOLD),("pT",VIOLET)]
    for i,(lb,co) in enumerate(cols):
        gap = 14 if i==9 else 0
        x=x0+i*46+gap
        if i==9: body+=T(x-10,ty+24,"…",18,SEC,"800",anchor="middle")
        body+=tok(x,ty,lb,co)
    body+=T(100,272,"state",12.5,TEAL,"700")+T(238,272,"action",12.5,GOLD,"700")+T(392,272,"return-to-go",12.5,VIOLET,"700")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],body)
    # c2 : masking scheme
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,298,560,158,fill=PANEL2,stroke=STROKE,rx=14)+
        rect(64,298,6,158,fill=TEAL,rx=6,sw=0)+
        T(92,332,"A masking scheme sets two things",16,TEAL,"800")+
        chip(92,350,240,"which inputs are visible",ACCENT,h=30)+
        chip(348,350,236,"which outputs are scored",GOLD,h=30)+
        para(92,410,"Different visible / predicted splits recover different inference tasks from one model.",14,SEC,50,22)[0])
    # c3 : tasks = maskings (BC / goal / reward)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(648,298,568,158,fill=PANEL,stroke=STROKE,rx=14)+
        rect(648,298,6,158,fill=GOLD,rx=6,sw=0)+
        T(676,332,"Reveal / predict = choose the task",16,GOLD,"800")+
        T(676,362,"BC:  see s_0:t , a_0:t-1  →  predict a_t",13.5,TEXT,"700",ff=MONO)+
        T(676,388,"Goal:  additionally reveal a future state",13.5,TEXT,"700",ff=MONO)+
        T(676,414,"Reward:  reveal return-to-go token",13.5,TEXT,"700",ff=MONO)+
        T(676,440,"backbone: bidirectional BERT-style encoder",12.5,ACCENT,"700"))
    # c4 : four regimes
    reg=[("Single-task",RED),("Multi-task",GOLD),("Random-mask",TEAL),("Fine-tune",GREEN)]
    body=rect(64,472,1152,86,fill=PANEL,stroke=STROKE,rx=14)+rect(64,472,6,86,fill=GREEN,rx=6,sw=0)
    body+=T(92,502,"Four training regimes compared",15.5,GREEN,"800")
    for i,(nm,co) in enumerate(reg):
        x=420+i*196
        body+=rect(x,484,180,54,fill=PANEL2,stroke=co,rx=10,sw=1.4)
        body+=T(x+90,510,nm,15,co,"800",anchor="middle")
        sub=["one task only","random scheme","arbitrary masking","pretrain + finetune"][i]
        body+=T(x+90,528,sub,11.5,SEC,"600",anchor="middle")
    b+=anchor(ch[3]["aid"],ch[3]["kw"],body)
    b+=T(64,592,"Random masking during pretraining, then task-specific fine-tuning, is the strongest recipe.",13.5,SEC,"600")
    return svg(b)

# ---------- SLIDE 6: DATASET / BENCHMARK ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Benchmark","Two decision-making environments")
    # c1 banner
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,60,fill=PANEL2,stroke=STROKE,rx=12)+
        rect(64,150,6,60,fill=ACCENT,rx=6,sw=0)+
        T(92,187,"The framework is evaluated on two environments — one discrete, one continuous",16,ACCENT,"800"))
    # c2 MiniGrid
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,228,560,236,fill=PANEL,stroke=TEAL,rx=14,sw=1.5)+
        rect(64,228,6,236,fill=TEAL,rx=6,sw=0)+
        T(92,264,"MiniGrid",19,TEAL,"800")+T(214,264,"discrete gridworld",13.5,SEC,"600")+
        rect(92,286,150,150,fill="#0E1B2E",stroke=STROKE,rx=8)+
        line(117,311,217,311,STROKE,1)+line(117,336,217,336,STROKE,1)+line(117,361,217,361,STROKE,1)+line(117,386,217,386,STROKE,1)+
        line(142,286,142,436,STROKE,1)+line(167,286,167,436,STROKE,1)+line(192,286,192,436,STROKE,1)+
        rect(97,291,40,40,fill=ACCENT,rx=4,sw=0,opacity=0.9)+T(117,316,"A",14,WHITE,"800",anchor="middle")+
        rect(172,391,40,40,fill=GREEN,rx=4,sw=0,opacity=0.9)+T(192,416,"G",14,WHITE,"800",anchor="middle")+
        rect(147,341,20,20,fill=GOLD,rx=3,sw=0)+
        para(262,314,"Agent must reach a fixed goal behind a locked door. Used to show the many inference tasks one model can do, and to compare task-specific validation losses.",13.5,SEC,32,21)[0])
    # c3 Maze2D
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(648,228,568,236,fill=PANEL,stroke=GOLD,rx=14,sw=1.5)+
        rect(648,228,6,236,fill=GOLD,rx=6,sw=0)+
        T(676,264,"Maze2D",19,GOLD,"800")+T(806,264,"continuous control · D4RL",13.5,SEC,"600")+
        para(676,300,"A MuJoCo-physics maze. Test-time reward over 1000 rollouts across 5 seeds.",13.5,SEC,44,21)[0]+
        T(676,352,"Baselines",13.5,TEXT,"800")+
        chip(676,364,168,"Feedforward net",SEC,h=30,sz=12.5)+
        chip(852,364,196,"Decision Transformer",ACCENT,h=30,sz=12.5)+
        chip(676,402,168,"Decision-GPT (ours)",GREEN,h=30,sz=12.5)+
        T(860,423,"context lengths 5 and 10",12.5,SEC,"600"))
    b+=line(64,488,1216,488,STROKE,1)
    b+=T(64,522,"MiniGrid probes task breadth; Maze2D measures reward against strong sequence baselines.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Train on many, win on each")
    # c1 MiniGrid
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,560,150,fill=PANEL,stroke=TEAL,rx=14,sw=1.5)+
        rect(64,150,6,150,fill=TEAL,rx=6,sw=0)+
        T(92,184,"MiniGrid",16.5,TEAL,"800")+
        para(92,214,"Random-mask training beats single-task on all tasks. Adding fine-tuning is best of all — winning on every task except behavior cloning.",14,SEC,44,22)[0]+
        chip(92,268,236,"random-mask > single-task (all)",TEAL,h=28,sz=12.5)+
        chip(340,268,180,"+ finetune = best",GREEN,h=28,sz=12.5))
    # c2 implication
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(648,150,568,150,fill=PANEL2,stroke=STROKE,rx=14)+
        rect(648,150,6,150,fill=GOLD,rx=6,sw=0)+
        T(676,184,"Why it matters",16.5,GOLD,"800")+
        para(676,220,"Even if you care about only one inference task, first training on many tasks generally helps that one task.",15,SEC,46,24)[0])
    # c3 Maze2D bars
    body=(rect(64,318,1152,204,fill=PANEL,stroke=GOLD,rx=14,sw=1.5)+
          rect(64,318,6,204,fill=GOLD,rx=6,sw=0)+
          T(92,352,"Maze2D reward — fine-tuning is critical (context length 5)",16.5,GOLD,"800"))
    bx=340; bw=720; vmax=3.0; y=372
    rows=[("Uni[MASK] multi-task + finetune",2.73,GREEN),
          ("Uni[MASK] random-mask + finetune",2.74,TEAL),
          ("Decision Transformer",1.49,ACCENT),
          ("Feedforward",1.60,SEC),
          ("Decision Transformer (BC)",1.13,RED)]
    for i,(lb,v,co) in enumerate(rows):
        body+=hbar(bx,y+i*28,bw,v,vmax,co,lb,f"{v:.2f}",h=22)
    body+=line(bx+bw*2.0/vmax,368,bx+bw*2.0/vmax,y+5*28-4,TER,1,dash="3 4")
    body+=T(bx+bw*2.0/vmax,366,"2.0",11,TER,"600",anchor="middle")
    b+=anchor(ch[2]["aid"],ch[2]["kw"],body)
    b+=T(64,552,"Fine-tuned Uni[MASK] reaches ~2.7, outperforming every baseline at context length 5.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation","Two controlled comparisons")
    # c1 regime comparison
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,560,150,fill=PANEL,stroke=STROKE,rx=14)+
        rect(64,150,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,184,"1 · Which ingredient matters?",16.5,ACCENT,"800")+
        para(92,214,"Comparing the four training regimes isolates each ingredient — and shows fine-tuning is the decisive one for the harder Maze2D environment.",14,SEC,44,22)[0]+
        chip(92,272,180,"fine-tune = decisive",GREEN,h=28,sz=12.5))
    # c2 backbone comparison
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(648,150,568,150,fill=PANEL,stroke=STROKE,rx=14)+
        rect(648,150,6,150,fill=GOLD,rx=6,sw=0)+
        T(676,184,"2 · BERT vs GPT backbone",16.5,GOLD,"800")+
        para(676,214,"Single-task Uni[MASK] vs Decision-GPT holds everything fixed except the backbone: bidirectional BERT-style vs autoregressive GPT-style.",14,SEC,46,22)[0]+
        chip(676,272,150,"BERT-style",TEAL,h=28,sz=12.5)+chip(838,272,150,"GPT-style",VIOLET,h=28,sz=12.5))
    # c3 nuance: context length
    body=(rect(64,318,1152,150,fill=PANEL2,stroke=STROKE,rx=14)+
          rect(64,318,6,150,fill=VIOLET,rx=6,sw=0)+
          T(92,352,"The nuance: context length flips the winner",16.5,VIOLET,"800"))
    body+=rect(96,368,520,84,fill="#0F2A28",stroke=TEAL,rx=10,sw=1.3)
    body+=T(356,394,"Context length 5",14,TEAL,"800",anchor="middle")
    body+=T(356,428,"BERT-style Uni[MASK] works well",14.5,TEXT,"700",anchor="middle")
    body+=rect(664,368,520,84,fill="#241A34",stroke=VIOLET,rx=10,sw=1.3)
    body+=T(924,394,"Context length 10",14,VIOLET,"800",anchor="middle")
    body+=T(924,428,"BERT degrades → Decision-GPT wins",14.5,TEXT,"700",anchor="middle")
    b+=anchor(ch[2]["aid"],ch[2]["kw"],body)
    b+=T(64,502,"Takeaway: BERT-style backbones struggle with longer-sequence generation.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The impact in four numbers",col=GOLD)
    # c1 banner
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,54,fill=PANEL2,stroke=STROKE,rx=12)+
        rect(64,150,6,54,fill=GOLD,rx=6,sw=0)+
        T(92,184,"A few numbers capture the impact",16,GOLD,"800"))
    # c2 KPI tiles (Maze2D ctx5)
    body=T(64,246,"Maze2D reward at context length 5",14.5,TEXT,"800")
    kx=64; kw=274; kg=18
    body+=kpi(kx,262,kw,"2.73",'Uni[MASK] finetune · BC',GREEN,nsize=36)
    body+=kpi(kx+(kw+kg),262,kw,"1.13",'Decision Transformer · BC',RED,nsize=36)
    body+=kpi(kx+2*(kw+kg),262,kw,"2.73",'Uni[MASK] finetune · RC',GREEN,nsize=36)
    body+=kpi(kx+3*(kw+kg),262,kw,"1.49",'Decision Transformer · RC',RED,nsize=36)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],body)
    # c3 seeds
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(64,398,560,116,fill=PANEL,stroke=STROKE,rx=14)+
        rect(64,398,6,116,fill=ACCENT,rx=6,sw=0)+
        T(92,432,"Averaged for reliability",16,ACCENT,"800")+
        T(92,470,"5 seeds",22,TEAL,"800")+T(196,470,"·",22,SEC,"800")+T(216,470,"1000 rollouts",22,TEAL,"800")+
        T(92,498,"per Maze2D configuration",13,SEC,"600"))
    # c4 one model many tasks
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(648,398,568,116,fill=PANEL,stroke=GREEN,rx=14,sw=1.5)+
        rect(648,398,6,116,fill=GREEN,rx=6,sw=0)+
        T(676,430,"One model, five inference tasks",16,GREEN,"800")+
        chip(676,446,168,"behavior cloning",TEAL,h=28,sz=12)+
        chip(852,446,150,"reward cond.",GOLD,h=28,sz=12)+
        chip(1010,446,170,"dynamics",ACCENT,h=28,sz=12)+
        chip(676,480,168,"goal conditioning",VIOLET,h=28,sz=12)+
        chip(852,480,196,"waypoint conditioning",GREEN,h=28,sz=12))
    b+=T(64,548,"Fine-tuned Uni[MASK] roughly doubles the Decision Transformer's reward, from one model.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Many tasks, one masked model",col=TEAL)
    cards=[
        (ch[0],TEAL,"Tasks are maskings","Many seemingly distinct sequential-decision tasks are just different maskings of the same trajectory — so one masked-prediction model can replace a zoo of specialized ones."),
        (ch[1],GREEN,"Pretrain on many, then fine-tune","Training on many masking schemes and then fine-tuning generally beats training on any single task alone — even when you only care about that one task."),
        (ch[2],GOLD,"The caveat is architectural","BERT-style backbones shine at short contexts but struggle to generate over longer sequences; combining GPT-style backbones with random masking is a promising next step."),
    ]
    y=160; hgt=118
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,hgt,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,hgt,fill=col,rx=6,sw=0)+
              circle(112,y+hgt/2,10,fill=col)+
              T(150,y+44,ti,18.5,TEXT,"800"))
        body+=para(150,y+76,tx,15,SEC,92,23)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=hgt+14
    b+=line(64,y+8,1216,y+8,STROKE,1)
    b+=T(64,y+40,"Uni[MASK]  ·  Unified Inference in Sequential Decision Problems",15.5,TEXT,"700")
    b+=T(1216,y+40,"NeurIPS 2022  ·  arXiv:2211.10869",13.5,SEC,"600",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline_numbers",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
