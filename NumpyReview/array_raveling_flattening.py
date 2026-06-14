"""
M. Pogash 2026-06-05

numpy 101
"""

# == IMPORT LIBRARIES ====================
import numpy as np
from print_np_array_stats import print_np_array_stats

# == ARRAY CREATION ====================
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])


# == RAVELING & FLATTENING ARRAYS =======================
# create 1D array by raveling the 2D array
arr2_ravel = arr2.ravel()
print_np_array_stats(arr2_ravel,"arr2_ravel")

# create 1D array by flattening the 2D array
arr2_flatten = arr2.flatten()
print_np_array_stats(arr2_flatten,"arr2_flatten")

# create 1D array by raveling the 2D array and transposing it
arr2_ravel_transpose = arr2.ravel().T
print_np_array_stats(arr2_ravel_transpose,"arr2_ravel_transpose")

# create 1D array by transposing the 2D array and then raveling it
arr2_transpose_ravel = arr2.T.ravel()
print_np_array_stats(arr2_transpose_ravel,"arr2_transpose_ravel")

# Ravel creates a view (pointer), flatten creates a deep copy
arr2_ravel[0] = 10
print(f"arr2_ravel[0] = 10; arr2 = {arr2}\n")

arr2_flatten[1] = 20
print(f"arr2_flatten[1] = 20; arr2 = {arr2}\n")

arr2_ravel[2] = 30
print(f"arr2_ravel[2] = 30; arr2 = {arr2}\n")



