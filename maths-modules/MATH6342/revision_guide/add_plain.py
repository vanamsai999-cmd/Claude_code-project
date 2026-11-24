"""Insert 'In plain words' boxes after each subsection and answer templates before
each chapter's exam questions. Idempotent: skips a label that already has a box.
Run once from this folder:  python3 add_plain.py"""
import glob, re

PLAIN = {
# ---------------- Chapter 1
"ss:1-1": (r"""A linear system is a \textbf{machine}: a signal $u(t)$ goes in, a signal $y(t)$ comes out. Inside, the signal passes through
simple ``boxes''. Each box does one job: \emph{scale it} (amplifier), \emph{add up the history} (integrator), \emph{measure how fast it changes}
(differentiator), \emph{combine signals} (summing junction) or \emph{copy it} (tap).
\textbf{Linear} means ``double the input, double the output; add two inputs, add the outputs''.""",
r"""``Show that $L$ is linear'' or ``which of these maps are linear?''."""),
"ss:1-2": (r"""\textbf{Feedback} means part of the output is sent back to the input. Think of a thermostat: the room temperature (output)
is measured and used to switch the heater (input). \textbf{Negative} feedback calms the system down (going faster creates drag);
\textbf{positive} feedback pushes it further the same way (more birds $\Rightarrow$ more births). Open loop = no signal ever comes back.""",
r"""``Find the output of this feedback diagram'' (write the equation at the summing junction and solve for $y$)."""),
"ss:1-3": (r"""Differentiators amplify noise, so we want diagrams built from \textbf{integrators} only.
The trick: \textbf{integrate the whole equation} until no derivatives are left. Then every term is ``an integral of $y$'' or
``an integral of $u$''. Terms with $y$ become a loop back from the output; terms with $u$ go forward from the input.""",
r"""``Express this ODE / integral equation as a block diagram with no differentiators'' (AE1, A1.1--A1.2). Usually 5 marks."""),
"ss:1-4": (r"""A big $n$-th order ODE is hard; $n$ small first-order ODEs are easy, and they fit into \textbf{one matrix equation}.
So we keep track of the list $y, y', \dots, y^{(n-1)}$ as one vector $X$ (the \emph{state}).
Each entry's derivative is simply the next entry, except the last, which the ODE tells us.""",
r"""``Introduce $v=dx/dt$ and write the system as $(A,B,C,D)$'' (AE1, A1.3)."""),
"ss:1-5": (r"""The companion matrix is a \textbf{ready-made matrix for any polynomial}: put ones just above the diagonal and the
polynomial's coefficients (with minus signs, constant term first) along the bottom row. Its characteristic polynomial is exactly
the polynomial you started with.""",
r"""``Find a matrix whose characteristic polynomial is $p(s)$'' (AE2, A2.2), or the induction proof."""),
# ---------------- Chapter 2
"ss:2-1": (r"""The \textbf{characteristic polynomial} $\det(sI-A)$ is the polynomial whose roots are the eigenvalues of $A$.
The eigenvalues control \emph{everything} later: how solutions grow or decay, the poles of $T(s)$, stability.
The \textbf{adjugate} is the ``almost-inverse'': $A^{-1}=\adj(A)/\det A$.""",
r"""a first step in almost every Chapter 2 question: ``find the eigenvalues of $A$''."""),
"ss:2-2": (r"""$(sI-A)^{-1}$ is just the inverse of a matrix whose entries contain the letter $s$.
Use the same recipe as for any inverse (cofactors, transpose, divide by the determinant); the entries come out as fractions in $s$.
You need it because $T(s)=D+C(sI-A)^{-1}B$, and because it is the Laplace transform of $\exp(tA)$.""",
r"""``Find $(sI-A)^{-1}$'' (AE1, A1.4), usually for a triangular or $2\times2$ matrix."""),
"ss:2-3": (r"""A \textbf{norm} measures size: $\|z\|$ is the length of a vector; $\|A\|$ is the most $A$ can stretch a vector of length 1.
Cauchy--Schwarz says a dot product can never be bigger than the product of the lengths. These are the tools that let us say
``$\exp(tA)$ stays bounded'' later.""",
r"""short bookwork: ``prove Cauchy--Schwarz'' or ``show $\|AB\|\le\|A\|\|B\|$''."""),
"ss:2-4": (r"""\textbf{Rank} = how many genuinely different directions the rows (or columns) give. Stacking $C, CA, CA^2,\dots$ tests whether the
output $y=CX$ can ``see'' every part of the state. Rank less than $n$ means some part of the system is invisible from the output
(and a pole will cancel in $T(s)$).""",
r"""``Show $Q^\top=R$, find $R$ when $C^\top$ is an eigenvector, find $\rank Q$'' (AE2, A2.3)."""),
"ss:2-5": (r"""If you change coordinates to the eigenvectors, $A$ becomes a \textbf{diagonal} matrix $\Delta$, and diagonal matrices are easy:
powers, polynomials and exponentials just act on each diagonal entry. Then change back: $g(A)=S\,g(\Delta)\,S^{-1}$.
Cayley--Hamilton: every matrix satisfies its own characteristic equation, so high powers of $A$ reduce to low ones.""",
r"""``Diagonalise $A$'', ``use Cayley--Hamilton to find $A^{-1}$ or $A^3$''."""),
"ss:2-6": (r"""For a number $a$, the solution of $x'=ax$ is $x=e^{at}x_0$. For a matrix it is the same with $\exp(tA)$ in place of $e^{at}$.
To compute it: \textbf{diagonalise} (then it is just $e^{\lambda t}$ on the diagonal), or for a repeated eigenvalue use
$e^{\lambda t}(I+tN)$. Each eigenvalue $\lambda$ contributes a term $e^{\lambda t}$: negative real part $\Rightarrow$ it dies away.""",
r"""``Find $\exp(tA)$'' (AE3, A3.3) --- one of the most common computations in the module."""),
"ss:2-7": (r"""The answer has two parts: \textbf{what the system does on its own} from its starting state ($\exp(tA)X_0$), plus
\textbf{the accumulated effect of all the inputs so far} (the integral: each past input $U(s)$ is pushed forward by $\exp((t-s)A)$ and added up).
Same idea as the integrating factor for $y'-ay=f$ in first year.""",
r"""``Prove the solution formula'' (bookwork) or ``find $y(t)$ for this input and initial state''."""),
"ss:2-8": (r"""$A$ = how the state evolves, $B$ = how inputs push the state, $C$ = what we measure, $D$ = input that goes straight to the output.
SISO = one input, one output (like a fan); MIMO = many (like a washing machine). Check shapes: they must multiply.""",
r"""``State the sizes of $A,B,C,D$'' or ``give an example of a MIMO system''."""),
"ss:2-9": (r"""The \textbf{transfer function} $T(s)$ is the system's ``multiplier'': in the Laplace world, output $=T(s)\times$ input.
It is a fraction of polynomials in $s$. Its \textbf{poles} (where the denominator is zero) are eigenvalues of $A$, and they decide stability.""",
r"""``Compute the transfer function $T(s)=D+C(sI-A)^{-1}B$'' (AE2, A2.1). Usually 4--8 marks."""),
"ss:2-10": (r"""Realisation is the \textbf{reverse} of the last subchapter: you are given $T(s)$ and must build a machine $(A,B,C,D)$ with that $T$.
Recipe: denominator coefficients go in the bottom row of a companion matrix, numerator coefficients go in $C$, and $D$ is the
constant left over after division.""",
r"""``Find a SISO $(A,B,C,D)$ with transfer function $T(s)$'', often followed by ``verify''."""),
# ---------------- Chapter 3
"ss:3-1": (r"""The Laplace transform is a \textbf{translator}: it turns a function of time $f(t)$ into a function of $s$, $\hat f(s)$.
The point is that hard calculus in $t$ becomes easy algebra in $s$. You will mostly use the \textbf{table}, not the integral.""",
r"""``Using the table, write down $\Lap(\dots)$'' or ``invert $F(s)$''."""),
"ss:3-2": (r"""The properties are the ``grammar'' of the translator. The most important: \textbf{differentiating in $t$ becomes multiplying by $s$}
(minus the starting value). So an ODE becomes an equation you can solve by dividing.""",
r"""``State and prove $\Lap(f')=s\Lap f-f(0)$'' or using the shift and $t f(t)$ rules to find a transform."""),
"ss:3-3": (r"""``From the definition'' means you must actually do the integral $\int_0^\infty f(t)e^{-st}dt$, not quote the table.
Two tricks cover almost everything: \textbf{integration by parts} (for powers of $t$) and \textbf{writing $\cos,\sin$ using $e^{\pm i a t}$}.""",
r"""``Calculate $\Lap(\cos2\omega t)$ from the definition, deduce $\Lap(\sin^2\omega t)$'' (AE3, A3.1)."""),
"ss:3-4": (r"""To go back from $s$ to $t$, break the fraction into \textbf{simple pieces} (partial fractions), because each simple piece is in the table.
Lerch's theorem guarantees the answer is unique, so ``looking it up'' is a valid method.""",
r"""the last step of every Laplace question: ``use partial fractions at the final step''."""),
"ss:3-5": (r"""Recipe: translate the whole ODE (initial values appear automatically), solve for $\hat y$ by simple algebra,
split into partial fractions, translate back. No guessing of particular integrals needed.""",
r"""``Solve the IVP by taking Laplace transforms'' (AE3, A3.2). Very likely in the exam."""),
"ss:3-6": (r"""A \textbf{convolution} $\int_0^tf(t-u)g(u)\,du$ is a ``weighted memory'' of $g$. Its transform is simply the \textbf{product} $\hat f\,\hat g$.
So an integral equation with $\int_0^tk(t-u)y(u)\,du$ becomes an algebraic equation for $\hat y$.""",
r"""``Solve the integral equation'' or ``prove the convolution theorem''."""),
"ss:3-7": (r"""Applying the translator to the whole system: integrating becomes dividing by $s$, so the matrix ODE becomes
$\hat X=(sI-A)^{-1}B\hat U$, and output $=T(s)\times$ input. This is \emph{why} $T(s)=D+C(sI-A)^{-1}B$.""",
r"""``Show that $\hat Y=T(s)\hat U$ when $X(0)=0$'' or ``find $\exp(tA)$ by inverting $(sI-A)^{-1}$''."""),
"ss:3-8": (r"""Not every matrix can be diagonalised. The \textbf{Jordan form} is the ``next best'': diagonal blocks with 1's just above the diagonal.
Each block with eigenvalue $\lambda$ gives terms $e^{\lambda t}, te^{\lambda t}, \dots$ in $\exp(tA)$. Count blocks = count eigenvectors.""",
r"""``Find the algebraic/geometric multiplicities and the minimal polynomial'' or ``write down $\exp(tA)$ for a Jordan block''."""),
# ---------------- Chapter 4
"ss:4-1": (r"""Two promises: \textbf{any} sensible $T(s)$ can be built as a real system, and a \textbf{stable} $T(s)$ can be built as a stable system.
So we can design with $T(s)$ alone.""",
r"""a statement question: ``state the realisation theorem''."""),
"ss:4-2": (r"""Feed in a pure tone $e^{i\omega t}$. A linear system sends out \textbf{the same tone}, only louder or quieter (\textbf{gain} $\Gamma$)
and shifted in time (\textbf{phase} $\phi$). Both come from the single complex number $T(i\omega)$: its size and its angle.
The \textbf{Nyquist plot} draws $T(i\omega)$ for all $\omega$; the \textbf{Bode plot} draws gain and phase against $\omega$.""",
r"""``Find the gain and phase'', ``sketch the Nyquist plot'', ``what is the steady-state output for input $\cos\omega t$?''."""),
"ss:4-3": (r"""Each eigenvalue $\lambda$ gives a term like $e^{\lambda t}$. If its real part is \textbf{negative} the term shrinks to 0;
\textbf{zero} real part, it neither grows nor shrinks (unless a Jordan block adds a factor $t$, which makes it grow);
\textbf{positive}, it blows up. Stability is just ``where are the eigenvalues?''.""",
r"""``Classify the stability of $\dot X=AX$ for these matrices''."""),
"ss:4-4": (r"""A car's suspension: $\beta$ is the shock absorber, $\gamma$ is the spring. With both positive, bumps die away (stable).
No damping ($\beta=0$): it bounces forever (marginal). Negative damping: the bouncing grows (unstable).""",
r"""``For which $\beta,\gamma$ is the oscillator stable?''."""),
"ss:4-5": (r"""Pushing a swing at exactly its natural rhythm makes it go higher and higher. That is \textbf{resonance}: a \emph{bounded} push gives an
\emph{unbounded} response. So a system with eigenvalues on the imaginary axis is not safe (not BIBO stable) even though it
does not blow up on its own.""",
r"""``Show the system is not BIBO stable by choosing a bounded input'' (use $\cos\nu t$ at the natural frequency)."""),
"ss:4-6": (r"""\textbf{BIBO} = ``bounded input $\Rightarrow$ bounded output''. The main theorem: if every eigenvalue has negative real part,
$\exp(tA)$ decays exponentially, so the accumulated effect of a bounded input stays bounded. And a transfer function is stable
exactly when some BIBO-stable machine has it.""",
r"""``Prove that if all $\Re\lambda_j<0$ then $(A,B,C,D)$ is BIBO stable'' (bookwork)."""),
# ---------------- Chapter 5
"ss:5-1": (r"""A polynomial is \textbf{stable} if all its roots are in the left half plane (so the matching terms $e^{\lambda t}$ decay).
Quick test without finding roots: a stable polynomial must have \textbf{all coefficients positive}. That is enough for degree 2,
but not for degree 3 or more (use $a_2a_1>a_0$ for degree 3).""",
r"""``Is this polynomial stable?'', ``for which $k$ is it stable?'', ``prove all coefficients are positive''."""),
"ss:5-2": (r"""$\mathcal S$ is the set of ``safe'' transfer functions: \textbf{proper} (does not blow up at high frequency) and all poles on the
left (does not blow up in time). Adding or multiplying safe functions gives safe functions.""",
r"""``Is $f\in\mathcal S$?'' or ``show $\mathcal S$ is not a field''."""),
"ss:5-3": (r"""Look at the picture of $R(i\omega)$. If it never loops around the point $-1$, then closing the loop (feeding the output back
negatively) keeps the system stable. Where the curve crosses the negative real axis tells you how much extra gain you can add
before it becomes unstable.""",
r"""``Use Nyquist's criterion to find the values of $k$ for which the closed loop is stable''."""),
"ss:5-4": (r"""A \textbf{controller} watches the output and corrects the input, like cruise control. With negative feedback through $K$, the new
transfer function is $T=G/(1+GK)$. We choose $K$ (often $a+b/s+cs$, a PID) so that the new denominator is a stable polynomial.""",
r"""``Find a controller of the form $-a-b/s$ that stabilises $G$'' --- set up the denominator and choose $a,b$."""),
"ss:5-5": (r"""The Euclidean algorithm finds the \textbf{highest common factor} of two polynomials by repeated long division, exactly like for
whole numbers. Working backwards writes $1=PM+QN$ whenever $P,Q$ have no common root. This identity is the engine of the next subchapter.""",
r"""``Find polynomials $M,N$ with $PM+QN=1$'' or ``complete this matrix to an invertible one''."""),
"ss:5-6": (r"""Goal: a \textbf{recipe that stabilises any plant}. Write $G=P/Q$ using only ``safe'' functions (the substitution $\lambda=1/(1+s)$ does this),
find $X,Y$ with $PX+QY=1$ (Euclid), and take the controller $K=X/Y$. Then all closed-loop functions are products of safe functions, so safe.""",
r"""``Find a coprime factorisation and a stabilising controller, and verify''. A long question, but purely mechanical."""),
"ss:5-7": (r"""It is not enough for the output to behave: \textbf{every signal inside the loop} must stay bounded too. If the controller cancels an
unstable part of the plant, the problem is hidden, not removed. So we check all four functions, not just $G/(1+GK)$.""",
r"""``Is the loop internally stable?'', ``when is the SFL well posed?''."""),
"ss:5-8": (r"""A \textbf{positive definite} matrix is the matrix version of a positive number: $\langle Kz,z\rangle>0$ for every nonzero $z$.
Three equivalent tests: the definition, all eigenvalues positive, or all top-left determinants positive (easiest by hand).""",
r"""``Show that $S'KS$ / $\exp(A')K\exp(A)$ / $K+L$ is positive definite'' (AE3, A3.4)."""),
"ss:5-9": (r"""Lyapunov's idea is an ``energy'' $V=\langle KX,X\rangle$. If you can show the energy never increases, the state can never run away.
This checks stability \emph{without} finding eigenvalues.""",
r"""``Use $K=I$ to show solutions are bounded'' or ``prove Lyapunov's criterion''."""),
"ss:5-10": (r"""$AY+YB=-C$ is just a (big) system of linear equations for the entries of $Y$. It has exactly one solution for every $C$ unless
$A$ and $-B$ share an eigenvalue (like $ay+yb=-c$ fails when $a=-b$).""",
r"""``When does Sylvester's equation have a unique solution?''."""),
}

