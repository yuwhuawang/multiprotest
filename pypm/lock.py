# coding:utf-8
# Author: yuwhuawang

import os
import multiprocessing
import time


def worker(lock, f):
	fs = open(f, 'a+')
	for i in range(10):
	fs = open(f, 'a+')
	time.sleep(0.5)
    	fs.write("Lock acquired by {}\n".format(os.getpid()))
    	fs.close()

def lock_process():
    lock = multiprocessing.Lock()
    f = "./file.txt"
    w1 = multiprocessing.Process(target=worker, args=(lock, f))
    w2 = multiprocessing.Process(target=worker, args=(lock, f))
    w1.start()
    w2.start()
    print "end"


if __name__ == '__main__':
    lock_process()
