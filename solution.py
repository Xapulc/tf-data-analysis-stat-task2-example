import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1007460447 # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    x_mean = x.mean()
    x_var = np.var(x)
    
    # Calculate mean and variance of generated significance level
    a = 0.032
    b_mean = 2*x_mean - a
    b_var = (b_mean - a)**2 / 12
    
    # Calculate confidence interval for upper bound b
    loc = (a + b_mean) / 2
    scale = np.sqrt(b_var) / np.sqrt(n)
    return loc - scale * norm.ppf(1 - alpha / 2), loc - scale * norm.ppf(alpha / 2)

