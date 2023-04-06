import numpy as np

from scipy.stats import gamma

chat_id = 756835435  # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = x.shape[0]
    alpha = 1 - p
    beta = 1 + p
    loc = x.mean()
    return loc / 2 - 0.25 + gamma.ppf(alpha / 2, n) / (2 * n), \
           loc / 2 - 0.25 + gamma.ppf(beta / 2, n) / (2 * n)
