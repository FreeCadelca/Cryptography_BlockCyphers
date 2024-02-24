from AlphabetConfig import *
from Matrix2x2 import Matrix2x2
from Matrix3x3 import Matrix3x3
from IntMod import IntMod


class HillCypher:
    def __init__(self, key):
        self.__key = Matrix2x2(key)

    def encrypt(self, x, key=None):
        if not key:
            key = self.__key
        y = ''
        if len(x) % 2 != 0:
            x += 'a' * (2 - len(x) % 2)
        for k in range(0, len(x), 2):
            block_x = x[k:k + 2]
            block_x_matrix = Matrix2x2([[IntMod(A_ID[i])] for i in block_x])
            block_y_matrix = key * block_x_matrix
            block_y = ''.join([str(A[i[0].getValue()]) for i in block_y_matrix.matrix])
            y += block_y
        return y

    def decrypt(self, y):
        return self.encrypt(y, self.__key.inv())

    def info(self):
        matrix = self.__key.matrix
        max_len = len(str((max(max(i) for i in matrix))))
        tab = max_len + 1
        print(f'key:')
        for i in range(len(matrix)):
            if i == 0:
                print('/', end='')
            elif i == len(matrix) - 1:
                print('\\', end='')
            else:
                print('|', end='')

            for j in range(len(matrix[i])):
                spacing = ' ' * (tab - len(str(matrix[i][j]))) if j != len(matrix[i]) - 1 else ''
                print(matrix[i][j], end=spacing)

            if i == 0:
                print('\\')
            elif i == len(matrix) - 1:
                print('/')
            else:
                print('|')
        print()
