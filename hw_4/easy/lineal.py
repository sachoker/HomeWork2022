def sum_fib(n):
    c = 1
    p = 0
    s = 0
    while (c < n):
        s += c
        c, p = c + p, c
    return s


def run_fib_lineal(n):
    res = []
    for i in range(10):
        res.append(sum_fib(n))
    return res
