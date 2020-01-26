# =========================================
# В какой-то момент в Институте биоинформатики биологи перестали понимать,
# что говорят информатики: они говорили каким-то странным набором звуков.
#
# В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр,
# т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ.
# Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:
#
# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
# Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита,
# на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом,
# и ещё одна строка, которую нужно расшифровать.
#
# Пусть, например, на вход программе передано:
# abcd
# *d%#
# abacabadaba
# #*%*d*%
#
# Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
# Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра.
# # Получаем следующие строки, которые и передаём на вывод программы:
# *d*%*d*#*d*
# dacabac
# =========================================================
# '''
# Вариант № 1
# '''
#
# a = [i for i in input()]
# b = [i for i in input()]
# c = [i for i in input()]
# d = [i for i in input()]
#
# aib = dict(zip(a, b))
# bia = dict(zip(b, a))
# ib = ''
# ia = ''
#
# for i in c:
#     ib += aib[i]
# print(ib)
# for i in d:
#     ia += bia[i]
# print(ia)
# =========================================================
# '''
# Вариант № 2
# '''
# alf1, alf2, crypt, uncrypt = input(), input(), input(), input(),
# for i in crypt:
#     print(alf2[alf1.index(i)], end='')
# print()
# for i in uncrypt:
#     print(alf1[alf2.index(i)], end='')
# =========================================================
# '''
# Вариант № 3
# '''
# a, b, c, d = input(), input(), input(), input()
# print(''.join(b[a.index(i)] for i in c))
# print(''.join(a[b.index(i)] for i in d))
# =========================================================
# '''
# Вариант № 4
# '''
#
# s = str(input())
# a = []
# for i in range(len(s)):
#     si = s[i]
#     a.append(si)
# b = []
# n = str(input())
# for j in range(len(n)):
#     sj = n[j]
#     b.append(sj)
# p = {}
# for pi in range(len(s)):
#     key = s[pi]
#     p[key] = 0
# j1 = 0
# for i in range(0, len(a)):
#     key = a[i]
#     while j1 < len(b):
#         bj = b[0]
#         if key in p:
#             p[key] = bj
#         b.remove(bj)
#         break
# c = []
# si = str(input())
# for si1 in range(0, len(si)):
#     ci = si[si1]
#     c.append(ci)
# co = []
# for ci in range(0, len(c)):
#     if c[ci] in p:
#         cco = c[ci]
#         pco = p[cco]
#         co.append(pco)
# d = []
# di = str(input())
# for sj1 in range(0, len(di)):
#     dj = di[sj1]
#     d.append(dj)
# do = []
# for di in range(0, len(d)):
#     for key in p:
#         pkey = key
#         if p.get(key) == d[di]:
#             ddo = pkey
#             do.append(ddo)
# for i in range(0, len(co)):
#     print(co[i], end='')
# print()
# for j in range(0, len(do)):
#     print(do[j], end='')
