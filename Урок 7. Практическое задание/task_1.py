"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import timeit
import random


def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list) - n):
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
        n += 1
    return orig_list


def bubble_modify_0(orig_list):
    for count in range(1, len(orig_list)):
        switch_counter = 0
        for i in range(len(orig_list) - count):
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1], switch_counter = orig_list[i +
                                                                           1], orig_list[i], switch_counter + 1
        if switch_counter == 0:
            break
    return orig_list


def memorize(func):
    def wrapped(first, second, memory={}):
        r = memory.get((first, second))
        if r is None:
            r = func(first, second)
            memory[(first, second)] = r
        return r
    return wrapped


@memorize
def compare_two_numbers(first, second):
    return True if first < second else False


def bubble_modify_1(orig_list):
    for count in range(1, len(orig_list)):
        switch_counter = 0
        for i in range(len(orig_list) - count):
            if compare_two_numbers(orig_list[i], orig_list[i + 1]):
                orig_list[i], orig_list[i + 1], switch_counter = orig_list[i +
                                                                           1], orig_list[i], switch_counter + 1
        if switch_counter == 0:
            break
    return orig_list


LIST_0 = [random.randint(-100, 100) for _ in range(10)]
LIST_1 = [random.randint(-100, 100) for _ in range(100)]
LIST_2 = [random.randint(-100, 100) for _ in range(1000)]
print(
    f'standart. 10: '
    f'{round(timeit.timeit("bubble_sort(LIST_0)", setup="from __main__ import bubble_sort, LIST_0", number=1000), 4)}'
    f',сек 100: '
    f'{round(timeit.timeit("bubble_sort(LIST_1)", setup="from __main__ import bubble_sort, LIST_1", number=1000), 4)}'
    f',сек 1000: '
    f'{round(timeit.timeit("bubble_sort(LIST_2)", setup="from __main__ import bubble_sort, LIST_2", number=1000), 4)}'
    f',сек')
LIST_0 = [random.randint(-100, 100) for _ in range(10)]
LIST_1 = [random.randint(-100, 100) for _ in range(100)]
LIST_2 = [random.randint(-100, 100) for _ in range(1000)]
print(
    f'modify_0. 10: '
    f'{round(timeit.timeit("bubble_modify_0(LIST_0)", setup="from __main__ import bubble_modify_0, LIST_0", number=1000), 4)}'
    f',сек 100: '
    f'{round(timeit.timeit("bubble_modify_0(LIST_1)", setup="from __main__ import bubble_modify_0, LIST_1", number=1000), 4)}'
    f',сек 1000: '
    f'{round(timeit.timeit("bubble_modify_0(LIST_2)", setup="from __main__ import bubble_modify_0, LIST_2", number=1000), 4)}'
    f',сек')
LIST_0 = [random.randint(-100, 100) for _ in range(10)]
LIST_1 = [random.randint(-100, 100) for _ in range(100)]
LIST_2 = [random.randint(-100, 100) for _ in range(1000)]
print(
    f'modify_1. 10: '
    f'{round(timeit.timeit("bubble_modify_1(LIST_0)", setup="from __main__ import bubble_modify_1, LIST_0", number=1000), 4)}'
    f',сек 100: '
    f'{round(timeit.timeit("bubble_modify_1(LIST_1)", setup="from __main__ import bubble_modify_1, LIST_1", number=1000), 4)}'
    f',сек 1000: '
    f'{round(timeit.timeit("bubble_modify_1(LIST_2)", setup="from __main__ import bubble_modify_1, LIST_2", number=1000), 4)}'
    f',сек')


"""Для проверки работоспособности пузырькового алгоритма"""
print('Проверка работоспособности алгоритмов:')
ORIGIN_LIST = [random.randint(-100, 100) for _ in range(10)]
print(
    f'Стандартный пузырьковый алгоритм. Входной массив: {ORIGIN_LIST}, отсортированый: {bubble_sort(ORIGIN_LIST)}')
ORIGIN_LIST = [random.randint(-100, 100) for _ in range(10)]
print(
    f'modify_0 алгоритм. Входной массив: {ORIGIN_LIST}, отсортированый: {bubble_modify_0(ORIGIN_LIST)}')
ORIGIN_LIST = [random.randint(-100, 100) for _ in range(10)]
print(
    f'modify_1 алгоритм. Входной массив: {ORIGIN_LIST}, отсортированый: {bubble_modify_1(ORIGIN_LIST)}')

"""
    Выводы:
    standart. 10: 0.0111,сек    100: 0.7179,сек     1000: 70.2344,сек
    modify_0. 10: 0.0022,сек    100: 0.0158,сек     1000: 0.2884,сек
    modify_1. 10: 0.004,сек     100: 0.0425,сек     1000: 0.6828,сек
    
    После доработки (modify_0) алгоритм стал выполняться выстрее.
    Для дальнейшей доработки алгоритма я решил воспользоваться мемоизацией (modify_1). Так как в 
    данном аглоритме  мы постоянно сравниваем 2 числа я решил записывать результаты сравнения в память
    и считывать результаты сравнения чисел из памяти. В результате алгоритм стал выполняться медленее 
    так как процесс сравнения 2 чисел выполняется быстрее чем процесс считывания результата сравнения
    из памяти.
    
    Проверка работоспособности алгоритмов:
    Стандартный пузырьковый алгоритм. Входной массив: [-41, 6, 59, -12, 39, -2, -61, 83, 26, -41], 
    отсортированый: [83, 59, 39, 26, 6, -2, -12, -41, -41, -61]
    modify_0 алгоритм. Входной массив: [28, 22, -97, 51, 42, -84, -12, 67, -88, 45], 
    отсортированый: [67, 51, 45, 42, 28, 22, -12, -84, -88, -97]
    modify_1 алгоритм. Входной массив: [-80, 88, 78, 29, 50, -26, 31, -45, 24, 5], 
    отсортированый: [88, 78, 50, 31, 29, 24, 5, -26, -45, -80]
"""