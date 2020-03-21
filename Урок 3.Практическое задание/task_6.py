"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""
import random
from functools import reduce
VALUES = {
    'MinValue': 0,
    'MaxValue': 0,
    'PositionOfMaxValue': 0,
    'PositionOfMinValue': 0
}
SUM_BETWEEN_ELEMENTS = 0
FIRST_INDEX = 0
SECOND_INDEX = 0
try:
    print('Введите количество элементов в массиве:', end=' ')
    NUM_OF_ELEMENTS = int(input())
    MASSIVE = [random.randint(0, 10) for x in range(NUM_OF_ELEMENTS)]
    # Нахождение минимального и максимального значения
    # Свой вариант min
    VALUES['MinValue'] = reduce(lambda x, y: x if x < y else y, MASSIVE)
    VALUES['PositionOfMinValue'] = MASSIVE.index(VALUES['MinValue'])
    # max
    VALUES['MaxValue'] = reduce(lambda x, y: x if x > y else y, MASSIVE)
    VALUES['PositionOfMaxValue'] = MASSIVE.index(VALUES['MaxValue'])
    # Нахождение суммы
    if VALUES['PositionOfMinValue'] > VALUES['PositionOfMaxValue']:
        FIRST_INDEX, SECOND_INDEX = VALUES['PositionOfMaxValue'] + \
            1, VALUES['PositionOfMinValue']
    else:
        FIRST_INDEX, SECOND_INDEX = VALUES['PositionOfMinValue'] + \
            1, VALUES['PositionOfMaxValue']
    for i in range(FIRST_INDEX, SECOND_INDEX):
        SUM_BETWEEN_ELEMENTS += MASSIVE[i]
    # Вывод результатов
    print(f'Массив:{MASSIVE}')
    print(
        'Сумма элементов между минимальным ({})  и максимальным ({}) элементами: {}'.format(
            VALUES['MinValue'],
            VALUES['MaxValue'],
            SUM_BETWEEN_ELEMENTS))
except ValueError:
    print('Value Error')
