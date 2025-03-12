from benchmarks.profiler import profile_function
from benchmarks.time import time_function
from random import randint

def main():
    @time_function(repetitions=10)
    @profile_function(profile_type="unoptimized")
    def inefficient_matrix_multiplication(A, B):
        n = len(A)  
        C = [[0] * n for _ in range(n)]  
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]
        return C
    
    size = 50
    min_val = 1
    max_val = 10
    A = [[randint(min_val, max_val) for _ in range(size)] for _ in range(size)]
    B = [[randint(min_val, max_val) for _ in range(size)] for _ in range(size)]

    inefficient_matrix_multiplication(A, B)

if __name__ == "__main__":
    main()
