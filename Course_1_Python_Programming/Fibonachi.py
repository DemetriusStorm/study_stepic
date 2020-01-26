# Вариант 1 (Рекурсия)
# Хорошее: Очень простая реализация, повторяющая математическое определение
# Плохое: Экспоненциальное время выполнения. Для больших n очень медленно
# Злое: Переполнение стека

# fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1

# Вариант 2 (Запоминание). Решение через словарь
# Хорошее: Просто превратить рекурсию в решение с запоминанием.
# Превращает экспоненциальное время выполнение в линейное, для чего тратит больше памяти.
# Плохое: Тратит много памяти
# Злое: Возможно переполнение стека, как и у рекурсии


# def fib(n):
#     m = {0: 0, 1: 1}
#     if n in m:
#         return m[n]
#     m[n] = fib(n - 1) + fib(n - 2)
#     return m[n]
#
#
# a = fib(3)  # max=997
# print(a)

# Вариант 3 (Динамическое программирование)
# Хорошее: Быстро работает для малых n, простой код
# Плохое: Всё ещё линейное время выполнения
# Злое: Да особо ничего.

# a = 12121212121221211516698989898989898987
# mylist = list(str(a))
# print(a)
# print(mylist[-1])

#
# def fib(n, m):
#     a, b = 0, 1
#     for __ in range(n):
#         a, b = b, a + b
#     return a % m
#
#
# c = fib(13, 2)
# print(c)


# import sys
#
#
# def fib(n, m):
#     # lineIn = sys.stdin.readline().split(" ")
#     # n = int(lineIn[0])
#     # m = int(lineIn[1])
#
#     fibprev = 0
#     fib = 1
#     cached = [fibprev, fib]
#
#     for curr in range(1, n):
#         fibold = fib
#         fib = (fib + fibprev) % m
#         fibprev = fibold
#
#         if fibprev == 0 and fib == 1:
#             cached.pop()
#             break
#         else:
#             cached.append(fib)
#
#     offset = n % len(cached)
#     return str(cached[offset])
#     #
#     # sys.stdout.write(str(cached[offset]))

# Вариант 4 (Матричная алгебра)
# Хорошее: Фиксированный объём памяти, логарифмическое время
# Плохое: Код посложнее
# Злое: Приходится работать с матрицами, хотя они не так уж и плохи

# def pow(x, n, i, mult):
#     """
#     Возвращает x в степени n. Предполагает, что I – это единичная матрица, которая
#     перемножается с mult, а n – положительное целое
#     """
#     if n == 0:
#         return i
#     elif n == 1:
#         return x
#     else:
#         y = pow(x, n // 2, i, mult)
#         y = mult(y, y)
#         if n % 2:
#             y = mult(x, y)
#         return y
#
#
# def identity_matrix(n):
#     """Возвращает единичную матрицу n на n"""
#     r = list(range(n))
#     return [[1 if i == j else 0 for i in r] for j in r]
#
#
# def matrix_multiply(a, b):
#     bt = list(zip(*b))
#     return [[sum(a * b
#                  for a, b in zip(row_a, col_b))
#              for col_b in bt]
#             for row_a in a]
#
#
# def fib(n):
#     f = pow([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)
#     return f[0][1]
#
#
# a = fib(20)
# print(a)


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


print(fib(50))
