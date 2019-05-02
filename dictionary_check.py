# Простейшая система проверки орфографии основана на использовании списка известных слов.
# Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.
# Напишем подобную систему.
# Через стандартный ввод подаётся следующая структура: первой строкой — количество dd записей в списке известных слов,
# после передаётся  dd строк с одним словарным словом на строку, затем —
# количество ll строк текста, после чего — ll строк текста.
# Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается.
# Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.

# # Вариант 1
# n = int(input())
# dictionary = [input().lower() for i in range(n)]
# n = int(input())
# words = []
# for i in range(n):
#     string = input().split(' ')
#     for word in string:
#         words.append(word)
#
# d = {*[elem for elem in words if dictionary.count(elem.lower()) == 0]}
#
# print(*d, sep='\n')
# ============================================

# формируем множество известных слов на основании построчного ввода
dic = {input().lower() for _ in range(int(input()))}

# заводим пустое множество для приема текста
wrd = set()

# т.к. текст построчно подается, а также в каждой строке несколько слов,
# то каждую строку превращаем во множество и добавляем в единое множество wrd
for _ in range(int(input())):
    wrd |= {i.lower() for i in input().split()}

# на вывод отправляем результат вычитания словарного множества dic
# из текстового множества wrd; впереди ставим *, чтобы раскрыть поэлементно
print(*(wrd - dic), sep="\n")

# Основа работы кода - свойство множеств хранить только уникальные значения.
# wrd |= {...} отвечает за добавление множества {...} в единое wrd (аналог метода update)
# Обращаем внимание на звездочку *, которая вытаскивает элементы на вывод, вместо того, чтобы печатать в виде множества
#
# Немного подрихтовал код:
# 1) заменил ненужные символы переменных на _
# 2) заменил метод difference на оператор вычитания, чтобы добиться единообразия -
# использовать для действий с множествами либо операторы, либо методы, а не все одновременно

# ============================================

# Вариант 2

# d = [input().lower() for x in range(int(input()))]
# [print(x) for x in set([i for s in [input().lower().split() for x in range(int(input()))] for i in s]).difference(d)]

# ============================================
# # Вариант 3
# count_dict = int(input())
# dict = []
# check_words = []
# result = []
#
# #заполняем словарь
# for i in range(count_dict):
#   dict.append(input().lower())
#
# count_lines = int(input())
#
# #заполняем список проверяемых слов
# for i in range(count_lines):
#   check_words += input().lower().strip().split(' ')
#
# #выбираем слова которые не проходят проверку
# for i in check_words:
#   if i not in dict and i not in result:
#     result.append(i)
#
# #печатаем
# for i in result:
#   print(i)
# ============================================
# Вариант 4

# n = set()
# m = set()
# [n.add(input().lower()) for i in range(int(input()))]  # множество известных слов
# [{m.add(i) for i in (input().lower().split())} for i in range(int(input()))]  # множество слов текста
# print("\n".join(m - n))  # разница множеств
# ============================================
# Вариант 5

# # пустое множество
# a = set()
# # множество для словаря + к нижнему регистру
# dictionary = {input().lower() for i in range(int(input()))}
# # добавляем в множество результат двухмерного списка
# our_text = [[a.add(k) for k in input().split()] for j in range(int(input()))]
# # виводим i если ее нет в словаре
# [print(i) for i in a if i.lower() not in dictionary]
# ============================================
# Вариант 6

# 1. универсальная функция ввода возвращающая множество слов из ввода (в аргумент присваивается список слов).
# 2. вызываем 2 раза функцию, первый раз для формирования словаря, второй раз множества слов из текста.
# 3. печать разницы множеств текста и словаря слов.

# def f(s):
#     n = int(input())
#     for i in range(n):
#         s += input().lower().split()
#     return set(s)
#
#
# s1, s2 = [], []
# s1, s2 = f(s1), f(s2)
#
# print(*(s2 - s1), sep='\n')
# ============================================
# Вариант 7

# Создаем множество из известных слов:
dct = set([input().lower().strip() for i in range(int(input()))])

# Получаем nested list: [['a', 'bb', 'aab', 'aba', 'ccc'], ['c', 'bb', 'aaa']]
# txt = [input().lower().split() for i in range(int(input()))]

# Делаем из него flatten list: ['a', 'bb', 'aab', 'aba', 'ccc', 'c', 'bb', 'aaa']
# txt = [ word for lst in txt for word in lst ]

# переводим в множество: {'a', 'aaa', 'aab', 'aba', 'bb', 'c', 'ccc'}
# txt = set(txt)

# Все то же самое одной строкой:
txt = set([word for lst in [input().lower().split() for i in range(int(input()))] for word in lst])
print(*(txt - dct), sep='\n')