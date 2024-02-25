from AlphabetConfig import *
from Matrix2x2 import Matrix2x2
from Matrix3x3 import Matrix3x3
from IntMod import IntMod


class RecHillCypher:
    def __init__(self, key_1, key_2):
        self.__key_1 = Matrix2x2(key_1)
        self.__key_2 = Matrix2x2(key_2)

    def encrypt(self, x):
        key_1 = self.__key_1
        key_2 = self.__key_2
        keys = [key_1, key_2]
        y = ''
        if len(x) % 2 != 0:
            x += 'z' * (2 - len(x) % 2)
        for k in range(0, len(x), 2):
            block_x = x[k:k + 2]
            block_x_matrix = Matrix2x2([[IntMod(A_ID[i])] for i in block_x])

            key = None
            if k == 0:
                key = keys[0]
            elif k == 2:
                key = keys[1]
            else:
                keys.append(keys[-2] * keys[-1])
                key = keys[-1]
            block_y_matrix = key * block_x_matrix
            block_y = ''.join([str(A[i[0].getValue()]) for i in block_y_matrix.matrix])
            y += block_y
        return y

    def decrypt(self, y):
        keys = [self.__key_1, self.__key_2]
        x = ''
        if len(y) % 2 != 0:
            y += 'a' * (2 - len(y) % 2)
        for k in range(0, len(y), 2):
            block_y = y[k:k + 2]
            block_y_matrix = Matrix2x2([[IntMod(A_ID[i])] for i in block_y])

            key = None
            if k == 0:
                key = keys[0]
            elif k == 2:
                key = keys[1]
            else:
                keys.append(keys[-2] * keys[-1])
                key = keys[-1]
            block_x_matrix = key.inv() * block_y_matrix
            block_x = ''.join([str(A[i[0].getValue()]) for i in block_x_matrix.matrix])
            x += block_x
        return x

    def info(self):
        matrix_1, matrix_2 = self.__key_1.matrix, self.__key_2.matrix
        max_len_1 = len(str((max(max(i) for i in matrix_1))))
        tab = max_len_1 + 1
        print(f'key_1:')
        for i in range(len(matrix_1)):
            if i == 0:
                print('/', end='')
            elif i == len(matrix_1) - 1:
                print('\\', end='')
            else:
                print('|', end='')

            for j in range(len(matrix_1[i])):
                spacing = ' ' * (tab - len(str(matrix_1[i][j]))) if j != len(matrix_1[i]) - 1 else ''
                print(matrix_1[i][j], end=spacing)

            if i == 0:
                print('\\')
            elif i == len(matrix_1) - 1:
                print('/')
            else:
                print('|')
        print()

        max_len_2 = len(str((max(max(i) for i in matrix_2))))
        tab = max_len_2 + 1
        print(f'key_2:')
        for i in range(len(matrix_2)):
            if i == 0:
                print('/', end='')
            elif i == len(matrix_2) - 1:
                print('\\', end='')
            else:
                print('|', end='')

            for j in range(len(matrix_2[i])):
                spacing = ' ' * (tab - len(str(matrix_2[i][j]))) if j != len(matrix_2[i]) - 1 else ''
                print(matrix_2[i][j], end=spacing)

            if i == 0:
                print('\\')
            elif i == len(matrix_2) - 1:
                print('/')
            else:
                print('|')
        print()
