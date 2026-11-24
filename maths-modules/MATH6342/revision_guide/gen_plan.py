import sys
# (minutes, label, title, do, gate)
CH = {
1: ("Chapter 1: Describing linear systems", "ch1", [
 (4,"ss:1-1",r"Linear operators and the five building blocks",
  r"Read the definition box. Say what each block does to a signal $u$. Do the exam tip: show $Lf=tf''+3\int_0^tf$ is linear.",
  r"say what a tap, summing junction, integrator, differentiator and amplifier do, and check linearity of a given $L$."),
 (5,"ss:1-2",r"Block diagrams: open loop and feedback",
  r"Cover and redo Black's amplifier ($y=u+\theta y\Rightarrow y=u/(1-\theta)$) and the cyclist ($v=-\frac km\int v+\frac1m\int u$).",
  r"tell open loop from feedback, and write the equation at a summing junction."),
 (10,"ss:1-3",r"How to turn an equation into a block diagram",
  r"Learn the 5-step method box. Cover and redo A1.1(i), A1.1(ii) (integrate twice, solve for $y$, nest the integrals) and A1.2.",
  r"turn $y''+4y=u'$ (or similar) into a diagram with \emph{no differentiators}, closed book."),
 (6,"ss:1-4",r"Reduction of order and the matrix form",
  r"Learn the 4-step method. Cover and redo A1.3 ($m\ddot x+kx=u$) and the damped oscillator.",
  r"write $A,B,C,D$ for any $n$-th order constant-coefficient ODE (remember to make it monic first)."),
 (5,"ss:1-5",r"The companion matrix",
  r"Learn the sign/order rule (last row $-a_0,\dots,-a_{n-1}$). Redo A2.2. Read the induction proof once.",
  r"write a matrix with characteristic polynomial $s^3-2s^2+s+7$ in 30 seconds."),
 (6,"ss:1-6",r"Exam-style questions for Chapter 1",
  r"Do Q1.1 and Q1.2 closed book, then mark against the solutions. Q1.3 if time.",
  r"get Q1.1 and Q1.2 fully right."),
]),
2: ("Chapter 2: Matrix theory", "ch2", [
 (4,"ss:2-1",r"Determinants, cofactors, characteristic polynomial",
  r"Read the box. Note: $\chi_A(s)=\det(sI-A)$, adjugate $=$ \emph{transpose} of cofactors, $2\times2$: $s^2-\tr A\,s+\det A$.",
  r"write $\chi_A$ for a $2\times2$ matrix instantly and explain what the adjugate is."),
 (7,"ss:2-2",r"Computing the resolvent $(sI-A)^{-1}$",
  r"Learn the 5-step method. Cover and redo A1.4 (upper triangular, so many cofactors are 0).",
  r"compute $(sI-A)^{-1}$ for a $2\times2$ matrix in under 3 minutes and check it."),
 (3,"ss:2-3",r"Norms and Cauchy--Schwarz",
  r"Read the results box and the Cauchy--Schwarz proof once (discriminant $\le0$ idea).",
  r"state $\|AB\|\le\|A\|\|B\|$ and the one-line idea of the Cauchy--Schwarz proof."),
 (4,"ss:2-4",r"Rank and the matrices $Q$, $R$ (AE2)",
  r"Redo A2.3(i)--(ii). Read the ``why rank matters'' box (rank drop $\leftrightarrow$ pole cancels).",
  r"prove $Q^\top=R$ and find $R$ when $C^\top$ is an eigenvector of $A^\top$."),
 (6,"ss:2-5",r"Eigenvalues, diagonalisation, Cayley--Hamilton",
  r"Read the results box and the $AS=S\Delta$ proof. Cover and redo the Cayley--Hamilton example ($A^{-1}$ and $A^3$).",
  r"explain why $g(A)=Sg(\Delta)S^{-1}$ and use Cayley--Hamilton to invert a $2\times2$."),
 (13,"ss:2-6",r"The matrix exponential",
  r"Learn the 3-way method box. Cover and redo: distinct eigenvalues, repeated eigenvalue ($e^{\lambda t}(I+t(A-\lambda I))$), $\pm i$ (rotation). Check $t=0$ every time. Read A3.3.",
  r"compute $\exp(tA)$ for a $2\times2$ with distinct \emph{and} with repeated eigenvalues, and check it."),
 (7,"ss:2-7",r"The solution formula for $\dot X=AX+BU$",
  r"Say the integrating-factor proof aloud. Cover and redo the step-response example; check $y(\infty)=T(0)$.",
  r"write $X(t)=\exp(tA)X_0+\int_0^t\exp((t-s)A)BU(s)\,ds$ and explain each term (CF and PI)."),
 (2,"ss:2-8",r"SISO and MIMO $(A,B,C,D)$",
  r"Read the box: names and shapes of $A,B,C,D$.",
  r"give the shapes of $A,B,C,D$ for $k$ inputs, $n$ states and $m$ outputs."),
 (7,"ss:2-9",r"Rational functions and the transfer function",
  r"Learn proper/strictly proper, poles/zeros, $T=D+C(sI-A)^{-1}B$. Redo the damped-oscillator example; read A2.1 and the proof of Prop 0.20.",
  r"compute $T(s)$ for a $2\times2$ system and say why every pole is an eigenvalue (but not conversely)."),
 (8,"ss:2-10",r"Realisation: from $T(s)$ back to $(A,B,C,D)$",
  r"Learn the 4-step method. Cover and redo the frame 79 example and the proper example with long division.",
  r"realise any proper $T(s)$ (including the $D\neq0$ case) and check it by the determinant formula."),
 (5,"ss:2-11",r"Exam-style questions for Chapter 2",
  r"Do Q2.1 closed book and mark it. Q2.2 if time.",
  r"get Q2.1 fully right."),
]),
3: ("Chapter 3: Laplace transforms", "ch3", [
 (4,"ss:3-1",r"Definition and the table",
  r"Read the definition. Cover the table and write it from memory twice.",
  r"write the whole table from memory."),
 (4,"ss:3-2",r"Properties",
  r"Learn the 6 properties; say the derivative-rule proof aloud (integration by parts).",
  r"state $\Lap(f')$, $\Lap(f'')$, the shift rule and the $t f(t)$ rule."),
 (5,"ss:3-3",r"Laplace transforms from the definition",
  r"Cover and redo A3.1 ($\cos2\omega t$ via $e^{\pm2i\omega t}$, then $\sin^2\omega t$). Read the $x^2$ example.",
  r"find $\Lap(e^{at})$ and $\Lap(\cos at)$ from the definition, stating the condition on $s$."),
 (5,"ss:3-4",r"Partial fractions and inverting",
  r"Learn the 5-step invert method and Lerch. Cover and redo the repeated-pole example.",
  r"invert a function with a repeated pole and one with an irreducible quadratic (complete the square)."),
 (9,"ss:3-5",r"Solving initial value problems",
  r"Learn the 5-step IVP method. Cover and redo A3.2 and the second-order step example.",
  r"solve a second-order IVP by Laplace from start to finish, including the check."),
 (5,"ss:3-6",r"Convolution and integral equations",
  r"Learn $\Lap(f*g)=\hat f\hat g$; read the proof. Cover and redo $y=t+\int_0^t\sin(t-u)y(u)\,du$.",
  r"spot a convolution in an integral equation and solve it."),
 (5,"ss:3-7",r"Laplace transform of $(A,B,C,D)$",
  r"Derive $\hat Y=T\hat U+C(sI-A)^{-1}X(0)$ yourself. Read the complex-eigenvalue $\exp(tA)$ example.",
  r"explain why $\hat Y=T(s)\hat U$ when $X(0)=0$, and get $\exp(tA)$ as $\Lap^{-1}[(sI-A)^{-1}]$."),
 (6,"ss:3-8",r"Jordan canonical form",
  r"Learn: algebraic mult.\ = total block size; geometric mult.\ = number of blocks; minimal polynomial uses the largest block. Read the corrected frame 119 example.",
  r"read off multiplicities and the minimal polynomial from a Jordan form, and find $\exp(tJ_2(\lambda))$."),
 (5,"ss:3-9",r"Exam-style questions for Chapter 3",
  r"Do Q3.2 and Q3.4 closed book and mark them.",
  r"get Q3.2 and Q3.4 fully right."),
]),
4: ("Chapter 4: Frequency response and stability", "ch4", [
 (2,"ss:4-1",r"Transfer functions and realisation",
  r"Read the box (Theorems 0.38 and 0.46).",
  r"state what can be realised by a SISO, and by a BIBO-stable SISO."),
 (8,"ss:4-2",r"Frequency response, gain and phase",
  r"Learn the method and the quadrant warning. Cover and redo $\frac1{s+1}$ including its Nyquist circle; read the $\frac1{as^2+bs+1}$ example.",
  r"find $\Gamma(\omega)$, $\phi(\omega)$ for a simple $T$ and sketch its Nyquist plot."),
 (6,"ss:4-3",r"Stability: the three cases",
  r"Learn the three-row table and the method. Go through the five worked examples and say why each is classified that way.",
  r"classify $\dot X=AX$ as exponentially stable, marginal or unstable, including the Jordan-block case."),
 (3,"ss:4-4",r"The damped harmonic oscillator",
  r"Read the table. Connect it to ``$s^2+\beta s+\gamma$ stable iff $\beta,\gamma>0$''.",
  r"say for which $\beta,\gamma$ the oscillator is stable, marginal or unstable."),
 (3,"ss:4-5",r"Resonance",
  r"Read the undamped oscillator example. Understand the double pole $\Rightarrow$ $t\sin\nu t$.",
  r"explain in two sentences why marginally stable is \emph{not} BIBO stable."),
 (5,"ss:4-6",r"BIBO stability theorems",
  r"Say the proof of Theorem 0.42 aloud (bound $\|\exp(tA)\|\le Me^{-\delta t}$, integrate). Read the outline of Theorem 0.45.",
  r"write the proof of Theorem 0.42 closed book."),
 (3,"ss:4-7",r"Exam-style questions for Chapter 4",
  r"Do Q4.1 closed book and mark it.",
  r"get Q4.1 fully right."),
]),
5: ("Chapter 5: Feedback control", "ch5", [
 (5,"ss:5-1",r"Stable polynomials",
  r"Learn Prop 0.43 and its proof, the counterexample $(s+1)(s^2+1)$, and the degree 2 and 3 tests.",
  r"decide whether a polynomial of degree $\le3$ is stable, and prove Prop 0.43."),
 (3,"ss:5-2",r"The ring $\mathcal S$",
  r"Learn the two conditions (proper, poles in open LHP) and why $\mathcal S$ is not a field.",
  r"say whether $\frac{s^2}{s+1}$, $\frac{1}{s^2+1}$, $\frac{s}{(s+1)^2}$ are in $\mathcal S$, with reasons."),
 (5,"ss:5-3",r"Nyquist's criterion",
  r"Learn the statement and $N=Z-P$. Cover and redo the $\frac{k}{(s+1)^3}$ example (crossing at $-k/8$).",
  r"find the gain range for stability from where the Nyquist plot crosses the negative real axis."),
 (6,"ss:5-4",r"The simple feedback loop and PID",
  r"Derive $T=G/(1+GK)$ from the diagram. Cover and redo the PI example and the proportional example.",
  r"find a PI or PD controller that stabilises a simple plant, stating your sign convention."),
 (4,"ss:5-5",r"Euclid, B\'ezout and matrix completion",
  r"Learn the algorithm. Cover and redo worked examples (a) and (b); read (c) and (d).",
  r"find $M,N$ with $PM+QN=1$ for two coprime polynomials of low degree."),
 (9,"ss:5-6",r"Coprime factorisation and Youla",
  r"Learn the 4-step algorithm and the four formulas $QY,PY,XQ,PX$. Cover and redo worked example A ($\frac1{s-1}$); read B.",
  r"do the whole algorithm for $G=\frac1{s-a}$ and check all four closed-loop functions."),
 (4,"ss:5-7",r"Well-posedness and internal stability",
  r"Read Lemma 0.51 and the ``trap'' example.",
  r"explain why all four functions must be in $\mathcal S$, using the trap example."),
 (4,"ss:5-8",r"Positive definite matrices",
  r"Learn the three equivalent conditions. Cover and redo A3.4 (i)--(v) and the minors example.",
  r"test a $3\times3$ matrix by leading minors and prove A3.4(iii)."),
 (4,"ss:5-9",r"Lyapunov's criterion and equation",
  r"Say the proof aloud ($V=\langle KX,X\rangle$ is decreasing). Redo the $K=I$ example; read the Lyapunov-equation example.",
  r"use $K=I$ to show solutions are bounded, and write the proof."),
 (2,"ss:5-10",r"Sylvester's equation",
  r"Read the result and the $1\times1$ intuition $a\neq-b$.",
  r"state when $AY+YB=-C$ has a unique solution for every $C$."),
 (4,"ss:5-11",r"Exam-style questions for Chapter 5",
  r"Do Q5.1 and Q5.3 closed book and mark them.",
  r"get Q5.1 and Q5.3 fully right."),
]),
}
BREAKS = {1:(5,"Stand up, get water, no phone."), 2:(10,"Longer break: eat something. You are halfway."),
          3:(5,"Short break."), 4:(5,"Short break. Last chapter next.")}

