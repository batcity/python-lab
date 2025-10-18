import threading
import time

mutex_lock = threading.Lock()

def do_work(thread_name):
    # non-critical section (runs in parallel)
    print(thread_name, "started working (non-critical section) in parallel")
    mutex_lock.acquire()
    try:
        print(thread_name, " is currently working")
        time.sleep(2)
    finally:
        mutex_lock.release()
        
threads = []

for i in range(6):
    t = threading.Thread(target=do_work, args=(f"Thread-{i}",))
    t.start()
    threads.append(t)
    
    
for thread in threads:
    thread.join()