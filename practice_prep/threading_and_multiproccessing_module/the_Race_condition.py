import threading
balance = 0
lock = threading.Lock() #the " key " to the variable
def update_balance():
    global balance
    for _ in range(1000000):
        #only the thread with the lock can enter this bolck
        with lock:
            balance +=1
t1 = threading.Thread(target=update_balance)
t2 = threading.Thread(target=update_balance)

t1.start()
t2.start()
t1.join()
t2.join()
print(f"FInal Balnce: {balance}")