# Транспонирование матрицы
matrix = [[0.5, 0, 0, 0, 0],
         [1, 0.5, 0, 0, 0],
         [1, 1, 0.5, 0, 0],
         [1, 1, 1, 0.5, 0],
         [1, 1, 1, 1, 0.5]]

matrix_t = list(zip(*matrix)) #zip -

for item in matrix:
    print(item)

print('*'*25)

for item in matrix_t:
    print(list(item))


