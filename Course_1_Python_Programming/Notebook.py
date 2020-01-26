# # вычисляем високосный год или нет
# a = int(input())
# if 1900 <= a <= 3000:
#     if a % 4 == 0 and not a % 100 == 0 or a % 400 == 0:
#         print("Високосный")
#     else:
#         print("Обычный")
# ============================================
# a = int(input())
# b = int(input())
# c = int(input())
#
# p = (a + b + c) / 2
# s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(float(s))
# ============================================
# a = int(input())
# if -15 < a <= 12 or 14 < a < 17 or 19 <= a:
#     print(True)
# else:
#     print(False)
# ============================================
# a = float(input())
# b = float(input())
# oper = input('')
# s = 0
# if oper == '+':
#     s = a + b;
#     print(s)
# elif oper == '-':
#     s = a - b
#     print(s)
# elif oper == '*':
#     s = a * b
#     print(s)
# elif oper == 'pow':
#     s = a ** b
#     print(s)
# elif oper == 'div' and b != 0:
#     s = a // b
#     print(s)
# elif oper == '/' and b != 0:
#     s = a / b
#     print(s)
# elif oper == 'mod' and b != 0:
#     s = a % b
#     print(s)
# else:
#     print("Деление на 0!")
# ============================================
# room = input('')
# a, b, c, r, p = 0, 0, 0, 0, 0
# pi = 3.14
# if room == "прямоугольник":
#     a = int(input())
#     b = int(input())
#     print(float(a * b))
# elif room == "треугольник":
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a + b + c) / 2
#     print(float(p * (p - a) * (p - b) * (p - c)) ** 0.5)
# elif room == "круг":
#     r = int(input())
#     print(float(pi * (r**2)))
# ============================================
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a <= b <= c:
#     print(c, '\n', a, '\n', b)
# elif a <= c <= b:
#     print(b, '\n', a, '\n', c)
# elif b <= a <= c:
#     print(c, '\n', b, '\n', a)
# elif b <= c <= a:
#     print(a, '\n', b, '\n', c)
# elif c <= a <= b:
#     print(b, '\n', c, '\n', a)
# elif c <= b <= a:
#     print(a, '\n', c, '\n', b)
# elif a == b <= c:
#     print(c, '\n', a, '\n', b)
# elif a <= b == c:
#     print(b, '\n', c, '\n', a)
# elif a <= c == b:
#     print(b, '\n', a, '\n', c)
# elif a == c <= b:
#     print(b, '\n', a, '\n', c)
# ============================================
# a = int(input())
# word = 'программист'
# if 111 <= a <= 114 or (a / 10) % 10 == 1 or a % 10 == 0 or 5 <= a % 10 <= 9:
# #     print(a, word + 'ов')
# # elif a % 10 == 1:
# #     print(a, word)
# # else:
#     print(a, word + 'а')


# a = int(input())
# word = 'программист'
# if 0 <= a <= 1000:
#    if (a / 10) % 10 == 1 or a % 10 == 0 or 5 <= a % 10 <= 9 or 10 <
#    a > 1 <= a % 10 and a != 0 and a not in range(21,9999999,10):
#         print(a, word + 'ов')
#     elif a == 1 or a in range(21, 9999999, 10):
#         print(a, word)
#     else:
#         print(a, word + 'а')

# a = int(input())
# lst_1 = (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94)
# lst_2 = (
#     1, 21, 31, 41, 51, 61, 71, 81, 91, 101, 121, 131, 141, 151, 161, 171, 181, 191, 221, 221, 231, 241, 251, 261, 271,
#     281, 291, 301, 321, 331, 341, 351, 361, 371, 381, 391, 401, 421, 431, 441, 451, 461, 471, 481, 491, 501, 521, 531,
#     541, 551, 561, 571, 581, 591, 601, 621, 631, 641, 651, 661, 671, 681, 691, 701, 721, 731, 741, 751, 761, 771, 781,
#     791, 801, 821, 831, 841, 851, 861, 871, 881, 891, 901, 921, 931, 941, 951, 961, 971, 981, 991)
# if a in lst_1:
#     print(a, 'программиста')
# elif a in lst_2:
#     print(a, 'программист')
# else:
#     print(a, 'программистов')

