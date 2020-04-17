"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import sys
from memory_profiler import profile, memory_usage
from time import process_time
from functools import reduce
from pympler.asizeof import asizeof

"""
Python 3.8.2
64 - разрядная windows 10 
"""


def decorator_with_args(decorator_to_enhance):
    def decorator_maker(function_name):
        def wrapped(func):
            return decorator_to_enhance(func, function_name)
        return wrapped
    return decorator_maker


@decorator_with_args
def get_execution_time_memory(function, function_name):
    def wrapped(*args, **kwargs):
        start_time = process_time()
        start_memory = memory_usage()
        return_value = function(*args, **kwargs)
        stop_time = process_time()
        stop_memory = memory_usage()
        print(
            f"Выполнение  функции {function_name} заняло {stop_time - start_time} сек и"
            f" {stop_memory[0] - start_memory[0]} Мб")
        return return_value
    return wrapped


@get_execution_time_memory('function_1')
# @profile
def function_1(max_value):
    """Функция возвращает сумму квадатов четных чисел от 0 до max_value"""
    gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
    value = reduce(lambda x, y: x + y, gen)
    return value


@get_execution_time_memory('function_2')
# @profile
def function_2(max_value):
    """Функция возвращает сумму квадатов четных чисел от 1 до max_value"""
    gen = (x**2 for x in range(1, max_value) if x % 2 == 0)
    value = reduce(lambda x, y: x + y, gen)
    return value


@get_execution_time_memory('function_3')
# @profile
def function_3(max_value):
    """Функция возвращает сумму квадатов четных чисел от 0 до max_value"""
    gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
    value = reduce(lambda x, y: x + y, gen)
    del gen
    return value


# print(function_1(999999))
# print(function_2(999999))
# print(function_3(999999))

"""
Выводы:
    В function_1: gen является сгенерированым списком [4, 16, 36, 64 и т д], который занимает внушительный 
    размер памяти. При вызове function_1(999999) видно:
    Line #    Mem usage    Increment   Line Contents
    ================================================
    36     13.3 MiB     13.3 MiB   @profile
    37                             def function_1(max_value):
    38                                 Функция возвращает сумму квадатов четных чисел от 0 до max_value
    39     26.6 MiB      0.2 MiB       gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
    40     26.6 MiB      0.0 MiB       value = reduce(lambda x, y: x + y, gen)
    41     26.6 MiB      0.0 MiB       return value
    Отсюда видно что gen занимает 0.2 MiB, однако реально размер увеличивается до 26.6 MiB, т е 13.3 MiB(почему?)
    и на выходе из функции размер остается 26.6 MiB из них 13.3 MiB - gen
    
    В function_3: после пахождения суммы вызывается деструктор gen
    Line #    Mem usage    Increment   Line Contents
    ================================================
    54     13.4 MiB     13.4 MiB   @profile
    55                             def function_3(max_value):
    56                                 Функция возвращает сумму квадатов четных чисел от 0 до max_value
    57     26.8 MiB      0.2 MiB       gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
    58     26.8 MiB      0.0 MiB       value = reduce(lambda x, y: x + y, gen)
    59     13.5 MiB      0.0 MiB       del gen
    60     13.5 MiB      0.0 MiB       return value
    Отсюда видно, что при выходе из функции остается 13.5 MiB из них 13.4 MiB - @profile(откуда 0,1 MiB?),
    что лучше чем при выполнении function_1
    
    В function_2: gen является объектом генератора <generator object <genexpr> at 0x036FE728>, равносильно генератору:
    def gen(max_value):
        for i in range(1, max_value):
            if i % 2 == 0:
                yield i**2
    значения генерируются и берутся поочередно, не хранясь в памяти.
    При вызове function_2(999999) видно:
    Line #    Mem usage    Increment   Line Contents
    ================================================
    45     13.4 MiB     13.4 MiB   @profile
    46                             def function_2(max_value):
    47                                 Функция возвращает сумму квадатов четных чисел от 1 до max_value
    48     13.4 MiB      0.0 MiB       gen = (x**2 for x in range(1, max_value) if x % 2 == 0)
    49     13.4 MiB      0.0 MiB       value = reduce(lambda x, y: x + y, gen)
    50     13.3 MiB      0.0 MiB       return value
    Отсюда видно что gen занимает 0.0 MiB
    и на выходе из функции размер остается 13.3 MiB из них 13.4 MiB - @profile(почему стала меньше?)
    
    Применив декоратор @get_execution_time_memory:
    Выполнение  функции function_1 заняло 0.3125 сек и 0.140625 Мб
    166666166667000000
    Выполнение  функции function_2 заняло 0.328125 сек и 0.0 Мб
    166666166667000000
    Выполнение  функции function_3 заняло 0.328125 сек и 0.58984375 Мб
    166666166667000000
    Получается что функции со списком выполняются с таким же временем, но занимают больше памяти
    чем функция с объектом генерации, однако почему то при выполнении function_3(999999) декоратор
    показывает больший объем занимаемой памяти относительно function_1(999999). Предположительно
    function_3 должна занимать такое же количество паняти как и function_2.
    (корректен ли такой декоратор для оценки памяти, которая выделяется под функцию?
    Если нет, то подскажите как его можно исправить?)
"""


class TcpClient:
    num_of_tcp_clients = 0

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        TcpClient.num_of_tcp_clients += 1

    def __del__(self):
        TcpClient.num_of_tcp_clients -= 1


class TcpClientWithSlots:
    num_of_tcp_clients = 0
    __slots__ = ('ip', 'port')

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        TcpClientWithSlots.num_of_tcp_clients += 1

    def __del__(self):
        TcpClientWithSlots.num_of_tcp_clients -= 1


TCP_CLIENT = TcpClient('192.168.1.0', 16000)
print(f'Словарь класса: {TCP_CLIENT.__dict__}. Размер словаря: {asizeof(TCP_CLIENT)}')
TCP_CLIENT_WITH_SLOTS = TcpClientWithSlots('192.168.1.0', 16000)
print(f'Слоты класса: {TCP_CLIENT_WITH_SLOTS.__slots__}. Размер слотов: {asizeof(TCP_CLIENT_WITH_SLOTS)}')


"""
Выводы:
    Словарь класса: {'ip': '192.168.1.0', 'port': 16000}. Размер словаря: 208
    Слоты класса: ('ip', 'port'). Размер слотов: 80
    
    Использование слотов приводит к экономии памяти, однако отсутствует возможность динамического добавления 
    атрибутов
"""
