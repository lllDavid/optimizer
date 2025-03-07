from random import randint

from functions.functions import inefficient_duplicates_check
from functions.functions import inefficient_sorting_repeatedly
from functions.functions import inefficient_matrix_multiplication

inefficient_duplicates_check([randint(1, 10) for _ in range(1000)])

# inefficient_sorting_repeatedly(1000)

'''
'n = 2 
min_val = 1
max_val = 10
inefficient_matrix_multiplication([[randint(min_val, max_val) for _ in range(n)] for _ in range(n)], [[randint(min_val, max_val) for _ in range(n)] for _ in range(n)])'
'''