# a = int(input())
# if a >= 0:
#     if a == 0:
#         print(str(a) + 'программистов')
#     elif a % 100 >= 10 and a % 100 <= 20:
#         print(str(a) + 'программистов')
#     elif a % 10 == 1:
#         print(str(a) + 'программист')
#     elif a % 10 >= 2 and a % 10 <= 4:
#         print(str(a) + 'программистов')
#     else:
#         print(str(a) + 'программистов')
# ============================================

# Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
# Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
# Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит равенство
# сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
# На вход программе подаётся строка из шести цифр.
# Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.

# element = list(input())
# if int(element[0]) + int(element[1]) + int(element[2]) == int(element[3]) + int(element[4]) + int(element[5]):
#     print('Счастливый')
# else:
#     print('Обычный')

# element = {False: 'Счастливый', True: 'Обычный'}
# b, c, d, e, f, g = (int(n) for n in input())
# print(element[bool((b + c + d) - (e + f + g))])
# ============================================
# a = 25
# while a >= 0:
#     print(a, end='~')
#     a -= 1
#
# a = 5
# while a <= 55:
#     if a % 2 == 1:
#         print(a)
#     a += 1

# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
#     print(i)

# n = int(input())
# c = 1
# while c <= n:
#     print('*' * c)
#     c += 1

# n = int(input())
# stars = '*'
# while len(stars) <= n:
#     print(stars)
#     stars += '*'
# ============================================
# # Сколько всего знаков * будет выведено после исполнения фрагмента программы:
# # Ответ: 17
# i = 0
# count = 0
# while i < 5:
#     print('*')
#     count += 1  # добавил
#     if i % 2 == 0:
#         print('**')
#         count += 2  # добавил
#     if i > 2:
#         print('***')
#         count += 3  # добавил
#     i = i + 1
# print(count)  # добавил
# ============================================
# s = 0
# i = a
# while i <= b:
#     s += i
#     i += 1
# print(s)
#
# n = int(input())
# sum_n = 0
# while n != 0:
#     sum_n += n
#     if n != 0:
#         n = int(input())
# print(sum_n)

# a = int(input())
# b = int(input())
# s = 1
# k = 2
# while s < k:
#     if s % a == 0 and s % b == 0:
#         k = s
#     else:
#         s = s + 1
#         k = k + 1
# print(s)

# a = int(input())
# b = int(input())
# d = a
# while d % b:
#     d += a
# print(d)
# ============================================
# # Читам 5 пар чисел и выводим их произведение
# i = 0
# while i < 5:
#     a, b = input().split()
#     a, b = int(a), int(b)
#     print(a * b)
#     i += 1
# # ИЛИ использовать break
# # Читам 5 пар чисел и выводим их произведение
# i = 0
# while i < 5:
#     a, b = input().split()
#     a, b = int(a), int(b)
#     if (a == 0) and (b == 0):
#         break  # досрочное завершение цикла
#     print(a * b)
#     i += 1
# # ИЛИ использовать continue
# # Читам 5 пар чисел и выводим их произведение, если одно из чисел == 0, игнорируем пару чисел
# i = 0
# while i < 5:
#     a, b = input().split()
#     a, b = int(a), int(b)
#     if (a == 0) and (b == 0):
#         break  # досрочное завершение цикла
#     if (a ==0) or (b == 0):
#         continue  # переходим к следующей итерации
#     print(a * b)
#     i += 1
#
# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
# print(i)  # 7

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)  # 10
# a = 0
# b = []
# while a <= 100:
#     a = int(input())
#     if a <= 10:
#         continue
#     if a > 100:
#         break
#     else:
#         b.append(a)
#         continue
# print(list(b), end='\n')

