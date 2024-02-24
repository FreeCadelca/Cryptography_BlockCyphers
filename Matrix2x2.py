from IntMod import IntMod


class Matrix2x2:
    def __init__(self, matrix_values):
        self.matrix = matrix_values

    def __mul__(self, other):
        result = [[IntMod(0) for _ in range(2)] for _ in range(2)]
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix2x2(result)

    def calculate_det(self):
        return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

    def inv(self):
        det = self.calculate_det()
        if det.getValue == 0:
            return "Matrix is singular and cannot be inverted"
        return Matrix2x2([[self.matrix[1][1] // det, IntMod(-1) * self.matrix[0][1] // det],
                          [IntMod(-1) * self.matrix[1][0] // det, self.matrix[0][0] // det]])


key2 = Matrix2x2([[IntMod(1), IntMod(4)],
                  [IntMod(2), IntMod(9)]]).inv()
print([[int(j) for j in i] for i in key2.matrix])

