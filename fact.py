from functools import lru_cache

# Рекурсивный факториал с мемоизацией
@lru_cache(maxsize=None)
def factorial_memo(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial_memo(n - 1)

# Рекурсивный факториал без мемоизации
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)
