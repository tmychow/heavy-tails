# https://www.benkuhn.net/outliers/

import numpy as np

def simulate_log_normal(mu, sigma, n, m):
    """Simulate a log-normal distribution."""
    initial_samples = np.random.lognormal(mean=mu, sigma=sigma, size=n)
    threshold = np.max(initial_samples) * 10
    new_samples = np.random.lognormal(mean=mu, sigma=sigma, size=m)
    return int(any(new_samples > threshold))

def monte_carlo(mu, sigma, n, m, num_trials):
    """Run a simulation for a set of parameters."""
    results = []
    for i in range(num_trials):
        results.append(simulate_log_normal(mu, sigma, n, m))
    return np.mean(results)

print(monte_carlo(0, 1, 400, 600, 10000))