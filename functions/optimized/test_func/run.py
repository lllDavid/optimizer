
from functions.optimized.test_func.optimized_test_func import test_func
from benchmarks.time import time_function
from benchmarks.profiler import profile_function
from random import randint

@time_function(repetitions=10)
# TODO: find way to profile the actual some_func lines not the wrapper
@profile_function(profile_type="optimized")
def decorated_test_func(*args, **kwargs):
    return test_func(*args, **kwargs)

def main():
    size = 50
    min_val = 1
    max_val = 10
    A = [[randint(min_val, max_val) for _ in range(size)] for _ in range(size)]
    B = [[randint(min_val, max_val) for _ in range(size)] for _ in range(size)]

    decorated_test_func(A, B)

if __name__ == "__main__":
    main()
