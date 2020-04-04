"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit


def get_prime_number_by_index(index):
    lst = []
    n = 3
    while len(lst) != index + 1:
        for i in range(2, n):
            for j in lst:
                if i % j == 0:
                    break
            else:
                lst.append(i)
        n += 1
    return f'{index} по счету простое число - {lst[index]}'


def get_prime_number_by_index_with_re(index):
    lst = [2]
    while len(lst) < index + 1:
        n = lst[-1]
        while True:
            n += 1
            for i in lst:
                if n % i == 0:
                    break
            else:
                lst.append(n)
                break
    return f'{index} по счету простое число - {lst[index]}'


"""Время выполнения 0.0110852 секунд"""
print(
    timeit.timeit(
        "get_prime_number_by_index(10)",
        setup="from __main__ import get_prime_number_by_index",
        number=100))
"""Время выполнения 8.184835000000001 секунд"""
print(
    timeit.timeit(
        "get_prime_number_by_index(100)",
        setup="from __main__ import get_prime_number_by_index",
        number=100))
"""Время выполнения 0.0008855000000007607 секунд"""
print(
    timeit.timeit(
        "get_prime_number_by_index_with_re(10)",
        setup="from __main__ import get_prime_number_by_index_with_re",
        number=100))
"""Время выполнения 0.03911060000000077 секунд"""
print(
    timeit.timeit(
        "get_prime_number_by_index_with_re(100)",
        setup="from __main__ import get_prime_number_by_index_with_re",
        number=100))
"""Время выполнения 3.497330700000001 секунд"""
print(
    timeit.timeit(
        "get_prime_number_by_index_with_re(1000)",
        setup="from __main__ import get_prime_number_by_index_with_re",
        number=100))

"""
    Выводы:
    - алгоритм без решета Эратосфена имеет квадратичную сложность O(n**2)
    - алгоритм с решетом Эратосфена имеет линейно-логарифмическую сложность O(n*log(n)), что отчетливо видно 
    по времени выполнения при нахождении 100 и 1000 простого числа 
"""