"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def task4(number_of_elements, element):
    result = 0
    result += element
    if number_of_elements <= 0:
        return 0
    else:
        number_of_elements -= 1
        element /= -2
        result += task4(number_of_elements, element)
        return result


try:
    print('Введите количество элементов:', end=" ")
    NUMBER_OF_ELEMENTS = int(input())
    print(f'Количество элементов - {NUMBER_OF_ELEMENTS},их сумма - {task4(NUMBER_OF_ELEMENTS, 1)}')
except ValueError:
    print('Ошибка ввода числа')
