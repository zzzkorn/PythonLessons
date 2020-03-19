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

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def task8(count_numbers, search_number):
    if count_numbers <= 0:
        return 0
    else:
        print('Число:', end=' ')
        search_count = 0
        try:
            number = int(input())
            count_numbers -= 1
            while number:
                a = number % 10
                if a == search_number:
                    search_count += 1
                number //= 10
        except ValueError:
            print('Ошибка ввода числа')
        return search_count + task8(count_numbers, search_number)


try:
    print('Сколько будет чисел? -', end=' ')
    COUNT_NUMBERS = int(input())
    print('Какую цифру считать? -', end=' ')
    SEARCH_NUMBER = int(input())
    print(
        f'Было введено {task8(COUNT_NUMBERS, SEARCH_NUMBER)} цифр {SEARCH_NUMBER}')
except ValueError:
    print('Ошибка ввода числа')