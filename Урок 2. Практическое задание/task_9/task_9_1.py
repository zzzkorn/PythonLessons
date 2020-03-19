"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
try:
    print('Введите количество чисел:', end=' ')
    COUNT_NUMBERS = int(input())
    MAX_NUMBER, MAX_SUM = 0, 0
    while COUNT_NUMBERS:
        try:
            print('Введите очередное число:', end=' ')
            NUMBER = int(input())
            COPY, SUM = NUMBER, 0
            COUNT_NUMBERS -= 1
            while COPY:
                A = COPY % 10
                SUM += A
                COPY //= 10
            if SUM > MAX_SUM:
                MAX_SUM, MAX_NUMBER = SUM, NUMBER
        except ValueError:
            print('Ошибка ввода числа')
    print(
        f'Наибольшее число по сумме цифр: {MAX_NUMBER}, сумма его цифр:{MAX_SUM}')
except ValueError:
    print('Ошибка ввода числа')
