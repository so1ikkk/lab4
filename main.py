import timeit
import matplotlib.pyplot as plt
from functools import lru_cache
import random


@lru_cache(maxsize=None)
def fact_recursive_memo(n: int) -> int:
    """
    Рекурсивный факториал с мемоизацией.

    Аргументы:
    n -- целое число, для которого вычисляется факториал

    Возвращает:
    целое число, факториал числа n
    """
    if n == 0:
        return 1
    return n * fact_recursive_memo(n - 1)


def fact_recursive_no_memo(n: int) -> int:
    """
    Рекурсивный факториал без мемоизации.

    Аргументы:
    n -- целое число, для которого вычисляется факториал

    Возвращает:
    целое число, факториал числа n
    """
    if n == 0:
        return 1
    return n * fact_recursive_no_memo(n - 1)


@lru_cache(maxsize=None)
def fact_iterative_memo(n: int) -> int:
    """
    Нерекурсивный факториал с мемоизацией.

    Аргументы:
    n -- целое число, для которого вычисляется факториал

    Возвращает:
    целое число, факториал числа n
    """
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def fact_iterative_no_memo(n: int) -> int:
    """
    Нерекурсивный факториал без мемоизации.

    Аргументы:
    n -- целое число, для которого вычисляется факториал

    Возвращает:
    целое число, факториал числа n
    """
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def benchmark(func, n: int, number: int = 1, repeat: int = 5) -> float:
    """
    Бенчмарк для измерения времени выполнения функции.

    Измеряет среднее время выполнения функции func(n) с использованием timeit.repeat.
    Возвращает минимальное время из нескольких повторений.

    Аргументы:
    func -- функция, время выполнения которой нужно замерить
    n -- аргумент, передаваемый функции func
    number -- количество повторений для одного замера
    repeat -- количество замеров

    Возвращает:
    минимальное время выполнения функции func(n) среди всех замеров
    """
    times = timeit.repeat(lambda: func(n), number=number, repeat=repeat)
    return min(times)


def main():
    """
    Главная функция, которая выполняет бенчмарк для различных вариантов вычисления факториала
    и строит графики для сравнения производительности.
    
    """
    random.seed(42)
    test_data = list(range(10, 300, 10))

    # Результаты для разных функций
    res_recursive_memo = []
    res_iterative_memo = []
    res_recursive_no_memo = []
    res_iterative_no_memo = []

    # Заполнение данных
    for n in test_data:
        # Рекурсивный факториал с мемоизацией
        res_recursive_memo.append(benchmark(fact_recursive_memo, n, repeat=5, number=1000))

        # Рекурсивный факториал без мемоизации
        res_recursive_no_memo.append(benchmark(fact_recursive_no_memo, n, repeat=5, number=1000))

        # Нерекурсивный факториал с мемоизацией
        res_iterative_memo.append(benchmark(fact_iterative_memo, n, repeat=5, number=1000))

        # Нерекурсивный факториал без мемоизации
        res_iterative_no_memo.append(benchmark(fact_iterative_no_memo, n, repeat=5, number=1000))

    # Визуализация для первого сравнения (lru_cache РекФакт и НРекФакт)
    plt.plot(test_data, res_recursive_memo, label="РекФакт с мемоизацией", color='blue')
    plt.plot(test_data, res_iterative_no_memo, label="НРекФакт без мемоизации", color='green')
    plt.xlabel("n")
    plt.ylabel("Время (сек.)")
    plt.title("Сравнение: РекФакт с мемоизацией vs НРекФакт без мемоизации")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Визуализация для второго сравнения (n/a optimization РекФакт и НРекФакт)
    plt.plot(test_data, res_recursive_no_memo, label="РекФакт без мемоизации", color='red')
    plt.plot(test_data, res_iterative_no_memo, label="НРекФакт без мемоизации", color='purple')
    plt.xlabel("n")
    plt.ylabel("Время (сек.)")
    plt.title("Сравнение: РекФакт без мемоизации vs НРекФакт без мемоизации")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Визуализация для третьего сравнения (РекФакт с мемоизацией vs РекФакт без мемоизации)
    plt.plot(test_data, res_recursive_memo, label="РекФакт с мемоизацией", color='blue')
    plt.plot(test_data, res_recursive_no_memo, label="РекФакт без мемоизации", color='red')
    plt.xlabel("n")
    plt.ylabel("Время (сек.)")
    plt.title("Сравнение: РекФакт с мемоизацией vs РекФакт без мемоизации")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Визуализация для четвёртого сравнения (НРекФакт с мемоизацией и без)
    plt.plot(test_data, res_iterative_memo, label="НРекФакт с мемоизацией", color='blue')
    plt.plot(test_data, res_iterative_no_memo, label="НРекФакт без мемоизации", color='green')
    plt.xlabel("n")
    plt.ylabel("Время (сек.)")
    plt.title("НРекФакт: С мемоизацией vs Без мемоизации")
    plt.legend()
    plt.grid(True)
    plt.show()

print(f"{timeit.timeit('fact.factorial_memo(10)', setup='import fact')} с мемо")
print(f"{timeit.timeit('fact.factorial(10)', setup='import fact')} без мемо")


if __name__ == "__main__":
    main()

