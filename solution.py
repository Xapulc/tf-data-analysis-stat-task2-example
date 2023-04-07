import pandas as pd
import numpy as np
from scipy.stats import t

chat_id = 1399245853 

def symmetric_confidence_interval(alpha, measurements):
    n = measurements.size
    x_mean = np.mean(measurements)
    s = np.sqrt(np.var(measurements, ddof=1))
    t_alpha_2 = t.ppf(1 - alpha/2, df=n-1)
    delta = t_alpha_2 * s / np.sqrt(n)
    left_boundary = x_mean - delta
    right_boundary = x_mean + delta
    return (left_boundary, right_boundary)
