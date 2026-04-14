#you have list of 5 filename. each file takes 1 second to "download", write a program
# using threading so that the total execution time is ~1 second instead of 5 seconds.
import threading
import time

def download_File(filename):
    print(f"Downloding {filename}...")
    time.sleep(1)
    print(f"Finished {filename}")
files = ["img1.jpg", "img2.jpg","img3.jpg", "img4.jpg","img5.jpg"]
threads = []
start_time =time.perf_counter()

for f in files:
    t = threading.Thread(target=download_File, args=(f,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()

print(f"Total time: {time.perf_counter() - start_time:.2f} seconds")
