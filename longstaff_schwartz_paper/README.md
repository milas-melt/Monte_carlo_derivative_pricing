Learning Least Square Monte Carlo Methods by replicating the research paper: Valuing American Options by Simulation: A Simple Least-Squares Approach. By Francis A. Longstaff and Eduardo S. Schwartz

Quick recap here:
**Definition:**

Let Ω,F,Q,Ft be a filtered probability space.

Let V be an FT1 - measurable random voriable defined as the conditional expectation of U:

V=EQU∣FT1. 

where U is at least F-measurable.

Let Y:=Y1,…,Yp be a given FT1-measurable random variable.

Let f:Rp×Rq be a given function.

Let Ω\*=ω1,…,wm be a drawing from Ω (e.g., Monte Carlo simulation for Q)

Let α\*:=(α1, …, αq) such that

U-fY,α\*L2(Ω\*)=minαU-fY,αL2(Ω\*)

Where U-fY,α\*2L2Ω\*=j=1mUωj-fYωj, α\*2

We set VLS:=f(Y, α\*)

The random variable VLS is FT1-measurable. It is defined over Ω and a least square approximation of V on Ω\*.



Following the instructions on Longstaff and Schwartz paper, the function f is chosen under the condition q=p such that

fy1,…,yp, α1,…,αq≔ i=1pαiyi

**Lemma: Linear regression**


Let Ω\*=w1,…,wm be a given sample space.


Let V:Ω\*→R and Y:=Y1,…,Yp:Ω\*→Rp be a given random variables.

fy1,…,yp,α1,…,αq:= αiyi

∀α\* with X⊤Xα\*=X⊤v

V-fY,α\*L2Ω\*=min∥V-f(Y,α)∥L2(Ω)\*

` `X:=Y1(ω)…Ypω1⋮⋮Y1ωm…Ypωm,v:=Vω1⋮Vωm


if X⊤X-1 exists, then α\*:=X⊤X-1X⊤v

**Proof of Lemma:**

` `∥V-f(Y,α)∥L22=⟨V-X⋅α,V-X⋅α⟩ =V⊤V-2α⊤X⊤V+α⊤X⊤α

Now we differentiate and set to 0

-2X⊤V+2X⊤Xα=0X⊤V+X⊤Xα=0

Then we recover α\* as stated in the lemma.

α⊤=X⊤X-1X⊤v
