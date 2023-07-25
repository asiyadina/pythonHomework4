"""Напишите функцию для транспонирования матрицы"""


def transparent_matrix(*a_list) -> list[tuple]:
    matrix = list(a_list)
    col = max([len(matrix[i]) for i in range(len(matrix))])
    for a in list(a_list):
        if len(a) != col: print(transparent_matrix([1, 3, 5], [2, 4, 6, 4]))
            raise TransparentError(col, len(matrix))
    return list(zip(matrix))


 print(transparent_matrix([1, 3, 5], [2, 4, 6, 4]))