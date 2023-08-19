Learning Least Square Monte Carlo Methods by replicating the research paper: Valuing American Options by Simulation: A Simple Least-Squares Approach. By Francis A. Longstaff and Eduardo S. Schwartz

Quick recap
# A simple approach to $\mathrm{LSMC}$

  

## Definition:

  

Let $\left(\Omega, F, \mathbb{Q},\left\{\mathcal{F}_{t}\right\}\right)$ be a filtered probability space.

  

Let $V$ be an $F_{T 1}$ - measurable random voriable defined as the conditional expectation of $U$ :

  

$$
V=E^{\mathbb{Q}}\left(U \mid  \mathcal{F}_{T 1}\right)
$$

  

where $U$ is at least $\mathcal{F}$-measurable.

  

Let $Y:=\left(Y_{1}, \ldots, Y_{p}\right)$ be a given $\mathcal{F}_{T 1}$-measurable random variable.

  

Let $f: \mathbb{R}^{p} \times  \mathbb{R}^{q}$ be a given function.

  

Let $\Omega^{*}=\left\{\omega_{1}, \ldots, w_{m}\right\}$ be a drawing from $\Omega$ (e.g., Monte Carlo simulation for $\mathbb{Q}$ ) Let $\alpha^{*}:=\left(\alpha_{1}, \ldots, \alpha_{\mathrm{q}}\right)$ such that

  

$$
\left\|U-f\left(Y, \alpha^{*}\right)\right\|_{L 2\left(\Omega^{*}\right)}=\min _{\alpha}\|U-f(Y, \alpha)\|_{L 2\left(\Omega^{*}\right)}
$$

  

Where $\left\|U-f\left(Y, \alpha^{*}\right)\right\|_{L 2\left(\Omega^{*}\right)}^{2}=\sum_{j=1}^{m}\left(U\left(\omega_{j}\right)-f\left(Y\left(\omega_{j}\right), \alpha^{*}\right)\right)^{2}$

  

We set $V^{L S}:=f\left(Y, \alpha^{*}\right)$

  

The random variable $V^{L S}$ is $\mathcal{F}_{T 1}-$ measurable. It is defined over $\Omega$ and a least square approximation of $V$ on $\Omega^{*}$.

  

Following the instructions on Longstaff and Schwartz paper, the function $f$ is chosen under the condition $q=p$ such that

  

## Lemma: Linear regression

  

$$
f\left(y_{1}, \ldots, y_{p}, \alpha_{1}, \ldots, \alpha_{q}\right):=\sum_{i=1}^{p} \alpha_{i} y_{i}
$$

  

Let $\Omega^{*}=\left\{w_{1}, \ldots, w_{m}\right\}$ be a given sample space.

  

Let $V: \Omega^{*} \rightarrow  \mathbb{R}$ and $Y:=\left(Y_{1}, \ldots, Y_{p}\right): \Omega^{*} \rightarrow  \mathbb{R}^{p}$ be a given random variables.

  

$$
f\left(y_{1}, \ldots, y_{p}, \alpha_{1}, \ldots, \alpha_{q}\right):=\sum  \alpha_{i} y_{i}
$$

  

$\forall  \alpha^{*}$ with $X^{\top} X \alpha^{*}=X^{\top} v$

  

$$
\begin{gathered}
\left\|V-f\left(Y, \alpha^{*}\right)\right\|_{L 2\left(\Omega^{*}\right)}=\min \|V-f(Y, \alpha)\|_{L 2(\Omega)}^{*} \\
X:=\left(\begin{array}{ccc}
Y_{1}(\omega) & \ldots & Y_{p}\left(\omega_{1}\right) \\
\vdots & & \vdots \\
Y_{1}\left(\omega_{m}\right) & \ldots & Y_{p}\left(\omega_{m}\right)
\end{array}\right), v:=\left(\begin{array}{c}
V\left(\omega_{1}\right) \\
\vdots \\
V\left(\omega_{m}\right)
\end{array}\right)
\end{gathered}
$$

  

${ }^{1}$ From LMU lectures available in the references if $\left(X^{\top} X\right)^{-1}$ exists, then $\alpha^{*}:=\left(X^{\top} X\right)^{-1} X^{\top} v$

  

## Proof of Lemma:

  

$$
\begin{aligned}
& \|V-f(Y, \alpha)\|_{L_{2}}^{2}=\langle V-X \cdot  \alpha, V-X \cdot  \alpha\rangle \\
& =V^{\top} V-2  \alpha^{\top} X^{\top} V+\alpha^{\top} X^{\top} \alpha
\end{aligned}
$$

  

Now we differentiate and set to 0

  

$$
\begin{gathered}
-2 X^{\top} V+2 X^{\top} X \alpha=0 \\
X^{\top} V+X^{\top} X \alpha=0
\end{gathered}
$$

  

Then we recover $\alpha^{*}$ as stated in the lemma.

  

$$
\alpha^{\top}=\left(X^{\top} X\right)^{-1} X^{\top} v
$$
