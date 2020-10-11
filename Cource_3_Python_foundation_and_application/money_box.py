"""
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет,
которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке,
предоставлять возможность добавлять монеты в копилку и узнавать,
можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
"""


class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.counter = 0

    def can_add(self, v):
        return True if v + self.counter <= self.capacity else False

    def add(self, v):
        if self.can_add(v):
            self.counter += v


box = MoneyBox(45)
print(f'capacity: {box.capacity}')
print(f'counter: {box.counter}')
box.add(44)
print(f'box: {box.counter}')
print(box.can_add(1))
box.add(1)
print(f'box: {box.counter}')
print(box.can_add(1))
box.add(1)
print(f'box: {box.counter}')
