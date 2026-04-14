import threading
import time
def task():
    time.sleep(2)
    print("Child thread finished!")
# t =threading.Thread(target=task)
# t.start()
# print("Main program dinished")

t= threading.Thread(target=task)
t.start()
t.join()
print("Main Program Finished!")