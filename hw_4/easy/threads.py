from concurrent.futures import ThreadPoolExecutor
from lineal import sum_fib


def run_fib_threads(n: int):
    executor = ThreadPoolExecutor(max_workers=10)
    res = list(executor.map(sum_fib, [n] * 10))
    executor.shutdown()
    return res
