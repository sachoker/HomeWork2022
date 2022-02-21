from easy import Matrix


class HashMixin:
    def __hash__(self):
        res = 0
        for i, a in enumerate(self.value):
            res += (sum(a) + i) * 12345
        res = bin(res)[2:]
        out = 0
        for i in range(6, len(res) - 2, 6):
            out += int(res[i - 6:i + 2])
        return out


class HashMatrix(Matrix, HashMixin):
    def __init__(self, matrix):
        self.mulcash = {}
        super(HashMatrix, self).__init__(matrix)

    def __and__(self, right):
        right = HashMatrix(right)
        if self.rows == right.columns:
            res = []
            right = right.traspon()
            for i in range(self.rows):
                res.append([])
                for j in range(self.rows):
                    res[i].append(0)
                    for k in range(self.rows):
                        res[i][j] += self[i][k] * right[k][j]
            res = HashMatrix(res)
            self.mulcash[(hash(self), hash(right.traspon()))] = hash(res)
            return res
        else:
            raise ValueError("Неверная размерность")


if __name__ == '__main__':
    A = HashMatrix([[2, 2], [2, 1]])
    B = HashMatrix([[10, 2], [21, 0]])
    C = HashMatrix([[2, 0], [0, 1]])
    D = HashMatrix([[10, 2], [21, 0]])
    for i in (('A', A), ('B', B), ('C', C), ('D', D)):
        with open(f'artifacts/hard/{i[0]}.txt', 'w+') as f:
            f.write(str(i[1]))
    with open('artifacts/hard/AB.txt', 'w+') as f:
        f.write(str(A & B))
    with open('artifacts/hard/CD.txt', 'w+') as f:
        f.write(str(C & D))
    with open('artifacts/hard/hash.txt', 'w+') as f:
        f.write(str(hash(A & B)) + '\n' + str(hash(C & D)))
