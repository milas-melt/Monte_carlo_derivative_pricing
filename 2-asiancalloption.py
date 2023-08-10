import numpy as np

n = 10000   # number of draws for monte carlo simulation
m = 3       # compute average over 3 days

# black scholes params
s0 = 100    # stock price today
r = 0.05   # risk free rate
sigma = 0.2 # stock (historical) volatility
T = 1  # Time to maturity (in years)
K = 100     # Strike price

s = [s0]
dt = T/m
c = []
for i in range(n):
    for j in range(m):
        z = np.random.normal(0,1) # draw normal random variable
        s.append(s[j] * np.exp((r - (sigma ** 2)) * dt + sigma * np.sqrt(dt) * z))
    
    savg = np.mean(s)
    s = [s[-1]]
    c.append(np.exp(-r * T) * max(0, savg - K))

print(np.mean(c))