ANSWER = {
"ss:1-6": r"""\textbf{Block diagram:} (1) integrate $k$ times, saying ``with zero initial conditions''; (2) solve for $y$; (3) draw, labelling every wire; (4) one line checking the diagram gives back the equation.\\
\textbf{Matrix form:} (1) make monic; (2) define the state vector in words (``let $x_1=y$, $x_2=y'$''); (3) write the first-order equations; (4) state $A,B,C,D$ clearly with their sizes.""",
"ss:2-11": r"""\textbf{Eigenvalues:} write $\det(sI-A)$, expand (say which row/column), factorise, list roots.\\
\textbf{$\exp(tA)$:} eigenvalues $\to$ eigenvectors $\to$ $S$, $S^{-1}$ $\to$ $S\exp(t\Delta)S^{-1}$ $\to$ ``check: $t=0$ gives $I$''.\\
\textbf{Transfer function:} state $T(s)=D+C(sI-A)^{-1}B$, compute $\adj(sI-A)B$, multiply by $C$, simplify, comment on poles.\\
\textbf{Realisation:} divide if needed, quote Prop 0.22, write $A,B,C,D$, verify with $\det(sI-A)$ and $C\adj(sI-A)B$.""",
"ss:3-9": r"""\textbf{IVP:} (1) ``Taking Laplace transforms, using $\Lap(y')=s\hat y-y(0)$\dots''; (2) solve for $\hat y$; (3) partial fractions with constants found; (4) ``by the table and Lerch's uniqueness theorem, $y(t)=\dots$''; (5) check $y(0)$.\\
\textbf{From the definition:} write the integral to $R$, evaluate, let $R\to\infty$, state the condition on $s$.\\
\textbf{Integral equation:} name the convolution, transform, solve, invert, check by substitution.""",
"ss:4-7": r"""\textbf{Stability:} list the eigenvalues with real parts, name the case (exponential / marginal / unstable), justify with the theorem; for $\Re\lambda=0$ discuss the Jordan blocks.\\
\textbf{Gain/phase:} put $s=i\omega$, write $T(i\omega)=\frac{\cdots}{X+iY}$, give $\Gamma$ and $\phi$, and state the quadrant.\\
\textbf{Not BIBO:} name a bounded input (e.g.\ $\cos\nu t$), compute the output, show it is unbounded.""",
"ss:5-11": r"""\textbf{Polynomial stability:} quote the test you use (positive coefficients / Routh--Hurwitz) and check each condition.\\
\textbf{Controller design:} state $T=G/(1+GK)$, find the closed-loop denominator, state conditions, choose values, give the final $T$ and say why it is in $\mathcal S$.\\
\textbf{Coprime/Youla:} follow the 4 steps with headings, show $PX+QY=1$ explicitly, give $K=X/Y$, list the four closed-loop functions.""",
}

for f in sorted(glob.glob('ch[1-5]_*.tex')):
    L = open(f).read().split('\n'); out = []
    i = 0
    while i < len(L):
        out.append(L[i])
        m = re.search(r'\\label\{(ss:\d-\d+)\}', L[i]) if L[i].startswith('\\subsection{') else None
        if m:
            lab = m.group(1)
            already = i+1 < len(L) and (L[i+1].startswith('\\begin{plainbox}') or L[i+1].startswith('\\begin{answerbox}'))
            if not already and lab in PLAIN:
                idea, exam = PLAIN[lab]
                out.append('\\begin{plainbox}\n' + idea + '\n\\par\\smallskip\\textbf{In the exam this looks like:} ' + exam + '\n\\end{plainbox}')
            if not already and lab in ANSWER:
                out.append('\\begin{answerbox}\n' + ANSWER[lab] + '\n\\end{answerbox}')
        i += 1
    with open(f, 'w') as fh: fh.write('\n'.join(out))
print('done')
