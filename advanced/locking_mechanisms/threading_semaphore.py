import threading
import time

sem = threading.Semaphore(3)

def do_work(thread_name):
    with sem:
        print(thread_name, " is currently working")
        time.sleep(2)
        
threads = []

for i in range(6):
    t = threading.Thread(target=do_work, args=(f"Thread-{i}",))
    t.start()
    threads.append(t)
    
    
for thread in threads:
    thread.join()