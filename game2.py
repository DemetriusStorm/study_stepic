import random

# PEP-8
words_list = ('автострада', 'бензин', 'инопланетянин', 'самолет',
             'библиотека', 'шайба', 'олимпиада')


def print_users_word(arg):
   print(''.join(arg))


secret_word = random.choice(words_list)
print(secret_word)

users_wors = ['*'] * len(secret_word)
print_users_word(users_wors)

# # print(secret_word[2])
# users_wors[2] = 'у'
# print_users_word(users_wors)

while True:
    letter = input('введите букву: ').lower()

    if len(letter) != 1 or not letter.isalpha():
        continue
    #print(ord(letter)) Сделать ввод только на русском!!!
    print(letter)