# a = 0
# while a <= 100:
#     a = int(input())
#     if a > 100:
#         break
#     if a < 10:
#         continue
#     print(a)
# ==============================
# # range(start=0, to, step1)
# for i in range(1,10,2):
#     print(i * i)
# ==============================
# b = [1, 2, 3, 4, 5, 6]
# for i in b[::2]:
#     print(i * i)
# ==============================
# n = int(input())
# for i in range(n):
#     print('*' * n)
# ==============================
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print('*', end='-')
#     print()
# ==============================
# # Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками.
# # Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
# # Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке.
# # Программа должна вывести фрагмент таблицы
# # умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d].
# # Числа a, b, c и d являются натуральными и не превосходят 10, a≤b, c≤d.
# # Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t'
# # — символ табуляции. Заметьте, что левым столбцом и верхней строкой выводятся сами числа
# # из заданных отрезков — заголовочные столбец и строка таблицы.﻿

# # В общем и целом - это таблица умножения!!!
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# for g in range(c, d + 1):
#     print('\t' + str(g), end='')
# print(end='\n')
# for i in range(a, b + 1):
#     print(str(i) + '\t', end='')
#     for j in range(c, d + 1):
#         print(str(i * j), end='\t')
#     print(end='\n')
# ==============================
# Вывести сумму всех нечетных чисел от 'a' до 'b' (включая обе границы)
# a = int(input())
# b = int(input())
# c = 0
# for element in range(a, b + 1):
#     if element % 2 != 0:
#         c += element
# print(c)

# a = int(input())
# b = int(input())
# c = 0
# if a % 2 == 0:
#     a += 1
# for element in range(a, b + 1, 2):
#     c += 1
# print(c)

# a, b = (int(i) for i in input().split())
# c = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1, 2):
#     c = + 1
# print(c)

# a = int(input())
# b = int(input())
# c = 0
# d = 0
# for element in range(a, b + 1):
#     if element % 3 == 0:
#         c += element
#         d += 1
# print(c / d)

# genome = 'ATGG'
# for i in range(4):
#     print(genome[i])

# genome = input()
# cnt = 0
# for nucl in genome:
#     if nucl == 'C':
#         cnt += 1
# print("Символ 'С' встретился", cnt, 'раза')

# genome = 'CACCTGGAC'
# print("Символ 'С' встретился", genome.count('C'), 'раза')

# s = 'аfGtnkpohGtsldtggt'
# print(s.upper().count('gt'.upper()))

# Рассчитать процент содержания символов 'g' и 'c', вне зависимости от регистра
# (4/10)*100 где 4 - количество символов g и c, в 10 - длина строки.

# s = input('')
# print(((s.lower().count('c'.lower()) + s.lower().count('g'.lower()))/len(s))*100)
# ===============================
# Поиск палиндрома вариант1(abba)
# ===============================
# s = input()
# i = 0
# j = len(s) - 1
# is_palindrom = True
# while i < j:
#     if s[i] != s[j]:
#         is_palindrom = False
#         break
#     i += 1
#     j -= 1
# if is_palindrom:
#     print('YES')
# else:
#     print('NO')
# # ===============================
# # Поиск палиндрома вариант2
# # ===============================
# s = input()
# r = s[::-1]
# if s == r:
#     print('YES')
# else:
#     print('NO')

# s = input()
# rez_str = ''
# rez = []
# rez2 = []
# for i in s:
#     rez.append(i)
#     for j in rez:a
#         if j >= j[0+1:-1+1]:
#             rez2.append(j + str(len(j)))
#         continue
#
# print(rez)
# print(rez2)

