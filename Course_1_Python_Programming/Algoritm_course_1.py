# # Методы сортировки.
# # Квадратиные сортировки O(N^2)
# # 1. Метод вставки (insert sort)
# # 2. Метод выбора (choice sort)
# # 3. Метод пузырька (bubble sort)
#
#
# def insert_sort(a):
#     """ сортировка списка А вставками """
#     n = len(a)
#     for top in range(1, n):
#         k = top
#         while k > 0 and a[k - 1] > a[k]:
#             a[k], a[k - 1] = a[k - 1], a[k]
#             k -= 1
#
#
# def choice_sort(a):
#     """ сортировка списка А выбором """
#     n = len(a)
#     for pos in range(0, n - 1):
#         for k in range(pos + 1, n):
#             if a[k] < a[pos]:
#                 a[k], a[pos] = a[pos], a[k]
#
#
# def bubble_sort(a):
#     """ сортировка списка А методом пузырька """
#     n = len(a)
#     for bypass in range(1, n):
#         for k in range(0, n - bypass):
#             if a[k] > a[k + 1]:
#                 a[k], a[k + 1] = a[k + 1], a[k]
#
#
# def test_sort(sort_algorithm):
#     print("Тестируем:", sort_algorithm.__doc__)
#     print("test_case #1: ", end="")
#     a = [4, 2, 5, 1, 3]
#     a_sorted = [1, 2, 3, 4, 5]
#     sort_algorithm(a)
#     print("OK" if a == a_sorted else "Fail")  # тернарный условный оператор
#
#     print("test_case #2: ", end="")
#     a = list(range(10, 20)) + list(range(0, 10))
#     a_sorted = list(range(20))
#     sort_algorithm(a)
#     print("OK" if a == a_sorted else "Fail")  # тернарный условный оператор
#
#     print("test_case #3: ", end="")
#     a = [4, 2, 4, 2, 1]
#     a_sorted = [1, 2, 2, 4, 4]
#     sort_algorithm(a)
#     print("OK" if a == a_sorted else "Fail")  # тернарный условный оператор
#
#
# if __name__ == "__main__":
#     test_sort(insert_sort)
#     test_sort(choice_sort)
#     test_sort(bubble_sort)
#
# # Методы сортировки.
# # Сортировка подсчетом O(N)
#
# n = 60
# f = [0] * 10
# for i in range(n):  # частотный анализ
#     x = int(input())
#     f[x] += 1
#     for digit in range(10):
#         print(digit)
#
# ======================================================================
# # Рекурсия. Матрешка.
#
#
# def matryoshka(n):
#     if n == 1:  # последняя маленькая матрешка
#         print("Матрёшка")
#     else:
#         print("Верх матрешки", n)
#         matryoshka(n - 1)
#         print("Низ матрешки n=", n)
#
#
# matryoshka(5)

# # Факторил
# def f(n):
#     assert n >= 0, "Факториал отрицательный не определен"
#     if n == 0:
#         return 1
#     print(n)
#     return f(n-1) * n
#
#
# f(56)
# ======================================================================
# # Алгоритм Евклида
#
#
# def gcd(a, b):
#     """ Два отрезка, какой длины орезок будет больше кратным А и одновременно кратным Б
#     (Наибольший общий делитель) GCD """
#     return a if b == 0 else gcd(b, a%b)
#
#
# print(gcd(6, 45))

# # Быстрое возведение в степень
#
#
# def pow(a:float, n:int):
#     if n == 0:
#         return 1
#     elif n%2 == 1:  # нечет
#         return pow(a, n-1)*a
#     else:  # n- четное
#         return pow(a**2, n//2)
#
# print(pow(6, 10000))
# ======================================================================

# Ханойские башни
# ..................
# Генерация всех перестановок


def gen_bin(m, prefix=""):
    if m == 0:
        print(prefix)
        return
    gen_bin(m - 1, prefix + "0")
    gen_bin(m - 1, prefix + "1")


def gen_bin_for(m, prefix=""):
    if m == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(m - 1, prefix + digit)


def generate_numbers(n: int, m: int, prefix=None):
    """ Генерирует все чисел (с лидирующими нулями)
        в n-ричной системе счисления (n <= 10)
        длины m
    """
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for digit in range(n):
        prefix.append(digit)
        print("добавили цифру", digit)
        generate_numbers(n, m - 1, prefix)
        prefix.pop()
        print("удалили из списка цифру", digit)


# только для двоичной СС (системы счисления)
# gen_bin(5)  # вариант1
# gen_bin_for(5)  # вариант2


# для произвольной СС (системы счисления)
# generate_numbers(2, 5)  # вариант3

# ======================================================================
def find(number, a):
    """ ищет x в a и возвращает True, если такой есть
        False, если такого нет """

    for x in a:
        if number == x:
            return True
    return False


