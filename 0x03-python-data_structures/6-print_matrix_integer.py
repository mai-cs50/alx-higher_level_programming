#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return None
    for submatrix in matrix:
        if len(submatrix) == 0:
            print()
        for i in range(len(submatrix)):
            if i == len(submatrix) - 1:
                print("{:d}".format(submatrix[i]))
            else:
                print("{:d}".format(submatrix[i]), end=" ")
