# coding:utf-8
# Author: yuwhuawang

import os
import multiprocessing
import time


# raw subprocess
def raw_process():
    pid = os.fork()
    if pid == 0:
        print ("I am a child process:{} created by process:{}.".format(os.getpid(),
                                                                       os.getppid()))
    else:
        print ("I am main process:{}, I just created a child process:{}.".format(os.getpid(),
                                                                                 pid))


def worker(i, s):
    print "worker_{}".format(i)
    time.sleep(s)
    print "worker_{} end".format(i)


def my_process():
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(i, 1, ), name="worker_{}".format(i))
        p.daemon = True
        p.start()
        p.join()
        print "process {} is alive :{}".format(p.name, p.is_alive())


# class based multiprocess
class MyProcess(multiprocessing.Process):
    def __init__(self, p_name):
        super(MyProcess, self).__init__()
        self.p_name = p_name

    def run(self):
        print ("process id :{}, my name is {}".format(self.pid, self.p_name))


def class_process():
    for i in range(5):
        MyProcess(i).start()


if __name__ == '__main__':

    # raw_process()
    my_process()
    # class_process()
    # https://www.cnblogs.com/kaituorensheng/p/4445418.html