# s = list(input())
# new_s = []
# counter = 1
#
# if len(s) == 1:
#     new_s.append(s.pop(0) + str(counter))
# else:
#     for i in s:
#         if s[0] == s[1]:
#             counter += 1
#             s.pop(0)
#         new_s.append(s.pop(0) + str(counter))
#         if s[0] != s[1]:
#             new_s.append(s.pop(0) + str(counter))
#             counter = 1
#
# print('Счетчик counter =', counter)
# print('Содержание s', s)
# print('Содержание new_s', str(new_s))

# # ===============================
# вариант1
# # ===============================
# s = str(input())
# l = len(s) - 1
# c = 1
# t = ''
# if len(s) == 1:
#     t += s + str(c)
# else:
#     for i in range(0, l):
#         if s[i] == s[i + 1]:
#             c += 1
#         elif s[i] != s[i + 1]:
#             t += s[i] + str(c)
#             c = 1
#     for j in range(l, l + 1):
#         if s[-1] == s[-2]:
#             t += s[j] + str(c)
#         elif s[-1] != s[-2]:
#             t += s[j] + str(c)
#             c = 1
# print(t)
# # ===============================
# вариант2
# # ===============================
# s, n = 0, input() + ' '
# for i in n:
#     if n[0] != i:
#         print(n[0], s, end='', sep='')
#         s, n = 0, i
#     s += 1
# # ===============================
# вариант3
# # ===============================
# g = str(input())
# rep = 1
# out = g[0]
# for i in range(1,len(g)):
#   if (g[i] == g[i-1]):
#     rep +=1
#   else:
#     out = out+str(rep)+g[i]
#     rep=1
# print(out+str(rep))
# # ===============================
# вариант4
# # ===============================
# import itertools
#
# # print("".join([k + str(len(list(g))) for k, g in itertools.groupby(input())]))
# a = [1, 2, 3]
# b = a
# # значения списка b?
# print(b)
# a[1] = 10
# # значения списка b?
# print(b)
# b[0] = 20
# # значения списка a?
# print(a)
# a = [5, 6]
# # значения списка b?
# print(b)
# print(a)
# ===============================================
# a = [0] * 5
# print(a)
#
# a = [0 for i in range(5)]
# print(a)
#
# a = [(i+1) for i in range(5)]
# print(a)
#
# a = [(i+1)*2 for i in range(5)]
# print(a)
#
# a = [i*i for i in range(5)]
# print(a)
#
# a = [(i+len(a))/100 for i in range(5)]
# print(a)
#
# a = [int(i) for i in input().split()]
# print(a)
# ===============================================
# a = [int(i) for i in input().split()]
# if len(a) == 1:
#     print(a[0])
# else:
#     [print(int(a[i - 1] + a[(i + 1) % len(a)]), end=' ') for i in range(len(a))]
# ===============================================
# a = [int(i) for i in input().split()]
# for i in a:
# a = [int(i) for i in input().split()]
# b = ["".join(str(set(a)))]
# print(b, end=' ')
# [print(set(str(i)), end=' ') for i in b if b.count(i) >= 1]

# Напишите программу, которая принимает на вход список чисел в одной строке и выводит
# на экран в одну строку значения, которые повторяются в нём более одного раза.
# Для решения задачи может пригодиться метод sort списка.
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

# a = [int(i) for i in input().split()]
# # a.sort()
# # c = []
# # k = 123456789
# # if len(a) != 1:
# #     for i in range(0, len(a) - 1):
# #         if a[i] == a[i + 1] and a[i] != k:
# #             c.append(a[i])
# #             k = a[i]
# #     for j in range(len(a) - 1, (len(a) - 1) + 1):
# #         if a[-1] == a[-2] and a[j] != k:
# #             c.append(a[j])
# # for n in range(0, len(c)):
# #     print(c[n], end=' ')
# ===============================================
# a = [int(i) for i in input().split()]
# b = []
# [b.append(i) for i in a if i not in b and a.count(i) > 1]
# print(*b)
# ===============================================

