"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
import random
from functools import reduce
MIN_VALUES = list()
MASSIVE = [random.randint(-100, 100) for x in range(10)]
# MASSIVE = [-100, -100, 8, 7]
print(f'Исходный массив: {MASSIVE}')
MIN_VALUES.append(reduce(lambda x, y: x if x < y else y, MASSIVE))
MASSIVE.remove(MIN_VALUES[0])
MIN_VALUES.append(reduce(lambda x, y: x if x < y else y, MASSIVE))
if MIN_VALUES[0] == MIN_VALUES[1]:
    print(
        f'Наименьший элемент: {MIN_VALUES[0]}, встречается в этом массиве 2 раза')
else:
    print(
        f'Наименьший элемент: {MIN_VALUES[0]}, встречается в этом массиве 1 раз')
    print(f'Второй наименьший элемент:{MIN_VALUES[1]}')
