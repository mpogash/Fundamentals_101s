"""
M. Pogash 2026-06-05

numpy 101
"""

# == IMPORT LIBRARIES ====================
import numpy as np
from print_np_array_stats import print_np_array_stats

## == MAKE A VIEW ======================
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr3 = arr1.view()
arr3[0] = 10
print(f"arr3 = arr1.view; arr3[0] = 10; arr1 = \n {arr1}")
del arr3

## == MAKE A COPY ======================
# copy duplicates the array and numerical data. If the 
# data is an python object array (list, dict, custom objects) 
# instead of raw numbers, than a pointer is made. This results 
# a shallow copy or the python objects
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr3 = np.copy(arr1)
arr3[0] = 10
print(f"arr3 = arr1.copy; arr3[0] = 10; arr1 = \n {arr1}")
del arr3

## == MAKE A DEEP COPY ======================
# deep copy duplicates the array, the references, and all
# the nested contents
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr3 = arr1.copy()
arr3[0] = 10
print(f"arr3 = arr1.copy; arr3[0] = 10; arr1 = \n {arr1}")
del arr3

## == MAKE A COPY ======================
# copy duplicates the array and numerical data. If the 
# data is an python object array (list, dict, custom objects) 
# instead of raw numbers, than a pointer is made. This results 
# a shallow copy or the python objects
arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
arr4 = np.copy(arr2)
arr4[0,0] = 10
print(f"arr4 = arr2.copy; arr4[0,0] = 10; arr2 = \n {arr2}")
del arr4

# This works b/c direct indexing breaks the pointer
arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]],dtype=object)
arr4 = np.copy(arr2)
arr4[0,0] = 10
print(f"arr4 = arr2.copy; arr4[0,0] = 10; arr2 = \n {arr2}")
del arr4

# This works b/c direct indexing breaks the pointer
# append breaks here b/c numpy thinks arr4[0] is [1, 2, 3]. 
# so, append does not make sense
#arr2 = np.array([[1, 2, 3],
#                [4, 5, 6],
#                [7, 8, 9]],dtype=object)
#arr4 = np.copy(arr2)
#arr4[0,0].append(10)
#print(f"arr4 = arr2.copy; arr4[0,0] = 10; arr2 = \n {arr2}")
#del arr4