# s = [int(i) for i in input().split()]
# t = []
# s.sort()
# l = len(s) - 1
# k = 100000
# if len(s) != 1:
#     for i in range(0, l):
#         if s[i] == s[i + 1] and s[i] != k:
#             t.append(s[i])
#             k = s[i]
#     for j in range(l, l + 1):
#         if s[-1] == s[-2] and s[j] != k:
#             t.append(s[j])
# n = len(t)
# for g in range(0, n):
#     print(t[g], end=' ')
# ===============================================
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(a)
# print(a[1])
# print(a[1][1])

# n = 3
# a = [[0] * n] * n
# print(a)
# a[0][0] = 5
# print(a)

# n = 3
# a = [[0] * n for i in range(n)]
# print(a)

# n = 3
# a = [[0 for j in range(n)] for i in range(n)]
# a[1][2] = 5
# print(a)
# ===============================================
# Поиск минимума в списке
# a = [int(i) for i in input().split()]
# m = a[0]
# for i in a:
#     if m > i:
#         m = i
# print(m)
# ===============================================
# Сапер
# Даны размеры поля для игры в сапер и координаты мин, стоящих на этом
# поле. Вывести поле игры на экран
# 5 4 4  - столбец, строка, кол-во мин.
# 1 1 - расположение 1-й мины [1][1]
# 2 2 - расположение 2-й мины [2][2]
# 3 2 - расположение 3-й мины [3][2]
# 4 4 - расположение 4-й мины [4][4]
# Понятие соседней мины:
# 1 2 3
# 4 * 5
# 6 7 8
# Вывод
# *21.
# 3*2.
# 2*31
# 112*
# ..11
# Мина будет обозначаться "-1"
# Сначало заполняем всё нулями. Потом заполняем -1 там где мины.
# После проверяем соседние клетки на наличие мины, если есть, добавляем в счетчик +1
# Всего на каждую клетку 8 соседей.
# i - номер строки, j - номер столбца
# ===============================================
# n, m, k = (int(i) for i in input().split())  # строка, столбец, мины
# a = [[0 for j in range(m)] for i in range(n)]  # инициализируем двумерный массив
# for i in range(k):
#     # Прочитаем координаты расположения мин, и каждую мину поместим в таблицу "-1"
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = -1
# for i in range(n):  # Заполняем таблицу
#     for j in range(m):
#         if a[i][j] == 0:
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()
# ===============================================
# Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор,
# пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
#
# Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0,
# после этого считывание продолжать не нужно.
#
# В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна нулю и
# выводим сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.﻿
# Sample Input:
# 1
# -3
# 5
# -6
# -10
# 13
# 4
# -8
#
# Sample Output:
# 340

# a = [int(input())]
# while sum(a) != 0:
#     a.append(int(input()))
#     print(sum(i ** 2 for i in a))
#
# ===============================================
# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число n
# — столько элементов последовательности должна отобразить программа.
# На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

# n = int(input())
# a = []
# i = 0
# while len(a) < n:
#     a += [i] * i
#     i += 1
# print(*a[:n])
# ===============================================
# Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки,
# которая выводит все позиции, на которых встречается число x в переданном списке lst.
# Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует"
# (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
# Sample Input 1:
# 5 8 2 7 8 8 2 4
# 8
# Sample Output 1:
# 1 4 5
#
# Sample Input 2:
# 5 8 2 7 8 8 2 4
# 10
# Sample Output 2:
# Отсутствует

# lst = [int(i) for i in input().split()]
# x = int(input())
# if x not in lst:
#     print('Отсутствует')
# for index, element in enumerate(lst):
#     if element == x:
#         print(index, end=' ')
# ===============================================
# a = [input().split()]  # строка, столбец
# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# # for i in a:
# #     for j in i:
# #         print(j, end=' ')
# #     print()
# for row in a:
#     print(' '.join([str(elem) for elem in row]))
# ===============================================
# # в первой строке ввода идёт количество строк массива
# n = int(input())
# a = []
# for i in range(n):
#     a.append([int(j) for j in input().split()])
# print(a)

