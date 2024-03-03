import math

from AlphabetConfig import *
from Matrix2x2 import Matrix2x2
from IntMod import IntMod

for a in range(0, m):
    for b in range(0, m):
        for c in range(0, m):
            for d in range(0, m):
                K = Matrix2x2([[IntMod(a), IntMod(b)],
                               [IntMod(c), IntMod(d)]])
                if K.calculate_det() != 0:
                    # первая проверка на соответствие шифртексту (первый блок символов)
                    x1 = Matrix2x2([[IntMod(4)],
                                   [IntMod(36)]])
                    y1 = K * x1
                    if y1.matrix[0][0].getValue() == 35 and y1.matrix[1][0].getValue() == 8:
                        # вторая проверка на соответствие шифртексту (второй блок символов)
                        x2 = Matrix2x2([[IntMod(36)],
                                        [IntMod(19)]])
                        y2 = K * x2
                        if y2.matrix[0][0].getValue() == 48 and y2.matrix[1][0].getValue() == 17:
                            print([[a, b], [c, d]])

