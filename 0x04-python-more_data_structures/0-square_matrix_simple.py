#!/usr/bin/python3
 def square_matrix_simple(matrix=[]):
     new_matrix = matrix.copy()

     for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

        return (new_matrix)

# def square_matrix_simple(L):
#    if type(L) is list:
#        return [square_matrix_simple(x) for x in L]
#    else:
#        new_matrix = L**2
#        return new_matrix
