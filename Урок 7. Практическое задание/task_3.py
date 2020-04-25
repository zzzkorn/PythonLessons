"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import statistics
import random
import copy
import timeit


def get_statistics_median(origin_list):
    return statistics.median(origin_list)


def get_user_median(input_list):
    count = len(input_list) // 2 + 1
    while count:
        max_value = input_list[0]
        for i in input_list:
            if i > max_value:
                max_value = i
        input_list.remove(max_value)
        count -= 1
    return max_value


def input_test():
    try:
        num_of_elements = int(input('Введите число элементов: '))
        origin_list = [random.randint(-100, 100)
                       for _ in range(num_of_elements)]
        origin_list_2 = copy.deepcopy(origin_list)
        origin_list_3 = sorted(copy.deepcopy(origin_list))
        print(f'Исходный - {origin_list}')
        print(get_statistics_median(origin_list))
        print(get_user_median(origin_list_2))
        print(origin_list_3)
    except ValueError:
        print('Ошибка ввода числа элементов')


def test_for_timeit(number_of_elements):
    origin_list = [random.randint(-100, 100)
                   for _ in range(number_of_elements)]
    get_user_median(origin_list)


LIST_0 = [random.randint(-100, 100) for _ in range(7)]
LIST_1 = [random.randint(-100, 100) for _ in range(77)]
LIST_2 = [random.randint(-100, 100) for _ in range(777)]
print(
    f'stat. 7: '
    f'{round(timeit.timeit("get_statistics_median(LIST_0)", setup="from __main__ import get_statistics_median, LIST_0", number=1000), 4)}'
    f',сек 77: '
    f'{round(timeit.timeit("get_statistics_median(LIST_1)", setup="from __main__ import get_statistics_median, LIST_1", number=1000), 4)}'
    f',сек 777: '
    f'{round(timeit.timeit("get_statistics_median(LIST_2)", setup="from __main__ import get_statistics_median, LIST_2", number=1000), 4)}'
    f',сек')
COUNT_0 = 7
COUNT_1 = 77
COUNT_2 = 777
print(
    f'user. 7: '
    f'{round(timeit.timeit("test_for_timeit(COUNT_0)", setup="from __main__ import test_for_timeit, COUNT_0", number=1000), 4)}'
    f',сек 77: '
    f'{round(timeit.timeit("test_for_timeit(COUNT_1)", setup="from __main__ import test_for_timeit, COUNT_1", number=1000), 4)}'
    f',сек 777: '
    f'{round(timeit.timeit("test_for_timeit(COUNT_2)", setup="from __main__ import test_for_timeit, COUNT_2", number=1000), 4)}'
    f',сек')
