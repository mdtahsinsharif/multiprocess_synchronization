import time
from multiprocessing import Process, Value, Lock
import thread1_

def thread1(val, lock):
    val.value = 0
    with lock:
        print("Before while in t1")
    while val.value==0:
        #with lock:
        with lock:
            print("running t1")
        time.sleep(1)
    with lock:
        print("reached end of t1 function")

def thread2(val, lock):
    #time.sleep(5)
    t = 0
    while True:
        if(t>10):
            
            time.sleep(1)
            if val.value == 0:
                with lock:
                    print("Setting val.value")
                val.value = 1
        with lock:
            print("running t2")
        time.sleep(1)
        t = t+1
#    for i in range(50):
#        time.sleep(0.01)
#        with lock:
#            val.value += 1

if __name__ == '__main__':
    v = Value('i', 0)
    lock = Lock()
    procs = [Process(target=thread2, args=(v,lock))]
    procs[0].start()
    procs.append(Process(target=thread1_.thread1_, args=(v,)))
    procs[1].start()

    #for p in procs: p.start()
    #for p in procs: p.join()

    