# ИЛИ

# в первой строке ввода идёт количество строк массива
# n = int(input())
# a = []
# for i in range(n):
#     row = input().split()
#     for i in range(len(row)):
#         row[i] = int(row[i])
#     a.append(row)
# print(a)

# ИЛИ

# в первой строке ввода идёт количество строк массива
# n = int(input())
# a = [[int(j) for j in input().split()] for i in range(n)]
# print(a)


# n = 4
# a = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i < j:
#             a[i][j] = 0
#         elif i > j:
#             a[i][j] = 2
#         else:
#             a[i][j] = 1
# for row in a:
#     print(' '.join([str(elem) for elem in row]))
#
# n = 5
# m = 6
# b = [print([i * j for j in range(m)], end=' ') for i in range(n)]

# n = 4
# a = [0] * n
# a = [[2] * i + [1] + [0] * (n - i - 1) for i in range(n)]
# for row in a:
#     print(' '.join([str(elem) for elem in row]))

# n = ''
# m = []
# while True:  # ожидаем ввод пока не будет end, выходим из ввода
#     n = str(input())  # ввод строк
#     if n == 'end':
#         break
#     m.append([int(s) for s in n.split()])  # добавляем все введенные елементы
# li, lj = len(m), len(m[0])
# new = [[sum([m[i - 1][j], m[(i + 1) % li][j], m[i][j - 1],
# m[i][(j + 1) % lj]]) for j in range(lj)] for i in range(li)]
#
# for i in range(li):
#     for j in range(lj):
#         print(new[i][j], end=' ')
#     print()
# Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали,
# выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):

# def spiral(n):
#     dx, dy = 1, 0
#     x, y = 0, 0
#     myarray = [[None] * n for j in range(n)]
#     for i in range(1, n ** 2 + 1):
#         myarray[x][y] = i
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < n and 0 <= ny < n and myarray[nx][ny] == None:
#             x, y = nx, ny
#         else:
#             dx, dy = -dy, dx
#             x, y = x + dx, y + dy
#     return myarray
#
#
# def printspiral(myarray):
#     n = range(len(myarray))
#     for y in n:
#         for x in n:
#             print(myarray[x][y], end=' ')
#         print()
#
#
# n = int(input())
# printspiral(spiral(n))

# n = int(input())
# m = n
# r, k, a = 0, 1, [[0] * n for i in range(n)]
#
# while n > n // 2 - 1:
#     for i in range(r, n):  # идем вправо
#         a[r][i] = k
#         k += 1
#     for i in range(r + 1, n):  # идем вниз
#         a[i][n - 1] = k
#         k += 1
#     for i in reversed(range(r, n - 1)):  # идем влево
#         a[n - 1][i] = k
#         k += 1
#     for i in reversed(range(r + 1, n - 1)):  # идем вверх
#         a[i][r] = k
#         k += 1
#     n -= 1
#     r += 1
#
# for i in range(m):  # вывод списка
#     for j in range(m):
#         print(a[i][j], end=' ')
#     print()
# ===============================================
# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
# f(x) = (1−(x+2)**2, при x <= -2
# f(x) = −(x/2), при -2 < x <= 2
# f(x) = (x−2)**2+1, при 2 < x
# Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.
# def f(x):
#     if x <= -2:
#         return 1 - (x + 2)**2
#     elif -2 < x <= 2:
#         return -(x/2)
#     elif x > 2:
#         return (x-2)**2 + 1
# print(f(1))
# ===============================================
# def modify_list(l):
#     l[:] = [i // 2 for i in l if i % 2 == 0]
#
#
# l = [8]
# print(modify_list(l))
# ===============================================
# basket = {'apple', 'orange', 'banana', 'apple', 'orange', 'pear'}
# for i in basket:
#     print(i)
#
# basket.clear()
#
# print(basket)

