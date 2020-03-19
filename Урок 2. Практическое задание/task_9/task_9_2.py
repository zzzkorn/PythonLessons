"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def task9(count):
    if count <= 0:
        return 0, 0
    else:
        print('Введите число:', end=' ')
        num = int(input())
        copy = num
        num_sum = 0
        while copy:
            a = copy % 10
            num_sum += a
            copy //= 10
        s, n = task9(count - 1)
        if s < num_sum:
            return num_sum, num
        else:
            return s, n


try:
    print('Введите количество чисел:', end=' ')
    COUNT_NUMBERS = int(input())
    MAX_SUM, MAX_NUMBER = task9(COUNT_NUMBERS)
    print(
        f'Наибольшее число по сумме цифр: {MAX_NUMBER}, сумма его цифр: {MAX_SUM}')
except ValueError:
    print('Ошибка ввода числа')
