"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import cProfile
import timeit


def get_execution_time(method):
    def wrapped(self, *args, **kwargs):
        start_time = timeit.default_timer()
        method(self, *args, **kwargs)
        print(f"Вемя выполнения метода: {timeit.default_timer() - start_time} секунд")
    return wrapped


def memorize(method):
    def wrapped(self, n, memory={}):
        r = memory.get(n)
        if r is None:
            r = method(self, n)
            memory[n] = r
        return r
    return wrapped


class EulerSecondTask:
    """Найти сумму всех четных элементов ряда Фибоначи, которые не превышают 4 милиона"""
    def __init__(self, maximum):
        self.max = maximum

    def _fibonacci_max_value_generator(self):
        """Генератор списка последовательности фибоначи до максимального значения"""
        a, b = 0, 1
        while b < self.max:
            a, b = b, a + b
            yield a

    @memorize
    def _fibonacci(self, n):
        """Получение значения элемента ряда Фибоначи по номеру"""
        if n < 2:
            return n
        return self._fibonacci(n - 1) + self._fibonacci(n - 2)

    @get_execution_time
    def get_result_with_generator(self):
        result = 0
        for i in self._fibonacci_max_value_generator():
            if i % 2 == 0:
                result += i
        print(f'сумму всех четных элементов ряда Фибоначи, который не превышают {self.max}: {result}')

    @get_execution_time
    def get_result_without_generator(self):
        result, count = 0, 0
        while True:
            element = self._fibonacci(count)
            if element < self.max:
                if element % 2 == 0:
                    result += element
                count += 1
            else:
                break
        print(f'сумму всех четных элементов ряда Фибоначи, который не превышают {self.max}: {result}')


class EulerNineTask:
    """"Существует только одна тройка Пифагора, для которой a + b + c = 1000. Найдите произведение abc."""

    def __init__(self, sum_a_b_c):
        self.sum_a_b_c = sum_a_b_c

    def _is_search_trio_slow(self, a, b, c):
        """Проверка на то, являются ли числа искомой тройкой Пифагора"""
        return a + b + c == self.sum_a_b_c and a < b < c and a**2 + b**2 == c**2

    def _is_search_trio_fast(self, m, n):
        """Проверка на то, являются ли числа искомой тройкой Пифагора (перегруженный метод)"""
        return 2 * m**2 + 2 * m * n == self.sum_a_b_c

    @get_execution_time
    def very_slow_result(self):
        """Медленое решение задачи"""
        for c in range(3, self.sum_a_b_c):
            for b in range(2, self.sum_a_b_c):
                for a in range(1, self.sum_a_b_c):
                    if self._is_search_trio_slow(a, b, c):
                        print(
                            f"Искомая тройка Пифагора: a = {a}, b = {b}, c= {c}. Произведение: {a * b * c}")
                        return

    @get_execution_time
    def slow_result(self):
        """Медленое решение задачи"""
        for c in range(3, self.sum_a_b_c):
            for b in range(2, c - 1):
                for a in range(1, b - 1):
                    if self._is_search_trio_slow(a, b, c):
                        print(
                            f"Искомая тройка Пифагора: a = {a}, b = {b}, c= {c}. Произведение: {a * b * c}")
                        return

    @get_execution_time
    def fast_result(self):
        """Быстрое решение задачи"""
        for m in range(2, self.sum_a_b_c):
            for n in range(1, m - 1):
                if self._is_search_trio_fast(m, n):
                    a, b, c = 2 * m * n, m**2 - n**2, m**2 + n**2
                    print(
                        f"Искомая тройка Пифагора: a={a}, b={b}, c={c}. Произведение: {a*b*c}")
                    return


def main():
    test = EulerNineTask(1000)
    """
        При вызове очень медленного метода выполнения нахождения исхомой тройки Пиффагора:
        O(1) + O(n**3) - кубическая сложность
        Вемя выполнения метода: 108.6233079 секунд
    """
    test.very_slow_result()
    """
        При вызове медленного метода выполнения нахождения исхомой тройки Пиффагора
        воспользуемся условием a<b<c (сложность осталась
        кубическая, но время выполнения резко снизилось): 
        O(n) * 0(n-1) * O(n-2) + O(2) - кубическая сложность ( не уверен в описании сложности)
        Вемя выполнения метода: 2.947995800000001 секунд
    """
    test.slow_result()
    """
        При вызове бустрого метода выполнения нахождения исхомой тройки Пиффагора
        воспользуемся коэффециентами m и n, а так же условием n<m: 
        O(n) * O(n-1) + O(2) - квадратичкая сложность ( не уверен в описании сложности)
        Вемя выполнения метода: 9.319999999490847e-05 секунд
    """
    test.fast_result()
    """
        Для меньшего значения суммы
    """
    # test = EulerNineTask(200)
    test.very_slow_result()
    # Вемя выполнения метода: 0.7973802000000001 секунд
    test.slow_result()
    # Вемя выполнения метода: 0.02275729999999998 секунд
    test.slow_result()
    # Вемя выполнения метода: 0.024082700000000012 секунд
    """
        Найти сумму всех четных элементов ряда Фибоначи, которые не превышают 4 милиона
    """
    test = EulerSecondTask(4000000)
    """
        При формировании ряда Фибоначи с помощью генератора
        Вемя выполнения метода: 2.989999999999937e-05 секунд
    """
    test.get_result_with_generator()
    """
        При формировании ряда Фибоначи с помощью рекурсии без мемоизации
        Вемя выполнения метода: 7.7567771 секунд
        При формировании ряда Фибоначи с помощью рекурсии с мемоизацией
        Вемя выполнения метода: 4.4900000000000495e-05 секунд
    """
    test.get_result_without_generator()
    """
        Выводы:
        - встроенные функции, генераторы и иттераторы самые быстрые
        - с мемоизацией рекурсия работает быстрее (очевидно почему) 
        
    """


main()
# cProfile.run('main()')
