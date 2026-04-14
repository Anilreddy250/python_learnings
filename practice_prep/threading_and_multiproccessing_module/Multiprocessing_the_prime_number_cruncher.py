import time
from concurrent.futures import ProcessPoolExecutor

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10**8 + 7, 10**8 + 9, 10**8 + 37, 10**8 + 39] * 2

if __name__ == "__main__":
    # 1. Sequential (Slow)
    start = time.perf_counter()
    [is_prime(n) for n in numbers]
    print(f"Sequential took: {time.perf_counter() - start}s")

    # 2. Multiprocessing (Fast)
    start = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        list(executor.map(is_prime, numbers))
    print(f"Multiprocessing took: {time.perf_counter() - start}s")