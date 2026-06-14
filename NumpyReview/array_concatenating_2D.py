"""
M. Pogash 2026-06-05

numpy 101
"""

# == IMPORT LIBRARIES ====================
import numpy as np
from print_np_array_stats import print_np_array_stats
from print_np_array_stats_short import print_np_array_stats_short

# == CREATE ARRAY ===========================
arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# == CONCATENATE 1D ARRAYS ==================
arr4 = np.concatenate((arr2,arr2))
print_np_array_stats_short(arr4,"np.concatenate((arr2,arr2))")

arr4 = np.concatenate((arr2,arr2),axis=0)
print_np_array_stats_short(arr4,"np.concatenate((arr2,arr2),axis=0)")

arr4 = np.concatenate((arr2,arr2),axis=1)
print_np_array_stats_short(arr4,"arr4 = np.concatenate((arr2,arr2),axis=1)")

# horizontal stack
arr4 = np.hstack((arr2,arr2))
print_np_array_stats_short(arr4,"np.hstack((arr2,arr2))")

# vertical stack
arr4 = np.vstack((arr2,arr2))
print_np_array_stats_short(arr4,"np.vstack((arr4,arr4))")

# row stack
arr4 = np.r_[arr2,arr2]
print_np_array_stats_short(arr4,"np.r_[arr1,arr1]")

# column stack
arr4 = np.column_stack((arr2,arr2))
print_np_array_stats_short(arr4,"np.column_stack((arr2,arr2))")

# column stack
arr4 = np.c_[arr2,arr2]
print_np_array_stats_short(arr4,"np.c_[arr2,arr2]")


