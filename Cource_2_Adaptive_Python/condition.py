def solution(string):
    result = []
    [result.append(element) for element in string if element not in result]
    # print(list(result).sort())
    return ''.join(result)


def solution2(string2):
    res = []
    for i in set(string2):
        for y in res:
            if i > res[y]:
                res.append(y)
    return res
    # return ''.join(set(string2))

x = 'asdasdssadadfghhh'
y = []
for i in x:
    if i not in y:
        y.append(i)
print(''.join(y))

print(solution('asdasdssadadfghhh'))
print(solution2('asdasdssadadfghhh'))
