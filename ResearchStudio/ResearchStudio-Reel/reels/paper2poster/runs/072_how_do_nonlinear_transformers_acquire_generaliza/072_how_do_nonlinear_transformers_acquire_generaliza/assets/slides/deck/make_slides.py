#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 072
(How Do Nonlinear Transformers Learn and Generalize in In-Context Learning? / ICML 2024).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue
pass resolves every anchor from PPTX geometry. All-native: zero <image>, zero gradients."""
import json, os

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

def poly(points,fill="none",stroke=None,sw=2,opacity=None,dash=None):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    d=f' stroke-dasharray="{dash}"' if dash else ""
    pts=" ".join(f"{a},{b}" for a,b in points)
    return f'<polyline points="{pts}" fill="{fill}"{st}{o}{d}/>'

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

def kpi(x,y,w,num,lbl,col,nsize=34,h=104,ff=SANS):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.52,num,nsize,col,"800",anchor="middle",ff=ff)+
            T(x+w/2,y+h*0.80,lbl,13,SEC,"600",anchor="middle"))

def chip(x,y,w,text,col,h=34,sz=14.5):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+5,text,sz,TEXT,"600"))

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICML 2024",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Rensselaer Polytechnic · IBM Watson",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"How Do Nonlinear Transformers Learn and",34,WHITE,"800")
    b+=T(64,192,"Generalize in In-Context Learning?",34,ACCENT,"800")
    b+=rect(64,216,196,30,fill="#0F2E2B",stroke=TEAL,rx=15,sw=1.5)+T(162,236,"First ICL theory",16,TEAL,"800",anchor="middle")
    b+=T(276,236,"nonlinear attention + nonlinear MLP, trained by gradient descent",15,SEC,"600")
    b+=T(64,272,"Hongkang Li · Meng Wang · Songtao Lu · Xiaodong Cui · Pin-Yu Chen",15,TER,"500")
    # four concept cards
    cy=300; cw=274; gap=18; cx=64
    data=[
        (ch[0],ACCENT,"In-context learning","A pretrained Transformer solves brand-new tasks from a few input-output examples in its prompt, with no fine-tuning."),
        (ch[1],GOLD,"The open question","Why does training produce this ability, and how far does it generalize? Nonlinear attention makes the math hard."),
        (ch[2],TEAL,"First training theory","The first analysis of training a Transformer with softmax attention and a ReLU MLP, with in- and out-of-domain guarantees."),
        (ch[3],GREEN,"Pruning is (almost) free","The first theory of pruning for ICL: removing the small-magnitude neurons barely hurts generalization."),
    ]
    for i,(c,col,ti,tx) in enumerate(data):
        x=cx+i*(cw+gap)
        body=(rect(x,cy,cw,226,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+28,cy+48,7,fill=col)+
              T(x+46,cy+54,ti,16,TEXT,"800"))
        body+=para(x+22,cy+94,tx,13.5,SEC,32,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,570,1216,570,STROKE,1)
    b+=T(64,606,"arXiv:2402.15607",14,ACCENT,"700")
    b+=T(300,606,"One-layer Transformer, provably trained for ICL",14,SEC,"600")
    b+=T(1216,606,"Generalizes in-domain and under distribution shift",14,TEAL,"700",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","A powerful ability we cannot explain")
    # c1 top band
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,150,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,188,"In-context learning: no fine-tuning required",16.5,ACCENT,"800")+
        para(92,218,"A pretrained Transformer handles a new task by simply padding the query with a handful of example input-output pairs. No weights are updated; the answer comes from the prompt alone.",15,SEC,98,24)[0]+
        # mini prompt strip
        chip(92,262,260,"example 1  (x1, y1)",TEAL,30,12.5)+
        chip(364,262,260,"example 2  (x2, y2)",TEAL,30,12.5)+
        chip(636,262,150,"...",SEC,30,12.5)+
        chip(800,262,240,"query  x  ->  ?",GOLD,30,12.5))
    # c2 left -- the puzzle
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,320,560,230,fill=PANEL,stroke=STROKE)+
        rect(64,320,6,230,fill=GOLD,rx=6,sw=0)+
        T(92,358,"The puzzle",17,GOLD,"800")+
        para(92,390,"Despite its empirical success, how a Transformer is actually trained to acquire in-context learning, and how far that ability generalizes, remains elusive.",14.5,SEC,58,23)[0]+
        chip(92,470,504,"How is ICL acquired during training?",ACCENT,32,13.5)+
        chip(92,510,504,"Does it generalize under distribution shift?",TEAL,32,13.5))
    # c3 right -- why it is hard
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,320,560,230,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(656,320,6,230,fill=RED,rx=6,sw=0)+
        T(684,358,"Why it is hard  ·  two nonlinearities",16.5,RED,"800")+
        para(684,390,"The training objective is nonconvex and resists the tools used for simpler models, because two layers are nonlinear:",14.5,SEC,58,23)[0]+
        chip(684,452,504,"softmax self-attention  ->  nonlinear",RED,32,13.5)+
        chip(684,492,504,"ReLU two-layer MLP  ->  nonlinear",GOLD,32,13.5))
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Prior theory keeps only part of the picture")
    # c1 top band
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,92,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,92,fill=TEAL,rx=6,sw=0)+
        T(92,186,"Recent works began to explain ICL",15,TEAL,"800",ls="1")+
        para(92,214,"Each existing analysis simplifies away one of the hard parts, so none captures a genuinely nonlinear Transformer trained end to end.",15,TEXT,100,24)[0])
    # three gap cards
    cw=368; gap=24; x0=64; cy=262; chh=200
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(x0,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0,cy,cw,6,fill=RED,rx=6,sw=0)+
        T(x0+28,cy+42,"Simplified models",16.5,RED,"800")+
        para(x0+28,cy+74,"Prior work ignores nonlinear self-attention, or replaces the nonlinear MLP with a linear one.",14.5,SEC,40,23)[0]+
        chip(x0+28,cy+140,cw-56,"drops softmax / linear MLP",RED,32,13))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(x0+cw+gap,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0+cw+gap,cy,cw,6,fill=GOLD,rx=6,sw=0)+
        T(x0+cw+gap+28,cy+42,"No shift, no pruning",16.5,GOLD,"800")+
        para(x0+cw+gap+28,cy+74,"Most study linear regression, none characterize training under distribution shift, and none analyze how pruning changes ICL.",14.5,SEC,40,23)[0]+
        chip(x0+cw+gap+28,cy+140,cw-56,"shift + pruning unexplained",GOLD,32,13))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(x0+2*(cw+gap),cy,cw,chh,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(x0+2*(cw+gap),cy,cw,6,fill=GREEN,rx=6,sw=0)+
        T(x0+2*(cw+gap)+28,cy+42,"Why it matters",16.5,GREEN,"800")+
        para(x0+2*(cw+gap)+28,cy+74,"Practitioners routinely prune large language models to save compute while hoping to keep their in-context skills.",14.5,TEXT,40,23)[0]+
        chip(x0+2*(cw+gap)+28,cy+140,cw-56,"close the theory-practice gap",GREEN,32,13))
    b+=rect(64,486,1152,64,fill=PANEL2,stroke=STROKE,rx=12)
    b+=T(92,524,"This paper keeps BOTH nonlinearities, trains by gradient descent, and covers distribution shift and pruning.",15.5,TEXT,"700")
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","Three firsts for ICL theory")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,64,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,64,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"A training theory for genuinely nonlinear Transformers, a mechanism, and the first analysis of pruning for ICL.",17,TEXT,"600"))
    cards=[
        (ch[1],ACCENT,"1","Train + generalize","First characterization of how to train a Transformer with both nonlinear self-attention and a nonlinear MLP, proving it generalizes in-context and quantifying the data, iterations, and context length required."),
        (ch[2],TEAL,"2","The mechanism","Explains how the ability arises: the attention layer and the MLP layer cooperate to make correct predictions on unseen tasks."),
        (ch[3],GOLD,"3","Pruning theory","First theoretical analysis of magnitude-based pruning for ICL, proving that removing the low-magnitude neurons is essentially harmless."),
    ]
    cw=368; gap=24; x0=64; cy=240; chh=310
    for idx,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+idx*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+52,cy+70,27,fill="none",stroke=col,sw=2.5)+
              T(x+52,cy+80,num,30,col,"800",anchor="middle"))
        yy=cy+140
        for j,ln in enumerate(wrap(ti,24)):
            body+=T(x+28,yy+j*28,ln,19,TEXT,"800")
        yy+=28*len(wrap(ti,24))+12
        body+=para(x+28,yy,tx,14,SEC,40,23)[0]
        b+=anchor(c["aid"],c["kw"],body)
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","One nonlinear layer, tracked through training")
    gx=[64,648]; gy=[152,362]; cw=568; chh=198
    # c1 the model
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(gx[0],gy[0],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[0],gy[0],6,chh,fill=ACCENT,rx=6,sw=0)+
        T(gx[0]+28,gy[0]+38,"The model  ·  minimal but nonlinear",16.5,ACCENT,"800")+
        para(gx[0]+28,gy[0]+68,"One self-attention head with a softmax, followed by a two-layer perceptron with ReLU activation.",14.5,SEC,58,22)[0]+
        chip(gx[0]+28,gy[0]+112,cw-56,"softmax self-attention  (nonlinear)",TEAL,34,13.5)+
        chip(gx[0]+28,gy[0]+154,cw-56,"two-layer ReLU MLP  (nonlinear)",GOLD,34,13.5))
    # c2 training setup + equation
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(gx[1],gy[0],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[1],gy[0],6,chh,fill=TEAL,rx=6,sw=0)+
        T(gx[1]+28,gy[0]+38,"Training  ·  hinge loss over prompts",16.5,TEAL,"800")+
        para(gx[1]+28,gy[0]+68,"Augment each query with a length-l context of example pairs; minimize hinge loss over a small subset of binary tasks.",14,SEC,60,22)[0]+
        rect(gx[1]+28,gy[0]+118,cw-56,58,fill=PANEL2,stroke=STROKE,rx=8)+
        T(gx[1]+cw/2,gy[0]+142,"F = a^T ReLU( W_O sum_i W_V p_i attn(i) )",14,TEXT,"800",anchor="middle",ff=MONO)+
        T(gx[1]+cw/2,gy[0]+164,"attn(i) = softmax( (W_K p_i)^T W_Q p_query )",13,SEC,"700",anchor="middle",ff=MONO))
    # c3 dynamics + shift
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(gx[0],gy[1],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[0],gy[1],6,chh,fill=GOLD,rx=6,sw=0)+
        T(gx[0]+28,gy[1]+38,"Analysis  ·  follow the GD trajectory",16.5,GOLD,"800")+
        para(gx[0]+28,gy[1]+68,"Track gradient descent on the query, key, value and MLP weights, then evaluate in-domain and under a distribution shift.",14,SEC,60,21)[0]+
        chip(gx[0]+28,gy[1]+118,cw-56,"in-domain  ->  same task distribution",ACCENT,32,13)+
        chip(gx[0]+28,gy[1]+156,cw-56,"out-of-domain  ->  patterns = linear combos",TEAL,32,13))
    # c4 alpha, beta
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(gx[1],gy[1],cw,chh,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(gx[1],gy[1],6,chh,fill=GREEN,rx=6,sw=0)+
        T(gx[1]+28,gy[1]+38,"Two quantities drive the guarantees",16.5,GREEN,"800")+
        rect(gx[1]+28,gy[1]+62,258,108,fill=PANEL2,stroke=STROKE,rx=10)+
        T(gx[1]+28+129,gy[1]+104,"alpha",26,ACCENT,"800",anchor="middle",ff=MONO)+
        T(gx[1]+28+129,gy[1]+134,"fraction of context sharing",12.5,SEC,"600",anchor="middle")+
        T(gx[1]+28+129,gy[1]+152,"the query's relevant pattern",12.5,SEC,"600",anchor="middle")+
        rect(gx[1]+302,gy[1]+62,258,108,fill=PANEL2,stroke=STROKE,rx=10)+
        T(gx[1]+302+129,gy[1]+104,"beta",26,TEAL,"800",anchor="middle",ff=MONO)+
        T(gx[1]+302+129,gy[1]+134,"magnitude of the",12.5,SEC,"600",anchor="middle")+
        T(gx[1]+302+129,gy[1]+152,"relevant features",12.5,SEC,"600",anchor="middle"))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","A synthetic setup that matches the theory")
    # c1 top band
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,80,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,80,fill=TEAL,rx=6,sw=0)+
        T(92,186,"Controlled synthetic tasks",15,TEAL,"800",ls="1")+
        para(92,214,"Binary classification tasks built from a fixed pool of patterns, so every quantity in the theorems can be measured directly.",15,TEXT,100,24)[0])
    # c2 left -- patterns
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,252,560,186,fill=PANEL,stroke=STROKE)+
        rect(64,252,6,186,fill=ACCENT,rx=6,sw=0)+
        T(92,290,"The pattern pool",16.5,ACCENT,"800")+
        kpi(92,308,246,"6","in-domain relevant (M1)",ACCENT,34,104)+
        kpi(350,308,246,"24","irrelevant patterns (M2)",GOLD,34,104)+
        T(92,428,"Only the relevant patterns determine an input's label.",13,SEC,"600"))
    # c3 right -- two models
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,252,560,186,fill=PANEL,stroke=STROKE)+
        rect(656,252,6,186,fill=GOLD,rx=6,sw=0)+
        T(684,290,"Two models trained",16.5,GOLD,"800")+
        chip(684,308,504,"One-layer Transformer  ->  the analyzed model",TEAL,32,13.5)+
        chip(684,348,504,"GPT-2  ->  3 layers, 2 heads (real-world)",ACCENT,32,13.5)+
        T(684,414,"The toy model the theory covers, plus a small practical Transformer.",13,SEC,"600"))
    # c4 bottom band -- training / OOD config
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,458,1152,92,fill=PANEL,stroke=STROKE)+
        rect(64,458,6,92,fill=GREEN,rx=6,sw=0)+
        T(92,492,"Configuration  ·  in-domain training and out-of-domain evaluation",16,GREEN,"800")+
        chip(92,506,300,"context length l = 20",GREEN,32,13.5)+
        chip(404,506,300,"relevant fraction alpha = 80%",ACCENT,32,13.5)+
        chip(716,506,420,"OOD: relevant patterns = linear combos",GOLD,32,13.5))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Provable ICL, in-domain and under shift")
    # c1 top band
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,96,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,96,fill=GREEN,rx=6,sw=0)+
        T(92,186,"Main theorem  ·  polynomial cost is enough",16.5,GREEN,"800")+
        para(92,216,"Iterations and a matching number of samples that grow only polynomially in the problem parameters drive the in-domain generalization error down to order epsilon.",14.5,SEC,104,23)[0]+
        rect(880,168,320,64,fill=PANEL2,stroke=STROKE,rx=8)+
        T(1040,196,"T = Theta( M1 alpha^-2/3",13.5,TEXT,"800",anchor="middle",ff=MONO)+
        T(1040,216,"beta^-2/3 sqrt(log M1) / eta )",13.5,TEXT,"800",anchor="middle",ff=MONO))
    # c2 left -- OOD condition
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,266,560,284,fill=PANEL,stroke=STROKE)+
        rect(64,266,6,284,fill=TEAL,rx=6,sw=0)+
        T(92,304,"Generalizes out of domain, too",16.5,TEAL,"800")+
        para(92,336,"The same trained model handles shifted tasks whenever the new relevant patterns are linear combinations of the training patterns.",14.5,SEC,58,23)[0]+
        rect(92,414,504,60,fill=PANEL2,stroke=STROKE,rx=8)+
        T(344,451,"combination strength  S1  >=  1",16,GOLD,"800",anchor="middle",ff=MONO)+
        para(92,506,"A single trained Transformer covers a whole family of shifted tasks, not just the ones it saw.",13.5,SEC,66,20)[0])
    # c3 right -- OOD error chart
    body=(rect(656,266,560,284,fill=PANEL,stroke=STROKE)+
        rect(656,266,6,284,fill=ACCENT,rx=6,sw=0)+
        T(684,304,"Out-of-domain error collapses at S1 = 1",15.5,ACCENT,"800"))
    body+=_ood_chart(700,326,486,196)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],body)
    return svg(b)

def _ood_chart(x,y,w,h):
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=10)
    ox=x+52; oy=y+h-34; pw=w-84; ph=h-64
    # axes
    out+=line(ox,y+14,ox,oy,STROKE,1.5)
    out+=line(ox,oy,ox+pw,oy,STROKE,1.5)
    # y ticks 0, 0.5 (top region ~0.5)
    out+=T(ox-10,oy+4,"0",11,TER,"600",anchor="end")
    out+=T(ox-10,y+20,"err",11,TER,"600",anchor="end")
    # x axis S1: 0 .. 2, marker at 1
    def px(s): return ox+pw*(s/2.0)
    def py(e): return oy-ph*(e/0.5)
    out+=T(px(0),oy+18,"0",11,TER,"600",anchor="middle")
    out+=T(px(1),oy+18,"1",12,GOLD,"800",anchor="middle")
    out+=T(px(2),oy+18,"2",11,TER,"600",anchor="middle")
    out+=T(x+w/2,y+h-4,"combination strength  S1",11.5,SEC,"700",anchor="middle")
    # S1=1 vertical guide
    out+=line(px(1),y+14,px(1),oy,GOLD,1.2,dash="4 4")
    # 0.01 threshold guide
    out+=line(ox,py(0.03),ox+pw,py(0.03),RED,1,dash="3 3")
    out+=T(ox+pw,py(0.03)-4,"< 0.01",11,RED,"800",anchor="end")
    # step curve: plateau ~0.45 for S1<1, sharp drop at 1, near 0 above
    pts=[]
    for i in range(0,101):
        s=2.0*i/100.0
        if s<1.0: e=0.46-0.06*s
        else: e=max(0.004,0.40*(1.0/(1.0+((s-1.0)*16))))
        pts.append((px(s),py(e)))
    out+=poly(pts,stroke=ACCENT,sw=3)
    out+=circle(px(1),py(0.008),5,fill=GREEN,stroke=WHITE,sw=1.5)
    out+=T(px(1)+8,py(0.008)+18,"drops below 1%",11.5,GREEN,"800")
    return out

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Relevant fraction sets the cost")
    # c1 top band
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,58,fill=ACCENT,rx=6,sw=0)+
        T(92,188,"Vary alpha, the fraction of context examples that share the query's relevant pattern.",16,TEXT,"600"))
    # c2 left -- scaling laws
    body=(rect(64,230,560,180,fill=PANEL,stroke=STROKE)+
        rect(64,230,6,180,fill=TEAL,rx=6,sw=0)+
        T(92,268,"As predicted by the theory",16.5,TEAL,"800"))
    body+=chip(92,286,504,"context length  ~  1 / alpha",TEAL,34,14)
    body+=chip(92,328,504,"iterations & samples  ~  alpha^(-2/3)",GOLD,34,14)
    body+=T(92,392,"Richer contexts converge faster and need shorter prompts.",13.5,SEC,"600")
    b+=anchor(ch[1]["aid"],ch[1]["kw"],body)
    # c3 right -- baselines list
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,230,560,180,fill=PANEL,stroke=STROKE)+
        rect(656,230,6,180,fill=GOLD,rx=6,sw=0)+
        T(684,268,"ICL vs. classical baselines",16.5,GOLD,"800")+
        chip(684,286,246,"logistic regression",SEC,32,13)+
        chip(940,286,246,"kernel SVM",SEC,32,13)+
        chip(684,326,246,"linear SVM",SEC,32,13)+
        chip(940,326,246,"nearest neighbor",SEC,32,13)+
        T(684,392,"Compared on sample efficiency across relevant fractions.",13.5,SEC,"600"))
    # c4 bottom band -- sample-efficiency bars at low fraction
    body=(rect(64,430,1152,120,fill=PANEL,stroke=STROKE)+
        rect(64,430,6,120,fill=GREEN,rx=6,sw=0)+
        T(92,462,"Hard low-fraction regime  ·  samples needed for the same accuracy (lower is better)",15.5,TEXT,"800"))
    body+=bar(380,478,540,10,60,GREEN,"In-context learning","most efficient",h=20)
    body+=bar(380,504,540,34,60,SEC,"kernel SVM / LogReg","",h=20)
    body+=bar(380,528,540,58,60,TER,"nearest neighbor","",h=20)
    body+=T(950,492,"ICL removes irrelevant data",12.5,GREEN,"800")
    body+=T(950,512,"and tolerates label noise best",12.5,SEC,"700")
    b+=anchor(ch[3]["aid"],ch[3]["kw"],body)
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The message in four numbers")
    # c1 top band -- cost scaling
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,74,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,74,fill=ACCENT,rx=6,sw=0)+
        T(92,182,"Training cost is governed by the relevant fraction alpha",15.5,ACCENT,"800")+
        chip(92,192,470,"iterations & samples  ~  alpha^(-2/3)",TEAL,30,13.5)+
        chip(576,192,470,"required context length  ~  1 / alpha",GOLD,30,13.5))
    # three KPI cards
    cw=368; gap=24; x0=64; cy=246; chh=200
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(x0,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0,cy,cw,6,fill=TEAL,rx=6,sw=0)+
        T(x0+cw/2,cy+92,"1 / sqrt(M1)",32,TEAL,"800",anchor="middle",ff=MONO)+
        T(x0+cw/2,cy+128,"vanishing fraction of tasks trained on",13,SEC,"600",anchor="middle")+
        T(x0+cw/2,cy+156,"yet it generalizes to all the rest",13,TER,"600",anchor="middle"))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(x0+cw+gap,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0+cw+gap,cy,cw,6,fill=GREEN,rx=6,sw=0)+
        T(x0+cw+gap+cw/2,cy+92,"< 0.01",40,GREEN,"800",anchor="middle")+
        T(x0+cw+gap+cw/2,cy+128,"out-of-domain error",13,SEC,"600",anchor="middle")+
        T(x0+cw+gap+cw/2,cy+156,"once combination strength S1 >= 1",13,TER,"600",anchor="middle"))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(x0+2*(cw+gap),cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0+2*(cw+gap),cy,cw,6,fill=GOLD,rx=6,sw=0)+
        T(x0+2*(cw+gap)+cw/2,cy+92,"~15%",40,GOLD,"800",anchor="middle")+
        T(x0+2*(cw+gap)+cw/2,cy+128,"of output neurons pruned, lossless",13,SEC,"600",anchor="middle")+
        T(x0+2*(cw+gap)+cw/2,cy+156,"small-magnitude neurons only",13,TER,"600",anchor="middle"))
    # bottom band -- pruning contrast
    b+=rect(64,466,1152,84,fill=PANEL2,stroke=STROKE,rx=12)
    b+=T(92,500,"Prune LOW-magnitude neurons  ->  error stays O( epsilon + 1 / sqrt(M1) ), essentially lossless",14.5,GREEN,"700")
    b+=T(92,530,"Prune LARGE-magnitude neurons  ->  error grows at least linearly in the pruning rate",14.5,RED,"700")
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","ICL in a nonlinear Transformer is not a black box")
    cards=[
        (ch[0],ACCENT,"Provably trainable","With both nonlinear attention and a nonlinear MLP, a one-layer model can be provably trained to generalize in-context, in-domain and under distribution shift, with effort set by how much of the context shares the query's relevant pattern."),
        (ch[1],TEAL,"How it works","Attention focuses on the context examples that match the query's relevant pattern, while the ReLU MLP amplifies their labels to make the prediction."),
        (ch[2],GREEN,"Pruning is essentially free","Because only the large-magnitude neurons carry this signal, pruning the small ones barely hurts, giving a principled reason why magnitude-based pruning preserves ICL."),
    ]
    y=168
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,118,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,118,fill=col,rx=6,sw=0)+
              circle(112,y+59,10,fill=col)+
              T(150,y+48,ti,19,TEXT,"800"))
        body+=para(150,y+80,tx,15,SEC,96,23)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=136
    b+=line(64,596,1216,596,STROKE,1)
    b+=T(64,632,"How Do Nonlinear Transformers Learn and Generalize in In-Context Learning?",16,TEXT,"700")
    b+=T(64,660,"ICML 2024  ·  arXiv:2402.15607  ·  Rensselaer Polytechnic Institute · IBM Watson",13.5,SEC,"600")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline_numbers",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
