# coding:utf-8
# Author: yuwhuawang

import os
import multiprocessing
import time


# exchanging objects between processes
# Queue is process safe
def q_put(q):
    time.sleep(3)
    q.put(['I am sub process :{}'.format(os.getpid())])
    q.put(['I am sub process :{}'.format(os.getpid())], timeout=1)


def q_get(q):
    print q.get(timeout=4)  # q.get(block=False, timeout=3)  # will block if block set True


def q_process():
    q = multiprocessing.Queue(1)  # Queues are thread and process safe.
    p_put = multiprocessing.Process(target=q_put, args=(q, ))
    p_get = multiprocessing.Process(target=q_get, args=(q, ))

    p_get.start()
    p_put.start()


if __name__ == '__main__':
    q_process()
