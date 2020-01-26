# Проверка корректности скобочной последовательности( СП/СВ )
# Корректным СП называют:
# 1. Пустое скобочное выражение: A = ""
# 2. Любое корректное скобочное выражение взятое в скобки B = (A)
# 3. Любые два скобочных выражения записанные рядом C = AB
# "((()))()()()" - корректно
# "())(()" - некорректно
# ===============
# B = [A]
# "[(())]([])" - корректно
# "[)", "[(])" - некорректно
# СТЭК
# Для очередной скобки, если она открывающаяся, тогда запись в СТЕК
# Если закывающаяся(иначе), проверка, если стек пуст, условие не корректное
# Иначе, x = pop() - удаляем верхнюю скобку из стека, после сравниваем,
# Если x НЕ соответствует y (очередной скобке), выход(ретурн)
# Если стек пуст, то корректно, иначе нет.


import a_stack


def is_braces_sequence_correct():
    """
    Проверяет корреткность скобочной последовательноси из кругнлых и квадртных скобок
    () []
    >>> is_braces_sequence_correct("(([()]))[]")
    True
    >>> is_braces_sequence_correct("([)]")
    False
    >>> is_braces_sequence_correct("(")
    False
    >>> is_braces_sequence_correct("]")
    False
    """

    for brace in s:
        if brace not in "()[]{}":
            continue
        if brace in "([{":
            a_stack.push(brace)
        else:
            assert brace in ")]}", "Ожидалась закрывающая сскобка: " + str(brace)
            if a_stack.is_empty():
                return False
            left = a_stack.pop()
            assert left in "([{", "Ожидалась открывающая скобка: " + str(brace)
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            elif left == "{":
                right = "}"
            if right != brace:
                return False
    return a_stack.is_empty()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
