import multiprocessing
import time
import random
def producer(queue):
    for _ in range(5):
        item = random.randint(1, 100)
        queue.put(item)
        print(f"Produced: {item}")
        time.sleep(0.5)
    queue.put(None) #signal to stop
def consumer(queue):
    while True:
        item = queue.get()
        if item is None: break # Exit if signal received
        print(f"Consumed and Squared: {item**2}")
if __name__ == "__main__":
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