def hm(m): return f"{m//60}:{m%60:02d}"
t = 14*60+30
out=[]; rows=[]
P=out.append
P(r"""% Study plan 14:30-19:00, subchapter by subchapter. GENERATED by gen_plan.py: edit there.
\providecommand{\G}[1]{\S\ref{#1}, p.\,\pageref{#1}}
\providecommand{\tick}{$\square$}
\newtcolorbox{chapplan}[1]{colback=white,colframe=navy,title={#1},left=2mm,right=2mm}
\newcommand{\sub}[5]{\par\smallskip\noindent\textbf{\color{navy}#1}\ \ {\small(#2 min)}\ \ \textbf{#4} \hfill{\small\color{grey}\G{#3}}\par
 \noindent\hspace*{4mm}\parbox{\dimexpr\linewidth-4mm}{\textbf{Do:} #5}\par}
\newcommand{\gate}[1]{\noindent\hspace*{4mm}\parbox{\dimexpr\linewidth-4mm}{\tick\ \textbf{Move on when you can} #1}\par\smallskip}
\newcommand{\pausebox}[2]{\begin{tcolorbox}[colback=green!6,colframe=green!60!black,title={Break \quad #1}]#2\end{tcolorbox}}

\section{Your study plan: 14:30 to 19:00, subchapter by subchapter}\label{sec:plan}

\subsection*{How it works}
You go through the guide \textbf{one subchapter at a time}, in order. Each subchapter has a time slot, a \textbf{Do} list and a
\textbf{Move on when you can\dots} test. Only move to the next subchapter when you can pass its test \emph{without looking}.

\begin{methodbox}[title={The loop for every subchapter}]
\begin{enumerate}
\item \textbf{Read} the definition and method boxes slowly. For every step ask ``\emph{why} is this allowed?''
\item \textbf{Cover} each worked example and do it yourself on paper; uncover one line only when stuck.
\item \textbf{Explain} the main idea aloud in one or two sentences, as if to a friend.
\item \textbf{Test}: close the guide and do the ``Move on when you can'' task. Pass $\Rightarrow$ tick the box and move on.
\end{enumerate}
\end{methodbox}
\begin{warnbox}[title={The stuck rule (keeps you on time without skipping understanding)}]
If you still cannot pass a test \textbf{3 minutes after its slot ends}, write the subchapter number on a ``come back'' list, put a star next to it, and move on.
Later subchapters often make earlier ones click. The final slot (18:50--19:00) is reserved for your starred subchapters.
Never just reread: always \emph{do} something (write, derive, explain aloud).
\end{warnbox}
Have ready: the guide, plain paper, pen, calculator, a ``come back'' list, phone in another room.
""")
# overview
start=t; t+=5
P(r"\begin{chapplan}{Start \quad "+hm(start)+"--"+hm(t)+r" \quad The whole module on one page}")
P(r"\sub{"+hm(start)+"--"+hm(t)+r"}{5}{sec:map}{The big picture}{Read the chapter table and the chain diagram. Then, closed book, write the chain ODE $\to$ diagram $\to$ $(A,B,C,D)$ $\to$ $T(s)$ $\to$ stability $\to$ feedback.}")
P(r"\gate{write $\dot X=AX+BU$, $Y=CX+DU$ and $T(s)=D+C(sI-A)^{-1}B$ from memory.}")
P(r"\end{chapplan}")
rows.append((hm(start)+"--"+hm(t),5,"Overview","sec:map"))
for c in range(1,6):
    name,lab,subs=CH[c]
    tot=sum(s[0] for s in subs); cs=t
    P(r"\begin{chapplan}{"+name+r" \quad "+hm(cs)+"--"+hm(cs+tot)+f" ({tot} min)"+"}")
    if c>1:
        P(r"\noindent\textbf{Warm-up recall (inside the first slot, 1 min, closed book):} "+
          {2:r"$A,B,C,D$ for $m\ddot x+kx=u$; the companion matrix of $s^3+2s+5$.",
           3:r"the solution formula for $\dot X=AX+BU$; $\exp(tA)$ for a double eigenvalue; $T(s)$.",
           4:r"$\Lap(f')$, $\Lap(f'')$, $\Lap(\sin at)$, $\Lap(f*g)$.",
           5:r"the stability table for $\dot X=AX$; the definition of BIBO."}[c]+r"\par")
    for (m,l,ti,do,gate) in subs:
        s0=t; t+=m
        P(r"\sub{"+hm(s0)+"--"+hm(t)+"}{"+str(m)+"}{"+l+"}{"+ti+"}{"+do+"}")
        P(r"\gate{"+gate+"}")
    P(r"\end{chapplan}")
    rows.append((hm(cs)+"--"+hm(t),tot,name,lab))
    if c in BREAKS:
        m,txt=BREAKS[c]; b0=t; t+=m
        P(r"\pausebox{"+hm(b0)+"--"+hm(t)+"}{"+txt+"}")
        rows.append((hm(b0)+"--"+hm(t),m,"Break",None))
