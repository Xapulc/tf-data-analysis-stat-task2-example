import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 462449141

def solution(p: float, x: np.array) -> tuple:
    const = 0.059
    x -= const
    return max(max(x), 2 * (x.mean() - np.sqrt(np.var(x)) * norm.ppf(1 - p / 2) / np.sqrt(len(x)))) + const, \
    max(max(x), 2 * (x.mean() - np.sqrt(np.var(x)) * norm.ppf(p / 2) / np.sqrt(len(x)))) + const
