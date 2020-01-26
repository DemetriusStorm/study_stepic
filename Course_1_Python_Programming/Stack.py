class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]


s = Stack()
dic = [['(', ')'], ['[', ']'], ['{', '}']]
dic2 = [['(', '[', '{'], [')', ']', '}']]
targ = '[print(int(a[i - 1] + a[(i + 1) % len(a)]), end=' ') for i in range(len(a))]'
new_dic = []
finish_dic = []
print('Это наш справочник', dic)
print('Это наша цель', targ)

for element in targ:
    for i in element.split():
        # print('Есть кто в targ?', i)
        for skobki in dic:
            for j in skobki:
                if i == j:
                    # print('Есть кто равный?', i)
                    new_dic.append(i)

# for i in new_dic:
#     if i == dic

for value in new_dic:
    if value in dic2[0]:
        s.push(value)
    else:
        if s.empty():
            break
        elif s.peek() in dic2[0]:
            s.push(value)


# for key, value in new_dic:
#     finish_dic.append(value)
#     for key1, value1 in finish_dic:
#         if value in finish_dic:
#             pass

# s.push('(')
# s.push(')')
# s.push('[')
# s.push(']')

print('Последний элемент стека:', s.peek())
print('Это конечный сборщик данных', *new_dic)
print('Стек пуст?', s.empty())
print('Размер стека', s.size())
print('Стек состоит из', *s.items)
