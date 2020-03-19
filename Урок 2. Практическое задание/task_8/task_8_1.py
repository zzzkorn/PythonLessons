"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
print('Сколько будет чисел? -', end=' ')
COUNT_NUMBERS = int(input())
print('Какую цифру считать? -', end=' ')
SEARCH_NUMBER = int(input())
COUNT_SEARCH_NUMBER = 0
COUNT = 1
while COUNT_NUMBERS:
    print(f'Число {COUNT}:', end=' ')
    try:
        INPUT_NUMBER = int(input())
        while INPUT_NUMBER:
            A = INPUT_NUMBER % 10
            if A == SEARCH_NUMBER:
                COUNT_SEARCH_NUMBER += 1
            INPUT_NUMBER //= 10
        COUNT_NUMBERS -= 1
        COUNT += 1
    except ValueError:
        print('Ошибка ввода числа')
print(f'Было введено {COUNT_SEARCH_NUMBER} цифр {SEARCH_NUMBER}')
