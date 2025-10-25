import multiprocessing
import time

def heavy_computation(x):
    # Make each computation heavy by looping
    s = 0
    for i in range(10_000):
        s += (x + i)**6
    return s

def main():
    N = 8_000  # total tasks
    numbers = list(range(N))

    print("CPU cores:", multiprocessing.cpu_count())

    # --- Single-core ---
    start = time.time()
    result = sum(heavy_computation(x) for x in numbers)
    end = time.time()
    print("Single-core result:", result)
    print("Single-core calculation took:", (end - start)*1000, "ms")

    # --- Multi-core ---
    start = time.time()
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        results = pool.map(heavy_computation, numbers)
    total_parallel = sum(results)
    end = time.time()
    print("Multi-core result:", total_parallel)
    print("Multi-core calculation took:", (end - start)*1000, "ms")

if __name__ == '__main__':
    main()
