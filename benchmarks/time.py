from time import perf_counter
from statistics import mean

def time_benchmark(func, repetitions, *args, **kwargs):
    results = []
    for _ in range(repetitions):
        start = perf_counter()
        func(*args,**kwargs)
        end = perf_counter()
        _time = end - start
        results.append(_time)
    print(f"Avg. execution time: {mean(results):.16f} seconds")




