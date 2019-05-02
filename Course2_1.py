# n = int(input())
# sums = 0
#
# for i in range(n):
#     elem = int(input())
#     sums += elem
#
# print(sums)
#
# # print(sum([int(input()) for i in range(int(input()))]))
# # print(sum([int(input()) for _ in range(int(input()))]))


# x = [1, 2, 3]
# print(id(x))
# print(id([1, 2, 3]))

# x = [1, 2, 3]
# y = x
# print(y is x)
# print(y is [1, 3, 4])

# x = [1, 2, 3]
# y = x
# print(y is x)
# x.append(4)
# print(x)
# print(y)
# # Идентификатор объекта – это целое число
# # Идентификаторы всех объектов уникальны


# x = [1, 2, 3]
# y = x
# y.append(4)
#
# s = "123"
# t = s
# t = t + "4"
#
# print(str(x) + " " + s)

# objects = [1, 2, 1, 2, 3, 5, 5, 5, 3, 6]
# objects2 = objects
# print(objects)
# print(set(objects2))
#
# print(len({id(x) for x in objects}))
# print(len(set(map(id, objects))))
# print(len(set([id(i) for i in objects])))
# n = []
# for i in objects:
#     if i not in n:
#         n.append(i)
# print(len(n))
#
#
# def list_sum(lst):
#     result = 0
#     for element in lst:
#         result += element
#     return result
#
#
# def sum(a, b):
#     return a + b
#
#
# y = sum(14, 29)
# z = list_sum([1, 2, 3])
# print(y)
# print(z)

# a = []
# def foo(arg1, arg2):
#     a.append("foo")
# foo(a.append("arg1"), a.append("arg2"))
# print(a)

#
# def g():
#     print('я в функции g')
# def f():
#     print('я в функции f')
#     g()
#     print('я в функции f')
#
# print('я вне функций')
# f()
# print('я вне функций')


# x = [1, 2, 3]
#
# x.append(4)
# x.append(5)
#
# print(x)
#
# top = x.pop()
# print(top)
# print(x)
#
# top = x.pop()
# print(top)
# print(x)

# x = print(4)
#
# print(type(x))
# print(x)
# print(type(print(4)))
# x = int()
# print(type(x))

# def closest_mod_5(x):
#     y = int()
#     y = x
#     while y % 5 != 0:
#         y += 1
#     return y
#
#
# '''
# return x if x % 5 == 0 else closest_mod_5(x + 1)
# '''
# '''
#     return (x + 4) // 5 * 5
# '''
#
# print(closest_mod_5(11))


# '''def function_name([ positional_args,
#                   [ postitional_args_with_default,
#                   [ *pos_args_name,  # Картеж
#                   [ keywowd_only_args,
#                   [ **kw_args_name]]]]]):  # Словарь
# '''
#
#
# def printab(a, b=10, *args, c=10, d, **kwargs):
#     print(a, b, c, d)
#
# printab(15, d=15)
#
# def s(a, *vs, b=10):
#    res = a + b
#    for v in vs:
#        res += v
#    return res
#
# print(s(11, 10))
# print(s(0, 0, 31))
# print(s(11, b=20))
# print(s(11, 10, b=10))
# print(s(5, 5, 5, 5, 1))
# print(s(11, 10, 10))
# #print(s(b=31))
# print(s(21))
# #print(s(b=31, 0))


# def nik(n, k):
#     if k == 0:
#         return 1
#     if k > n:
#         return 0
#     else:
#         return nik(n - 1, k) + nik(n - 1, k - 1)
#
#
# n, k = map(int, input().split())
# print(nik(n, k))


# class Node(object):
#     def __init__(self, ns, parent=None):
#         self.ns = ns
#         self.parent = parent
#         self.v = set()
#
#
# class Tree(object):
#     def __init__(self):
#         self.d = {'global': Node('global')}
#
#     def create_ns(self, ns, parent):
#         n = self.d[parent]
#         self.d[ns] = Node(ns, n)
#
#     def add_var(self, ns, var):
#         n = self.d[ns]
#         n.v.add(var)
#
#     def find_var(self, ns, var):
#         name = ns
#         while True:
#             n = self.d[name]
#             if var in n.v:
#                 return n.ns
#             if not n.parent:
#                 return None
#             name = n.parent.ns
#
#
# # t = '''\
# # add global a
# # create foo global
# # add foo b
# # get foo a
# # get foo c
# # create bar foo
# # add bar a
# # get bar a
# # get bar b'''
#
# tree = Tree()
# t = int(input())
# for line in range(t):
# # for line in t.split('\n'):
#     cmd, namesp, arg = input().split(' ')
#     if cmd == 'create':
#         tree.create_ns(namesp, arg)
#     elif cmd == 'add':
#         tree.add_var(namesp, arg)
#     elif cmd == 'get':
#         print(tree.find_var(namesp, arg))

