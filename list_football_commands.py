# Напишите программу, которая принимает на стандартный вход список игр футбольных команд
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число n — количество завершенных игр.
# После этого идет n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
#
# Sample Input:
# 3
# Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2
#
# Sample Output:
# Зенит:2 2 0 0 6
# ЦСКА:2 0 1 1 1
# Спартак:2 0 1 1 1

# string = [
#     'Зенит;3;Спартак;1',
#     'Спартак;1;ЦСКА;1',
#     'ЦСКА;0;Зенит;2',
# ]
# dct = {}
# for i in range(0, len(string)):
#     item = string[i].split(';')
#     dct[item[0]] = [0, 0, 0]
#     dct[item[2]] = [0, 0, 0]
#
# for j in range(0, len(string)):
#     item = string[j].split(';')
#     if int(item[1]) > int(item[3]):
#         dct[item[0]][0] += 1
#         dct[item[2]][2] += 1
#     elif int(item[1]) < int(item[3]):
#         dct[item[0]][2] += 1
#         dct[item[2]][0] += 1
#     else:
#         dct[item[0]][1] += 1
#         dct[item[2]][1] += 1
#
# for key, value in dct.items():
#     res = value[0] * 3 + value[1]
#     value.insert(0, sum(value))
#     value.append(res)
#     print(key + ':', *value)

'''d = {}
for i in range(int(input())):
    t1, sc1, t2, sc2 = input().split(";")
    for k in (t1, t2):
        if k not in d: d[k] = [0, 0, 0]

    if sc1 < sc2:
        d[t1][2] += 1
        d[t2][0] += 1

    elif sc1 > sc2:
        d[t1][0] += 1
        d[t2][2] += 1

    else:
        d[t1][1] += 1
        d[t2][1] += 1

for t in d:
    print('%s:%i %i %i %i %i' % (t, sum(d[t]), *d[t], d[t][0] * 3 + d[t][1]))
'''

'''
import collections
n  = int(input())
d = dict()

for i in range(n):
    line =  input().split(';')
    d.setdefault(line[0], {'Всего_игр': 0,
                                               'Побед': 0,
                                               'Ничьих': 0,
                                               'Поражений': 0,
                                               'Всего_очков': 0})
    d.setdefault(line[2], {'Всего_игр': 0,
                                               'Побед': 0,
                                               'Ничьих': 0,
                                               'Поражений': 0,
                                               'Всего_очков': 0})
    d[line[0]]['Всего_игр'] += 1
    d[line[2]]['Всего_игр'] += 1
    if int(line[1]) > int(line[3]):
        d[line[0]] ['Побед'] += 1
        d[line[2]] ['Поражений'] += 1
        d[line[0]]['Всего_очков'] += 3
    elif int(line[1]) < int(line[3]):
        d[line[2]] ['Побед'] += 1
        d[line[0]] ['Поражений'] += 1
        d[line[2]]['Всего_очков'] += 3
    elif int(line[1]) == int(line[3]):
        d[line[2]] ['Ничьих'] += 1
        d[line[0]] ['Ничьих'] += 1
        d[line[2]]['Всего_очков'] += 1
        d[line[0]]['Всего_очков'] += 1
for key, val in d.items():
    print(key, end='' )
    print(': ', end='')
    print(val['Всего_игр'], val['Побед'], val['Ничьих'], val[ 'Поражений'], val['Всего_очков'])
'''

'''
r = {}
def add_r(d,k,a,b):
    if k not in d:
        d[k] = [0,0,0,0,0]
    d[k][0] += 1
    d[k][1] += a > b
    d[k][2] += a == b
    d[k][3] += a < b
    d[k][4] += 3 * (a > b) + (a == b)
for i in range(int(input())):
    a = input().split(';')
    add_r(r,a[0],a[1],a[3])
    add_r(r,a[2],a[3],a[1])
for i in r:
    print(i+':',*r[i])
'''
'''
dictionary={} # create empty dictionary
#positions of data in list by each command: Всего_игр, Побед, Ничьих, Поражений, Всего_очков
games,wins,draws,loss,points=0,1,2,3,4
n=int(input())# Input number of games
for i in range(n): 
    lst=input().split(';') #create list and split values by ';'
    key=lst[0] # 1-st command in the lst
    if key not in dictionary:
        dictionary[key]=[1,0,0,0,0] # create in dictioanry pare Key and list of data [Всего_игр, Побед, Ничьих, Поражений, Всего_очков] 
    else:
        dictionary[key][games]+=1 #count games
    #***
    key=lst[2] # 2-nd command in the lst
    if key not in dictionary:
        dictionary[key]=[1,0,0,0,0] # create in dictioanry pare Key and list of data [Всего_игр, Побед, Ничьих, Поражений, Всего_очков] 
    else:
        dictionary[key][games]+=1 #count games    
    
    #analyse score
    if lst[1]>lst[3]: 
        dictionary[lst[0]][wins]+=1 #1-st command win
        dictionary[lst[0]][points]+=3 #1-st command points
        dictionary[lst[2]][loss]+=1 #2-nd command loss
    elif lst[1]<lst[3]:  
        dictionary[lst[0]][loss]+=1 #1-st command loss
        dictionary[lst[2]][wins]+=1  #2-nd command win
        dictionary[lst[2]][points]+=3 #2-nd command points
    else: # score is equal
        dictionary[lst[0]][draws]+=1
        dictionary[lst[0]][points]+=1 #1-st command points
        dictionary[lst[2]][draws]+=1
        dictionary[lst[2]][points]+=1 #2-nd command points
        
for key,value in dictionary.items(): #get multitude pairs of dictionary
    print(key,end=':')
    print(*value)
'''

'''
a = {}
for i in range(int(input())):
    s = str(input()).split(';')
    if s[0] not in a:
        a[s[0]] = [0,0,0]
    if s[2] not in a:
        a[s[2]] = [0,0,0]
    if int(s[3]) > int(s[1]):
        a[s[2]][0] += 1
        a[s[0]][2] += 1
    elif int(s[3]) < int(s[1]):
        a[s[0]][0] += 1
        a[s[2]][2] += 1
    else:
        a[s[2]][1] += 1
        a[s[0]][1] += 1
for i in a.keys():
    print("%s:%d" % (i, sum(a[i])), *a[i], 3*a[i][0] + a[i][1])
'''