e0=t; t+=10
P(r"\begin{chapplan}{Finish \quad "+hm(e0)+"--"+hm(t)+r" \quad Come-back list and recall}")
P(r"\sub{"+hm(e0)+"--"+hm(e0+7)+r"}{7}{sec:proofs}{Your starred subchapters}{Go back to each subchapter on your ``come back'' list and retry its test. If the list is empty, do mock question M2 (\G{sec:mock}).}")
P(r"\gate{pass the test of at least one starred subchapter.}")
P(r"\sub{"+hm(e0+7)+"--"+hm(t)+r"}{3}{sec:mock}{Formula sheet from memory}{Cover the formula sheet (last page) and write as many lines as you can; mark what you missed.}")
P(r"\gate{write at least 15 of the 20 formula-sheet lines.}")
P(r"\end{chapplan}")
rows.append((hm(e0)+"--"+hm(t),10,"Come-back list and recall","sec:proofs"))
assert t==19*60, hm(t)
# overview table
tab=[r"\subsection*{Timetable at a glance}",r"\begin{center}\renewcommand{\arraystretch}{1.25}\small",
     r"\begin{tabular}{@{}p{2.3cm}p{1cm}p{7.5cm}p{3.4cm}@{}}\toprule",
     r"\textbf{Time} & \textbf{Min} & \textbf{Part} & \textbf{Guide}\\\midrule"]
