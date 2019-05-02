import random

words_list = ('автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека', 'шайба', 'олимпиада')

secret_word = random.choice(words_list)
print(secret_word)

users_word = ['*'] * len(secret_word)

users_word[2] = 'у'
print(''.join(users_word))

