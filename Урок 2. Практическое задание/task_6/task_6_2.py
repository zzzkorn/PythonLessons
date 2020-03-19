"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from random import randint


def task6(counter, param):
    try:
        print('Угадайте загаданое число:')
        num = int(input())
        if param == num or counter == 1:
            print(f'Загаданное число: {param}')
            return 1
        elif param < num:
            print('Меньше', end=', ')
        elif num < param:
            print('Больше', end=', ')
        counter -= 1
        print(f'осталось попыток {counter}')
    except ValueError:
        print('Ошибка ввода числа')
    task6(counter, param)


task6(10, randint(0, 100))