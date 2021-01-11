import numpy as np
import random
# sudoku = [[0 for _ in range(0, 9)] for _ in range(0, 9)]


def sudo(sudoko):
    for i in range(0, 9):
        for j in range(1, 10):
            if j != sudoku[0][i] and j != sudoku[i][0]:
                sudoku[i][j] == j
                sudo(sudoku)
                sudoku[i][j] == 0
    return sudoku


sudok = """400000805
030000000
000700000
020000060
000080400
000010000
000603070
500200000
104000000"""
sudoku = []
for i in sudok.split():
    row = [j for j in i]
    sudoku.append(row)

print(sudo(sudoku))
