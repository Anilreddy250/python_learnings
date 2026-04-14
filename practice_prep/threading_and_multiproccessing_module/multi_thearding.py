import time

# start = time.perf_counter()
start = time.time()

def do_something():
    print('sleeping 1 second....')
    time.sleep(5)
    print("Done sleeping")
do_something()
finish = time.time()

print(f" Finisher in {finish-start} seconds")

current_time = time.time("dd/mm/yyyy")
print(current_time)