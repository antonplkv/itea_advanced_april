import time
from threading import Thread, enumerate
from multiprocessing import Process



#
#
# t = Thread(target=do_nothing, args=(5, ))
#
#
# print('Hello')
# t.start()
# print('World')


# def cpu_burn():
#     a = []
#     for i in range(15_000_000):
#         a.append(i)
#
#
#
# import time
#
# start_time = time.time()
#
# for i in range(3):
#     t = Process(target=cpu_burn)
#     t.start()
#
#
# print(time.time() - start_time)

def do_nothing(sec):
    print(f'I am going to sleep for {sec} seconds')
    time.sleep(sec)
    print('Wake up')


thread_list = []


for i in range(5):
    t = Thread(target=do_nothing, args=(4, ), daemon=True)
    thread_list.append(t)
    t.start()


while True:
    for thread in thread_list:
        print(thread.getName(), thread.is_alive())
    time.sleep(2)