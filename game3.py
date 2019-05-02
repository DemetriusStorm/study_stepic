import random

MAX_ERRORS = 8

words_list = ('автострада', 'бензин', 'инопланетянин', 'самолет',
              'библиотека', 'шайба', 'олимпиада')


def print_users_word(arg):
    print(''.join(arg))


secret_word = random.choice(words_list)
print(secret_word)

users_wors = ['*'] * len(secret_word)
print_users_word(users_wors)

errors_counter = 0
while True:
    letter = input('введите букву: ').lower()

    if len(letter) != 1 or not letter.isalpha():
        continue

    if letter in secret_word:
        idx = 0
        for idx, _char in enumerate(secret_word):
            if _char == letter:
                users_wors[idx] = letter
        if '*' not in users_wors:
            print('вы выйграли')
            print('\t\tбыло загадано слово:', secret_word)
            break
    else:
        errors_counter += 1
        # errors_counter++
        # errors_counter = errors_counter + 1
        print('\tсовершено ошибок:', errors_counter)
        if errors_counter == MAX_ERRORS:
            print('вы проиграли ;(')
            break

    print_users_word(users_wors)

print('до встречи')