# d = {'C': 14, 'A': 12, 'T': 9, 'G': 18}
# for key in d:  # Возвращаем список ключей словаря
#     print(key, end=' ')
# print()
# for key in d.keys():  # Возвращаем список ключей словаря
#     print(key, end=' ')
# print()
# for value in d.values():  # Возвращаем список значений словаря
#     print(value, end=' ')
# print()
# for key, value in d.items():   # Возвращаем список ключей и их значений словаря
#     print(key, value, end=';')
# ===============================================
# Напишите функцию update_dictionary(d, key, value),
# которая принимает на вход словарь d и два числа: key и value.
#
# Если ключ key
# есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
# Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2⋅key.
# Если и ключа 2⋅key нет, то нужно добавить ключ 2⋅key в словарь
# и сопоставить ему список из переданного элемента [value].
#
# Требуется реализовать только эту функцию, кода вне неё не должно быть.
# Функция не должна вызывать внутри себя функции input и print.

# # Решение
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key] += [value]
#     elif 2*key in d:
#         d[2*key] += [value]
#     else:
#         d[2*key] = [value]
#
# # Проверка
# d = {}
# print(update_dictionary(d, 1, -1))
# print(d)
# update_dictionary(d, 2, -2)
# print(d)
# update_dictionary(d, 1, -3)
# print(d)
# ===============================================
# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова,
# разделённые пробелом и вывести получившуюся статистику.
# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального
# слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.
# Sample Input 1:
# a aa abC aa ac abc bcd a

# Sample Output 1:
# ac 1
# a 2
# abc 2
# bcd 1
# aa 2

# Sample Input 2:
# a A a

# Sample Output 2:
# a 3

# Вариант 1
# n = str(input())  # Подаем на ввод строку
# m = []  # Инициализируем список
# d = {}  # Инициализируем словарь
# m.append([str(s.lower()) for s in n.split()])  # Добавляем в список введенную строку, разделенную пробелом
# for i in range(len(m)):
#     for j in range(len(m[0])):
#         p = m[i][j]
#         if p in d:
#             d[p] += 1
#         else:
#             d[p] = 1
# [print(key, value, end='\n') for key, value in d.items()]
# =========
# Вариант 2
# s = input().lower().split()
# for i in set(s):
#     print(i, s.count(i))
# ===============================================
# Имеется реализованная функция f(x), принимающая на вход целое число x,
# которая вычисляет некоторое целочисленое значение и возвращает его в качестве результата работы.
# Функция вычисляется достаточно долго, ничего не выводит на экран, не пишет
# в файлы и зависит только от переданного аргумента x.
#
# Напишите программу, которой на вход в первой строке подаётся число n
# — количество значений x, для которых требуется узнать значение функции f(x), после чего
# сами эти n значений, каждое на отдельной строке. Программа должна после каждого введённого
# значения аргумента вывести соответствующие значения функции f на отдельной строке.
#
# Для ускорения вычисления необходимо сохранять уже вычисленные значения функции при известных аргументах.
# Обратите внимание, что в этой задаче установлено достаточно сильное ограничение в две
# секунды по времени исполнения кода на тесте.
# Sample Input:
#
# 5
# 5
# 12
# 9
# 20
# 12
#
# Sample Output:
#
# 11
# 41
# 47
# 61
# 41
# ===============================================
# d = {}
# k = []
# n = int(input())
# for i in range(n):
#     x = int(input())
#     k.append(x)
# for j in range(0, len(k)):
#     key = k[j]
#     if key in d:
#         print(d[key])
#     elif key not in d:
#         p = k[j]
#         d[key] = f(p)
#         print(d.get(key))
# ===============================================
# inf = open('D:\\Projects\\pass.txt', 'r')
# s1 = inf.readline()
# s2 = inf.readline()
# inf.close()
# print(s1, s2)

