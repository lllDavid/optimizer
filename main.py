from functions.functions import find_large_primes
from benchmarks import time
from benchmarks import cprofile

time.time_benchmark(find_large_primes, 10, 100)
cprofile.run_profiling()