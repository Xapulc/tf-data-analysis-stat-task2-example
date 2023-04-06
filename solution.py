import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 285518472 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    df = 2 * x.shape[0]
    r2 = np.dot(x, x) ** 0.5
    z1 = chi2.ppf(alpha/2, df)
    z2 = chi2.ppf(1-alpha/2, df)
    left = r2 / (5 * z2**0.5)
    right = r2 / (5 * z1**0.5)
    return left, right
