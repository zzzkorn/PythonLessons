"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

1-я строка:
3
3
3
3
2-я строка:
3
3
3
3
3-я строка:
3
3
3
3
4-я строка:
3
3
3
3
5-я строка:
3
3
3
3

[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
"""
from functools import reduce


# Через рекурсию
# def task8(num_string, num_strings):
#     return_list = list()
#     input_string = list()
#     if num_string > num_strings:
#         return 0
#     else:
#         print(f'{num_string + 1}-я строка:')
#         for i in range(5):
#             input_string.append(int(input()))
#         input_string.append(reduce(lambda x, y: x + y, input_string))
#         return_list.append(input_string)
#     return input_string.append(task8(num_string + 1, num_strings))
#
#
# RESULT = task8(0, 4)
# for i in range(len(RESULT)):
#     print(RESULT[i + 1])


# Через цикл
NUMBER_OF_STRING = 5
INPUT_STRINGS = list()
COUNT = 0
while COUNT < NUMBER_OF_STRING:
    INPUT_STRING = list()
    print(f'{COUNT + 1}-я строка:')
    for i in range(5):
        INPUT_STRING.append(int(input()))
    INPUT_STRING.append(reduce(lambda x, y: x + y, INPUT_STRING))
    INPUT_STRINGS.append(INPUT_STRING)
    COUNT += 1
print()
for i in range(len(INPUT_STRINGS)):
    print(INPUT_STRINGS[i])
