# coding:utf-8
# Author: yuwhuawang

import os
import multiprocessing
import time


def worker(lock, f):
    lock.acquire()
    try:
        fs = open(f, 'a+')
        n = 10
        while n > 1:
            fs.write("Lock acquired by {}\n".format(os.getpid()))
            n -= 1
        fs.close()
    finally:
        lock.release()


def lock_process():
    lock = multiprocessing.Lock()
    f = "/data/wangyuehua/file.txt"
    w1 = multiprocessing.Process(target=worker, args=(lock, f))
    w2 = multiprocessing.Process(target=worker, args=(lock, f))
    w1.start()
    w2.start()
    print "end"


if __name__ == '__main__':
    lock_process()
