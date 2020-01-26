# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
    splits = word.split(x)
    return (len(splits) - 1)


# Uncomment these function calls to test your  function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))


# should print 1

# ==========================================================
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
    start_ind = word.find(start)
    end_ind = word.find(end)
    if start_ind > -1 and end_ind > -1:
        return (word[start_ind + 1:end_ind])
    return word


# Uncomment these function calls to test your tip function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))


# should print "apple"

# ==========================================================

# Write your every_other_letter function here:
def every_other_letter(word):
    every_other = ""
    for i in range(0, len(word), 2):
        every_other += word[i]
    return every_other


# Uncomment these function calls to test your tip function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))


# should print

# ==========================================================
# Write your reverse_string function here:
def reverse_string(word):
    reverse_word = ""
    reverse_word = word[::-1]
    return reverse_word


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))


# should print

# ==========================================================
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
    end_word1 = word2[:1] + word1[1:]
    end_word2 = word1[:1] + word2[1:]
    end_word = end_word1 + " " + end_word2
    return end_word


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))


# should print b a
# ==========================================================
# Write your add_exclamation function here:
def add_exclamation(word):
    while (len(word) < 20):
        word += "!"
    return word


# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
# ==========================================================
# Import datetime from datetime below:
from datetime import datetime

current_time = datetime.now()
print(current_time)
# ==========================================================
# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1,101) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)
# ==========================================================
