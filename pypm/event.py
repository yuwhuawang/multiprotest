# coding:utf-8
# Author: yuwhuawang

import os
import multiprocessing
import time


def wait_for_event_timeout(e, t):
    print("wait_for_event_timeout,{}:starting".format(multiprocessing.current_process().name))
    e.wait(t)
    print("wait_for_event_timeout,{}:e.is_set->{}".format(multiprocessing.current_process().name,
                                                          e.is_set()))


def event_process():
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name="block",
                                 target=wait_for_event_timeout,
                                 args=(e,5))

    w2 = multiprocessing.Process(name="non-block",
                                 target=wait_for_event_timeout,
                                 args=(e, 2))
    w1.start()
    w2.start()

    time.sleep(3)

    e.set()
    print("main: event is set")


if __name__ == "__main__":
    event_process()