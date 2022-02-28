from time import time
from threads import run_fib_threads
from multiproc import run_fib_process
from lineal import run_fib_lineal


if __name__ == '__main__':
    with open(r'C:\Users\Sanya\PycharmProjects\HomeWork\hw_4\artifacts\easy.txt', 'w') as f:
        n = 10000**10000
        startlin = time()
        run_fib_lineal(n)
        f.write(f'Время линейного исполнения:{str(time() - startlin)}\n')
        startthread = time()
        run_fib_lineal(n)
        f.write(f'Время потокового исполнения:{str(time() - startthread)}\n')
        startproc = time()
        run_fib_process(n)
        f.write(f'Время мультипроцессингово исполнения:{str(time() - startproc)}\n')
