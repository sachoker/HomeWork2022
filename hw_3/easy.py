import numpy as np


class BeatifullMixin:
    def __repr__(self):
        res = list(map(list, self.value))
        return '\n'.join(map(str, res))

    def __str__(self):
        res = '\n'.join(map(str, list(map(list, self.value))))
        return res


class ValuePropertyMixin:
    @property
    def value(self):
        try:
            return list(map(list, self._value))
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


class Matrix(ValuePropertyMixin, BeatifullMixin):
    def __init__(self, matrix):
        self._value = []
        if type(matrix) == np.ndarray or type(matrix) == np.array:
            for i in matrix:
                self._value.append(list(i))
        elif type(matrix) == list:
            self._value = matrix
        elif type(matrix) == self.__class__ or type(Matrix) == super:
            self._value = matrix.value
        else:
            raise TypeError("Неверный тип массива")
        self._columns = len(self.value[0])
        self._rows = len(self.value)

    @property
    def columns(self):
        return self._columns

    @property
    def rows(self):
        return self.columns

    def __and__(self, right):
        """matmul realisation"""
        right = self.__class__(right)
        if self.rows == right.columns:
            res = []
            right = right.traspon()
            for i in range(self.rows):
                res.append([])
                for j in range(self.rows):
                    res[i].append(0)
                    for k in range(self.rows):
                        res[i][j] += self[i][k] * right[k][j]
            return self.__class__(res)
        else:
            raise ValueError("Неверная размерность")

    def __add__(self, other):
        other = self.__class__(other)
        if self.ln(self.value) != self.ln(other):
            raise ValueError("Неверная размерность")
        res = []
        for i, a in enumerate(self):
            res.append([])
            for j, b in enumerate(a):
                res[i].append(self[i][j] + b)
        return self.___class__(res)

    def __mul__(self, other):
        res = []
        if type(other) == self.__class__:
            if self.rows == other.rows and self.columns == other.columns:
                for i, a in enumerate(self):
                    res.append([])
                    for j, b in enumerate(a):
                        res[i].append(b * other[i][j])
            return self.__class__(res)
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
        return self.__class__(res)

    @staticmethod
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


def check_work(Class, path_to_save):
    np.random.seed(0)
    a, b = Class(np.random.randint(0, 10, (10, 10))), Class(np.random.randint(0, 10, (10, 10)))
    add = open(path_to_save + '/matrix+', 'w')
    mmul = open(path_to_save + '/matmul', 'w')
    cmul = open(path_to_save + '/componentmul', 'w')
    add.write(str(a + b))
    mmul.write(str(a & b))
    cmul.write(str(a * b))


if __name__ == '__main__':
    check_work(Matrix, 'artifacts/easy')
