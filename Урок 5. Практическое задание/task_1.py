"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import namedtuple
from collections import defaultdict
from collections import Counter
from functools import reduce


def fill_enterprises_namedtuple(enterprises, number_of_enterprises):
    if number_of_enterprises:
        try:
            name = input("Введите название предприятия: ")
            quarterly_profit = list(map(int, str(input(
                "Через пробел введите прибыль данного предприятия за каждый "
                "квартал(Всего 4 квартала): ")).split(' ')))
            if len(quarterly_profit) == 4:
                year_profit = sum(quarterly_profit)
                enterprise = namedtuple('enterprise',
                                        'name quarterly_profit year_profit')
                ent = enterprise(
                    name=name,
                    quarterly_profit=quarterly_profit,
                    year_profit=year_profit
                )
                enterprises.append(ent)
                return fill_enterprises_namedtuple(
                    enterprises, number_of_enterprises - 1)
            else:
                print('Должна быть введена прибыль за 4 квартала, попробуйте еще раз!')
                return fill_enterprises_namedtuple(
                    enterprises, number_of_enterprises)
        except ValueError:
            print('Ошибка ввода, попробуйте еще раз!')
            return fill_enterprises_namedtuple(
                enterprises, number_of_enterprises)
    else:
        return sum(i.year_profit for i in enterprises) / len(enterprises)
        # return reduce(lambda x, y: x.year_profit + y.year_profit,
        # enterprises) / len(enterprises) - НЕ РАБОТАЕТ!!!!


def fill_enterprises_default_dict(enterprises, number_of_enterprises):
    if number_of_enterprises:
        try:
            name = input("Введите название предприятия: ")
            print(
                "Введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ")
            for i in range(1, 5):
                profit = (name, int(input(f"{i} квартал: ")))
                enterprises.append(profit)
            return fill_enterprises_default_dict(
                enterprises, number_of_enterprises - 1)
        except ValueError:
            print('Ошибка ввода, попробуйте еще раз!')
            return fill_enterprises_default_dict(
                enterprises, number_of_enterprises)
    else:
        ent = defaultdict(list)
        for k, v in enterprises:
            ent[k].append(v)
        print(ent)
        averaged_profit = sum(ent.values()) / len(ent)
        return ent, averaged_profit


def fill_enterprises_counter(enterprises, number_of_enterprises):
    if number_of_enterprises:
        try:
            name = input("Введите название предприятия: ")
            print(
                "Введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ")
            for i in range(1, 5):
                for j in range(int(input(f"{i} квартал: "))):
                    enterprises.append(name)
            return fill_enterprises_counter(
                enterprises, number_of_enterprises - 1)
        except ValueError:
            print('Ошибка ввода, попробуйте еще раз!')
            return fill_enterprises_counter(enterprises, number_of_enterprises)
    else:
        ent = Counter(enterprises)
        averaged_profit = sum(ent.values()) / len(ent)
        return ent, averaged_profit


def task1_namedtuple():
    try:
        number_of_enterprises = int(
            input('Введите количество предприятий для расчета прибыли: '))
        enterprises = []
        averaged_profit = fill_enterprises_namedtuple(
            enterprises, number_of_enterprises)
        print(f'Средняя годовая прибыль всех предприятий: {averaged_profit}')
        print("Предприятия, с прибылью выше среднего значения:")
        for i in filter(
                lambda x: x.year_profit > averaged_profit,
                enterprises):
            print(i.name)
        print("Предприятия, с прибылью ниже среднего значения:")
        for i in filter(
                lambda x: x.year_profit <= averaged_profit,
                enterprises):
            print(i.name)
    except ValueError:
        print('Ошибка ввода количества предприятий!')


def task1_default_dict():
    try:
        number_of_enterprises = int(
            input('Введите количество предприятий для расчета прибыли: '))
        enterprises = []
        enterprises, averaged_profit = fill_enterprises_default_dict(
            enterprises, number_of_enterprises)
        print(f'Средняя годовая прибыль всех предприятий: {averaged_profit}')
        print("Предприятия, с прибылью выше среднего значения:")
        for i in {x: y for x, y in enterprises.items() if y > averaged_profit}:
            print(i)
        print("Предприятия, с прибылью ниже среднего значения:")
        for i in {x: y for x, y in enterprises.items() if y <= averaged_profit}:
            print(i)
    except ValueError:
        print('Ошибка ввода количества предприятий!')


def task1_counter():
    try:
        number_of_enterprises = int(
            input('Введите количество предприятий для расчета прибыли: '))
        enterprises = []
        enterprises, averaged_profit = fill_enterprises_counter(
            enterprises, number_of_enterprises)
        print(f'Средняя годовая прибыль всех предприятий: {averaged_profit}')
        print("Предприятия, с прибылью выше среднего значения:")
        for i in {x: y for x, y in enterprises.items() if y > averaged_profit}:
            print(i)
        print("Предприятия, с прибылью ниже среднего значения:")
        for i in {x: y for x, y in enterprises.items() if y <=
                  averaged_profit}:
            print(i)
    except ValueError:
        print('Ошибка ввода количества предприятий!')


def main():
    task1_namedtuple()
    task1_default_dict()
    task1_counter()


main()

