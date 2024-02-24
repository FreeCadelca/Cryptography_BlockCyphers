from IntMod import IntMod


class Matrix3x3:
    def __init__(self, matrix_values):
        self.matrix = matrix_values

    def __mul__(self, other):
        result = [[IntMod(0) for _ in range(3)] for _ in range(3)]

        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return Matrix3x3(result)

    def calculate_det(self):
        return self.matrix[0][0] * (self.matrix[1][1] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][1]) - \
            self.matrix[0][1] * (self.matrix[1][0] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][0]) + \
            self.matrix[0][2] * (self.matrix[1][0] * self.matrix[2][1] - self.matrix[1][1] * self.matrix[2][0])

    def inv(self):
        det = self.calculate_det()

        if det.getValue == 0:
            return "Matrix is singular and cannot be inverted"

        inv_det = IntMod(1) // det
        result = [[IntMod(0) for _ in range(3)] for _ in range(3)]

        result[0][0] = (self.matrix[1][1] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][1]) * inv_det
        result[0][1] = (self.matrix[0][2] * self.matrix[2][1] - self.matrix[0][1] * self.matrix[2][2]) * inv_det
        result[0][2] = (self.matrix[0][1] * self.matrix[1][2] - self.matrix[0][2] * self.matrix[1][1]) * inv_det
        result[1][0] = (self.matrix[1][2] * self.matrix[2][0] - self.matrix[1][0] * self.matrix[2][2]) * inv_det
        result[1][1] = (self.matrix[0][0] * self.matrix[2][2] - self.matrix[0][2] * self.matrix[2][0]) * inv_det
        result[1][2] = (self.matrix[0][2] * self.matrix[1][0] - self.matrix[0][0] * self.matrix[1][2]) * inv_det
        result[2][0] = (self.matrix[1][0] * self.matrix[2][1] - self.matrix[1][1] * self.matrix[2][0]) * inv_det
        result[2][1] = (self.matrix[0][1] * self.matrix[2][0] - self.matrix[0][0] * self.matrix[2][1]) * inv_det
        result[2][2] = (self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]) * inv_det

        return Matrix3x3(result)
