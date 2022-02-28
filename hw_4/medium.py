import logging
import math
import multiprocessing as mp
import os
import time
from threading import Thread, Lock

logger = mp.log_to_stderr(logging.INFO)
logger.root = r'C:\Users\Sanya\PycharmProjects\HomeWork\hw_4\artifacts\medium\medlogs.log'


def integrate(f, a, b, *, n_jobs=1, n_iter=1000):
    manager = mp.Manager()
    acc = manager.Value('i', 0)
    lock = manager.Lock()
    logerlock = manager.RLock()
    step = (b - a) / n_iter
    with mp.Pool(n_jobs) as pool:
        for i in range(n_iter):
            pool.apply(count, [i, lock, acc, f, step, a, logerlock])
        # acc += f(a + i * step) * step
    return acc


def count(i, lock, acc, f, step, a, logerlock: Lock):
    logger.info(f'New task in process {os.getpid()}')
    res = f(a + i * step) * step
    lock.acquire()
    acc.set(acc.get() + res)
    lock.release()
    logger.info(f'Task in process {os.getpid()} complete')


def write_in_file(res, lock: Lock):
    lock.acquire()
    with open(r'C:\Users\Sanya\PycharmProjects\HomeWork\hw_4\artifacts\medium\times.txt', 'a') as f:
        f.write(f'{res} -- {i} задействованных процессов\n')
    lock.release()


if __name__ == '__main__':
    with open(r'C:\Users\Sanya\PycharmProjects\HomeWork\hw_4\artifacts\medium\times.txt', 'w') as f:
        pass
    for i in range(1, 17):
        logger.info(f'Start new iteration with {i} process')
        start = time.time()
        gral = integrate(math.cos, 0, math.pi / 2, n_jobs=i)
        res = time.time() - start
        filelock = Lock()
        Thread(target=write_in_file, args=(res, filelock)).start()
        logger.info(f'Finished iteration with {i} process')
