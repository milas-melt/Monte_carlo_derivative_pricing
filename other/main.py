from scipy.stats.distributions import lognorm
import numpy as np

np.random.seed(123456)

class GeometricBrownianMotion:
    def __init__(self, mu: float = 0.0, sigma: float = 1.0):
        self.mu = mu
        self.sigma = sigma

    def simulate(self, t, n):
        """
        Simulate `n` paths of the Geometric Brownian Motion.
        t: np.array
        n: int

        returns: np.array
        """
        dt = np.concatenate((t[0:1], np.diff(t)))
        # dW = np.random.normal(size=(n, m)) * np.sqrt(dt)
        dW = (np.random.normal(size=(t.size, n)).T * np.sqrt(dt)).T
        W = np.cumsum(dW, axis=0)
        return np.exp(self.sigma * W.T + (self.mu - self.sigma**2 / 2) * t).T

    def distribution(self, t):
        """
        Return the distribution of the Geometric Brownian Motion at time `t`.
        t: float

        returns: scipy.stats.lognorm
        """
        mu_t = (self.mu - self.sigma**2 / 2) * t
        sigma_t = self.sigma * np.sqrt(t)
        return lognorm(scale=np.exp(mu_t), s=sigma_t)
    

# Model parameters
t = np.linspace(0, 5, 100)  # timegrid for simulation
r = 0.01  # riskless rate
sigma = 0.15  # annual volatility of underlying
n = 100  # number of simulated paths

# Simulate the underlying
gbm = GeometricBrownianMotion(mu=r, sigma=sigma)
x = gbm.simulate(t, n)  # x.shape == (t.size, n)

# Payoff (exercise) function
strike = 0.95

def put_payoff(spot):
    return np.maximum(strike - spot, 0.0)

# Discount factor function
def constant_rate_df(t_from, t_to):
    return np.exp(-r * (t_to - t_from))

# Approximation of continuation value
def fit_quadratic(x, y):
    return np.polynomial.Polynomial.fit(x, y, 2, rcond=None)

# Selection of paths to consider for exercise
# (and continuation value approxmation)
def itm(payoff, spot):
    return payoff > 0

def LSMC(X, t, df, fit, exercise_payoff, itm_select=None):
    cashflow = exercise_payoff(X[-1, :])
    for i in reversed(range(1, X.shape[0] - 1)):
        cashflow = cashflow * df(t[i], t[i + 1])
        x = X[i, :]
        exercise = exercise_payoff(x)
        itm = itm_select(exercise, x) if itm_select else np.full(x.shape, True)
        fitted = fit(x[itm], cashflow[itm])
        continuation = fitted(x)
        ex_idx = itm & (exercise > continuation)
        cashflow[ex_idx] = exercise[ex_idx]
    return cashflow.mean(axis=0) * df(t[0], t[1])

# Run valuation of American put option
npv_american = LSMC(x, t, constant_rate_df,
                                  fit_quadratic, put_payoff, itm)

# European put option for comparison
npv_european = constant_rate_df(t[0], t[-1]) * put_payoff(x[-1]).mean()

# print results
print(f"npv_american: {npv_american}")
print(f"npv_european: {npv_european}")
