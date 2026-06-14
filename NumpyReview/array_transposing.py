"""
M. Pogash 2026-06-05

numpy 101
"""

# == IMPORT LIBS= =======================
import numpy as np
from print_np_array_stats import print_np_array_stats

# == ARRAY CREATION ====================
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# == ARRAY TRANSPOSING =================
# Transpose the 1D array
arr1_transpose = arr1.T
print_np_array_stats(arr1_transpose,"arr1_transpose")

# Transpose the 2D array
arr2_transpose = arr2.T
print_np_array_stats(arr2_transpose,"arr2_transpose")

# Transpose the 1D array correctly with 3 methods
arr1_transpose_m1 = arr1[:,np.newaxis]
print_np_array_stats(arr1_transpose_m1,"arr1_transpose_m1")

arr1_transpose_m2 = arr1[np.newaxis,:].T
print_np_array_stats(arr1_transpose_m2,"arr1_transpose_m2")

arr1_transpose_m3 = arr1.reshape(-1,1)
print_np_array_stats(arr1_transpose_m3,"arr1_transpose_m3")
