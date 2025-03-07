# Functions to optimize
from benchmarks.cprofile import profile_function
from benchmarks.time import time_function

# 1
@time_function(repetitions=10)
@profile_function
def inefficient_duplicates_check(arr):
    """
    Check if a list has duplicates by using a list to track already-seen elements.
    This is inefficient because checking membership in a list takes O(n) time.
    """
    seen = []  
    
    for num in arr:
        if num in seen:  
            return True
        seen.append(num)  
    
    return False


# 2
@time_function(repetitions=10)
@profile_function
def inefficient_matrix_multiplication(A, B):
    """
    Perform matrix multiplication using nested loops (inefficient).
    This method is inefficient because it uses three nested loops, resulting in a time complexity of O(n^3).
    """
    n = len(A)  
    C = [[0] * n for _ in range(n)]  

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

# 3
@time_function(repetitions=10)
@profile_function
def inefficient_sorting_repeatedly(n):
    """
    Generate a list of `n` random numbers and sort it repeatedly.
    This function uses bubble sort for sorting, which is inefficient.
    """
    import random

    def bubble_sort(arr):
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    numbers = [random.randint(1, 1000) for _ in range(n)]
    
    for _ in range(100):  
        bubble_sort(numbers)
    
    return numbers

