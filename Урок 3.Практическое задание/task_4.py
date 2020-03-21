"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
import random
import operator

DICT = {}
MASSIVE = [random.randint(-1, 2) for i in range(10)]
print(MASSIVE)
for i in set(MASSIVE):
    DICT[i] = len(list(filter(lambda x: x == i, MASSIVE)))
print(DICT)
print(
    f'Чаще всего встречающееся число: {max(DICT.items(), key=operator.itemgetter(1))[0]}')
