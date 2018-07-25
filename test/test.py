"""
@author: MH
@contact: menghedianmo@163.com
@file: test.py
@time: 2018/7/24 9:53

        线程
"""

import threading

a = 0


def worker():
    thread = threading.current_thread()
    for j in range(0, 10):
        global a
        a += 1
        print(thread.getName() + str(a))


new_t = threading.Thread(target=worker, name='dm')
new_t.start()
new_t2 = threading.Thread(target=worker, name='dm~')
new_t2.start()
