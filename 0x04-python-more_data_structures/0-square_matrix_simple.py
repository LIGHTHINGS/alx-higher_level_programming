# #!/usr/bin/python3
# def square_matrix_simple(matrix=[]):
#     new_matrix = matrix.copy()

#     for i in range(len(matrix)):
#         new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

#     return (new_matrix)

def SquareList(L):
    if type(L) is list:
        return [SquareList(x) for x in L]
    else:
        return L**2

print(SquareList([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]))