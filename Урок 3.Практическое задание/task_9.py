"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""
import random
from functools import reduce


MIN_VALUES = []
MATRIX = []
try:
    print(f'Задайте количество строк в матрице:', end=' ')
    NUMBER_OF_LINES = int(input())
    print(f'Задайте количество столбцов в матрице:', end=' ')
    NUMBER_OF_COLUMNS = int(input())
    # Формирование матрицы
    MATRIX = [[random.randint(0, 100) for i in range(NUMBER_OF_LINES)]
              for i in range(NUMBER_OF_COLUMNS)]
    # Вывод матрицы
    for i in range(NUMBER_OF_LINES):
        for j in range(NUMBER_OF_COLUMNS):
            print(MATRIX[j][i], end=' ')
        print()
    # Формирование списка минимальных значений по столбцам
    for i in MATRIX:
        MIN_VALUES.append(reduce(min, i))
    # Вывод результата
    print(f'{MIN_VALUES} минимальные значения по столбцам')
    print(
        f'Максимальное среди них = {reduce(max, MIN_VALUES)}')
except ValueError:
    print('Value Error')
