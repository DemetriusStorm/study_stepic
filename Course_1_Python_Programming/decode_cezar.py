"""
|Шифр Цезаря заключается в замене каждого символа входной строки на символ,
находящийся на несколько позиций левее или правее его в алфавите.
Для всех символов сдвиг один и тот же. Сдвиг циклический,
т.е. если к последнему символу алфавита применить единичный сдвиг, то он заменится на первый символ, и наоборот.
Напишите программу, которая шифрует текст шифром Цезаря.
Используемый алфавит −
пробел и малые символы латинского алфавита: ' abcdefghijklmnopqrstuvwxyz'

Формат ввода:
На первой строке указывается используемый сдвиг шифрования: целое число. Положительное число соответствует сдвигу вправо
На второй строке указывается непустая фраза для шифрования. Ведущие и завершающие пробелы не учитывать.

Формат вывода:
Единственная строка, в которой записана фраза: Result: "..." ,
где вместо многоточия внутри кавычек записана зашифрованная последовательность.

Sample Input 1:
3
i am caesar
Sample Output 1:
Result: "lcdpcfdhvdu"

Sample Input 2:
-2
az
Sample Output 2:
Result: "zx"

Sample Input 3:
27
abc
Sample Output 3:
Result: "abc"
"""

# def for_coding():
#     alfavit = ' abcdefghijklmnopqrstuvwxyz'
#     zdvig = 3
#     fraza = 'abc def'
#     # zdvig = int(input('Введите целое число, используемый сдвиг: '))
#     # fraza = input('Введите фразу которую необхдоимо зашифровать: ')
#     result = ''
#
#     for letter in fraza:
#         for alfa in alfavit:
#             if letter == alfa:
#                 result += alfavit[(alfavit.index(alfa)):(alfavit.index(alfa)):zdvig]
#
#     # return 'Result: '.join(result)
#     return result
#
#
# print(for_coding())

alfavit = ' abcdefghijklmnopqrstuvwxyz'
zdvig = -2
fraza = 'az'
result = ''

for letter in fraza:
    for alfa in alfavit:
        if letter == alfa:

            if len(alfavit) > zdvig > 0:
                result += alfavit[alfavit.index(alfa) + zdvig]

            elif zdvig >= len(alfavit):
                zdvig -= len(alfavit)
                result += alfavit[alfavit.index(alfa) - zdvig]

            elif zdvig < 0:
                # alfavit = alfavit[::-1]
                print(alfavit)
                # zdvig = len(alfavit) - zdvig
                # result += alfavit[alfavit.index(alfa) + zdvig]
                # print(alfavit[alfavit.index(alfa) + abs(zdvig)])
print(result)
