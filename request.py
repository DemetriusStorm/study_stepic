# import requests
#
# r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/699.txt')
# counter = 0
# for i in r.text.splitlines():
#     counter += 1
# print(counter)
# ================================================
# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
#
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
#
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
#
# Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
# Вариант 1
# import requests
#
# download_link = 'https://stepic.org/media/attachments/course67/3.6.3/'
# filename = '699991.txt'
# while filename:
#     print(filename)
#     r = requests.get(download_link + filename)
#     filename = None if r.text.startswith('We') else r.text
#
#     print(r.text)

# Вариант 2
# import requests
#
# url = "https://stepic.org/media/attachments/course67/3.6.3/"
# r = requests.get(url + "699991.txt")
# while not r.text.startswith("We"):
#     r = requests.get(url + r.text)
#     print(r.text)
# # print(r.text)
# ================================================
