import numpy as np
from scipy.stats.distributions import lognorm

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
    

    