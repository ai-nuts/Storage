#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 086 (PIXIU / financial LLM benchmark).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue
pass resolves every anchor from PPTX geometry. Zero <image>, zero gradients, ASCII
mono equations only."""
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

def kpi(x,y,num,lbl,col,w=168,h=100):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+56,num,30,col,"800",anchor="middle")+
            T(x+w/2,y+82,lbl,12.5,SEC,"600",anchor="middle"))

def chip(x,y,text,col,w=512,h=34):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+6,text,14.5,TEXT,"600"))

def eqbox(x,y,w,expr,size=17,h=44):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            T(x+w/2,y+h/2+6,expr,size,TEXT,"800",anchor="middle",ff=MONO))

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"NeurIPS 2023",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Wuhan U.  ·  Sun Yat-Sen U.  ·  U. Florida  ·  ChanceFocus",13.5,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"PIXIU: A Comprehensive Benchmark, Instruction",34,WHITE,"800")
    b+=T(64,192,"Dataset & Large Language Model for Finance",34,ACCENT,"800")
    b+=T(64,232,"The first fully open triad for financial AI: dataset, model, and benchmark",19,TEAL,"700")
    b+=T(64,270,"Qianqian Xie · Weiguang Han · Xiao Zhang · Yanzhao Lai · Min Peng · A. Lopez-Lira · Jimin Huang",14,SEC,"500")
    # four concept cards (2x2) = anchors
    cw=560; chh=118; gap=32; x0=64; x1=x0+cw+gap; cy0=304; cy1=cy0+chh+22
    data=[
        (ch[0],ACCENT,x0,cy0,"PIXIU  ·  open-source financial AI","A comprehensive open-source framework for financial artificial intelligence, presented at NeurIPS 2023."),
        (ch[1],GOLD,x1,cy0,"Three gaps before PIXIU","No openly released financial LLM, no financial instruction-tuning data, and no holistic evaluation benchmark."),
        (ch[2],TEAL,x0,cy1,"FIT · FinMA · FLARE","A 136K-sample instruction dataset, the first open instruction-following financial LLM, and a unified benchmark."),
        (ch[3],GREEN,x1,cy1,"Built in the open","Together they let the community build, compare, and advance financial LLMs entirely in the open."),
    ]
    for c,col,x,cy,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,6,chh,fill=col,rx=6,sw=0)+
              T(x+28,cy+36,ti,18,TEXT,"800"))
        body+=para(x+28,cy+62,tx,14,SEC,68,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,616,1216,616,STROKE,1)
    b+=T(64,650,"arXiv:2306.05443",14,ACCENT,"700")
    b+=T(300,650,"github.com/chancefocus/PIXIU  —  open data, open model, open benchmark.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","No open resources for financial LLMs")
    # c1 domain-specific need (left tall card)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"Finance needs domain models",18,TEXT,"800")+
        para(92,240,"FinTech has advanced fast with NLP, but the highly technical nature of financial text demands domain-specific models.",15,SEC,42,24)[0]+
        rect(92,352,320,150,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,384,"General LLM",13,TER,"700")+
        T(112,414,"generic text",13,SEC,"500")+
        T(252,384,"->",22,GOLD,"800")+
        T(300,384,"Financial LLM",13,ACCENT,"700")+
        T(300,414,"reports · filings · tickers",12.5,SEC,"500")+
        T(112,470,"Jargon, numbers, and time-series break generic models.",12.5,TEAL,"700"))
    # right: three failing resources
    fx=500; fw=716
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,110,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,110,fill=GOLD,rx=6,sw=0)+
        T(fx+28,196,"Existing financial models are small",16,GOLD,"800")+
        para(fx+28,226,"finBERT and FLANG stay below one billion parameters, which limits their generalization to new financial tasks.",14.5,SEC,74,22)[0])
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,282,fw,110,fill=PANEL,stroke=STROKE)+
        rect(fx,282,6,110,fill=RED,rx=6,sw=0)+
        T(fx+28,320,"BloombergGPT is a closed 50B model",16,RED,"800")+
        para(fx+28,350,"The one large financial model releases neither weights nor training data, and it is not instruction-following.",14.5,SEC,74,22)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,406,fw,144,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(fx,406,6,144,fill=RED,rx=6,sw=0)+
        T(fx+28,446,"The core gap",16,RED,"800")+
        para(fx+28,476,"No open financial instruction datasets and no standardized benchmark for comprehensively assessing financial LLMs.",14.5,TEXT,74,22)[0]+
        T(fx+28,540,"no open data   ·   no open model   ·   no open benchmark",14.5,RED,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Two gaps hold financial AI back")
    # c1 instruction-tuning gap (left)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=TEAL,rx=6,sw=0)+
        T(92,198,"Gap 1  ·  no financial instructions",18,TEAL,"800")+
        para(92,230,"Instruction tuning is essential for a model's zero-shot ability on downstream tasks, yet no financial instruction data exists to enable it.",14.5,SEC,50,22)[0]+
        rect(92,338,504,86,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,368,"instruction tuning",13.5,ACCENT,"800")+
        T(112,394,"stronger zero-shot on new tasks",13,SEC,"500")+
        T(560,368,"MISSING",14,RED,"800",anchor="end")+
        rect(92,440,504,90,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,470,"The prize",13.5,TEAL,"800")+
        para(112,494,"Open instruction data would unlock financial LLMs for everyone.",13.5,SEC,60,20)[0])
    # right: benchmark gap + PIXIU answer
    rx=648; rw=568
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(rx,158,rw,116,fill=PANEL,stroke=STROKE)+
        rect(rx,158,6,116,fill=GOLD,rx=6,sw=0)+
        T(rx+28,196,"Gap 2  ·  NLP-only benchmarks",16,GOLD,"800")+
        para(rx+28,226,"Existing financial benchmarks such as FLUE cover only natural language processing tasks.",14.5,SEC,60,22)[0])
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,286,rw,120,fill=PANEL,stroke=STROKE)+
        rect(rx,286,6,120,fill=RED,rx=6,sw=0)+
        T(rx+28,324,"They ignore financial prediction",16,RED,"800")+
        para(rx+28,354,"Tasks like stock movement prediction need both text and time-series data, and are far closer to real-world finance.",14.5,SEC,60,22)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,418,rw,132,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(rx,418,6,132,fill=GREEN,rx=6,sw=0)+
        T(rx+28,456,"PIXIU closes both gaps",16,GREEN,"800")+
        para(rx+28,486,"Open resources, multi-task coverage, multi-modal data, and greater task diversity.",14.5,TEXT,60,22)[0]+
        T(rx+28,540,"open  ·  multi-task  ·  multi-modal",14,GREEN,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","Four contributions")
    cards=[
        (ch[0],ACCENT,"1","FIT dataset","The first multi-task, multi-modal financial instruction dataset: five tasks, nine datasets, 136K samples."),
        (ch[1],TEAL,"2","FLARE benchmark","The first evaluation benchmark spanning both financial language understanding and financial prediction."),
        (ch[2],GOLD,"3","FinMA model","The first openly released instruction-following financial LLM, reaching SOTA on three NLP tasks and one prediction task."),
        (ch[3],GREEN,"4","Benchmarking study","Benchmarks FinMA against existing LLMs, revealing both its superiority and its key limitations for finance."),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    for i,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+66,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+76,num,28,col,"800",anchor="middle"))
        yy=cy+134
        for j,ln in enumerate(wrap(ti,17)):
            body+=T(x+24,yy+j*26,ln,17.5,TEXT,"800")
        yy+=26*len(wrap(ti,17))+10
        body+=para(x+24,yy,tx,14,SEC,30,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,584,"One dataset, one benchmark, one open model  —  and the study that ties them together.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Gather, instruction-tune, evaluate")
    # LEFT: stage 1 (gather data) + stage 2 (instructions) -> FIT
    lx=64; lw=568
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,200,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,200,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,196,"Stage 1  ·  gather open data",16.5,ACCENT,"800")+
        para(lx+28,226,"Collect open-released data across five financial tasks.",14,SEC,58,21)[0]+
        chip(lx+28,254,"Sentiment  ·  Headline  ·  NER",ACCENT,w=lw-56,h=30)+
        chip(lx+28,292,"Question answering  ·  Stock movement prediction",ACCENT,w=lw-56,h=30)+
        T(lx+28,340,"Five tasks span text, tables, and time series.",13.5,TEAL,"700"))
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(lx,374,lw,176,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(lx,374,6,176,fill=TEAL,rx=6,sw=0)+
        T(lx+28,412,"Stage 1b  ·  build FIT instructions",16,TEAL,"800")+
        para(lx+28,442,"Domain experts write diverse task-specific instructions, assembled with the data samples to form the FIT dataset.",14,SEC,58,21)[0]+
        T(lx+28,514,"multi-modal:  text  +  tables  +  historical prices",14,TEXT,"800",ff=MONO))
    # RIGHT: stage 2 (fine-tune) + stage 3 (evaluate)
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,200,fill=PANEL,stroke=STROKE)+
        rect(rxx,158,6,200,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,196,"Stage 2  ·  fine-tune LLaMA",16.5,GOLD,"800")+
        para(rxx+28,226,"LLaMA checkpoints at 7B and 30B are fine-tuned on FIT with multi-task instruction tuning.",14,SEC,56,21)[0]+
        T(rxx+28,300,"LLaMA 7B / 30B",15,SEC,"700")+
        T(rxx+250,300,"+ FIT  ->",18,GOLD,"800")+
        T(rxx+360,300,"FinMA",18,GOLD,"800")+
        T(rxx+28,336,"The FinMA model family.",13.5,TEAL,"700"))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,374,rw,176,fill=PANEL,stroke=STROKE)+
        rect(rxx,374,6,176,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,412,"Stage 3  ·  evaluate on FLARE",16,GREEN,"800")+
        para(rxx+28,442,"FinMA and other LLMs are scored on FLARE, which unifies financial language and prediction tasks.",14,SEC,56,21)[0]+
        T(rxx+28,514,"4 NLP tasks / 6 datasets   +   1 prediction / 3 datasets",13.5,TEXT,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 6: DATASET / BENCHMARK ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","FIT to train, FLARE to evaluate")
    # c1 FIT strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"FIT  ·  instruction tuning",18,ACCENT,"800")+
        kpi(92,214,"136K","samples",ACCENT,w=150,h=76)+
        kpi(258,214,"5","tasks",ACCENT,w=140,h=76)+
        kpi(416,214,"9","datasets",ACCENT,w=140,h=76))
    # c2 FLARE strip
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(656,158,560,150,fill=PANEL,stroke=STROKE)+
        rect(656,158,6,150,fill=TEAL,rx=6,sw=0)+
        T(684,196,"FLARE  ·  evaluation",18,TEAL,"800")+
        kpi(684,214,"4 NLP","6 datasets",TEAL,w=176,h=76)+
        kpi(876,214,"1 pred.","3 datasets",GOLD,w=160,h=76)+
        kpi(1052,214,"5","task types",TEAL,w=140,h=76))
    # c3 task -> dataset mapping
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(64,326,1152,150,fill=PANEL,stroke=STROKE)+
        rect(64,326,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,360,"Tasks and their datasets",16,TEXT,"800")+
        chip(92,378,"Sentiment: Financial Phrase Bank · FiQA-SA",ACCENT,w=540,h=30)+
        chip(648,378,"Headline classification: Headline",GOLD,w=540,h=30)+
        chip(92,416,"NER: financial NER   ·   QA: FinQA · ConvFinQA",TEAL,w=540,h=30)+
        chip(648,416,"Stock movement: BigData22 · ACL18 · CIKM18",GREEN,w=540,h=30))
    # c4 metrics
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,494,1152,58,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,494,6,58,fill=GOLD,rx=6,sw=0)+
        T(92,530,"Each task uses its standard metric:  weighted F1  ·  entity-level F1  ·  exact-match accuracy  ·  Matthews correlation (prediction).",14.5,TEXT,"600"))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","FinMA beats far larger models")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,50,fill=PANEL,stroke=STROKE)+
        rect(64,150,6,50,fill=GREEN,rx=6,sw=0)+
        T(92,182,"On FLARE, fine-tuned FinMA significantly outperforms other LLMs on most financial NLP tasks.",16.5,TEXT,"700"))
    # c2 FPB sentiment bars (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,214,560,264,fill=PANEL,stroke=STROKE)+
        rect(64,214,6,264,fill=TEAL,rx=6,sw=0)+
        T(92,250,"Financial Phrase Bank  ·  weighted F1",16,TEAL,"800")+
        bar(320,278,230,0.51,0.90,RED,"BloombergGPT","0.51",h=30)+
        bar(320,326,230,0.78,0.90,GOLD,"GPT-4","0.78",h=30)+
        bar(320,374,230,0.88,0.90,GREEN,"FinMA-30B","0.88",h=30)+
        rect(92,418,504,44,fill="#0F2E2B",stroke=TEAL,rx=10,sw=1.5)+
        T(112,446,"FinMA-30B: +10% F1 vs GPT-4, +37% vs BloombergGPT",14,TEAL,"800"))
    # c3 two honest limitations (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,214,560,128,fill=PANEL,stroke=STROKE)+
        rect(656,214,6,128,fill=GOLD,rx=6,sw=0)+
        T(684,252,"Limitation  ·  quantitative QA",16,GOLD,"800")+
        para(684,282,"FinMA underperforms on question answering that demands quantitative reasoning, inherited from LLaMA's weak math ability.",14,SEC,58,22)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,358,560,120,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(656,358,6,120,fill=RED,rx=6,sw=0)+
        T(684,396,"Open challenge  ·  stock prediction",16,RED,"800")+
        para(684,426,"Across all models, stock movement prediction stays hard, leaving clear room for future work.",14,TEXT,58,22)[0])
    b+=T(64,506,"Tailoring an open LLM to finance via instruction tuning pays off on language tasks.",14.5,SEC,"600")
    b+=T(64,540,"Higher is better on the Financial Phrase Bank sentiment benchmark; values are weighted F1.",13,TER,"600")
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Data diversity over raw scale")
    # c1 setup (left top)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,96,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,96,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Comparing model variants",16.5,ACCENT,"800")+
        para(92,226,"How much does parameter count actually help across financial tasks?",14.5,SEC,54,22)[0])
    # c2 30B vs 7B bars (left bottom)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,270,560,280,fill=PANEL,stroke=STROKE)+
        rect(64,270,6,280,fill=TEAL,rx=6,sw=0)+
        T(92,306,"30B vs 7B  ·  most NLP & stock tasks",15.5,TEXT,"800")+
        bar(300,336,240,1.0,1.05,ACCENT,"FinMA-7B","similar",h=30)+
        bar(300,384,240,1.0,1.05,TEAL,"FinMA-30B","similar",h=30)+
        rect(92,430,504,100,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,460,"Scaling barely moves the needle",13.5,GOLD,"800")+
        para(112,484,"Instruction-data quality and diversity matter more than sheer parameter count.",13.5,SEC,60,20)[0])
    # c3 where scale helps (right top)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,180,fill=PANEL,stroke=STROKE)+
        rect(656,158,6,180,fill=GOLD,rx=6,sw=0)+
        T(684,196,"Where scale does help",16.5,GOLD,"800")+
        para(684,226,"On complex quantitative QA like ConvFinQA, the larger model improves, mirroring LLaMA's better math at scale.",14.5,SEC,56,22)[0]+
        rect(684,290,504,34,fill=PANEL2,stroke=STROKE,rx=8)+
        T(936,312,"ConvFinQA:  30B > 7B   (still trails GPT-4)",14.5,GOLD,"800",anchor="middle",ff=MONO))
    # c4 best-on-ACL18 (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,354,560,196,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,354,6,196,fill=GREEN,rx=6,sw=0)+
        T(684,392,"Task-specific tuning wins",16.5,GREEN,"800")+
        para(684,424,"FinMA-7B-full, fine-tuned on both NLP and prediction tasks, is the best of all models on ACL18 stock prediction.",14.5,TEXT,56,22)[0]+
        chip(684,494,"Best on ACL18: FinMA-7B-full",GREEN,w=504,h=34))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The results in one place")
    cw=560; gap=32; x0=64; x1=x0+cw+gap; chh=184; ry0=168; ry1=ry0+chh+18
    # c1 FIT (top-left)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(x0,ry0,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0,ry0,6,chh,fill=ACCENT,rx=6,sw=0)+
        T(x0+28,ry0+40,"FIT  ·  instruction dataset",16.5,ACCENT,"800")+
        kpi(x0+28,ry0+60,"136K","samples",ACCENT,w=160,h=88)+
        kpi(x0+204,ry0+60,"5","tasks",ACCENT,w=150,h=88)+
        kpi(x0+370,ry0+60,"9","datasets",ACCENT,w=150,h=88))
    # c2 FinMA / LLaMA base (top-right)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(x1,ry0,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x1,ry0,6,chh,fill=TEAL,rx=6,sw=0)+
        T(x1+28,ry0+40,"FinMA  ·  built on open LLaMA",16.5,TEAL,"800")+
        kpi(x1+28,ry0+60,"7B","FinMA-7B",TEAL,w=250,h=88)+
        kpi(x1+306,ry0+60,"30B","FinMA-30B",TEAL,w=250,h=88))
    # c3 FPB headline lift (bottom-left)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(x0,ry1,cw,chh,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(x0,ry1,6,chh,fill=GREEN,rx=6,sw=0)+
        T(x0+28,ry1+40,"Financial Phrase Bank  ·  weighted F1",15.5,GREEN,"800")+
        kpi(x0+28,ry1+60,"+10%","F1 vs GPT-4",GREEN,w=250,h=88)+
        kpi(x0+306,ry1+60,"+37%","F1 vs Bloomberg",GOLD,w=250,h=88)+
        T(x0+28,ry1+172,"FinMA-30B reaches about 0.88 weighted F1.",13,SEC,"600"))
    # c4 SOTA / fully open (bottom-right)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(x1,ry1,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x1,ry1,6,chh,fill=GOLD,rx=6,sw=0)+
        T(x1+28,ry1+40,"State of the art  ·  fully open",16.5,GOLD,"800")+
        kpi(x1+28,ry1+60,"3","SOTA NLP tasks",GOLD,w=250,h=88)+
        kpi(x1+306,ry1+60,"1","SOTA prediction",GOLD,w=250,h=88)+
        T(x1+28,ry1+172,"All achieved while being fully open-sourced.",13,SEC,"600"))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Open resources move finance forward")
    cards=[
        (ch[0],ACCENT,"A simple takeaway","PIXIU gives the financial AI community open resources it never had before."),
        (ch[1],TEAL,"The first fully open triad","An instruction-following financial LLM (FinMA), a large multi-task instruction dataset (FIT), and a holistic benchmark (FLARE)."),
        (ch[2],GREEN,"Small, open, and competitive","Careful domain instruction tuning lets a relatively small open model beat far larger general systems on financial language, while quantitative reasoning and stock prediction remain open challenges."),
    ]
    y=176
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,116,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,116,fill=col,rx=6,sw=0)+
              circle(112,y+58,10,fill=col)+
              T(150,y+46,ti,19,TEXT,"800"))
        body+=para(150,y+78,tx,15.5,SEC,88,24)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=132
    b+=line(64,596,1216,596,STROKE,1)
    b+=T(64,632,"PIXIU: A Comprehensive Benchmark, Instruction Dataset & Large Language Model for Finance",15.5,TEXT,"700")
    b+=T(64,660,"NeurIPS 2023  ·  Xie et al.  ·  arXiv:2306.05443  ·  github.com/chancefocus/PIXIU",13.5,SEC,"600")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
