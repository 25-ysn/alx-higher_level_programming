#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for x in range(len(matrix)):
            for item in range(len(matrix[x])):
                if item != len(matrix[x]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[x][item]), end=endspace)
            print()