# Пример решения. Будем хранить две структуры:
# 1) Кто чей родитель
# 2) Переменные объявленные в данном пространстве имён
#
# Если команда create -- создаём новое пространство имён
# (запоминаем родителя и создаём пустое множество переменных, объявленных в этом пространстве имен).
#
# Если команда add -- то просто помещаем имя переменной в соответствующее множество.
#
# Если команда get -- то проверяем наличие данной переменной в нашем пространстве имён, если не нашли:
# проверяем в родителе. Если не нашли в родителе, проверяем в родителе родителя и так далее.
# Как только нашли имя переменной -- вывели на экран пространство имён, в котором нашли.
# Если в процессе поиска мы имя не нашли (fst is None) -- выводим None на экран.

# n = int(input())
#
# parent = {"global": None}
# vs = {"global": set()}
#
# for _ in range(n):
#     t, fst, snd = input().split()
#     if t == "create":
#         parent[fst] = snd
#         vs[fst] = set()
#     elif t == "add":
#         vs[fst].add(snd)
#     else:  # t == get
#         while fst is not None:
#             if snd in vs[fst]:
#                 break
#             fst = parent[fst]
#         print(fst)


# dct = {'global': ['None']}  # словарь списков(родитель,переменные)
# for ops, nms, v in [input().split() for i in range(int(input()))]:  # цикл операций
#     if ops == 'create':
#         dct[nms] = [v]  # создать пространство-новый список в словаре
#     elif ops == 'add':
#         dct[nms].append(v)  # новая переменная-добавить в список
#     elif ops == 'get':  # поиск переменной (циклом)
#         while nms != 'None' and v not in dct[nms]:  # если нет в пространстве-меняем на родителя(пока не None)
#             nms = dct[nms][0]
#         print(nms)


# put your python code here
# Словарь пространтсва имен,
# ключи - наши пронстранства имен
# Значения - словарь с двумя значениями:
#   потомок (если пространтсво имен global, то None)
#   переменные пронстрантства


# spaces = {'global': {'parrent': None, 'values': []}}
#
#
# def create(namespace, parent='global'):
#     '''
#     Добпавляет новое пространство имен, по умолчанию родитель - global
#     :param namespace:   пронстранство имен
#     :param parent: потомок (по умолчанию global)
#     :return: Null
#     '''
#     spaces[namespace] = {'parrent': parent, 'values': []}
#
#
# def add(namespace, var):
#     '''
#     Добавляет переменную в пронстранство имен
#     :param namespace:  пронстранство имен
#     :param var: переменная
#     :return:
#     '''
#     spaces[namespace]['values'].append(var)
#
#
# def get(namespace, var):
#     '''
#     Возвращает име пронстранство имен, если переменная принадлежит заданному пронстрантству имен
#     в противном случае идет вверх до global
#     :param namespace:  пронстранство имен
#     :param var: переменная
#     :return: пронстранство имен или родитель (до global)
#     '''
#     if var in spaces[namespace]['values']:
#         return namespace
#     if namespace == 'global':
#         return None
#     return get(spaces[namespace]['parrent'], var)
#
#
# for i in range(int(input().strip())):
#     cmd, namesp, arg = input().split()
#     if cmd == 'get':
#         print(get(namesp, arg))
#     elif cmd == 'add':
#         add(namesp, arg)
#     elif cmd == 'create':
#         create(namesp, arg)


namespace = {'global': {'parent': 'None', 'childrens': []}}


def create(a, b):
    namespace[b]['childrens'].append(a)
    namespace[a] = {'parent': b, 'childrens': []}


def add(a, b):
    namespace[a]['childrens'].append(b)
    namespace[b] = {'parent': a}


def get(a, b):
    if b in namespace[a]['childrens']:
        print(a)
    else:
        if namespace[a]['parent'] != 'None':
            get(namespace[a]['parent'], b)
        else:
            print('None')


for i in range(int(input())):
    f, a, b = input().split()
    globals()[f](a, b)
