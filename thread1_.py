import time
def thread1_(val):
    val.value = 0
    print("Before while in t1")
    while val.value==0:
        #with lock:
        print("running t1")
        time.sleep(1)
    print("reached end of t1 function")