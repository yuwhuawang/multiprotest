# coding:utf-8
# Author: yuwhuawang

import os
import multiprocessing
import time


def f(x):
    time.sleep(2)
    return x*x


def pool_simple():
    start = time.time()
    pool = multiprocessing.Pool(processes=10)
    print [i for i in pool.map(f, range(10))]
    print ('used {}...'.format(time.time()-start))


def pool_result():
    start = time.time()
    res = list()
    pool = multiprocessing.Pool(processes=10)
    for i in range(10):
        res.append(pool.apply_async(f, (i,)))
    pool.close()
    pool.join()
    print [i.get(timeout=1) for i in res]
    print ('used {}...'.format(time.time()-start))

if __name__ == '__main__':
   #  pool_simple()
   pool_result()
