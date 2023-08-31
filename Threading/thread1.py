import time
import threading

start = time.perf_counter()

def dosomething():
    print('sleep 1 sec..')
    time.sleep(1)
    print('done sleeping...')

t1 = threading.Thread(target=dosomething)
t2 = threading.Thread(target=dosomething)

t1.start()
t2.start()

t1.join()
t2.join()
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')