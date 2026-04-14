import threading
import requests
from concurrent.futures import ThreadPoolExecutor
import time

urls = ["https://www.google.com", "https://www.python.org", "https://www.github.com"] * 5

def fetch_url(url):
    response = requests.get(url)
    return f"{url} retruned {response.status_code}"
#execution
start = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch_url, urls))
end = time.perf_counter()
print("\n".join(results[:3])) #print first 3 results
print(f"Threading took:{end - start:.2f} seconds")