"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from collections import deque


class UserNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        try:
            return UserNumber.get_16_to_list(
                int(self.number, 16) + int(other.number, 16))
        except ValueError:
            print("Ошибка ввода 16-ричного числа")

    def __mul__(self, obj):
        try:
            return UserNumber.get_16_to_list(
                int(self.number, 16) * int(obj.number, 16))
        except ValueError:
            print("Ошибка ввода 16-ричного числа")

    @staticmethod
    def get_one_number_16_to_str(number):
        if number < 10:
            return str(number)
        elif number == 10:
            return 'A'
        elif number == 11:
            return 'B'
        elif number == 12:
            return 'C'
        elif number == 13:
            return 'D'
        elif number == 14:
            return 'E'
        elif number == 15:
            return 'F'

    @staticmethod
    def get_16_to_list(number):
        return_list = deque()
        while number:
            return_list.appendleft(UserNumber.get_one_number_16_to_str(number % 16))
            number = number // 16
        return return_list


def task_2_class():
    num_1 = UserNumber(input('Введите первое 16-ричное число: '))
    num_2 = UserNumber(input('Введите второе 16-ричное число: '))
    print(f'Сумма: {num_1 + num_2}')
    print(f'Произведение: {num_1 * num_2}')


task_2_class()
