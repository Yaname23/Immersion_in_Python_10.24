"""Напишите функцию для транспонирования матрицы"""

matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

def transpose(matrix):
    return list( map( lambda x: list(x), zip(*matrix) ) )

print(transpose(matrix))
