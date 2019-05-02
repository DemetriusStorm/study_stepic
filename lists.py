# def count_chars(string, char):
#     index = len(string) - 1
#     result = 0
#     while index >= 0:
#         if string[index] == char:
#             result += 1
#         index -= 1
#     return result
#
#
# string = 'If I look back I am lost'
# print(count_chars(string, 'I'))  # => 3
# print(count_chars(string, 'z'))  # => 0
# print(count_chars(string, 'o'))  # => 3

#
# def get_even_numbers_up_to(number):
#     counter = 1
#     result = ''
#
#     while counter <= number:
#         if counter % 2 == 0:
#             result += str(counter) + ','
#         counter += 1
#
#     new_result = result[:-1] + result[-1].replace(',', '.')
#     return new_result
#
#
# print(get_even_numbers_up_to(8))


# def does_contain(string, letter):
#     index = len(string)-1
#     while index >= 0:
#         if string[index] != letter:
#             index -= 1
#             if string[index] == letter:
#                 return True
#     return False
#
#
# def does_contain1(string, char):
#     index = 0
#     while index < len(string):
#         if string[index] == char:
#             return True
#         index += 1
#     return False
#
#
# print(does_contain('Renly', 'R'))  # => True
# print(does_contain('Renly', 'r'))  # => False
# print(does_contain('Tommy', 'm'))  # => True
# print(does_contain('Tommy', 'd'))  # => False

emps = [{"name": "John",
         "ser_num": (6345, 5489754)}]

# Берем нулевой элемент списка который является словарем первым параметром
# Вторым параметром берем ключ по имени,
# на выходе получаем множество из двух значений,
# которые присваем два переменным ser и num
ser, num = emps[0]["ser_num"]

print(emps[0]["name"], ":", emps[0]["ser_num"])
