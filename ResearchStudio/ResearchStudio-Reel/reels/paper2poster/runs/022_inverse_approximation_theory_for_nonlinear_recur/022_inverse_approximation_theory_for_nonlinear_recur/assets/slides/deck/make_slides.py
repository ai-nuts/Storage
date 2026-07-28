#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 022
(Inverse Approximation Theory for Nonlinear Recurrent Neural Networks / ICLR 2024).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue
pass resolves every anchor from PPTX geometry. All-native: zero <image>, zero gradients."""
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

def kpi(x,y,w,num,lbl,col,nsize=34,h=104,ff=SANS,sub=None):
    out=(rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
         T(x+w/2,y+h*0.52,num,nsize,col,"800",anchor="middle",ff=ff)+
         T(x+w/2,y+h*0.80,lbl,13,SEC,"600",anchor="middle"))
    if sub: out+=T(x+w/2,y+h*0.95,sub,11.5,TER,"600",anchor="middle")
    return out

def chip(x,y,w,text,col,h=34,sz=14.5):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+5,text,sz,TEXT,"600"))

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICLR 2024",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"MSR Asia · NUS · IFIM",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"Inverse Approximation Theory for",34,WHITE,"800")
    b+=T(64,192,"Nonlinear Recurrent Neural Networks",34,ACCENT,"800")
    b+=rect(64,216,232,30,fill="#0F2E2B",stroke=TEAL,rx=15,sw=1.5)+T(180,236,"Bernstein-type theorem",16,TEAL,"800",anchor="middle")
    b+=T(312,236,"efficient stable approximation forces exponentially decaying memory",15,SEC,"600")
    b+=T(64,272,"Zhong Li · Shida Wang · Qianxiao Li",15,TER,"500")
    # four concept cards
    cy=300; cw=274; gap=18; cx=64
    data=[
        (ch[0],ACCENT,"RNNs, but memory fades","The workhorse for sequence data, yet RNNs famously struggle the moment the signal carries long-term dependencies."),
        (ch[1],GOLD,"An inverse theorem","A Bernstein-type result: whatever an RNN can stably approximate must have a memory that decays exponentially in time."),
        (ch[2],TEAL,"Not just optimization","So the failure is a fundamental limit of the RNN hypothesis space, extending the curse of memory from linear to nonlinear."),
        (ch[3],GREEN,"A principled cure","A stable reparameterization of the recurrent weights lets RNNs escape the limit, confirmed with numerical experiments."),
    ]
    for i,(c,col,ti,tx) in enumerate(data):
        x=cx+i*(cw+gap)
        body=(rect(x,cy,cw,226,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+28,cy+48,7,fill=col)+
              T(x+46,cy+54,ti,15.5,TEXT,"800"))
        body+=para(x+22,cy+94,tx,13.5,SEC,31,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,570,1216,570,STROKE,1)
    b+=T(64,606,"arXiv:2305.19190",14,ACCENT,"700")
    b+=T(300,606,"Extends the curse of memory to nonlinear RNNs",14,SEC,"600")
    b+=T(1216,606,"Stable reparameterization provably relaxes it",14,TEAL,"700",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Why do RNNs fail on long memory?")
    # c1 top band
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,150,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,188,"RNNs: a basic model for sequential and temporal data",16.5,ACCENT,"800")+
        para(92,218,"Recurrent networks are among the most fundamental architectures for learning from sequences, spanning a wide range of everyday tasks.",15,SEC,98,24)[0]+
        chip(92,262,258,"time series",TEAL,30,12.5)+
        chip(362,262,190,"speech",TEAL,30,12.5)+
        chip(564,262,170,"text",TEAL,30,12.5)+
        chip(746,262,290,"sentiment analysis",GOLD,30,12.5))
    # c2 left -- the observation
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,320,560,230,fill=PANEL,stroke=STROKE)+
        rect(64,320,6,230,fill=GOLD,rx=6,sw=0)+
        T(92,358,"The long-standing observation",17,GOLD,"800")+
        para(92,390,"Empirically, RNNs falter whenever the data has long-term dependencies: distant inputs stop influencing the output.",14.5,SEC,58,23)[0]+
        chip(92,470,504,"short memory  ->  learns fine",GREEN,32,13.5)+
        chip(92,510,504,"long memory  ->  training breaks down",RED,32,13.5))
    # c3 right -- the open question
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,320,560,230,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(656,320,6,230,fill=RED,rx=6,sw=0)+
        T(684,358,"The open question",16.5,RED,"800")+
        para(684,390,"Is this failure only about training dynamics, or a deeper limit on what RNNs can represent at all?",14.5,SEC,58,23)[0]+
        chip(684,452,504,"just exploding / vanishing gradients?",GOLD,32,13.5)+
        chip(684,492,504,"or a structural limitation of the model?",RED,32,13.5))
    # c4 footer -- the resolution
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        T(64,594,"Answering this needs an approximation-theoretic lens, not an optimization one.",14.5,SEC,"600"))
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Two directions of approximation theory")
    # c1 top band -- forward theorems
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,92,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,92,fill=TEAL,rx=6,sw=0)+
        T(92,186,"Forward  ·  Jackson-type theorems",15,TEAL,"800",ls="1")+
        para(92,214,"Assume the target is regular, then bound how well the model can approximate it. They tell you what an architecture CAN do.",15,TEXT,100,24)[0])
    # three cards
    cw=368; gap=24; x0=64; cy=262; chh=200
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(x0,cy,cw,chh,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(x0,cy,cw,6,fill=RED,rx=6,sw=0)+
        T(x0+28,cy+42,"Inverse  ·  Bernstein-type",16.5,RED,"800")+
        para(x0+28,cy+74,"Run the other way: assume the target is efficiently approximable, then deduce what regularity it MUST have.",14.5,SEC,40,23)[0]+
        chip(x0+28,cy+140,cw-56,"approximable  ->  regularity",RED,32,13))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(x0+cw+gap,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0+cw+gap,cy,cw,6,fill=GOLD,rx=6,sw=0)+
        T(x0+cw+gap+28,cy+42,"Exposes hard limits",16.5,GOLD,"800")+
        para(x0+cw+gap+28,cy+74,"Inverse theorems are the tool for fundamental limitations. Prior work proved one for LINEAR RNNs.",14.5,SEC,40,23)[0]+
        chip(x0+cw+gap+28,cy+140,cw-56,"linear: memory decays exp.",GOLD,32,13))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(x0+2*(cw+gap),cy,cw,chh,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(x0+2*(cw+gap),cy,cw,6,fill=GREEN,rx=6,sw=0)+
        T(x0+2*(cw+gap)+28,cy+42,"The pressing question",16.5,GREEN,"800")+
        para(x0+2*(cw+gap)+28,cy+74,"Nonlinearity greatly increases capacity. Would adding it BREAK this curse of memory?",14.5,TEXT,40,23)[0]+
        chip(x0+2*(cw+gap)+28,cy+140,cw-56,"does nonlinearity escape it?",GREEN,32,13))
    b+=rect(64,486,1152,64,fill=PANEL2,stroke=STROKE,rx=12)
    b+=T(92,524,"This paper settles it: the curse of memory survives the jump from linear to nonlinear RNNs.",15.5,TEXT,"700")
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","Two tools, one theorem, one cure")
    cards=[
        (ch[0],ACCENT,"1","Memory function","Extends the memory function from linear to general nonlinear functional sequences, and it can be numerically quantified by querying a trained model."),
        (ch[1],TEAL,"2","Stable approximation","A mild framework requiring the approximant to behave continuously under small parameter perturbations, exactly what gradient descent needs."),
        (ch[2],GOLD,"3","Bernstein theorem","Using both tools, the first Bernstein-type approximation theorem for nonlinear RNNs, believed to be new to the literature."),
        (ch[3],GREEN,"+","Principled cure","On top of the theory, a reparameterization method that overcomes the limitation, confirmed by numerical experiments."),
    ]
    cw=274; gap=18; x0=64; cy=168; chh=380
    for idx,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+idx*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+72,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+82,num,28,col,"800",anchor="middle"))
        yy=cy+142
        for j,ln in enumerate(wrap(ti,20)):
            body+=T(x+26,yy+j*26,ln,18,TEXT,"800");
        yy+=26*len(wrap(ti,20))+14
        body+=para(x+26,yy,tx,13.5,SEC,30,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,592,"Memory + stability are the ingredients; the theorem is the result; the reparameterization is the fix.",14.5,SEC,"600")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","From a memory function to a stable fix")
    gx=[64,648]; gy=[152,362]; cw=568; chh=198
    # c1 memory function
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(gx[0],gy[0],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[0],gy[0],6,chh,fill=ACCENT,rx=6,sw=0)+
        T(gx[0]+28,gy[0]+38,"1 · Memory function for nonlinear maps",16.5,ACCENT,"800")+
        para(gx[0]+28,gy[0]+68,"Over Heaviside step inputs, measure how strongly the output at time t still depends on the input.",14.5,SEC,58,22)[0]+
        rect(gx[0]+28,gy[0]+112,cw-56,58,fill=PANEL2,stroke=STROKE,rx=8)+
        T(gx[0]+cw/2,gy[0]+138,"M(t) = | d y(t) / d (step input) |",14,TEXT,"800",anchor="middle",ff=MONO)+
        T(gx[0]+cw/2,gy[0]+160,"task-independent  ·  numerically queryable",12.5,SEC,"700",anchor="middle"))
    # c2 stability framework
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(gx[1],gy[0],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[1],gy[0],6,chh,fill=TEAL,rx=6,sw=0)+
        T(gx[1]+28,gy[0]+38,"2 · Stable approximation",16.5,TEAL,"800")+
        para(gx[1]+28,gy[0]+68,"Perturbation error at width m: the worst output error when parameters move inside a ball of radius beta.",14,SEC,60,22)[0]+
        rect(gx[1]+28,gy[0]+118,cw-56,58,fill=PANEL2,stroke=STROKE,rx=8)+
        T(gx[1]+cw/2,gy[0]+142,"E_m(beta) = max_{||dW|| <= beta} || y - y_perturbed ||",13,TEXT,"800",anchor="middle",ff=MONO)+
        T(gx[1]+cw/2,gy[0]+164,"stable if E_m stays continuous up to some beta > 0",12.5,SEC,"700",anchor="middle"))
    # c3 central theorem
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(gx[0],gy[1],cw,chh,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(gx[0],gy[1],6,chh,fill=GREEN,rx=6,sw=0)+
        T(gx[0]+28,gy[1]+38,"3 · The central theorem",16.5,GREEN,"800")+
        para(gx[0]+28,gy[1]+68,"If a target is stably approximated by RNNs with controlled weights, its memory MUST decay exponentially.",14,TEXT,60,22)[0]+
        chip(gx[0]+28,gy[1]+118,cw-56,"stability  ->  hidden-state derivatives -> 0",GREEN,32,13)+
        chip(gx[0]+28,gy[1]+156,cw-56,"Hartman-Grobman bounds the eigenvalues",TEAL,32,13))
    # c4 reparameterization
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(gx[1],gy[1],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[1],gy[1],6,chh,fill=GOLD,rx=6,sw=0)+
        T(gx[1]+28,gy[1]+38,"4 · Stable reparameterization",16.5,GOLD,"800")+
        para(gx[1]+28,gy[1]+68,"Replace the recurrent weight with a map that always lands in stable, negative-real-part matrices.",14,SEC,60,22)[0]+
        chip(gx[1]+28,gy[1]+118,cw-56,"W  =  f(theta),   Re(eig) < 0  always",GOLD,32,13)+
        chip(gx[1]+28,gy[1]+156,cw-56,"exponential / softplus maps stay stable",TEAL,32,13))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Synthetic targets and two real tasks")
    # c1 top band
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,80,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,80,fill=TEAL,rx=6,sw=0)+
        T(92,186,"Experiments span synthetic and real data",15,TEAL,"800",ls="1")+
        para(92,214,"Controlled synthetic targets probe the theory directly; real tasks test memory and the optimization benefit of the fix.",15,TEXT,100,24)[0])
    # c2 left -- synthetic targets
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,252,560,186,fill=PANEL,stroke=STROKE)+
        rect(64,252,6,186,fill=ACCENT,rx=6,sw=0)+
        T(92,290,"Synthetic functional targets",16.5,ACCENT,"800")+
        chip(92,308,504,"linear & nonlinear targets",ACCENT,32,13.5)+
        chip(92,348,246,"exp. decay memory",GREEN,32,12.5)+
        chip(350,348,246,"poly. decay memory",RED,32,12.5)+
        T(92,424,"Sweep the hidden dimension m from about 2 up to 64.",13,SEC,"600"))
    # c3 right -- teacher models
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,252,560,186,fill=PANEL,stroke=STROKE)+
        rect(656,252,6,186,fill=GOLD,rx=6,sw=0)+
        T(684,290,"Randomly initialized teachers",16.5,GOLD,"800")+
        kpi(684,308,246,"256",  "teacher hidden dim",GOLD,34,104)+
        kpi(942,308,246,"student","RNN approximates it",ACCENT,22,104)+
        T(684,428,"Filter teachers by the stability test.",13,SEC,"600"))
    # c4 bottom band -- real data
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,458,1152,92,fill=PANEL,stroke=STROKE)+
        rect(64,458,6,92,fill=GREEN,rx=6,sw=0)+
        T(92,492,"Real data  ·  query memory and test the reparameterization",16,GREEN,"800")+
        chip(92,506,470,"LSTM memory on IMDB sentiment",TEAL,32,13.5)+
        chip(576,506,470,"nonlinear RNN on MNIST classification",ACCENT,32,13.5))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Stable approximation forces exponential memory")
    # c1 top band -- the inverse statement
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,96,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,96,fill=GREEN,rx=6,sw=0)+
        T(92,186,"The headline  ·  a clean inverse statement",16.5,GREEN,"800")+
        para(92,216,"If a nonlinear RNN can stably approximate a target sequence relationship, then that target's memory must decay exponentially.",14.5,SEC,104,23)[0]+
        rect(872,168,328,64,fill=PANEL2,stroke=STROKE,rx=8)+
        T(1036,196,"stably approximable",13.5,TEXT,"800",anchor="middle",ff=MONO)+
        T(1036,216,"=>  memory ~ exp(-t)",13.5,GREEN,"800",anchor="middle",ff=MONO))
    # c2 left -- intrinsic limit
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,266,560,284,fill=PANEL,stroke=STROKE)+
        rect(64,266,6,284,fill=TEAL,rx=6,sw=0)+
        T(92,304,"An intrinsic limit, not a training artifact",15.5,TEAL,"800")+
        para(92,336,"This extends the linear curse of memory to the nonlinear regime, so the long-term-dependency failure lives in the RNN hypothesis space itself.",14.5,SEC,58,23)[0]+
        chip(92,440,504,"teacher filter: only survivors decay exp.",GREEN,34,13.5)+
        para(92,500,"Keeping only teachers that are both approximable AND stable leaves exactly the exponential-memory ones.",13.5,SEC,66,20)[0])
    # c3 right -- perturbation-error chart
    body=(rect(656,266,560,284,fill=PANEL,stroke=STROKE)+
        rect(656,266,6,284,fill=ACCENT,rx=6,sw=0)+
        T(684,304,"Poly-memory: curves intersect further left",15.5,ACCENT,"800"))
    body+=_pert_chart(700,326,486,196)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],body)
    # c4 lives on the teacher-filter chip inside c2 region? give c4 its own tiny footer band
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        T(656,590,"Slowly-decaying targets take ~1000 epochs to fit vs ~10 for exponential ones.",13.5,SEC,"600"))
    return svg(b)

def _pert_chart(x,y,w,h):
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=10)
    ox=x+46; oy=y+h-38; pw=w-72; ph=h-64
    out+=line(ox,y+14,ox,oy,STROKE,1.5)
    out+=line(ox,oy,ox+pw,oy,STROKE,1.5)
    out+=T(ox-10,y+22,"E_m",11,TER,"600",anchor="end")
    out+=T(ox-10,oy+4,"0",11,TER,"600",anchor="end")
    def px(bt): return ox+pw*bt            # beta 0..1
    def py(e):  return oy-ph*e             # error 0..1
    out+=T(px(0),oy+18,"0",11,TER,"600",anchor="middle")
    out+=T(px(1.0),oy+18,"beta",11.5,SEC,"700",anchor="middle")
    out+=T(x+w/2,y+h-4,"perturbation radius  beta",11.5,SEC,"700",anchor="middle")
    # three curves for increasing m: as m grows the curve rises earlier (crossing drifts left)
    curves=[(0.62,ACCENT,"m=8"),(0.40,TEAL,"m=32"),(0.22,GOLD,"m=128")]
    for x0c,col,lbl in curves:
        pts=[]
        for i in range(0,101):
            bt=i/100.0
            # low-then-sharp-rise sigmoid centered at x0c
            e=0.08+0.82/(1.0+math.exp(-(bt-x0c)*14))
            pts.append((px(bt),py(e)))
        out+=poly(pts,stroke=col,sw=2.6)
        out+=T(px(x0c),py(0.5)-8,lbl,11,col,"800",anchor="middle")
    # markers for crossing drift
    for bx,col in [(0.22,GOLD),(0.40,TEAL),(0.62,ACCENT)]:
        out+=line(px(bx),y+14,px(bx),oy,col,1,dash="3 3")
    out+=T(ox+pw,y+26,"no stable beta > 0 survives",11,RED,"800",anchor="end")
    return out

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Only the parameterization changes")
    # c1 top band
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,58,fill=ACCENT,rx=6,sw=0)+
        T(92,188,"Vary ONLY how the recurrent weight is parameterized; hold the initialization fixed.",16,TEXT,"600"))
    # c2 left -- MNIST reparam speedup
    body=(rect(64,230,560,180,fill=PANEL,stroke=STROKE)+
        rect(64,230,6,180,fill=TEAL,rx=6,sw=0)+
        T(92,268,"MNIST: stable maps train faster",16.5,TEAL,"800"))
    body+=chip(92,286,504,"softplus / exponential / inverse  ->  stable",GREEN,34,13.5)
    body+=chip(92,328,504,"direct (weight used as-is)  ->  unstable",RED,34,13.5)
    body+=T(92,392,"All three stable maps beat the direct baseline on accuracy.",13.5,SEC,"600")
    b+=anchor(ch[1]["aid"],ch[1]["kw"],body)
    # c3 right -- capacity unchanged
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,230,560,180,fill=PANEL,stroke=STROKE)+
        rect(656,230,6,180,fill=GOLD,rx=6,sw=0)+
        T(684,268,"Capacity is unchanged",16.5,GOLD,"800")+
        para(684,300,"Reparameterization does not alter the model's inherent capacity, so final accuracy across stable variants is comparable.",14.5,SEC,58,23)[0]+
        chip(684,368,504,"isolates an OPTIMIZATION & stability gain",GOLD,32,13))
    # c4 bottom band -- synthetic restoration
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,430,1152,120,fill=PANEL,stroke=STROKE)+
        rect(64,430,6,120,fill=GREEN,rx=6,sw=0)+
        T(92,462,"Synthetic  ·  reparameterization restores the continuous limiting-error curve",15.5,TEXT,"800")+
        chip(92,486,540,"linear RNN + poly-decay target  ->  unstable curve",RED,34,13.5)+
        chip(648,486,540,"+ exponential / softplus map  ->  stability recovered",GREEN,34,13.5)+
        T(92,540,"Confirms that the stability the theory predicts is exactly what the fix brings back.",13,SEC,"600"))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The message in four numbers")
    # c1 top band
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,74,fill=PANEL,stroke=STROKE)+
        rect(64,152,6,74,fill=ACCENT,rx=6,sw=0)+
        T(92,182,"MNIST, 10 epochs, averaged over 3 runs  ·  stable vs direct parameterization",15.5,ACCENT,"800")+
        chip(92,192,470,"stable maps  ->  faster + higher accuracy",GREEN,30,13.5)+
        chip(576,192,470,"direct map  ->  unstable baseline",RED,30,13.5))
    # three KPI cards
    cw=368; gap=24; x0=64; cy=246; chh=200
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(x0,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0,cy,cw,6,fill=GREEN,rx=6,sw=0)+
        T(x0+cw/2,cy+96,"71.36%",42,GREEN,"800",anchor="middle")+
        T(x0+cw/2,cy+132,"softplus stable reparameterization",13,SEC,"600",anchor="middle")+
        T(x0+cw/2,cy+160,"best MNIST test accuracy",13,TER,"600",anchor="middle"))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(x0+cw+gap,cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0+cw+gap,cy,cw,6,fill=RED,rx=6,sw=0)+
        T(x0+cw+gap+cw/2,cy+96,"68.47%",42,RED,"800",anchor="middle")+
        T(x0+cw+gap+cw/2,cy+132,"direct, unstable baseline",13,SEC,"600",anchor="middle")+
        T(x0+cw+gap+cw/2,cy+160,"exp. & inverse maps also > 70%",13,TER,"600",anchor="middle"))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(x0+2*(cw+gap),cy,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0+2*(cw+gap),cy,cw,6,fill=GOLD,rx=6,sw=0)+
        T(x0+2*(cw+gap)+cw/2,cy+96,"10 vs 1000",34,GOLD,"800",anchor="middle")+
        T(x0+2*(cw+gap)+cw/2,cy+132,"epochs to fit exp. vs poly. memory",13,SEC,"600",anchor="middle")+
        T(x0+2*(cw+gap)+cw/2,cy+160,"poly. targets still fail the stability test",13,TER,"600",anchor="middle"))
    # bottom band -- contrast
    b+=rect(64,466,1152,84,fill=PANEL2,stroke=STROKE,rx=12)
    b+=T(92,500,"Stable reparameterization  ->  nearly +3 points over the unstable baseline, and it converges far sooner",14.5,GREEN,"700")
    b+=T(92,530,"Teacher-filtering experiment uses hidden dimension 256; only exponential-memory teachers survive",14.5,SEC,"700")
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","The curse of memory, and its cure")
    cards=[
        (ch[0],ACCENT,"A limit baked into the architecture","No matter how they are trained, plain nonlinear RNNs can only stably approximate sequence relationships whose memory fades exponentially, so the long-term-dependency struggle is intrinsic, not just an optimizer issue."),
        (ch[1],TEAL,"But the analysis points to a cure","The same stability argument that exposes the limit also shows how to relax it."),
        (ch[2],GREEN,"Reparameterize the recurrent weights","With a stable map like exponential or softplus, the network keeps eigenvalues near the edge of stability, provably relaxing the curse and, on MNIST, training faster and generalizing better."),
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
    b+=T(64,632,"Inverse Approximation Theory for Nonlinear Recurrent Neural Networks",16,TEXT,"700")
    b+=T(64,660,"ICLR 2024  ·  arXiv:2305.19190  ·  Microsoft Research Asia · NUS · IFIM",13.5,SEC,"600")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline_numbers",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