# with open('D:\\Projects\\pass.txt', 'r') as inf:
#     s1 = inf.readline().strip()
#     s2 = inf.readline().strip()
# print(s1, s2)

# with open('D:\\Projects\\pass.txt', 'r') as inf:
#     for line in inf:
#         line = line.strip()
#         print(line)

# ouf = open('D:\\Projects\\pass_blabla.txt', 'w')
# ouf.write('blabla\n')
# ouf.write(str(25))
# ouf.close()

# with open('D:\\Projects\\pass_blabla.txt', 'w') as ouf:
#     ouf.write('2_balbal\n')
#     ouf.write(str(25))
#     ouf.write('25+25\n+25+25\n+252+25')
# ==================================================================
# На прошлой неделе мы сжимали строки, используя кодирование повторов.
# Теперь нашей задачей будет восстановление исходной строки обратно.
#
# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью
# кодирования повторов, и производит обратную операцию, получая исходный текст.
#
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
#
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
#
# Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz"
# у вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со
# входными данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных.
# Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.
#
# Sample Input:
# a3b4c2e10b1
#
# Sample Output:
# aaabbbbcceeeeeeeeeeb

# Вариант 2
# with open('dataset_3363_2 (2)', 'r') as (e):
#     s1 = e.readline()
# f = 0
# n = ''
# l = []
# for i in range(len(s1)):
#     # print (s1[i])
#     if s1[i].isdigit():
#         n += s1[i]
#     elif s1[i].isalpha():
#         if i >= 1:
#             n1 = int(n)
#             l.append(n1)
#             n = ''
#         l.append(s1[i])
# if len(n) > 0:
#     l.append(int(n))
# n = ''
# for i in range(0, len(l), 2):
#     n += (l[i] * l[i + 1])
# with open('dataset_3363_2 (2)', 'w') as (e):
#     e.write(n)
# Вариант 2
# with open('D:\\Projects\\dataset_3363_2.txt', 'r') as file_in:
#     s = file_in.read(1)
#     while s.strip('\n'):
#         s_now = s
#         print('symbol_now =', s_now)
#         s = file_in.read(1)
#         nums = 0
#         while s.strip('\n').isdigit():
#             nums = nums * 10 + int(s)
#             s = file_in.read(1)
#         print('nums =', nums)
#         if nums != 0:
#             with open('D:\\Projects\\dataset_3363_2_out.txt', 'a') as file_out:
#                 file_out.write(s_now * nums)
# ==================================================================
# Недавно мы считали для каждого слова количество его вхождений в строку.
# Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
#
# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
# и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
# Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
#
# Слова, написанные в разных регистрах, считаются одинаковыми.
#
# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC
#
# Sample Output:
# abc 3

# with open('D:\\dataset_3363_3.txt') as inf, open('D:\\MostPopularWord.txt', 'w') as ouf:
#     maxc = 0
#     s = inf.read().lower().strip().split()
#     s.sort()
#     for word in s:
#         counter = s.count(word)
#         if counter > maxc:
#             maxc = counter
#             result_word = word
#     ouf.write(result_word + ' ' + str(maxc))
# ==================================================================
# Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк,
# где в каждой строке записана следующая информация:
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
# Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента
# выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
# Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике,
# физике и русскому языку по всем абитуриентам:
# Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
#
# Sample Input:
# Петров;85;92;78
# Сидоров;100;88;94
# Иванов;58;72;85
#
# Sample Output:
# 85.0
# 94.0
# 71.666666667
# 81.0 84.0 85.666666667

# lines = []
# with open(r"d:\1.txt", "rt") as f:
#     for line in map(str.strip, f):
#         line = tuple(map(int, line.split(";")[1:]))
#         print(round(sum(line) / len(line),9))
#         lines.append(line)
# count = len(lines)
# for value in (sum(_) / count for _ in zip(*lines)):
#     print(round(value, 9), end=" ")
# print()
# ==================================================================
# import math
#
# n = float(input())
# print(2*math.pi*n)
