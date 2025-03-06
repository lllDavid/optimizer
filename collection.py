##
from numpy import sort, random

# 1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_large_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# 2
def large_matrix_multiply(A, B):
    N = len(A)
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# 3
from itertools import permutations
data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
result = list(permutations(data))  

# 4
large_data = random.randint(0, 1000000, 10000000)
sorted_data = sort(large_data)  



