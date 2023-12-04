#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in range(len(matrix)):
        for t in range(len(matrix[m])):
            print("{:d}".format(matrix[m][t]), end="")
            if t != (len(matrix[m]) - 1):
                print(" ", end="")
        print("")
