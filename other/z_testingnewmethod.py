import numpy as np

np.random.seed(123456)

class GeometricBrownianMotion:
    def __init__(self, mu: float = 0.0, sigma: float = 1.0):
        self.mu = mu
        self.sigma = sigma

    def simulate(self, t, n):
        dt = np.concatenate((t[0:1], np.diff(t)))
        dW = (np.random.normal(size=(t.size, n)).T * np.sqrt(dt)).T
        W = np.cumsum(dW, axis=0) 
        return np.exp(self.sigma * W.T + (self.mu - self.sigma**2 / 2) * t).T

def american_put_option_price(simulated_paths, strike_price, discount_rate, time_steps):
    option_values = np.maximum(strike_price - simulated_paths, 0)  # Payoff of the option
    option_prices = np.zeros_like(option_values)

    # Initialize option prices at maturity (last time step)
    option_prices[-1, :] = option_values[-1, :]

    for t in range(time_steps - 2, -1, -1):
        intrinsic_value = np.maximum(strike_price - simulated_paths[t, :], 0)
        continuation_value = np.exp(-discount_rate) * option_prices[t + 1, :]

        option_prices[t, :] = np.maximum(intrinsic_value, continuation_value)

    return option_prices[0, :]

# Parameters
initial_stock_price = 36
strike_price = 40
interest_rate = 0.06
sigma = 0.2
num_paths = 10**4
num_time_steps_per_year = 50  # Number of exercise opportunities per year
total_time_years = 2  # Time to maturity

# Calculate the total number of time steps
num_time_steps = num_time_steps_per_year * total_time_years

# Time steps for simulation
time_steps = np.linspace(0, total_time_years, num_time_steps + 1)

# Simulate stock price paths
gbm = GeometricBrownianMotion(mu=interest_rate, sigma=sigma)
simulated_paths = gbm.simulate(time_steps, num_paths)
simulated_paths *= initial_stock_price

# Calculate option price
option_price = np.mean(american_put_option_price(simulated_paths, strike_price, interest_rate, num_time_steps))

print("American Put Option Price:", option_price)
