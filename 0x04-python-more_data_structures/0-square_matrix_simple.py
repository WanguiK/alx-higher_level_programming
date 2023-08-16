#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            squared_num = num**2
            new_row.append(squared_num)
        new_matrix.append(new_row)
    return (new_matrix)
