from random import randint

from functions.before.functions import inefficient_matrix_multiplication

from benchmarks.results.analyze import analyze
from benchmarks.results.compare import compare

n = 2 
min_val = 1
max_val = 10
inefficient_matrix_multiplication([[randint(min_val, max_val) for _ in range(n)] for _ in range(n)], [[randint(min_val, max_val) for _ in range(n)] for _ in range(n)])

analyze()

file_name = input("Benchmarks to compare:")
compare(file_name)
