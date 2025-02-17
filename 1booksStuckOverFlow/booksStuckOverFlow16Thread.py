# Многопоточность
import threading
from threading import Thread
import requests
from queue import Queue
def foo():
    print("Hello threading")

my_thread = threading.Thread(target=foo)
my_thread.start()


# q = Queue(maxsize=20)
# def put_page(page_num):
#     q.put(requests.get("https://gordeevopark.ru", page_num))
#
# def compile(q):
#     if not q.full:
#         raise ValueError
#     else:
#         print("Done compiling")
#
# threads = []
#
# for page_num in range(20):
#     t = Thread(target=requests.get, args=(page_num,))
#     t.start()
#     threads.append(t)
#     t.join()
#     compile(q)

