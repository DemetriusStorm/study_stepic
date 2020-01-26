#File name new_file.py

dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

index = 3
while index < len(dog_breeds):
  print(dog_breeds[index])
  index += 1


#Write your function here вывод индекса на одинаковых элементах списков
def same_values(lst1, lst2):
  new_lst = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      new_lst.append(i)
  return new_lst


def common_letters(string_one, string_two): # добавляет в common уникальные символы, если символ а из string_one есть в string_two
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common


first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_password


def get_length(word): #длина строки
  counter = 0
  for letter in word:
    counter += 1
  return counter



temp_password = password_generator(first_name, last_name)
print(temp_password)

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


def username_generator(first_name, last_name):
  if len(first_name) < 3:
    user_name = first_name
  else:
    user_name = first_name[:3]
  if len(last_name) < 4:
    user_name += last_name
  else:
    user_name += last_name[:4]
  return user_name

def password_generator(user_name):
  password = ""
  for i in range(0, len(user_name)):
    password += user_name[i - 1]
  return password

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)
#===================================================
author_names = authors.split(',')

print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])

print(author_last_names)
#===================================================
spring_storm_lines = spring_storm_text.split('\n')
spring_storm_lines = spring_storm_text.split('\t')
reapers_line_one = ' '.join(reapers_line_one_words)
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
disown_placement = god_wills_it_line_one.find("earth")
#===================================================
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms',
                    '           like flowering mines    ', '\n', '   to conquer me home.    ']

love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
  love_maybe_lines_stripped.append(line.strip())

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)
#===================================================
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

my_beard_description = poem_description(author = "Shel Silverstein",
title = "My Beard",
original_work = "Where the Sidewalk Ends",
publishing_date = "1974"
)
print (my_beard_description)
#===================================================
#.upper(),.title() и.lower() изменяют регистр строки.
#.split() принимает  строку и создает список подстрок.
#.join() берет список строк и создает строку.
#.strip() удаляет  пробелы или другие шумы в начале и концес троки.
#.replace() заменяет все вхождения символа / строки в строке другим символом / строкой.
#.find() ищет строку для символа / строки  и возвращает значение индекса, в котором находится символ / строка.
#.format() и f - строки позволяют вам интерполировать строку с переменными.
#

def print_some_characters(word):
  for i in range(len(word)):
    if i % 2 == 0:
      print(word[i])

print_some_characters("watermelon")

