"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
from random import randint

COUNT = 10
PARAM = randint(0, 100)
while COUNT:
    try:
        COUNT -= 1
        print('Угадайте загаданое число:')
        NUM = int(input())
        if PARAM == NUM or COUNT == 0:
            print(f'Загаданное число: {PARAM}')
            break
        elif PARAM < NUM:
            print('Меньше', end=', ')
        elif PARAM > NUM:
            print('Больше', end=', ')
        print(f'осталось попыток {COUNT}')
    except ValueError:
        print('Ошибка ввода числа')