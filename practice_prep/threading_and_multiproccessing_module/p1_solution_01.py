import threading

NUM_ITER = 100
counter = 0
sum_ = 0

def do_work():
    global counter
    global sum_

    counter = counter +1
    next_sum = sum_ + counter
    print (f"{sum_} + {counter} = {next_sum}")
    sum_ = next_sum

if __name__ == "__main__":
    threads =[]
    for l in range(NUM_ITER):
        threads.append(threading.Thread(target=do_work))
    for thread in threads:
        thread.start()
    # print("DONE")
    for thread in threads:
        thread.join()
    print("Done")
