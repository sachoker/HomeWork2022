import numpy as np


class Matrix:
    def __init__(self, matrix):
        if type(matrix) == np.ndarray or type(matrix) == np.array:
            for i in matrix:
                self.value.append(list(i))
        elif type(matrix) == list:
            self.value = matrix
        elif type(matrix) == self.__class__:
            self.value = matrix.value
        else:
            raise TypeError("Неверный тип массива")
        self._columns = len(self.value[0])
        self._rows = len(self.value)

    @property
    def value(self):
        try:
            return self._value
        except AttributeError:
            self._value = []
            return self._value

    @value.setter
    def value(self, matrix: np.array):
        for i in matrix:
            self._value.append(list(i))

    @value.setter
    def value(self, matrix: list):
        self._value = matrix

    @property
    def columns(self):
        return self._columns

    @property
    def rows(self):
        return self.columns

    def __and__(self, right):
        """matmul realisation"""
        right = Matrix(right)
        if self.rows == right.columns:
            res = []
            right = right.traspon()
            for i in range(self.rows):
                res.append([])
                for j in range(self.rows):
                    res[i].append(0)
                    for k in range(self.rows):
                        res[i][j] += self[i][k] * right[k][j]
            return Matrix(res)
        else:
            raise ValueError("Неверная размерность")

    def __add__(self, other):
        other = Matrix(other)
        if ln(self.value) != ln(other):
            raise ValueError("Неверная размерность")
        res = []
        for i, a in enumerate(self):
            res.append([])
            for j, b in enumerate(a):
                res[i].append(self[i][j] + b)
        return res

    def __mul__(self, other):
        res = []
        if type(other) == self.__class__:
            if self.rows == other.rows and self.columns == other.columns:
                for i, a in enumerate(self):
                    res.append([])
                    for j, b in enumerate(a):
                        res[i].append(b * other[i][j])
            return Matrix(res)
        elif type(other) == int:
            for i in self:
                res.append([other * j for j in i])
            return res
        else:
            raise TypeError("Неверный тип данных")

    def __iter__(self):
        return iter(self.value)

    def __getitem__(self, item):
        return self.value[item]

    def __setitem__(self, key, value):
        self.value[key] = value

    def traspon(self):
        res = []
        for i in range(self.columns):
            res.append([])
            for j in range(self.rows):
                res[i].append(self[j][i])
        return Matrix(res)


def ln(arr):
    row = 0
    col = 0
    for i in arr:
        row += 1
        try:
            for j in i:
                col += 1
        except:
            pass
    return row, col


np.random.seed(0)
a, b = np.random.randint(0, 10, (10, 10)), np.random.randint(0, 10, (10, 10))
add = open('artifacts/easy/matrix+', 'w')
mmul = open('artifacts/easy/matmul', 'w')
cmul = open('artifacts/easy/componentmul', 'w')
add.write(str(a + b))
mmul.write(str(a & b))
cmul.write(str(a * b))
