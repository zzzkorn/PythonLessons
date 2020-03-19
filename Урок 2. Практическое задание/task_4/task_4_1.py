"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
try:
    print('Введите количество элементов:', end=" ")
    NUMBER_OF_ELEMENTS = int(input())
    RESULT = 0
    PARAM = 1
    print(f'Количество элементов - {NUMBER_OF_ELEMENTS},', end=" ")
    while NUMBER_OF_ELEMENTS:
        RESULT += PARAM
        PARAM /= -2
        NUMBER_OF_ELEMENTS -= 1
    print(f'их сумма - {RESULT}')
except ValueError:
    print('Ошибка ввода числа')