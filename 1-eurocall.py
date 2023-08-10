import numpy as np
from scipy.stats import norm

n = 1000000 # number of draws for monte carlo simulation

# black scholes params
s0 = 100    # stock price today
r = 0.05   # risk free rate
sigma = 0.2 # stock (historical) volatility
T = 1  # Time to maturity (in years)
K = 100     # Strike price

def montecarlo(n, s0, r, sigma, T, K):
    c = []
    for i in range(n):
        z = np.random.normal(0,1) # draw normal random variable
        s = s0 * np.exp((r - 0.5 * (sigma ** 2)) * T + z * sigma * np.sqrt(T)) # calculate price
        _c = np.exp(-r * T) * max(s - K, 0) # discount price and compute payoff
        c.append(_c) 

    return (np.mean(c)) # calculate average price

def closed_form_BS(s0, r, sigma, T, K):
    d1 = (np.log(s0/K) + (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return s0*norm.cdf(d1) - K * np.exp(-r*T)* norm.cdf(d2)

print(f"Monte Carlo: {montecarlo(n, s0, r, sigma, T, K)}")
print(f"Closed Form: {closed_form_BS(s0, r, sigma, T, K)}")