#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    #if not matrix:
        #return None
    for submatrix in matrix:
        #if len(submatrix) == 0:
            for i in range(len(submatrix)):
                print("{:d}".format(submatrix[i]),end=" ")
            print()
