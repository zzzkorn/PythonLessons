"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""
import random
from functools import reduce
VALUES = {
    'MinValue': 0,
    'MaxValue': 0,
    'PositionOfMaxValue': 0,
    'PositionOfMinValue': 0
}
# Нахождение минимального и максимального значения
MASSIVE = [random.randint(-100, 100) for x in range(5)]
VALUES['MinValue'] = reduce(min, MASSIVE)
VALUES['PositionOfMinValue'] = MASSIVE.index(VALUES['MinValue'])
VALUES['MaxValue'] = reduce(max, MASSIVE)
VALUES['PositionOfMaxValue'] = MASSIVE.index(VALUES['MaxValue'])
# Первая часть вывода
print(
    'В данном массиве чисел максимальное число {} стоит на'.format(
        VALUES['MaxValue']))
print('{} позиции, а минимальное число {} стоит на {} позиции' .format(
    VALUES['PositionOfMaxValue'], VALUES['MinValue'], VALUES['PositionOfMinValue']))
print(MASSIVE)
print('Заменяем их')
# Замена чисел
MASSIVE[VALUES['PositionOfMinValue']], VALUES['PositionOfMinValue'], MASSIVE[VALUES['PositionOfMaxValue']], \
    VALUES['PositionOfMaxValue'] = [MASSIVE[VALUES['PositionOfMaxValue']], VALUES['PositionOfMaxValue'],
                                    MASSIVE[VALUES['PositionOfMinValue']], VALUES['PositionOfMinValue']]
print(
    'В данном массиве чисел максимальное число {} стоит на'.format(
        VALUES['MaxValue']))
print('{} позиции, а минимальное число {} стоит на {} позиции' .format(
    VALUES['PositionOfMaxValue'], VALUES['MinValue'], VALUES['PositionOfMinValue']))
print(MASSIVE)
