Learning Least Square Monte Carlo Methods by replicating the research paper: Valuing American Options by Simulation: A Simple Least-Squares Approach. By Francis A. Longstaff and Eduardo S. Schwartz

# Before delving into the subject, quick recap of the basics (Monte Carlo)
## Motivation Monte Carlo
<img width="465" alt="Screenshot 2023-08-19 at 21 07 52" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/74920ce5-15f7-415e-b2b4-7f748ed56575">

## RNV
<img width="465" alt="Screenshot 2023-08-19 at 21 09 05" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/7f9e0e05-ceb9-47d7-8ad1-1f9c882f7d24">

## Numerical solution
<img width="465" alt="Screenshot 2023-08-19 at 21 09 57" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/63f416aa-3f2c-468d-aef3-a934dad2010c">


# Quick recap of LMSC

We use Longstaff & Schwartz notations and setup. Screenshots from Chapter 2 of the paper:
<img width="483" alt="Screenshot 2023-08-24 at 12 25 50" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/1b28df7c-9432-4fc3-8e29-0c39549737ff">

<img width="470" alt="Screenshot 2023-08-24 at 12 25 11" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/adcbddfc-5f85-4853-84a5-f0afd2c03770">
<img width="470" alt="Screenshot 2023-08-24 at 12 25 30" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/2b8fdc9b-1410-40c2-aaff-06615cf46a9f">


## Definition:
<img width="690" alt="Screenshot 2023-08-19 at 21 01 49" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/05d28825-0dd8-44ee-86a3-f8b95d641746">

## Lemma
<img width="690" alt="Screenshot 2023-08-19 at 21 02 26" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/cf7daed3-6182-4697-ac00-070b18cfc952">
<img width="690" alt="Screenshot 2023-08-19 at 21 02 37" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/f1096119-bbd8-4041-a5d3-04369acd46ab">

## Demo results for simple American put
### Exercise value computation of the simulated paths for an American put
<img width="695" alt="Screenshot 2023-08-19 at 21 04 25" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/376d986f-9b91-443b-8d3f-50c1adf6ce19">

### Exercise value / Continuation value vs underlying price
<img width="568" alt="Screenshot 2023-08-19 at 21 05 11" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/192ed598-bcb9-43f1-8271-7b45427793fd">

### Fitted Exercise value / Continuation value vs underlying price
<img width="568" alt="Screenshot 2023-08-19 at 21 05 26" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/be83ba7e-3f52-45c6-9254-34593d4c21cd">

### Approximation of continuation value at t=today vs t=maturity
<img width="700" alt="Screenshot 2023-08-19 at 21 05 55" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/0e15aefe-3651-4ff7-b929-eb2fa9598c88">

### Exercise decision vs time
<img width="396" alt="Screenshot 2023-08-19 at 21 06 33" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/20fc6df8-fa87-4167-a472-375cdb140568">

### Adjusted exercise decision vs time
<img width="465" alt="Screenshot 2023-08-19 at 21 06 52" src="https://github.com/milas-melt/Monte_carlo_derivative_pricing/assets/55765976/10dc925a-2df0-4436-81a8-7e7636326354">

