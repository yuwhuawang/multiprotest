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
    pool = multiprocessing.Pool(processes=4)
    print [i for i in pool.map(f, range(10))]
    print ('used {}...'.format(time.time()-start))


def pool_result():
    res = list()
    pool = multiprocessing.Pool(processes=4)
    for i in range(4):
        res.append(pool.apply_async(f, (i,)))
    pool.close()
    pool.join()
    for i in res:
        print i.get(timeout=1)


if __name__ == '__main__':
    pool_simple()
    # pool_result()
