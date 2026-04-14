import threading
import queue
import time

#create a shared queue
q = queue.Queue()
def producer():
    for i in range(5):
        print(f"Producer: Created item {i}")
        q.put(i) #put item in box
        time.sleep(0.5)
def consumer():
    while True:
        item =q.get() #take item out (waits if box is empty)
        if item is None: break
        print(f"Consumer: Processed item {item}")
        q.task_done()
#start the threads
p = threading.Thread(target=producer)
c = threading.Thread(target=consumer, daemon=True) #Daemon stops when main ends

p.start()
c.start()
p.join()  #wait for the producer to finish
