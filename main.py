from random import randint

from functions.unoptimized.functions import inefficient_matrix_multiplication as unoptimized
from functions.optimized.functions import inefficient_matrix_multiplication as optimized

from benchmarks.results.analyze import analyze
from benchmarks.results.compare import compare

from benchmarks.profiler import get_mean_profile_times

n = 2 
min_val = 1
max_val = 10

matrix_a = [[randint(min_val, max_val) for _ in range(n)] for _ in range(n)]
matrix_b = [[randint(min_val, max_val) for _ in range(n)] for _ in range(n)]

print("\n--- Running 'unoptimized' version of matrix multiplication ---")
unoptimized(matrix_a, matrix_b)
print("\nProfiling results for 'unoptimized' version:")
get_mean_profile_times()
print("\nAnalysis of 'unoptimized' version:")
analyze()

print("\n--- Running 'optimized' version of matrix multiplication ---")
optimized(matrix_a, matrix_b)
print("\nAnalysis of 'optimized' version:")
analyze()

file_name = input("\nEnter the benchmark file name to compare results: ").strip()
print(f"\n--- Comparing results using file: {file_name} ---")
compare(file_name)
