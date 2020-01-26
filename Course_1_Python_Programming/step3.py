hours = ('1 час', '2 час', '3 час', '4 час')
worker_1 = (58.5, 97.63, 45.65, 12.12, 45.66)
worker_2 = (54.5, 17.63, 35.55, 12.17)

# result = list(zip(hours, worker_1, worker_2))
# print(result)

args = [hours, worker_1, worker_2]
result = list(zip(*args))
print(result)