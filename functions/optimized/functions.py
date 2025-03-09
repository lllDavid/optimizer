# Optimized functions
from benchmarks.profiler import profile_function
from benchmarks.time import time_function

# 1
@time_function(repetitions=10)
@profile_function
def inefficient_duplicates_check(data):
    pass


# 2
@time_function(repetitions=10)
@profile_function
def inefficient_matrix_multiplication(A, B):
    pass

# 3
@time_function(repetitions=10)
@profile_function
def inefficient_sorting_repeatedly(n):
    pass