for (tm,m,n,l) in rows:
    tab.append(f"{tm} & {m} & {n} & "+(r"\G{"+l+"}" if l else "")+r"\\")
tab+= [r"\bottomrule\end{tabular}\end{center}",
       r"Each chapter is split into its subchapters on the following pages, with the minutes chosen by how hard and how examinable each one is.",
       r"\subsection*{Subchapter by subchapter}"]
idx=[i for i,s in enumerate(out) if s.startswith(r"\begin{chapplan}{Start")][0]
out[idx:idx]=tab
# tracker
out.append(r"""\subsection*{Come-back list}
\begin{center}\renewcommand{\arraystretch}{1.6}
\begin{tabular}{@{}p{2.5cm}p{8cm}p{3.5cm}@{}}\toprule
\textbf{Subchapter} & \textbf{What I could not do} & \textbf{Fixed? (time)}\\\midrule
 & & \\ & & \\ & & \\ & & \\ & & \\ & & \\\bottomrule\end{tabular}\end{center}
\begin{exambox}[title={Next session}]
Start with 10 minutes writing the formula sheet from memory, then your come-back list, then the proofs list (\G{sec:proofs}) and the full mock paper (\G{sec:mock}).
\end{exambox}
\newpage""")
with open(sys.argv[1],'w') as fh: fh.write('\n'.join(out)+'\n')
print("ok, ends", hm(t))
