from multiprocessing import Pool
from lineal import sum_fib


def run_fib_process(n: int):
    with Pool(processes=10) as pool:
        res = []
        for i in pool.imap_unordered(sum_fib, [n]*10):
            res.append(i)
        return res
