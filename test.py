from time import perf_counter
from statistics import mean
from functions import find_large_primes

def time_benchmark(func, repetitions, *args, **kwargs):
    results = []
    for _ in range(repetitions):
        start = perf_counter()
        func(*args,**kwargs)
        end = perf_counter()
        _time = end - start
        results.append(_time)
    print(f"Avg. execution time: {mean(results):.16f} seconds")


time_benchmark(find_large_primes, 10, 100)