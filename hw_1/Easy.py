n = int(input())
for i in range(1, n + 1):
    print(int((((1 + 5 ** (1 / 2)) / 2) ** i - ((1 - 5 ** (1 / 2)) / 2) ** i) / (5 ** (1 / 2))))

