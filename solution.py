import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 680977959 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = (1 + p) / 2
    n = len(x)
    xx = x * x
    k = n / (25 * sum(xx))
    fp = norm.ppf(alpha)

    return k / (1 + fp), k / (1 - fp)