def generate_permutations(n: int, m: int = -1, prefix=None):
    """ Генерация всех перестановок n числе в m позициях,
        с префиксом prefix """

    m = n if m == -1 else m  # по умолчанию n чисел m позициях
    prefix = prefix or []
    if m == 0:
        print(*prefix, end=", ", sep="")
        return
    for number in range(1, n + 1):
        if find(number, prefix) in prefix:
            continue
        prefix.append(number)
        generate_permutations(n, m - 1, prefix)
        prefix.pop()


# generate_permutations(3, 3)
# ======================================================================
# РЕКУРРЕНТНЫЕ СОРТИРОВКИ:
# 1. Быстрая сортировка Тони Хоара (QuickSort)
# W(N * log_2(N))
# по скорость как O(N^2)
# сортирующее действие на прямом ходу рекурсии
# может быть реализована без дополнительной памяти
# относится к алгоритмам "Разделяй и влавствуй"

def hoar_sort(a):
    if len(a) <= 1:
        return  # return None
    barrier = a[0]
    left = []
    middle = []
    right = []
    for x in a:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    hoar_sort(left)
    hoar_sort(right)
    k = 0
    for x in left + middle + right:
        a[k] = x
        k += 1
    return a


# a = [1, 3, 5, 9, 7, 8, 2, 3, 4, 6, 0, 9]
# print(hoar_sort(a))

# 2. Сортировка слиянием (слияние отсортированных массивов в один)
# O(N * log(N))
# сортирующее действие на обратном ходу рекурсии (возвращаемся)
# нужна дополнительная память (нужно запамянать O(N) доп. памяти (медленнее)
# !!! Сортировка называется УСТОЙЧИВОЙ, если она не меняет порядок равных элементов

def merge(a: list, b: list):
    c = [0] * (len(a) + len(b))
    print("Это входные данные массивов A и B", a, b)
    print("Это исходный массив С с нулями:", c)
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:  # УСТОЙЧИВЫЙ ПОРЯДОК СОРТИРОВКИ <=
            c[n] = a[i]
            i += 1
            n += 1
            print("Это c", c)
        else:
            c[n] = b[k]
            k += 1
            n += 1
            print("Это c", c)
    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
        print("Это c", c)
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
        print("Это c", c)
    print("Это готовый список С:", c)
    return c


# Рекурсивная (рекуррентная) функция сортировки)

def merge_sort(a):
    if len(a) <= 1:
        return
    middle = len(a) // 2
    left = [a[i] for i in range(0, middle)]
    right = [a[i] for i in range(middle, len(a))]
    merge_sort(left)
    merge_sort(right)
    c = merge(left, right)
    for i in range(len(a)):
        a[i] = c[i]


# a = [1, 3, 5, 9, 7, 8, 2, 3, 4, 6, 0, 9]
# merge_sort(a)

# ======================================================================
# проверка массива, отсортирован или нет
# проверка по умолчанию, что массив отсротирован по возрастанию (ascending=True)

def check_sorted(a, ascending=True):
    """ Проверка отсортированности за O(len(a)) (О(N))"""
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0, a - 1):
        if s * a[i] > s * a[i + 1]:
            flag = False
            break
    return flag

# ======================================================================
# Бинарный поиск в массиве
# Требования:
# Массив должен быть отсортирован (в данном случае по возрастанию)
# Разбиваем массив на две границы, левую и правую.
# Элемент ЛЕВОЙ границы должен быть меньше искомого числа.
# Элемент ПРАВОЙ границы может равняться искомому числу.
# т.о. мы сближаем границы.


def left_bound(a, key):  # key - искомый элемент/ ИЩЕМ ЛЕВУЮ ГРАНИЦУ
    left = -1
    right = len(a)
    while (left - right) > 1:
        middle = (left + right) // 2
        if a[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(a, key):  # key - искомый элемент/ ИЩЕМ ПРАВУЮ ГРАНИЦУ
    left = -1
    right = len(a)
    while (left - right) > 1:
        middle = (left + right) // 2
        if a[middle] <= key:
            left = middle
        else:
            right = middle
    return right

# ======================================================================
# Обратная польская нотация.
# Алгоритм вычисления арифметических выражений в постфиксной нотации (записи)
# На пример:
# [5, 2, '+'] == 5+2
# (2+7)*5 == [2,7,'+',5,'*']
# 2+7*5 = [2,7,5,'*','+']
# Для каждого токена:
# Если токен (элемент списка) - число, то мы его кладем в стек,
# иначе - он операция.
# В этом случае берем со стека y = pop(), x = pop() (берем два числа)
# Вычисляем z = x операция y
# Результат операции кладем в стек push(z)
# Результат rezult = pop()
# ======================================================================
